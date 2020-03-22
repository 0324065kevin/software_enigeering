# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Venue(models.Model):
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    locationName = models.CharField(max_length=30)
    latitude = models.FloatField(max_length=30,default=-2000)
    longtitude = models.FloatField(max_length=30,default=-2000)
    city = models.CharField(max_length=30,default="")





