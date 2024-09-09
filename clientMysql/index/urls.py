from django.urls import path
from django.contrib import admin
import rest
from . import views

urlpatterns = [
    path('', views.computers),
    path('computers', views.computers),
    path('index/logs.html', views.logs),
    path('index/NeoWeb.html', views.NeoWeb)

]
