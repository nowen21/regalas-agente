# -*- coding: utf-8 -*-
"""Los proyectos en `/admin/`: para marcar cuál es el estándar mismo."""
from django.contrib import admin

from .models import Proyecto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("identificador", "nombre", "es_el_estandar",
                    "version_reglas", "conectado")
    list_filter = ("es_el_estandar",)
    search_fields = ("identificador", "nombre", "ruta_codigo")
    fields = ("identificador", "nombre", "ruta_codigo", "es_el_estandar",
              "version_reglas", "conectado", "desconectado")
    readonly_fields = ("identificador", "ruta_normalizada")
