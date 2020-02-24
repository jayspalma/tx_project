from django.shortcuts import get_object_or_404, render
from tx_discrepancy.models import Discrepancy
# Create your views here.
# def login(request):
#     return render(request,'login.html')

def base(request):
    return render(request,'base.html')



