from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Car Selling Website!")
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Cars app!")
# cars/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the car site!")
