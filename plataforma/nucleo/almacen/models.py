# -*- coding: utf-8 -*-
"""El índice. No es la fuente: se puede borrar entero y rehacer (`DA-01`).

Por eso acá no hay ningún dato que no esté también en el texto de `datos/`. Si
algún día aparece un campo que solo viva acá, la decisión `DA-01` dejó de
cumplirse y hay que mirarla de nuevo.
"""
from django.db import models


class Anotado(models.Model):
    """Un archivo de `datos/`, con lo mínimo para encontrarlo sin abrirlo."""

    nombre = models.CharField(max_length=500, unique=True)
    huella = models.CharField(max_length=64)
    tamano = models.IntegerField()
    visto = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
