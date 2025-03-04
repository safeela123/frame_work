from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    dnames=Department.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        dpk=request.POST['dname']
        dname=Department.objects.get(pk=dpk)
        data=Student.objects.create(name=name,age=age,email=email,dname=dname) # first name,age,email,dname are of from models.py
        data.save()
        return redirect(see_all)
    return render(request,'index.html',{'dnames':dnames})

def see_all(request):
    dnames=Department.objects.all()
    sts=Student.objects.all()
    if request.method=='POST':
        dpk=request.POST['dname']
        dname=Department.objects.get(pk=dpk)
        sts=Student.objects.filter(dname=dname)
    return render(request,'see_all.html',{'dnames':dnames,'sts':sts})
        