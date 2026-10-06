# -*- coding: utf-8 -*-
"""Un proyecto que Cimiento administra.

**No se borra, se desactiva.** El gasto de tokens y los niveles de las reglas
de un proyecto siguen siendo su historia aunque ya no se trabaje en él.

**La ruta se compara sin distinguir mayúsculas.** En Windows `C:\\X` y `c:\\x` son
la misma carpeta, y el índice único de la base no lo sabe: lo revisa `clean`.

**Su configuración va en tres capas** (`EP-025·HU-013`): los ajustes de la base
de Cimiento, los del proyecto y las suspensiones. Los límites de tokens, que
eran columnas del proyecto, son ajustes.
"""
import os

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from . import ajustes as catalogo
from .claude import carpeta_de_claude


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ruta = models.CharField(max_length=500, unique=True,
                            help_text="La carpeta del proyecto en esta máquina.")
    carpeta_claude = models.CharField(
        "carpeta de Claude Code", max_length=500, editable=False,
        help_text="Dentro de ~/.claude/projects/; se calcula desde la ruta.")
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

    def ajustes(self):
        """`{clave: (valor, capa)}` de lo que vale en este proyecto (`EP-025·HU-013`)."""
        return catalogo.efectivos(dict(AjusteBase.objects.values_list("clave", "valor")),
                                  dict(self.ajustes_propios.values_list("clave", "valor")))

    def ajuste(self, clave):
        return self.ajustes()[clave][0]

    def suspensiones_vigentes(self):
        return self.suspensiones.filter(levantada__isnull=True, vence__gt=timezone.now())


class AnalisisPrendido(models.Model):
    """`EP-025·HU-023` · El análisis que recibe la conversación de una sesión.

    Era un archivo de `historico-chat/.estado/` que hubo que editar a mano; lo
    que se maneja desde Cimiento vive en su base (análisis 3 del pendiente 119,
    acuerdo 3). Lo escriben los enganches con PyMySQL, sin Django.
    """

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="analisis_prendidos")
    sesion = models.CharField(max_length=255, help_text="La transcripción de la sesión, relativa al proyecto.")
    analisis = models.CharField(max_length=500, help_text="El análisis, relativo al proyecto.")
    desde = models.PositiveIntegerField(help_text="El primer turno que entra.")
    pausa = models.PositiveIntegerField(null=True, blank=True, help_text="Desde qué turno está en pausa.")
    pausas = models.CharField(max_length=500, blank=True, default="", help_text="Los tramos ya pausados: 3-5,9-9.")
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["proyecto", "sesion"], name="un_analisis_por_sesion")]

    def __str__(self):
        return "%s · %s" % (self.proyecto, self.analisis)


_CLAVES = [(clave, ajuste.titulo) for clave, ajuste in catalogo.AJUSTES.items()]


class AjusteBase(models.Model):
    """`EP-025·HU-013` · Capa 1: el valor común de un ajuste para todos los proyectos."""

    clave = models.CharField(max_length=50, unique=True, choices=_CLAVES)
    valor = models.CharField(max_length=200)

    def __str__(self):
        return "%s = %s" % (self.clave, self.valor)


class AjusteDelProyecto(models.Model):
    """`EP-025·HU-013` · Capa 2: el valor de un ajuste que manda solo en un proyecto."""

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="ajustes_propios")
    clave = models.CharField(max_length=50, choices=_CLAVES)
    valor = models.CharField(max_length=200)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["proyecto", "clave"], name="un_valor_por_ajuste")]

    def __str__(self):
        return "%s · %s = %s" % (self.proyecto, self.clave, self.valor)


class Suspension(models.Model):
    """`EP-025·HU-013` · Capa 3: una regla, o el freno entero, apagada un tiempo.

    Lleva motivo y vencimiento (análisis 3 del pendiente 119, acuerdos 1 y 5).
    No se borra: se levanta, y queda quién y cuándo.
    """

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="suspensiones")
    tipo = models.CharField(max_length=10, choices=catalogo.TIPOS)
    nombre = models.CharField(max_length=30, help_text="El ID de la regla, o «freno».")
    motivo = models.CharField(max_length=500)
    vence = models.DateTimeField()
    creada = models.DateTimeField(auto_now_add=True)
    creada_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
                                   related_name="suspensiones_creadas")
    levantada = models.DateTimeField(null=True, blank=True)
    levantada_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name="suspensiones_levantadas")

    class Meta:
        ordering = ["-creada", "-id"]

    def __str__(self):
        return "%s · %s hasta %s" % (self.proyecto, self.nombre, self.vence)

    def vigente(self, ahora=None):
        return self.levantada is None and self.vence > (ahora or timezone.now())
