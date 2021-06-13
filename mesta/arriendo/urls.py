from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
path('',views.index,name='index'),
path('register/',views.register,name='register'),
path('nuevo-arrendatario/', views.crear_arrendatario, name='nuevo_arrendatario'),
path('nuevo-arrendador/', views.crear_arrendador, name='nuevo_arrendador'),
path('estacionamientos/',views.estacionamientos,name='estacionamientos'),

]

