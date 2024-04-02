from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def user_details(request):
    """ Display the user's details. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    template = 'profiles/user_details.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, user_id):
    # Retrieve the user's orders based on the user_id
    orders = Order.objects.filter(user_profile__user_id=user_id)

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)