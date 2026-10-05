"""Un documento contra la plantilla de la que salió.

La plantilla es la fuente de verdad: **nada se codifica acá**. Se abre
`plantillas/X.md` del estándar, se ve qué secciones y qué marcadores tiene, y se
compara. Si la plantilla cambia, la comprobación cambia con ella.

Cinco comprobaciones:
  1. Líneas sin llenar      — FALLA. Quedó texto literal de la plantilla.
  2. Notas de la plantilla  — AVISO. Las instrucciones `>` no se borraron.
  3. Secciones ausentes     — AVISO. Las plantillas permiten borrar lo que no
                              aplica, así que no se puede afirmar que falte.
  4. Reglas sin origen      — FALLA, solo en la especificación de módulo.
  5. El bloque fijo perdido — FALLA. El texto que la plantilla pone antes de su
                              primer separador es instrucción de uso, no relleno.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Markdown, Proyecto
from .base import Validador

# El prefijo del identificador en el H1 basta: «HU-014 — Registrar cliente».
POR_PREFIJO = {
    "HU-": "plantillas/ciclo-vida-proyectos/04-HU.md",
    "EP-": "plantillas/ciclo-vida-proyectos/03-epica.md",
    "ADR-": "plantillas/ADR.md",
}

# Cuando el identificador no dice nada, se deduce por el nombre del archivo.
POR_NOMBRE = {
    "planteamiento": "plantillas/ciclo-vida-proyectos/01-planteamiento.md",
    "dominio": "plantillas/dominio.md",
    "stack": "plantillas/stack.md",
    "fase": "plantillas/ciclo-vida-proyectos/05-fase.md",
    "trabajo": "plantillas/ciclo-vida-proyectos/07-plan-trabajo.md",
    "pruebas": "plantillas/ciclo-vida-proyectos/08-plan-pruebas.md",
    "marco-normativo": "plantillas/marco-normativo.md",
    "mapeo-nombres": "plantillas/mapeo-nombres.md",
    "analisis": "plantillas/analisis.md",
    "cierre-analisis": "plantillas/cierre-analisis.md",
    "recomendaciones-del-analisis": "plantillas/recomendaciones-del-analisis.md",
    "estado-fase": "plantillas/ciclo-vida-proyectos/10-estado-fase.md",
    "plan_trabajo": "plantillas/ciclo-vida-proyectos/07-plan-trabajo.md",
    "plan_pruebas": "plantillas/ciclo-vida-proyectos/08-plan-pruebas.md",
    "funcionalidad_implementada": "plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md",
    "catalogo-modulos": "plantillas/catalogo-modulos.md",
    "modulos": "plantillas/catalogo-modulos.md",
    "reglas-proyecto": "plantillas/reglas-proyecto.md",
    "mapa-dependencias": "plantillas/mapa-dependencias.md",
    "adr": "plantillas/ADR.md",
    "spec": "plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md",
}

SPEC_MODULO = "plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md"

_SECCION_REGLAS = re.compile(r"^##\s+\d*\.?\s*Reglas de negocio\s*$(.*?)(?=^##\s|\Z)", re.M | re.S | re.I)
_REGLA = re.compile(r"^\s*\d+\.\s+(.*\S)\s*$", re.M)
# Un identificador de origen: `RF-13`, `HU-001`, `D-22`, `RN-05`, `CA-01`…
_IDENTIFICADOR = re.compile(r"\b[A-ZÁÉÍÓÚÑ]{1,6}-\d+\b")
_H1 = re.compile(r"^#\s+(.*?)\s*$")
_MARCADOR_EN_TITULO = re.compile(r"\[[^\[\]\n]+\](?!\()")
# Una fecha en el bloque fijo delata que ahí se contó de dónde salió el documento.
_FECHA = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
# Donde termina la cabecera: el primer separador, o el primer `##` si no hay.
_FIN_DE_CABECERA = re.compile(r"^(?:-{3,}\s*|##\s+.*)$")


def _recorte(texto, largo=60):
    return texto if len(texto) <= largo else texto[:largo - 3] + "..."


class DocumentoContraPlantilla(Validador):
    """Necesita el documento; la plantilla se deduce si no se da."""

    nombre = "plantilla"
    regla = "13·DOC15"
    descripcion = "un documento contra la plantilla de la que salió"

    def __init__(self, proyecto, documento, plantilla=None, archivos=None):
        super().__init__(proyecto, archivos)
        self.documento = documento
        self.plantilla = plantilla

    @staticmethod
    def ruta_en_el_estandar(relativa):
        return os.path.normpath(os.path.join(Proyecto.estandar() or "", *relativa.split("/")))

    @classmethod
    def deducir(cls, ruta_documento, texto):
        """La ruta de la plantilla que le corresponde, o `None` si no se sabe."""
        for _, linea in Markdown.lineas_utiles(texto):
            m = _H1.match(linea)
            if m:
                titulo = m.group(1).strip().upper()
                for prefijo, plantilla in POR_PREFIJO.items():
                    if titulo.startswith(prefijo):
                        return cls.ruta_en_el_estandar(plantilla)
                break
        base = os.path.splitext(os.path.basename(ruta_documento))[0].lower()
        if base in POR_NOMBRE:
            return cls.ruta_en_el_estandar(POR_NOMBRE[base])
        # `prompts/<slug>-planteamiento.md`. Se exige la carpeta: el sufijo
        # suelto tomaba por planteamiento un pendiente que se llama
        # `el-estandar-tiene-su-planteamiento.md`.
        carpeta = os.path.basename(os.path.dirname(os.path.abspath(ruta_documento)))
        if carpeta.lower() == "prompts" and base.endswith("-planteamiento"):
            return cls.ruta_en_el_estandar(POR_NOMBRE["planteamiento"])
        return None

    @staticmethod
    def notas(texto):
        """Las líneas `>`: en las plantillas son instrucciones para quien llena."""
        return [(n, l.strip()) for n, l in Markdown.lineas_utiles(texto) if l.strip().startswith(">")]

    @staticmethod
    def reglas_sin_origen(texto, plantilla_texto=""):
        """`[(línea, regla)]` del §4 que no dicen de dónde bajan.

        Se busca un identificador (`RF-13`, `HU-001`, `D-22`) y no una frase:
        «lo pidió el cliente» no se puede seguir hasta ninguna parte. Lo que
        sigue igual que en la plantilla no cuenta: eso ya lo reporta la
        comprobación de líneas sin llenar.
        """
        seccion = _SECCION_REGLAS.search(texto)
        if not seccion:
            return []
        del_molde = {m.group(1).strip() for s in _SECCION_REGLAS.finditer(plantilla_texto or "")
                     for m in _REGLA.finditer(s.group(1))}
        salida = []
        for m in _REGLA.finditer(seccion.group(1)):
            regla = m.group(1).strip()
            if regla in del_molde or not regla.strip("«»…. ") or _IDENTIFICADOR.search(regla):
                continue
            salida.append((texto[:seccion.start(1) + m.start(1)].count("\n") + 1, regla))
        return salida

    @staticmethod
    def bloque_fijo(texto):
        """`[(línea, texto)]` de lo que la plantilla pone antes de su primer separador.

        No es el recuadro `>` que se borra: es la prosa de debajo, que dice cómo
        se usa el documento ya llenado. Se identifica por posición y no por su
        etiqueta, porque la etiqueta cambia.
        """
        salida = []
        for n, linea in Markdown.lineas_utiles(texto):
            recortada = linea.strip()
            if not recortada:
                continue
            if _FIN_DE_CABECERA.match(recortada):
                break
            if not recortada.startswith(("#", ">", "|")):
                salida.append((n, recortada))
        return salida

    def validar(self):
        documento = self.archivos.leer(self.documento)
        plantilla_ruta = self.plantilla or self.deducir(self.documento, documento)
        if not plantilla_ruta:
            return []
        plantilla = self.archivos.leer(plantilla_ruta)
        return (self._sin_llenar(documento, plantilla) + self._notas_sin_borrar(documento, plantilla)
                + self._secciones_ausentes(documento, plantilla)
                + self._reglas_sin_origen(documento, plantilla, plantilla_ruta)
                + self._bloque_fijo_perdido(documento, plantilla))

    def _sin_llenar(self, documento, plantilla):
        """Se compara la línea entera y no el marcador suelto: `[Backend]` en una
        tarea ya llena es una etiqueta, no un hueco."""
        del_molde = {l.strip() for _, l in Markdown.lineas_utiles(plantilla) if l.strip()}
        con_marcador = {n for n, _ in Markdown.marcadores(documento)}
        return [Hallazgo(FALLA, self.documento, n, "línea sin llenar, igual que en la plantilla: %s"
                         % _recorte(linea.strip()))
                for n, linea in Markdown.lineas_utiles(documento)
                if n in con_marcador and linea.strip() in del_molde]

    def _notas_sin_borrar(self, documento, plantilla):
        del_molde = {t for _, t in self.notas(plantilla)}
        return [Hallazgo(AVISO, self.documento, n, "nota de la plantilla sin borrar: %s" % _recorte(t))
                for n, t in self.notas(documento) if t in del_molde]

    def _secciones_ausentes(self, documento, plantilla):
        """AVISO: las plantillas dicen «elimine las secciones que no apliquen».
        Los títulos con un marcador adentro son ejemplos y no se comparan."""
        presentes = {t for _, t in Markdown.encabezados(documento)}
        return [Hallazgo(AVISO, self.documento, 0, "sección de la plantilla ausente: «%s» "
                                                   "— confirma que no aplica" % titulo)
                for _, titulo in Markdown.encabezados(plantilla)
                if not _MARCADOR_EN_TITULO.search(titulo) and titulo not in presentes]

    def _reglas_sin_origen(self, documento, plantilla, plantilla_ruta):
        """Solo en la especificación de módulo: se ata a la plantilla, no al título."""
        if os.path.normpath(plantilla_ruta) != self.ruta_en_el_estandar(SPEC_MODULO):
            return []
        return [Hallazgo(FALLA, self.documento, linea,
                         "regla de negocio sin decir de dónde baja: %s — falta el identificador del "
                         "requisito, la historia o la decisión; si no lo tiene, la regla se sube a la "
                         "historia que corresponda y baja desde allá" % _recorte(regla))
                for linea, regla in self.reglas_sin_origen(documento, plantilla)]

    def _bloque_fijo_perdido(self, documento, plantilla):
        """Lo que se exige sale de la plantilla: si no tiene bloque fijo, no se pide ninguno."""
        fijo_plantilla = self.bloque_fijo(plantilla)
        if not fijo_plantilla:
            return []
        fijo_documento = self.bloque_fijo(documento)
        muestra = _recorte(fijo_plantilla[0][1])
        if not fijo_documento:
            return [Hallazgo(FALLA, self.documento, 0,
                             "falta el texto que la plantilla fija antes de su primer separador: «%s» — "
                             "no es relleno, es la instrucción de uso del documento, y se conserva al "
                             "llenarlo" % muestra)]
        if (any(_FECHA.search(t) for _, t in fijo_documento)
                and not any(_FECHA.search(t) for _, t in fijo_plantilla)):
            return [Hallazgo(FALLA, self.documento, fijo_documento[0][0],
                             "el texto fijo trae una fecha, y el de la plantilla no: ahí se está contando "
                             "de dónde salió el documento en vez de cómo se usa — la procedencia va en la "
                             "identificación, y ese lugar lo ocupa lo que la plantilla pone: «%s»" % muestra)]
        return []
