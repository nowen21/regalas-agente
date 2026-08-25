# -*- coding: utf-8 -*-
"""Guardar y leer. La fuente es el texto; la base es un índice que se rehace.

Todo lo que la plataforma guarda queda como un archivo de texto dentro de
`datos/`, legible sin la plataforma y versionable línea por línea (`DA-01`). El
índice existe solo para buscar rápido, y se puede borrar entero: la función
`reconstruir_indice` lo rehace leyendo los archivos.

**Qué NO hace este módulo:** escribir fuera de `datos/`. Cualquier ruta que
apunte afuera se rechaza, y esa es la comprobación `CP-006` del plan de pruebas.

**Y no escribe nada sin constancia.** Desde la fase D, `guardar` exige el
comprobante de que la acción ya quedó registrada en la auditoría. Antes se
podía llamar directo y el archivo cambiaba sin dejar rastro: eso era el hueco
que encontró `CP-007`, y con él abierto `CA-01` no se cumplía.
"""
import hashlib
import io
import os

from django.conf import settings

from nucleo.constancia import Constancia, SinConstancia


class RutaFueraDeLaPlataforma(Exception):
    """Se intentó escribir fuera de `datos/`. Nunca se escribe afuera."""


def carpeta_datos():
    """La carpeta donde vive la fuente. Se crea si no está."""
    ruta = settings.CARPETA_DATOS
    os.makedirs(ruta, exist_ok=True)
    return ruta


def _ruta_real(nombre):
    """La ruta absoluta de un archivo de `datos/`, comprobando que no se salga."""
    base = os.path.realpath(carpeta_datos())
    destino = os.path.realpath(os.path.join(base, nombre))
    if destino != base and not destino.startswith(base + os.sep):
        raise RutaFueraDeLaPlataforma(
            "«%s» apunta fuera de la carpeta de datos: %s" % (nombre, destino))
    return destino


def huella(texto):
    """Un resumen corto del texto, para saber si cambió.

    Es lo que permite que una aprobación caduque sola cuando el documento se
    edita (`DA-07`).
    """
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def guardar(nombre, texto, constancia):
    """Escribe un texto en `datos/<nombre>` y lo deja en el índice.

    Pide la `constancia` de que la acción ya quedó registrada, y comprueba que
    sea la de **este** archivo: una constancia de otra cosa no sirve. La emite
    `nucleo.auditoria.core.registrar`, y lo normal es no llamar acá directo
    sino usar `con_constancia`, que hace las dos cosas en orden.

    Devuelve la huella de lo guardado.
    """
    if not isinstance(constancia, Constancia):
        raise SinConstancia(
            "«%s» se iba a escribir sin constancia. Primero se registra la "
            "acción en la auditoría, y después se escribe." % nombre)
    if not constancia.autoriza(nombre):
        raise SinConstancia(
            "La constancia es de «%s», no de «%s». Una constancia no sirve "
            "para escribir otra cosa." % (constancia.sobre_que, nombre))
    destino = _ruta_real(nombre)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with io.open(destino, "w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(texto)
    _indexar(nombre, texto)
    return huella(texto)


def leer(nombre):
    """Devuelve el texto guardado, o `None` si ese archivo no está."""
    destino = _ruta_real(nombre)
    if not os.path.exists(destino):
        return None
    with io.open(destino, encoding="utf-8") as archivo:
        return archivo.read()


def _indexar(nombre, texto):
    from .models import Anotado
    Anotado.objects.update_or_create(
        nombre=nombre,
        defaults={"huella": huella(texto), "tamano": len(texto)})


def reconstruir_indice():
    """Borra el índice y lo rehace leyendo `datos/`. Devuelve cuántos entraron.

    Es la comprobación de que perder la base no pierde información (`RNF-04`).
    """
    from .models import Anotado
    Anotado.objects.all().delete()
    base = carpeta_datos()
    cuantos = 0
    for raiz, _, archivos in os.walk(base):
        for archivo in archivos:
            completa = os.path.join(raiz, archivo)
            nombre = os.path.relpath(completa, base).replace(os.sep, "/")
            with io.open(completa, encoding="utf-8") as abierto:
                _indexar(nombre, abierto.read())
            cuantos += 1
    return cuantos
