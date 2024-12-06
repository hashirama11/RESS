# Direcciones URL para la aplicacion home


from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'), # type: ignore # Plantilla de Benvenida de app Home
    path('tipo_cuenta/', views.tipo_cuenta_view, name='tipo_cuenta'), # type: ignore # Plantilla de inicio de session segun tipo de cuenta
    path('registro_cuenta/', views.registro_cuenta_view, name='registro_cuenta'), # type: ignore # Plantilla de creacion de cuenta
]