from django.shortcuts import render
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect

# Create your views here.
def index(request):
    
    return render(
        request,
        'index.html',
        )

def login(request):
	return render(request, 'login.html') 

def estacionamientos(request):
	return render(request, 'estacionamientos.html')    