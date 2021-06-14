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

urlpatterns+=[
path('estacionamientos/create/', views.estacionamiento_create, name='estacionamiento_create'),
path('estacionamientos/<str:pk>', views.EstacionamientoDetailView.as_view(), name='estacionamiento_detail'),
path('estacionamientos/<str:pk>/update/', views.EstacionamientoUpdate.as_view(), name='estacionamiento_update'),
path('estacionamientos/<str:pk>/delete/', views.EstacionamientoDelete.as_view(), name='estacionamiento_create'),
]

