from django.urls import path
from django.contrib import admin
import rest
from . import views

urlpatterns = [
    path('addr', views.addr),
    path('directory/getform.html', views.getform),

]
