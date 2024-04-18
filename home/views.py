from django.shortcuts import render
from activities.models import Activity, Category


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

    categories = Category.objects.all()

    template = 'home/about.html'
    context = {
        'categories': categories,
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