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
            data=User.objects.create_user(first_name=name,email=email,username=uname,password=psw) # User is imported User
            data.save() # here first name,username,email etc are from auth_user table
            return redirect(Userlogin)
        else:
            print('password doesnt match')
    return render(request,'register.html')
def Userlogin(request):
    if request.method=='POST': 
        name=request.POST['uname']
        psw=request.POST['psw']
        user=auth.authenticate(username=name,password=psw) #auth.authenticate() checks if a user with the given username and password exists in the database.
                                                            # If valid, it returns the user object.
                                                            # If invalid, it returns None.
        if user is not None:
            auth.login(request,user)  #If authentication is successful (user is not None), Django logs in the user and 
                                        #redirects them to the index page.
            return redirect(index)
    return render(request,'login.html') # Renders the login page if authentication fails

def index(request):
    if request.user.is_authenticated: # request.user.is_authenticated is True if the user is logged in.
        context = {'loguser': request.user}    #Passes the logged-in user’s details to index.html for display.

     
        return render(request,'index.html',context)
    else:
            return redirect(Userlogin) # Redirects to login page if the user is not logged in
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(Userlogin)
    else:
        return redirect(Userlogin)