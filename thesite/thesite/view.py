#coding: utf-8
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def home(request):
    return render(request, 'home.html')

def start(request):
	return render(request, 'start.html')

def data(request):
	return render(request, 'data.html')