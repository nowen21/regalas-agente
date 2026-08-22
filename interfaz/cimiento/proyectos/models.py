# -*- coding: utf-8 -*-
"""El registro de proyectos: la fuente de verdad de qué usa el estándar.

Antes era una tabla escrita a mano en `plantillas/proyectos.md`. Ahora el
registro vive acá y aquel archivo **se genera** desde esta base (el instalador
y los avisos lo siguen leyendo, así que se regenera tras cada cambio).
"""
from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    ruta = models.CharField(
        max_length=500,
        help_text="Carpeta raíz del proyecto en esta máquina.")
    scope = models.CharField(
        max_length=120, blank=True,
        help_text="Scope de memoria, p. ej. proyecto:mi-proyecto.")
    stack = models.CharField(
        max_length=300, blank=True, default="por detectar",
        help_text="Con qué está construido; «por detectar» hasta llenarse.")
    activo = models.BooleanField(
        default=True,
        help_text="Un proyecto dado de baja no recibe avisos ni instalaciones; "
                  "no se borra, para conservar su historia.")
    notas = models.TextField(blank=True, default="")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
