from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render  #, HttpResponse
from django.views import View

from .models import (
    GPSDeviceDetails,
    GPSDeviceStatus,
    UserProfile,
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
        user = request.user.username
        loginuser = User.objects.get(username=user)
        userid = int(loginuser.id) + 1
        #print(userid)
        #userid=2
        loginvendor = VendorProfile.objects.get(user=userid)
        #print(loginvendor.vendorid)
        
        vehicletotalregnolist = []
        vehiclelistquery = VehicleDetails.objects.filter(vendorid=loginvendor.vendorid)
        print(vehiclelistquery)
        for vehiclelist in vehiclelistquery:
            vehicletotalregnolist.append(vehiclelist.vehicleregno)
        print("total registration no :",vehicletotalregnolist)
            
        
        vehicletotalcount = len(vehiclelistquery)
        print(vehicletotalcount)
        
        gpsdevicelist = []
        for vehiclename in vehiclelistquery:
            query = GPSDeviceDetails.objects.filter(vehiclename = vehiclename)
            for gps_device in query:
                gpsdevicelist.append(gps_device.deviceserialno)
        
        print("GPS Device Found : " ,gpsdevicelist)
        totalgpsdeviceserialno = len(gpsdevicelist)
        
        
        
        #gpsdevicedetailsquery = GPSDeviceDetails.object.filter()
        context = {
            'user': user, 'totalvehicle':vehicletotalcount, 'vehicletotalregnolist':vehicletotalregnolist, 
            'totalgpsdevice':totalgpsdeviceserialno, 'gpsdevicelist':gpsdevicelist,
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