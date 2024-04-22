# Generated by Django 5.0.4 on 2024-04-22 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0002_alter_gpsdevicedetails_deviceserialno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCodeDetails',
            fields=[
                ('countryname', models.CharField(max_length=25, verbose_name='Vendor Country Name')),
                ('countrycode', models.IntegerField(max_length=4, primary_key=True, serialize=False, verbose_name='Country Code')),
            ],
        ),
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorname', models.CharField(max_length=50, verbose_name='Vendor name')),
                ('vendoraddress', models.TextField(verbose_name='Vendor Address')),
                ('vendormob1', models.IntegerField(unique=True, verbose_name='Vendor Mobile no_1')),
                ('vendormob2', models.IntegerField(verbose_name='Vendor Mobile no_2')),
                ('vendordistrict', models.CharField(max_length=50, verbose_name='Vendor District')),
                ('vendorcountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.countrycodedetails')),
            ],
        ),
    ]
