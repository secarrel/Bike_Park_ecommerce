from django.shortcuts import render
import cloudinary.uploader

# Create your views here.
def index(request):
    """ A view to return the index page """

    def test_cloudinary(request):
        cloudinary_response = cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg",
                                                     public_id="olympic_flag")
        return render(request, 'home/index.html', {'cloudinary_response': cloudinary_response})

