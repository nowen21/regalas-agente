# -*- coding: utf-8 -*-
"""Dónde guarda Claude Code los registros de un proyecto.

Claude Code los deja en `~/.claude/projects/«carpeta»/`, y la carpeta sale de
la ruta del proyecto: cada carácter que no es letra o número pasa a `-`.
`C:\\Ing. Jose\\ia\\agente` da `c--Ing--Jose-ia-agente`.

**La letra de la unidad** queda como venía la ruta al abrir la herramienta: en
esta máquina, en minúscula. Se calcula en minúscula, y si existe la carpeta con
la letra en mayúscula, se usa esa.
"""
import os
import re

_NO_ALFANUMERICO = re.compile(r"[^A-Za-z0-9]")


def proyectos_de_claude():
    """La carpeta donde Claude Code guarda los registros de todos los proyectos."""
    return os.path.join(os.path.expanduser("~"), ".claude", "projects")


def nombre_de_carpeta(ruta):
    """El nombre que Claude Code le da a la carpeta de `ruta`, con la unidad en minúscula."""
    absoluta = os.path.abspath(ruta)
    unidad, resto = os.path.splitdrive(absoluta)
    return _NO_ALFANUMERICO.sub("-", unidad.lower() + resto)


def carpeta_de_claude(ruta, base=None):
    """El nombre de la carpeta de `ruta` dentro de `base` (por defecto, la de Claude Code)."""
    base = base or proyectos_de_claude()
    nombre = nombre_de_carpeta(ruta)
    mayuscula = nombre[:1].upper() + nombre[1:]
    if not os.path.isdir(os.path.join(base, nombre)) and os.path.isdir(os.path.join(base, mayuscula)):
        return mayuscula
    return nombre
