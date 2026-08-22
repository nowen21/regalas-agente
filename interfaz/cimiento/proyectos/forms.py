# -*- coding: utf-8 -*-
from django import forms

from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["nombre", "ruta", "scope", "stack", "activo", "notas"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "ruta": forms.TextInput(attrs={"class": "form-control"}),
            "scope": forms.TextInput(attrs={"class": "form-control"}),
            "stack": forms.TextInput(attrs={"class": "form-control"}),
            "notas": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
