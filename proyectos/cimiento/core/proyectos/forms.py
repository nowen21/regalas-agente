from django import forms

from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["nombre", "ruta", "limite_enganche", "limite_archivo", "activo"]
