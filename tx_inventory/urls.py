from django.urls import path
from tx_inventory import views

urlpatterns = [
    path('',views.inventory,name='inventory')
]