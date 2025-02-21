from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return render (request,'puma_women.html')

