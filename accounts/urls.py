from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.login_request,name='login'),
    path('login/',views.login_request,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_request,name='logout'),
]
