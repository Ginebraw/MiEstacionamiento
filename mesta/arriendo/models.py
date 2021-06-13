from django.db import models

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