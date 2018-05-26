from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Access_Log,Data_LogA,Data_LogB,Data_LogC,Data_LogD
from django.contrib.auth.models import User
from .serializer import Access_Log_Serializer,UserSerializer,Data_LogASerializer,Data_LogBSerializer,Data_LogCSerializer,Data_LogDSerializer

class Access_LogList(APIView):
    def get(self,request):
        access=Access_Log.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Access_Log_Serializer(access,many=True)
        return Response(serializer.data)
    def post(self):
        pass

# Create your views here.
class UserList(APIView):
    def get(self,request):
        user=User.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class Data_LogAList(APIView):
    def get(self,request):
        data_log=Data_LogA.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogASerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class Data_LogBList(APIView):
    def get(self,request):
        data_log=Data_LogB.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogBSerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class Data_LogCList(APIView):
    def get(self,request):
        data_log=Data_LogC.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogCSerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class Data_LogDList(APIView):
    def get(self,request):
        data_log=Data_LogD.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogDSerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self):
        pass