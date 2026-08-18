#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Qué está versionado que no debería — `base/09-git.md` · G3.

G3 manda al archivo de exclusión: **secretos**, **datos sensibles/reales**,
**artefactos generados** y **config local** de máquina/editor; y versionar en su
lugar una **plantilla de ejemplo sin valores**.

La fuente de verdad es `git ls-files`: lo que git tiene registrado, no lo que
hay en disco. Un archivo puede estar en el disco y estar bien ignorado — eso no
es incumplimiento. El incumplimiento es que git lo tenga.

**Por qué esta regla es distinta a las demás:** un secreto subido a git no se
borra editándolo. Queda en el historial de todos los que clonaron. Por eso los
secretos son FALLA y no AVISO.
"""
import os
import re
import subprocess

import comun
from comun import AVISO, FALLA, Hallazgo

# Nombres de plantilla de ejemplo que G3 sí quiere versionados.
EJEMPLOS = re.compile(
    r"\.(example|sample|template|dist|ejemplo|plantilla)$|"
    r"^\.env\.(example|sample|template|dist)$", re.IGNORECASE)

# FALLA — secretos y dependencias. No hay lectura razonable en que estén bien.
PROHIBIDO = [
    (re.compile(r"(^|/)\.env(\.|$)", re.IGNORECASE),
     "entorno real con valores"),
    (re.compile(r"(^|/)node_modules/"),
     "dependencias instaladas"),
    (re.compile(r"\.(pem|key|p12|pfx|jks|keystore|ppk)$", re.IGNORECASE),
     "archivo de clave"),
    (re.compile(r"(^|/)id_(rsa|dsa|ecdsa|ed25519)$"),
     "clave SSH privada"),
    (re.compile(r"(^|/)\.npmrc$|(^|/)\.pypirc$|(^|/)\.netrc$"),
     "credenciales de repositorio"),
]

# AVISO — puede ser deliberado. Se señala, no se bloquea.
DUDOSO = [
    (re.compile(r"\.(log)$", re.IGNORECASE), "registro generado"),
    (re.compile(r"\.(sqlite|sqlite3|db|mdb)$", re.IGNORECASE), "base de datos"),
    # El `.sql` se decide por contenido, no por extensión — ver _es_volcado().
    (re.compile(r"(^|/)(\.idea|\.vscode)/"), "config local del editor"),
    (re.compile(r"(^|/)__pycache__/|\.pyc$"), "compilado de Python"),
    (re.compile(r"(^|/)(dist|build)/"), "artefacto de compilación"),
    (re.compile(r"(^|/)(\.DS_Store|Thumbs\.db)$"), "basura del sistema"),
]


def _git(repo, *args):
    salida = subprocess.run(
        ["git", "-C", repo, *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if salida.returncode != 0:
        return []
    return [l.strip() for l in salida.stdout.splitlines() if l.strip()]


def archivos_versionados(repo):
    """Lo que git tiene registrado en este repositorio."""
    return _git(repo, "ls-files")


def archivos_preparados(repo):
    """Lo que entra en el commit que se está por hacer.

    El enganche revisa **solo esto**, no el repositorio entero. Si mirara todo,
    un archivo dudoso que lleva meses ahí bloquearía cada commit futuro, y a la
    semana alguien desactiva el enganche. Se revisa lo que entra ahora.
    """
    return _git(repo, "diff", "--cached", "--name-only", "--diff-filter=ACMR")


MINIMO_INSERTS = 5
_INSERT = re.compile(r"\bINSERT\s+INTO\b", re.IGNORECASE)


def _es_volcado_con_datos(ruta_absoluta):
    """¿Este `.sql` trae datos, o solo estructura?

    G3 prohíbe versionar **datos reales**, no cualquier `.sql`. Un esquema, una
    migración o un `.sql` de documentación son estructura y se versionan sin
    problema; un volcado con filas de la base productiva, no.

    Se decide por contenido: varios `INSERT INTO` es un volcado. Marcarlo por
    la extensión daba falsos positivos en todos los repositorios reales.
    """
    try:
        with open(ruta_absoluta, encoding="utf-8", errors="replace") as f:
            muestra = f.read(2_000_000)     # 2 MB basta para decidir
    except OSError:
        return False
    return len(_INSERT.findall(muestra)) >= MINIMO_INSERTS


def _es_vendor_de_dependencias(ruta):
    """`vendor/` en la raíz son dependencias; más adentro suele ser deliberado.

    Distinción necesaria: Composer instala en `vendor/` (no se versiona), pero
    `static/vendor/` o `assets/vendor/` son librerías copiadas a propósito para
    funcionar sin internet — eso sí se versiona.
    """
    return ruta.startswith("vendor/")


def clasificar(repo, archivo):
    """Devuelve (severidad, motivo) si el archivo no debería estar versionado.

    Un archivo se clasifica **una sola vez**, en este orden: exento, prohibido,
    dudoso. Devuelve None si está bien versionado.
    """
    if EJEMPLOS.search(archivo):
        return None         # plantilla sin valores: G3 la quiere versionada

    if _es_vendor_de_dependencias(archivo):
        return FALLA, "dependencias instaladas"

    for patron, motivo in PROHIBIDO:
        if patron.search(archivo):
            return FALLA, motivo

    # Librería copiada a propósito (`public/vendor/…`, `static/vendor/…`): su
    # contenido es de terceros y suele traer `dist/`, minificados y demás. Se
    # versiona entero y a conciencia, así que no se opina sobre sus archivos.
    if "/vendor/" in f"/{archivo}":
        return None

    # El `.sql` se decide por contenido: estructura sí, datos reales no.
    if archivo.lower().endswith(".sql"):
        if _es_volcado_con_datos(os.path.join(repo, archivo)):
            return AVISO, "volcado con datos reales"
        return None

    for patron, motivo in DUDOSO:
        if patron.search(archivo):
            return AVISO, motivo

    return None


def validar(repo, ruta_mostrada=None, solo_preparados=False):
    origen = ruta_mostrada or repo
    hallazgos = []
    versionados = (archivos_preparados(repo) if solo_preparados
                   else archivos_versionados(repo))

    for archivo in versionados:
        veredicto = clasificar(repo, archivo)
        if veredicto:
            severidad, motivo = veredicto
            texto = ("versionado y no debería" if severidad == FALLA
                     else "¿debería estar versionado?")
            hallazgos.append(Hallazgo(
                severidad, origen, 0, f"{texto} ({motivo}): {archivo}"))

    # G3 cierra pidiendo la plantilla de ejemplo. Si el proyecto usa un archivo
    # de entorno pero nadie versionó el molde, quien clone no sabe qué llenar.
    if solo_preparados:
        return hallazgos    # el molde se revisa sobre el repo completo

    hay_entorno = os.path.isfile(os.path.join(repo, ".env"))
    hay_molde = any(a.lower().startswith(".env.") and EJEMPLOS.search(a)
                    for a in versionados)
    if hay_entorno and not hay_molde:
        hallazgos.append(Hallazgo(
            AVISO, origen, 0,
            "existe `.env` pero no hay plantilla de ejemplo versionada "
            "(G3: se versiona el molde sin valores)"))

    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("versionado")
