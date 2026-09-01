# -*- coding: utf-8 -*-
"""Escribir una regla y derogarla. **Siempre en el archivo, nunca en la base.**

El cuerpo de reglas es texto, y esa es su forma final: se lee sin la
plataforma, se versiona, y viaja a los proyectos que lo heredan. Guardarlo en
una base y generar el texto haría del texto una copia, y la copia se queda vieja
el día que alguien edite el archivo a mano, que es como se ha trabajado siempre.

**Derogar no borra.** La regla se queda escrita, se le pone la marca, y su
número queda ocupado para siempre. Es lo que exige `M11`, y el porqué es el
mismo del número: una cita escrita hace un año tiene que seguir apuntando a lo
que apuntaba.

**La regla nueva nace con sus huecos puestos.** El cuerpo y el ejemplo salen con
la marca de espacio por llenar, que es la convención del estándar. Así el módulo
Ciclo de vida puede llenarlos, y mientras tanto cualquiera ve que falta algo.
"""
import io
import os
import re
import unicodedata

from . import catalogo, numeracion

MARCA_DEL_HUECO = u"«…»"

# La marca que convierte una regla vigente en una derogada.
_DEROGADA = re.compile(u"\\[DEROGADA en [\\d.]+ → ver [^\\]]+\\]")

# El encabezado de una regla: `## F26 · Su título`.
_ENCABEZADO = re.compile(u"(?m)^## +([A-Za-z]+[\\d.]+) +· +(.+?)\\s*$")


class NoSePuedeTocar(Exception):
    """Esa regla no se puede cambiar desde acá, y se dice por qué."""


def _en_minusculas_sin_tildes(texto):
    """El título convertido en nombre de archivo."""
    plano = unicodedata.normalize("NFKD", texto or "")
    plano = u"".join(c for c in plano if not unicodedata.combining(c))
    plano = re.sub(u"[^A-Za-z0-9]+", u"-", plano).strip(u"-").lower()
    return plano or u"sin-titulo"


def nombre_de_archivo(identificador, titulo):
    return u"%s-%s.md" % (identificador, _en_minusculas_sin_tildes(titulo))


def molde(identificador, titulo, capitulo):
    """El texto de una regla nueva, con el formato canónico y sus huecos.

    `capitulo` es como se nombra en la primera línea, del estilo de
    `20 · Meta-reglas`. Lo que va en el cuerpo y en el ejemplo queda marcado
    como espacio por llenar: la regla nace incompleta **y se le nota**.
    """
    return (
        u"> Regla del capítulo [`%s`](../base.md).\n"
        u"\n"
        u"## %s · %s\n"
        u"\n"
        u"%s\n"
        u"\n"
        u"```\n"
        u"INCORRECTO: %s\n"
        u"CORRECTO:   %s\n"
        u"```\n"
    ) % (capitulo, identificador, titulo,
         MARCA_DEL_HUECO, MARCA_DEL_HUECO, MARCA_DEL_HUECO)


def crear(raiz, carpeta_del_capitulo, prefijo, titulo, capitulo):
    """Escribe una regla nueva y devuelve `(identificador, ruta)`.

    El identificador se pide **antes** de escribir, y se comprueba que esté
    libre: después de escribir ya habría dos reglas con el mismo número.
    """
    identificador = numeracion.siguiente_libre(raiz, prefijo)
    numeracion.comprobar_libre(raiz, identificador)

    destino = os.path.join(raiz, carpeta_del_capitulo.replace("/", os.sep),
                           "reglas", nombre_de_archivo(identificador, titulo))
    if os.path.exists(destino):
        raise NoSePuedeTocar("Ya hay un archivo ahí: %s" % destino)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with io.open(destino, "w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(molde(identificador, titulo, capitulo))
    return identificador, destino


def _regla(raiz, identificador):
    for una in catalogo.todas(raiz):
        if una.id == identificador:
            return una
    return None


def derogar(raiz, identificador, en_version, ver, porque):
    """Marca una regla como derogada, **sin borrar su texto**.

    Devuelve la ruta del archivo. Levanta `NoSePuedeTocar` si la regla no
    existe, si ya está derogada, o **si es blindada**: esas no se derogan desde
    acá, y el porqué es que sostienen a las demás.
    """
    una = _regla(raiz, identificador)
    if una is None:
        raise NoSePuedeTocar("No hay ninguna regla con el identificador «%s»."
                             % identificador)
    if una.derogada:
        raise NoSePuedeTocar("«%s» ya está derogada." % identificador)
    if una.blindada:
        raise NoSePuedeTocar(
            "«%s» es blindada: sostiene a las demás y no se deroga desde acá."
            % identificador)

    with io.open(una.archivo, encoding="utf-8", newline="") as archivo:
        texto = archivo.read()

    encontrado = _ENCABEZADO.search(texto)
    if not encontrado:
        raise NoSePuedeTocar(
            "No se encontró el encabezado de «%s» en su archivo." % identificador)

    marca = u"[DEROGADA en %s → ver %s]" % (en_version, ver)
    nuevo = u"## %s · %s  ·  `%s`" % (encontrado.group(1),
                                                encontrado.group(2), marca)
    aviso = (u"\n\n> **Ya no rige.** %s El texto original se conserva debajo y "
             u"el ID no se reutiliza." % porque)

    texto = (texto[:encontrado.start()] + nuevo + aviso
             + texto[encontrado.end():])
    with io.open(una.archivo, "w", encoding="utf-8", newline="") as archivo:
        archivo.write(texto)
    return una.archivo


def esta_derogada_en_el_texto(texto):
    """Si ese texto trae la marca de derogación. Para comprobar sin releer."""
    return bool(_DEROGADA.search(texto or ""))
