from django.shortcuts import render # type: ignore
from django.http import HttpResponse, HttpResponseRedirect # type: ignore


# Vistas de la aplicacion home
from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def home(request):
    """
    Página principal de Bienvenida
    """
    try:
        if request.method == 'GET':
            return render(request, 'home/home.html', {})
        else:
            return HttpResponse("Hubo un error", status=405)
    except Exception as e:
        import traceback
        error_message = f"Error en la página principal: {str(e)}\n{traceback.format_exc()}"
        return HttpResponse(error_message, status=500)


def tipo_cuenta_view(request):
    """
    Pagina para seleccionar el tipo de cuenta a login
    """
    try:
        if request.method == 'GET':
            return render(request, 'cuentas/tipo_cuenta.html', {})
        else:
            return HttpResponse("Hubo un error", status=405)
    except Exception as e:
        return HttpResponse(f"Error en la vista de tipo de cuenta: {str(e)}", status=500)
    

# Tipo de perfil para crear cuenta
def registro_cuenta_view(request):
    try:
        """
        Pagina para crear un tipo de cuenta
        """
        if request.method == 'GET':
            return render(request, 'cuentas/registro_cuenta.html', {})
        else:
            return HttpResponse("Hubo un error")
    except Exception as e:
        return HttpResponse(f"Error en la vista de registro de cuenta: {str(e)}", status=500)