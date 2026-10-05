"""El mapa de completitud del expediente: qué entregables del ciclo tiene el proyecto.

El ciclo de vida no hace excepciones: todos sus entregables existen, y el que no
tenga materia lo declara con «No aplica porque...». Esto responde de una qué
entregable existe, cuál falta, cuántos espacios por llenar le quedan y cuál
declaró no aplicar.

**Informa, no detiene.** Un entregable que falta es aviso: la puerta que detiene
es la de cada regla (`02·F26` y las demás).

**Cómo encuentra cada uno**: por el nombre del archivo, en cualquier carpeta;
`matematica-planteamiento.md` y `planteamiento.md` cuentan igual. Las estaciones
03 a 11 se cuentan por su estructura canónica (`documentacion/epicas/`).
"""
import io
import os
import re

from ..comun import AVISO, Hallazgo
from .base import Validador

MARCA = "«…»"          # el espacio por llenar (13·DOC19)
NO_APLICA = re.compile(r"no aplica", re.IGNORECASE)

# `plantillas/` va excluida a propósito: ahí viven los moldes, y un molde no es
# el entregable (el propio estándar daba 13 de 13 por encontrar sus moldes).
EXCLUIDAS = {".git", ".venv", "node_modules", "__pycache__", "vendor",
             "staticfiles", ".claude", "plantillas", "terceros"}

# Cada entregable con las terminaciones de nombre que lo identifican, en el
# orden del ciclo y con el número de su molde.
ENTREGABLES = (
    ("01", "Planteamiento", ("planteamiento.md",)),
    ("02", "Inventario de funcionalidades", ("inventario-funcionalidades.md",)),
    ("12", "Estudio de factibilidad", ("estudio-factibilidad.md", "factibilidad.md")),
    ("13", "Acta de constitución y plan de proyecto",
     ("acta-de-constitucion-y-plan-de-proyecto.md", "acta-de-constitucion.md", "plan-de-proyecto.md")),
    ("14", "Modelo de datos", ("modelo-de-datos.md", "modelo-datos.md")),
    ("15", "Diseño de interfaz", ("diseno-de-interfaz.md", "diseño-de-interfaz.md")),
    # `contrato-de-la-interfaz.md` es el mismo entregable con el nombre que el
    # estándar le da en su tabla de moldes: sin él daba «falta» sobre un documento escrito.
    ("16", "Documentación de API", ("documentacion-de-api.md", "documentacion-api.md",
                                    "contrato-de-la-interfaz.md")),
    ("17", "Manual de instalación", ("manual-de-instalacion.md", "manual-instalacion.md")),
    ("18", "Manual técnico y de operación",
     ("manual-tecnico-y-de-operacion.md", "manual-de-operacion.md", "manual-tecnico.md")),
    ("19", "Notas de versión", ("notas-de-version.md",)),
    ("20", "Acta de entrega", ("acta-de-entrega.md",)),
    ("21", "Bitácora de operación", ("bitacora-de-operacion.md", "bitacora.md")),
    ("22", "Plan de mantenimiento", ("plan-de-mantenimiento.md",)),
)

_DETALLE = {"completo": "Completo", "no aplica": "Declara no aplicar"}


def _leer(ruta):
    """El texto, o `""`. No anota el archivo: acá solo se cuentan espacios."""
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


class Expediente(Validador):
    """Un aviso por entregable que falta; el detalle va en `reporte()`."""

    nombre = "expediente"
    regla = ""
    descripcion = "qué entregables del ciclo tiene el proyecto: informa, no detiene"

    def archivos_md(self):
        """Todos los `.md` del proyecto, saltando lo que no es del proyecto.
        El orden es el del disco: el primero que aparece es el que se nombra."""
        raiz = self.proyecto.raiz
        salida = []
        for carpeta, subcarpetas, archivos in os.walk(raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
            if self.proyecto.es_excluida(os.path.relpath(carpeta, raiz).replace(os.sep, "/")):
                subcarpetas[:] = []
                continue
            salida += [os.path.join(carpeta, n) for n in archivos if n.lower().endswith(".md")]
        return salida

    @staticmethod
    def buscar(terminaciones, archivos):
        """Los archivos cuyo nombre es alguna terminación o acaba en `-terminación`."""
        return [ruta for ruta in archivos
                if any(os.path.basename(ruta).lower() == fin or os.path.basename(ruta).lower().endswith("-" + fin)
                       for fin in terminaciones)]

    @staticmethod
    def estado(texto):
        """`(estado, marcas)`: `completo`, `en llenado` o `no aplica`.

        Declarar y dejar espacios a la vez es `en llenado`: la declaración exige
        su porqué escrito.
        """
        marcas = texto.count(MARCA)
        if marcas:
            return ("en llenado", marcas)
        if NO_APLICA.search(texto):
            return ("no aplica", 0)
        return ("completo", 0)

    def cadena_de_ejecucion(self):
        """`(épicas, HU, fases con plan)`: las estaciones 03 a 11, por su estructura."""
        epicas = hus = fases = 0
        base = os.path.join(self.proyecto.raiz, "documentacion", "epicas")
        if not os.path.isdir(base):
            return epicas, hus, fases
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
                fases += sum(1 for fase in os.listdir(ruta_hu)
                             if os.path.isfile(os.path.join(ruta_hu, fase, "plan_trabajo.md")))
        return epicas, hus, fases

    def reporte(self):
        """`(lineas, hallazgos)`: la tabla del expediente y un aviso por faltante."""
        raiz = self.proyecto.raiz
        archivos = self.archivos_md()
        lineas = ["| # | Entregable | Dónde está | Estado |", "|---|---|---|---|"]
        hallazgos = []
        presentes = completos = 0
        for numero, nombre, terminaciones in ENTREGABLES:
            encontrados = self.buscar(terminaciones, archivos)
            if not encontrados:
                lineas.append("| %s | %s | (no hay) | **Falta** |" % (numero, nombre))
                hallazgos.append(Hallazgo(AVISO, raiz, 0, "el expediente no tiene «%s» (molde %s del ciclo); si no "
                                                          "tiene materia, existe igual y declara por qué no aplica"
                                          % (nombre, numero)))
                continue
            presentes += 1
            est, marcas = self.estado(_leer(encontrados[0]))
            rel = os.path.relpath(encontrados[0], raiz).replace("\\", "/")
            extra = " y otros %d" % (len(encontrados) - 1) if len(encontrados) > 1 else ""
            detalle = _DETALLE.get(est) or "En llenado (%d espacios)" % marcas
            if est != "en llenado":
                completos += 1
            lineas.append("| %s | %s | `%s`%s | %s |" % (numero, nombre, rel, extra, detalle))
        epicas, hus, fases = self.cadena_de_ejecucion()
        lineas += ["",
                   "Estaciones 03 a 11 (la cadena de ejecución): %d épica(s), %d HU, %d fase(s) con plan. "
                   "El detalle lo dan `validar.py fases` y `trazabilidad`." % (epicas, hus, fases),
                   "Expediente: %d de %d entregables presentes; %d sin espacios por llenar."
                   % (presentes, len(ENTREGABLES), completos)]
        return lineas, hallazgos

    def validar(self):
        return self.reporte()[1]
