#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilidades compartidas por los validadores del estándar.

Principio: los validadores COMPRUEBAN, no arreglan. La norma vive en los `.md`;
aquí solo se verifica lo que se puede verificar sin criterio.

Dos severidades:
  FALLA — incumplimiento claro. Rompe la ejecución (código de salida 1).
  AVISO — algo que un humano debe mirar. No rompe nada.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FALLA = "FALLA"
AVISO = "AVISO"

# Carpetas que nunca se recorren.
EXCLUIDAS = {".git", "__pycache__", ".venv", "venv", "node_modules", "vendor"}

# Un marcador de plantilla: [texto] que NO es un enlace markdown ](...)
# ni una casilla de verificación - [ ] / - [x].
_MARCADOR = re.compile(r"\[([^\[\]\n]+)\](?!\()")
_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_CERCA = re.compile(r"^\s*(```|~~~)")
_ENLACE = re.compile(r"\[([^\]\n]*)\]\(([^)\s]+)")


class Hallazgo:
    """Un incumplimiento o aviso, anclado a archivo y línea."""

    def __init__(self, severidad, archivo, linea, mensaje):
        self.severidad = severidad
        self.archivo = archivo
        self.linea = linea          # 0 = el archivo completo, sin línea concreta
        self.mensaje = mensaje

    def __str__(self):
        rel = relativo(self.archivo)
        donde = f"{rel}:{self.linea}" if self.linea else rel
        return f"[{self.severidad}] {donde} — {self.mensaje}"


def preparar_salida():
    """La consola de Windows no siempre es UTF-8; evita que un acento rompa todo."""
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def relativo(ruta):
    """Ruta relativa al repositorio; absoluta si el archivo vive fuera de él."""
    try:
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
    except ValueError:      # otra unidad en Windows
        return ruta.replace("\\", "/")
    if rel.startswith(".."):
        return os.path.abspath(ruta).replace("\\", "/")
    return rel


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def lineas_utiles(texto):
    """Devuelve (numero_de_linea, contenido) saltando los bloques de código.

    Sin esto, un ejemplo dentro de ``` se trataría como encabezado o marcador.
    """
    dentro = False
    for n, linea in enumerate(texto.splitlines(), start=1):
        if _CERCA.match(linea):
            dentro = not dentro
            continue
        if not dentro:
            yield n, linea


def encabezados(texto, desde_nivel=2):
    """Encabezados del documento, del nivel indicado hacia abajo.

    Se ignora el H1 a propósito: en un documento real lleva el ID y el título
    concretos, así que nunca coincide con el de la plantilla.
    """
    salida = []
    for n, linea in lineas_utiles(texto):
        m = _ENCABEZADO.match(linea)
        if m and len(m.group(1)) >= desde_nivel:
            salida.append((n, m.group(2).strip()))
    return salida


def marcadores(texto):
    """Marcadores [así] sin llenar. Excluye enlaces y casillas de verificación."""
    salida = []
    for n, linea in lineas_utiles(texto):
        for m in _MARCADOR.finditer(linea):
            contenido = m.group(1).strip()
            if contenido and contenido not in ("x", "X"):
                salida.append((n, m.group(0)))
    return salida


def enlaces(texto):
    """Enlaces markdown del documento: (numero_de_linea, texto, destino)."""
    salida = []
    for n, linea in lineas_utiles(texto):
        for m in _ENLACE.finditer(linea):
            salida.append((n, m.group(1), m.group(2)))
    return salida


def recorrer_md(raiz):
    """Todos los .md bajo `raiz`, saltando las carpetas excluidas."""
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
        for nombre in sorted(archivos):
            if nombre.lower().endswith(".md"):
                yield os.path.join(carpeta, nombre)


def reportar(hallazgos, titulo=None):
    """Imprime los hallazgos y devuelve el código de salida (1 si hay FALLA)."""
    fallas = [h for h in hallazgos if h.severidad == FALLA]
    avisos = [h for h in hallazgos if h.severidad == AVISO]

    if titulo:
        print(f"== {titulo} ==")

    for h in fallas:
        print(str(h))
    for h in avisos:
        print(str(h))

    if not hallazgos:
        print("OK: sin incumplimientos.")
        return 0

    print(f"\n{len(fallas)} falla(s), {len(avisos)} aviso(s).")
    return 1 if fallas else 0
