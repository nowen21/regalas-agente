# -*- coding: utf-8 -*-
"""`EP-029·HU-005` · Las pruebas de navegador de un proyecto: encontrarlas y correrlas.

**Las escribe cada proyecto; Cimiento las corre** (análisis 1 del pendiente 141,
acuerdo 6). Un proyecto las tiene si trae `playwright.config` (ts, js o mjs), o
archivos de prueba en Python que usan Playwright.

**Con lo del proyecto**: `npx playwright test` en la carpeta del `playwright.config`,
o el Python del proyecto. En Django, `manage.py test` ya las corre dentro de la
revisión, pero aparte se sabe cuáles fallaron sin mezclarlas con las demás.

**Sin Django**: lo usa la revisión, y no necesita más.
"""
import json
import os
import re
import shutil
import subprocess

from .lenguaje import DJANGO, SE_SALTAN, _carpetas, python_del_proyecto, reconocer

PASARON, FALLARON, SIN_PRUEBAS = "pasaron", "fallaron", "sin pruebas"
CONFIGURACIONES = ("playwright.config.ts", "playwright.config.js", "playwright.config.mjs")
_USA_PLAYWRIGHT = re.compile(r"^\s*(from|import)\s+playwright\b", re.M)
TOPE = 30 * 60


class Navegador:

    def __init__(self, correr=None, buscar=None):
        # Se buscan al usarlos, no al cargar el módulo: así una prueba puede cambiarlos.
        self.correr = correr or (lambda *a, **k: subprocess.run(*a, **k))
        self.buscar = buscar or (lambda nombre: shutil.which(nombre))

    def orden(self, partes, carpeta):
        return self.correr(partes, cwd=carpeta, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=TOPE)

    @staticmethod
    def configuracion(raiz):
        """La carpeta que tiene un `playwright.config`, o `None`."""
        for carpeta in _carpetas(raiz):
            if any(os.path.isfile(os.path.join(carpeta, n)) for n in CONFIGURACIONES):
                return carpeta
        return None

    @staticmethod
    def archivos_python(carpeta):
        """Los módulos de prueba que usan Playwright, como `app.tests_pantallas`, desde `carpeta`."""
        modulos = []
        for actual, carpetas, archivos in os.walk(carpeta):
            carpetas[:] = sorted(c for c in carpetas if c not in SE_SALTAN and not c.startswith("."))
            for nombre in sorted(archivos):
                if not (nombre.startswith("test") and nombre.endswith(".py")):
                    continue
                ruta = os.path.join(actual, nombre)
                try:
                    with open(ruta, encoding="utf-8", errors="replace") as f:
                        if not _USA_PLAYWRIGHT.search(f.read()):
                            continue
                except OSError:
                    continue
                relativa = os.path.relpath(ruta, carpeta)[:-3]
                modulos.append(relativa.replace(os.sep, "."))
        return modulos

    def revisar(self, raiz):
        """`{"navegador": …, "navegador_detalle": …}` para la revisión del proyecto en `raiz`."""
        try:
            carpeta = self.configuracion(raiz)
            if carpeta:
                return self.con_npx(carpeta)
            lenguaje = reconocer(raiz)
            if lenguaje and lenguaje.carpeta:
                modulos = self.archivos_python(lenguaje.carpeta)
                if modulos:
                    return self.con_python(lenguaje, raiz, modulos)
        except subprocess.TimeoutExpired:
            return {"navegador": FALLARON, "navegador_detalle": "Tardaron más de 30 minutos y se detuvieron."}
        except OSError as error:
            return {"navegador": FALLARON, "navegador_detalle": "No se pudieron correr: %s" % error}
        return {"navegador": SIN_PRUEBAS, "navegador_detalle": ""}

    def con_npx(self, carpeta):
        npx = self.buscar("npx")
        if not npx:
            return {"navegador": FALLARON,
                    "navegador_detalle": "En esta máquina no está instalado Node.js, que se necesita para correrlas."}
        corrida = self.orden([npx, "playwright", "test", "--reporter=json"], carpeta)
        try:
            datos = json.loads(corrida.stdout or "")
            stats = datos.get("stats", {})
            bien, mal = int(stats.get("expected", 0)), int(stats.get("unexpected", 0))
        except (ValueError, AttributeError):
            return {"navegador": FALLARON, "navegador_detalle": "No dejaron un resultado que se pueda leer."}
        if mal:
            return {"navegador": FALLARON, "navegador_detalle": "%d fallaron y %d pasaron." % (mal, bien)}
        return {"navegador": PASARON, "navegador_detalle": "Pasaron las %d." % bien}

    def con_python(self, lenguaje, raiz, modulos):
        py = python_del_proyecto(lenguaje.carpeta, raiz)
        if not py:
            return {"navegador": FALLARON,
                    "navegador_detalle": "No se encontró el Python del proyecto (la carpeta .venv o venv)."}
        if lenguaje.nombre == DJANGO:
            partes = [py, "manage.py", "test", "--noinput", *modulos]
        else:
            partes = [py, "-m", "unittest", *modulos]
        corrida = self.orden(partes, lenguaje.carpeta)
        cuantos = "%d archivo(s) de pruebas de navegador" % len(modulos)
        if corrida.returncode != 0:
            return {"navegador": FALLARON, "navegador_detalle": "Fallaron en %s." % cuantos}
        return {"navegador": PASARON, "navegador_detalle": "Pasaron en %s." % cuantos}
