from django.contrib import admin

from .models import (
    CountryCodeDetails,
    GPSDeviceDetails,
    UserProfile,
    VehicleDetails,
    VendorProfile,
)


class classuserprofile(admin.ModelAdmin):
    list_display = ['user','bio']
admin.site.register(UserProfile, classuserprofile)
    
class classvehicledetails(admin.ModelAdmin):
    list_display = ['vehiclename','vehicleregno','vehicletype']
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
