# -*- coding: utf-8 -*-
"""`EP-029·HU-003` · La parte que revisa las pruebas de un proyecto: ponerla y quitarla.

**Sin Django**: la llaman el instalador y el desinstalador, que corren sueltos.

**Según el lenguaje** (análisis 1 del pendiente 141, acuerdos 4 y 7):

- Python y Django: coverage.py en el Python del proyecto. Si le falta, se instala.
- Laravel: PHPUnit y la extensión PCOV de PHP. No se instalan: PCOV depende de
  cada máquina; se dice cómo ponerla.
- Angular: `karma-coverage`, que trae Angular. Si falta, se dice cómo ponerla.

**Se quita solo lo que puso Cimiento** (`02·F30`): la que ya tenía el proyecto es suya.

**Quien corre las órdenes se puede cambiar**, para probar sin instalar nada (`08·T3`).
"""
import json
import os
import shutil
import subprocess

from .lenguaje import ANGULAR, DJANGO, LARAVEL, PYTHON, python_del_proyecto, reconocer

SIN_LENGUAJE = "revisión de pruebas: Cimiento todavía no sabe revisar proyectos de este tipo"
SIN_PYTHON = "revisión de pruebas: falta el Python del proyecto (.venv o venv); crearlo y volver a instalar"
YA_ESTABA = "revisión de pruebas: coverage.py ya estaba en el proyecto"
INSTALAR = "revisión de pruebas: instalar coverage.py en el Python del proyecto"
NO_SE_PUDO = "revisión de pruebas: no se pudo instalar coverage.py (%s)"
SIN_PHPUNIT = "revisión de pruebas: falta PHPUnit; correr «composer install» en el proyecto"
SIN_PCOV = ("revisión de pruebas: falta PCOV, la extensión de PHP que revisa las pruebas; "
            "instalarla con «pecl install pcov» y activarla en php.ini")
SIN_KARMA = ("revisión de pruebas: falta karma-coverage; correr «npm install --save-dev karma-coverage» "
             "en el proyecto")
LISTA = "revisión de pruebas: el proyecto tiene con qué revisar sus pruebas"
QUITAR = "revisión de pruebas: quitar coverage.py, que puso Cimiento"
SE_QUEDA = "revisión de pruebas: coverage.py se queda, porque ya era del proyecto"


class ParteQueRevisa:

    def __init__(self, ejecutar=None, buscar=None):
        # Se buscan al usarlos, no al cargar el módulo: así una prueba puede cambiarlos.
        self.ejecutar = ejecutar or (lambda *a, **k: subprocess.run(*a, **k))
        self.buscar = buscar or (lambda nombre: shutil.which(nombre))

    def correr(self, partes, carpeta=None):
        return self.ejecutar(partes, cwd=carpeta, capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=600)

    def poner(self, ruta, aplicar):
        """`(pasos, tiene, puesta)`: qué se hizo, si el proyecto quedó con la parte y si la puso Cimiento."""
        lenguaje = reconocer(ruta)
        if lenguaje is None:
            return [SIN_LENGUAJE], False, False
        if lenguaje.nombre in (DJANGO, PYTHON):
            return self.poner_coverage(lenguaje.carpeta, ruta, aplicar)
        if lenguaje.nombre == LARAVEL:
            return self.revisar_laravel(lenguaje.carpeta)
        return self.revisar_angular(lenguaje.carpeta)

    def poner_coverage(self, carpeta, ruta, aplicar):
        py = python_del_proyecto(carpeta, ruta)
        if not py:
            return [SIN_PYTHON], False, False
        if self.correr([py, "-c", "import coverage"], carpeta).returncode == 0:
            return [YA_ESTABA], True, False
        if not aplicar:
            return [INSTALAR], False, False
        r = self.correr([py, "-m", "pip", "install", "coverage"], carpeta)
        if r.returncode != 0:
            ultima = ((r.stderr or r.stdout or "").strip().splitlines() or ["sin detalle"])[-1]
            return [NO_SE_PUDO % ultima[:200]], False, False
        return [INSTALAR], True, True

    def revisar_laravel(self, carpeta):
        php = self.buscar("php")
        if not os.path.isfile(os.path.join(carpeta, "vendor", "bin", "phpunit")):
            return [SIN_PHPUNIT], False, False
        if not php or "pcov" not in (self.correr([php, "-m"], carpeta).stdout or "").lower():
            return [SIN_PCOV], False, False
        return [LISTA], True, False

    def revisar_angular(self, carpeta):
        if os.path.isdir(os.path.join(carpeta, "node_modules", "karma-coverage")):
            return [LISTA], True, False
        try:
            with open(os.path.join(carpeta, "package.json"), encoding="utf-8") as f:
                paquete = json.load(f)
        except (OSError, ValueError):
            paquete = {}
        if "karma-coverage" in {**paquete.get("dependencies", {}), **paquete.get("devDependencies", {})}:
            return [LISTA], True, False
        return [SIN_KARMA], False, False

    def quitar(self, ruta, puesta, aplicar):
        """Los pasos de quitar: solo desinstala si la puso Cimiento."""
        if not puesta:
            return [SE_QUEDA]
        lenguaje = reconocer(ruta)
        py = python_del_proyecto(lenguaje.carpeta, ruta) if lenguaje else None
        if py and aplicar:
            self.correr([py, "-m", "pip", "uninstall", "-y", "coverage"], lenguaje.carpeta)
        return [QUITAR]
