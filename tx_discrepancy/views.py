from django.shortcuts import render
from tx_discrepancy.models import Discrepancy


# Create your views here.

def discrepancy(request):
    discrepancies = Discrepancy.objects.all()
    context = {
        'discrepancies':discrepancies
    }
    return render(request,'discrepancies/discrepancy.html',context)