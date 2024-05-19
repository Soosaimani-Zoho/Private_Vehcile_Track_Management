from django import forms
from .models import VehicleDetails, DriverDetails, CountryCodeDetails, RouteDetails, VendorProfile, vehiclemake

class vehicledetailsform(forms.ModelForm):
    vendorid = forms.ModelChoiceField(queryset=VendorProfile.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    vehiclename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Name'}))
    vehicleregno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Registration Name'}))
    vehicletype = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Type'}))
    vehicleimage = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),required=False)
    odometerreading = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Odometer Reading'}))
    vehiclemake = forms.ModelChoiceField(queryset=vehiclemake.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    modelyear = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Name'}))
    chessisno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Chessis Number'}))    
    expectmileage = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Expected Mileage'}))
    
    class Meta:
        model = VehicleDetails
        fields = "__all__"

from django.forms import formset_factory

class StopnameForm(forms.Form):
    stopname = forms.CharField(max_length=100)

StopFormSet = formset_factory(StopnameForm, extra=1)  # You can set extra to control the number of initial forms

class DriverdetailsForm(forms.ModelForm):
    drivername = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Driver Name'}))
    phoneno1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone No.1'}))
    phoneno2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone No.2(Optional)'}))
    #vehicleregno = forms.ModelChoiceField(queryset=VehicleDetails.objects.values_list('vehicleregno', flat=True), empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    vehicleregno = forms.ModelChoiceField(queryset=VehicleDetails.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    licenseno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Driver License No.'}))
    guarantorname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guarantor Name'}))
    guarandorphoneno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guarantor  Phone No.'}))
    countrycode = forms.ModelChoiceField(queryset=CountryCodeDetails.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    aadharno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Aadhar No'}))
    licenseissuedate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    licenseexpirtydate =  forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    driverid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Driver ID as Unique'}))
    driverimage = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),required=False)
    pancardimage = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),required=False)
    driverlicense =forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),required=False)
    drivermisc =forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),required=False)
    
    class Meta:
        model = DriverDetails
        fields = "__all__"

class RouteDetailsForm(forms.ModelForm):
    routeid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Unique Route ID.'}))
    routename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Route Name.'}))
    stop1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name1'}))
    stop2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name2'}))
    stop3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name3'}),required=False)
    stop4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name4'}),required=False)
    stop5 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name5'}),required=False)
    stop6 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name6'}),required=False)
    stop7 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name7'}),required=False)
    stop8 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name8'}),required=False)
    stop9 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name9'}),required=False)
    stop10 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name10'}),required=False)
    stop11 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name11'}),required=False)
    stop12 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name12'}),required=False)
    stop13 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name13'}),required=False)
    stop13 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name13'}),required=False)
    stop14 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name14'}),required=False)
    stop15 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stop Name15'}),required=False)
    
    class Meta:
        model = RouteDetails
        fields = "__all__"