from django.db import models
from django.urls import reverse

# Create your models here.
class Arrendatario(models.Model):

    rut = models.CharField(max_length=12)
    nom = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank=True)

    def _str(self):
        return self.rut

class Arrendador(models.Model):

    rut = models.CharField(max_length=12)
    nom = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank=True)

    def _str(self):
        return self.rut


class Estacionamiento(models.Model):
    n_esta =models.CharField(primary_key=True, max_length=8)
    Pequeño="Pequeño"
    Mediano="Mediano"
    Grande="Grande"
    tamaño_choices=((Pequeño,"Pequeño"),(Mediano,"Mediano"),(Grande,"Grande"))
    tamaño = models.CharField(null=False, max_length=8, default="Mediano", choices=tamaño_choices)
    direccion = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.n_esta

    def get_absolute_url(self):
        return reverse('estacionamiento_detail', args=[str(self.n_esta)])    


