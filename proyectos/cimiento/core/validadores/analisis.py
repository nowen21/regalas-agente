"""`EP-023 · HU-001` · Lo que un análisis aprobado tiene que traer.

**Qué comprueba.**

- Todo `analisis-N.md` aprobado lleva una sección por cada parte que no habla en
  la conversación: Cimiento, el proyecto, lo aprendido y el entorno (CA-06).
- El aprobado desde la 44.0.0, además (CA-22): «Recomendaciones» con las que
  consultó (CA-19), «Dónde más puede pasar» con lo que cubre cada caso (CA-17),
  y la tabla de HU sin una HU antes de otra de la que depende ni un puesto sin
  razón (CA-18).
- Las recomendaciones de Cimiento y las del proyecto: cada una con su origen y
  sin dos que digan lo mismo (CA-19).
- Lo que suma cada análisis aprobado está, letra por letra, en el análisis
  principal de su alcance (CA-24).
- Aviso: el análisis aprobado que no aparece en la «Lista de análisis» del
  principal (CA-20). Revisa todos, sin puerta de versión (análisis 9).

**Lo que no mira, y se declara.** El análisis abierto, que todavía se está
llenando; lo nuevo de la 44.0.0 en uno aprobado antes, que no se reabre
(`20·M10`) y que sin versión en la marca se lee como anterior; el análisis con la
forma vieja de `analisis/`, al que solo se le pide estar en la lista del
principal; y si lo escrito en cada sección es acertado, que es un juicio.
"""
import os
import re
import sqlite3

from ..comun import AVISO, FALLA, Hallazgo, Proyecto
from ..enganches.analisis_en_curso import AnalisisEnCurso
from .base import Validador

# Las cuatro partes, por el comienzo del título de su sección.
PARTES = ("Cimiento", "El proyecto", "Lo aprendido", "El entorno")

# Desde esta versión se exigen las secciones nuevas (CA-22).
DESDE = (44, 0, 0)

# `EP-023·HU-006` · Desde esta versión cada lección enlaza su señal y dice qué
# recomendación alimenta.
DESDE_LECCIONES = (46, 0, 0)

RECOMENDACIONES = ("plantillas/recomendaciones-del-analisis.md", "analisis/recomendaciones.md")

_ARCHIVO = re.compile(r"^analisis-\d+\.md$")
_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
_VERSION = re.compile(r"^> \*\*Aprobado\*\* .*?con la versión (\d+)\.(\d+)\.(\d+)", re.M)
_RECOMENDACION = re.compile(r"^\| *(R-\d+|RP-\d+) *\|(.*)\|\s*$", re.M)
_CITA_R = re.compile(r"\bR-\d+|\bRP-\d+")
_HU_NUM = re.compile(r"\d+")
_SENAL_CITADA = re.compile(r"\bS-\d+\b")
_RECOMENDACION_CITADA = re.compile(r"\b(?:complementa|nueva)\s+(R-\d+|RP-\d+)", re.I)

# Lo que no es del repositorio: local, generado o de terceros.
FUERA = {".git", ".venv", "venv", "__pycache__", "node_modules", "terceros"}

# Lo que vive en `analisis/` y no es un análisis.
NO_SON = {"readme.md", "recomendaciones.md"}


def _celdas(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


class AnalisisAprobados(Validador):
    """Las partes que un análisis aprobado trae, y su paso al análisis principal."""

    nombre = "analisis"
    regla = "13·DOC24"
    descripcion = "las cuatro partes de cada análisis aprobado"

    def __init__(self, proyecto, archivos=None):
        super().__init__(proyecto, archivos)
        self.curso = AnalisisEnCurso(self.proyecto.raiz)

    def _leer(self, ruta):
        return self.archivos.leer(ruta)

    @staticmethod
    def _mostrar(ruta):
        return Proyecto(Proyecto.estandar()).mostrar(ruta)

    # ── qué se revisa ─────────────────────────────────────────────────────

    def analisis(self):
        """Las rutas de todos los `analisis-N.md` del repositorio."""
        salida = []
        for carpeta, subcarpetas, archivos in os.walk(self.proyecto.raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
            for nombre in archivos:
                if _ARCHIVO.match(nombre):
                    salida.append(os.path.join(carpeta, nombre))
        return sorted(salida)

    def de_forma_anterior(self):
        """Los análisis con la forma vieja: lo que vive junto a un análisis principal
        y no es él. Solo cuenta la carpeta `analisis/` que tiene su principal: otra
        con ese nombre, como `prompts/analisis/`, guarda otra cosa."""
        salida = []
        for carpeta, subcarpetas, archivos in os.walk(self.proyecto.raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
            if os.path.basename(carpeta) != "analisis" or not any("analisis-principal" in n for n in archivos):
                continue
            for nombre in archivos:
                if nombre.endswith(".md") and nombre.lower() not in NO_SON and "analisis-principal" not in nombre:
                    salida.append(os.path.join(carpeta, nombre))
        return sorted(salida)

    # ── el texto de un análisis ───────────────────────────────────────────

    @staticmethod
    def faltantes(texto):
        """Las partes que no tienen su sección `### ` en el análisis."""
        return [p for p in PARTES if not re.search(r"^### %s\b" % re.escape(p), texto, re.M)]

    @staticmethod
    def version_de(texto):
        m = _VERSION.search(texto)
        return tuple(int(x) for x in m.groups()) if m else None

    @classmethod
    def exige_lo_nuevo(cls, texto):
        """Si el análisis se aprobó desde la versión que trae las secciones nuevas."""
        version = cls.version_de(texto)
        return bool(version) and version >= DESDE

    @staticmethod
    def tabla(parte, *columnas):
        """`[{columna: celda}]` de la primera tabla de `parte` cuyo encabezado trae `columnas`."""
        lineas = parte.split("\n")
        for i, linea in enumerate(lineas):
            if linea.startswith("|") and all(c in linea for c in columnas):
                cabeza = _celdas(linea)
                filas = []
                for fila in lineas[i + 2:]:
                    if not fila.startswith("|"):
                        break
                    filas.append(dict(zip(cabeza, _celdas(fila))))
                return filas
        return None

    @staticmethod
    def subseccion(texto, titulo):
        """El texto de `### <titulo>` hasta el siguiente título de nivel 2 o 3."""
        m = re.search(r"^#{2,3} %s.*$" % re.escape(titulo), texto, re.M)
        if not m:
            return None
        fin = re.search(r"^#{2,3} ", texto[m.end():], re.M)
        return texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]

    @classmethod
    def lo_nuevo(cls, texto):
        """Lo que le falta a un análisis aprobado desde la 44.0.0 (CA-17, CA-18 y CA-19)."""
        salida = []
        if not _CITA_R.search(AnalisisEnCurso.seccion(texto, "Recomendaciones")):
            salida.append("no dice qué recomendaciones consultó")
        casos = cls.subseccion(texto, "Dónde más puede pasar")
        if casos is None:
            salida.append("falta la sección «Dónde más puede pasar»")
        else:
            for fila in cls.tabla(casos, "Caso", "Lo cubre") or []:
                if not fila.get("Lo cubre"):
                    salida.append("el caso «%s» de «Dónde más puede pasar» no dice qué lo cubre" % fila.get("Caso", ""))
        filas = cls.tabla(AnalisisEnCurso.seccion(texto, "Propuesta final"), "Orden", "Depende de") or []
        puesto = {}
        for fila in filas:
            hu, orden = _HU_NUM.findall(fila.get("HU", "")), _HU_NUM.findall(fila.get("Orden", ""))
            if hu and orden:
                puesto[int(hu[0])] = int(orden[0])
        for fila in filas:
            hu = _HU_NUM.findall(fila.get("HU", ""))
            if not hu:
                continue
            hu = int(hu[0])
            if not fila.get("Por qué en ese orden"):
                salida.append("la HU %d no dice por qué va en su puesto" % hu)
            for dep in (int(x) for x in _HU_NUM.findall(fila.get("Depende de", ""))):
                if dep in puesto and puesto[dep] > puesto[hu]:
                    salida.append("la HU %d va antes de la HU %d, de la que depende" % (hu, dep))
        return salida

    # ── las lecciones y las recomendaciones ───────────────────────────────

    @staticmethod
    def base_de_senales():
        return os.environ.get("MEMORIA_DB") or os.path.join(Proyecto.estandar(), "memoria", "senales.db")

    @classmethod
    def tipos_de_senal(cls):
        """`{S-NNN: tipo}` de la base de señales, que es la única fuente (análisis 10
        del pendiente 103, acuerdo 7). Sin base en esta máquina, `None`: no hay con
        qué comparar, y la lección no se da por mala."""
        ruta = cls.base_de_senales()
        if not os.path.isfile(ruta):
            return None
        try:
            con = sqlite3.connect(ruta)
            try:
                return dict(con.execute("SELECT id, tipo FROM senales"))
            finally:
                con.close()
        except sqlite3.Error:
            return None

    def recomendaciones_existentes(self):
        numeros = set()
        for relativa in RECOMENDACIONES:
            numeros |= {n for n, _ in _RECOMENDACION.findall(self._leer(self.proyecto.ruta(relativa)))}
        return numeros

    def lecciones(self, texto):
        """`CA-01` y `CA-02` de la HU-006 · lo que le falta a la tabla de lecciones."""
        salida = []
        filas = self.tabla(AnalisisEnCurso.seccion(texto, "Lecciones aprendidas"), "Lección", "Señal") or []
        senales = self.tipos_de_senal()
        existentes = self.recomendaciones_existentes()
        for fila in filas:
            numero = fila.get("#", "")
            citadas = _SENAL_CITADA.findall(fila.get("Señal", ""))
            if not citadas or (senales is not None and any(senales.get(s) != "leccion" for s in citadas)):
                salida.append("la lección %s no enlaza una señal de tipo `leccion`" % numero)
            recomendacion = fila.get("Recomendación", "")
            if not recomendacion:
                salida.append("la lección %s no dice qué recomendación alimenta" % numero)
                continue
            for r in _RECOMENDACION_CITADA.findall(recomendacion):
                if r not in existentes:
                    salida.append("la lección %s nombra la %s, que no existe" % (numero, r))
        return salida

    def recomendaciones(self):
        """`[(ruta, mensaje)]`: una recomendación sin origen o dos que dicen lo mismo (CA-19)."""
        salida = []
        for relativa in RECOMENDACIONES:
            ruta = self.proyecto.ruta(relativa)
            if not os.path.isfile(ruta):
                continue
            vistas = {}
            for numero, resto in _RECOMENDACION.findall(self._leer(ruta)):
                celdas = _celdas(resto)
                que = celdas[0] if celdas else ""
                if not re.search(r"[Aa]nálisis \d+", celdas[-1] if celdas else ""):
                    salida.append((ruta, f"la {numero} no dice de qué análisis sale"))
                clave = re.sub(r"[^a-záéíóúñü0-9 ]", "", que.lower()).strip()
                if clave in vistas:
                    salida.append((ruta, f"la {numero} dice lo mismo que la {vistas[clave]}"))
                vistas.setdefault(clave, numero)
        return salida

    # ── el paso al análisis principal ─────────────────────────────────────

    def _aprobados_y_viejos(self):
        for ruta in self.analisis() + self.de_forma_anterior():
            texto = self._leer(ruta)
            if _ARCHIVO.match(os.path.basename(ruta)) and not _APROBADO.search(texto):
                continue
            yield ruta, texto

    def copias(self):
        """`[(ruta, mensaje)]`: lo que suma un análisis aprobado no está tal cual en su principal (CA-24)."""
        salida = []
        for ruta, texto in self._aprobados_y_viejos():
            datos = AnalisisEnCurso.aporte(texto)
            principal = self.curso.principal_de(ruta)
            if datos and principal and datos[1] not in self._leer(principal):
                salida.append((ruta, "lo que suma no está tal cual en %s" % self._mostrar(principal)))
        return salida

    def fuera_de_la_lista(self):
        """`[(ruta, mensaje)]`: el análisis aprobado que no aparece en la «Lista de análisis» (CA-20)."""
        salida = []
        for ruta, _ in self._aprobados_y_viejos():
            principal = self.curso.principal_de(ruta)
            if not principal:
                continue
            enlace = os.path.relpath(ruta, os.path.dirname(principal)).replace(os.sep, "/")
            if "](%s)" % enlace not in AnalisisEnCurso.seccion(self._leer(principal), "Lista de análisis"):
                salida.append((ruta, "no aparece en la «Lista de análisis» de %s" % self._mostrar(principal)))
        return salida

    # ── todo junto ────────────────────────────────────────────────────────

    def revisar(self):
        """Una línea por cada falla de un análisis aprobado."""
        raiz = self.proyecto.raiz
        salida = []
        for ruta in self.analisis():
            texto = self._leer(ruta)
            if not _APROBADO.search(texto):
                continue
            relativa = os.path.relpath(ruta, raiz)
            for parte in self.faltantes(texto):
                salida.append(f"{relativa}: falta la sección «{parte}»: el análisis se aprobó sin revisar esa parte")
            if self.exige_lo_nuevo(texto):
                for mensaje in self.lo_nuevo(texto):
                    salida.append(f"{relativa}: {mensaje}")
            version = self.version_de(texto)
            if version and version >= DESDE_LECCIONES:
                for mensaje in self.lecciones(texto):
                    salida.append(f"{relativa}: {mensaje}")
        for ruta, mensaje in self.recomendaciones() + self.copias():
            salida.append(f"{os.path.relpath(ruta, raiz)}: {mensaje}")
        return salida

    def validar(self):
        """Lo de `revisar` como falla, y el aviso de la lista."""
        raiz = self.proyecto.raiz
        hallazgos = []
        for linea in self.revisar():
            ruta, mensaje = linea.split(": ", 1)
            hallazgos.append(Hallazgo(FALLA, os.path.join(raiz, ruta), 0, mensaje))
        for ruta, mensaje in self.fuera_de_la_lista():
            hallazgos.append(Hallazgo(AVISO, ruta, 0, mensaje))
        return hallazgos
