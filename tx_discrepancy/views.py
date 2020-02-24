from django.shortcuts import render
from tx_discrepancy.models import Discrepancy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from details.choices import site_class_choices,report_status_choices,site_code_choices


# Create your views here.

def discrepancy(request):
    discrepancies = Discrepancy.objects.all()

    paginator = Paginator(discrepancies,2)
    page = request.GET.get('page')
    paged_discrepancies = paginator.get_page(page)



    context = {
        'discrepancies':paged_discrepancies,
        'site_code_choices':site_code_choices,
        'site_class_choices':site_class_choices,
        'report_status_choices':report_status_choices,
    }
    return render(request,'discrepancies/discrepancy.html',context)

