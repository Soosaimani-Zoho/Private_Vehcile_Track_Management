from django import forms
from .models import VehicleDetails

class vehicledetailsform(forms.ModelForm):
    class Meta:
        model = VehicleDetails
        fields = "__all__"

from django.forms import formset_factory

class StopnameForm(forms.Form):
    stopname = forms.CharField(max_length=100)

StopFormSet = formset_factory(StopnameForm, extra=1)  # You can set extra to control the number of initial forms