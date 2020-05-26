from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getPersonAll/', views.getPersonAll, name='getPersonAll'),
    path('messageBoard/', views.messageBoard, name='messageBoard'),
    path('getMessageAll/', views.getMessageAll, name='getMessageAll'),
]