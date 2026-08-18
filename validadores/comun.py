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

# Un tramo `entre comillas invertidas`, con una o varias comillas de apertura,
# como en markdown. Lo de adentro es una muestra, no contenido del documento.
_CODIGO_EN_LINEA = re.compile(r"(`+)(?:(?!\1).)*?\1")


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


def sin_codigo_en_linea(linea):
    """La línea con los tramos `entre comillas invertidas` en blanco.

    `55` · Un plan de pruebas escribió, entre comillas, el texto que el caso
    tenía que encontrar: `` `[historico-chat/…](../../…)` ``. Eso no es un
    enlace, es una muestra — y el validador lo reportó roto dos veces. Las dos
    salidas eran malas: redactar torcido para callarlo, o aprender a ignorarlo.

    Se reemplaza por espacios en vez de borrarse, para no correr las columnas:
    el número de línea y la posición siguen valiendo.
    """
    return _CODIGO_EN_LINEA.sub(lambda m: " " * len(m.group(0)), linea)


def enlaces(texto):
    """Enlaces markdown del documento: (numero_de_linea, texto, destino).

    No mira dentro de los bloques cercados (`lineas_utiles`) ni de las comillas
    invertidas: ahí lo que hay son ejemplos de cómo se escribe un enlace, no
    enlaces a ninguna parte.
    """
    salida = []
    for n, linea in lineas_utiles(texto):
        for m in _ENLACE.finditer(sin_codigo_en_linea(linea)):
            salida.append((n, m.group(1), m.group(2)))
    return salida


def _celdas(linea):
    """Las celdas de una fila markdown, sin los bordes ni los espacios."""
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def _es_separador(celdas):
    return bool(celdas) and all(re.fullmatch(r":?-{2,}:?", c) for c in celdas)


def tablas(texto):
    """Las tablas markdown del documento.

    Devuelve `[(encabezados, filas)]`, donde `filas` es `[(numero_de_linea,
    celdas)]`. Se salta los bloques de código, así que una tabla de ejemplo
    dentro de ``` no cuenta como tabla del documento.

    Una tabla es un bloque de renglones que empiezan por `|` cuya segunda línea
    es la de guiones. Sin esa línea, markdown no la dibuja como tabla y aquí
    tampoco cuenta.
    """
    salida = []
    bloque = []

    def cerrar():
        if len(bloque) >= 2 and _es_separador(_celdas(bloque[1][1])):
            encabezados = _celdas(bloque[0][1])
            filas = [(n, _celdas(l)) for n, l in bloque[2:]]
            salida.append((encabezados, filas))
        bloque.clear()

    for n, linea in lineas_utiles(texto):
        if linea.strip().startswith("|"):
            bloque.append((n, linea))
        else:
            cerrar()
    cerrar()
    return salida


def filas_de(texto, *columnas):
    """Las filas de la primera tabla que tenga todas esas columnas.

    Devuelve `[(numero_de_linea, {columna: valor})]`. Busca por nombre de
    columna y no por posición: así una tabla que gane una columna al final no
    rompe a quien la lee.
    """
    objetivo = [c.lower() for c in columnas]
    for encabezados, filas in tablas(texto):
        bajos = [e.lower() for e in encabezados]
        if not all(c in bajos for c in objetivo):
            continue
        salida = []
        for n, celdas in filas:
            fila = {e: (celdas[i] if i < len(celdas) else "")
                    for i, e in enumerate(bajos)}
            salida.append((n, fila))
        return salida
    return []


def valor_limpio(celda):
    """El contenido de una celda, sin comillas invertidas ni marcador de plantilla.

    Una celda que sigue trayendo el `«…»` de la plantilla es una celda **sin
    llenar**: vale lo mismo que vacía, y devolver el marcador haría que el
    validador comparara contra un texto que nadie escribió.
    """
    v = celda.strip().strip("`").strip()
    if not v or v in ("—", "-", "–") or ("«" in v and "»" in v):
        return ""
    return v


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


def no_es_punto_de_entrada(subcomando=None):
    """Muere diciendo por dónde se corre. Nunca devuelve.

    Un módulo de comprobación **importado** por `validar.py` no hace nada al
    ejecutarse solo: cae hasta el final del archivo y sale con código 0. Y un
    código 0 sin salida se lee igual que «no encontré nada» — que es la peor
    mentira que puede decir un validador, porque afirma sin haber mirado.

    Ya costó una métrica falsa: la fase `B-EP-005-HU-008` escribió «cero
    enlaces rotos» el 2026-08-16 porque corrió `enlaces.py` a mano y no
    imprimió nada. El entrypoint real reportaba veinte.

    Sale con código 2 —ni 0 ni 1— para que un guion que lo llame por error
    pueda distinguir «no comprobé nada» de «comprobé y hay fallas».
    """
    modulo = os.path.basename(sys.argv[0]) or "este módulo"
    linea = (f"python validadores/validar.py {subcomando}" if subcomando
             else "python validadores/validar.py --help")
    preparar_salida()
    print(f"{modulo} no se corre solo: es una pieza de `validar.py`, "
          f"y correrlo así **no comprueba nada**.", file=sys.stderr)
    print(f"\nSe corre con:\n  {linea}", file=sys.stderr)
    sys.exit(2)
