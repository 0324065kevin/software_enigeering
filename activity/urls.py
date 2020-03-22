from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
app_name = 'activity'

urlpatterns = [
    # activity page
    path('data/' , views.getNewdataset , name = 'getdata'),

    # path('' , views.getactivity , name = 'getactivity'),

    path('activitysearch/', views.queryactivity , name= 'query'),

    path('detail/<int:id>', views.activity_detail, name= 'activity_detail'),

    path('collect/<int:id>' , views.favorite , name = 'activity_collect'),

    path('deletfavorite/<int:id>' , views.delet_favorite , name = 'delet_favorite'),

    # path('', views.getactivity, name='getactivity'),



]