from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def management(request):
    datas=students.objects.all()  #it for show output in browser page
    # print(datas)
    
    if request.method =='POST':
        a=int(request.POST['no'])
        b=request.POST['name']
        c=int(request.POST['age'])
        d=request.POST['mail']
        e=int(request.POST['class'])
        f=request.POST['sub']
        # print(a,b,c,d,e,f)
        data=students.objects.create(ad_no=a,name=b,age=c,mail=d,cls=e,subject=f)
        data.save()

    return render(request,'main.html',{'datas':datas})

def update(request,pk):
    data=students.objects.get(pk=pk) #first pk is pk of database,other is of fn
    print(data)
    if request.method=='POST':
        no=int(request.POST['no'])
        name=request.POST['name']
        age=int(request.POST['age'])
        email=request.POST['mail']
        cls=int(request.POST['class'])
        subject=request.POST['sub']
        students.objects.filter(pk=pk).update(ad_no=no,name=name,age=age,mail=email,cls=cls,subject=subject)
   
        return redirect(management)

    return render(request,'update.html',{'data':data})

def delete(request,pk):
    students.objects.filter(pk=pk).delete()
    
  
    return redirect(management)

 