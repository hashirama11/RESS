import re
from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse, Http404 # type: ignore
from django.contrib.auth.models import User # type: ignore
from . import models # type: ignore
from django.contrib import messages # type: ignore

# Create your views here.


def login_paciente_view(request):
    """
    Página para inicio de session de pacientes.
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/pacientes/login_paciente.html', {})
        else:
            return HttpResponse("Hubo un error", status=405)
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)



def registro_paciente_view(request):
    """
    Página para registrar nuevos pacientes.
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/pacientes/register_paciente.html', {}) 
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)


def tipo_cuenta_view(request):
    """
    Página para seleccionar el tipo de cuenta para iniciar session.
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/tipo_cuenta.html', {}) 
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)


def registro_cuenta(request):
    """
    Página para registrar nuevos pacientes
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/registro_cuenta.html', {}) 
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)
    

def registro_especialista_view(request):
    """
    Página para registrar nuevos especialistas
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/especialistas/register_especialista.html', {}) 
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)
    
def login_especialista_view(request):
    """
    Página para inicio de session de especialistas
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/especialistas/login_especialista.html', {}) 
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)
    

    


    



