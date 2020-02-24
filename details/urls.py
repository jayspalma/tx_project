from django.urls import path
from details import views

urlpatterns = [
    path('<int:discrepancy_id>',views.details,name='details'),
    path('search/',views.search,name='search')
]
