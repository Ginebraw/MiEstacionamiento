from django import forms
from django.forms import ModelForm
from .models import Arrendatario, Arrendador

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