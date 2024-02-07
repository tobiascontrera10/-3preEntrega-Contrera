from django.urls import path, include #importamos el include 
from .views import * #importamos todas las funciones que se encuentar dentro de views.py
from django.urls import path

urlpatterns = [
    path('',home, name="home"), # creamos el Home/inicio, todas las funciones tienen que estar creadas en el views.py de la app
    path('ingresos/',ingresos, name="ingresos"),
    path('gastos/', gastos, name="gastos"),
    path('objetivos', objetivos, name="objetivos"),
    #
    path('extendGastos', extendGastos, name="extendGastos"),
    path('extendIngresos', extendIngresos, name="extendIngresos"),
    path('extendObjetivos', extendObjetivos, name="extendObjetivos"),
    #
    path('buscar/', lupa, name="lupa"),
    path('buscador/', buscador, name="buscador"),
    
]
#el name es para enlazarlo en el html 