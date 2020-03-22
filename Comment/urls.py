from django.urls import path
from django.views.generic import RedirectView
from .views import *

# urlpatterns = [
#     path('', RedirectView.as_view(url='message/')),
#     path('message/', MessageList.as_view()),
#     path('message/<int:pk>/', MessageDetail.as_view()),
#     path('message/create/', MessageCreate.as_view()),
#     path('message/<int:pk>/delete/', MessageDelete.as_view()),
# ]
app_name = "Comment"
urlpatterns = [
    path('message/list', list, name="message/list"),
    path('message/create/', create, name="message/create"),
    path('message/edit/<int:pk>/', edit, name="message/edit"),
    path('message/delete/<int:pk>/', delete, name="message/delete"),
]