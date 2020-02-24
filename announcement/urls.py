from django.urls import path
from announcement import views

urlpatterns = [
    path('',views.home,name='home')
]
