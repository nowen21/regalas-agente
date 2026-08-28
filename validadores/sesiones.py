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


# `EP-005·HU-020` · El registro deja de depender de con qué se escribió.
#
# **El caso que lo hizo falta.** Un commit se llevó 712 líneas ajenas y la
# comprobación de arriba dijo OK: pregunta si **dos sesiones registradas**
# tocaron lo mismo, y a esos archivos **no los había registrado ninguna**. Un
# archivo sin registro no parece de otro: parece de nadie (`S-071`).
#
# **Y afinar la comprobación no servía.** Avisar de lo que no tiene registro
# habría hablado en **siete de los últimos doce commits, con hasta 31 archivos**:
# el registro solo se llenaba desde las herramientas de escritura, y la mayoría
# de los archivos los escriben guiones que se corren en la terminal. *«Sin
# registro»* significaba *«escrito como se escribe casi todo»* (`S-072`).
#
# **Lo que sí separa es anotar lo que cambió, mire quien lo mire.** Si otra
# sesión escribe mientras esta trabaja, **las dos lo anotan**, y la comprobación
# que ya existe ve la colisión. No hizo falta comprobación nueva: hizo falta que
# su registro dejara de tener el hueco.
def _estado_de_git(raiz):
    """`(cambiadas, borradas)` según git. Vacías si acá no hay repositorio."""
    try:
        salida = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=raiz, stderr=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError):
        return ([], [])
    cambiadas, borradas = [], []
    for linea in salida.decode("utf-8", "replace").splitlines():
        if len(linea) < 4:
            continue
        marca, ruta = linea[:2], linea[3:].strip().strip('"')
        if " -> " in ruta:                  # renombrado: cuenta el destino
            ruta = ruta.split(" -> ")[-1]
        # Los ignorados no salen sin `--ignored`, y **no se piden a propósito**:
        # no son trabajo versionado, y el propio registro vive en uno de ellos.
        if "D" in marca:
            borradas.append(ruta)
        else:
            cambiadas.append(ruta)
    return (cambiadas, borradas)


def cambios_del_turno(raiz, desde):
    """Lo que cambió después de `desde`. Con `desde` en `None`, **nada**.

    **La primera vuelta no reclama nada, y es deliberado.** Sin una fecha
    anterior contra la cual comparar, cualquier criterio se llevaría todo lo que
    estuviera sucio — y la primera sesión del día se atribuiría el árbol entero.
    El registro arranca su reloj y anota desde la vuelta siguiente.

    **Un borrado se anota siempre.** No tiene fecha que mirar, así que no se
    puede saber si cayó dentro de la ventana. Se prefiere anotar de más: dos
    sesiones que borran lo mismo es justo lo que hay que ver.
    """
    if desde is None:
        return []
    cambiadas, borradas = _estado_de_git(raiz)
    salida = list(borradas)
    for ruta in cambiadas:
        completa = os.path.join(raiz, *ruta.split("/"))
        try:
            if os.path.getmtime(completa) > desde:
                salida.append(ruta)
        except OSError:
            continue                        # desapareció entre medias: no se afirma
    return salida


def anotar_el_turno(raiz, sesion, ahora=None):
    """Anota lo que cambió desde la última vuelta. Devuelve lo anotado.

    Se apoya en la fecha del propio registro: **no hace falta estado nuevo**, y
    lo que no se pudo saber no se inventa.
    """
    if not sesion:
        return []
    raiz = raiz or RAIZ
    if not os.path.isdir(raiz):
        # La herramienta puede mandar una carpeta que ya no está. Crearla sería
        # escribir fuera de todo proyecto (`04·S9`).
        return []
    ruta = os.path.join(_carpeta(raiz), _limpio(sesion) + ".txt")
    desde = os.path.getmtime(ruta) if os.path.isfile(ruta) else None

    nuevos = cambios_del_turno(raiz, desde)
    for archivo in nuevos:
        anotar(raiz, sesion, os.path.join(raiz, *archivo.split("/")))

    if desde is None:
        # Arranca el reloj sin reclamar nada: recién creado, el archivo ya trae
        # la hora de ahora, y desde la vuelta siguiente hay contra qué comparar.
        if not os.path.isdir(_carpeta(raiz)):
            os.makedirs(_carpeta(raiz))
        io.open(ruta, "a", encoding="utf-8").close()
    return nuevos


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
