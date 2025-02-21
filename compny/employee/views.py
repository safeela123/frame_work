from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
l=[]
def job(request):
    if request.method =='POST':
        a=int(request.POST['no'])
        b=request.POST['name']
        c=int(request.POST['age'])
        d=request.POST['mail']
        e=request.POST['position']
        f=int(request.POST['year'])
        print(a,b,c,d,e,f)
        l.append({'id':a,'name':b,'age':c,'mail':d,'position':e,'experience':f})

    return render(request,'employment.html',{'data1':l})

def update(request,id):
    data=0
    for i in l:
            if id==i['id']:
                data=i
    if request.method =='POST':
        
        a1=int(request.POST['id'])
        b2=request.POST['name']
        c3=int(request.POST['age'])
        d4=request.POST['email']
        e5=request.POST['position']
        f6=int(request.POST['experience'])
        for i in l:
            if id==i['id']:
                i['id']=a1
                i['name']=b2
                i['age']=c3
                i['mail']=d4
                i['position']=e5
                i['experience']=f6
                return redirect(job)
    return render(request,'update.html',{'data':data})

def delete(request,id):
    data2=0
   
    for i in l:
        if id == i['id']:
            data2=i
            l.remove(data2)
            return redirect(job)
    
    return render(request,'delete.html',{'data':data2})

