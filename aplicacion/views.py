from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.

 #funciones que se importaran a la urls.py :

def home(request):
    return render(request, "aplicacion/home.html") # ruta donde se encuentra el html 
 #render es un metodo de busqueda
 #en esta funcion le estamos pidiendo a django que busque en html que lo encontrara en la carpeta TEMPLATES creada dentro de la app
#-------------------------------------------------------------------------------------------------------------------------------------

def gastos(request):
    contexto = {'gasto': Gasto.objects.all()}  #importamos los datos de la data base de sql
    return render(request, "aplicacion/gastos.html", contexto) # ruta donde se encuentra el html, luego hay que poner el los tacs en el html

def extendGastos (request):
    if request.method == "POST":
        miForm = ExtendGastos(request.POST)
        if miForm.is_valid():
             gasto_descripcion = miForm.cleaned_data.get("descripcion")
             gasto_monto = miForm.cleaned_data.get("monto")
             gasto_fecha = miForm.cleaned_data.get("fecha")
             gasto = Gasto(descripcion=gasto_descripcion, monto=gasto_monto, fecha=gasto_fecha)
             gasto.save()
             return render(request, "aplicacion/gastos.html")
    else:
        miForm = ExtendGastos()

    miForm = ExtendGastos()
       
    return render (request, "aplicacion/extendGastos.html", {"form": miForm})  #creamos el htlm 
#-------------------------------------------------------------------------------------------------------------------------------------

def ingresos(request):
    contexto = {'ingreso': Ingreso.objects.all()}  #importamos los datos de la data base de sql
    return render(request, "aplicacion/ingresos.html", contexto) # ruta donde se encuentra el html 

def extendIngresos (request):
    if request.method == "POST":
        miForm = ExtendIngresos(request.POST)
        if miForm.is_valid():
            ingreso_descripcion = miForm.cleaned_data.get("ingreso")
            ingreso_monto = miForm.cleaned_data.get("monto")
            ingreso = Ingreso(ingreso=ingreso_descripcion, monto=ingreso_monto)
            ingreso.save()
            return render(request, "aplicacion/home.html")
    else:
        miForm = ExtendIngresos()

    miForm = ExtendIngresos()
       
    return render (request, "aplicacion/extendIngresos.html", {"form": miForm})  #creamos el htlm 
#-------------------------------------------------------------------------------------------------------------------------------------

def objetivos (request):
    contexto = {'objetivo': Objetivo.objects.all()}  #importamos los datos de la data base de sql
    return render(request, "aplicacion/objetivos.html", contexto) # ruta donde se encuentra el html html 

def extendObjetivos (request):
    if request.method == "POST":
        miForm = ExtendObjetivo(request.POST)
        if miForm.is_valid():
            objetivo_descripcion = miForm.cleaned_data.get("descripcion")
            objetivo_monto = miForm.cleaned_data.get("monto")
            objetivo = Objetivo(descripcion=objetivo_descripcion, monto=objetivo_monto)
            objetivo.save()
            return render(request, "aplicacion/home.html")
    else:
        miForm = ExtendObjetivo()

    miForm = ExtendObjetivo()
    return render (request, "aplicacion/extendIngresos.html", {"form": miForm})  #creamos el htlm 

#-------------------------------------------------------------------------------------------------------------------------------------

def buscador(request):
    if request.GET["lupa"]:
        patron = request.GET["lupa"]
        gastos = Gasto.objects.filter(descripcion__icontains=patron)
        contexto = {"gastos": gastos}
        return render(request, "aplicacion/gastos.html", contexto)
    return HttpResponse("Sin busqueda")

def lupa(request):
    return render(request,"aplicacion/lupa.html")