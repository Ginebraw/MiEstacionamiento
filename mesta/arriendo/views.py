from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from . forms import  ArrendadorForm, ArrendatarioForm, EstacionamientoForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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
    num_est=Estacionamiento.objects.all()
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

#CRUD Estacionamiento

def estacionamiento_create(request):
    
    if request.method == "POST":
        form = EstacionamientoForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Estacionamiento creado')
            return redirect(to="estacionamientos")
        
    return render(request, 'Estacionamiento/estacionamiento_form.html')    
    

class EstacionamientoDetailView(generic.DetailView):
    model = Estacionamiento

class EstacionamientoDelete(DeleteView):
    model = Estacionamiento
    success_url = reverse_lazy('estacionamiento')

class EstacionamientoUpdate(UpdateView):
    model = Estacionamiento
    fields = ['direccion','tamaño']
    success_url = reverse_lazy('estacionamiento')
    template_name_suffix = '_update_form'    