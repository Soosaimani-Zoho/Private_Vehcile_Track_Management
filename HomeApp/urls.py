#from django.contrib import admin
from django.urls import path

from .views import HomeApp

urlpatterns = [
    path('',HomeApp.as_view(),name="HomeApp" )
]

