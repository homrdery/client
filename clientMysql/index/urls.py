from django.urls import path
from django.contrib import admin
import rest
from . import views

urlpatterns = [
    path('', views.computers),
    path('computers', views.computers),
    path('logs.html', views.logs)
]
