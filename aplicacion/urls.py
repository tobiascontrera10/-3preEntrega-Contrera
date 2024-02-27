from django.urls import path, include #importamos el include 
from .views import * #importamos todas las funciones que se encuentar dentro de views.py
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    #pag de inicio
    path('',home, name="home"), 
    path('acercaDemi/',acercaDeMi, name="acercaDeMi"), 

    
    #ingresos:
    path('ingresos/',ingresos, name="ingresos"),
    path('extendIngresos', extendIngresos, name="extendIngresos"),   
    path('buscarI/', lupaI, name="lupaI"),
    path('buscadorI/', buscadorI, name="buscadorI"),
    path('updateI/<id_ingresos>/', updateI, name="actualizarI"),
    path('deleateI/<id_ingresos>/', deleateI, name="borrarI"),

    #gastos:
    path('gastos/', gastos, name="gastos"),
    path('extendGastos', extendGastos, name="extendGastos"),
    path('buscar/', lupa, name="lupa"),
    path('buscador/', buscador, name="buscador"),
    path('updateG/<id_gastos>/', updateG, name="actualizar"),
    path('deleateG/<id_gastos>/', deleateG, name="borrar"),
    
    #objetivos
    path('objetivos', objetivos, name="objetivos"),
    path('extendObjetivos', extendObjetivos, name="extendObjetivos"),      
    path('updateO/<id_objetivos>/', updateO, name="actualizarO"),
    path('deleateO/<id_objetivos>/', deleateO, name="borrarO"),

    #login y usuario:
    path('login/', registro, name="login"), # ingresar un usuario
    path('registro/', registrarse, name="registrarse"), #crear un usuario
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"), #cerrar sesion
    path('editUsuario/', editarPerfil, name="editarPerfil"), #editar perfil
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),#avatar

]


 