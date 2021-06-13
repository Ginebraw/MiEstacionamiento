from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from . forms import  ArrendadorForm, ArrendatarioForm
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(
        request,
        'index.html',
        )

def register(request):
    return render(
        request,
        'register.html',
    )


def login(request):
    return render(request, 'login.html') 

def estacionamientos(request):
	return render(request, 'estacionamientos.html')    


#CRUD ARRENDATARIO

def crear_arrendatario(request):
    data = {
        'form' : ArrendatarioForm()
    }

    if request.method == 'POST':
        formulario = ArrendatarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Arrendatario creado')
            return redirect(to="index")
    return render(
        request,
        'crear_arrendatario.html', data
    )


#CRUD ARRENDADOR

def crear_arrendador(request):
    data = {
        'form' : ArrendadorForm()
    }

    if request.method == 'POST':
        formulario = ArrendadorForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Arrendatario creado')
            return redirect(to="index")
    return render(
        request,
        'crear_arrendador.html', data
    )