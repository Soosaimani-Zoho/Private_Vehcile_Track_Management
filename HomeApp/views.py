from django.shortcuts import render  #, HttpResponse
from django.views import View


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