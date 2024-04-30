from django.contrib import admin

from .models import (
    CountryCodeDetails,
    GPSDeviceDetails,
    GPSDeviceStatus,
    UserProfile,
    VehicleDetails,
    VendorProfile,
    vehiclemake,
    vehiclegroup,
    vehiclefueltype,
    DriverDetails,
    TripDetails,
    RouteDetails,
    SubscriptionMode,
    SubscriptionDetails
)


class classuserprofile(admin.ModelAdmin):
    list_display = ['user','bio']
admin.site.register(UserProfile, classuserprofile)
    
class classvehicledetails(admin.ModelAdmin):
    #list_display = ['vehiclename','vehicleregno','vehicletype']
    list_display = [field.name for field in VehicleDetails._meta.fields]
#admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(VehicleDetails, classvehicledetails)

class classgsdevicedetails(admin.ModelAdmin):
    list_display = ['vehiclename','deviceserialno','installedat','expiredat']
admin.site.register(GPSDeviceDetails,classgsdevicedetails)


class classcountrycodedetails(admin.ModelAdmin):
    list_display = ['countryname','countrycode']
admin.site.register(CountryCodeDetails, classcountrycodedetails)

class classvendorprofile(admin.ModelAdmin):
    list_display = ['vendorname','vendoraddress','vendorcountry','vendormob1','vendordistrict']
admin.site.register(VendorProfile,classvendorprofile)
# Register your models here.

class classgpsdevicestatus(admin.ModelAdmin):
    list_display = [field.name for field in GPSDeviceStatus._meta.fields]
admin.site.register(GPSDeviceStatus, classgpsdevicestatus)

class classvehiclemake(admin.ModelAdmin):
    list_display = [field.name for field in vehiclemake._meta.fields]
admin.site.register(vehiclemake, classvehiclemake)

class classvehiclegroup(admin.ModelAdmin):
    list_display = [field.name for field in vehiclegroup._meta.fields]
admin.site.register(vehiclegroup, classvehiclegroup)

class classvehiclefueltype(admin.ModelAdmin):
    list_display = [field.name for field in vehiclefueltype._meta.fields]
admin.site.register(vehiclefueltype,classvehiclefueltype)

class classdriverdetails(admin.ModelAdmin):
    list_display = [field.name for field in DriverDetails._meta.fields]
admin.site.register(DriverDetails, classdriverdetails)

class classtripdetails(admin.ModelAdmin):
    list_display = [field.name for field in TripDetails._meta.fields]
admin.site.register(TripDetails,classtripdetails)

class classrotuedetails(admin.ModelAdmin):
    list_display = [field.name for field in RouteDetails._meta.fields]
admin.site.register(RouteDetails,classrotuedetails)

class classsubscriptionmode(admin.ModelAdmin):
    list_display = [field.name for field in SubscriptionMode._meta.fields]
admin.site.register(SubscriptionMode, classsubscriptionmode)

class classsubscriptiondetails(admin.ModelAdmin):
    list_display = [field.name for field in SubscriptionDetails._meta.fields]
admin.site.register(SubscriptionDetails, classsubscriptiondetails)
