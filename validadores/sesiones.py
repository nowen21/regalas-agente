#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Qué archivo tocó cada sesión, para que un commit no se lleve lo ajeno.

**El caso que lo hizo falta.** El 2026-08-22 dos sesiones trabajaron a la vez
sobre este repositorio. Una hizo `git add` de todo el árbol y commiteó: se llevó
un validador a medio corregir —con el criterio que reprobaba documentos
correctos—, un archivo de pruebas sin sus últimos casos y tres carpetas de fase
con los moldes sin llenar. Estuvo ocho minutos publicado. El caso ya estaba
listado como riesgo en el planteamiento del estándar; esta es la primera vez que
se documenta con daño medido, y quedó en el [pendiente 80].

**Lo que se comprueba no es de quién es el commit, sino que mezcle.** Saber qué
sesión está commiteando exigiría que `git` lo supiera, y no lo sabe: el enganche
de `pre-commit` lo lanza `git`, no la herramienta. Pero no hace falta. La señal
que importa es más simple y no necesita identidad: **si lo que entra al commit
lo tocaron dos sesiones distintas, alguien está publicando trabajo que no es
suyo.** Un commit legítimo sale de una sola conversación.

**Avisa, no detiene.** Mezclar puede ser deliberado: retomar el trabajo que otra
sesión dejó a medias es normal, y a veces es justo lo que se quiere. Lo que no
es normal es hacerlo sin darse cuenta. Un enganche que rechaza el commit se
apaga en una tarde, y ese es el defecto más caro de esta casa.

**El registro no se versiona.** Es estado de trabajo, no memoria: vive en
`historico-chat/.tocado/` y está en el `.gitignore`. Versionarlo lo convertiría
en el próximo archivo que dos sesiones se pisan.
"""
import io
import os
import subprocess
import time

import comun
from comun import AVISO, Hallazgo, RAIZ, relativo

CARPETA = os.path.join("historico-chat", ".tocado")

# Una sesión que lleva más de esto sin escribir ya no está viva, y su registro
# no debería hacer ruido en el commit de mañana. Doce horas cubre una jornada
# larga sin cubrir la del día siguiente.
VIGENCIA = 12 * 3600


def _carpeta(raiz):
    return os.path.join(raiz or RAIZ, CARPETA)


def anotar(raiz, sesion, archivo):
    """Deja escrito que `sesion` tocó `archivo`. Sin sesión, no hace nada."""
    if not sesion or not archivo:
        return
    carpeta = _carpeta(raiz)
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)

    rel = os.path.relpath(os.path.abspath(archivo), raiz or RAIZ)
    rel = rel.replace(os.sep, "/")
    if rel.startswith(".."):
        return                      # de otro proyecto: no es asunto de acá

    ruta = os.path.join(carpeta, _limpio(sesion) + ".txt")
    if rel in leer_sesion(ruta):
        # Se vuelve a tocar el mismo archivo todo el tiempo. Sin esto, el
        # registro crece sin límite y la hora de la última escritura deja de
        # decir cuándo la sesión hizo algo nuevo.
        os.utime(ruta, None)
        return
    with io.open(ruta, "a", encoding="utf-8", newline="\n") as f:
        f.write(rel + "\n")


def _limpio(sesion):
    """El identificador, sin nada que pueda salirse de la carpeta."""
    return "".join(c for c in str(sesion) if c.isalnum() or c in "-_")[:64]


def leer_sesion(ruta):
    if not os.path.isfile(ruta):
        return set()
    with io.open(ruta, encoding="utf-8") as f:
        return {l.strip() for l in f if l.strip()}


def registros(raiz=None, ahora=None):
    """`{sesión: {archivos}}` de las sesiones todavía vivas."""
    carpeta = _carpeta(raiz)
    if not os.path.isdir(carpeta):
        return {}
    ahora = ahora if ahora is not None else time.time()
    salida = {}
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.endswith(".txt"):
            continue
        ruta = os.path.join(carpeta, nombre)
        if ahora - os.path.getmtime(ruta) > VIGENCIA:
            continue
        archivos = leer_sesion(ruta)
        if archivos:
            salida[nombre[:-4]] = archivos
    return salida


def preparados(raiz=None):
    """Lo que entra en el commit, en rutas del repositorio."""
    raiz = raiz or RAIZ
    try:
        salida = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only"],
            cwd=raiz, stderr=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError):
        return []
    texto = salida.decode("utf-8", "replace")
    return [l.strip() for l in texto.splitlines() if l.strip()]


def validar_preparados(raiz=None, ahora=None):
    """Avisa si lo que entra al commit lo tocaron dos sesiones. `[Hallazgo]`."""
    raiz = raiz or RAIZ
    entrando = set(preparados(raiz))
    if not entrando:
        return []

    de_quien = {}
    for sesion, archivos in registros(raiz, ahora).items():
        comunes = entrando & archivos
        if comunes:
            de_quien[sesion] = comunes

    if len(de_quien) < 2:
        return []

    detalle = " · ".join(
        "%s: %d" % (sesion[:8], len(archivos))
        for sesion, archivos in sorted(de_quien.items()))
    ejemplos = sorted(
        a for sesion, archivos in sorted(de_quien.items())[1:]
        for a in archivos)[:3]

    return [Hallazgo(
        AVISO, os.path.join(raiz, ".git"), 0,
        "este commit mezcla archivos de %d sesiones (%s) — si no es a "
        "propósito, saca del commit lo que no salió de esta conversación; "
        "empieza por %s"
        % (len(de_quien), detalle, ", ".join(ejemplos)))]


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("sesiones")
