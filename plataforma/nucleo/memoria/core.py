# -*- coding: utf-8 -*-
"""Lo que el agente aprendió, guardado donde una persona lo puede leer.

**La memoria vive en el repositorio del proyecto, no en la plataforma.** Un
archivo por recuerdo, en texto. Es la misma decisión que gobierna todo lo
demás: lo que se puede leer sin la herramienta es lo que sobrevive a la
herramienta. Y acá tiene un motivo extra, que la ficha de `F-024` nombra:
**hoy solo el agente ve lo que recuerda**, y eso es un problema de confianza
antes que de comodidad.

**Lo de un proyecto no se mezcla con lo de otro.** Cada proyecto tiene la suya,
en su propia carpeta. Un recuerdo de un cliente aplicado a otro es peor que no
recordar nada.

**Corregir deja constancia de qué decía antes.** Un recuerdo que cambia sin
dejar rastro es indistinguible de uno que siempre dijo eso, y entonces nadie
puede saber si el agente aprendió o si alguien le cambió la memoria.

**Y dar de baja no borra.** Se marca, y deja de entregarse. Lo que se borra no
se puede volver a leer para entender por qué se creyó.
"""
import io
import os
import re
import time

from django.conf import settings

from nucleo.proyectos.models import Proyecto

# Dónde vive la memoria dentro de un proyecto.
CARPETA = os.path.join("historico-chat", "memory")

# El archivo que hace de índice, y no es un recuerdo.
INDICE = "memory.md"

# La marca de un recuerdo dado de baja, en su primera línea.
DE_BAJA = u"> **Ya no vale.**"

# Lo que se escribe encima de la versión anterior al corregir.
ANTES_DECIA = u"---\n\n> **Antes decía esto**, hasta el %s. Se conserva porque un recuerdo que cambia sin dejar rastro no se distingue de uno que siempre dijo eso.\n\n"

_TITULO = re.compile(u"(?m)^#\\s+(.+?)\\s*$")


class NoHayMemoria(Exception):
    """Ese proyecto no tiene carpeta de memoria, y se dice."""


def _carpeta(proyecto):
    try:
        registrado = Proyecto.objects.get(identificador=proyecto)
    except Proyecto.DoesNotExist:
        raise NoHayMemoria(
            "No hay un proyecto registrado con el nombre «%s»." % proyecto)
    return os.path.join(registrado.ruta_codigo, CARPETA)


def _leer(ruta):
    try:
        with io.open(ruta, encoding="utf-8", newline="") as archivo:
            return archivo.read()
    except OSError:
        return ""


def todos(proyecto):
    """Todos los recuerdos de ese proyecto, **incluidos los dados de baja**.

    El índice no es un recuerdo y no sale.
    """
    carpeta = _carpeta(proyecto)
    if not os.path.isdir(carpeta):
        raise NoHayMemoria(
            "Ese proyecto no tiene memoria escrita: no existe %s." % carpeta)

    recuerdos = []
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.endswith(".md") or nombre == INDICE:
            continue
        texto = _leer(os.path.join(carpeta, nombre))
        titulo = _TITULO.search(texto)
        recuerdos.append({
            "nombre": nombre,
            "titulo": titulo.group(1) if titulo else nombre[:-3],
            "texto": texto,
            "de_baja": DE_BAJA in texto,
            "ruta": os.path.join(carpeta, nombre),
        })
    return recuerdos


def vigentes(proyecto):
    """Los que todavía valen. **Es lo que se le entrega al agente.**"""
    return [uno for uno in todos(proyecto) if not uno["de_baja"]]


def buscar(proyecto, palabra=""):
    """Los recuerdos vigentes que contienen esa palabra.

    Sin palabra, salen todos los vigentes. **Si no hay ninguno, se dice**, en
    vez de devolver una lista vacía que se leería como «no hay memoria».
    """
    encontrados = vigentes(proyecto)
    if palabra:
        buscada = palabra.lower()
        encontrados = [uno for uno in encontrados
                       if buscada in uno["texto"].lower()
                       or buscada in uno["titulo"].lower()]
    return encontrados


def guardar(proyecto, nombre, texto):
    """Escribe un recuerdo nuevo. Devuelve su ruta.

    **No pisa uno que ya exista:** para cambiar uno está `corregir`, que deja
    constancia de qué decía antes.
    """
    carpeta = _carpeta(proyecto)
    if not nombre.endswith(".md"):
        nombre += ".md"
    destino = os.path.join(carpeta, nombre)
    if os.path.exists(destino):
        raise NoHayMemoria(
            "Ya hay un recuerdo con ese nombre: %s. Para cambiarlo está "
            "corregir, que conserva lo que decía antes." % nombre)
    os.makedirs(carpeta, exist_ok=True)
    with io.open(destino, "w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(texto if texto.endswith("\n") else texto + "\n")
    return destino


def corregir(proyecto, nombre, texto_nuevo, cuando=""):
    """Cambia un recuerdo **conservando lo que decía antes**, debajo.

    Un recuerdo que cambia sin dejar rastro es indistinguible de uno que
    siempre dijo eso.
    """
    carpeta = _carpeta(proyecto)
    if not nombre.endswith(".md"):
        nombre += ".md"
    destino = os.path.join(carpeta, nombre)
    anterior = _leer(destino)
    if not anterior:
        raise NoHayMemoria("No hay ningún recuerdo llamado «%s»." % nombre)

    cuando = cuando or time.strftime("%Y-%m-%d")
    nuevo = (texto_nuevo.rstrip("\n") + "\n\n" + (ANTES_DECIA % cuando)
             + anterior.rstrip("\n") + "\n")
    with io.open(destino, "w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(nuevo)
    return destino


def dar_de_baja(proyecto, nombre, porque, cuando=""):
    """Marca un recuerdo como que ya no vale. **No lo borra.**

    Deja de entregarse al agente, y sigue ahí para entender por qué se creyó.
    """
    carpeta = _carpeta(proyecto)
    if not nombre.endswith(".md"):
        nombre += ".md"
    destino = os.path.join(carpeta, nombre)
    texto = _leer(destino)
    if not texto:
        raise NoHayMemoria("No hay ningún recuerdo llamado «%s»." % nombre)
    if DE_BAJA in texto:
        raise NoHayMemoria("«%s» ya está dado de baja." % nombre)

    cuando = cuando or time.strftime("%Y-%m-%d")
    aviso = (u"%s %s Dado de baja el %s. El texto se conserva: lo que se borra "
             u"no se puede volver a leer para entender por qué se creyó.\n\n"
             % (DE_BAJA, porque, cuando))
    with io.open(destino, "w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(aviso + texto.lstrip("\n"))
    return destino


def resumen(proyecto):
    """Cuántos recuerdos hay, y cuántos siguen valiendo."""
    recuerdos = todos(proyecto)
    return {"todos": len(recuerdos),
            "vigentes": sum(1 for uno in recuerdos if not uno["de_baja"]),
            "de_baja": sum(1 for uno in recuerdos if uno["de_baja"])}
