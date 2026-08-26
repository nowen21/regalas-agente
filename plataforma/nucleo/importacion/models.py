# -*- coding: utf-8 -*-
"""El índice de lo traído. La fuente son los archivos copiados en `datos/`.

**Un documento se identifica por su ruta dentro del proyecto de origen**, y no
por su contenido. Es lo que hace que traer dos veces no duplique, y que un
documento editado entre con su versión nueva sin crear otro.
"""
from django.db import models


class Traido(models.Model):
    """Un documento que se trajo de un proyecto."""

    proyecto = models.CharField(max_length=120, db_index=True)
    # La ruta dentro del proyecto de origen. Es lo que lo identifica.
    origen = models.CharField(max_length=500)
    tipo = models.CharField(max_length=60, blank=True)
    guardado_en = models.CharField(max_length=600)

    class Meta:
        ordering = ["proyecto", "origen"]
        unique_together = [("proyecto", "origen")]

    def __str__(self):
        return "%s · %s" % (self.proyecto, self.origen)
