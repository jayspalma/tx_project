from django.shortcuts import render,redirect
from accounts import views
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Wrong Username/Password")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
        

def register(request):
    if request.method == "POST":

        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        #Check if password match
        if password == confirm_password:
            #Check if username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exist")
                return redirect('register')
            else:
                #Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request,"You are now registered. Please log in.")
                    return redirect('login')
        else:
            messages.error(request,"Passwords do not match!")
            return redirect('register')
    else:
        return render(request,'accounts/register.html')


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

