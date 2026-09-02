# -*- coding: utf-8 -*-
"""Aprobar un documento, y saber si lo aprobado sigue siendo lo que hay.

**Tres estados, no dos.** Un documento puede estar **aprobado**, puede tener una
aprobación que **caducó** porque el texto cambió, y puede **no tener ninguna**.
Las tres se dicen distinto:

- «Sin aprobación» no es «en borrador rechazado»: es que nadie lo ha mirado.
- «Caducada» no es «sin aprobación»: alguien la aprobó, y el texto cambió
  después. Lo primero que hay que ver es **qué cambió**.

**Y se dice con palabras, no con color.** Lo pide la ficha de `F-016`: quien no
distingue colores tiene que poder saberlo igual.

**Nada se borra.** Cuando una aprobación caduca, la anterior se queda como
historia: es el registro de qué se autorizó y cuándo, y sin él el documento
queda como si nunca hubiera pasado por nadie.
"""
import hashlib
import io
import os
import time

from django.conf import settings

from nucleo.auditoria.core import con_constancia
from nucleo.proyectos.models import Proyecto
from .models import Aprobacion

APROBADO = "aprobado"
CADUCADA = "caducada"
SIN_APROBACION = "sin aprobación"

# Qué se le dice a una persona en cada caso. **Con palabras, no con color.**
EN_PALABRAS = {
    APROBADO: "Aprobado",
    CADUCADA: "La aprobación caducó: el documento cambió después de aprobarse",
    SIN_APROBACION: "Sin aprobación: nadie lo ha aprobado todavía",
}


class NoSePuedeAprobar(Exception):
    """Falta algo para aprobar, y se dice qué."""


def _ruta(proyecto, documento):
    try:
        registrado = Proyecto.objects.get(identificador=proyecto)
    except Proyecto.DoesNotExist:
        return ""
    return os.path.join(registrado.ruta_codigo, documento.replace("/", os.sep))


def _texto(ruta):
    try:
        with io.open(ruta, encoding="utf-8", newline="") as archivo:
            return archivo.read()
    except OSError:
        return None


def huella(texto):
    """La huella del texto aprobado."""
    return hashlib.sha256((texto or "").encode("utf-8")).hexdigest()


def aprobar(proyecto, documento, quien, cuando=""):
    """Registra que alguien aprobó ese documento, sobre el texto que hay.

    **No se puede aprobar un documento que no existe.** Aprobar algo que no
    está sería firmar en blanco: cuando aparezca, diría que ya se aprobó.
    """
    ruta = _ruta(proyecto, documento)
    if not ruta:
        raise NoSePuedeAprobar(
            "No hay un proyecto registrado con el nombre «%s»." % proyecto)
    texto = _texto(ruta)
    if texto is None:
        raise NoSePuedeAprobar(
            "Ese documento no existe: %s. **Aprobar algo que no está sería "
            "firmar en blanco.**" % ruta)

    cuando = cuando or time.strftime("%Y-%m-%d %H:%M:%S")
    return con_constancia(
        lambda comprobante: Aprobacion.objects.create(
            proyecto=proyecto, documento=documento, quien=quien, cuando=cuando,
            huella=huella(texto), tamano=len(texto)),
        que_se_hizo="aprobar un documento", sobre_que=documento, quien=quien,
        proyecto=proyecto, que_cambio="%d caracteres" % len(texto))


def historia_de(proyecto, documento):
    """Todas las aprobaciones de ese documento, de la más nueva a la más vieja.

    **Las caducadas también salen.** Son la historia de qué se autorizó, y
    borrarlas dejaría el documento como si nunca hubiera pasado por nadie.
    """
    return list(Aprobacion.objects.filter(proyecto=proyecto,
                                          documento=documento))


def estado_de(proyecto, documento):
    """En qué estado de aprobación está ese documento.

    Devuelve `{"estado", "en_palabras", "desde", "quien", "cuantas",
    "cambio_desde", "existe"}`.
    """
    aprobaciones = historia_de(proyecto, documento)
    ruta = _ruta(proyecto, documento)
    texto = _texto(ruta) if ruta else None

    if not aprobaciones:
        return {"estado": SIN_APROBACION,
                "en_palabras": EN_PALABRAS[SIN_APROBACION],
                "desde": "", "quien": "", "cuantas": 0, "cambio_desde": 0,
                "existe": texto is not None}

    ultima = aprobaciones[0]
    if texto is None:
        return {"estado": CADUCADA,
                "en_palabras": "La aprobación caducó: el documento ya no está",
                "desde": ultima.cuando, "quien": ultima.quien,
                "cuantas": len(aprobaciones), "cambio_desde": 0,
                "existe": False}

    if huella(texto) == ultima.huella:
        estado = APROBADO
    else:
        estado = CADUCADA
    return {"estado": estado, "en_palabras": EN_PALABRAS[estado],
            "desde": ultima.cuando, "quien": ultima.quien,
            "cuantas": len(aprobaciones),
            "cambio_desde": len(texto) - ultima.tamano,
            "existe": True}


def que_cambio(proyecto, documento):
    """Qué cambió desde lo aprobado. Devuelve `(lineas_de_mas, lineas_de_menos)`.

    **No es un diff completo:** es lo que alcanza para decidir si vale la pena
    mirar. El diff de verdad lo da el control de versiones, que ya lo hace bien.
    """
    aprobaciones = historia_de(proyecto, documento)
    if not aprobaciones:
        return (0, 0)
    ruta = _ruta(proyecto, documento)
    texto = _texto(ruta)
    if texto is None:
        return (0, aprobaciones[0].tamano)
    diferencia = len(texto) - aprobaciones[0].tamano
    return (max(diferencia, 0), max(-diferencia, 0))


def de_un_proyecto(proyecto, documentos):
    """El estado de aprobación de varios documentos, en orden.

    `documentos` es la lista de rutas a mirar. **Un documento sin aprobación
    aparece así, no vacío:** lo pide el `CA-3` de `F-016`.
    """
    return [dict(estado_de(proyecto, uno), documento=uno)
            for uno in documentos]
