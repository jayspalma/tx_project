from django.db import models
from datetime import datetime

# Create your models here.
class Site(models.Model):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=120)
  def __str__(self):
    return self.name

class Discrepancy(models.Model):
    date = models.DateField()
    site_class = models.CharField(max_length=10)
    report_status = models.CharField(max_length=20)
    description = models.TextField()
    sites = models.ForeignKey(Site,on_delete=models.CASCADE)

    class Meta:
      verbose_name_plural = "Discrepancies"

    def __str__(self):
        return self.site_class