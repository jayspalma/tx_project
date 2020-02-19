from django.shortcuts import render
from accounts import views

# Create your views here.
def login(request):
    return render(request,'accounts/login.html')

def register(request):
    return render(request,'accounts/register.html')

