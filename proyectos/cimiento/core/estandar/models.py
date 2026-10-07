# -*- coding: utf-8 -*-
"""`EP-026·HU-003` · Un documento del estándar y un recuerdo de un proyecto.

Lo que se guarda en ellos tiene historia (HU-001) y sube la versión del
estándar o la del proyecto (HU-002): la tabla del estándar es de la app
`estandar`, que `historia.versiones` sube como estándar.
"""
from django.db import models


class Documento(models.Model):
    """Un documento de `base/`, con su ruta desde la raíz del estándar y su texto exacto."""

    ruta = models.CharField(max_length=255, unique=True, help_text="base/01-conducta.md")
    contenido = models.TextField(blank=True, default="")
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ruta"]

    def __str__(self):
        return self.ruta


class Recuerdo(models.Model):
    """Un recuerdo de la memoria de un proyecto (`01·C19`)."""

    proyecto = models.ForeignKey("proyectos.Proyecto", on_delete=models.PROTECT, related_name="recuerdos")
    nombre = models.CharField(max_length=200, help_text="como el archivo: aprobar-antes-de-commit.md")
    contenido = models.TextField(blank=True, default="")
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["proyecto", "nombre"]
        constraints = [models.UniqueConstraint(fields=["proyecto", "nombre"], name="un_recuerdo_por_nombre")]

    def __str__(self):
        return "%s · %s" % (self.proyecto, self.nombre)


PENDIENTE, APROBADA, RECHAZADA = "pendiente", "aprobada", "rechazada"
ESTADOS = [(PENDIENTE, "Pendiente"), (APROBADA, "Aprobada"), (RECHAZADA, "Rechazada")]
DOCUMENTO, RECUERDO = "documento", "recuerdo"
OBJETOS = [(DOCUMENTO, "Documento del estándar"), (RECUERDO, "Recuerdo de un proyecto")]
CREAR, CAMBIAR, QUITAR = "crear", "cambiar", "quitar"
ACCIONES = [(CREAR, "Crear"), (CAMBIAR, "Cambiar"), (QUITAR, "Quitar")]


class Propuesta(models.Model):
    """`EP-026·HU-005` · Lo que propone el agente o un programa. No cambia nada
    hasta que el administrador la aprueba en la pantalla (acuerdo 3)."""

    objeto = models.CharField(max_length=10, choices=OBJETOS)
    accion = models.CharField(max_length=10, choices=ACCIONES)
    ruta = models.CharField(max_length=255, blank=True, default="", help_text="del documento: base/…")
    proyecto = models.ForeignKey("proyectos.Proyecto", null=True, blank=True, on_delete=models.PROTECT,
                                 related_name="propuestas")
    nombre = models.CharField(max_length=200, blank=True, default="", help_text="del recuerdo")
    contenido = models.TextField(blank=True, default="", help_text="el texto completo que queda")
    motivo = models.TextField(blank=True, default="")
    quien = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default=PENDIENTE)
    resuelta_por = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="propuestas_resueltas")
    resuelta = models.DateTimeField(null=True, blank=True)
    # `EP-028·HU-004` · Rechazar pide el motivo (guía de diseño de pantallas, §11).
    motivo_rechazo = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-fecha", "-id"]

    def destino(self):
        return self.ruta if self.objeto == DOCUMENTO else "%s · %s" % (self.proyecto, self.nombre)

    def __str__(self):
        return "%s %s %s" % (self.get_estado_display(), self.accion, self.destino())


ABIERTO, CORREGIDO, DESCARTADO = "abierto", "corregido", "descartado"
ESTADOS_DEL_REPORTE = [(ABIERTO, "Abierto"), (CORREGIDO, "Corregido"), (DESCARTADO, "Descartado")]


class Reporte(models.Model):
    """`EP-026·HU-008` · Lo que un proyecto encuentra mal en el estándar.

    No sube versión al llegar: la sube la corrección, y el reporte apunta a la
    versión que lo corrigió (análisis 1 del pendiente 132, acuerdo 13).
    """

    proyecto = models.ForeignKey("proyectos.Proyecto", on_delete=models.PROTECT, related_name="reportes")
    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, default="")
    regla = models.CharField(max_length=20, blank=True, default="", help_text="la regla que toca, como 02·F8")
    quien = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS_DEL_REPORTE, default=ABIERTO)
    corregido_en = models.ForeignKey("historia.Version", null=True, blank=True, on_delete=models.PROTECT,
                                     related_name="reportes_corregidos")
    motivo = models.TextField(blank=True, default="", help_text="por qué se descartó")
    resuelto_por = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="reportes_resueltos")
    resuelto = models.DateTimeField(null=True, blank=True)
    avisado = models.BooleanField(default=False, help_text="el proyecto ya se enteró de cómo quedó")

    class Meta:
        ordering = ["-fecha", "-id"]

    def __str__(self):
        return "%s · %s" % (self.proyecto, self.titulo)
