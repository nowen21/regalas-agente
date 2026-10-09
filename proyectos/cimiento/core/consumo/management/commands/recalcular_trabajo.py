# -*- coding: utf-8 -*-
"""`manage.py recalcular_trabajo`: vuelve a sacar el trabajo de los mensajes ya guardados.

    python manage.py recalcular_trabajo

`EP-025·HU-028` · El trabajo de un mensaje sale del análisis que dice su aviso,
de lo que tocó su turno o de su conversación (`guardar.poner_trabajo`). Los
mensajes guardados antes de esa historia lo sacaban solo de las rutas, y solo de
fases `A-`. Esta orden vuelve a leer las líneas de sesión de la base, archivo
por archivo, y les pone el trabajo con las reglas de hoy. El mensaje cuyas
líneas no están en la base conserva el trabajo que tenía, y si no tenía, queda
en su conversación (fase B). Correrla otra vez da lo mismo.
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from core.comun.consola import preparar_salida

from ...formato import miles
from ...guardar import poner_trabajo
from ...lector import LectorDeClaudeCode
from ...models import LineaDeSesion, Pedido
from ...trabajo import DEL_TITULO, trabajo_de_la_conversacion


def recalcular():
    """`(archivos, mensajes)` revisados."""
    archivos = mensajes = 0
    for archivo in LineaDeSesion.objects.values_list("archivo", flat=True).distinct().order_by("archivo"):
        textos = LineaDeSesion.objects.filter(archivo=archivo).order_by("posicion").values_list("texto", flat=True)
        lectura = LectorDeClaudeCode(archivo).leer_lineas(list(textos))
        sesiones = {p.sesion for p in lectura.pedidos}
        identificadores = {p.identificador[:64] for p in lectura.pedidos}
        if not identificadores:
            continue
        pedidos = {p.identificador: p for p in
                   Pedido.objects.filter(sesion__in=sesiones, identificador__in=identificadores)}
        with transaction.atomic():
            Pedido.objects.filter(pk__in=[p.pk for p in pedidos.values()]).update(trabajo="", origen="")
            for pedido in pedidos.values():
                pedido.trabajo, pedido.origen = "", ""
            poner_trabajo(pedidos, lectura, list(pedidos.values()))
        archivos += 1
        mensajes += len(pedidos)
    # Fase B · El mensaje cuyas líneas ya no están (Claude Code borró su `.jsonl`) queda en su
    # conversación, por el código: ninguno se queda sin trabajo.
    for pedido in Pedido.objects.filter(trabajo=""):
        pedido.trabajo, pedido.origen = trabajo_de_la_conversacion(pedido.sesion), DEL_TITULO
        pedido.save(update_fields=["trabajo", "origen"])
        mensajes += 1
    return archivos, mensajes


class Command(BaseCommand):
    help = "Vuelve a sacar el trabajo de los mensajes ya guardados, desde las líneas de sesión de la base."

    def handle(self, *args, **opciones):
        preparar_salida()
        antes = Pedido.objects.filter(trabajo="").count()
        archivos, mensajes = recalcular()
        despues = Pedido.objects.filter(trabajo="").count()
        total = Pedido.objects.count()
        self.stdout.write("%s mensaje(s) de %s archivo(s) recalculados. Sin trabajo: %s antes, %s ahora, de %s."
                          % (miles(mensajes), miles(archivos), miles(antes), miles(despues), miles(total)))
