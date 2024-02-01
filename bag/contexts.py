from decimal import Decimal
from django.conf import settings

MAXIMUM_ITEMS_ALLOWED = 10  

def bag_item(request):
    bag_items = []
    total = 0
    item_count = 0


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
