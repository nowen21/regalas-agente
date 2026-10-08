# -*- coding: utf-8 -*-
"""`EP-026·HU-005` · Cambiar el estándar y la memoria en la base.

**Lo derivado se arma en la misma versión.** El mapa de tareas y las reglas por
tarea salen de las reglas: al guardar un documento se vuelven a armar en la
base, con los mismos `MapaDeTareas.armar` y `armar_por_tarea` de siempre. Si no
se armaran, el agente recibiría las reglas de antes.

**Quién y por qué los pone quien llama**: la pantalla (por el middleware, con
las dos preguntas) o `quien_y_por_que`. Así cada envío es una versión.
"""
import os

from django.db import transaction
from django.utils import timezone

from core.comun import Proyecto as Carpeta
from core.herramientas.mapa_tareas import MAPA, POR_TAREA, MapaDeTareas

from . import en_base, reglas
from .models import APROBADA, CAMBIAR, CREAR, DOCUMENTO, PENDIENTE, QUITAR, RECHAZADA, Documento, Recuerdo

PREFIJO = "base/"


class CambioInvalido(Exception):
    """El cambio no se puede hacer; el mensaje dice por qué."""


def _igual(a, b):
    return (a or "").replace("\r\n", "\n") == (b or "").replace("\r\n", "\n")


def ruta_valida(ruta):
    ruta = (ruta or "").strip().replace("\\", "/")
    if not ruta.startswith(PREFIJO) or not ruta.endswith(".md") or ".." in ruta.split("/"):
        raise CambioInvalido("un documento del estándar va bajo base/ y termina en .md")
    return ruta


def rearmar_mapa(raiz=None):
    """Arma de nuevo el mapa y las reglas por tarea desde lo que hay en la base, y
    guarda solo lo que cambió. Las reglas por tarea que sobran se quitan."""
    raiz = os.path.abspath(raiz or Carpeta.estandar())
    lector = en_base.ArchivosEnBase(raiz, dict(Documento.objects.values_list("ruta", "contenido")))
    mapa = MapaDeTareas(raiz, lector)
    esperados = {MAPA: mapa.armar()}
    for nombre, texto in mapa.armar_por_tarea().items():
        esperados["%s/%s" % (POR_TAREA, nombre)] = texto
    actuales = {d.ruta: d for d in Documento.objects.filter(ruta__startswith=POR_TAREA + "/")}
    actuales.update({d.ruta: d for d in Documento.objects.filter(ruta=MAPA)})
    for ruta, texto in esperados.items():
        documento = actuales.get(ruta)
        if documento is None:
            Documento.objects.create(ruta=ruta, contenido=texto)
        elif not _igual(documento.contenido, texto):
            documento.contenido = texto
            documento.save()
    for ruta, documento in actuales.items():
        if ruta.startswith(POR_TAREA + "/") and ruta not in esperados:
            documento.delete()
    en_base.olvidar()


def guardar_documento(ruta, contenido, raiz=None):
    """Crea o cambia un documento del estándar y vuelve a armar el mapa. Devuelve el documento."""
    ruta = ruta_valida(ruta)
    with transaction.atomic():
        documento = Documento.objects.filter(ruta=ruta).first()
        if documento is None:
            documento = Documento.objects.create(ruta=ruta, contenido=contenido)
        elif not _igual(documento.contenido, contenido):
            documento.contenido = contenido
            documento.save()
        reglas.pasar_y_armar(documento)
        rearmar_mapa(raiz)
    return documento


def quitar_documento(documento, raiz=None):
    with transaction.atomic():
        reglas.soltar_reglas(documento)
        documento.delete()
        rearmar_mapa(raiz)


def guardar_recuerdo(proyecto, nombre, contenido):
    nombre = (nombre or "").strip()
    if not nombre.endswith(".md") or "/" in nombre or "\\" in nombre:
        raise CambioInvalido("un recuerdo se llama como un archivo .md, sin carpetas")
    recuerdo = Recuerdo.objects.filter(proyecto=proyecto, nombre=nombre).first()
    if recuerdo is None:
        return Recuerdo.objects.create(proyecto=proyecto, nombre=nombre, contenido=contenido)
    if not _igual(recuerdo.contenido, contenido):
        recuerdo.contenido = contenido
        recuerdo.save()
    return recuerdo


def aplicar(propuesta, cuenta, raiz=None):
    """Aplica una propuesta pendiente y la deja aprobada, a nombre de `cuenta`."""
    if propuesta.estado != PENDIENTE:
        raise CambioInvalido("la propuesta ya está %s" % propuesta.get_estado_display().lower())
    with transaction.atomic():
        if propuesta.objeto == DOCUMENTO:
            if propuesta.accion == QUITAR:
                documento = Documento.objects.filter(ruta=propuesta.ruta).first()
                if documento is None:
                    raise CambioInvalido("el documento ya no existe")
                quitar_documento(documento, raiz)
            else:
                guardar_documento(propuesta.ruta, propuesta.contenido, raiz)
        else:
            if propuesta.accion == QUITAR:
                Recuerdo.objects.filter(proyecto=propuesta.proyecto, nombre=propuesta.nombre).delete()
            else:
                guardar_recuerdo(propuesta.proyecto, propuesta.nombre, propuesta.contenido)
        _resolver(propuesta, cuenta, APROBADA)


def rechazar(propuesta, cuenta, motivo=""):
    if propuesta.estado != PENDIENTE:
        raise CambioInvalido("la propuesta ya está %s" % propuesta.get_estado_display().lower())
    propuesta.motivo_rechazo = (motivo or "").strip()
    _resolver(propuesta, cuenta, RECHAZADA)


def actual_de(propuesta):
    """El texto que hay hoy en el lugar que la propuesta cambia; "" si es nuevo."""
    if propuesta.objeto == DOCUMENTO:
        documento = Documento.objects.filter(ruta=propuesta.ruta).only("contenido").first()
        return documento.contenido if documento else ""
    recuerdo = Recuerdo.objects.filter(proyecto=propuesta.proyecto, nombre=propuesta.nombre).only("contenido").first()
    return recuerdo.contenido if recuerdo else ""


def que_cambia(propuesta, contexto=2):
    """`EP-028·HU-004` · Lo que la propuesta quita y agrega, línea por línea, con
    `contexto` líneas de alrededor: `[(tipo, texto)]`, con tipo «sale», «entra»,
    «igual» o «salto». Lo calcula `difflib`, que trae Python."""
    import difflib

    antes = actual_de(propuesta).splitlines()
    despues = [] if propuesta.accion == QUITAR else propuesta.contenido.splitlines()
    salida = []
    for linea in difflib.unified_diff(antes, despues, lineterm="", n=contexto):
        if linea.startswith(("---", "+++")):
            continue
        if linea.startswith("@@"):
            salida.append(("salto", "…"))
        elif linea.startswith("-"):
            salida.append(("sale", linea[1:]))
        elif linea.startswith("+"):
            salida.append(("entra", linea[1:]))
        else:
            salida.append(("igual", linea[1:]))
    return salida


def _resolver(propuesta, cuenta, estado):
    propuesta.estado = estado
    propuesta.resuelta_por = cuenta if getattr(cuenta, "is_authenticated", False) else None
    propuesta.resuelta = timezone.now()
    propuesta.save()


def accion_para(objeto, existe, quitar=False):
    if quitar:
        return QUITAR
    return CAMBIAR if existe else CREAR


__all__ = ["CambioInvalido", "aplicar", "rechazar", "guardar_documento", "quitar_documento", "guardar_recuerdo",
           "rearmar_mapa", "ruta_valida", "accion_para", "DOCUMENTO"]
