# -*- coding: utf-8 -*-
"""`EP-026·HU-003` · Pasa el estándar y la memoria de cada proyecto a la base.

**Una sola vez** (RN-05): si la base ya tiene el estándar, se niega. Desde ese
momento la fuente es la base; importar encima borraría lo que se cambió en ella.

**El texto entra exacto** (RNF-01): se lee sin traducir los saltos de línea.

**Es la versión de partida** (acuerdo 6): el número del archivo `VERSION`, y
todos los documentos son cambios de esa versión.
"""
import io
import os

from django.db import transaction

from core.comun import Proyecto as Carpeta
from core.historia import versiones
from core.historia.registro import en_version, quien_y_por_que
from core.proyectos.models import Proyecto

from .models import Documento, Recuerdo

BASE = "base"
MEMORIA = os.path.join("historico-chat", "memory")
QUIEN = "importar_estandar"


class YaImportado(Exception):
    """La base ya tiene el estándar."""


def _texto(ruta):
    with io.open(ruta, encoding="utf-8", newline="") as f:
        return f.read()


def documentos(raiz):
    """`[(ruta desde la raíz con /, ruta en disco)]` de todo lo que hay en `base/`."""
    salida = []
    for carpeta, subcarpetas, archivos in os.walk(os.path.join(raiz, BASE)):
        subcarpetas.sort()
        for nombre in sorted(archivos):
            if nombre.startswith(".") or nombre.endswith(".pyc"):
                continue
            completa = os.path.join(carpeta, nombre)
            salida.append((os.path.relpath(completa, raiz).replace(os.sep, "/"), completa))
    return salida


def recuerdos(proyecto):
    """`[(nombre, ruta en disco)]` de la memoria del proyecto."""
    carpeta = os.path.join(proyecto.ruta, MEMORIA)
    if not os.path.isdir(carpeta):
        return []
    return [(n, os.path.join(carpeta, n)) for n in sorted(os.listdir(carpeta))
            if n.endswith(".md") and os.path.isfile(os.path.join(carpeta, n))]


def _en_git(raiz, revision="HEAD"):
    """`{ruta: texto}` de `base/` tal como está guardado en git, sin lo que haya sin guardar."""
    from core.comun.git import Git

    git = Git(raiz)
    salida = {}
    for ruta in git.lineas("ls-tree", "-r", "--name-only", revision, BASE):
        salida[ruta] = git.correr("show", "%s:%s" % (revision, ruta))
    return salida


def _igual(a, b):
    return a.replace("\r\n", "\n") == b.replace("\r\n", "\n")


def sincronizar(raiz=None, tipo=None, motivo=""):
    """`EP-026·HU-004` · Pone la base al día con lo que dice git de `base/`: lo que
    cambió, lo nuevo y lo que ya no está. Todo en una versión del estándar, con su
    historia. Sin diferencias no sube versión. Devuelve `(creados, cambiados, quitados)`."""
    raiz = os.path.abspath(raiz or Carpeta.estandar())
    en_git = _en_git(raiz)
    if not en_git:
        raise ValueError("git no devolvió nada de %s/ en %s" % (BASE, raiz))
    en_base = {d.ruta: d for d in Documento.objects.all()}
    nuevos = sorted(set(en_git) - set(en_base))
    quitados = sorted(set(en_base) - set(en_git))
    cambiados = sorted(r for r in set(en_git) & set(en_base) if not _igual(en_git[r], en_base[r].contenido))
    if not (nuevos or quitados or cambiados):
        return 0, 0, 0
    motivo = motivo or "La base toma lo guardado en git de base/ (EP-026·HU-004)"
    with transaction.atomic(), quien_y_por_que(quien="sincronizar_estandar", motivo=motivo, tipo=tipo):
        for ruta in nuevos:
            Documento.objects.create(ruta=ruta, contenido=en_git[ruta])
        for ruta in cambiados:
            documento = en_base[ruta]
            texto = en_git[ruta]
            if "\r\n" in documento.contenido and "\r\n" not in texto:
                texto = texto.replace("\n", "\r\n")
            documento.contenido = texto
            documento.save()
        for ruta in quitados:
            en_base[ruta].delete()
    from .en_base import olvidar

    olvidar()
    return len(nuevos), len(cambiados), len(quitados)


def importar(raiz=None):
    """Importa y devuelve `(versión, documentos, recuerdos)`."""
    if Documento.objects.exists():
        raise YaImportado("la base ya tiene el estándar: desde la importación, la fuente es la base")
    raiz = os.path.abspath(raiz or Carpeta.estandar())
    numero = versiones.del_archivo()
    motivo = "El estándar %d.%d.%d entra a la base (EP-026·HU-003)" % numero
    n_doc = n_rec = 0
    with transaction.atomic(), quien_y_por_que(quien=QUIEN, motivo=motivo):
        version = versiones.de_partida(numero, motivo, QUIEN)
        with en_version(version):
            for ruta, completa in documentos(raiz):
                Documento.objects.create(ruta=ruta, contenido=_texto(completa))
                n_doc += 1
            for proyecto in Proyecto.objects.filter(activo=True):
                for nombre, completa in recuerdos(proyecto):
                    Recuerdo.objects.create(proyecto=proyecto, nombre=nombre, contenido=_texto(completa))
                    n_rec += 1
    return version, n_doc, n_rec
