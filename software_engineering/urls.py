"""software_engineering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
# Import view functions from trips app.

from django.contrib import admin
from django.urls import path
from Member import views as views1
from Comment import views as views2
from activity import views as views3

from django.urls import path,re_path
from django.urls import include

urlpatterns = [
    path('', views3.home),
    path('index/', views3.home),
    path('ticketsale/', views1.ticketsale),
    path('login/', views1.login),
    path('logout/', views1.logout),
    path('fourm/list/', views2.list),
    path('admin/', admin.site.urls),
    path('register/', views1.register),
    path('myfavorite/', views3.collection),
    path('', include('Comment.urls')),
    path('activity/', include('activity.urls')),
    path('venue/' , include('venue.urls')),
]