"""`EP-023 · HU-002 · CA-01` · Cada punto dice de qué punto del anterior sale.

**Qué comprueba** (`02·F27`). En cada épica que nació de un análisis, sigue la
cadena de «Sale de» hacia arriba y detiene el punto que no cita su origen, o que
cita uno que no existe:

- el pendiente, frente al hallazgo que cita en «De dónde sale»;
- el punto de «Lo acordado», frente al turno de su conversación;
- la fila de «Lo que se tiene que hacer», frente al punto de «Lo acordado» que cita;
- el criterio de la HU, frente al punto de «Lo que se tiene que hacer»;
- la decisión del plan, frente al acuerdo que cita, o marcada como propuesta del
  agente (`EP-023 · HU-002 · CA-05`), en los planes aprobados desde 50.0.0.

**Lo que no mira, y se declara.** La tarea del plan frente a su criterio (la
mira `flujo`, por `02·F18`); las épicas que no nacieron de un análisis, que no
se reabren (`20·M10`); el análisis sin aprobar, que todavía se está llenando y
que «Apruebo el análisis» revisa con `revisar_uno()`; y si el origen citado es
el correcto, que es un juicio y se lee.
"""
import glob
import os
import re

from ..comun import FALLA, Archivos, Hallazgo, Markdown, Proyecto
from ..validadores.base import Validador
from .plan_vs_hecho import PlanDeTrabajo

ANALISIS = re.compile(r"^analisis-(\d+)\.md$")
APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
_TURNO = re.compile(r"^### (\d+) · Usuario", re.M)
_FILA = re.compile(r"^\| *(\d+) *\|(.*)\|\s*$", re.M)
_PUNTO = re.compile(r"^(\d+)\. (.*)$", re.M)
CRITERIO = re.compile(r"^### (CA-\d+)", re.M)
SALE_DE = re.compile(r"^\*\*Sale de:\*\*(.*)$", re.M)
CITA = re.compile(r"análisis (\d+), puntos? (\d+(?:(?:, | y )\d+)*)")
# `EP-023 · HU-002 · CA-05`: desde esta versión, cada decisión del plan dice de
# qué acuerdo sale o que es propuesta del agente. Lo aprobado antes no se reabre.
DESDE_DECISIONES = (50, 0, 0)
_DECISIONES = re.compile(r"(?ms)^###\s*2\.6[^\n]*\n(.*?)(?=^##)")
_PROPUESTA = re.compile(r"(?i)propuesta del agente")
_CITA_ACUERDO = re.compile(r"[Aa]nálisis (\d+)[^,;|]*?,\s*acuerdos? (\d+(?:(?:, | y )\d+)*)")
_CITA_REGLA = re.compile(r"\b(\d{2})·([A-Z]+\d+)\b")
_ENLACE_H = re.compile(r"\[[^\]]*?(H-\d+)[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)")

# Lo que no es del repositorio: local, generado o de terceros.
FUERA = {".git", ".venv", "venv", "__pycache__", "node_modules", "terceros"}


class LectorDeAnalisis:
    """Lo que se lee de un `analisis-N.md`: sus turnos, lo acordado y lo que se
    tiene que hacer. Lo usan el validador, los acuerdos y el freno."""

    @staticmethod
    def seccion(texto, titulo):
        """El texto de la sección `## <titulo>…` hasta la siguiente `## `."""
        m = re.search(r"^## %s.*$" % re.escape(titulo), texto, re.M)
        if not m:
            return ""
        fin = re.search(r"^## ", texto[m.end():], re.M)
        return texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]

    @staticmethod
    def filas(seccion):
        """`{número: [celdas]}` de las filas numeradas de una tabla."""
        return {int(n): [c.strip() for c in resto.split("|")] for n, resto in _FILA.findall(seccion)}

    @staticmethod
    def puntos(seccion):
        """`{número: texto}` de los puntos de una lista numerada."""
        return {int(n): resto for n, resto in _PUNTO.findall(seccion)}

    @classmethod
    def leer(cls, ruta, archivos=None):
        """Lo que el validador necesita de un análisis."""
        texto = (archivos or Archivos()).leer(ruta)
        return {
            "aprobado": bool(APROBADO.search(texto)),
            "turnos": {int(n) for n in _TURNO.findall(texto)},
            "acordado": cls.puntos(cls.seccion(texto, "Lo acordado")),
            "hacer": cls.filas(cls.seccion(texto, "Lo que se tiene que hacer")),
        }


class OrigenDeCadaPunto(Validador):
    """El punto que no dice de dónde sale, o que cita algo que no existe."""

    nombre = "origen"
    regla = "02·F27"
    descripcion = "cada punto de la cadena dice de qué punto del anterior sale"

    def validar(self):
        return [Hallazgo(FALLA, ruta, 0, "%s (02·F27)" % mensaje) for ruta, mensaje in self.revisar()]

    def _leer(self, ruta):
        return self.archivos.leer(ruta)

    def _analisis(self, ruta):
        return LectorDeAnalisis.leer(ruta, self.archivos)

    def epicas(self):
        """`{carpeta de la épica: [carpetas de pendiente con análisis]}`."""
        salida = {}
        for carpeta, subcarpetas, archivos in os.walk(self.proyecto.raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
            if any(ANALISIS.match(n) for n in archivos):
                salida.setdefault(self.epica_de(carpeta), []).append(carpeta)
        return salida

    @staticmethod
    def epica_de(carpeta):
        """La carpeta que contiene la del pendiente, saltando la carpeta `pendientes/`
        (`EP-023·HU-003·CA-08`): las HU que salen de él son hijas de esa épica."""
        arriba = os.path.dirname(carpeta)
        return os.path.dirname(arriba) if os.path.basename(arriba) == "pendientes" else arriba

    @staticmethod
    def regla_existe(capitulo, regla):
        """Si el estándar tiene la regla `NN·XXN` (análisis 14 del pendiente 103, acuerdo 11)."""
        return bool(glob.glob(os.path.join(Proyecto.estandar(), "base", capitulo + "-*", "reglas", regla + "-*.md")))

    @classmethod
    def revisar_analisis(cls, ruta, datos, del_pendiente=None):
        """`del_pendiente`: `{número: datos}` de los análisis del mismo pendiente.

        «Sale de lo acordado» es un número de este análisis, «Análisis N, acuerdo M»
        de otro del mismo pendiente (análisis 14 del pendiente 103, acuerdo 4), o una
        regla del estándar, como `13·DOC26` (acuerdo 11).
        """
        del_pendiente = del_pendiente or {}
        salida = []
        for n, texto in sorted(datos["acordado"].items()):
            m = re.search(r"\(([^()]*[Tt]urnos? [^()]*)\)\.?\s*$", texto)
            turnos = [int(x) for x in re.findall(r"\d+", m.group(1))] if m else []
            if not turnos:
                salida.append((ruta, f"el punto {n} de «Lo acordado» no dice de qué turno sale"))
            for t in turnos:
                if t not in datos["turnos"]:
                    salida.append((ruta, f"el punto {n} de «Lo acordado» cita el turno {t}, que no está en la conversación"))
        for n, celdas in sorted(datos["hacer"].items()):
            celda = celdas[1] if len(celdas) > 2 else ""
            de_otros = _CITA_ACUERDO.findall(celda)
            reglas = _CITA_REGLA.findall(celda)
            citas = [int(x) for x in re.findall(r"\d+", _CITA_REGLA.sub("", _CITA_ACUERDO.sub("", celda)))]
            if not citas and not de_otros and not reglas:
                salida.append((ruta, f"el punto {n} de «Lo que se tiene que hacer» no dice de qué punto de «Lo acordado» sale"))
            for c in citas:
                if c not in datos["acordado"]:
                    salida.append((ruta, f"el punto {n} de «Lo que se tiene que hacer» cita el punto {c} de «Lo acordado», que no existe"))
            for numero, acuerdos in de_otros:
                otro = del_pendiente.get(int(numero))
                for a in (int(x) for x in re.findall(r"\d+", acuerdos)):
                    if otro is None or a not in otro["acordado"]:
                        salida.append((ruta, f"el punto {n} de «Lo que se tiene que hacer» cita el acuerdo {a} "
                                             f"del análisis {numero}, que no existe"))
            for capitulo, regla in reglas:
                if not cls.regla_existe(capitulo, regla):
                    salida.append((ruta, f"el punto {n} de «Lo que se tiene que hacer» cita la regla "
                                         f"{capitulo}·{regla}, que no existe"))
        return salida

    @staticmethod
    def del_pendiente(carpeta, archivos=None):
        """`{número: datos}` de los análisis de la carpeta de un pendiente."""
        salida = {}
        for nombre in sorted(os.listdir(carpeta)):
            m = ANALISIS.match(nombre)
            if m:
                salida[int(m.group(1))] = LectorDeAnalisis.leer(os.path.join(carpeta, nombre), archivos)
        return salida

    @classmethod
    def revisar_uno(cls, ruta, archivos=None):
        """Las fallas de origen de un análisis, aprobado o no: lo usa «Apruebo el análisis»."""
        return [mensaje for _, mensaje in cls.revisar_analisis(
            ruta, LectorDeAnalisis.leer(ruta, archivos), cls.del_pendiente(os.path.dirname(ruta), archivos))]

    def revisar_pendiente(self, ruta):
        fila = re.search(r"^\|[^|\n]*De dónde sale[^|\n]*\|(.*)\|\s*$", self._leer(ruta), re.M)
        if not fila:
            return [(ruta, "el pendiente no tiene «De dónde sale»")]
        citas = _ENLACE_H.findall(fila.group(1))
        if not citas:
            # El reporte de un proyecto que enlaza su pendiente de seguimiento ya
            # dice de dónde sale (análisis 1 del pendiente 110, acuerdo 5).
            if re.search(r"\]\(([^)]*/)?pendiente\.md\)", fila.group(1)):
                return []
            return [(ruta, "«De dónde sale» no enlaza ningún hallazgo")]
        salida = []
        for h, destino in citas:
            archivo = os.path.normpath(os.path.join(os.path.dirname(ruta), destino))
            if not os.path.isfile(archivo) or not re.search(
                    r"^### %s\b" % re.escape(h), self._leer(archivo), re.M):
                salida.append((ruta, f"cita {h}, que no está en {destino}"))
        return salida

    def revisar_hu(self, ruta, analisis):
        partes = CRITERIO.split(self._leer(ruta))
        salida = []
        for i in range(1, len(partes), 2):
            ca, cuerpo = partes[i], partes[i + 1]
            m = SALE_DE.search(cuerpo)
            if not m:
                salida.append((ruta, f"el {ca} no tiene «Sale de»"))
                continue
            citas = CITA.findall(m.group(1))
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

    def revisar_plan(self, ruta, analisis):
        """`CA-05` · la decisión del plan que no cita un acuerdo que existe ni es propuesta del agente."""
        texto = self._leer(ruta)
        if not PlanDeTrabajo.aprobado(ruta, texto, DESDE_DECISIONES):
            return []
        m = _DECISIONES.search(texto)
        filas = Markdown.filas_de(m.group(1), "Decisión", "Sale de") if m else []
        if m and not filas and Markdown.filas_de(m.group(1), "Decisión"):
            return [(ruta, "la tabla 2.6 no tiene la columna «Sale de»")]
        salida = []
        for _, fila in filas:
            decision, sale = fila.get("decisión", ""), fila.get("sale de", "")
            if not decision.strip():
                continue
            corta = decision.strip()[:60]
            if _PROPUESTA.search(sale):
                continue
            citas = _CITA_ACUERDO.findall(sale)
            if not citas:
                salida.append((ruta, f"la decisión «{corta}» no dice de qué acuerdo sale ni que es propuesta del agente"))
            for numero, acuerdos in citas:
                datos = analisis.get(int(numero))
                for a in (int(x) for x in re.findall(r"\d+", acuerdos)):
                    if datos is None or a not in datos["acordado"]:
                        salida.append((ruta, f"la decisión «{corta}» cita el acuerdo {a} del análisis {numero}, que no existe"))
        return salida

    def revisar(self):
        """`[(ruta, mensaje)]`: un punto sin origen, o con un origen que no existe."""
        salida = []
        for epica, pendientes in sorted(self.epicas().items()):
            analisis = {}
            for carpeta in pendientes:
                del_pendiente = self.del_pendiente(carpeta, self.archivos)
                for numero, datos in sorted(del_pendiente.items()):
                    analisis[numero] = datos
                    if datos["aprobado"]:
                        ruta = os.path.join(carpeta, "analisis-%d.md" % numero)
                        salida.extend(self.revisar_analisis(ruta, datos, del_pendiente))
                pendiente = os.path.join(carpeta, "pendiente.md")
                if os.path.isfile(pendiente):
                    salida.extend(self.revisar_pendiente(pendiente))
            for nombre in sorted(os.listdir(epica)):
                hu = os.path.join(epica, nombre, nombre + ".md")
                if nombre.startswith("HU-") and os.path.isfile(hu):
                    salida.extend(self.revisar_hu(hu, analisis))
                    for fase in sorted(os.listdir(os.path.join(epica, nombre))):
                        plan = os.path.join(epica, nombre, fase, "plan_trabajo.md")
                        if os.path.isfile(plan):
                            salida.extend(self.revisar_plan(plan, analisis))
        return salida
