# Generated by Django 5.0.4 on 2024-04-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehiclegroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=50, verbose_name='Vehicle Group Name')),
                ('vehicleregnolist', models.TextField(verbose_name='Vehicle Reg No list as json')),
            ],
        ),
    ]
