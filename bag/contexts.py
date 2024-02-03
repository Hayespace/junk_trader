from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item

MAXIMUM_ITEMS_ALLOWED = 10  

def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.base_price
        item_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item, 
        })


    # Check if the number of items exceeds the maximum allowed
    if item_count > MAXIMUM_ITEMS_ALLOWED:
        max_items_message = f"You have exceeded the maximum allowed items of {MAXIMUM_ITEMS_ALLOWED}. Please upgrade your bag."
    else:
        max_items_message = None

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'max_items_message': max_items_message,
        
    }

    return context
