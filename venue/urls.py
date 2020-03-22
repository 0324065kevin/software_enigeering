from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
app_name = 'venue'

urlpatterns = [

    path('',views.venuesearch,name='venuesearch'),
    path('venueresult/',views.venueresult,name='venueresult'),
   
]