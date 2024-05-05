from rest_framework import serializers
from .models import VendorProfile,UserProfile,CountryCodeDetails
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user']

class CountryCodeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryCodeDetails
        fields = '__all__'  # Adjust fields as needed


class VendorProfilesSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    #user = UserProfileSerializer() #--> Alternatively used not tested suggest by GPT
    #vendorcountry = serializers.PrimaryKeyRelatedField(queryset=CountryCodeDetails.objects.all())
    #vendorcountry = CountryCodeDetailsSerializer()
    class Meta:
        model = VendorProfile
        fields = '__all__'

