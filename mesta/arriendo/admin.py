from django.contrib import admin

# Register your models here.
from .models import Arrendatario, Arrendador

admin.site.register(Arrendatario)
admin.site.register(Arrendador)
