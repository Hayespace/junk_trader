from django.contrib import admin
from .models import Item

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'name',
        'base_price',
        'quantity_available',
        'image',
    )

    ordering = ('name',)

admin.site.register(Item, ItemsAdmin)