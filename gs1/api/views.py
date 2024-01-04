from django.shortcuts import render, HttpResponse
from rest_framework import response
from .models import Member


# Create your views here.

def home(request):
    # create_obj = Member(firstname = 'rahul', lastname = 'arora')

    # create_obj.save()

    return HttpResponse("welcome")
