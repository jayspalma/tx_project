from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def base(request):
    return render(request,'base.html')

def discrepancy(request):
    return render(request,'discrepancy.html')

def inventory(request):
    return render(request,'inventory.html')