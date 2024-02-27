#IMPORTS:
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 


 #FUNCIONES:

#-----------------------------------------------------------------------------------------------------------------------------------Home
@login_required
def home(request):
    return render(request, "aplicacion/home.html") # ruta donde se encuentra el html 

#-----------------------------------------------------------------------------------------------------------------------------------Informacion personal

@login_required
def acercaDeMi(request):
    return render(request, "aplicacion/acercaDeMi.html") 


#-----------------------------------------------------------------------------------------------------------------------------------Gastos

#lista de gastos:
@login_required
def gastos(request):
    contexto = {'gasto': Gasto.objects.all()}  #importamos los datos de la data base de sql
    return render(request, "aplicacion/gastos.html", contexto) # ruta donde se encuentra el html, luego hay que poner el los tacs en el html

#Agregar un gasto:
@login_required
def extendGastos (request):
    if request.method == "POST":
        miForm = ExtendGastos(request.POST)
        if miForm.is_valid():
             gasto_descripcion = miForm.cleaned_data.get("descripcion")
             gasto_monto = miForm.cleaned_data.get("monto")
             gasto_fecha = miForm.cleaned_data.get("fecha")
             gasto = Gasto(descripcion=gasto_descripcion, monto=gasto_monto, fecha=gasto_fecha)
             gasto.save()
             return redirect(reverse_lazy('gastos')) 
    else:
        miForm = ExtendGastos()
    miForm = ExtendGastos()
    return render (request, "aplicacion/extendGastos.html", {"form": miForm})  #creamos el htlm 
 
 #Modificador de dato 
@login_required
def updateG (request, id_gastos):
    gastos = Gasto.objects.get(id=id_gastos)
    if request.method == "POST":
        miForm = ExtendGastos(request.POST)
        if miForm.is_valid():
            gastos.descripcion = miForm.cleaned_data.get('descripcion')
            gastos.monto = miForm.cleaned_data.get('monto')
            gastos.save()
            return redirect(reverse_lazy('gastos'))
    else:
        miForm = ExtendGastos(initial={
            'descripcion' : gastos.descripcion,
            'monto': gastos.monto,
        }) 
    return render(request, "aplicacion/extendGastos.html", {'form': miForm})

 #Funcion de borrar
@login_required
def deleateG (request, id_gastos):
    gastos = Gasto.objects.get(id=id_gastos)
    gastos.delete()
    return redirect(reverse_lazy('gastos'))

#Buscador de datos
@login_required
def buscador(request):
    if "lupa" in request.GET and request.GET["lupa"]:
        patron = request.GET["lupa"]
        gastos = Gasto.objects.filter(descripcion__icontains=patron.lower())
        contexto = {"gastos": gastos}
        return render(request, "aplicacion/gastos.html", contexto)
    else:
        return render(request, "aplicacion/lupa.html")
    
@login_required
def lupa(request):
    return render(request,"aplicacion/lupa.html")

#-----------------------------------------------------------------------------------------------------------------------------------ingresos

#lista de Ingresos:
@login_required
def ingresos(request):
    contexto = {'ingreso': Ingreso.objects.all()}  #importamos los datos de la data base de sql
    return render(request, "aplicacion/ingresos.html", contexto) # ruta donde se encuentra el html 

#Agregar un ingreso:
@login_required
def extendIngresos (request):
    if request.method == "POST":
        miForm = ExtendIngresos(request.POST)
        if miForm.is_valid():
            ingreso_descripcion = miForm.cleaned_data.get("ingreso")
            ingreso_monto = miForm.cleaned_data.get("monto")
            ingreso = Ingreso(ingreso=ingreso_descripcion, monto=ingreso_monto)
            ingreso.save()
            return redirect(reverse_lazy('ingresos'))  #funciona para redirijir la lista de ingresos
    else:
        miForm = ExtendIngresos()
    miForm = ExtendIngresos()
    return render (request, "aplicacion/extendIngresos.html", {"form": miForm})  #creamos el htlm 

#Modificador de dato 
@login_required
def updateI (request, id_ingresos):
    ingresos = Ingreso.objects.get(id=id_ingresos)
    if request.method == "POST":
        miForm = ExtendIngresos(request.POST)
        if miForm.is_valid():
            ingresos.ingreso = miForm.cleaned_data.get('ingreso')
            ingresos.monto = miForm.cleaned_data.get('monto')
            ingresos.save()
            return redirect(reverse_lazy('ingresos'))
    else:
        miForm = ExtendIngresos(initial={
            'ingreso' : ingresos.ingreso,
            'monto': ingresos.monto,
        }) 
    return render(request, "aplicacion/extendIngresos.html", {'form': miForm})

#Funcion de borrar
@login_required
def deleateI (request, id_ingresos):
    ingresos = Ingreso.objects.get(id=id_ingresos)
    ingresos.delete()
    return redirect(reverse_lazy('ingresos'))

#Buscador de datos
@login_required
def buscadorI(request):
    if request.GET["lupaI"]:
        patron = request.GET["lupaI"]
        ingresos = Ingreso.objects.filter(ingreso__icontains=patron)
        contexto = {"ingresos": ingresos}
        return render(request, "aplicacion/ingresos.html", contexto)
    return HttpResponse("Sin busqueda")
@login_required
def lupaI(request):
    return render(request,"aplicacion/lupaI.html")

#-----------------------------------------------------------------------------------------------------------------------------------Objetivos

#lista de objetivos:
@login_required
def objetivos (request):
    contexto = {'objetivo': Objetivo.objects.all()}  #importamos los datos de la data base de sql
    return render(request, "aplicacion/objetivos.html", contexto) # ruta donde se encuentra el html html 

#Agregar un objetivo:
@login_required
def extendObjetivos (request):
    if request.method == "POST":
        miForm = ExtendObjetivo(request.POST)
        if miForm.is_valid():
            objetivo_descripcion = miForm.cleaned_data.get("descripcion")
            objetivo_monto = miForm.cleaned_data.get("monto")
            objetivo = Objetivo(descripcion=objetivo_descripcion, monto=objetivo_monto)
            objetivo.save()
            return redirect(reverse_lazy('objetivos'))  #funciona para redirijir la lista de objetivos
    else:
        miForm = ExtendObjetivo()

    miForm = ExtendObjetivo()
    return render (request, "aplicacion/extendIngresos.html", {"form": miForm})  #creamos el htlm 


#Modificador de dato 
@login_required
def updateO (request, id_objetivos):
    objetivos = Objetivo.objects.get(id=id_objetivos)
    if request.method == "POST":
        miForm = ExtendObjetivo(request.POST)
        if miForm.is_valid():
            objetivos.descripcion = miForm.cleaned_data.get('descripcion')
            objetivos.monto = miForm.cleaned_data.get('monto')
            objetivos.save()
            return redirect(reverse_lazy('objetivos'))
    else:
        miForm = ExtendObjetivo(initial={
            'descripcion' : objetivos.descripcion,
            'monto': objetivos.monto,
        }) 
    return render(request, "aplicacion/extendObjetivos.html", {'form': miForm})

#Funcion de borrar
@login_required
def deleateO (request, id_objetivos):
    objetivos = Objetivo.objects.get(id=id_objetivos)
    objetivos.delete()
    return redirect(reverse_lazy('objetivos'))


#------------------------------------------------------------------------------------------------------------------------------------- Administracion

#registro en aplicacion
def registro(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            password = miForm.cleaned_data.get("password")
            user = authenticate(request, username=usuario, password=password) # Funcion que nos permite saber si el usuario esta en la base de datos
            if user is not None: #(si el usuario existe)
                login(request,user) 
            
            # (dentro del Avatar)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
            
            #-----------------------------------------------------------
            return redirect(reverse_lazy('home'))
        else: #si el usuario no existe
                return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {"form": miForm})

#Funcion para registrarse 
def registrarse (request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))    
    else:
        miForm = RegistroForm()
    return render(request,"aplicacion/registro.html", {"form": miForm})

#Editar perfil de usuario
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = EditUsuario(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = EditUsuario(instance=usuario)

    return render(request, "aplicacion/editUsuario.html", {"form": form }) 


#Foto e icono
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)
            Avatar.objects.filter(user=usuario).delete()
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()
            request.session["avatar"] = avatar.imagen.url
            return redirect("home")  
    else:    
        form = AvatarForm()
    return render(request, "aplicacion/agregarAvatar.html", {"form": form })