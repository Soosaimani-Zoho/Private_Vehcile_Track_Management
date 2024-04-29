from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
import json
from django.core.exceptions import ValidationError

 


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for your user profile
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.user)
    '''def loginid(self,username):
        user = UserProfile.objects.get(user=username)
        return user.id'''

class CountryCodeDetails(models.Model):
    countryname = models.CharField(_("Vendor Country Name"), max_length=25)
    countrycode = models.IntegerField(_("Country Code"), primary_key=True,validators=[MinValueValidator(0),MaxValueValidator(9999)])
    
    def __str__(self):
        return str(self.countrycode)
    
class vehiclemake(models.Model):
    vehiclemake = models.CharField(_("Vehicle Make"), max_length=50, primary_key=True)
    
    def __str__(self):
        return self.vehiclemake
    
class vehiclefueltype(models.Model):
    fueltype = models.CharField(_("Vehicle Fuel Type"), max_length=50, primary_key=True)
    
    def __str__(self):
        return self.fueltype
    
class vehiclegroup(models.Model):
    groupname = models.CharField(_("Vehicle Group Name"), max_length=50)
    vehicleregnolist = models.TextField(_("Vehicle Reg No list as json"))

    def setlist(self, name, regnolist):
        self.groupname = name
        try:
            self.vehicleregnolist = json.dumps(regnolist)
        except json.JSONEncodeError as e:
            raise ValidationError(f"Error encoding JSON: {e}")

    def getlist(self):
        try:
            return json.loads(self.vehicleregnolist)
        except json.JSONDecodeError as e:
            raise ValidationError(f"Error decoding JSON: {e}")
    
    
    
class VendorProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    vendorname = models.CharField(_("Vendor name"),max_length=50)
    vendorid = models.CharField(_("Vendor ID"), max_length=50, primary_key=True)
    vendoraddress = models.TextField(_("Vendor Address"))
    vendorcountry = models.ForeignKey(CountryCodeDetails, on_delete=models.CASCADE)
    vendormob1 =models.IntegerField(_("Vendor Mobile no_1"), unique=True)
    vendormob2 = models.IntegerField(_("Vendor Mobile no_2"))
    vendordistrict = models.CharField(_("Vendor District"), max_length=50)
    isactive = models.BooleanField(_(" Active or Not"))
    
    def __str__(self):
        return self.vendorname

    
class VehicleDetails(models.Model):
    vendorid = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    vehiclename = models.CharField(_("Vehicle Name"), max_length=50)
    vehicleregno = models.CharField(_("Vehicle Reg No"), max_length=50, unique=True)
    vehicletype = models.CharField(_("Vehicle Type"), max_length=50)
    vehicleimage = models.ImageField(_("Vehicle Image"), upload_to=None, null= True, blank= True, height_field=None, width_field=None, max_length=None)
    odometerreading = models.IntegerField(_("Vehicle Odometer Reading"))
    vehiclemake = models.ForeignKey(vehiclemake, on_delete=models.CASCADE)
    modelyear = models.IntegerField(_("Vehicle Model Year"))
    chessisno = models.CharField(_("Vehicle Chassis No"), max_length=50)
    
    expectmileage = models.IntegerField(_("Expected Mileage"))
    isdelete = models.BooleanField(_(" Delete or Not"))
    createdat = models.DateTimeField(_("Created At"),auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated At"), auto_now=True)
    
    
    
    def __str__(self):
        return self.vehiclename
    
    @classmethod
    def get_vehicleregno_list(cls):
        return cls.objects.values_list('vehicleregno', flat=True)
    
    
        
    
class GPSDeviceDetails(models.Model):
    vehiclename = models.OneToOneField(VehicleDetails, on_delete=models.CASCADE)
    deviceserialno = models.CharField(_("GPSDevice Serial No"), max_length=50,unique=True)
    installedat = models.DateTimeField(_("GPSDevice Installed Date"), auto_now=True, auto_now_add=False)
    expiredat = models.DateTimeField(_("GPSDevice Expirty Date"), auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.deviceserialno
    
    
class GPSDeviceStatus(models.Model):
    deviceserialno = models.OneToOneField(GPSDeviceDetails, on_delete=models.CASCADE)
    moving = models.BooleanField(_("GPS Device Move Status"))
    stopped = models.BooleanField(_("GPS Device Stopped Status"))
    idlling = models.BooleanField(_("GPS Device Idlling Status"))
    offline = models.BooleanField(_("GPS Device Offline Status"))
    subsexpired = models.BooleanField(_("GPS Device Subscription Expiry Status"))
    ignition = models.BooleanField(_("GPS Device Ignition Status"))
    gpssignal = models.CharField(_("GPS Signal Status"), max_length=50)
    speed = models.IntegerField(_("GPS Device Speed"))
    orientationvalue = models.IntegerField(_("GPS Device Orientation value"))
    deviceexternalpower = models.BooleanField(_("GPS Device External Power Status"))
    location = models.TextField(_("GPS Device Location"))
    temperature = models.IntegerField(_("GPS Device temperature"))
    internalbatterypower = models.IntegerField(_("GPS Device Internal Battery Power"))
    movmentvalue = models.IntegerField(_("GPS Device Movement Value"))
    gsmstrength = models.FloatField(_("GPS Device GSM Strength"))
    lat = models.FloatField(_("GPS Device Latitude"))
    long = models.FloatField(_("GPS Device Longitude"))
    
    def __str__(self):
        return f"{self.lat},{self.long}"
    

class DriverDetails(models.Model):
    drivername = models.CharField(_("Driver Name"), max_length=50)
    phoneno1 = models.CharField(_("Driver Mob No1"), max_length=50)
    phoneno2 = models.CharField(_("Driver Mob No2"), max_length=50, null=True)
    
    vehicleregno = models.ForeignKey(VehicleDetails, on_delete=models.CASCADE)
    licenseno = models.CharField(_("License No"), max_length=50)
    guarantorname = models.CharField(_("Guarantor Name"), max_length=50, null=True)
    guarandorphoneno = models.CharField(_("Guarantor Mob No"), max_length=50, null=True)
    countrycode = models.ForeignKey(CountryCodeDetails, on_delete=models.CASCADE)
    aadharno = models.CharField(_("Aadhar Number"), max_length=50)
    licenseissuedate = models.DateField(auto_now=False, auto_now_add=False)
    licenseexpirtydate = models.DateField(auto_now=False, auto_now_add=False)
    driverid = models.CharField(_("Driver ID"), max_length=50,unique=True)
    driverimage = models.ImageField(_("Driver Image"), upload_to=None, null= True, blank= True, height_field=None, width_field=None, max_length=None)
    pancardimage = models.ImageField(_("pancard Image"), upload_to=None, null= True, blank= True, height_field=None, width_field=None, max_length=None)
    driverlicense = models.ImageField(_("Driver license"), upload_to=None, null= True, blank= True, height_field=None, width_field=None, max_length=None)
    drivermisc = models.ImageField(_("Driver Miscellaneous"), upload_to=None, null= True, blank= True, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.drivername
    

    
class RouteDetails(models.Model):
    routeid = models.CharField(_("Route ID"), max_length=50, unique=True)
    routename = models.CharField(_("Route Name"), max_length=50)
    stop1 = models.CharField(_("Stop 1"), max_length=50)
    stop2 = models.CharField(_("Stop 2"), max_length=50)
    stop3 = models.CharField(_("Stop 3"), max_length=50, null=True,blank=True)
    stop4 = models.CharField(_("Stop 4"), max_length=50, null=True,blank=True)
    stop5 = models.CharField(_("Stop 5"), max_length=50, null=True,blank=True)
    stop6 = models.CharField(_("Stop 6"), max_length=50, null=True,blank=True)
    stop7 = models.CharField(_("Stop 7"), max_length=50, null=True,blank=True)
    stop8 = models.CharField(_("Stop 8"), max_length=50, null=True,blank=True)
    stop9 = models.CharField(_("Stop 9"), max_length=50, null=True,blank=True)
    stop10 = models.CharField(_("Stop 10"), max_length=50, null=True,blank=True)
    stop11 = models.CharField(_("Stop 11"), max_length=50, null=True,blank=True)
    stop12 = models.CharField(_("Stop 12"), max_length=50, null=True,blank=True)
    stop13 = models.CharField(_("Stop 13"), max_length=50, null=True,blank=True)
    stop14 = models.CharField(_("Stop 14"), max_length=50, null=True,blank=True)
    stop15 = models.CharField(_("Stop 15"), max_length=50, null=True,blank=True)
    
    def __str__(self):
        return self.routename

class TripDetails(models.Model):
    tripid = models.CharField(_("Trip ID"),unique=True)
    tripname = models.ForeignKey(RouteDetails, on_delete=models.CASCADE)
    vehicleregno = models.ForeignKey(VehicleDetails, on_delete=models.CASCADE)
    driverid = models.ForeignKey(DriverDetails, on_delete=models.CASCADE)
    gpsdeviceserialno = models.ForeignKey(GPSDeviceDetails, on_delete=models.CASCADE)
    tripsourceplace = models.CharField(_("Trip Source Place"), max_length=50)
    tripstarttime = models.TimeField(_("Trip Start Time"), auto_now=False, auto_now_add=False)
    tripdestinationplace = models.CharField(_("Trip Destination Place"), max_length=50)
    tripendtime = models.TimeField(_("Trip End Time"), auto_now=False, auto_now_add=False)
    tripstate = models.CharField(_("Trip State"), max_length=50)

    def __str__(self):
        return self.tripname
    
class SubscriptionMode(models.Model):
    subscripmode = models.CharField(_("Subscription Status Mode"), max_length=50, unique=True)
    def __str__(self):
        return self.subscriptionmode
    
class SubscriptionDetails(models.Model):
    CHOICES = (
        ('Day', 'Day'),
        ('Week', 'Week'),
        ('Month', 'Month'),
        ('Year','Year')
    )
    devicesrno = models.ForeignKey(GPSDeviceDetails, on_delete=models.CASCADE)
    subscriptioncode = models.CharField(_("Subscription Code"), max_length=50, unique=True)
    durationno = models.IntegerField(_("Duration in Numbers"), default=0)
    durationperiod =models.CharField(_("Duration Period"),choices=CHOICES, max_length=50)
    expireson = models.DateTimeField(_("Expires On"), auto_now=False, auto_now_add=False)
    createdat = models.DateTimeField(_("Created At"),auto_now=False, auto_now_add=True)
    updatedat = models.DateTimeField(_("Updated At"), auto_now=True, auto_now_add=False)
    subscriptionstatus = models.ForeignKey(SubscriptionMode, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subscriptionstatus