from django.urls import path
from django.contrib import admin
import rest
from . import views

urlpatterns = [
    path('', views.index),
    path('logs.html', views.logs),
    path('Addr.html', views.addr),
    path('Addr/addPost/', views.addPost),
    path('getform.html', views.getform)
]
