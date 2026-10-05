# -*- coding: utf-8 -*-
"""El gasto de tokens guardado: lo que Claude Code borra a los 30 días queda acá.

Las llamadas traen tokens contados por Claude Code. Los enganches y los
archivos leídos traen caracteres, y sus tokens son una estimación
(`lector.CARACTERES_POR_TOKEN`). No se guarda texto.
"""
from django.db import models

from core.proyectos.models import Proyecto

from .lector import estimar_tokens


class Pedido(models.Model):
    """`EP-025·HU-010` · Un mensaje del usuario: su palabra de `01·C28` y el trabajo
    que tocó su turno. No se guarda su texto."""

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="pedidos")
    sesion = models.CharField(max_length=64, db_index=True)
    identificador = models.CharField(max_length=64)
    fecha = models.DateTimeField(null=True, db_index=True)
    palabra = models.CharField("palabra clave", max_length=40, blank=True)
    trabajo = models.CharField(max_length=200, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["sesion", "identificador"], name="un_pedido_por_mensaje")]


class Llamada(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="llamadas")
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True, related_name="llamadas")
    # El tipo de agente auxiliar que la hizo (`agentType` de su meta), o vacío.
    agente = models.CharField(max_length=100, blank=True)
    sesion = models.CharField(max_length=64, db_index=True)
    mensaje = models.CharField(max_length=100)
    fecha = models.DateTimeField(null=True, db_index=True)
    modelo = models.CharField(max_length=100, blank=True)
    entrada = models.PositiveIntegerField(default=0)
    cache_creada = models.PositiveIntegerField(default=0)
    cache_leida = models.PositiveIntegerField(default=0)
    salida = models.PositiveIntegerField(default=0)
    auxiliar = models.BooleanField(default=False)
    # La misma llamada llega por el `.jsonl` y por la telemetría; esto las une.
    solicitud = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["sesion", "mensaje"], name="una_llamada_por_mensaje"),
                       models.UniqueConstraint(fields=["sesion", "solicitud"], name="una_llamada_por_solicitud")]

    @property
    def total(self):
        return self.entrada + self.cache_creada + self.cache_leida + self.salida


class GastoDeEnganche(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="gastos_de_enganche")
    sesion = models.CharField(max_length=64, db_index=True)
    identificador = models.CharField(max_length=64)
    fecha = models.DateTimeField(null=True, db_index=True)
    nombre = models.CharField(max_length=200)
    evento = models.CharField(max_length=50, blank=True)
    caracteres = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["sesion", "identificador"], name="un_gasto_por_enganche")]

    @property
    def tokens_estimados(self):
        return estimar_tokens(self.caracteres)


class GastoDeArchivo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="gastos_de_archivo")
    sesion = models.CharField(max_length=64, db_index=True)
    identificador = models.CharField(max_length=64)
    fecha = models.DateTimeField(null=True, db_index=True)
    ruta = models.CharField(max_length=500)
    caracteres = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["sesion", "identificador"], name="un_gasto_por_lectura")]

    @property
    def tokens_estimados(self):
        return estimar_tokens(self.caracteres)


class GastoDeHerramienta(models.Model):
    """`EP-025·HU-010` · Un uso de una herramienta y el tamaño de su resultado."""

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="gastos_de_herramienta")
    sesion = models.CharField(max_length=64, db_index=True)
    identificador = models.CharField(max_length=64)
    fecha = models.DateTimeField(null=True, db_index=True)
    nombre = models.CharField(max_length=100)
    caracteres = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["sesion", "identificador"], name="un_gasto_por_herramienta")]

    @property
    def tokens_estimados(self):
        return estimar_tokens(self.caracteres)


class AvanceDeLectura(models.Model):
    """Hasta qué byte se leyó cada `.jsonl`, y cómo estaba el archivo entonces."""

    archivo = models.CharField(max_length=500, unique=True)
    # El mensaje en curso donde quedó: la lectura siguiente le une las llamadas que faltan.
    pedido = models.CharField(max_length=64, blank=True)
    posicion = models.PositiveBigIntegerField(default=0)
    tamano = models.PositiveBigIntegerField(default=0)
    modificado = models.FloatField(default=0)
    actualizado = models.DateTimeField(auto_now=True)
