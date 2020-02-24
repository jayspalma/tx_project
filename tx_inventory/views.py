from django.shortcuts import render
from tx_inventory.models import Inventory
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def inventory(request):
    inventories = Inventory.objects.all()

    context = {
        'inventories':inventories,
    }
    return render(request,'inventory/inventory.html',context)