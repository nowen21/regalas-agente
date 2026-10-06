# -*- coding: utf-8 -*-
"""Guarda en la base lo nuevo de los registros de Claude Code de cada proyecto.

    python manage.py leer_consumo
    python manage.py leer_consumo --proyecto agente

Lo de todos los días lo guarda `vigilar_consumo` en cuanto se escribe
(`EP-025·HU-011`); esta orden lee de una vez lo que haga falta, por ejemplo
después de borrar el avance de lectura. La suma del total es la de `presupuesto.py`.
"""
from django.core.management.base import BaseCommand

from core.comun.consola import preparar_salida
from core.enganches.presupuesto import Presupuesto
from core.proyectos.models import Proyecto

from ...formato import miles
from ...guardar import GuardadoDeConsumo


def consumo_de(llamada):
    """La fila guardada, como la suma `presupuesto.py`."""
    return {"entrada": llamada.entrada + llamada.cache_creada, "salida": llamada.salida,
            "cache": llamada.cache_leida}


class Command(BaseCommand):
    help = "Guarda lo nuevo de los registros de Claude Code de cada proyecto activo."

    def add_arguments(self, parser):
        parser.add_argument("--proyecto", help="solo el proyecto con este nombre")

    def handle(self, *args, proyecto=None, **opciones):
        preparar_salida()
        proyectos = Proyecto.objects.filter(activo=True)
        if proyecto:
            proyectos = proyectos.filter(nombre=proyecto)
        if not proyectos.exists():
            self.stdout.write("No hay proyectos activos registrados en Cimiento.")
            return
        for registrado in proyectos:
            guardado = GuardadoDeConsumo(registrado)
            nuevo = guardado.leer_todo()
            total = Presupuesto.resumen(consumo_de(l) for l in registrado.llamadas.all())
            self.stdout.write(
                f"{registrado.nombre}: {nuevo['leidos']} archivo(s) con algo nuevo; "
                f"{nuevo['llamadas']} llamada(s), {nuevo['enganches']} enganche(s) y "
                f"{nuevo['archivos']} archivo(s) leído(s) nuevos. Total guardado: "
                f"{miles(total['turnos'])} llamada(s), {miles(total['entrada'])} tokens de entrada, "
                f"{miles(total['salida'])} de salida y {miles(total['cache'])} leídos de caché.")
