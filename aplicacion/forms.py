from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ExtendGastos(forms.Form):
    descripcion = forms.CharField(max_length=100, required=True)
    monto = forms.DecimalField(max_digits=10, decimal_places=0, required=True)
    fecha = forms.CharField(max_length=100)

class ExtendIngresos(forms.Form):
    ingreso = forms.CharField(max_length=100, required=True)
    monto = forms.DecimalField(max_digits=10, decimal_places=0, required=True)

class ExtendObjetivo(forms.Form):
    descripcion = forms.CharField(max_length=100)
    monto = forms.DecimalField(max_digits=10, decimal_places=0)


class RegistroForm(UserCreationForm): #es el formulario que viene con el modelo de autentificacion
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:  #los campos que quiero mostrar en el formulario
        model = User
        fields = ['username','email', 'password1', 'password2']


#Editar perfil
class EditUsuario(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


#avatar
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)