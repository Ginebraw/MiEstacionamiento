from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Arrendador, Arrendatario

class ArrendatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrendatario
        fields = ['rut' , 'nom' , 'telefono' ,'email', 'imagen', 'password1', 'password2']

class ArrendadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrendador
        fields = ['rut' , 'nom' , 'telefono' ,'email', 'imagen', 'password1', 'password2']
