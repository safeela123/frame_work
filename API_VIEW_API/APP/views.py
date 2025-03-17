from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import *
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins

# Create your views here.
@api_view(['GET','POST'])
def fun1(req):
    if req.method=='GET':
        d=student.objects.all()
        s=model_serializers(d,many=True)
        return Response(s.data)
    
    elif req.method=='POST':
        s=model_serializers(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def fun2(req,d):
    try:
        demo=student.objects.get(pk=d)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=model_serializers(demo)
        return Response(s.data)
    elif req.method =='PUT':
        s=model_serializers(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class fun3(APIView):
    def get(self,request):
            demo=student.objects.all()
            s=model_serializers(demo,many=True)
            return Response(s.data)
    def post(self,request):
            s=model_serializers(data=request.data)
            if s.is_valid():
                s.save()
                return Response(s.data,status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

class fun4(APIView):
    def get(self,req,d):
        try:
            demo=student.objects.get(pk=d)
            s=model_serializers(demo)
            return Response(s.data)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self,req,d):
        try:
            demo=student.objects.get(pk=d)
            s=model_serializers(demo,data=req.data)
            if s.is_valid():
                s.save()
                return Response(s.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,req,d):
        try:
            demo=student.objects.get(pk=d)
            demo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

# generic api :-

class genericapiview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=model_serializers
    queryset=student.objects.all()
    def get(self,req):
        return self.list(req)
    def post(self,req):
        return self.create(req)
    
class update(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=model_serializers
    queryset=student.objects.all()
    lookup_field='id'
    def get(self,req,id=None):
        return self.retrieve(req)
    def put(self,req,id=None):
        return self.update(req,id)
    def delete(self,req,id):
        return self.destroy(req,id)
        

