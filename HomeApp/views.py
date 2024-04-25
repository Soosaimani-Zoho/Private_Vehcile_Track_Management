from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render  #, HttpResponse
from django.views import View
import datetime
from datetime import date
from datetime import datetime
import json

from .models import (
    GPSDeviceDetails,
    GPSDeviceStatus,
    #UserProfile,
    VehicleDetails,
    VendorProfile,
)


class Login(View):
    def get(self, request):
        #return HttpResponse("welcome")
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("User Found")
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error':'Invalid Username and Password'})

def logout_view(request):
    logout(request)
    return redirect('Login')


class HomeApp(View):
    def get(self, request):
        #return HttpResponse("welcome")
        return render(request, 'index.html')
    
class all_vehicle(View):
    
    def get(self, request):
        #---------------------------------login user------------------
        user = request.user.username
        #---------------------------------find loginuser ID-----------
        loginuser = User.objects.get(username=user)
        userid = int(loginuser.id)
        #print(userid)
        #userid=2
        #---------------------------------find login vendor name by ID-------
        try:
            loginvendor = VendorProfile.objects.get(user=userid)
            #print(loginvendor.vendorid)
        except:
            return render(request,'all_vehicle.html', {'error':'Profile Not Found'})
        
        #--------------------------------
        vehicletotalregnolist = []
        vehiclesubscriptionlist=[]
        vehiclelistquery = VehicleDetails.objects.filter(vendorid=loginvendor.vendorid)
        print(vehiclelistquery)
        for vehiclelist in vehiclelistquery:
            vehicletotalregnolist.append(vehiclelist.vehicleregno)
        print("total registration no :",vehicletotalregnolist)
        
        
        
            
        
        vehicletotalcount = len(vehiclelistquery)
        print(vehicletotalcount)
        
        gpsdevicelist = []
        gpsdeviceidlist = []
        gpssubscriptionlist=[]
        for vehiclename in vehiclelistquery:
            query = GPSDeviceDetails.objects.filter(vehiclename = vehiclename)
            for gps_device in query:
                #print(gps_device.id)
                gpsdevicelist.append(gps_device.deviceserialno)
                gpsdeviceidlist.append(gps_device.id)
                gpssubscriptionlist.append(gps_device.expiredat)
        
        [print(date_obj.date()) for date_obj in gpssubscriptionlist]
        #print(dates)
        times = [date_obj.time() for date_obj in gpssubscriptionlist]
        
        today = datetime.now()
        devregwithsubexpirty = [(regno, subscription_date, today) for regno, subscription_date in zip(vehicletotalregnolist, gpssubscriptionlist)]
        print(devregwithsubexpirty)

        #print("Dates:", dates)
        #print("Times:", times)
        
        print("GPS Device Found : " ,gpsdevicelist)
        print("ID is :", gpsdeviceidlist)
        totalgpsdeviceserialno = len(gpsdevicelist)
        print("gps subscription date",gpssubscriptionlist)
        
        
        #gpsdevicestatuslist =[]
        gps_data = {}

        for gpsdevice in gpsdeviceidlist:
            query = GPSDeviceStatus.objects.filter(deviceserialno=gpsdevice)
            gps_data[gpsdevice] = {
                'moving': [],
                'stopped': [],
                'idlling': [],
                'offline': [],
                'subsexpired': [],
                'ignition': [],
                'gpssignal': [],
                'speed': [],
                'orientationvalue': [],
                'deviceexternalpower': [],
                'location': [],
                'temperature': [],
                'internalbatterypower': [],
                'movmentvalue': [],
                'gsmstrength': [],
                'lat': [],
                'long': [],
            }
            
            for gpsstatus in query:
                gps_data[gpsdevice]['moving'].append(gpsstatus.moving)
                gps_data[gpsdevice]['stopped'].append(gpsstatus.stopped)
                gps_data[gpsdevice]['idlling'].append(gpsstatus.idlling)
                gps_data[gpsdevice]['offline'].append(gpsstatus.offline)
                gps_data[gpsdevice]['subsexpired'].append(gpsstatus.subsexpired)
                gps_data[gpsdevice]['ignition'].append(gpsstatus.ignition)
                gps_data[gpsdevice]['gpssignal'].append(gpsstatus.gpssignal)
                gps_data[gpsdevice]['speed'].append(gpsstatus.speed)
                gps_data[gpsdevice]['orientationvalue'].append(gpsstatus.orientationvalue)
                gps_data[gpsdevice]['deviceexternalpower'].append(gpsstatus.deviceexternalpower)
                gps_data[gpsdevice]['location'].append(gpsstatus.location)
                gps_data[gpsdevice]['temperature'].append(gpsstatus.temperature)
                gps_data[gpsdevice]['internalbatterypower'].append(gpsstatus.internalbatterypower)
                gps_data[gpsdevice]['movmentvalue'].append(gpsstatus.movmentvalue)
                gps_data[gpsdevice]['gsmstrength'].append(gpsstatus.gsmstrength)
                gps_data[gpsdevice]['lat'].append(gpsstatus.lat)
                gps_data[gpsdevice]['long'].append(gpsstatus.long)
        gpsdata_json = json.dumps(gps_data)
        #print(gps_data)
        #print(gps_data.get(1)) 
        #print(gps_data.get(2))
        #print(gps_data.get(1).get('moving'))
        movecounttrue= 0
        movecountfalse=0
        stopcountertrue=0
        idllingcountertrue=0
        offlinecountertrue=0
        #nodevicecountertrue=0
        subscripexpcountertrue=0
        latitude_list = []
        longitude_list = []
        location_list =[]
        
        for key, value in gps_data.items():            
            latitude_list.append(value['lat'][0])            
            longitude_list.append(value['long'][0])
            location_list.append(value['location'][0])
        coordinates = zip(latitude_list, longitude_list,vehicletotalregnolist,latitude_list,longitude_list, location_list) # now its create as object
        
        
        print("Latitude 1:", latitude_list[0], "Longitude 1:", longitude_list[0])
        print("Latitude 2:", latitude_list[1], "Longitude 2:", longitude_list[1])
        print("Latitude 3:", latitude_list[2], "Longitude 3:", longitude_list[2])
        #print(coordinates)
        
        for key,value in gps_data.items():
            if 'moving' in value:
                move_value = value['moving']
                if True in move_value:
                    movecounttrue += 1 
                '''elif False in move_value:
                    movecountfalse += 1'''
            if 'stopped' in value:
                stop_value = value['stopped']
                if True in stop_value:
                    stopcountertrue += 1
            if 'idlling' in value:
                idle_value = value['idlling']
                if True in idle_value:
                    idllingcountertrue += 1
            if 'offline' in value:
                offline_value = value['offline']
                if True in offline_value:
                    offlinecountertrue += 1
            if 'subsexpired' in value:
                subexpir_value = value['subsexpired']
                if True in subexpir_value:
                    subscripexpcountertrue += 1
            
                
        
        
        #print(movecounttrue)
        #print(stopcountertrue)
        #print(movecountfalse)
        #print(gpsdevicestatuslist)
        #print(query)
        #gpsdevicedetailsquery = GPSDeviceDetails.object.filter()
        context = {
            'user': user, 'totalvehicle':vehicletotalcount, 'vehicletotalregnolist':vehicletotalregnolist, 
            'totalgpsdevice':totalgpsdeviceserialno, 'gpsdevicelist':gpsdevicelist,'gpsdata': gps_data,
            'moving':movecounttrue,'stopped':stopcountertrue,'idlling':idllingcountertrue,'offline':offlinecountertrue,
            'subscriptionexpired':subscripexpcountertrue, 'regnowithexpiry':devregwithsubexpirty, 'devicelatlist':latitude_list,
            'devicelonglisst':longitude_list, 'gpscoordinates':coordinates
        }
        return render(request,'all_vehicle.html', context)
    
    
class vehicle_directory(View):
    def get(self, request):
        return render(request,'vehicle_directory.html')

class vehicle_group(View):
    def get(self, request):
        return render(request,'vehicle_group.html')
    
class vehicle_states(View):
    def get(self, request):
        return render(request,'vehicle_states.html')
    
class all_trips(View):
    def get(self, request):
        return render(request,'all_trips.html')
    
class trip_schedules(View):
    def get(self, request):
        return render(request, 'trip_schedules.html')
class routes(View):
    def get(self,request):
        return render(request,'routes.html')
    
class consigners(View):
    def get(self, request):
        return render(request,'consigners.html')
    
class my_expances(View):
    def get(self, request):
        return render(request,'my_expances.html')
    



class service_history(View):
    def get(self,request):
        return render(request, 'service_history.html')
    
class service_schedules(View):
    def get(self,request):
        return render(request,'service_schedules.html')
