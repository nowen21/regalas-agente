# -*- coding: utf-8 -*-
"""`EP-005·HU-019` · Anota el hash del commit en la fase que ese commit cierra.

**La estación 12 del ciclo es «commit», y el commit ocurre después de que el
agente termina de escribir.** En ese momento ya reportó, el usuario aprueba, se
commitea — y nadie vuelve al `estado-fase.md` a marcar la casilla. No es
descuido: es la forma del ciclo. Solo el 2026-08-27 se marcó a mano cinco veces.

## Lo que se midió antes de construir, y cambió el alcance

De los **140** `estado-fase.md` del árbol: 11 con la estación 12 marcada, 23 sin
marcar, y **106 sin la fila siquiera** (`S-066`). Tres de cada cuatro fases **no
tienen dónde marcar**, así que esto actúa sobre una minoría — y decirlo es parte
del trabajo, porque un automatismo que parece cubrirlo todo es peor que ninguno.

## Por qué el hash queda fuera de su propio commit

**Antes del commit el hash no existe**, así que esto corre después y **el
archivo queda modificado y sin guardar**. Se midió, y las otras dos salidas se
descartaron con argumento: reescribir el commit se muerde la cola —cambia el
hash— y hacer un segundo commit automático cruza `00·N1`. Está en `S-067`.

**No corrige, no mueve, no borra.** Escribe una casilla vacía y nada más.
"""
import io
import os
import re

import comun

# La fila de la estación 12 en la tabla de estaciones del molde `10`.
# Se exige la tabla: **no se inventa una fila donde no hay ninguna**, que es lo
# que pasaría en 106 de los 140 documentos del árbol.
_FILA_12 = re.compile(
    r"^(\|\s*12\s*\|[^|\n]*\|[^|\n]*\|)(\s*)([^|\n]*?)(\s*\|)\s*$", re.M)

# Ya marcada: trae un ✅ o algo con pinta de hash.
_YA_MARCADA = re.compile(r"✅|`[0-9a-f]{7,40}`")


def _leer(ruta):
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def tiene_fila_de_estacion(texto):
    """`True` si el documento trae la fila 12 donde escribir."""
    return bool(_FILA_12.search(texto or ""))


def ya_esta_marcada(texto):
    """`True` si la casilla ya trae un hash o un visto.

    **No se pisa.** El hash dice *qué commit cerró la fase*; reescribirlo con el
    último la haría apuntar a una corrección de una coma.
    """
    dice = _FILA_12.search(texto or "")
    return bool(dice and _YA_MARCADA.search(dice.group(3)))


def marcar(texto, hash_corto):
    """El texto con la casilla 12 marcada, o `None` si no hay que tocarlo.

    Devuelve `None` —y no el mismo texto— para que quien llame **no pueda
    reescribir el archivo sin querer**: sin cambio no hay escritura.
    """
    if not texto or not hash_corto:
        return None
    if not tiene_fila_de_estacion(texto) or ya_esta_marcada(texto):
        return None

    def reemplazo(m):
        return "%s ✅ `%s` |" % (m.group(1), hash_corto)

    nuevo = _FILA_12.sub(reemplazo, texto, count=1)
    return nuevo if nuevo != texto else None


def fase_de(ruta_relativa):
    """La carpeta de la fase a la que pertenece un archivo, o `""`.

    Se reconoce por su forma —`X-EP-nnn-HU-nnn-…`— y no por una lista: así
    sirve igual en cualquier proyecto que herede el estándar.
    """
    partes = ruta_relativa.replace("\\", "/").split("/")
    for i, tramo in enumerate(partes):
        if re.match(r"^[A-Z]{1,3}(-[A-Z]{1,3})?-EP-\d+-HU-\d+-.+$", tramo):
            return "/".join(partes[:i + 1])
    return ""


def fases_que_toca(archivos):
    """Las carpetas de fase que aparecen entre los archivos de un commit."""
    vistas = []
    for archivo in archivos:
        carpeta = fase_de(archivo)
        if carpeta and carpeta not in vistas:
            vistas.append(carpeta)
    return vistas


def marcar_las_fases(proyecto, archivos, hash_corto, cerrada_en_git):
    """Escribe el hash en las fases que el commit cierra. Devuelve las tocadas.

    `cerrada_en_git(ruta_cierre)` dice si el documento de cierre de esa fase ya
    está guardado: **una fase cuyo cierre no está en git no se marca**, porque
    diría que se commiteó algo que no se commiteó.
    """
    tocadas = []
    for carpeta in fases_que_toca(archivos):
        ruta = os.path.join(proyecto, *carpeta.split("/"))
        estado = os.path.join(ruta, "estado-fase.md")
        cierre = os.path.join(ruta, "funcionalidad_implementada.md")
        if not os.path.isfile(estado) or not cerrada_en_git(cierre):
            continue
        nuevo = marcar(_leer(estado), hash_corto)
        if nuevo is None:
            continue
        try:
            with io.open(estado, "w", encoding="utf-8", newline="\n") as f:
                f.write(nuevo)
        except OSError:
            continue                    # no se detiene nada por no poder escribir
        tocadas.append(carpeta)
    return tocadas


if __name__ == "__main__":
    comun.no_es_punto_de_entrada(
        la_corre="el enganche `post-commit` de git, después de cada commit")
