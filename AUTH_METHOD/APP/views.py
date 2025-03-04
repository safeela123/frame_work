from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth

# Create your views here.
def UserReg(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        uname=request.POST['username']
        psw=request.POST['password']
        cnf_psw=request.POST['cnf_password']
        if cnf_psw==psw:
            data=User.objects.create_user(first_name=name,email=email,username=uname,password=psw)
            data.save()
            return redirect(Userlogin)
        else:
            print('password doesnt match')
    return render(request,'register.html')
def Userlogin(request):
    if request.method=='POST':
        name=request.POST['uname']
        psw=request.POST['psw']
        user=auth.authenticate(username=name,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect(index)
    return render(request,'login.html')

def index(request):
    if request.user.is_authenticated:
        context = {'user': request.user}

     
        return render(request,'index.html',{'value':context})
    else:
            return redirect(Userlogin)
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(Userlogin)
    else:
        return redirect(Userlogin)