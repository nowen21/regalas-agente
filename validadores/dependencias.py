#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lockfile presente y versionado — `10·DEP2`.

DEP2 pide fijar versiones con el **lockfile** del ecosistema y **versionarlo**,
para que todos —incluida producción— instalen exactamente lo mismo.

Es el complemento de `versionado.py` (G3), que revisa lo contrario: que **no** se
versione lo *instalado* (`vendor/`, `node_modules/`). Aquí se revisa que sí se
versione la **declaración** que lo reconstruye.

La comprobación no opina: si hay un manifiesto versionado (`composer.json`,
`package.json`…), su lockfile hermano tiene que estar versionado también. Se mira
`git ls-files`, no el disco: un lockfile en disco pero sin versionar no sirve —
quien clone no lo recibe.

Todo es **AVISO**: puede haber un motivo (un paquete raíz sin dependencias, un
`pyproject.toml` que es solo config de build). Lo señala para que un humano mire.
"""
import os

import instalar
import versionado
import comun
from comun import AVISO, Hallazgo

# manifiesto -> lockfiles que lo satisfacen (basta uno) · nombre del ecosistema.
ECOSISTEMAS = [
    ("composer.json", ("composer.lock",), "Composer/PHP"),
    ("package.json", ("package-lock.json", "yarn.lock", "pnpm-lock.yaml"), "npm/Node"),
    ("Pipfile", ("Pipfile.lock",), "Pipenv"),
    ("pyproject.toml", ("poetry.lock", "pdm.lock", "uv.lock"), "Python"),
    ("Gemfile", ("Gemfile.lock",), "Bundler/Ruby"),
    ("go.mod", ("go.sum",), "Go"),
    ("Cargo.toml", ("Cargo.lock",), "Cargo/Rust"),
]

# El manifiesto de una dependencia instalada no cuenta: no es la raíz del proyecto.
_INSTALADO = ("vendor/", "node_modules/")


def _es_instalado(ruta):
    return ruta.startswith(_INSTALADO) or "/vendor/" in f"/{ruta}" or "/node_modules/" in f"/{ruta}"


def revisar(versionados, prefijo=""):
    """Núcleo puro: dada la lista de archivos versionados, ¿falta algún lockfile?

    Aislado de git para poder probarlo sin un repositorio real. `validar()` solo
    le pasa lo que `git ls-files` devuelve por cada repo.
    """
    versionados = set(versionados)
    hallazgos = []
    for ruta in sorted(versionados):
        if _es_instalado(ruta):
            continue
        carpeta, nombre = os.path.split(ruta)
        for manifiesto, locks, ecosistema in ECOSISTEMAS:
            if nombre != manifiesto:
                continue
            esperados = [os.path.join(carpeta, l).replace("\\", "/") for l in locks]
            if not any(e in versionados for e in esperados):
                hallazgos.append(Hallazgo(
                    AVISO, f"{prefijo}{ruta}", 0,
                    f"{ecosistema}: hay `{manifiesto}` pero no un lockfile "
                    f"versionado ({' o '.join(locks)}) · DEP2"))
            break
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
        hallazgos += revisar(versionado.archivos_versionados(repo), prefijo)
    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("dependencias")
