from django.shortcuts import (
    get_object_or_404, render, redirect, reverse, HttpResponse
    )
from timeslots.models import Timeslot
from django.contrib import messages


def view_basket(request):
    """ A view that renders the basket contents page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a timeslot and quantity of the specified activity
    to the shopping bag """
    if request.method == 'POST':
        timeslot_id = request.POST.get('timeslot')
        timeslot = get_object_or_404(Timeslot, pk=timeslot_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        basket = request.session.get('basket', {})

        if timeslot.available_capacity < quantity:
            messages.error(
                request, (
                    f'Could not add {timeslot} to your basket. Not enough \n'
                    f'available spaces in this timeslot.'))
        else:
            # Count quantity of each item in basket
            if timeslot_id in basket:
                currentQuantity = basket[timeslot_id]
                sumQuantity = currentQuantity + quantity
                if sumQuantity > timeslot.available_capacity:
                    messages.error(
                        request, (
                            f'There are not enough spaces in this timeslot. \n'
                            f'You already have {currentQuantity} spaces in \n'
                            f'your basket'))
                else:
                    basket[timeslot_id] += quantity
            else:
                basket[timeslot_id] = quantity

            messages.success(
                request, f'{timeslot.activity} has been added to your basket')
            request.session['basket'] = basket

    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Update the quantity of specified product """
    basket = request.session.get('basket', {})
    currentQuantity = basket.get(item_id, 0)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity != currentQuantity:
            timeslot = get_object_or_404(Timeslot, pk=item_id)
            if quantity > 0:
                if quantity <= timeslot.available_capacity:
                    basket[item_id] = quantity
                    messages.success(
                        request, f'{timeslot.activity} quantity has \n'
                                 f'been updated to {quantity}')
                else:
                    messages.error(
                        request, f'Can not update quantity. There \n'
                                 f'are only {timeslot.available_capacity} \n'
                                 f'spaces available to book.')
            else:
                basket.pop(item_id, None)
                messages.info(
                    request, f'Quantity is "0" so {timeslot.activity} \n'
                             f'has been removed from your basket')
            request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove specified product from basket """
    if request.method == 'POST':

        try:
            basket = request.session.get('basket', {})
            basket.pop(item_id, None)
            request.session['basket'] = basket
            timeslot = get_object_or_404(Timeslot, pk=item_id)
            messages.success(
                request,
                f'{timeslot.activity} has been removed from your basket')
            return HttpResponse(status=200)
        except Exception:
            messages.error(
                request, f'Error removing {timeslot.activity} from basket')
            return HttpResponse(status=500)

    return HttpResponse(status=400)
