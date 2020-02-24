from django.db import models
from datetime import datetime
from tx_discrepancy.models import Site


class Inventory(models.Model):
    site_name = models.ForeignKey(Site,on_delete=models.CASCADE)
    transmitter = models.CharField(max_length=50)
    component = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    class Meta:
      verbose_name_plural = "Inventories"

    def __str__(self):
        return self.component
        
