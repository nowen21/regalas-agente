#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validadores que **corren la herramienta del ecosistema** — Q6, T5, DEP3.

Categoría aparte de los demás validadores. Los otros leen archivos y deciden
solos; estos **invocan una herramienta externa** y reportan su resultado:

  Q6  · linter/formateador sin advertencias  → pint/phpstan, eslint/prettier, ruff…
  T5  · las pruebas se corren y se reporta    → phpunit/artisan, npm test, pytest…
  DEP3· audit de vulnerabilidades             → composer/npm/pip audit…

Por eso **no van en el hook automático**: dependen del toolchain instalado,
tardan y tienen efectos (T5 toca la BD, DEP3 va a la red). Se corren a demanda.

Multiproyecto **por detección de stack**: se localiza cada manifiesto versionado
(`composer.json`, `package.json`…) y se corre la herramienta **en su carpeta**,
sin asumir un framework. Si no hay herramienta, se avisa; no se inventa nada.

La norma no se duplica: linting, pruebas y audit los define y ejecuta la
herramienta del ecosistema; aquí solo se la invoca y se traduce su salida.
"""
import os
import shutil
import subprocess

import instalar
import versionado
from comun import AVISO, FALLA, Hallazgo

# Manifiesto versionado -> ecosistema. Un proyecto puede tener varios.
MANIFIESTOS = [
    ("composer.json", "php"),
    ("package.json", "node"),
    ("pyproject.toml", "python"),
    ("requirements.txt", "python"),
    ("Pipfile", "python"),
    ("Gemfile", "ruby"),
    ("go.mod", "go"),
]

_INSTALADO = ("vendor/", "node_modules/")


def stack_de_manifiesto(nombre):
    """Ecosistema de un manifiesto por su nombre, o None. Puro, para pruebas."""
    for manif, stack in MANIFIESTOS:
        if nombre == manif:
            return stack
    return None


def _es_instalado(ruta):
    return ruta.startswith(_INSTALADO) or "/vendor/" in f"/{ruta}" \
        or "/node_modules/" in f"/{ruta}"


def proyectos(repo):
    """(carpeta_absoluta, stack) por cada manifiesto versionado del repo."""
    hallados = set()
    for ruta in versionado.archivos_versionados(repo):
        if _es_instalado(ruta):
            continue
        stack = stack_de_manifiesto(os.path.basename(ruta))
        if stack:
            carpeta = os.path.normpath(os.path.join(repo, os.path.dirname(ruta)))
            hallados.add((carpeta, stack))
    return sorted(hallados)


def _bin_local(carpeta, nombre):
    """Ruta a un ejecutable instalado por el proyecto (`vendor/bin`,
    `node_modules/.bin`). En Windows prioriza `.bat`/`.cmd`/`.exe`: el archivo
    sin extensión es el script unix (PHP/sh) y no corre como programa nativo."""
    exts = (".bat", ".cmd", ".exe", "") if os.name == "nt" else ("", ".bat", ".cmd", ".exe")
    for sub in ("vendor/bin", "node_modules/.bin"):
        for ext in exts:
            p = os.path.join(carpeta, sub.replace("/", os.sep), nombre + ext)
            if os.path.isfile(p):
                return p
    return None


def _correr(carpeta, args, timeout):
    """Corre `args` en `carpeta`. Devuelve (returncode, salida) o (None, motivo)
    si no se pudo (herramienta ausente o tiempo agotado)."""
    exe = args[0]
    if os.sep not in exe and "/" not in exe:
        # Nombre pelado (composer, npm): resolverlo por PATH. `shutil.which`
        # respeta PATHEXT en Windows, así encuentra el `.bat`/`.cmd` real.
        resuelto = shutil.which(exe)
        if not resuelto:
            return None, "herramienta no encontrada"
        args = [resuelto] + list(args[1:])
    try:
        r = subprocess.run(args, cwd=carpeta, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        return r.returncode, ((r.stdout or "") + (r.stderr or "")).strip()
    except FileNotFoundError:
        return None, "herramienta no encontrada"
    except subprocess.TimeoutExpired:
        return None, f"tiempo agotado ({timeout}s)"
    except OSError as e:
        return None, str(e)


def _resumen(salida, lineas=2, tope=200):
    """Últimas líneas útiles de la salida, acotadas: da contexto sin volcar todo
    (una herramienta puede escupir un JSON enorme). El detalle se ve corriéndola."""
    utiles = [l.strip() for l in salida.splitlines() if l.strip()]
    texto = " · ".join(utiles[-lineas:]) if utiles else "sin salida"
    return texto if len(texto) <= tope else texto[:tope] + "… (correr la herramienta para el detalle)"


# ── Selección de comando por stack ──────────────────────────────────────────

def _cmd_linter(carpeta, stack):
    if stack == "php":
        if _bin_local(carpeta, "pint"):
            return "pint", [_bin_local(carpeta, "pint"), "--test"]
        if _bin_local(carpeta, "phpstan"):
            return "phpstan", [_bin_local(carpeta, "phpstan"), "analyse", "--no-progress"]
        if _bin_local(carpeta, "php-cs-fixer"):
            return "php-cs-fixer", [_bin_local(carpeta, "php-cs-fixer"), "fix", "--dry-run"]
    if stack == "node":
        if _bin_local(carpeta, "eslint"):
            return "eslint", [_bin_local(carpeta, "eslint"), "."]
        if _bin_local(carpeta, "prettier"):
            return "prettier", [_bin_local(carpeta, "prettier"), "--check", "."]
    if stack == "python":
        if _bin_local(carpeta, "ruff"):
            return "ruff", [_bin_local(carpeta, "ruff"), "check"]
        if _bin_local(carpeta, "flake8"):
            return "flake8", [_bin_local(carpeta, "flake8")]
    return None, None


def _cmd_suite(carpeta, stack):
    if stack == "php":
        if _bin_local(carpeta, "phpunit"):
            return "phpunit", [_bin_local(carpeta, "phpunit"), "--no-coverage"]
    if stack == "node":
        return "npm test", ["npm", "test", "--silent"]
    if stack == "python":
        if _bin_local(carpeta, "pytest"):
            return "pytest", [_bin_local(carpeta, "pytest"), "-q"]
    return None, None


def _cmd_audit(carpeta, stack):
    if stack == "php":
        return "composer audit", ["composer", "audit", "--no-interaction", "--format=plain"]
    if stack == "node":
        return "npm audit", ["npm", "audit"]
    if stack == "python":
        if _bin_local(carpeta, "pip-audit"):
            return "pip-audit", [_bin_local(carpeta, "pip-audit")]
    return None, None


# ── Corredor genérico ───────────────────────────────────────────────────────

def _validar(raiz, elegir_cmd, regla, falla_si_rc, timeout):
    raiz = os.path.abspath(raiz)
    repos = instalar.repositorios_git(raiz)
    if not repos:
        return [Hallazgo(AVISO, raiz, 0, "no hay repositorios git que revisar")]

    hallazgos = []
    for repo in repos:
        for carpeta, stack in proyectos(repo):
            donde = os.path.relpath(carpeta, raiz).replace("\\", "/")
            nombre, args = elegir_cmd(carpeta, stack)
            if not nombre:
                hallazgos.append(Hallazgo(
                    AVISO, donde, 0,
                    f"{stack}: no se encontró herramienta para {regla}"))
                continue
            rc, salida = _correr(carpeta, args, timeout)
            if rc is None:
                hallazgos.append(Hallazgo(
                    AVISO, donde, 0, f"no se pudo correr {nombre}: {salida} ({regla})"))
            elif rc != 0:
                sev = FALLA if falla_si_rc else AVISO
                hallazgos.append(Hallazgo(
                    sev, donde, 0, f"{nombre} reporta problemas — {_resumen(salida)} ({regla})"))
    return hallazgos


def linter(raiz):
    return _validar(raiz, _cmd_linter, "Q6", falla_si_rc=False, timeout=300)


def suite(raiz):
    return _validar(raiz, _cmd_suite, "T5", falla_si_rc=True, timeout=600)


def auditoria(raiz):
    return _validar(raiz, _cmd_audit, "DEP3", falla_si_rc=False, timeout=180)
