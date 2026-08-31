# -*- coding: utf-8 -*-
"""Indexar lo conversado y buscar en ello. **Se lee; no se toca nada.**

La fuente es el texto que el enganche del estándar ya escribió en
`historico-chat/` del proyecto. Este módulo **solo lee**: no modifica, no mueve
y no borra ningún archivo del histórico, y ese es el criterio de «que NO pase»
de la historia (`CA-04`).

**Tampoco copia el texto a la plataforma.** Se indexa donde ya vive, versionado
en el repositorio del proyecto. Es la excepción declarada a `DA-01` en la §12 de
la especificación del módulo: lo que esa decisión protege —que perder la base no
pierda información— se cumple igual, porque el índice se rehace leyendo esos
mismos archivos.

**Un archivo ilegible se reporta y no detiene el resto.** Un archivo roto no
puede llevarse lo que ya se sabía.
"""
import hashlib
import io
import os
import re

from . import conversacion
from .models import Mensaje, Sesion

# Dónde escribe el enganche del estándar, dentro del proyecto.
CARPETA = "historico-chat"

# El nombre de un archivo de sesión: empieza con la fecha. Lo que no encaje
# —el índice, los resúmenes, la memoria— no es una sesión.
_SESION = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$", re.IGNORECASE)


class NoSePuedeIndexar(Exception):
    """El proyecto no tiene dónde buscar: su ruta no existe."""


def huella(texto):
    """La misma forma de huella que usa el almacén: el texto identifica al archivo."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def _tema_de(nombre):
    """El tema que el nombre del archivo declara, o vacío si todavía no tiene.

    `2026-08-31-sesion.md` es el nombre que el enganche pone cuando nadie sabe
    todavía de qué va a tratar: eso no es un tema.
    """
    m = _SESION.match(nombre)
    if not m:
        return ""
    resto = m.group(2)
    if resto.lower().startswith("sesion"):
        return ""
    return resto.replace("-", " ")


def archivos_de_sesion(raiz_proyecto):
    """Los archivos de conversación de un proyecto, del más viejo al más nuevo."""
    carpeta = os.path.join(raiz_proyecto, CARPETA)
    if not os.path.isdir(carpeta):
        return []
    return [n for n in sorted(os.listdir(carpeta)) if _SESION.match(n)]


def indexar(proyecto):
    """Indexa las conversaciones de un proyecto. `{"sesiones","mensajes","ilegibles"}`.

    Lo ya indexado de ese proyecto se reemplaza: el texto manda, y una sesión
    que creció desde la última pasada tiene que quedar completa, no duplicada.
    """
    raiz = proyecto.ruta_codigo
    if not os.path.isdir(raiz):
        raise NoSePuedeIndexar(
            "No está la carpeta del proyecto: %s" % raiz)

    carpeta = os.path.join(raiz, CARPETA)
    cuenta = {"sesiones": 0, "mensajes": 0, "ilegibles": []}

    Sesion.objects.filter(proyecto=proyecto).delete()

    for nombre in archivos_de_sesion(raiz):
        completa = os.path.join(carpeta, nombre)
        try:
            with io.open(completa, encoding="utf-8") as abierto:
                texto = abierto.read()
        except (OSError, UnicodeError) as falla:
            # Se dice cuál y por qué. Saltarlo en silencio dejaría un índice
            # incompleto que se lee como completo.
            cuenta["ilegibles"].append((nombre, str(falla)))
            continue

        sesion = Sesion.objects.create(
            proyecto=proyecto,
            archivo="%s/%s" % (CARPETA, nombre),
            fecha=_SESION.match(nombre).group(1),
            tema=_tema_de(nombre),
            huella=huella(texto))
        cuenta["sesiones"] += 1

        for orden, (quien, cuando, dicho) in enumerate(
                conversacion.turnos(texto), 1):
            if not dicho:
                continue
            Mensaje.objects.create(sesion=sesion, orden=orden, quien=quien,
                                   cuando=cuando, texto=dicho)
            cuenta["mensajes"] += 1

    return cuenta


def reconstruir_indice(proyectos):
    """Borra el índice entero y lo rehace leyendo los archivos. Devuelve la cuenta.

    Es la comprobación de que perder la base no pierde información: la fuente
    es el texto, y esto lo demuestra en vez de prometerlo (`CA-02`).
    """
    Sesion.objects.all().delete()
    total = {"sesiones": 0, "mensajes": 0, "ilegibles": []}
    for proyecto in proyectos:
        if not os.path.isdir(proyecto.ruta_codigo):
            continue                    # la ruta perdida ya la reporta Proyectos
        cuenta = indexar(proyecto)
        total["sesiones"] += cuenta["sesiones"]
        total["mensajes"] += cuenta["mensajes"]
        total["ilegibles"] += cuenta["ilegibles"]
    return total


def buscar(texto, proyecto=None, limite=50):
    """Los mensajes donde aparece `texto`. Lista vacía si no aparece en ninguno.

    Quien llama distingue «no hay coincidencias» de «no hay nada indexado»
    mirando `hay_algo_indexado()`: las dos cosas devuelven una lista vacía y no
    significan lo mismo.
    """
    if not (texto or "").strip():
        return []
    mensajes = Mensaje.objects.filter(texto__icontains=texto.strip())
    if proyecto is not None:
        mensajes = mensajes.filter(sesion__proyecto=proyecto)
    return list(mensajes.select_related("sesion")[:limite])


def hay_algo_indexado(proyecto=None):
    """Si hay conversaciones en el índice. Separa «no hay» de «no encontré»."""
    sesiones = Sesion.objects.all()
    if proyecto is not None:
        sesiones = sesiones.filter(proyecto=proyecto)
    return sesiones.exists()
