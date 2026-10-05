# -*- coding: utf-8 -*-
"""El nivel de una regla en un proyecto, y la historia de sus cambios.

**Sin fila, la regla frena**, que es lo que hacía siempre: la tabla solo guarda
lo que alguien cambió. El freno (`EP-025·HU-005`) la lee por proyecto y ID.

**El ID va completo**, `02·F8`, como el freno nombra la regla en sus avisos.
"""
from django.conf import settings
from django.db import models

from core.proyectos.models import Proyecto

FRENA, AVISA, APAGADA = "frena", "avisa", "apagada"
NIVELES = [(FRENA, "Frena"), (AVISA, "Avisa"), (APAGADA, "Apagada")]


class NivelDeRegla(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="niveles")
    regla = models.CharField(max_length=20)
    nivel = models.CharField(max_length=10, choices=NIVELES, default=FRENA)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["proyecto", "regla"], name="un_nivel_por_regla")]

    def __str__(self):
        return f"{self.proyecto} {self.regla}: {self.nivel}"


class CambioDeNivel(models.Model):
    """Quién cambió qué nivel y cuándo. No se edita ni se borra."""

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="cambios_de_nivel")
    regla = models.CharField(max_length=20)
    anterior = models.CharField(max_length=10, choices=NIVELES)
    nuevo = models.CharField(max_length=10, choices=NIVELES)
    cuenta = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha", "-id"]
