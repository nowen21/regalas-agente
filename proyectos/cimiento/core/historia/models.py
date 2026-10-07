# -*- coding: utf-8 -*-
"""`EP-026·HU-001` · Un cambio en una tabla de Cimiento.

**No se edita ni se borra.** Deshacer un cambio no lo quita: suma otro que dice
cuál deshizo (`20·M11`).

**Antes y después llevan solo lo que cambió**, sin las fechas automáticas: al
crear, todo va en «después»; al borrar, todo en «antes».
"""
from django.conf import settings
from django.db import models

CREAR, CAMBIAR, BORRAR = "crear", "cambiar", "borrar"
ACCIONES = [(CREAR, "Crear"), (CAMBIAR, "Cambiar"), (BORRAR, "Borrar")]

# `EP-026·HU-002` · El tipo de una versión (`20·M10`).
MAYOR, MENOR, PARCHE = "MAYOR", "MENOR", "PARCHE"
TIPOS = [(MAYOR, "Mayor"), (MENOR, "Menor"), (PARCHE, "Parche")]
ESTANDAR, PROYECTO = "estandar", "proyecto"
AMBITOS = [(ESTANDAR, "El estándar"), (PROYECTO, "Un proyecto")]


class Version(models.Model):
    """`EP-026·HU-002` · Una versión del estándar o de un proyecto. No se edita ni se borra."""

    ambito = models.CharField(max_length=10, choices=AMBITOS)
    proyecto = models.ForeignKey("proyectos.Proyecto", null=True, blank=True, on_delete=models.PROTECT,
                                 related_name="versiones")
    mayor = models.PositiveIntegerField()
    menor = models.PositiveIntegerField()
    parche = models.PositiveIntegerField()
    tipo = models.CharField(max_length=6, choices=TIPOS)
    resumen = models.TextField(blank=True, default="")
    fecha = models.DateTimeField(auto_now_add=True)
    cuenta = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name="versiones_hechas")
    quien = models.CharField(max_length=100)

    class Meta:
        ordering = ["-fecha", "-id"]

    @property
    def numero(self):
        return "%d.%d.%d" % (self.mayor, self.menor, self.parche)

    def __str__(self):
        return "%s %s" % (self.proyecto or "estándar", self.numero)


class Cambio(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, db_index=True)
    cuenta = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name="cambios_hechos")
    quien = models.CharField(max_length=100, help_text="cuenta, agente o el programa que lo hizo")
    tabla = models.CharField(max_length=100, db_index=True, help_text="app.modelo, como proyectos.ajustedelproyecto")
    fila = models.CharField(max_length=64)
    accion = models.CharField(max_length=10, choices=ACCIONES)
    antes = models.JSONField(null=True, blank=True)
    despues = models.JSONField(null=True, blank=True)
    motivo = models.TextField(blank=True, default="")
    deshace = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                related_name="deshecho_por")
    version = models.ForeignKey(Version, null=True, blank=True, on_delete=models.PROTECT, related_name="cambios")

    class Meta:
        ordering = ["-fecha", "-id"]

    def __str__(self):
        return "%s %s %s #%s" % (self.fecha, self.accion, self.tabla, self.fila)

    def quien_lo_hizo(self):
        return self.cuenta.get_username() if self.cuenta else self.quien
