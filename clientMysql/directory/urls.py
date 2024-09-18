from django.urls import path
from django.contrib import admin
import rest
from directory import views

urlpatterns = [
    path('/dir', views)
]
