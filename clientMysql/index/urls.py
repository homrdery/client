from django.urls import path
from django.contrib import admin
import rest
from . import views

urlpatterns = [
    path('', views.computers),
    path('mainpage.html', views.computers),
    path('logs.html', views.logs),
    path('Addr.html', views.addr),
    path('Addr/add/', views.add)

]
