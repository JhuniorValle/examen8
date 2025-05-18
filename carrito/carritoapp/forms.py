from django import forms
from .models import Taller, Vehiculo

class TallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ['nombre', 'ubicacion', 'tipo_servicio', 'logo']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['taller', 'placa', 'modelo', 'marca', 'foto']
