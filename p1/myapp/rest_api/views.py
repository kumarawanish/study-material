from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
  
# import local data
from .serializers import MySerialiazer, StudentSerialiazer
from .models import MyModel, Student
  
# create a viewset
class MyEthic(viewsets.ModelViewSet):
    # define queryset
    queryset = MyModel.objects.all()
      
    # specify serializer to be used
    serializer_class = MySerialiazer



class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiazer


