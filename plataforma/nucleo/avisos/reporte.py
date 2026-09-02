# -*- coding: utf-8 -*-
"""Cómo va cada proyecto, con la misma medida — `F-030`.

**Comparar proyectos distintos con la misma medida engaña si no se dice qué
mide.** Está en la ficha de `F-030`, y la respuesta no es dejar de comparar: es
que el reporte lleve encima, siempre, la definición de cada columna. Por eso
`QUE_MIDE` no es documentación suelta: sale impresa con la tabla.

**Un proyecto sin datos aparece así, no en cero.** Cero fases terminadas de cero
es una división que no existe, y escribir «0 %» ahí dice que el proyecto va mal
cuando lo que pasa es que no se sabe. Es la misma distinción de `S-107`: un
estado que admite «no se sabe» necesita su propio nombre.
"""
import os

from nucleo.avisos import core
from nucleo.ciclo_de_vida import estaciones

SIN_DATOS = "sin datos"

QUE_MIDE = (
    ("avance", "fases con las trece estaciones pasadas, sobre el total de "
               "fases. No mide funcionalidad entregada: mide fases cerradas"),
    ("deuda", "avisos vivos: fases detenidas, historias sin fase y "
              "funcionalidades construidas sin verificar"),
    ("vencida", "de esa deuda, la parte que lleva más de %d días sin moverse. "
                "**El estándar nunca le puso fecha a una deuda**, así que "
                "«vencida» acá quiere decir eso y nada más" % core.DIAS),
    ("quietas", "fases sin cerrar que no dicen desde cuándo llevan quietas: no "
                "se cuentan como vencidas ni como al día"),
)


def de_un_proyecto(identificador, raiz, hoy, dias=core.DIAS):
    """La fila de un proyecto. Los números que no se pueden calcular, `None`."""
    fases = estaciones.de_un_proyecto(str(raiz))
    cuenta = estaciones.resumen(fases)
    avisos = core.de_un_proyecto(raiz, hoy, dias, tope=10 ** 6)
    detenidas = avisos["por_clase"].get(core.DETENIDA, 0)
    quietas = len([una for una in fases
                   if una["actual"] != estaciones.TERMINADA
                   and estaciones.detenida_desde(una, hoy) < 0])

    return {
        "proyecto": identificador,
        "fases": cuenta["cuantas"],
        "terminadas": cuenta["terminadas"],
        # `None`, no cero: sin fases no hay avance que medir.
        "avance": (None if not cuenta["cuantas"]
                   else round(100.0 * cuenta["terminadas"] / cuenta["cuantas"], 1)),
        "deuda": avisos["cuantos"],
        "vencida": detenidas,
        "quietas": quietas,
        "callados": avisos["callados"],
    }


def de_todos(hoy, dias=core.DIAS):
    """Una fila por proyecto conectado, del que peor va al que mejor.

    Los que no tienen datos van **al final**, y no primeros: no son los peores,
    son los que no se sabe.
    """
    from nucleo.proyectos.models import Proyecto
    filas = []
    for registrado in Proyecto.objects.all().order_by("identificador"):
        filas.append(de_un_proyecto(registrado.identificador,
                                    registrado.ruta_codigo, hoy, dias))
    filas.sort(key=lambda una: (una["avance"] is None,
                                una["avance"] if una["avance"] is not None else 0,
                                una["proyecto"]))
    return filas


def como_se_escribe(valor):
    """Un número, o `sin datos` cuando no hay con qué calcularlo."""
    return SIN_DATOS if valor is None else "%.1f %%" % valor


def dicho(filas):
    """El reporte entero, con la definición de cada columna debajo."""
    if not filas:
        return ("No hay ningún proyecto conectado. No es un cero: es que "
                "todavía no se ha conectado ninguno.")
    lineas = ["%-32s %10s %7s %8s %8s" % ("proyecto", "avance", "deuda",
                                          "vencida", "quietas")]
    for una in filas:
        lineas.append("%-32s %10s %7d %8d %8d" % (
            una["proyecto"][:32], como_se_escribe(una["avance"]),
            una["deuda"], una["vencida"], una["quietas"]))
    lineas.append("")
    lineas.append("Qué mide cada columna:")
    for nombre, definicion in QUE_MIDE:
        lineas.append("  %-9s %s" % (nombre, definicion))
    sin_datos = [una["proyecto"] for una in filas if una["avance"] is None]
    if sin_datos:
        lineas.append("")
        lineas.append("Sin datos (no es cero, es que no hay fases escritas): %s"
                      % ", ".join(sin_datos))
    return "\n".join(lineas)
