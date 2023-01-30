"""programowanie URL Configuration

URLS dla dashboard

"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main_page),
    path('cennik', views.cennik_page),
    path('czat', views.czat_page),
    path('kalendarz', views.kalendarz_page),
    path('pacjenci', views.pacjenci_page),
    path('wizyty', views.wizyty_page),
]
