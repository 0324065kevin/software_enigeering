# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from .models import activity

from .models import Favorite

# Register your models here.
admin.site.register(activity)

admin.site.register(Favorite)
