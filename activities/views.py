from django.shortcuts import render, redirect, reverse, get_object_or_404
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

    # Set variable values
    activities = Activity.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    current_sorting = None

    if request.GET:
        # Check for sort request and set value
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                activities = activities.annotate(lower_name=Lower('name'))

            # Check sort direction request and set value
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            activities = activities.order_by(sortkey)

        # Check if a category has been selected and set category value
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            activities = activities.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Check for search queries, set query value
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    ("You didn't enter any search criteria." +
                     " Here are all activities offered at the park.")
                )
                return redirect(reverse('activities'))

            # Only display activities that match the query
            queries = Q(name__icontains=query)
            activities = activities.filter(queries)

        # Sort activities that match above requests
        current_sorting = f'{sort}_{direction}'

    context = {
        'activities': activities,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'activities/activities.html', context)


def activity_details(request, activity_id):
    """ A view for displaying details of a specific activity """

    activity = get_object_or_404(Activity, pk=activity_id)
    category = activity.category

    # Save activity to session to help with navigation on other pages.
    current_activity = activity_id
    activity_capacity = activity.capacity
    request.session['current_activity'] = current_activity
    request.session['activity_capacity'] = activity_capacity

    # Only show timeslots that are in the future
    future_timeslots = activity.timeslot.filter(start_time__gt=timezone.now())

    # Only show reviews for current activity
    # Sort most recent first
    reviews = Review.objects.filter(activity=activity).order_by('-review_time')

    for timeslot in future_timeslots:
        timeslot.total_capacity = (
            timeslot.available_capacity + timeslot.spaces_booked)
        print(timeslot.total_capacity)

    context = {
        'activity': activity,
        'future_timeslots': future_timeslots,
        'reviews': reviews,
        'category': category,
    }

    return render(request, 'activities/activity_details.html', context)


@login_required
def manage_activities(request):
    """ Show manage activities options """
    # Only let superuser view this page
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

    # Only let superuser view this page
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    # Check if form is submitted
    if request.method == "POST":
        # Get form input values
        form = ActivityForm(request.POST, request.FILES)
        # Check form validity
        if form.is_valid():
            # Save activity and confirm success
            activity = form.save()
            messages.success(request, 'Successfully added activity!')
            return redirect(reverse('activity_details', args=[activity.id]))
        else:
            messages.error(
                request,
                'Failed to add activity. Please ensure the form is valid.'
                )
    else:
        # If form isn't submitted, render the form empty
        form = ActivityForm()

    context = {
        'form': form,
    }

    return render(request, 'activities/add_activity.html', context)


@login_required
def add_timeslot(request):
    """ Add a timeslot to an activity """

    # Only let superuser view this page
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    # Get most recent activity from the session
    current_activity = request.session.get('current_activity')
    activity_capacity = request.session.get('activity_capacity')

    if current_activity is None:
        messages.error(
            request,
            ('Unable to load form, please return to' +
             'the activity page and try again')
        )
    else:
        # Get values from form if submitted and valid, save as new timeslot
        if request.method == "POST":
            form = TimeslotForm(request.POST)
            if form.is_valid():
                timeslot = form.save()
                messages.success(request, f'Successfully added {timeslot}!')
                return redirect(
                    reverse('activity_details', args=[current_activity]))
            else:
                messages.error(
                    request,
                    'Failed to add timeslot. Please ensure the form is valid.')
        else:
            # Populate form with activity from session
            form = TimeslotForm(
                initial={
                    'activity': current_activity,
                    'available_capacity': activity_capacity,
                    })

    context = {
        'form': form,
        'current_activity': current_activity,
    }

    return render(request, 'activities/add_timeslot.html', context)


@login_required
def edit_activity(request, activity_id):
    """ Edit an activity """

    # Only let superuser view this page
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    activity = get_object_or_404(Activity, pk=activity_id)

    if request.method == "POST":
        # Get values from activity form and save
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
        # Prefill values of activity form
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

    # Only let superuser view this page
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    timeslot = get_object_or_404(Timeslot, pk=timeslot_id)
    activity = timeslot.activity

    if request.method == "POST":
        # Get values from activity form and update
        form = TimeslotForm(request.POST, instance=timeslot)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated timeslot!')
            return redirect(
                reverse('activity_details', args=[timeslot.activity.id]))
        else:
            messages.error(
                request,
                'Failed to update timeslot. Please ensure the form is valid.')
    else:
        # Prefill values of timeslot form fields
        form = TimeslotForm(instance=timeslot)

    template = 'activities/edit_timeslot.html'
    context = {
        'form': form,
        'timeslot': timeslot,
        'activity': activity,
    }

    return render(request, template, context)


@login_required
def delete_activity(request, activity_id):
    """ Delete activity """

    # Only let superuser view this page
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    activity = get_object_or_404(Activity, id=activity_id)

    # Delete activity if request is post, otherwise, display template
    if request.method == 'POST':
        activity.delete()
        messages.success(request, 'Activity Deleted')
        return redirect('manage_activities')

    template = 'activities/delete_activity.html'
    context = {
        'activity': activity,
    }

    return render(request, template, context)


@login_required
def delete_timeslot(request, timeslot_id):
    """ Delete timeslot """

    # Only let superuser view this page
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you are not authorized to complete this action.')
        return redirect(reverse('home'))

    timeslot = get_object_or_404(Timeslot, id=timeslot_id)
    activity = timeslot.activity

    # Delete timeslot if request is post, otherwise, display template
    if request.method == 'POST':
        timeslot.delete()
        messages.success(request, 'Timeslot Deleted')
        return redirect(reverse('activity_details', args=[activity.id]))

    template = 'activities/delete_timeslot.html'
    context = {
        'timeslot': timeslot,
        'activity': activity,
    }

    return render(request, template, context)


def requirements(request):
    """ Display the requirements template """

    template = 'activities/requirements.html'

    return render(request, template)
