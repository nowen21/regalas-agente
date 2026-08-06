#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas aisladas y deterministas — `08·T4` y `08·T3`.

T4: las pruebas corren contra un entorno **efímero y aislado** (BD en memoria o
dedicada que se crea y destruye por corrida), nunca contra datos reales.

T3: **independientes** (cualquier orden) y **deterministas** (mismo input, mismo
resultado; nada de flaky por reloj, azar o red). Comprobable: la suite se corre
en **orden aleatorio** y los tests no usan fuentes de azar/tiempo sin fijar.

Comprobable en Laravel por `phpunit.xml` (BD y `executionOrder`) y por las
fuentes flaky en los archivos de prueba. Django/pytest crean la BD de test de
fábrica, así que su aislamiento lo garantiza el framework. Todo **AVISO**.
"""
import os
import re

import codigo
import instalar
import versionado
from comun import AVISO, Hallazgo, leer

_ENV = re.compile(r'<env\s+name="([^"]+)"\s+value="([^"]*)"')

# T3 · orden de ejecución de la suite (phpunit) y fuentes de no-determinismo.
_EXEC_ORDER = re.compile(r'executionOrder\s*=\s*"([^"]*)"')
_ES_TEST = re.compile(r"(^|/)(tests?|spec)/|(Test|Spec)\.[a-z]+$|(^|/)test_[^/]+\.py$")
# `uniqid` queda fuera a propósito: se usa para datos únicos y el test sigue
# siendo determinista. Se marcan azar de valores y reloj, que sí rompen asserts.
_FLAKY = re.compile(r"\b(mt_rand|rand|array_rand|microtime|shuffle)\s*\(")


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


def revisar_orden(texto):
    """Núcleo puro: motivo si el `phpunit.xml` no corre en orden aleatorio, o None."""
    m = _EXEC_ORDER.search(texto)
    if m and "random" in m.group(1).lower():
        return None
    return ("la suite no se corre en orden aleatorio "
            "(T3: `executionOrder=\"random\"` para que no dependan del orden)")


def revisar_test(texto):
    """Núcleo puro: líneas de un archivo de prueba con fuentes de no-determinismo."""
    return [(n, m.group(1)) for n, linea in enumerate(texto.splitlines(), 1)
            for m in [_FLAKY.search(linea)] if m]


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
            for motivo in (revisar_phpunit(texto, hay_env), revisar_orden(texto)):
                if motivo:
                    hallazgos.append(Hallazgo(AVISO, f"{prefijo}{a}", 0, motivo))

    # T3 · fuentes de no-determinismo en los archivos de prueba.
    for donde, texto in codigo.archivos(raiz):
        if not _ES_TEST.search(donde):
            continue
        for linea, fuente in revisar_test(texto):
            hallazgos.append(Hallazgo(
                AVISO, donde, linea,
                f"fuente de azar/tiempo (`{fuente}`) en una prueba — T3: fijar "
                f"semilla/reloj o usar dobles (evita tests flaky)"))
    return hallazgos
