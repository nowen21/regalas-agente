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
        """En qué va, según lo que la plataforma tenga escrito de él.

        En esta fase siempre responde `sin empezar`, y eso es un dato y no una
        pantalla vacía: todavía no hay documentos que mirar. Calcularlo de
        verdad es la fase G.
        """
        return self.SIN_EMPEZAR

    @property
    def adopto_el_estandar(self):
        return bool(self.version_reglas)
