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

    return render(request, )
