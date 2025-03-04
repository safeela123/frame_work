from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def user_form(request):
    data=user_forms()
    if request.method=='POST':
        form=user_forms(request.POST)
        if form.is_valid():
            
