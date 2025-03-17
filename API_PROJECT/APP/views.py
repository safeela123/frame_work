from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import *
from .models import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def fun(request):
#     return JsonResponse({'name':'safeela','age':'14'})

# def fun2(request):    # it is user defined sterilizer
#     if request.mthod=='GET':
#         d=student.objects.all()
#         s=sample(d,many=True)  # sample is serializers class and many for send serializers more value, if it is false it send only single value
#         return JsonResponse(s.data,safe=False)

@csrf_exempt
def fun3(request):
    if request .method=='GET':
        data=student.objects.all()
        s=model_serializers(data,many=True)
        return JsonResponse(s.data,safe=False)
    elif request.method =='POST':
        d=JSONParser().parse(request)
        s=model_serializers(data=d) # model name in serializers.py is model_serializers
        print(s)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,safe=False)
        else:
            return JsonResponse(s.errors)

@csrf_exempt
def fun4(request,d):
    try:
        demo=student.objects.get(pk=d)
    except:
        return HttpResponse("invalid")
    if request.method=='GET':
        s=model_serializers(demo)
        return JsonResponse(s.data)
    if request.method=='PUT':
        d=JSONParser().parse(request)
        s=model_serializers(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif request.method=='DELETE':
        demo.delete()
        return HttpResponse('deleted')