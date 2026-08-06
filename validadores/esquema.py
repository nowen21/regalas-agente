#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integridad de esquema: FK con política de borrado — `03·D1`.

D1 pide, entre otras cosas, **integridad en la BD**: toda clave foránea con
**política de borrado explícita**. Esa es la parte comprobable sin criterio.

El resto de D1 se queda como juicio humano: la **normalización** (1FN/2FN/3FN) y
qué columnas de **auditoría** corresponden dependen del significado de cada
tabla —qué es pivot, qué es transaccional—, algo que dos personas pueden discutir.

Multiproyecto **por detección de stack**, y reconociendo que algunos lo resuelven
solos: se revisan migraciones Laravel (`->foreign`/`->constrained` sin `onDelete`)
y SQL crudo (`REFERENCES` sin `ON DELETE`). Django no se revisa porque su ORM
**exige** `on_delete` de fábrica: una FK sin política ni siquiera corre.

Todo **AVISO**: puede haber un motivo (una FK a un catálogo inmutable). Lo
confirma un humano.
"""
import os

import re

import codigo
import instalar
import migraciones
import versionado
from comun import AVISO, Hallazgo, leer

_FK_LARAVEL = re.compile(r"->\s*(foreign|foreignId|foreignIdFor|constrained)\b")
_POLITICA_LARAVEL = re.compile(r"(?i)on_?delete")       # onDelete, cascadeOnDelete…
_REFERENCES = re.compile(r"(?i)\breferences\b")
_ON_DELETE_SQL = re.compile(r"(?i)\bon\s+delete\b")


def _limites_sentencia(texto, pos):
    """La sentencia PHP que contiene `pos`, entre el `;` anterior y el siguiente."""
    ini = texto.rfind(";", 0, pos) + 1
    fin = texto.find(";", pos)
    return ini, (fin if fin != -1 else len(texto))


def revisar_esquema(ruta, texto):
    """Núcleo puro: devuelve una lista de `(linea, motivo)`. Aislado de git."""
    ext = os.path.splitext(ruta.lower())[1]
    hallazgos = []

    if ext == ".php":
        vistas = set()
        for m in _FK_LARAVEL.finditer(texto):
            ini, fin = _limites_sentencia(texto, m.start())
            if ini in vistas:
                continue                        # una sentencia, un hallazgo
            vistas.add(ini)
            if not _POLITICA_LARAVEL.search(texto[ini:fin]):
                hallazgos.append((codigo.linea_de(texto, m.start()),
                                  "clave foránea sin política de borrado explícita "
                                  "(D1: FK con `onDelete`)"))
    elif ext == ".sql":
        for m in _REFERENCES.finditer(texto):
            if not _ON_DELETE_SQL.search(texto[m.end():m.end() + 140]):
                hallazgos.append((codigo.linea_de(texto, m.start()),
                                  "`REFERENCES` sin `ON DELETE` "
                                  "(D1: FK con política de borrado)"))
    return hallazgos


def validar(raiz):
    raiz = os.path.abspath(raiz)
    repos = instalar.repositorios_git(raiz)
    if not repos:
        return [Hallazgo(AVISO, raiz, 0, "no hay repositorios git que revisar")]

    hallazgos = []
    for repo in repos:
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        prefijo = "" if etiqueta == "." else f"{etiqueta}/"
        for a in versionado.archivos_versionados(repo):
            if not migraciones.es_candidata(a):
                continue
            if os.path.splitext(a.lower())[1] not in (".php", ".sql"):
                continue
            try:
                texto = leer(os.path.join(repo, a))
            except OSError:
                continue
            for linea, motivo in revisar_esquema(a, texto):
                hallazgos.append(Hallazgo(AVISO, f"{prefijo}{a}", linea, motivo))
    return hallazgos
