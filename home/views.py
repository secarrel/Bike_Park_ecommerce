from django.shortcuts import render
from activities.models import Activity, Category
from django.conf import settings


def index(request):
    """ A view to return the index page """

    categories = Category.objects.all()

    template = 'home/index.html'
    context = {
        'categories': categories,
    }

    return render(request, template, context)


def about(request):
    """ A view to return the about page """

    api_key = settings.GOOGLE_API_KEY

    template = 'home/about.html'
    context = {
        'api_key': api_key,
    }

    return render(request, template, context)


def trails(request):
    """ A view to return the trails page """

    categories = Category.objects.all()

    template = 'home/trails.html'
    context = {
        'categories': categories,
    }

    return render(request, template, context)