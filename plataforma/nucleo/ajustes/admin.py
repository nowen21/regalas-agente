# -*- coding: utf-8 -*-
"""Cómo se ven los ajustes en `/admin/`, que es donde se cambian."""
from django.contrib import admin

from .models import Ajuste, EtapaDelCiclo


@admin.register(Ajuste)
class AjusteAdmin(admin.ModelAdmin):
    list_display = ("clave", "para_que", "fue_cambiado")
    list_filter = ("tipo",)
    search_fields = ("clave", "valor", "para_que")
    readonly_fields = ("clave", "tipo", "de_fabrica")
    fields = ("clave", "para_que", "valor", "tipo", "de_fabrica")

    @admin.display(boolean=True, description="Cambiado")
    def fue_cambiado(self, ajuste):
        return ajuste.fue_cambiado

    def has_add_permission(self, peticion):
        # No se agregan a mano: los siembra la plataforma. Uno inventado acá no
        # lo pide nadie, y quien lo escriba creería que sirve.
        return False


@admin.register(EtapaDelCiclo)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ("orden", "nombre", "carpeta", "pregunta")
    ordering = ("orden",)
    fields = ("orden", "carpeta", "nombre", "pregunta", "queda")
