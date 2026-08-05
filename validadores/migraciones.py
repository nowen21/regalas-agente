#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Migraciones reversibles — `03·D2`.

D2: cada cambio de esquema es una migración **reversible**, con aplicación y
reversión funcionales. La parte comprobable sin criterio es que exista la
**reversión**; que funcione de verdad es harina de otro costal.

Multiproyecto **por detección de stack**: no se asume ningún framework. Se
reconoce la convención de cada migración por su extensión y la firma de su
contenido, y se aplica la regla de reversibilidad que le corresponde:

  Laravel/PHP     `function up` exige `function down`.
  Alembic/Python  `def upgrade` exige `def downgrade`.
  Django/Python   `RunPython`/`RunSQL` exigen `reverse_code`/`reverse_sql`;
                  el resto de operaciones de esquema Django las revierte solo.
  Rails/Ruby      `def change` (auto-reversible) o `def up` + `def down`.
  Node (js/ts)    `up` exige `down` (knex, sequelize, typeorm…).
  Pares SQL       `X.up.sql` exige `X.down.sql` (go-migrate, dbmate…).

Todo es **AVISO**: una migración puede ser deliberadamente irreversible y estar
documentada (D2 lo contempla). Se señala para que un humano lo confirme.
"""
import os
import re

import instalar
import versionado
from comun import AVISO, Hallazgo, leer

# Carpetas donde viven las migraciones, sin importar el framework.
_CARPETAS = ("/migrations/", "/migrate/", "/versions/")
_EXTENSIONES = (".php", ".py", ".rb", ".js", ".ts", ".mjs", ".cjs", ".sql")
_SALTAR = re.compile(r"(^|/)(vendor|node_modules)/")


def es_candidata(ruta):
    """¿Este archivo versionado tiene pinta de migración? Por ubicación o por
    ser una mitad de un par `.up.sql`/`.down.sql`."""
    r = ruta.lower()
    if _SALTAR.search(r):
        return False
    if r.endswith((".up.sql", ".down.sql")):
        return True
    if any(c in f"/{r}" for c in _CARPETAS):
        return r.endswith(_EXTENSIONES)
    return False


def revisar_migracion(ruta, texto, hermanos=()):
    """Núcleo puro: ¿esta migración declara su reversión? Devuelve el motivo si
    no, o None. `hermanos` = nombres de archivo en la misma carpeta (para los
    pares `.sql`). Aislado de git y del disco para probarlo directo."""
    base = os.path.basename(ruta)
    low = base.lower()
    ext = os.path.splitext(low)[1]
    t = texto

    if low.endswith(".up.sql"):
        pareja = base[:-len(".up.sql")] + ".down.sql"
        if pareja not in hermanos:
            return f"falta el archivo de reversión `{pareja}` (D2)"
        return None
    if low.endswith(".down.sql"):
        return None                             # la pareja la evalúa el `.up`

    if ext == ".py":
        if "django.db" in t or "from django" in t:
            faltan = []
            if "RunPython(" in t and "reverse_code" not in t:
                faltan.append("RunPython sin reverse_code")
            if "RunSQL(" in t and "reverse_sql" not in t:
                faltan.append("RunSQL sin reverse_sql")
            return (f"migración Django no reversible: {', '.join(faltan)} (D2)"
                    if faltan else None)
        if re.search(r"def\s+upgrade\b", t):
            return (None if re.search(r"def\s+downgrade\b", t)
                    else "Alembic: `upgrade` sin `downgrade` (D2)")
        return None

    if ext == ".rb":
        if re.search(r"def\s+change\b", t):
            return None                         # `change` se revierte solo
        if re.search(r"def\s+up\b", t) and not re.search(r"def\s+down\b", t):
            return "Rails: `up` sin `down` ni `change` (D2)"
        return None

    if ext == ".php":
        if re.search(r"function\s+up\b", t) and not re.search(r"function\s+down\b", t):
            return "`up` sin `down` (D2)"
        return None

    if ext in (".js", ".ts", ".mjs", ".cjs"):
        up = re.search(r"exports\.up|function\s+up\b|\bup\s*[:(=]", t)
        down = re.search(r"exports\.down|function\s+down\b|\bdown\s*[:(=]", t)
        return "`up` sin `down` (D2)" if (up and not down) else None

    return None


def validar(raiz):
    raiz = os.path.abspath(raiz)
    repos = instalar.repositorios_git(raiz)
    if not repos:
        return [Hallazgo(AVISO, raiz, 0, "no hay repositorios git que revisar")]

    hallazgos = []
    for repo in repos:
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        prefijo = "" if etiqueta == "." else f"{etiqueta}/"
        candidatas = [a for a in versionado.archivos_versionados(repo)
                      if es_candidata(a)]

        # Nombres por carpeta, para resolver los pares `.up.sql`/`.down.sql`.
        por_carpeta = {}
        for a in candidatas:
            por_carpeta.setdefault(os.path.dirname(a), set()).add(os.path.basename(a))

        for a in candidatas:
            try:
                texto = leer(os.path.join(repo, a))
            except OSError:
                continue
            motivo = revisar_migracion(a, texto, por_carpeta[os.path.dirname(a)])
            if motivo:
                hallazgos.append(Hallazgo(AVISO, f"{prefijo}{a}", 0, motivo))

    return hallazgos
