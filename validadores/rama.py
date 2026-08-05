#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trabajo en rama dedicada y al día — `09·G4`.

G4: el trabajo va en una **rama** dedicada (salvo que la capa 3 diga otra cosa),
mantenida **al día** con la principal, y la principal queda siempre funcional.

Universal a cualquier proyecto git: se detecta el nombre de la principal (sea
`main`, `master` o lo que apunte `origin/HEAD`), no se asume ninguno.

Todo es **AVISO**: trabajar sobre la principal puede ser deliberado —la capa 3
de un proyecto puede permitirlo, y este mismo repo lo hace—; e ir un poco atrás
es una señal para sincronizar, no un incumplimiento que deba frenar nada.
"""
import os
import subprocess

import instalar
from comun import AVISO, Hallazgo


def _git(repo, *args):
    salida = subprocess.run(
        ["git", "-C", repo, *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if salida.returncode != 0:
        return []
    return [l.strip() for l in salida.stdout.splitlines() if l.strip()]


def rama_actual(repo):
    salida = _git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    return salida[0] if salida else None


def rama_principal(repo):
    """El nombre de la principal, sin asumir cuál es.

    Primero lo que declare el remoto (`origin/HEAD`); si no, el primer nombre
    convencional que exista como rama local.
    """
    ref = _git(repo, "symbolic-ref", "--short", "refs/remotes/origin/HEAD")
    if ref:
        return ref[0].split("/", 1)[-1]         # "origin/main" -> "main"
    for candidata in ("main", "master", "trunk", "develop"):
        if _git(repo, "rev-parse", "--verify", "--quiet", f"refs/heads/{candidata}"):
            return candidata
    return None


def commits_detras(repo, principal):
    """Cuántos commits tiene la principal que HEAD no. Prefiere la rama local;
    si solo existe en el remoto, la del remoto."""
    for ref in (principal, f"origin/{principal}"):
        salida = _git(repo, "rev-list", "--count", f"HEAD..{ref}")
        if salida:
            try:
                return int(salida[0])
            except ValueError:
                return 0
    return 0


def evaluar(actual, principal, detras, donde=""):
    """Núcleo puro: dado el estado de las ramas, ¿qué señala G4? Aislado de git
    para probarlo sin un repositorio real."""
    if actual == "HEAD":
        return [Hallazgo(AVISO, donde, 0,
                         "HEAD desprendido: no se está en una rama (G4)")]
    if principal is None or actual is None:
        return []                               # no se pudo determinar: no se opina
    if actual == principal:
        return [Hallazgo(AVISO, donde, 0,
                         f"se está trabajando en la rama principal `{actual}`; "
                         f"G4 pide una rama dedicada (salvo que la capa 3 lo permita)")]
    if detras > 0:
        return [Hallazgo(AVISO, donde, 0,
                         f"la rama `{actual}` está {detras} commit(s) detrás de "
                         f"`{principal}`; G4 pide mantenerla al día")]
    return []


def validar(raiz):
    raiz = os.path.abspath(raiz)
    repos = instalar.repositorios_git(raiz)
    if not repos:
        return [Hallazgo(AVISO, raiz, 0, "no hay repositorios git que revisar")]

    hallazgos = []
    for repo in repos:
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        donde = raiz if etiqueta == "." else f"{etiqueta}/"
        actual = rama_actual(repo)
        principal = rama_principal(repo)
        detras = commits_detras(repo, principal) if principal else 0
        hallazgos += evaluar(actual, principal, detras, donde)
    return hallazgos
