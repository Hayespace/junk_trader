# items/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('<item_id>', views.items_detail, name='items_detail'),
    
]
