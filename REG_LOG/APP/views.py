from django.shortcuts import render,redirect
from .models import *
def userReg(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        uname=request.POST['uname']
        psw=request.POST['password']
        cnf_psw=request.POST['cnf_password']
        if cnf_psw==psw:
            data=Users.objects.create(name=name,email=email,uname=uname,psw=psw)
            data.save()
            return redirect(userlogin)
        else:
            print('password doesnt match')
    return render (request,'register.html')

def userlogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        try:
            data=Users.objects.get(psw=psw,uname=uname)
            request.session['user']=uname
            #
            request.session['user1']=psw
            return redirect(index)
        except:
            return redirect(userlogin)
    return render(request,'login.html')

def index(request):
    if 'user' in request.session:
        print(request.session['user'])
        user=Users.objects.get(uname=request.session['user'],psw=request.session['user1'])
        print(user)
        return render (request,'index.html',{'user':user})
    else:
        return redirect(userlogin)
    
def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect(userlogin)
    else:
        return redirect()


# Create your views here.
