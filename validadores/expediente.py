# -*- coding: utf-8 -*-
"""El mapa de completitud del expediente: qué entregables del ciclo tiene el proyecto.

**Para qué existe.** El ciclo de vida no hace excepciones: todos sus entregables
existen en todo proyecto, y el que no tenga materia lo declara con «No aplica
porque...». Hasta hoy, saber si un proyecto cumplía era abrir carpeta por
carpeta. Este lector responde de una: qué entregable existe, cuál falta, cuántos
espacios por llenar («...») le quedan a cada uno y cuál declaró no aplicar.

**Informa, no detiene.** Igual que `vigencia`: la lista se mira y las decisiones
las toma una persona. Un entregable «Falta» no bloquea nada por sí solo; la
puerta que sí detiene es la de cada regla (`02·F26` y las demás).

**Cómo encuentra cada entregable.** Por el nombre del archivo, en cualquier
carpeta del proyecto: `matematica-planteamiento.md`, `01-planteamiento.md` y
`planteamiento.md` cuentan igual. Es la misma convención del punto «cadena» de
la revisión de instalación. Las estaciones 03 a 11 (épicas, HU y documentos de
fase) no se buscan por nombre suelto: se cuentan por su estructura, que ya es
canónica (`documentacion/epicas/`).

Se corre con `validar.py expediente [--raiz <proyecto>]`.
"""
import io
import os
import re

import comun
from comun import AVISO, Hallazgo

MARCA = "«…»"          # «…» — el espacio por llenar (13·DOC19)
NO_APLICA = re.compile(r"no aplica", re.IGNORECASE)

# `plantillas/` va excluida a propósito: ahí viven los moldes, y un molde no es
# el entregable (se notó midiendo el propio estándar, que daba 13 de 13 por
# encontrar sus propios moldes).
EXCLUIDAS = {".git", ".venv", "node_modules", "__pycache__", "vendor",
             "staticfiles", ".claude", "plantillas", "terceros"}

# Cada entregable con las terminaciones de nombre que lo identifican.
# El orden es el del ciclo; el número es el del molde en
# plantillas/ciclo-vida-proyectos/.
ENTREGABLES = (
    ("01", "Planteamiento", ("planteamiento.md",)),
    ("02", "Inventario de funcionalidades", ("inventario-funcionalidades.md",)),
    ("12", "Estudio de factibilidad", ("estudio-factibilidad.md",
                                       "factibilidad.md")),
    ("13", "Acta de constitución y plan de proyecto",
     ("acta-de-constitucion-y-plan-de-proyecto.md", "acta-de-constitucion.md",
      "plan-de-proyecto.md")),
    ("14", "Modelo de datos", ("modelo-de-datos.md", "modelo-datos.md")),
    ("15", "Diseño de interfaz", ("diseno-de-interfaz.md",
                                  "diseño-de-interfaz.md")),
    ("16", "Documentación de API", ("documentacion-de-api.md",
                                    "documentacion-api.md")),
    ("17", "Manual de instalación", ("manual-de-instalacion.md",
                                     "manual-instalacion.md")),
    ("18", "Manual técnico y de operación",
     ("manual-tecnico-y-de-operacion.md", "manual-de-operacion.md",
      "manual-tecnico.md")),
    ("19", "Notas de versión", ("notas-de-version.md",)),
    ("20", "Acta de entrega", ("acta-de-entrega.md",)),
    ("21", "Bitácora de operación", ("bitacora-de-operacion.md",
                                     "bitacora.md")),
    ("22", "Plan de mantenimiento", ("plan-de-mantenimiento.md",)),
)


def _archivos_md(raiz):
    """Todos los `.md` del proyecto, saltando lo que no es del proyecto."""
    salida = []
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
        for nombre in archivos:
            if nombre.lower().endswith(".md"):
                salida.append(os.path.join(carpeta, nombre))
    return salida


def _leer(ruta):
    try:
        return io.open(ruta, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


def buscar(terminaciones, archivos):
    """Los archivos cuyo nombre termina en alguna de las terminaciones."""
    salida = []
    for ruta in archivos:
        nombre = os.path.basename(ruta).lower()
        for fin in terminaciones:
            if nombre == fin or nombre.endswith("-" + fin):
                salida.append(ruta)
                break
    return salida


def estado(texto):
    """`(estado, marcas)` de un entregable ya encontrado.

    `completo` (sin espacios por llenar), `en llenado` (con ellos), o
    `no aplica` (lo declara y no le quedan espacios). Declarar y dejar
    espacios a la vez es `en llenado`: la declaración exige su porqué escrito.
    """
    marcas = texto.count(MARCA)
    if marcas:
        return ("en llenado", marcas)
    if NO_APLICA.search(texto):
        return ("no aplica", 0)
    return ("completo", 0)


def _cadena_de_ejecucion(raiz):
    """Los conteos de las estaciones 03 a 11, por su estructura canónica."""
    epicas = hus = fases = 0
    base = os.path.join(raiz, "documentacion", "epicas")
    if os.path.isdir(base):
        for ep in sorted(os.listdir(base)):
            ruta_ep = os.path.join(base, ep)
            if not os.path.isdir(ruta_ep) or not ep.startswith("EP-"):
                continue
            if os.path.isfile(os.path.join(ruta_ep, "epica.md")):
                epicas += 1
            for hu in sorted(os.listdir(ruta_ep)):
                ruta_hu = os.path.join(ruta_ep, hu)
                if not os.path.isdir(ruta_hu) or not hu.startswith("HU-"):
                    continue
                hus += 1
                for fase in sorted(os.listdir(ruta_hu)):
                    if os.path.isfile(os.path.join(ruta_hu, fase,
                                                   "plan_trabajo.md")):
                        fases += 1
    return epicas, hus, fases


def reporte(raiz):
    """`(lineas, hallazgos)`: la tabla del expediente y un aviso por faltante."""
    archivos = _archivos_md(raiz)
    lineas = []
    hallazgos = []
    presentes = completos = 0

    lineas.append("| # | Entregable | Dónde está | Estado |")
    lineas.append("|---|---|---|---|")
    for numero, nombre, terminaciones in ENTREGABLES:
        encontrados = buscar(terminaciones, archivos)
        if not encontrados:
            lineas.append(f"| {numero} | {nombre} | (no hay) | **Falta** |")
            hallazgos.append(Hallazgo(
                AVISO, raiz, 0,
                f"el expediente no tiene «{nombre}» (molde {numero} del "
                f"ciclo); si no tiene materia, existe igual y declara "
                f"por qué no aplica"))
            continue
        presentes += 1
        ruta = encontrados[0]
        est, marcas = estado(_leer(ruta))
        rel = os.path.relpath(ruta, raiz).replace("\\", "/")
        extra = f" y otros {len(encontrados) - 1}" if len(encontrados) > 1 else ""
        detalle = {"completo": "Completo",
                   "no aplica": "Declara no aplicar",
                   "en llenado": f"En llenado ({marcas} espacios)"}[est]
        if est != "en llenado":
            completos += 1
        lineas.append(f"| {numero} | {nombre} | `{rel}`{extra} | {detalle} |")

    epicas, hus, fases = _cadena_de_ejecucion(raiz)
    lineas.append("")
    lineas.append(f"Estaciones 03 a 11 (la cadena de ejecución): "
                  f"{epicas} épica(s), {hus} HU, {fases} fase(s) con plan. "
                  f"El detalle lo dan `validar.py fases` y `trazabilidad`.")
    total = len(ENTREGABLES)
    lineas.append(f"Expediente: {presentes} de {total} entregables presentes; "
                  f"{completos} sin espacios por llenar.")
    return lineas, hallazgos


def validar(raiz):
    """Solo los hallazgos, para quien componga esto con otros validadores."""
    return reporte(raiz)[1]


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("expediente")
