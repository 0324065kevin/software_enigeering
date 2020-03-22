# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from venue.models import Venue

# Create your models here.

class activity(models.Model):
    # activity_id = models.AutoField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=30 , default='')
    category = models.CharField(max_length=30)
    ShowUnit = models.CharField(max_length=30)
    discontinfo = models.CharField(max_length=30)
    descriptionFilterHtml = models.CharField(max_length=30)
    imageUrl = models.CharField(max_length=30)
    masterUnit = models.CharField(max_length=30)
    webSales = models.CharField(max_length=30)
    sourceWebPromote = models.CharField(max_length=30)
    time = models.DateField(max_length=30)
    endtime = models.DateField(max_length=30)
    onSales = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    city = models.CharField(max_length=30,default='')
    comment = models.CharField(max_length=30,default="")
    editModifyDate = models.CharField(max_length=30,default="")
    period = models.CharField(max_length=30, default="")
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE)
    locationName = models.CharField(max_length=30 , default="")


class Favorite(models.Model):
    # favorite_id = models.AutoField(auto_created=True ,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_fk = models.ForeignKey(activity, on_delete=models.CASCADE)


