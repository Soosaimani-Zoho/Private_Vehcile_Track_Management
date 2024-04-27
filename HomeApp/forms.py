from django import forms
from .models import VehicleDetails

class vehicledetailsform(forms.ModelForm):
    class Meta:
        model = VehicleDetails
        fields = "__all__"
