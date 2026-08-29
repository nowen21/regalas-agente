#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corre las pruebas de `validadores/tests/` y **dice cuántas corrió**.

**El caso que lo hizo falta.** La carpeta tiene 67 archivos y 650 pruebas, y
ningún comando del repositorio las ejecutaba. La orden documentada desde la
primera prueba —`python -m unittest discover -s validadores/tests`— se caía
antes de correr nada porque faltaba el `__init__.py`, y su error se leía como
ruido. Una prueba escrita hace diez días para cazar exactamente el defecto que
tuvimos seis días en rojo **nunca se corrió** (`S-075`).

**Por qué no basta el archivo que faltaba.** Con él, `discover` carga. Pero
`discover` sobre una carpeta vacía **termina en 0**, y eso es el defecto que
estamos arreglando, no su arreglo: un silencio que se lee como éxito. Acá cero
pruebas es **rojo**.

**Un solo proceso, y está medido.** Los 650 casos cargados juntos dan las mismas
fallas en los mismos archivos que corriéndolos uno por uno: no se estorban. Un
proceso por archivo costaría 67 arranques de Python para el mismo resultado.

**Se puede pedir un subconjunto**, que es lo que hace cumplible `02·F5` sobre
esta carpeta: una fase corre las pruebas que toca, no las 650. Un nombre que no
existe es **rojo**, no una corrida vacía en verde.

**No sustituye a `pruebas.py`.** Son dos suites y siguen separadas, a propósito.
"""
import importlib.util
import io
import os
import subprocess
import sys
import time
import unittest

import comun
from comun import AVISO, FALLA, Hallazgo

CARPETA = os.path.join("validadores", "tests")

# El sello de la última corrida completa **en verde**. Vive junto al registro
# de sesiones, que ya está fuera del control de versiones: es estado de
# trabajo de esta máquina, no memoria del proyecto.
SELLO = os.path.join("historico-chat", ".tocado", "internas-verde.txt")


def carpeta_de(raiz=None):
    return os.path.join(raiz or comun.RAIZ, CARPETA)


def archivos_de(carpeta):
    """Los archivos de prueba, ordenados. Vacío si la carpeta no está."""
    if not os.path.isdir(carpeta):
        return []
    return sorted(n for n in os.listdir(carpeta)
                  if n.startswith("test") and n.endswith(".py"))


def _cargar(carpeta, nombre):
    """El módulo, cargado por su ruta. Devuelve `(modulo, None)` o `(None, error)`.

    Por ruta y no por importación normal: así el corredor funciona esté o no la
    carpeta armada como paquete, y un archivo que no carga **se reporta** en vez
    de tumbar la corrida entera (`EP-004·HU-003`).
    """
    ruta = os.path.join(carpeta, nombre)
    marca = "corredor_" + nombre[:-3]
    spec = importlib.util.spec_from_file_location(marca, ruta)
    if spec is None or spec.loader is None:
        return (None, "no se pudo leer como módulo de Python")
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[marca] = modulo
    try:
        spec.loader.exec_module(modulo)
    except Exception as e:                                  # noqa: BLE001
        del sys.modules[marca]
        return (None, "%s: %s" % (type(e).__name__, e))
    return (modulo, None)


def _sin_ruido(funcion):
    """Corre `funcion` con la salida de las pruebas tapada.

    Las pruebas de esta carpeta imprimen bastante —informes de instalación,
    reportes de validadores— y eso enterraría el conteo, que es lo único que
    hay que leer. Se tapa la salida, **no los errores**.
    """
    antes = sys.stdout
    sys.stdout = io.open(os.devnull, "w", encoding="utf-8")
    try:
        return funcion()
    finally:
        sys.stdout.close()
        sys.stdout = antes


def correr(raiz=None, solo=None):
    """Corre la carpeta. Devuelve `(resultado, hallazgos, nombres)`.

    `solo` es una lista de nombres de archivo; sin ella van todos.
    """
    carpeta = carpeta_de(raiz)
    hallazgos = []
    if not os.path.isdir(carpeta):
        return (None, [Hallazgo(FALLA, carpeta, 0,
                                "no existe la carpeta de pruebas — no se "
                                "comprobó nada, y eso no es lo mismo que estar "
                                "bien (08·T5)")], [])

    disponibles = archivos_de(carpeta)
    if solo:
        pedidos, faltantes = [], []
        for n in solo:
            n = n if n.endswith(".py") else n + ".py"
            (pedidos if n in disponibles else faltantes).append(n)
        for n in faltantes:
            hallazgos.append(Hallazgo(
                FALLA, carpeta, 0,
                "se pidió `%s` y no está en la carpeta — un nombre mal "
                "escrito no puede terminar en una corrida vacía y verde" % n))
        disponibles = pedidos

    suite = unittest.TestSuite()
    cargador = unittest.TestLoader()
    corridos = []
    for nombre in disponibles:
        modulo, error = _cargar(carpeta, nombre)
        if error:
            hallazgos.append(Hallazgo(
                FALLA, os.path.join(carpeta, nombre), 0,
                "no se pudo cargar — %s" % error))
            continue
        suite.addTests(cargador.loadTestsFromModule(modulo))
        corridos.append(nombre)

    resultado = unittest.TestResult()
    _sin_ruido(lambda: suite.run(resultado))

    # **Cero pruebas es rojo.** Es el defecto que originó esta pieza: una orden
    # que no corría nada, y su silencio leído como que todo estaba bien.
    if resultado.testsRun == 0:
        hallazgos.append(Hallazgo(
            FALLA, carpeta, 0,
            "se corrieron **0 pruebas** — cero no es verde: quiere decir "
            "que no se comprobó nada (08·T5)"))

    for caso, traza in list(resultado.failures) + list(resultado.errors):
        hallazgos.append(Hallazgo(
            FALLA, os.path.join(carpeta, _archivo_de(caso, corridos)), 0,
            "%s — %s" % (_nombre_de(caso), _ultima_linea(traza))))

    return (resultado, hallazgos, corridos)


def _archivo_de(caso, corridos):
    """De qué archivo salió el caso. `?` si no se puede saber, sin inventar."""
    marca = getattr(caso, "__module__", "") or ""
    if marca.startswith("corredor_"):
        candidato = marca[len("corredor_"):] + ".py"
        if candidato in corridos:
            return candidato
    return "?"


def _nombre_de(caso):
    try:
        return caso.id().split(".", 1)[-1]
    except Exception:                                       # noqa: BLE001
        return str(caso)


def _ultima_linea(traza):
    lineas = [l.strip() for l in (traza or "").splitlines() if l.strip()]
    return lineas[-1][:160] if lineas else "sin detalle"


def sellar(raiz=None, cuando=None):
    """Deja escrito que la carpeta entera pasó en verde, y cuándo."""
    ruta = os.path.join(raiz or comun.RAIZ, SELLO)
    carpeta = os.path.dirname(ruta)
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write("%s\n" % (cuando or time.strftime("%Y-%m-%d %H:%M:%S")))
    return ruta


def _ultimo_commit(raiz):
    """La hora del último commit. `None` si acá no hay repositorio."""
    try:
        salida = subprocess.check_output(
            ["git", "log", "-1", "--format=%ct"],
            cwd=raiz, stderr=subprocess.DEVNULL)
        return float(salida.decode("ascii", "replace").strip())
    except (OSError, ValueError, subprocess.CalledProcessError):
        return None


def reclamo(raiz=None):
    """Avisa si lo que se va a publicar es más nuevo que la última corrida.

    **Reclama, no corre.** Las 650 pruebas tardan 9,6 minutos, y este
    repositorio hace 16 commits por día: correrlas en cada uno costaría 39
    horas cada dos semanas. Un peaje así se apaga en una tarde, y entonces
    quedamos peor que hoy — con un control que figura como puesto.

    Lo que cuesta esto es mirar la fecha de un archivo.
    """
    raiz = raiz or comun.RAIZ
    ruta = os.path.join(raiz, SELLO)
    if not os.path.isfile(ruta):
        return [Hallazgo(AVISO, ruta, 0,
                         "las pruebas del estándar nunca corrieron en esta "
                         "copia — `python validadores/validar.py internas` "
                         "(tarda ~10 min; no detiene el push)")]
    commit = _ultimo_commit(raiz)
    if commit is None or os.path.getmtime(ruta) >= commit:
        return []
    return [Hallazgo(AVISO, ruta, 0,
                     "hay commits posteriores a la última corrida de las "
                     "pruebas del estándar — `python validadores/validar.py "
                     "internas` (tarda ~10 min; no detiene el push)")]


def validar(raiz=None, solo=None):
    """`[Hallazgo]`, más el resumen como aviso. Para `validar.py`."""
    resultado, hallazgos, corridos = correr(raiz, solo)
    if resultado is not None:
        # **Solo sella la corrida entera y limpia.** Sellar un subconjunto
        # diría «esto se comprobó» sobre lo que no se miró, que es el defecto
        # del que sale toda esta pieza.
        if not solo and not [h for h in hallazgos if h.severidad == FALLA]:
            sellar(raiz)
        hallazgos.append(Hallazgo(
            AVISO, carpeta_de(raiz), 0,
            "%d prueba(s) en %d archivo(s) · %d falla(s) · %d error(es)"
            % (resultado.testsRun, len(corridos),
               len(resultado.failures), len(resultado.errors))))
    return hallazgos


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("corredor")
