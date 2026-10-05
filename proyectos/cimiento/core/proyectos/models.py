# -*- coding: utf-8 -*-
"""Un proyecto que Cimiento administra.

**No se borra, se desactiva.** El gasto de tokens y los niveles de las reglas
de un proyecto siguen siendo su historia aunque ya no se trabaje en él.

**La ruta se compara sin distinguir mayúsculas.** En Windows `C:\\X` y `c:\\x` son
la misma carpeta, y el índice único de la base no lo sabe: lo revisa `clean`.
"""
import os

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from .claude import carpeta_de_claude
from .limites import LIMITE_ARCHIVO, LIMITE_ENGANCHE


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ruta = models.CharField(max_length=500, unique=True,
                            help_text="La carpeta del proyecto en esta máquina.")
    carpeta_claude = models.CharField(
        "carpeta de Claude Code", max_length=500, editable=False,
        help_text="Dentro de ~/.claude/projects/; se calcula desde la ruta.")
    limite_enganche = models.PositiveIntegerField(
        "límite por enganche", default=LIMITE_ENGANCHE, validators=[MinValueValidator(1)],
        help_text="Tokens que puede agregar un enganche antes de avisar.")
    limite_archivo = models.PositiveIntegerField(
        "límite por archivo", default=LIMITE_ARCHIVO, validators=[MinValueValidator(1)],
        help_text="Tokens que puede ocupar un archivo leído antes de avisar.")
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def clean(self):
        if not self.ruta:
            return
        self.ruta = os.path.abspath(self.ruta.strip())
        if not os.path.isdir(self.ruta):
            raise ValidationError({"ruta": "La carpeta no existe en esta máquina."})
        repetida = Proyecto.objects.exclude(pk=self.pk).filter(ruta__iexact=self.ruta).first()
        if repetida:
            raise ValidationError({"ruta": f"Esta carpeta ya está registrada como «{repetida.nombre}»."})

    def save(self, *args, **kwargs):
        self.carpeta_claude = carpeta_de_claude(self.ruta)
        super().save(*args, **kwargs)
