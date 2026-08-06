#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integración continua — `09·G6`.

G6: las **pruebas y el linter** corren en un **pipeline reproducible** (CI), no
dependen de que alguien se acuerde. Comprobable: existe un archivo de pipeline y
menciona correr pruebas y linter.

Multiproyecto: reconoce los CI más comunes por su ubicación (GitHub Actions,
GitLab, Azure, CircleCI, Jenkins, Bitbucket, Drone, Travis), sin asumir stack.

**AVISO**: puede haber CI en un sistema no reconocido, o el pipeline llamar a un
script propio; se señala para que un humano confirme, no se bloquea.
"""
import os
import re

import instalar
import versionado
from comun import AVISO, Hallazgo, leer

_CI = re.compile(
    r"(^|/)\.github/workflows/[^/]+\.ya?ml$|(^|/)\.gitlab-ci\.yml$|"
    r"(^|/)(azure-pipelines|bitbucket-pipelines)\.yml$|(^|/)Jenkinsfile$|"
    r"(^|/)\.circleci/config\.yml$|(^|/)\.drone\.yml$|(^|/)\.travis\.yml$")

_CORRE_PRUEBAS = re.compile(
    r"(?i)\b(test|tests|pruebas|phpunit|pytest|jest|vitest|artisan\s+test|npm\s+test|go\s+test)\b")
_CORRE_LINTER = re.compile(
    r"(?i)\b(lint|linter|pint|phpstan|psalm|eslint|prettier|ruff|flake8|rubocop|golangci)\b")


def revisar_ci(textos):
    """Núcleo puro: dada la lista de contenidos de los archivos de CI, ¿corren
    pruebas y linter? Devuelve la lista de motivos (vacía si todo bien).
    Sin archivos de CI = lista con el motivo de ausencia. Aislado de git."""
    if not textos:
        return ["no se ve un pipeline de CI (G6): pruebas y linter deberían "
                "correr solos en cada cambio"]
    junto = "\n".join(textos)
    motivos = []
    if not _CORRE_PRUEBAS.search(junto):
        motivos.append("el CI no parece correr las pruebas (G6)")
    if not _CORRE_LINTER.search(junto):
        motivos.append("el CI no parece correr el linter (G6)")
    return motivos


def validar(raiz):
    raiz = os.path.abspath(raiz)
    repos = instalar.repositorios_git(raiz)
    if not repos:
        return [Hallazgo(AVISO, raiz, 0, "no hay repositorios git que revisar")]

    hallazgos = []
    for repo in repos:
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        donde = raiz if etiqueta == "." else f"{etiqueta}/"
        textos = []
        for a in versionado.archivos_versionados(repo):
            if _CI.search(a):
                try:
                    textos.append(leer(os.path.join(repo, a)))
                except OSError:
                    pass
        for motivo in revisar_ci(textos):
            hallazgos.append(Hallazgo(AVISO, donde, 0, motivo))
    return hallazgos
