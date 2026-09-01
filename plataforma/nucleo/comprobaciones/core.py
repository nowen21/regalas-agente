# -*- coding: utf-8 -*-
"""Dice si un proyecto cumple lo que las reglas exigen. **No corrige nada.**

**Las comprobaciones son del estándar, y no se duplican.** Acá solo se le pide
que las corra contra un proyecto y se lee lo que responde. Copiarlas dejaría dos
versiones que se separan, y la vieja daría por bueno lo que la nueva rechaza.

**Se le pide por su punto de entrada, en un proceso aparte.** Es como se corren
de verdad: el estándar arma su contexto, descubre sus comprobaciones y las
corre. Cargar sus archivos desde acá daría un número que nadie más obtiene, y el
día que cambie por dentro esto se rompería sin que nadie lo note. Es la misma
decisión que ya tomó el corredor del estándar para correr la batería de la
plataforma, en la dirección contraria.

**Sin comprobar no es lo mismo que en verde.** Un proyecto sin el estándar
instalado no se puede juzgar, y decir que cumple sería mentir. Se dice.
"""
import os
import re
import subprocess
import sys
import time

from django.conf import settings

from nucleo.proyectos.models import Proyecto
from nucleo.seguridad import claves

# Lo que el estándar imprime al final: «32 comprobación(es) corridas · 1 con
# fallas». Es su resumen, y de ahí salen los dos números que importan.
_RESUMEN = re.compile(
    u"(\d+)\s+comprobaci\u00f3n\(es\) corridas\s*·\s*(\d+) con fallas")

# Cada falla, tal como el estándar la reporta: `[FALLA] archivo:linea — qué`.
_FALLA = re.compile(u"^\[FALLA\]\s+([^\s:]+(?::\d+)?)\s*[—-]\s*(.+)$",
                    re.MULTILINE)

# Cuánto se espera, como mucho. Las 32 comprobaciones de este repositorio tardan
# menos de un minuto; el margen es para un proyecto mucho más grande.
ESPERA_MAXIMA = 900


class Veredicto(object):
    """Lo que se sabe de un proyecto después de comprobarlo.

    `se_pudo` distingue las dos formas de no estar en verde: **no cumple** y
    **no se pudo comprobar**. Confundirlas hace que nadie mire el rojo.
    """

    def __init__(self, se_pudo, porque="", corridas=0, con_fallas=0,
                 fallas=(), segundos=0.0):
        self.se_pudo = se_pudo
        self.porque = porque
        self.corridas = corridas
        self.con_fallas = con_fallas
        self.fallas = list(fallas)
        self.segundos = segundos

    @property
    def cumple(self):
        """Cumple solo si se pudo comprobar, corrió algo y nada falló."""
        return self.se_pudo and self.corridas > 0 and self.con_fallas == 0


def _tiene_el_estandar(ruta):
    """Si esa carpeta tiene el cuerpo de reglas instalado."""
    return os.path.isdir(os.path.join(ruta, "base"))


def comprobar(identificador):
    """Corre las comprobaciones del estándar contra un proyecto conectado.

    Devuelve un `Veredicto`. **Nunca modifica nada**: el estándar solo lee, y
    acá no se escribe ni siquiera el resultado.
    """
    try:
        proyecto = Proyecto.objects.get(identificador=identificador)
    except Proyecto.DoesNotExist:
        return Veredicto(False, "no hay un proyecto registrado con ese nombre")

    ruta = proyecto.ruta_codigo
    if not os.path.isdir(ruta):
        return Veredicto(False, "la carpeta del proyecto ya no está: %s" % ruta)
    if not _tiene_el_estandar(ruta):
        return Veredicto(
            False,
            "ese proyecto no tiene el estándar instalado, así que no hay contra "
            "qué comprobarlo. **No es lo mismo que estar en verde**")

    entrada = os.path.join(str(settings.CARPETA_VALIDADORES), "validar.py")
    if not os.path.isfile(entrada):
        return Veredicto(False,
                         "no está el punto de entrada del estándar: %s" % entrada)

    empezo = time.time()
    try:
        corrida = subprocess.run(
            [sys.executable, entrada, "todo", "--raiz", ruta],
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=ESPERA_MAXIMA)
    except (OSError, subprocess.SubprocessError) as falla:
        return Veredicto(False, "no se pudieron correr las comprobaciones: %s"
                         % falla)
    segundos = time.time() - empezo

    salida = (corrida.stdout or "") + (corrida.stderr or "")
    # La salida trae fragmentos de los archivos del proyecto, y uno de esos
    # puede traer una clave. Se tapa antes de que nadie la vea.
    salida, _ = claves.tapar(salida)

    resumen = _RESUMEN.search(salida)
    if not resumen:
        return Veredicto(False, "el estándar no respondió con su resumen; no se "
                                "puede decir si cumple")

    corridas = int(resumen.group(1))
    con_fallas = int(resumen.group(2))
    fallas = [{"donde": donde, "que": que.strip()}
              for donde, que in _FALLA.findall(salida)]
    return Veredicto(True, "", corridas, con_fallas, fallas, segundos)
