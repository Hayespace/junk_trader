from django.shortcuts import render
from .models import Item

def get_available_quantity(item):
    
    return item.quantity_available

def all_items(request):

    items = Item.objects.all()
    

    # Add available_quantity for each item
    for item in items:
        item.available_quantity = get_available_quantity(item)

    context = {
        'items': items,
    }
    return render(request, 'items/items.html', context)


