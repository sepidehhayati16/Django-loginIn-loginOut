from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    messages.success(request,'You are now logout')
    return redirect('login')