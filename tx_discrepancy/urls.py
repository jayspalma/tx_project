from django.urls import path
from tx_discrepancy import views

urlpatterns = [
    path('',views.discrepancy,name='discrepancy')
]