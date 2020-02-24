from django.shortcuts import render,get_object_or_404
from tx_discrepancy.models import Discrepancy
from details.choices import site_class_choices,report_status_choices,site_code_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def details(request,discrepancy_id):
    discrepancy = get_object_or_404(Discrepancy, pk=discrepancy_id)
    context = {
        'discrepancy': discrepancy
    }
    return render(request,'details/details.html',context)

def search(request):
    query_set = Discrepancy.objects.order_by('-date')


    #Site class
    if 'site_class' in request.GET:
        site_class = request.GET['site_class']
        if site_class:
            query_set = query_set.filter(site_class__iexact=site_class)

    #Report Status
    if 'report_status' in request.GET:
        report_status = request.GET['report_status']
        if report_status:
            query_set = query_set.filter(report_status__iexact=report_status)

    #Site code
    if 'sites' in request.GET:
        sites = request.GET['sites']
        if sites:
            query_set = query_set.filter(sites__code__iexact=sites)

    
    # paginator = Paginator(query_set,3)
    # page = request.GET.get('page')
    # paged_discrepancies = paginator.get_page(page)

    context = {
        'discrepancies':query_set,
        'site_class_choices':site_class_choices,
        'report_status_choices':report_status_choices,
        'site_code_choices':site_code_choices,
        'values':request.GET,
    }
 
    return render(request,'details/search.html',context)