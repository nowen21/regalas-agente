# -*- coding: utf-8 -*-
"""`EP-029·HU-001` · El estado de la revisión de pruebas de cada proyecto.

**Dos tablas** (análisis 1 del pendiente 141, punto 3): si el proyecto tiene la
parte que revisa, que la pone el instalador (`HU-003`), y cada revisión que se
hizo, con su fecha, la herramienta, qué parte quedó sin pruebas archivo por
archivo y cómo les fue a las pruebas de navegador (`HU-005`).

**Vive en la base de Cimiento** (acuerdo 9): el proyecto la consulta ahí.
"""
from django.db import models
from django.utils import timezone

from core.proyectos.models import Proyecto


class PruebasDelProyecto(models.Model):
    """Lo que Cimiento sabe de las pruebas de un proyecto, fuera de cada revisión."""

    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE, related_name="pruebas")
    tiene_parte = models.BooleanField(
        "tiene la parte que revisa", default=False,
        help_text="La pone el instalador; sin ella, el proyecto no se puede revisar.")
    # `EP-029·HU-003` · Si la herramienta la puso Cimiento: solo así la quita al
    # desinstalar, porque la que ya tenía el proyecto es suya (`02·F30`).
    instalada_por_cimiento = models.BooleanField(default=False)
    # `EP-029·HU-002` · Mientras la revisión corre aparte, la página dice «Revisando».
    revisando_desde = models.DateTimeField(null=True, blank=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "pruebas de los proyectos"

    def __str__(self):
        return "Pruebas de %s" % self.proyecto

    @classmethod
    def de(cls, proyecto):
        """El de `proyecto`, creado si no existía."""
        return cls.objects.get_or_create(proyecto=proyecto)[0]


class Revision(models.Model):
    """Una revisión: qué parte del proyecto quedó sin pruebas en ese momento."""

    HECHA, SIN_MEDICION, FALLO = "hecha", "sin medición", "falló"
    RESULTADOS = [(HECHA, "Hecha"), (SIN_MEDICION, "Sin medición"), (FALLO, "Falló")]
    PASARON, FALLARON, SIN_PRUEBAS = "pasaron", "fallaron", "sin pruebas"
    NAVEGADOR = [(PASARON, "Pasaron"), (FALLARON, "Fallaron"), (SIN_PRUEBAS, "Sin pruebas de navegador")]

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="revisiones")
    fecha = models.DateTimeField(default=timezone.now)
    # `EP-029·HU-007` · El programa revisado, como carpeta dentro del proyecto
    # (`proyectos/rni-back`); vacío si el proyecto es uno solo en su raíz.
    programa = models.CharField(max_length=300, blank=True)
    herramienta = models.CharField(max_length=100, blank=True,
                                   help_text="Con qué se revisó: coverage.py, PHPUnit, ng test…")
    resultado = models.CharField(max_length=20, choices=RESULTADOS, default=HECHA)
    porcentaje = models.FloatField(null=True, blank=True,
                                   help_text="Qué parte del programa tiene pruebas, de 0 a 100.")
    archivos = models.JSONField(default=list, blank=True,
                                help_text="Cada archivo con su porcentaje y sus líneas sin pruebas.")
    mensaje = models.TextField(blank=True, help_text="Qué pasó, en palabras sencillas.")
    navegador = models.CharField(max_length=20, choices=NAVEGADOR, blank=True,
                                 help_text="Cómo les fue a las pruebas de navegador; vacío si no se corrieron.")
    navegador_detalle = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "revisión de pruebas"
        verbose_name_plural = "revisiones de pruebas"

    def __str__(self):
        return "%s · %s" % (self.proyecto, timezone.localtime(self.fecha).strftime("%Y-%m-%d %H:%M"))

    @classmethod
    def ultima(cls, proyecto):
        """La revisión más reciente del proyecto, o `None` si nunca se revisó."""
        return cls.objects.filter(proyecto=proyecto).first()

    @classmethod
    def ultimas(cls, proyecto):
        """`EP-029·HU-007` · Las revisiones de la última vez, una por programa."""
        ultima = cls.ultima(proyecto)
        return list(cls.objects.filter(proyecto=proyecto, fecha=ultima.fecha).order_by("programa")) if ultima else []

    @staticmethod
    def la_de_menos_pruebas(revisiones):
        """La que tiene menos pruebas: primero las que no se pudieron medir (acuerdo 2 del análisis 4)."""
        if not revisiones:
            return None
        return min(revisiones, key=lambda r: -1 if r.porcentaje is None else r.porcentaje)


AL_DIA, VENCIDA, NUNCA = "Al día", "Vencida", "Nunca se ha revisado"


def como_va(ultima, dias, ahora=None):
    """`EP-029·HU-002` · Si la revisión está al día, vencida o nunca se hizo, según
    cada cuántos días toca (`dias_revision`, `EP-029·HU-001`)."""
    if ultima is None:
        return NUNCA
    ahora = ahora or timezone.now()
    return VENCIDA if ahora - ultima.fecha > timezone.timedelta(days=dias) else AL_DIA
