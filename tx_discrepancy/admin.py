from django.contrib import admin
from tx_discrepancy.models import Site, Discrepancy

class DiscrepancyAdmin(admin.ModelAdmin):
    list_display = ('date','site_class','report_status','sites')
    list_display_links = ('date','site_class')
    list_filter = ('sites','site_class',)
    search_fields = ('site_class',)
    list_per_page = (30)

# Register your models here.
admin.site.register(Site)
admin.site.register(Discrepancy,DiscrepancyAdmin)