from django import forms
from .models import VehicleDetails

class vehicledeailsform(forms.ModelForm):
    class Meta:
        model = VehicleDetails
        fields = "__all__"
