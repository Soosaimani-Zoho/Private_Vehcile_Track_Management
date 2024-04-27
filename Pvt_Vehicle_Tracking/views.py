from django.views import View
from django.shortcuts import redirect, render  , HttpResponse
from django.contrib.auth import authenticate, login, logout


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
            return redirect('gotoz/')
        else:
            return render(request, 'login.html', {'error':'Invalid Username and Password'})

def logout_view(request):
    logout(request)
    return redirect('Login')