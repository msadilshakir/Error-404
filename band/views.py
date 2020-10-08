from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def base(request):
    return render(request,'base.html')

def admin(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.error(request,'Successfully Logged IN')
            return render(request,'user.html',{'user':user})
            
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/') 

    else:
        return render(request,'base.html')        


def logout(request):
    auth.logout(request)
    return redirect('/')

def user(request):
    return render(request,'user.html')
    