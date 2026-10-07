# -*- coding: utf-8 -*-
"""`EP-026·HU-004` · El estándar se lee de la base, con los mismos lectores de antes.

**Sin Django**, como los niveles: lo leen los enganches en cada mensaje y el
freno en cada acción. Trae todos los documentos de `base/` en una consulta y los
sirve con la misma cara que `Archivos`: `leer(ruta)`, más `recorrer` y `existe`,
que es lo que los lectores (`CuerpoDeReglas`, `MapaDeTareas`, `recuperar.py`,
`autorizado.py`, `cargador.py`) hacían con el disco.

**Solo para el estándar central.** Una carpeta que no es la del estándar (las
pruebas, un proyecto) se sigue leyendo del disco.

**Sin base no hay estándar** (análisis 1 del pendiente 132, acuerdos 5 y 9):
`fuente` levanta `BaseSinRespuesta`; el enganche de reglas lo dice y el freno
no deja modificar. Si la base responde pero el estándar todavía no se importó,
se lee del disco: es el paso de una fuente a la otra.
"""
import os

from ..comun import Archivos
from ..enganches.niveles import SIN_TABLA, BaseSinRespuesta, NivelesDelProyecto

PREFIJO = "base/"
_CACHE = {}


def _orden(relativa):
    """La clave que reproduce el orden de `os.walk` con carpetas y archivos
    ordenados: en cada nivel, primero los archivos y después las carpetas."""
    partes = relativa.split("/")
    return [(1, p) for p in partes[:-1]] + [(0, partes[-1])]


class ArchivosEnBase(Archivos):
    """`Archivos` que sirve `base/` del estándar desde la base de Cimiento."""

    def __init__(self, raiz, documentos):
        super().__init__()
        self.raiz = os.path.abspath(raiz)
        self.documentos = documentos            # {ruta relativa con /: texto}

    def _relativa(self, ruta):
        rel = os.path.relpath(os.path.abspath(ruta), self.raiz).replace(os.sep, "/")
        return rel if rel.startswith(PREFIJO) else None

    def leer(self, ruta):
        rel = self._relativa(ruta)
        if rel is None:
            return super().leer(ruta)
        return self.documentos.get(rel, "")

    def existe(self, ruta):
        rel = self._relativa(ruta)
        return rel in self.documentos if rel is not None else os.path.isfile(ruta)

    def recorrer(self, desde="base", excluir=(), extension=".md"):
        """Las rutas absolutas de los documentos bajo `desde`, en el orden de `os.walk`."""
        desde = desde.strip("/") + "/"
        salida = [rel for rel in self.documentos
                  if rel.startswith(desde) and rel.endswith(extension)
                  and not any(parte in excluir for parte in rel.split("/")[:-1])]
        return [os.path.join(self.raiz, *rel.split("/")) for rel in sorted(salida, key=_orden)]


def recorrer(archivos, raiz, desde="base", excluir=(), extension=".md"):
    """Lo mismo que `ArchivosEnBase.recorrer`, o el disco si `archivos` no viene de la base."""
    if hasattr(archivos, "recorrer"):
        return archivos.recorrer(desde, excluir, extension)
    salida = []
    for carpeta, subcarpetas, nombres in os.walk(os.path.join(raiz, *desde.split("/"))):
        subcarpetas[:] = sorted(s for s in subcarpetas if s not in excluir)
        for nombre in sorted(nombres):
            if nombre.endswith(extension):
                salida.append(os.path.join(carpeta, nombre))
    return salida


def existe(archivos, ruta):
    return archivos.existe(ruta) if hasattr(archivos, "existe") else os.path.isfile(ruta)


def _documentos(raiz, ajustes=None):
    """`{ruta: texto}` de la base, o None si el estándar no está importado."""
    try:
        import pymysql
    except ImportError:
        raise BaseSinRespuesta("falta PyMySQL en el Python que corre los enganches") from None
    niveles = NivelesDelProyecto(raiz, estandar=raiz, ajustes=ajustes)
    a = niveles.ajustes()
    try:
        conexion = pymysql.connect(host=a["HOST"], port=int(a["PORT"]), user=a["USER"], password=a["PASSWORD"],
                                   database=a["NAME"], charset="utf8mb4", connect_timeout=2)
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT ruta, contenido FROM estandar_documento")
                filas = cursor.fetchall()
        finally:
            conexion.close()
    except pymysql.MySQLError as error:
        if error.args and error.args[0] == SIN_TABLA:
            return None
        raise BaseSinRespuesta(niveles.explicar(error)) from None
    return {ruta: contenido for ruta, contenido in filas} or None


def fuente(raiz, archivos=None, ajustes=None):
    """De dónde se lee el estándar en `raiz`: la base si `raiz` es el estándar y
    ya se importó; si no, el disco. Sin base, `BaseSinRespuesta`."""
    from ..comun import Proyecto

    if hasattr(archivos, "recorrer"):
        return archivos                     # ya es un lector del estándar en la base
    estandar = Proyecto.estandar()
    if not estandar or os.path.normcase(os.path.abspath(raiz)) != os.path.normcase(os.path.abspath(estandar)):
        return archivos or Archivos()
    clave = os.path.normcase(os.path.abspath(raiz))
    if clave not in _CACHE:
        documentos = _documentos(raiz, ajustes)
        _CACHE[clave] = ArchivosEnBase(raiz, documentos) if documentos else None
    return _CACHE[clave] or archivos or Archivos()


def olvidar():
    """Vacía lo leído: lo usan las pruebas y quien acaba de cambiar el estándar."""
    _CACHE.clear()
