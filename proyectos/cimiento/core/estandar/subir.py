# -*- coding: utf-8 -*-
"""`EP-026·HU-007` · El commit de lo que cambió una sesión, y su subida, desde la pantalla.

**Oprimir el botón es la aprobación** (análisis 1 del pendiente 132, acuerdos 3,
8 y 22): solo el grupo administrador llega acá.

**Solo lo de una sesión**: `CambiosPorSesion` prepara sus archivos; lo que
tocaron dos se nombra y no entra.

**El mensaje sigue la convención del repositorio**: el asunto, la idea del
usuario y después lo que hizo el agente. Nunca `Co-Authored-By`.

**Nada queda a medias**: si el commit falla, se suelta lo preparado (si no,
entraría en el commit siguiente). Si falla solo la subida, el commit queda y se
dice. La cuenta para subir es la del computador: Cimiento no guarda claves.
"""
import subprocess

from core.herramientas.cambios import CambiosPorSesion


class SinSubir(Exception):
    """El commit o la subida no se hicieron; el mensaje dice por qué."""


def mensaje(asunto, idea, hecho):
    asunto = (asunto or "").strip()
    if not asunto:
        raise SinSubir("el commit necesita su asunto")
    partes = [asunto] + [p.strip() for p in (idea, hecho) if (p or "").strip()]
    return "\n\n".join(partes) + "\n"


def _git(raiz, *argumentos, entrada=None):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + list(argumentos), cwd=raiz, input=entrada,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def guardar(raiz, sesion, asunto, idea, hecho, subir=False):
    """Hace el commit de lo de `sesion` y, con `subir`, lo sube. Devuelve `(hash, subido)`."""
    texto = mensaje(asunto, idea, hecho)
    cambios = CambiosPorSesion(raiz)
    try:
        sesion, archivos, _compartidos = cambios.preparar(sesion, escribir=True)
    except ValueError as error:
        raise SinSubir(str(error)) from None
    if not archivos:
        raise SinSubir("esa sesión no tiene archivos propios para guardar")
    proceso = _git(raiz, "commit", "-F", "-", entrada=texto)
    if proceso.returncode != 0:
        cambios.soltar(sesion, escribir=True)
        raise SinSubir("git no hizo el commit:\n" + (proceso.stdout + proceso.stderr).strip())
    hash_ = _git(raiz, "rev-parse", "--short", "HEAD").stdout.strip()
    if not subir:
        return hash_, False
    empuje = _git(raiz, "push")
    if empuje.returncode != 0:
        raise SinSubir("el commit %s quedó hecho, pero no se subió:\n%s" % (hash_, (empuje.stdout + empuje.stderr).strip()))
    return hash_, True
