from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Activity, Category, Review
from .forms import ActivityForm, TimeslotForm
from timeslots.models import Timeslot
from django.utils import timezone


def all_activities(request):
    """ A view to all activities, including sorting and search queries."""

    activities = Activity.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    current_sorting = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                activities = activities.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            activities = activities.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            activities = activities.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 
                    ("You didn't enter any search criteria." + 
                    " Here are all activities offered at the park.")
                )
                return redirect(reverse('activities'))
            
            queries = Q(name__icontains=query)
            activities = activities.filter(queries)

        current_sorting = f'{sort}_{direction}'

    context = {
        'activities': activities,
        'search-term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'activities/activities.html', context)


def activity_details(request, activity_id):
    """ A view for displaying details of a specific activity """

    activity = get_object_or_404(Activity, pk=activity_id)
    current_activity = activity.id
    activity_capacity = activity.capacity
    request.session['current_activity'] = current_activity
    request.session['activity_capacity'] = activity_capacity
    future_timeslots = activity.timeslot.filter(start_time__gt=timezone.now())
    reviews = Review.objects.filter(activity=activity)
    context = {
        'activity': activity,
        'future_timeslots': future_timeslots,
        'reviews': reviews
    }

    return render(request, 'activities/activity_details.html', context)


@login_required
def manage_activities(request):
    """ Show manage activities options """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    activities = Activity.objects.all()

    context = {
        'activities': activities,
    }

    return render(request, 'activities/manage_activities.html', context)


@login_required
def add_activity(request):
    """ Add a activity to a catgeory """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save()
            messages.success(request, 'Successfully added activity!')
            return redirect(reverse('activity_details', args=[activity.id]))
        else:
            messages.error(
                request,
                'Failed to add activity. Please ensure the form is valid.'
                )
    else:
        form = ActivityForm()

    context = {
        'form': form,
    }

    return render(request, 'activities/add_activity.html', context)


@login_required
def add_timeslot(request):
    """ Add a timeslot to an activity """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))
    current_activity = request.session.get('current_activity')
    activity_capacity = request.session.get('activity_capacity')
    if current_activity is None:
        messages.error(
            request, 
            ('Unable to load form, please return to' + 
            'the activity page and try again')
        )
    else:
        if request.method == "POST":
            form = TimeslotForm(request.POST)
            if form.is_valid():
                timeslot = form.save()
                messages.success(request, 'Successfully added timeslot!')
                return redirect(
                    reverse('activity_details', args=[current_activity]))
            else:
                messages.error(
                    request,
                    'Failed to add timeslot. Please ensure the form is valid.')
        else:
            form = TimeslotForm(
                initial={
                    'activity': current_activity,
                    'available_capacity': activity_capacity})


    context = {
        'form': form,
        'current_activity': current_activity
    }

    return render(request, 'activities/add_timeslot.html', context)


@login_required
def edit_activity(request, activity_id):
    """ Edit an activity """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated activity!')
            return redirect(reverse('activity_details', args=[activity.id]))
        else:
            messages.error(
                request,
                'Failed to update activity. Please ensure the form is valid.')
    else:
        form = ActivityForm(instance=activity)

    template = 'activities/edit_activity.html'
    context = {
        'form': form,
        'activity': activity,
    }

    return render(request, template, context)


@login_required
def edit_timeslot(request, timeslot_id):
    """ Edit an activity """
    
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))
    
    timeslot = get_object_or_404(Timeslot, pk=timeslot_id)

    if request.method == "POST":
        form = TimeslotForm(request.POST, instance=timeslot)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated timeslot!')
            return redirect(reverse('activity_details', args=[timeslot.activity.id]))
        else:
            messages.error(
                request,
                'Failed to update timeslot. Please ensure the form is valid.')
    else:
        form = TimeslotForm(instance=timeslot)

    template = 'activities/edit_timeslot.html'
    context = {
        'form': form,
        'timeslot': timeslot,
    }

    return render(request, template, context)


@login_required
def delete_activity(request, activity_id):
    """ Delete activity """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    activity = get_object_or_404(Activity, id=activity_id)
    activity.delete()
    messages.success(request, 'Activity Deleted')
    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        # Check if the referer contains 'manage_activities'
        if 'manage_activities' in referer:
            # Redirect to manage_activities page
            return HttpResponseRedirect(referer)

    # If the referer does not contain 'manage_activities' or is None,
    # redirect to 'activities' page
    return redirect(reverse('activities'))


@login_required
def delete_timeslot(request, timeslot_id):
    """ Delete activity """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    timeslot = get_object_or_404(Timeslot, id=timeslot_id)
    activity = timeslot.activity
    timeslot.delete()
    messages.success(request, 'Timeslot Deleted')
    return redirect(reverse('activity_details', args=[activity.id]))
