# -*- coding: utf-8 -*-
"""La puerta de antes de publicar: que lo nuevo no haya roto lo anterior.

**Publicar es la acción que no se puede deshacer del lado de quien recibe.** Un
proyecto que adopta una versión rota se lleva el problema, y retirarla no le
devuelve el día que perdió.

**Qué se vuelve a correr:** las comprobaciones del estándar y sus dos baterías
de pruebas. Eso es «lo que ya funcionaba»: no una lista escrita a mano de lo que
alguien se acuerda, sino todo lo que estaba en verde.

**Y qué obliga a rehacer se declara.** Una funcionalidad en «no cumple» no
detiene la publicación por sí sola si nadie la prometió en esta versión, pero sí
tiene que salir dicha: publicar sabiendo qué queda mal es una decisión; publicar
sin saberlo es un accidente.
"""
import os
import subprocess
import sys
import time

from django.conf import settings

from nucleo.proyectos.models import Proyecto
from nucleo.seguridad import claves
from . import core, estado

# Cuánto se espera, como mucho. Las comprobaciones tardan cerca de dos minutos y
# las baterías otro tanto; el margen es para un proyecto mucho más grande.
ESPERA_MAXIMA = 1800


class Puerta(object):
    """Si se puede publicar, y por qué no si no se puede."""

    def __init__(self, se_pudo, porque="", veredicto=None, pruebas=None,
                 rehacer=(), sin_verificar=(), segundos=0.0):
        self.se_pudo = se_pudo
        self.porque = porque
        self.veredicto = veredicto
        self.pruebas = pruebas or {}
        self.rehacer = list(rehacer)
        self.sin_verificar = list(sin_verificar)
        self.segundos = segundos

    @property
    def pasa(self):
        """Pasa solo si se pudo revisar, todo está en verde y nada rompió.

        **Lo que está sin verificar no la detiene**, y sí se declara: que una
        funcionalidad no tenga prueba no quiere decir que esta versión la haya
        roto.
        """
        if not self.se_pudo or self.veredicto is None:
            return False
        return (self.veredicto.cumple and self.pruebas.get("verdes", False)
                and not self.rehacer)


def _correr_las_baterias(raiz):
    """Las dos baterías del proyecto, por el punto de entrada del estándar.

    Devuelve `{"corrio", "verdes", "salida"}`. Si no se pudo correr, `corrio`
    es falso: **no haber podido correrlas no es lo mismo que tenerlas en
    verde**, y publicar con esa duda es publicar a ciegas.

    **Se le pide la suite del proyecto, no la del estándar.** La primera vez
    esto pedía `internas`, que corre las pruebas del estándar donde el estándar
    vive, y con un argumento que ese subcomando no acepta. Salió con error, y
    la puerta lo leyó como **rojo**: dijo que no se publicaba, con las pruebas
    en verde. Es el error más parecido a lo que esta puerta viene a evitar.
    """
    entrada = os.path.join(str(settings.CARPETA_VALIDADORES), "validar.py")
    if not os.path.isfile(entrada):
        return {"corrio": False, "verdes": False,
                "salida": "no está el punto de entrada del estándar"}
    try:
        corrida = subprocess.run(
            [sys.executable, entrada, "suite", "--raiz", raiz],
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=ESPERA_MAXIMA)
    except (OSError, subprocess.SubprocessError) as falla:
        return {"corrio": False, "verdes": False,
                "salida": "no se pudieron correr las pruebas: %s" % falla}
    salida, _ = claves.tapar((corrida.stdout or "") + (corrida.stderr or ""))
    return {"corrio": True, "verdes": corrida.returncode == 0,
            "salida": salida}


def revisar_antes_de_publicar(identificador):
    """Corre todo lo que ya funcionaba y dice si se puede publicar.

    **Sin trabajo manual:** una sola orden corre las comprobaciones y las dos
    baterías. Si todo está verde y nada quedó en «no cumple», pasa.
    """
    try:
        proyecto = Proyecto.objects.get(identificador=identificador)
    except Proyecto.DoesNotExist:
        return Puerta(False, "no hay un proyecto registrado con ese nombre")

    empezo = time.time()
    veredicto = core.comprobar(identificador)
    if not veredicto.se_pudo:
        return Puerta(False, veredicto.porque, veredicto,
                      segundos=time.time() - empezo)

    pruebas = _correr_las_baterias(proyecto.ruta_codigo)
    if not pruebas["corrio"]:
        return Puerta(False, pruebas["salida"], veredicto, pruebas,
                      segundos=time.time() - empezo)

    estados = estado.estado_de_todas(proyecto.ruta_codigo)
    rehacer = [uno["funcionalidad"] for uno in estados
               if uno["estado"] == estado.NO_CUMPLE]
    sin_verificar = [uno["funcionalidad"] for uno in estados
                     if uno["estado"] == estado.SIN_VERIFICAR]

    return Puerta(True, "", veredicto, pruebas, rehacer, sin_verificar,
                  time.time() - empezo)
