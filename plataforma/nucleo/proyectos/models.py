# -*- coding: utf-8 -*-
"""El índice de proyectos. La fuente es la ficha en texto de cada uno.

**La ruta viva y el estado no son campos: son preguntas que se responden al
mirarlas.** Guardarlos crearía una segunda verdad que envejece, y el modelo de
datos aprobado lo dice así.
"""
import os

from django.db import models


class Proyecto(models.Model):
    """Un proyecto que la plataforma administra. Su código sigue donde estaba."""

    SIN_EMPEZAR = "sin empezar"

    identificador = models.CharField(max_length=120, unique=True)
    nombre = models.CharField(max_length=200)
    ruta_codigo = models.CharField(max_length=500)
    # La misma carpeta escrita de dos maneras es la misma carpeta: acá va la
    # forma comparable, y en `ruta_codigo` la que el usuario escribió.
    ruta_normalizada = models.CharField(max_length=500, db_index=True)
    version_reglas = models.CharField(max_length=40, blank=True)
    conectado = models.CharField(max_length=20)
    # Vacío mientras el proyecto esté conectado. Con fecha, está desconectado y
    # su documentación se quedó donde estaba. **La marca vive también en la
    # ficha**, no solo acá: si viviera solo en la base, rehacer el índice
    # resucitaría al proyecto (`DA-01`).
    desconectado = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    @property
    def ruta_viva(self):
        """Si la carpeta de su código todavía existe. Se calcula, no se guarda."""
        return os.path.isdir(self.ruta_codigo)

    @property
    def estado(self):
        """En qué va, según lo que la plataforma tenga **traído** de él.

        Se calcula al pedirlo y no se guarda: un estado guardado a mano
        envejece y miente. Y se calcula sin abrir la carpeta del proyecto, que
        es lo que `CA-01` de `HU-003` exige.
        """
        from . import estado as calculo
        return calculo.de(self).resumen

    @property
    def detalle_del_estado(self):
        """El estado completo: etapas, fases, aprobaciones y lo ilegible."""
        from . import estado as calculo
        return calculo.de(self)

    @property
    def adopto_el_estandar(self):
        return bool(self.version_reglas)

    @property
    def esta_conectado(self):
        return not self.desconectado
