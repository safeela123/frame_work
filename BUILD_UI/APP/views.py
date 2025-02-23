from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def add_data(request):

    datas=ui.objects.all()
    if request.method == 'POST':
        text=request.POST['type']
        data=ui.objects.create(text=text)
        data.save()

        
    return render(request,'main.html',{'datas':datas})

def update(request,pk):
    data=ui.objects.get(pk=pk)
    # print(data)
    if request.method=='POST':
        text=request.POST['text']
        ui.objects.filter(pk=pk).update(text=text)
        return redirect(add_data)
    return render(request,'update.html',{'data':data})

def delete(request,pk):
    ui.objects.filter(pk=pk).delete()

    return redirect(add_data)



