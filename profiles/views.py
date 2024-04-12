from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from activities.forms import ReviewForm
from activities.models import Activity, Review


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

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def add_review(request, activity_id):
    """ Add a timeslot to an activity """
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.activity = activity
            form.save()
            messages.success(request, 'Successfully added Review!')
            return redirect(reverse('order_history', kwargs={'user_id': request.user.id }))
        else:
            messages.error(
                request,
                'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm(initial={'activity': activity}) 

    context = {
        'form': form,
    }

    return render(request, 'profiles/add_review.html', context)


# def edit_review(request, review_id):
#     """ Edit an activity """
#     review = get_object_or_404(Review, pk=review_id)
#     form = ReviewForm(instance=review)

#     template = 'activities/edit_review.html'
#     context = {
#         'form': form,
#         'review': review,
#     }

#     return render(request, template, context)
