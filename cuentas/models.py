from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore


# Modelos para la gestion de Cuentas

class Perfil(models.Model):
    """
    Modelo para el Perfil de Usuario paciente
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cuenta = models.CharField(max_length=12, choices=[("Paciente", "paciente"), ("Especialista", "especialista")])
    numero_phone = models.CharField(max_length=30)
    numero_dni = models.CharField(max_length=60)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    

class PerfilEspecialista(models.Model):
    """
    Modelo para el Perfil de Usuario Especialista
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cuenta = models.CharField(max_length=12, choices=[("Paciente", "paciente"), ("Especialista", "especialista")])
    numero_phone = models.CharField(max_length=30)
    numero_dni = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=100)
    sub_especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


