"""Los formularios de «Proyectos» y de «Configuración».

`EP-025·HU-013` · Cada ajuste se ofrece con «el de la capa de abajo» como
primera opción: vacío, el proyecto usa el de la base y la base el de fábrica.
"""
from datetime import timedelta

from django import forms
from django.db import transaction
from django.utils import timezone

from . import ajustes as catalogo
from .models import AjusteBase, AjusteDelProyecto, Proyecto, Suspension


def campo_de_ajuste(clave, vacio):
    """El campo de un ajuste; `vacio` dice qué vale si se deja en blanco."""
    ajuste = catalogo.AJUSTES[clave]
    if ajuste.opciones is int:
        return forms.IntegerField(label=ajuste.titulo, required=False, min_value=1,
                                  help_text="%s Vacío: %s." % (ajuste.ayuda, vacio))
    return forms.ChoiceField(label=ajuste.titulo, required=False,
                             choices=[("", "Vacío: %s" % vacio)] + [(o, o.capitalize()) for o in ajuste.opciones],
                             help_text=ajuste.ayuda)


class ProyectoForm(forms.ModelForm):
    """El proyecto y sus ajustes propios, que mandan solo para él."""

    class Meta:
        model = Proyecto
        fields = ["nombre", "ruta", "activo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        propios = dict(self.instance.ajustes_propios.values_list("clave", "valor")) if self.instance.pk else {}
        for clave in catalogo.AJUSTES:
            self.fields[clave] = campo_de_ajuste(clave, "el de la configuración de Cimiento")
            self.fields[clave].initial = propios.get(clave, "")

    def save(self, commit=True):
        with transaction.atomic():
            proyecto = super().save(commit=commit)
            for clave in catalogo.AJUSTES:
                valor = catalogo.limpio(clave, self.cleaned_data.get(clave))
                if valor:
                    AjusteDelProyecto.objects.update_or_create(proyecto=proyecto, clave=clave,
                                                               defaults={"valor": valor})
                else:
                    AjusteDelProyecto.objects.filter(proyecto=proyecto, clave=clave).delete()
        return proyecto


class ConfiguracionForm(forms.Form):
    """Capa 1: el valor común de cada ajuste."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        guardados = dict(AjusteBase.objects.values_list("clave", "valor"))
        for clave, ajuste in catalogo.AJUSTES.items():
            self.fields[clave] = campo_de_ajuste(clave, "el de fábrica, %s" % ajuste.fabrica)
            self.fields[clave].initial = guardados.get(clave, "")

    def guardar(self):
        with transaction.atomic():
            for clave in catalogo.AJUSTES:
                valor = catalogo.limpio(clave, self.cleaned_data.get(clave))
                if valor:
                    AjusteBase.objects.update_or_create(clave=clave, defaults={"valor": valor})
                else:
                    AjusteBase.objects.filter(clave=clave).delete()


class SuspensionForm(forms.ModelForm):
    """Capa 3: una regla, o el freno entero, apagada con motivo y hasta una fecha."""

    class Meta:
        model = Suspension
        fields = ["tipo", "nombre", "motivo", "vence"]
        widgets = {"vence": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M")}
        labels = {"nombre": "Regla (p. ej. 02·F8), o «freno»", "vence": "Vence"}

    def clean(self):
        datos = super().clean()
        tipo, nombre = datos.get("tipo"), (datos.get("nombre") or "").strip()
        if tipo == catalogo.ENGANCHE:
            nombre = catalogo.FRENO
        datos["nombre"] = nombre
        if not catalogo.se_puede_suspender(tipo, nombre):
            raise forms.ValidationError("Eso no se suspende: el núcleo y el histórico protegen los datos y las claves.")
        if tipo == catalogo.REGLA:
            from core.niveles.catalogo import ids_configurables
            if nombre not in ids_configurables():
                raise forms.ValidationError("«%s» no es una regla vigente del estándar." % nombre)
        if not (datos.get("motivo") or "").strip():
            raise forms.ValidationError("La suspensión lleva su motivo.")
        vence = datos.get("vence")
        ahora = timezone.now()
        if vence and vence <= ahora:
            raise forms.ValidationError("El vencimiento tiene que ser después de ahora.")
        if vence and vence > ahora + timedelta(days=catalogo.DIAS_MAXIMOS):
            raise forms.ValidationError("Una suspensión dura a lo sumo %d días." % catalogo.DIAS_MAXIMOS)
        return datos
