from django import forms
from django.forms import ModelForm
from .models import Arrendatario, Arrendador, Estacionamiento

class ArrendatarioForm(forms.ModelForm):
    rut = forms.CharField(label='Rut',max_length=9,help_text='Ingrese rut sin puntos ni comas')
    nom = forms.CharField(label='Nombre Completo',max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(label='Telefono')
    email = forms.EmailField()
    imagen = forms.ImageField(label='Imagen',widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Arrendatario
        fields = ['rut' , 'nom' , 'telefono' ,'email', 'imagen', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class ArrendadorForm(forms.ModelForm):
    rut = forms.CharField(label='Rut',max_length=9,help_text='Ingrese rut sin puntos ni comas')
    nom = forms.CharField(label='Nombre Completo',max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(label='Telefono')
    email = forms.EmailField()
    imagen = forms.ImageField(label='Imagen',widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Arrendador
        fields = ['rut' , 'nom' , 'telefono' ,'email', 'imagen', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class EstacionamientoForm(forms.ModelForm):
    n_esta = forms.CharField(label='N° Estacionamiento',max_length=8,help_text='Ingrese N° de estacionamiento')
    direccion = forms.CharField(label='Dirección',max_length=50,help_text='Ingrese dirección', widget=forms.TextInput(attrs={'class':'form-control'}))


    class meta:
         model = Estacionamiento
         fields = '__all__'


         widgets={'tamaño': forms.Select(attrs={'class':'form-control'})}