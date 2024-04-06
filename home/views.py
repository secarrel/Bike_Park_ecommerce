from django.shortcuts import render
import cloudinary.uploader

# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

