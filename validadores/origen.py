# -*- coding: utf-8 -*-
"""`EP-023 · HU-002 · CA-01` · Cada punto dice de qué punto del anterior sale.

**Qué comprueba** (`02·F27`). En cada épica que nació de un análisis, sigue la
cadena de «Sale de» hacia arriba y detiene el punto que no cita su origen, o que
cita uno que no existe:

- el pendiente, frente al hallazgo que cita en «De dónde sale»;
- la conclusión del análisis, frente al turno de su conversación;
- la fila de «Lo que se tiene que hacer», frente a la conclusión que cita;
- el criterio de la HU, frente al punto de «Lo que se tiene que hacer».

**Lo que no mira, y se declara.**

- La tarea del plan frente a su criterio: la mira `flujo.py`, por `02·F18`.
- Las épicas que no nacieron de un análisis: no se reabren (`20·M10`), y así lo
  dice la excepción de `F27`.
- El análisis abierto: todavía se está llenando.
- Si el origen citado es el correcto: eso es un juicio y se lee.
"""
import os
import re

import comun
from comun import FALLA, Hallazgo, leer

_ANALISIS = re.compile(r"^analisis-(\d+)\.md$")
_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
_TURNO = re.compile(r"^### (\d+) · Usuario", re.M)
_FILA = re.compile(r"^\| *(\d+) *\|(.*)\|\s*$", re.M)
_CRITERIO = re.compile(r"^### (CA-\d+)", re.M)
_SALE_DE = re.compile(r"^\*\*Sale de:\*\*(.*)$", re.M)
_CITA = re.compile(r"análisis (\d+), puntos? (\d+(?:(?:, | y )\d+)*)")
_ENLACE_H = re.compile(r"\[[^\]]*?(H-\d+)[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)")

# Lo que no es del repositorio: local, generado o de terceros.
FUERA = {".git", ".venv", "venv", "__pycache__", "node_modules", "terceros"}


def _seccion(texto, titulo):
    """El texto de la sección `## <titulo>…` hasta la siguiente `## `."""
    m = re.search(r"^## %s.*$" % re.escape(titulo), texto, re.M)
    if not m:
        return ""
    fin = re.search(r"^## ", texto[m.end():], re.M)
    return texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]


def _filas(seccion):
    """`{número: [celdas]}` de las filas numeradas de una tabla."""
    return {int(n): [c.strip() for c in resto.split("|")] for n, resto in _FILA.findall(seccion)}


def leer_analisis(ruta):
    """Lo que el validador necesita de un análisis."""
    texto = leer(ruta)
    return {
        "aprobado": bool(_APROBADO.search(texto)),
        "turnos": {int(n) for n in _TURNO.findall(texto)},
        "conclusiones": _filas(_seccion(texto, "Conclusiones")),
        "hacer": _filas(_seccion(texto, "Lo que se tiene que hacer")),
    }


def epicas(raiz=None):
    """`{carpeta de la épica: [carpetas de pendiente con análisis]}`."""
    raiz = raiz or comun.RAIZ
    salida = {}
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
        if any(_ANALISIS.match(n) for n in archivos):
            salida.setdefault(os.path.dirname(carpeta), []).append(carpeta)
    return salida


def _revisar_analisis(ruta, datos):
    salida = []
    for n, celdas in sorted(datos["conclusiones"].items()):
        turnos = [int(x) for x in re.findall(r"\d+", celdas[-1])] if re.search(r"[Tt]urno", celdas[-1]) else []
        if not turnos:
            salida.append((ruta, f"la conclusión {n} no dice de qué turno sale"))
        for t in turnos:
            if t not in datos["turnos"]:
                salida.append((ruta, f"la conclusión {n} cita el turno {t}, que no está en la conversación"))
    for n, celdas in sorted(datos["hacer"].items()):
        citas = [int(x) for x in re.findall(r"\d+", celdas[1])] if len(celdas) > 2 else []
        if not citas:
            salida.append((ruta, f"el punto {n} de «Lo que se tiene que hacer» no dice de qué conclusión sale"))
        for c in citas:
            if c not in datos["conclusiones"]:
                salida.append((ruta, f"el punto {n} de «Lo que se tiene que hacer» cita la conclusión {c}, que no existe"))
    return salida


def _revisar_pendiente(ruta):
    texto = leer(ruta)
    fila = re.search(r"^\|[^|\n]*De dónde sale[^|\n]*\|(.*)\|\s*$", texto, re.M)
    if not fila:
        return [(ruta, "el pendiente no tiene «De dónde sale»")]
    citas = _ENLACE_H.findall(fila.group(1))
    if not citas:
        return [(ruta, "«De dónde sale» no enlaza ningún hallazgo")]
    salida = []
    for h, destino in citas:
        archivo = os.path.normpath(os.path.join(os.path.dirname(ruta), destino))
        if not os.path.isfile(archivo) or not re.search(
                r"^### %s\b" % re.escape(h), leer(archivo), re.M):
            salida.append((ruta, f"cita {h}, que no está en {destino}"))
    return salida


def _revisar_hu(ruta, analisis):
    texto = leer(ruta)
    partes = _CRITERIO.split(texto)
    salida = []
    for i in range(1, len(partes), 2):
        ca, cuerpo = partes[i], partes[i + 1]
        m = _SALE_DE.search(cuerpo)
        if not m:
            salida.append((ruta, f"el {ca} no tiene «Sale de»"))
            continue
        citas = _CITA.findall(m.group(1))
        if not citas:
            salida.append((ruta, f"el {ca} no cita un punto de «Lo que se tiene que hacer»"))
        for numero, puntos in citas:
            datos = analisis.get(int(numero))
            for p in (int(x) for x in re.findall(r"\d+", puntos)):
                if datos is None:
                    salida.append((ruta, f"el {ca} cita el análisis {numero}, que no existe"))
                    break
                if p not in datos["hacer"]:
                    salida.append((ruta, f"el {ca} cita el punto {p} del análisis {numero}, que no existe"))
    return salida


def revisar(raiz=None):
    """`[(ruta, mensaje)]`: un punto sin origen, o con un origen que no existe."""
    raiz = raiz or comun.RAIZ
    salida = []
    for epica, pendientes in sorted(epicas(raiz).items()):
        analisis = {}
        for carpeta in pendientes:
            for nombre in sorted(os.listdir(carpeta)):
                m = _ANALISIS.match(nombre)
                if not m:
                    continue
                ruta = os.path.join(carpeta, nombre)
                datos = leer_analisis(ruta)
                analisis[int(m.group(1))] = datos
                if datos["aprobado"]:
                    salida.extend(_revisar_analisis(ruta, datos))
            pendiente = os.path.join(carpeta, "pendiente.md")
            if os.path.isfile(pendiente):
                salida.extend(_revisar_pendiente(pendiente))
        for nombre in sorted(os.listdir(epica)):
            hu = os.path.join(epica, nombre, nombre + ".md")
            if nombre.startswith("HU-") and os.path.isfile(hu):
                salida.extend(_revisar_hu(hu, analisis))
    return salida


def validar(raiz=None):
    """Lo mismo que `revisar`, en la forma que reporta `validar.py`."""
    raiz = raiz or comun.RAIZ
    return [Hallazgo(FALLA, ruta, 0, f"{mensaje} (02·F27)") for ruta, mensaje in revisar(raiz)]


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("origen")
