from django.urls import path # type: ignore
from . import views, views_service


# Importamos las vistas de la aplicación cuentas

urlpatterns = [
    # URLS de tipo Template
    #URLS de Pacientes
    path('login_paciente/', views.login_paciente_view, name='login_paciente'), # type: ignore #Para Inicio de session de paciente
    path('registro_paciente/', views.registro_paciente_view, name='register_paciente'), # type: ignore #Para registtrar nueva cuenta paciente
    # Urls para seleccionar tipo de cuenta
    path('tipo_cuenta/', views.tipo_cuenta_view, name='tipo_cuenta'), # type: ignore # Para Seleccionar tipo de cuenta a login
    path('registro_cuenta/', views.registro_cuenta, name='register_cuenta'), # type: ignore # Para Seleccionar tipo de registro nueva cuenta
    # URLS de Especialistas
    path('login_especialista', views.login_especialista_view, name='login_especialista'), # type: ignore # Para Inicio de session de especialista
    path('register_especialista', views.registro_especialista_view, name='register_especialista'), # type: ignore # Para registrar nueva cuenta especialista
    
    

    # URLS de tipo Servicios
        # URLS de Creacion de Cuentas
    path("account_p/", views_service.account_p, name="account_p"), # type: ignore # Para Crear cuenta paciente
    path("account_e/", views_service.account_e, name="account_e"), # type: ignore # Para Crear cuenta especialista
        # URLS de login
    path("login_p/", views_service.login_view_p, name="login_p"), # type: ignore # Para Inicio de session paciente
    path("login_e/", views_service.login_view_e, name="login_e"), # type: ignore # Para Inicio de session especialista
        # URLS de Logout
    path("logout_p/", views_service.logout_view_p, name="logout_p"), # type: ignore # Para Cerrar session paciente
    path("logout_e/", views_service.logout_view_e, name="logout_e"), # type: ignore # Para Cerrar session especialista


    # URL DE PRUEBA
    path('test/', views_service.test_view, name='test'), # type: ignore # Para Prueba de la Aplicación paciente
    path('test2/', views_service.test2_view, name='test2'), # type: ignore # Para Prueba de la Aplicación especialista

]

