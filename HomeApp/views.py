from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render  , HttpResponse
from django.views import View
from django.views.generic import ListView
import datetime
from datetime import date
from datetime import datetime
import json
from django.contrib import messages

#-------------------API Imports---------------------------------------------------
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import VendorProfilesSerializer, UserProfileSerializer
from rest_framework import status
#-------------------API Imports---------------------------------------------------

from .models import (
                    GPSDeviceDetails,
                    GPSDeviceStatus,
                    UserProfile,
                    VehicleDetails,
                    VendorProfile,
                    DriverDetails,
                    RouteDetails,
                    SubscriptionDetails
    
                    )

from .forms import vehicledetailsform, DriverdetailsForm, RouteDetailsForm

vehicle_reg_numbers = VehicleDetails.get_vehicleregno_list()  # to get vechile regno list from db
#loingid = UserProfile.loginid(request)


def get_login_user_id(request):
    # Get the username of the logged-in user
    username = request.user.username
    # Find the logged-in user object
    login_user = User.objects.get(username=username)
    # Return the ID of the logged-in user
    return login_user.id

def get_vendor_name(userid,request):
    try:
        #global loginvendor
        loginvendor = VendorProfile.objects.get(user=userid)
        print("loginvendor", loginvendor)
        return loginvendor
    except:
        return render(request,'all_vehicle.html', {'error':'Profile Not Found'})

def get_vehicle_list(loginvendor):
    vehicletotalregnolist = []
    vehiclesubscriptionlist=[]
    global vehiclelistquery
    vehiclelistquery = VehicleDetails.objects.filter(vendorid=loginvendor.vendorid)
    print(vehiclelistquery)
    for vehicle in vehiclelistquery:
        vehicletotalregnolist.append(vehicle.vehicleregno)
    print("total registration no :",vehicletotalregnolist)
    return vehicletotalregnolist
    pass

def gps_device_list():    
    pass
    
#----------------------API- Views--------------------------VVVVVV--------------------------------------------------------------------
class API_VendorProfiles(APIView):
    
    def get(self, request):
        try:
            queryset = VendorProfile.objects.all()
            serialized_data = VendorProfilesSerializer(queryset, many=True)
            return Response(serialized_data.data)
        except Exception as e:
            # Print detailed error message for debugging
            print("Serialization Error:", e)
            # Return an appropriate response indicating a server error
            return Response({"error": "An error occurred during serialization."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self, request):
        pass

class API_VehicleDetails(APIView):    
    def get(self, request):
        try:
            queryset = VendorProfile.objects.all()
            serialized_data = VendorProfilesSerializer(queryset, many=True)
            return Response(serialized_data.data)
        except Exception as e:
            # Print detailed error message for debugging
            print("Serialization Error:", e)
            # Return an appropriate response indicating a server error
            return Response({"error": "An error occurred during serialization."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self, request):
        pass
    
    
class API_VendorProfiles(APIView):
    
    def get(self, request):
        try:
            queryset = VendorProfile.objects.all()
            serialized_data = VendorProfilesSerializer(queryset, many=True)
            return Response(serialized_data.data)
        except Exception as e:
            # Print detailed error message for debugging
            print("Serialization Error:", e)
            # Return an appropriate response indicating a server error
            return Response({"error": "An error occurred during serialization."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self, request):
        pass

class API_VeihleDetails(APIView):    
    def get(self, request):
        try:
            queryset = VendorProfile.objects.all()
            serialized_data = VendorProfilesSerializer(queryset, many=True)
            return Response(serialized_data.data)
        except Exception as e:
            # Print detailed error message for debugging
            print("Serialization Error:", e)
            # Return an appropriate response indicating a server error
            return Response({"error": "An error occurred during serialization."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self, request):
        pass
#----------------------API- Views-------------------^^^^^-----------------------------------------------------------------------------






class HomeApp(View):
    def get(self, request):
        #return HttpResponse("welcome")
        return render(request, 'gotoz\index.html')
    
class all_vehicle(View):
    
    def get(self, request):
        #---------------------------------get login user------------------
        user = request.user.username
        #---------------------------------find loginuser ID-----------
        #loginuser = User.objects.get(username=user)
        userid = int(get_login_user_id(request))
        login_vendor_list = VendorProfile.objects.all()
        #print('Login vendor list:')
        '''for vendor_profile in login_vendor_list:
            print(vars(vendor_profile))'''
        #print(userid)
        #userid=2
        #---------------------------------find login vendor name by ID-------
        '''try:
            loginvendor = VendorProfile.objects.get(user=userid)
            #print(loginvendor.vendorid)
        except:
            return render(request,'all_vehicle.html', {'error':'Profile Not Found'})'''
        loginvendor = get_vendor_name(userid, request)
        #--------------------------------
        '''vehicletotalregnolist = []
        vehiclesubscriptionlist=[]
        vehiclelistquery = VehicleDetails.objects.filter(vendorid=loginvendor.vendorid)
        print(vehiclelistquery)
        for vehiclelist in vehiclelistquery:
            vehicletotalregnolist.append(vehiclelist.vehicleregno)
        print("total registration no :",vehicletotalregnolist)'''
        vehicletotalregnolist = get_vehicle_list(loginvendor)
        
        #print("vehicletotalregnolist",vehicletotalregnolist)
        
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
        
        context={
            'vechileregnolists':vehicletotalregnolist,
            'all':len(vehicletotalregnolist),
            
        }
        return render(request,'all_vehicle.html', context)
        
        
            
        
        '''vehicletotalcount = len(vehiclelistquery)
        print(vehicletotalcount)
        
        
        
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
        
        
        #print("Latitude 1:", latitude_list[0], "Longitude 1:", longitude_list[0])
        #print("Latitude 2:", latitude_list[1], "Longitude 2:", longitude_list[1])
        #print("Latitude 3:", latitude_list[2], "Longitude 3:", longitude_list[2])
        #print(coordinates)
        
        for key,value in gps_data.items():
            if 'moving' in value:
                move_value = value['moving']
                if True in move_value:
                    movecounttrue += 1'''
'''                elif False in move_value:
                    movecountfalse += 1'''
'''            if 'stopped' in value:
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
        }'''
        
    
    
class vehicle_directory(View):
    def get(self, request):
        user = request.user.username
        userid = int(get_login_user_id(request))
        loginvendor = get_vendor_name(userid, request)
        vehicletotalregnolist = get_vehicle_list(loginvendor) 
        
        context = {
            'vechiledetails':vehiclelistquery
        }
        return render(request,'vehicle_directory.html',context)
    def post(self,request):
        vehicle_id = request.POST.get('vehicleid')
        print('Vehicle ID:', vehicle_id)
        vehicle = VehicleDetails.objects.get(id=vehicle_id)
        context = {
        'vehiclename' : vehicle.vehiclename,
        'vehicleregno' : vehicle.vehicleregno,
        'vehicletype' : vehicle.vehicletype,
        'vehicleimage' : vehicle.vehicleimage,
        'odometerreading' : vehicle.odometerreading,
        'vehiclemake' : vehicle.vehiclemake,
        'modelyear' : vehicle.modelyear,
        'chessisno' : vehicle.chessisno,
        
        'expectmileage' :vehicle.expectmileage,
        'isdelete' : vehicle.isdelete
        }
            
        

        return render(request,'vehicle_directory_edit.html',context)

class vehicle_directory_add(View):
    def get(self, request):
        user = request.user.username
        userid = int(get_login_user_id(request))
        loginvendor = get_vendor_name(userid, request)
        print("loginvendor",loginvendor)
        
        form = vehicledetailsform()
        
        return render(request, 'vehicle_directory_add.html',{'form':form, 'loginvendor':loginvendor})
        pass
    
    def post(self,request):        
        form = vehicledetailsform(request.POST,request.FILES)
        try:
            form.is_valid()
            form.save()
            messages.success(request,"Your Vehicle Details saved Successfully")
        except Exception as e:
            # Print detailed error message for debugging
            print("Form save Error:", e)
            form = vehicledetailsform()
            messages.info(request, "{}".format(e))
        return render(request, 'vehicle_directory_add.html', {'form': form})
        

class vehicle_group(View):
    def get(self, request):
        return render(request,'vehicle_group.html')
    
class vehicle_states(View):
    def get(self, request):
        return render(request,'vehicle_states.html')

class my_driver(View):
    def get(self, request):
        driverdetails = DriverDetails.objects.all()
        #print(driverdetails)
        context = {
            'driverdetails':driverdetails,
        }
        return render(request,'my_driver.html',context)

class my_driver_add(View):
    def get(self, request):
        form = DriverdetailsForm()
        return render(request, 'my_driver_add.html',{'form':form})
    def post(self, request):
        form = DriverdetailsForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the form data into the database
            messages.success(request,"Your Details saved Successfully")
            print("Form saved successfully")
        else:
            print("not valid")
            messages.error(request,"Not valid Details.")
        return render(request, 'my_driver_add.html', {'form':form})
  
class all_trips(View):
    def get(self, request):
        return render(request,'all_trips.html')
    
class trip_schedules(View):
    def get(self, request):
        return render(request, 'trip_schedules.html')

class routes(View):
    
    def get(self,request):
        routedetails = RouteDetails.objects.all()
        context = {
            'allroutedetails':routedetails
        }
        return render(request,'routes.html',context)

class routes_add(View):
    def get(self, request):
        form = RouteDetailsForm()        
        return render(request, 'routes_add.html',{'form':form})
    def post(self, request):
        form = RouteDetailsForm(request.POST)
        if form.is_valid():
            #selection = form.cleaned_data['selection'] #need to customise to clean form afte save. now no time.
            form.save()
            print("Route Details Added")
        else:
            errors = form.errors
            print("Form not valid error is :", errors)
        return render(request,'routes_add.html',{'form':form})
        
        
    
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
    

class subscription_history(ListView):
    model = SubscriptionDetails
    template_name = 'subscription_history.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscription_details'] = SubscriptionDetails.objects.all()
        #context['another_model_data'] = AnotherModel.objects.all() #if need to add another model.
        return context
    
class subscription_renew(View):
    template_name = 'subscription_renew.html'
    def get(self, request):
        return render(request, self.template_name)