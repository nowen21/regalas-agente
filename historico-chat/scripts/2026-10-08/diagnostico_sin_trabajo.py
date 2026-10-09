# -*- coding: utf-8 -*-
"""`EP-025·HU-028`, fase B · Por qué cada mensaje de los últimos días quedó «(sin trabajo)».

Uso, desde la raíz del repositorio:
    proyectos/cimiento/.venv/Scripts/python.exe historico-chat/scripts/2026-10-08/diagnostico_sin_trabajo.py [días]

Vuelve a leer las líneas de sesión de la base y clasifica cada mensaje sin trabajo
por su causa. Solo lee: no cambia nada.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import timedelta

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

import django  # noqa: E402

django.setup()

from django.utils import timezone  # noqa: E402

from core.consumo.lector import LectorDeClaudeCode  # noqa: E402
from core.consumo.models import LineaDeSesion, Pedido  # noqa: E402


def nombre(ruta):
    """El archivo, o «orden de consola» si es una orden."""
    if len(ruta) > 150 or " " in ruta.strip():
        return "(orden de consola)"
    return re.split(r"[\\/]", ruta)[-1][:60]


def main(dias=7):
    vacios = list(Pedido.objects.filter(fecha__gte=timezone.now() - timedelta(days=dias), trabajo="")
                  .select_related("proyecto").order_by("fecha"))
    print("Mensajes sin trabajo en %d días: %d" % (dias, len(vacios)))
    por_sesion = defaultdict(list)
    for p in vacios:
        por_sesion[p.sesion].append(p)

    causas, tocados, palabras, titulos = Counter(), Counter(), Counter(), {}
    por_causa = defaultdict(Counter)
    for sesion, pedidos in por_sesion.items():
        archivos = list(LineaDeSesion.objects.filter(archivo__contains=sesion)
                        .values_list("archivo", flat=True).distinct())
        if not archivos:
            causas["la conversación no tiene sus líneas en la base"] += len(pedidos)
            por_causa[sesion]["sin líneas"] += len(pedidos)
            continue
        rutas, textos = {}, []
        for archivo in archivos:
            lineas = list(LineaDeSesion.objects.filter(archivo=archivo).order_by("posicion")
                          .values_list("texto", flat=True))
            textos += lineas
            rutas.update(LectorDeClaudeCode(archivo).leer_lineas(lineas).rutas)
        for texto in textos:
            if '"ai-title"' in texto or '"summary"' in texto:
                try:
                    dato = json.loads(texto)
                except ValueError:
                    continue
                titulos[sesion] = dato.get("aiTitle") or dato.get("summary") or titulos.get(sesion)
        primero = Pedido.objects.filter(sesion=sesion).exclude(trabajo="").order_by("fecha").first()
        for p in pedidos:
            palabras[p.palabra or "(sin palabra)"] += 1
            if p.identificador in rutas:
                causa = "tocó archivos, ninguno de una fase o un análisis"
                for ruta in rutas[p.identificador]:
                    tocados[nombre(ruta)] += 1
            elif primero is None:
                causa = "no tocó nada, en una conversación sin ningún trabajo"
            elif p.fecha < primero.fecha:
                causa = "no tocó nada, antes del primer trabajo de su conversación"
            else:
                causa = "no tocó nada, y el mensaje anterior tampoco tenía trabajo"
            causas[causa] += 1
            por_causa[sesion][causa] += 1

    print("\nPor causa:")
    for causa, n in causas.most_common():
        print("  %5d  %s" % (n, causa))
    print("\nPor palabra clave:", palabras.most_common(10))
    print("\nLo que más tocaron sin ser de una fase:", tocados.most_common(20))
    print("\nConversaciones (%d), con su título si Claude Code lo dejó:" % len(por_sesion))
    for sesion, pedidos in sorted(por_sesion.items(), key=lambda s: -len(s[1])):
        print("  %4d  %s  %s  %s" % (len(pedidos), sesion[:8], pedidos[0].proyecto.nombre, titulos.get(sesion, "(sin título)")))
        print("        %s" % dict(por_causa[sesion]))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
