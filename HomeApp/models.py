from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for your user profile
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user

class CountryCodeDetails(models.Model):
    countryname = models.CharField(_("Vendor Country Name"), max_length=25)
    countrycode = models.IntegerField(_("Country Code"), primary_key=True,validators=[MinValueValidator(0),MaxValueValidator(9999)])
    
    def __str__(self):
        return self.countrycode
    
    
class VendorProfile(models.Model):
    vendorname = models.CharField(_("Vendor name"),max_length=50)
    vendoraddress = models.TextField(_("Vendor Address"))
    vendorcountry = models.ForeignKey(CountryCodeDetails, on_delete=models.CASCADE)
    vendormob1 =models.IntegerField(_("Vendor Mobile no_1"), unique=True)
    vendormob2 = models.IntegerField(_("Vendor Mobile no_2"))
    vendordistrict = models.CharField(_("Vendor District"), max_length=50)
    
    def __str__(self):
        return self.vendorname

    
class VehicleDetails(models.Model):
    vehiclename = models.CharField(_("Vehicle Name"), max_length=50)
    vehicleregno = models.CharField(_("Vehicle Reg No"), max_length=50, unique=True)
    vehicletype = models.CharField(_("Vehicle Type"), max_length=50)
    
    def __str__(self):
        return self.vehiclename
    
class GPSDeviceDetails(models.Model):
    veciclename = models.OneToOneField(VehicleDetails, on_delete=models.CASCADE)
    deviceserialno = models.CharField(_("GPSDevice Serial No"), max_length=50,unique=True)
    installedat = models.DateTimeField(_("GPSDevice Installed Date"), auto_now=True, auto_now_add=False)
    expiredat = models.DateTimeField(_("GPSDevice Expirty Date"), auto_now=False, auto_now_add=False)
    
