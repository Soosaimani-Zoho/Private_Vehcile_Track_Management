from django.shortcuts import render  #, HttpResponse
from django.views import View

class Login(View):
    def get(self, request):
        #return HttpResponse("welcome")
        return render(request, 'login.html')


class HomeApp(View):
    def get(self, request):
        #return HttpResponse("welcome")
        return render(request, 'index.html')
    
class all_vehicle(View):
    def get(self, request):
        return render(request,'all_vehicle.html')
    
    
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