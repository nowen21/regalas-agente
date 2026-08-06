#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integridad de esquema en las migraciones — `03·D1`, `03·D3`, `14·EST2`.

Tres cosas comprobables sin criterio sobre las migraciones:

  D1 (FK) · toda clave foránea con **política de borrado explícita**.
  D3      · una columna **obligatoria nueva** en una tabla existente debe traer
            **default** (si no, rompe las filas ya guardadas).
  EST2    · **límite de longitud** de identificadores (un nombre que pasa el
            máximo del motor, típico 64 en MySQL, revienta o se trunca).

Lo demás de esas reglas es juicio humano: la **normalización** y qué **auditoría**
corresponde (D1), y la **convención de nombres** en sí (EST2, EST1) dependen del
significado del dominio, que dos personas pueden discutir.

Multiproyecto **por detección de stack**, reconociendo que algunos lo resuelven
solos: se revisan migraciones Laravel y SQL crudo. Django no se revisa para D1
porque su ORM **exige** `on_delete` de fábrica.

Todo **AVISO**: puede haber un motivo legítimo (FK a un catálogo inmutable, una
columna que se puebla en el mismo lote). Lo confirma un humano.
"""
import os

import re

import codigo
import instalar
import migraciones
import versionado
from comun import AVISO, Hallazgo, leer

# D1
_FK_LARAVEL = re.compile(r"->\s*(foreign|foreignId|foreignIdFor|constrained)\b")
_POLITICA_LARAVEL = re.compile(r"(?i)on_?delete")       # onDelete, cascadeOnDelete…
_REFERENCES = re.compile(r"(?i)\breferences\b")
_ON_DELETE_SQL = re.compile(r"(?i)\bon\s+delete\b")

# D3 · una columna nueva en un ALTER. Solo aplica si el archivo es alter
# (`Schema::table`) y no crea la tabla (`Schema::create`): en una tabla nueva,
# NOT NULL está bien porque no hay filas que romper.
_COLUMNA_LARAVEL = re.compile(
    r"->\s*(string|char|text|longText|mediumText|integer|tinyInteger|"
    r"smallInteger|mediumInteger|bigInteger|unsignedBigInteger|unsignedInteger|"
    r"boolean|date|dateTime|dateTimeTz|timestamp|time|year|decimal|float|double|"
    r"json|jsonb|enum|uuid|ulid|foreignId|foreignUlid|ipAddress|binary)\s*\(")
_D3_SEGURO = re.compile(r"->\s*(nullable|default|change|useCurrent|autoIncrement)\b")
_ADD_NOT_NULL_SQL = re.compile(r"(?i)\bADD\b(?:\s+COLUMN)?\b[^;,]*\bNOT\s+NULL\b")
_DEFAULT_SQL = re.compile(r"(?i)\bDEFAULT\b")

# EST2 · identificador (nombre de tabla/columna/índice) sobre el límite del motor.
_LIMITE = 64
_IDENTIFICADOR = re.compile(r"['\"]([a-z_][a-z0-9_]{%d,})['\"]" % _LIMITE)


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
        es_alter = "Schema::table(" in texto and "Schema::create(" not in texto
        vistas_fk, vistas_d3 = set(), set()
        for m in _FK_LARAVEL.finditer(texto):
            ini, fin = _limites_sentencia(texto, m.start())
            if ini in vistas_fk:
                continue                        # una sentencia, un hallazgo
            vistas_fk.add(ini)
            if not _POLITICA_LARAVEL.search(texto[ini:fin]):
                hallazgos.append((codigo.linea_de(texto, m.start()),
                                  "clave foránea sin política de borrado explícita "
                                  "(D1: FK con `onDelete`)"))
        if es_alter:
            for m in _COLUMNA_LARAVEL.finditer(texto):
                ini, fin = _limites_sentencia(texto, m.start())
                if ini in vistas_d3:
                    continue
                vistas_d3.add(ini)
                if not _D3_SEGURO.search(texto[ini:fin]):
                    hallazgos.append((codigo.linea_de(texto, m.start()),
                                      "columna nueva obligatoria sin `default` en un "
                                      "ALTER (D3: rompe las filas existentes)"))
    elif ext == ".sql":
        for m in _REFERENCES.finditer(texto):
            if not _ON_DELETE_SQL.search(texto[m.end():m.end() + 140]):
                hallazgos.append((codigo.linea_de(texto, m.start()),
                                  "`REFERENCES` sin `ON DELETE` "
                                  "(D1: FK con política de borrado)"))
        for m in _ADD_NOT_NULL_SQL.finditer(texto):
            if not _DEFAULT_SQL.search(m.group(0)):
                hallazgos.append((codigo.linea_de(texto, m.start()),
                                  "`ADD ... NOT NULL` sin `DEFAULT` "
                                  "(D3: rompe las filas existentes)"))

    # EST2 · identificadores demasiado largos, en cualquier migración.
    for m in _IDENTIFICADOR.finditer(texto):
        hallazgos.append((codigo.linea_de(texto, m.start()),
                          f"identificador de {len(m.group(1))} caracteres, sobre el "
                          f"límite habitual de {_LIMITE} (EST2: longitud)"))
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
