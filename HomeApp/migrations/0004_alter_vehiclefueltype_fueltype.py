# Generated by Django 5.0.2 on 2024-04-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0003_alter_vehicledetails_vehiclemake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclefueltype',
            name='fueltype',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Vehicle Fuel Type'),
        ),
    ]
