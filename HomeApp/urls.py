#from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',HomeApp.as_view(),name="HomeApp" ),
    path('all_vehicle',all_vehicle.as_view(),name="all_vehicle"),
]

