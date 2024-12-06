from venv import logger
from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from . import models # type: ignore
from django.http import HttpResponse, Http404 # type: ignore
import re # type: ignore
import logging  # type: ignore
from django.conf import settings # type: ignore
from django.contrib.auth.tokens import default_token_generator  # Para generar tokens de restablecimiento # type: ignore
from django.utils.http import urlsafe_base64_encode  # Para codificar el usuario # type: ignore
from django.template.loader import render_to_string  # Para renderizar correos electrónicos # type: ignore
from django.core.mail import send_mail  # Para enviar correos electrónicos # type: ignore
from django.contrib.auth import authenticate, login, logout, get_user_model # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore





def account_p(request):
    """
    Vista para crear una nueva cuenta de usuario paciente
    """
    if request.method == "POST":
        # Recuperar los datos del formulario
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dni = request.POST.get('dni')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        # Validar los datos del formulario
        tipo_cuenta = "Paciente"
        errors = []

        if not username:
            errors.append("El nombre de usuario es obligatorio")
        elif User.objects.filter(username=username).exists():
            errors.append("El nombre de usuario ya existe")

        if not first_name:
            errors.append("El nombre es obligatorio")

        if not last_name:
            errors.append("El apellido es obligatorio")

        if not email:
            errors.append("El correo electrónico es obligatorio")
        elif User.objects.filter(email=email).exists():
            errors.append("El correo electrónico ya existe")

        if not phone:
            errors.append("El número de teléfono es obligatorio")

        if not dni:
            errors.append("El DNI es obligatorio")

        if not password:
            errors.append("La contraseña es obligatoria")
        elif password != repeat_password:
            errors.append("Las contraseñas no coinciden")

        # Si hay errores, mostrar los mensajes
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'cuentas/pacientes/register_paciente.html')
        else:
            try:
                # Crear el nuevo usuario y el perfil
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                profile = models.Perfil.objects.create(user=user, numero_phone=phone, numero_dni=dni, tipo_cuenta=tipo_cuenta)
                profile.save()

                # Autenticar y iniciar sesión al nuevo usuario
                user = authenticate(username=username, password=password)
                login(request, user)

                messages.success(request, 'Cuenta creada correctamente')

                # Redireccionar al inicio
                return redirect('home_view')
            except Exception as e:
                messages.error(request, f"Ha ocurrido un error al crear la cuenta: {e}")
                return render(request, 'cuentas/pacientes/register_paciente.html')

    # Mostrar el formulario de registro
    return render(request, 'cuentas/pacientes/register_paciente.html')

def account_e(request):
    """
    Vista para crear una nueva cuenta de usuario especialista
    """
    if request.method == "POST":
        # Recuperar los datos del formulario
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dni = request.POST.get('dni')
        especialidad = request.POST.get('especialidad')
        sub_especialidad = request.POST.get('sub_especialidad')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        tipo_cuenta = "Especialista"

        # Validar los datos del formulario
        errors = []

        if not username:
            errors.append("El nombre de usuario es obligatorio")
        elif User.objects.filter(username=username).exists():
            errors.append("El nombre de usuario ya existe")

        if not first_name:
            errors.append("El nombre es obligatorio")

        if not last_name:
            errors.append("El apellido es obligatorio")

        if not email:
            errors.append("El correo electrónico es obligatorio")
        elif User.objects.filter(email=email).exists():
            errors.append("El correo electrónico ya existe")

        if not phone:
            errors.append("El número de teléfono es obligatorio")

        if not dni:
            errors.append("El DNI es obligatorio")

        if not especialidad:
            errors.append("La especialidad es obligatoria")

        if not password:
            errors.append("La contraseña es obligatoria")
        elif password != repeat_password:
            errors.append("Las contraseñas no coinciden")

        # Si hay errores, mostrar los mensajes
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'cuentas/especialista/register_especialista.html')
        else:
            try:
                # Crear el nuevo usuario y el perfil
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                profile = models.PerfilEspecialista.objects.create(user=user, numero_phone=phone, numero_dni=dni, especialidad=especialidad, sub_especialidad=sub_especialidad, tipo_cuenta=tipo_cuenta)
                profile.save()

                # Autenticar y iniciar sesión al nuevo usuario
                user = authenticate(username=username, password=password)
                login(request, user)

                messages.success(request, 'Cuenta creada correctamente')

                # Redireccionar al inicio
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Ha ocurrido un error al crear la cuenta: {e}")
                return render(request, 'cuentas/especialistas/register_especialista.html')

    # Mostrar el formulario de registro
    return render(request, 'cuentas/especialista/register_especialista.html')


logger = logging.getLogger(__name__)

def login_view_p(request):
    """
    Vista para iniciar sesión de un paciente
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validación exhaustiva
        if not email or not password:
            messages.error(request, 'Debes ingresar tu correo electrónico y contraseña')
        elif not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            messages.error(request, 'El correo electrónico no es válido')
        elif len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres')
        else:
            # Autenticación con manejo de errores
            try:
                user = authenticate(username=email, password=password)
                if user is not None and user.is_active:
                    try:
                        perfil = models.Perfil.objects.get(user=user)
                        if perfil.tipo_cuenta == "Paciente":
                            login(request, user)
                            messages.success(request, 'Inicio de sesión exitoso')
                            return redirect('test')
                        else:
                            messages.error(request, 'Solo los pacientes pueden iniciar sesión aquí.')
                    except models.Perfil.DoesNotExist:
                        messages.error(request, 'Solo los pacientes pueden iniciar sesión aquí.')
                else:
                    messages.error(request, 'Usuario o contraseña incorrectos')
                    logger.debug(f'Usuario o contraseña incorrectos para {email}')
            except Exception as e:
                # Loggear el error para depuración
                logger.error(f"Error de autenticación: {e}")
                messages.error(request, 'Ha ocurrido un error al iniciar sesión.')

    return render(request, 'cuentas/pacientes/login_paciente.html')


def login_view_e(request):
    """
    Vista para iniciar sesión de un especialista
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validación exhaustiva
        if not email or not password:
            messages.error(request, 'Debes ingresar tu correo electrónico y contraseña')
        elif not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            messages.error(request, 'El correo electrónico no es válido')
        elif len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres')
        else:
            # Autenticación con manejo de errores
            try:
                user = authenticate(username=email, password=password)
                if user is not None and user.is_active:
                    try:
                        perfil_especialista = models.PerfilEspecialista.objects.get(user=user)
                        if perfil_especialista.tipo_cuenta == "Especialista":
                            login(request, user)
                            messages.success(request, 'Inicio de sesión exitoso')
                            return redirect('test2')
                        else:
                            messages.error(request, 'Solo los especialistas pueden iniciar sesión aquí.')
                    except models.PerfilEspecialista.DoesNotExist:
                        messages.error(request, 'Solo los especialistas pueden iniciar sesión aquí.')
                else:
                    messages.error(request, 'Usuario o contraseña incorrectos')
            except Exception as e:
                # Loggear el error para depuración
                logger.error(f"Error de autenticación: {e}")
                messages.error(request, 'Ha ocurrido un error al iniciar sesión.')

    return render(request, 'cuentas/especialistas/login_especialista.html')


@login_required
def test_view(request):
    """
    Página para prueba de la Aplicación paciente
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/test.html', {}) 
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)


@login_required
def test2_view(request):
    """
    Página para prueba de la Aplicación paciente
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/test2.html', {}) 
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)


def logout_view_p(request):
    """
    Página para cerrar la sesión de pacientes
    """
    try:
        if request.method == 'POST':
            logout(request)
            return redirect('home')
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)
    

def logout_view_e(request):
    """
    Página para cerrar la sesión de especialistas
    """
    try:
        if request.method == 'POST':
            logout(request)
            return redirect('home')
        else:
            return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(f"Error en la página principal: {str(e)}", status=500)