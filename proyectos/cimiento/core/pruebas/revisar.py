# -*- coding: utf-8 -*-
"""`EP-029·HU-002` · Revisar qué parte de un proyecto queda sin pruebas.

**Cada lenguaje con su herramienta** (análisis 1 del pendiente 141, acuerdo 4):
Python y Django con coverage.py, Laravel con PHPUnit y PCOV, Angular con
`ng test --code-coverage`. El que no se reconoce queda «sin medición» y no falla.

**Se corre con lo del proyecto**: su Python (`.venv` o `venv`), su PHPUnit, su
Angular. Las pruebas del proyecto necesitan sus propias dependencias.

**Los mensajes son para quien no sabe del tema** (acuerdo 8): dicen qué pasó y
qué hacer, sin nombrar lo que pasa por dentro.

**Quien corre las órdenes se puede cambiar** (`correr`), para probar sin tener
las herramientas instaladas (`08·T3`).
"""
import json
import os
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from django.utils import timezone

from .lenguaje import ANGULAR, DJANGO, LARAVEL, PYTHON, python_del_proyecto, reconocer
from .models import PruebasDelProyecto, Revision
from .navegador import Navegador

TOPE = 30 * 60
MAS_LINEAS = 200

SIN_MEDICION = ("Cimiento todavía no sabe revisar proyectos de este tipo. "
                "Sabe revisar los hechos en Python, Django, Laravel y Angular.")
SIN_PYTHON = ("No se encontró el Python del proyecto (la carpeta .venv o venv). "
              "Hay que crearlo e instalar lo que el proyecto necesita.")
FALTA_HERRAMIENTA = ("Al proyecto le falta la herramienta que revisa las pruebas. "
                     "Para ponerla, hay que volver a instalar Cimiento en él.")
FALTA_PROGRAMA = "En esta máquina no está instalado %s, que se necesita para revisar este proyecto."
TARDO = "La revisión tardó más de 30 minutos y se detuvo."
FALLARON = "Algunas pruebas fallaron; el resultado cuenta solo lo que alcanzaron a recorrer."
SIN_RESULTADO = "Las pruebas no se pudieron correr. Lo último que dijeron: %s"


class Revisor:
    """Corre la revisión de un proyecto y devuelve los campos de su `Revision`."""

    def __init__(self, correr=None, buscar=None):
        # Se buscan al usarlos, no al cargar el módulo: así una prueba puede cambiarlos.
        self.correr = correr or (lambda *a, **k: subprocess.run(*a, **k))
        self.buscar = buscar or (lambda nombre: shutil.which(nombre))

    # -- lo común --------------------------------------------------------

    def orden(self, partes, carpeta, entorno=None):
        extra = {"env": {**os.environ, **entorno}} if entorno else {}
        return self.correr(partes, cwd=carpeta, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=TOPE, **extra)

    @staticmethod
    def fallo(herramienta, mensaje):
        return {"herramienta": herramienta, "resultado": Revision.FALLO, "porcentaje": None,
                "archivos": [], "mensaje": mensaje}

    @staticmethod
    def hecha(herramienta, porcentaje, archivos, pruebas_fallaron):
        archivos = sorted(archivos, key=lambda a: (a["porcentaje"], a["archivo"]))
        return {"herramienta": herramienta, "resultado": Revision.HECHA,
                "porcentaje": round(porcentaje, 1), "archivos": archivos,
                "mensaje": FALLARON if pruebas_fallaron else ""}

    @staticmethod
    def ultimo_dicho(salida):
        lineas = [l for l in (salida or "").strip().splitlines() if l.strip()]
        return " ".join(lineas[-3:])[:500] or "nada"

    def revisar(self, raiz):
        lenguaje = reconocer(raiz)
        if lenguaje is None:
            return {"herramienta": "", "resultado": Revision.SIN_MEDICION, "porcentaje": None,
                    "archivos": [], "mensaje": SIN_MEDICION}
        hacer = {DJANGO: self.django, PYTHON: self.python, LARAVEL: self.laravel, ANGULAR: self.angular}
        try:
            return hacer[lenguaje.nombre](lenguaje.carpeta, raiz)
        except subprocess.TimeoutExpired:
            return self.fallo("", TARDO)
        except OSError as error:
            return self.fallo("", SIN_RESULTADO % error)

    # -- Python y Django -------------------------------------------------

    def django(self, carpeta, raiz):
        return self.con_coverage(carpeta, raiz, ["manage.py", "test", "--noinput"])

    def python(self, carpeta, raiz):
        return self.con_coverage(carpeta, raiz, ["-m", "unittest", "discover"])

    def con_coverage(self, carpeta, raiz, pruebas):
        herramienta = "coverage.py"
        py = python_del_proyecto(carpeta, raiz)
        if not py:
            return self.fallo(herramienta, SIN_PYTHON)
        with tempfile.TemporaryDirectory() as tmp:
            reporte = os.path.join(tmp, "cobertura.json")
            # Los datos de coverage.py van a la carpeta temporal: si no, quedaría un
            # `.coverage` suelto en el repositorio del proyecto revisado.
            datos_coverage = {"COVERAGE_FILE": os.path.join(tmp, ".coverage")}
            corrida = self.orden([py, "-m", "coverage", "run", "--source=.", *pruebas], carpeta, datos_coverage)
            if "No module named coverage" in (corrida.stderr or ""):
                return self.fallo(herramienta, FALTA_HERRAMIENTA)
            self.orden([py, "-m", "coverage", "json", "-o", reporte], carpeta, datos_coverage)
            if not os.path.isfile(reporte):
                return self.fallo(herramienta, SIN_RESULTADO % self.ultimo_dicho(corrida.stderr))
            with open(reporte, encoding="utf-8") as f:
                datos = json.load(f)
        archivos = [{"archivo": nombre.replace("\\", "/"),
                     "porcentaje": round(info["summary"]["percent_covered"], 1),
                     "sin_pruebas": info.get("missing_lines", [])[:MAS_LINEAS]}
                    for nombre, info in datos.get("files", {}).items()]
        return self.hecha(herramienta, datos["totals"]["percent_covered"], archivos, corrida.returncode != 0)

    # -- Laravel ---------------------------------------------------------

    def laravel(self, carpeta, raiz):
        herramienta = "PHPUnit con PCOV"
        php = self.buscar("php")
        if not php:
            return self.fallo(herramienta, FALTA_PROGRAMA % "PHP")
        phpunit = os.path.join(carpeta, "vendor", "bin", "phpunit")
        if not os.path.isfile(phpunit):
            return self.fallo(herramienta, FALTA_HERRAMIENTA)
        with tempfile.TemporaryDirectory() as tmp:
            reporte = os.path.join(tmp, "clover.xml")
            corrida = self.orden([php, phpunit, "--coverage-clover", reporte], carpeta)
            if "No code coverage driver" in (corrida.stdout or "") + (corrida.stderr or ""):
                return self.fallo(herramienta, FALTA_HERRAMIENTA)
            if not os.path.isfile(reporte):
                return self.fallo(herramienta, SIN_RESULTADO % self.ultimo_dicho(corrida.stdout))
            return self.leer_clover(reporte, carpeta, herramienta, corrida.returncode != 0)

    def leer_clover(self, reporte, carpeta, herramienta, pruebas_fallaron):
        proyecto = ET.parse(reporte).getroot().find("project")
        total = proyecto.find("metrics")
        archivos = []
        for archivo in proyecto.iter("file"):
            m = archivo.find("metrics")
            instrucciones = int(m.get("statements", 0))
            if not instrucciones:
                continue
            nombre = os.path.relpath(archivo.get("name"), carpeta).replace("\\", "/") \
                if os.path.isabs(archivo.get("name")) else archivo.get("name")
            archivos.append({"archivo": nombre,
                             "porcentaje": round(100.0 * int(m.get("coveredstatements", 0)) / instrucciones, 1),
                             "sin_pruebas": [int(l.get("num")) for l in archivo.iter("line")
                                             if l.get("type") == "stmt" and l.get("count") == "0"][:MAS_LINEAS]})
        instrucciones = int(total.get("statements", 0))
        porcentaje = 100.0 * int(total.get("coveredstatements", 0)) / instrucciones if instrucciones else 0.0
        return self.hecha(herramienta, porcentaje, archivos, pruebas_fallaron)

    # -- Angular ---------------------------------------------------------

    def angular(self, carpeta, raiz):
        herramienta = "ng test"
        npx = self.buscar("npx")
        if not npx:
            return self.fallo(herramienta, FALTA_PROGRAMA % "Node.js")
        corrida = self.orden([npx, "ng", "test", "--code-coverage", "--watch=false",
                              "--browsers=ChromeHeadless"], carpeta)
        m = re.search(r"Lines\s*:\s*([\d.]+)%", corrida.stdout or "")
        if not m:
            return self.fallo(herramienta, SIN_RESULTADO % self.ultimo_dicho(corrida.stdout))
        return self.hecha(herramienta, float(m.group(1)), [], corrida.returncode != 0)


def revisar_y_guardar(proyecto, revisor=None):
    """Revisa el proyecto, guarda su `Revision` y apaga «Revisando». Devuelve la revisión."""
    estado = PruebasDelProyecto.de(proyecto)
    estado.revisando_desde = estado.revisando_desde or timezone.now()
    estado.save()
    try:
        revisor = revisor or Revisor()
        campos = revisor.revisar(proyecto.ruta)
        # `EP-029·HU-005` · Y las pruebas de navegador del proyecto, si las tiene.
        campos.update(Navegador(revisor.correr, revisor.buscar).revisar(proyecto.ruta))
        return Revision.objects.create(proyecto=proyecto, **campos)
    finally:
        estado.revisando_desde = None
        estado.save()
