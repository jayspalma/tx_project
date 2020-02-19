from django.shortcuts import render,get_object_or_404
from tx_discrepancy.models import Discrepancy

# Create your views here.
def details(request,discrepancy_id):
    discrepancy = get_object_or_404(Discrepancy, pk=discrepancy_id)
    context = {
        'discrepancy': discrepancy
    }
    return render(request,'details/details.html',context)