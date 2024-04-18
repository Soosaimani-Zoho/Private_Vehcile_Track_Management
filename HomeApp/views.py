from django.shortcuts import render  #, HttpResponse
from django.views import View


class HomeApp(View):
    def get(self, request):
        #return HttpResponse("welcome")
        return render(request, 'index.html')
# Create your views here.
