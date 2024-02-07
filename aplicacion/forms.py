from django import forms 

class ExtendGastos(forms.Form):
    descripcion = forms.CharField(max_length=100, required=True)
    monto = forms.DecimalField(max_digits=10, decimal_places=0, required=True)
    fecha = forms.CharField(max_length=100)

class ExtendIngresos(forms.Form):
    ingreso = forms.CharField(max_length=100, required=True)
    monto = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

class ExtendObjetivo(forms.Form):
    descripcion = forms.CharField(max_length=100)
    monto = forms.DecimalField(max_digits=10, decimal_places=2)