#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas contra una BD efímera, no real — `08·T4`.

T4: las pruebas corren contra un entorno **efímero y aislado** (BD en memoria o
dedicada que se crea y destruye por corrida), nunca contra datos reales.

Comprobable en Laravel por su `phpunit.xml`: si fija `DB_DATABASE` a `:memory:`
o a una base con "test" en el nombre, está aislado; si la apunta a otra base, o
no configura ninguna, las pruebas podrían caer sobre la BD real → **AVISO**.

Multiproyecto por detección: Django y pytest-django crean una BD de test con
prefijo `test_` **de fábrica**, así que su aislamiento lo garantiza el framework
y no se marca. Se cubre lo que un proyecto puede desconfigurar a mano.
"""
import os
import re

import instalar
import versionado
from comun import AVISO, Hallazgo, leer

_ENV = re.compile(r'<env\s+name="([^"]+)"\s+value="([^"]*)"')


def revisar_phpunit(texto, hay_env_testing=False):
    """Núcleo puro: motivo si el `phpunit.xml` no asegura una BD efímera, o None."""
    env = {n: v for n, v in _ENV.findall(texto)}
    base = env.get("DB_DATABASE")

    if base is not None:
        if base == ":memory:" or "test" in base.lower():
            return None                         # en memoria o dedicada: aislado
        return (f"las pruebas apuntan a `DB_DATABASE={base}`, que no parece "
                f"efímera ni dedicada (T4: usar `:memory:` o una BD de test)")

    if hay_env_testing:
        return None                             # el aislamiento va en `.env.testing`
    return ("`phpunit.xml` no fija una BD de pruebas aislada; podría usar la real "
            "(T4: fijar `DB_DATABASE=:memory:` o un `.env.testing`)")


def validar(raiz):
    raiz = os.path.abspath(raiz)
    repos = instalar.repositorios_git(raiz)
    if not repos:
        return [Hallazgo(AVISO, raiz, 0, "no hay repositorios git que revisar")]

    hallazgos = []
    for repo in repos:
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        prefijo = "" if etiqueta == "." else f"{etiqueta}/"
        versionados = set(versionado.archivos_versionados(repo))
        for a in versionados:
            if os.path.basename(a).lower() != "phpunit.xml":
                continue
            carpeta = os.path.dirname(a)
            hay_env = f"{carpeta}/.env.testing".lstrip("/") in versionados \
                or os.path.isfile(os.path.join(repo, carpeta, ".env.testing"))
            try:
                texto = leer(os.path.join(repo, a))
            except OSError:
                continue
            motivo = revisar_phpunit(texto, hay_env)
            if motivo:
                hallazgos.append(Hallazgo(AVISO, f"{prefijo}{a}", 0, motivo))
    return hallazgos
