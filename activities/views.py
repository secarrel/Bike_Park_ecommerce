from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Activity, Category
from .forms import ActivityForm, TimeslotForm

# Create your views here.
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
                messages.error(request, "You didn't enter any search criteria")
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

    context = {
        'activity': activity,
    }

    return render(request, 'activities/activity_details.html', context)


def manage_activities(request):
    """ Show manage activities options """
    activities = Activity.objects.all()
    
    context = {
        'activities': activities,
    }

    return render(request, 'activities/manage_activities.html', context)

def manage_timeslots(request):
    """ Show manage timeslots options """

    return render(request, 'activities/manage_timeslots.html')


def add_activity(request):
    """ Add a activity to a catgeory """
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added activity!')
            return redirect(reverse('add_activity'))
        else: 
            messages.error(request, 'Failed to add activity. Please ensure the form is valid.')
    else:
        form = ActivityForm()

    context = {
        'form': form,
    }

    return render(request, 'activities/add_activity.html', context)

def add_timeslot(request):
    """ Add a timeslot to an activity """
    if request.method == "POST":
        form = TimeslotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added timeslot!')
            return redirect(reverse('add_timeslot'))
        else: 
            messages.error(request, 'Failed to add timeslot. Please ensure the form is valid.')
    else:
        form = TimeslotForm()

    context = {
        'form': form,
    }

    return render(request, 'activities/add_timeslot.html', context)

def edit_activity(request, activity_id):
    """ Edit an activity """
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated activity!')
            return redirect(reverse('activity_details', args=[activity.id]))
        else: 
            messages.error(request, 'Failed to update activity. Please ensure the form is valid.')
    else:
        form = ActivityForm(instance=activity)
        messages.info(request, f'You are editing {activity.name}')

    template = 'activities/edit_activity.html'
    context = {
        'form': form,
        'activity': activity,
    }

    return render(request, template, context)


def edit_timeslot(request, timeslot_id):
    """ Edit an activity """

    timeslot = get_object_or_404(Activity, pk=timeslot_id)
    form = TimeslotForm(instance=timeslot)
    messages.info(request, f'You are editing {timeslot.name}')

    template = 'activities/edit_timeslot.html'
    context = {
        'form': form,
        'timeslot': timeslot,
    }

    return render(request, template, context)
