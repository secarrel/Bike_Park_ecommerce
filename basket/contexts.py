from timeslots.models import Timeslot
from django.shortcuts import get_object_or_404


def basket_contents(request):
    basket_items = []
    total = 0
    basket = request.session.get('basket', {})

    activity_ids = set()
    timeslot_ids = set()

    for item_id, quantity in basket.items():
        timeslot = get_object_or_404(Timeslot, pk=item_id)
        activity = timeslot.activity
        total += quantity * float(activity.price)
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'activity': activity,
            'timeslot': timeslot
        })
        activity_ids.add(activity.id)
        timeslot_ids.add(timeslot.id)

    activity_count = len(activity_ids)
    timeslot_count = len(timeslot_ids)

    context = {
        'basket_items': basket_items,
        'activity_count': activity_count,
        'timeslot_count': timeslot_count,
        'total': total,
    }

    return context
