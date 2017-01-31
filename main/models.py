from django.db import models
from geoposition.fields import GeopositionField

class Order(models.Model):
    current_point = GeopositionField(blank=False)
    current_date = models.DateField(blank=True)
    current_time = models.TimeField(blank=True)
    phone4 = models.CharField(max_length=17, blank=False)

class CallBack2(models.Model):
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=17, blank=False)



