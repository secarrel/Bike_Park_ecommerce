from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Activity, Category

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