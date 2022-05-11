from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView

from .forms import UserForm

def index(request):
    return render(request, 'index.html', {})

class Register(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = UserForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect('index')

        return render(request, 'register.html', {'form': form})

class User_login(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        form = UserForm()
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password')) 
        if user:
            login(request, user) 
            return redirect('index')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')