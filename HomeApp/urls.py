#from django.contrib import admin
from django.urls import path

from .views import (
    HomeApp,
    all_trips,
    all_vehicle,
    vehicle_directory_add,
    my_driver,
    my_driver_add,
    consigners,
    
    my_expances,
    routes,
    routes_add,
    service_history,
    service_schedules,
    trip_schedules,
    vehicle_directory,
    vehicle_group,
    vehicle_states,
    subscription_history,
    subscription_renew,
    
    #--------------API Views---------------
    API_VendorProfiles, API_VehicleDetails,API_VeihleDetails
    #--------------API Views---------------
)

#----------------------API Swagger-------------------------------------------------------------------
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
       title="KSM RestAPI Swagger",
       default_version='v1',
       description="KSM API Description",
       terms_of_service="https://www.example.com/policies/terms/",
       contact=openapi.Contact(email="soosaimanni@gotoz.com"),
       license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
#----------------------API Swagger-----------------------------------------------------------------


urlpatterns = [
    #path('logout',logout_view,name='logout'),    
    path('',HomeApp.as_view(),name="dashboard"),
    path('all_vehicle/',all_vehicle.as_view(),name="all_vehicle"),
    path('vehicle_directory', vehicle_directory.as_view(), name = 'vehicle_directory'),
    path('vehicle_directory/add',vehicle_directory_add.as_view(),name='vehicle_directory_add'),
    #path('/vehicle_directory/<pk>', vehicle_directory.as_view(), name = 'vehicle_directory_edit'),
    path('vehicle_group/',vehicle_group.as_view(), name='vehicle_group'),
    path('vehicle_states/',vehicle_states.as_view(),name='vehicle_states'),
    path('my_driver/',my_driver.as_view(),name='my_driver'),
    path('my_driver/add',my_driver_add.as_view(),name='my_driver_add'),
    path('all_trips/',all_trips.as_view(),name='all_trips'),
    path('trip_schedules/',trip_schedules.as_view(),name='trip_schedules'),
    path('routes/',routes.as_view(),name='routes'),
    path('routes/add/',routes_add.as_view(),name='routes_add'),
    path('consigners/',consigners.as_view(),name='consigners'),
    path('my_expances/',my_expances.as_view(),name='my_expances'),
    path('service_history/',service_history.as_view(), name = 'service_history'),
    path('service_schedules/',service_schedules.as_view(),name='service_schedules'),
    path('subscription_history/',subscription_history.as_view(),name='subscription_history'),
    path('subscription_renew/',subscription_renew.as_view(),name='subscription_renew'),
    
    
    #-------------------------------Swagger API-----------------------------------------------------
    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/vendorprofile',API_VendorProfiles.as_view(),name='VendorProfiles_List'),
    path('swagger/vehicledetails',API_VehicleDetails.as_view(),name='Vehicle Details'),
    path('swagger/API_VeihleDetails',API_VehicleDetails.as_view(),name='API_VeihleDetails'),
    
    #-------------------------------Swagger API------------------------------------------------------
    
]

