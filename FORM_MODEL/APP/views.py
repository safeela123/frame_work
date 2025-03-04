from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def user_form(request):
    data=model_form()

    if request.method=='POST':
        form=model_form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'data':data})
 