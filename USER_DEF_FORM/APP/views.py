from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def user_form(request):
    data=user_forms()  # user_forms  is the class in forms.py
    if request.method =='POST':
         
        form=user_forms(request.POST)# here it check user_forms is post,if then it store to form variable 
        if form.is_valid(): 
            roll=form.cleaned_data['roll'] #['roll'] is from forms.py
            name=form.cleaned_data['name']  #cleaned _data using do get values only from form then other tags etc in form are removed
            mark=form.cleaned_data['mark']
            d=forms.objects.create(roll=roll,name=name,mark=mark)
            d.save()

            
    return render(request,'index.html',{'data':data})