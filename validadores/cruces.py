#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El cruce entre dos módulos se registra en los dos — `13·DOC7`.

Cuando la especificación de un módulo declara que consume otro, el consumido tiene que
anotarlo en su historial cruzado. La regla lo dice sin medias tintas: **los dos
lados o ninguno**, porque si solo se escribe en uno, el conocimiento queda
atrapado ahí y el módulo consumido cambia sin enterarse de quién dependía de él.

Lo que se comprueba es el registro, no la narrativa: que a cada declaración de un
lado le corresponda la del otro. Si el cruce está bien contado —qué se consume y
por qué, qué cambió y cuándo— lo lee una persona.

  A dice "consumo de B"  →  B tiene a A en su historial cruzado.
  B dice "A consume"     →  A lo declara en su tabla de consumos.

De dónde salen: de la tabla de módulos de `.agente/dominio.md`, donde el proyecto
declara dónde vive la especificación de cada uno. Sin esa tabla no hay qué cruzar,
y se dice.

Todo **AVISO**: la especificación puede estar a medio escribir, y una fase en curso es
exactamente eso.
"""
import os

import declaracion
import comun
from comun import AVISO, Hallazgo, filas_de, leer, valor_limpio

# La fila que dice "acá no hay nada", que no es lo mismo que una tabla vacía.
_NINGUNO = ("ninguno", "ninguna", "no aplica", "n/a")


def _texto(ruta):
    try:
        return leer(ruta)
    except OSError:
        return ""


def _modulos(celda):
    """Los módulos nombrados en una celda, en minúsculas y sin adornos."""
    valor = valor_limpio(celda)
    if not valor or valor.lower() in _NINGUNO:
        return []
    return [p.strip().strip("`").lower() for p in valor.split(",") if p.strip()]


def consume(texto):
    """Los módulos que esta especificación declara consumir."""
    salida = []
    for _, fila in filas_de(texto, "módulo", "qué consume", "por qué"):
        salida += _modulos(fila["módulo"])
    return salida


def historial(texto):
    """Los módulos que esta especificación registra como consumidores suyos."""
    salida = []
    for _, fila in filas_de(texto, "fecha", "módulo que consume"):
        salida += _modulos(fila["módulo que consume"])
    return salida


def validar(proyecto):
    proyecto = os.path.abspath(proyecto)
    d = declaracion.leer_declaracion(proyecto)
    if not d.modulos:
        return [Hallazgo(
            AVISO, os.path.join(proyecto, declaracion.DOMINIO), 0,
            f"el proyecto no declara sus módulos en `{declaracion.DOMINIO}`: "
            f"no hay especificaciones que cruzar (DOC7)")]

    especificaciones = {}
    for modulo in d.modulos:
        if not modulo.especificacion:
            continue
        ruta = os.path.join(proyecto, *modulo.especificacion.split("/"))
        texto = _texto(ruta)
        if texto:
            especificaciones[modulo.nombre.lower()] = (modulo, modulo.especificacion, texto)

    hallazgos = []
    for nombre, (modulo, ruta, texto) in sorted(especificaciones.items()):
        for otro in consume(texto):
            if otro not in especificaciones:
                hallazgos.append(Hallazgo(
                    AVISO, ruta, 0,
                    f"declara que consume `{otro}`, que no es un módulo "
                    f"declarado del proyecto (DOC7)"))
                continue
            if nombre not in historial(especificaciones[otro][2]):
                hallazgos.append(Hallazgo(
                    AVISO, especificaciones[otro][1], 0,
                    f"`{modulo.nombre}` declara que lo consume y su historial "
                    f"cruzado no lo registra — DOC7 pide los dos lados"))

        for otro in historial(texto):
            if otro in especificaciones and nombre not in consume(especificaciones[otro][2]):
                hallazgos.append(Hallazgo(
                    AVISO, especificaciones[otro][1], 0,
                    f"`{modulo.nombre}` lo registra como consumidor y esta especificación "
                    f"no declara qué consume de él — DOC7 pide los dos lados"))
    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada()
