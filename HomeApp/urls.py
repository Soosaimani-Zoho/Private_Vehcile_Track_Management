#from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',Login.as_view(),name="Login" ),
    path('dashboard',HomeApp.as_view(),name="dashboard"),
    path('all_vehicle',all_vehicle.as_view(),name="all_vehicle"),
    path('vehicle_directory', vehicle_directory.as_view(), name = 'vehicle_directory'),
    path('vehicle_group',vehicle_group.as_view(), name='vehicle_group'),
    path('vehicle_states',vehicle_states.as_view(),name='vehicle_states'),
    path('my_expances',my_expances.as_view(),name='my_expances'),
    path('service_history',service_history.as_view(), name = 'service_history'),
    path('service_schedules',service_schedules.as_view(),name='service_schedules'),
]

