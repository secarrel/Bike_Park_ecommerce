from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from activities.forms import ReviewForm
from activities.models import Activity, Review
from timeslots.models import Timeslot


def profile(request):
    """Display the user's profile."""

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    # Dictionary to store timeslots and their quantities
    timeslot_quantities = {}

    # Iterate through orders
    for order in orders:
        # Iterate through items in the order
        for item in order.lineitems.all():
            timeslot = item.timeslot
            quantity = item.quantity
            start_time = timeslot.start_time

            # Check timeslot is in the future
            if start_time > timezone.now():

                # Check if the timeslot is already in the dictionary
                if timeslot in timeslot_quantities:
                    # Increment the quantity if the timeslot exists
                    timeslot_quantities[timeslot] += quantity
                else:
                    # Add timeslot to the dictionary with the initial quantity
                    timeslot_quantities[timeslot] = quantity

    # Sort timeslot_quantities by start time
    sorted_timeslot_quantities = dict(
        sorted(
            timeslot_quantities.items(), key=lambda item: item[0].start_time))

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'sorted_timeslot_quantities': sorted_timeslot_quantities,
    }

    return render(request, template, context)


@login_required
def user_details(request):
    """ Display the user's details. """
    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/user_details.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, user_id):
    """ Display the user's order history. """
    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    # Dictionary to store timeslots and their quantities
    timeslot_past = {}
    timeslot_future = {}

    # Iterate through orders
    for order in orders:
        # Iterate through items in the order
        for item in order.lineitems.all():
            timeslot = item.timeslot
            quantity = item.quantity
            start_time = timeslot.start_time

            # Check timeslot is in the future
            if start_time < timezone.now():

                # Check if the timeslot is already in the dictionary
                if timeslot in timeslot_past:
                    # Increment the quantity if the timeslot exists
                    timeslot_past[timeslot] += quantity
                else:
                    # Add timeslot to the dictionary with the initial quantity
                    timeslot_past[timeslot] = quantity

            # Check timeslot is in the future
            if start_time > timezone.now():

                # Check if the timeslot is already in the dictionary
                if timeslot in timeslot_future:
                    # Increment the quantity if the timeslot exists
                    timeslot_future[timeslot] += quantity
                else:
                    # Add timeslot to the dictionary with the initial quantity
                    timeslot_future[timeslot] = quantity

    # Sort timeslot_quantities by start time
    sorted_timeslot_past = dict(
        sorted(
            timeslot_past.items(),
            key=lambda item: item[0].start_time,
            reverse=True))
    sorted_timeslot_future = dict(
        sorted(timeslot_future.items(),
               key=lambda item: item[0].start_time))

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
        'sorted_timeslot_future': sorted_timeslot_future,
        'sorted_timeslot_past': sorted_timeslot_past,
    }

    return render(request, template, context)


@login_required
def order_details(request, order_number):
    """ Display specific order details """
    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, order_number=order_number)
    order_line_item = OrderLineItem.objects.filter(order=order)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_line_item': order_line_item,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_review(request, activity_id):
    """ Add a timeslot to an activity """
    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(
            reverse('order_history', kwargs={'user_id': request.user.id}))

    activity = get_object_or_404(Activity, pk=activity_id)
    user = request.user.id

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.activity = activity
            review.reviewer = request.user
            form.save()
            messages.success(request, 'Successfully added Review!')
            return redirect(
                reverse('order_history',
                        kwargs={'user_id': request.user.id}
                        ))
        else:
            messages.error(
                request,
                'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm(
            initial={'activity': activity, 'reviewer': request.user})

    context = {
        'form': form,
        'activity': activity,
        'user': user
    }

    return render(request, 'profiles/add_review.html', context)


def user_reviews(request):
    """ Edit an activity """
    reviews = Review.objects.filter(reviewer=request.user)

    template = 'profiles/user_reviews.html'
    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete activity """
    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))
    
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review Deleted')
        return redirect(reverse('user_reviews'))
    
    template = 'profiles/delete_review.html'
    context = {
        'review': review,
    }
    return render(request, template, context)


def bookings(request):
    """ Display future bookings """
    orders = Order.objects.all()
    timeslot_list = {}

    # Iterate through orders
    for order in orders:
        # Iterate through items in the order
        for item in order.lineitems.all():
            # Set relevant variables
            timeslot = item.timeslot
            quantity = item.quantity
            capacity = timeslot.available_capacity + timeslot.spaces_booked
            formatted_date = timeslot.start_time.strftime('%d/%m/%Y')
            # Check if the timeslot is already in the dictionary
            if timeslot in timeslot_list:
                # Increase the quantity if the timeslot exists
                timeslot_list[timeslot]['quantity'] += quantity
            else:
                # Add timeslot to the dictionary with the initial quantity
                timeslot_list[timeslot] = {
                    'quantity': quantity,
                    'capacity': capacity,
                    'date': formatted_date,
                    }

    date_filter = request.GET.get('date')
    filtered_timeslots = {}

    if date_filter:
        # Only show bookings on selected date
        date = datetime.strptime(date_filter, '%d/%m/%Y').date()
        for timeslot, info in timeslot_list.items():
            if timeslot.start_time.date() == date:
                filtered_timeslots[timeslot] = info
        timeslot_list = filtered_timeslots
    else:
        # Only show future bookings
        for timeslot, info in timeslot_list.items():
            if timeslot.start_time > timezone.now():
                filtered_timeslots[timeslot] = info
        timeslot_list = filtered_timeslots

    # Sort future bookings to show soonest first
    timeslot_list = dict(
        sorted(timeslot_list.items(),
               key=lambda item: item[0].start_time))

    activities = Activity.objects.all()

    template = 'profiles/bookings.html'
    context = {
        'timeslot_list': timeslot_list,
        'activities': activities,
    }

    return render(request, template, context)


def booking_info(request, timeslot_id):

    timeslot = get_object_or_404(Timeslot, pk=timeslot_id)
    orders = OrderLineItem.objects.filter(timeslot=timeslot)
    template = 'profiles/booking_info.html'
    context = {
        'timeslot': timeslot,
        'orders': orders,
        }
    return render(request, template, context)
