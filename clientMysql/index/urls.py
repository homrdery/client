from django.urls import path
from django.contrib import admin
import rest
from . import views

urlpatterns = [
    path('', views.index),
    path('computers', views.computers),
]
