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
import re
import subprocess
import sys
import time
import unittest

import comun
from comun import AVISO, FALLA, Hallazgo

CARPETA = os.path.join("validadores", "tests")

# `EP-005·HU-021` fase B · **La otra batería de este repositorio.** La
# plataforma tiene sus propias pruebas y las corre su marco, no `unittest`
# a secas: se le pide por su punto de entrada. Estuvieron fuera de esta
# corrida hasta el 2026-08-31, y ese día una subida de versión las puso en
# rojo por la mañana y se supo por la tarde, de casualidad (`S-097`).
PLATAFORMA = "plataforma"

# El sello de la última corrida completa. Es estado de trabajo de esta máquina,
# no memoria del proyecto, así que no se versiona.
#
# **Y va en su propia carpeta, no junto al registro de sesiones.** La primera
# versión lo puso en `.tocado/`, donde `sesiones.registros()` lee **todo** `.txt`
# como si fuera el registro de una conversación: el sello se contaba como una
# sesión viva llamada «internas», con dos archivos que en realidad eran una
# fecha y un número. Dos cosas distintas en el mismo cajón.
SELLO = os.path.join("historico-chat", ".estado", "internas.txt")


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


def sellar(raiz=None, fallas=0, cuando=None):
    """Deja constancia de la última corrida entera, **y de cómo le fue**.

    **Se sella toda corrida entera, no solo la limpia.** La primera versión
    sellaba únicamente el verde, y el reclamo decía «nunca corrieron» sobre una
    carpeta que había corrido dos veces ese día — lo dijo en el primer push de
    verdad. Quien leyera eso iría a correr diez minutos para volver a leer lo
    mismo. **Un aviso que manda a hacer algo que no cambia nada se apaga.**
    """
    ruta = os.path.join(raiz or comun.RAIZ, SELLO)
    carpeta = os.path.dirname(ruta)
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write("%s\n%d\n" % (cuando or time.strftime("%Y-%m-%d %H:%M:%S"),
                              fallas))
    return ruta


def _sello(raiz):
    """`(cuando, fallas)` de la última corrida entera. `None` si no hay."""
    ruta = os.path.join(raiz, SELLO)
    if not os.path.isfile(ruta):
        return None
    try:
        with io.open(ruta, encoding="utf-8") as f:
            lineas = [l.strip() for l in f if l.strip()]
        # Un sello viejo trae solo la fecha: se lee como corrida limpia, que es
        # lo único que aquella versión sellaba.
        return (lineas[0], int(lineas[1]) if len(lineas) > 1 else 0)
    except (OSError, ValueError, IndexError):
        return None


def _ultimo_commit(raiz):
    """La hora del último commit. `None` si acá no hay repositorio."""
    try:
        salida = subprocess.check_output(
            ["git", "log", "-1", "--format=%ct"],
            cwd=raiz, stderr=subprocess.DEVNULL)
        return float(salida.decode("ascii", "replace").strip())
    except (OSError, ValueError, subprocess.CalledProcessError):
        return None


ORDEN = "`python validadores/validar.py internas` (tarda ~10 min; no detiene el push)"


def reclamo(raiz=None):
    """Dice si hace falta correr las pruebas, y **por qué hace falta**.

    **Reclama, no corre.** Las 650 tardan 9,6 minutos y este repositorio hace 16
    commits por día: correrlas en cada uno costaría 39 horas cada dos semanas.
    Un peaje así se apaga en una tarde, y entonces quedamos peor que hoy — con
    un control que figura como puesto. Esto cuesta leer un archivo.

    **Los tres motivos se dicen distinto**, porque llevan a cosas distintas:
    nunca corrieron, la última dejó fallas, o hay trabajo que no vieron.
    """
    raiz = raiz or comun.RAIZ
    ruta = os.path.join(raiz, SELLO)
    sello = _sello(raiz)

    if sello is None:
        return [Hallazgo(AVISO, ruta, 0,
                         "las pruebas del estándar nunca corrieron en esta "
                         "copia — " + ORDEN)]

    cuando, fallas = sello
    if fallas:
        return [Hallazgo(AVISO, ruta, 0,
                         "la última corrida de las pruebas del estándar "
                         "(%s) dejó **%d falla(s)** — %s"
                         % (cuando, fallas, ORDEN))]

    commit = _ultimo_commit(raiz)
    if commit is None or os.path.getmtime(ruta) >= commit:
        return []
    return [Hallazgo(AVISO, ruta, 0,
                     "hay commits posteriores a la última corrida de las "
                     "pruebas del estándar (%s) — %s" % (cuando, ORDEN))]


def plataforma_de(raiz=None):
    """La carpeta de la plataforma, exista o no."""
    return os.path.join(raiz or comun.RAIZ, PLATAFORMA)


# Lo que su corredor imprime al terminar: `Ran 187 tests in 28.638s`.
_CUANTAS = re.compile(r"^Ran (\d+) tests? in ", re.MULTILINE)
_FALLAS = re.compile(r"FAILED \(([^)]*)\)")
_CUENTA = re.compile(r"(failures|errors)=(\d+)")


def correr_la_plataforma(raiz=None):
    """`(hallazgos, cuantas)` de la otra batería de este repositorio.

    **Se le pide por su punto de entrada**, que es como se corre de verdad: su
    marco arma la base de prueba, descubre las aplicaciones y las corre. Cargar
    sus archivos a mano desde acá daría un número que nadie más obtiene.

    **Si no está, se dice.** Un proyecto que hereda el estándar no tiene
    plataforma, y saltársela en silencio es lo mismo que no mirarla: el aviso
    distingue «no hay» de «está bien».
    """
    carpeta = plataforma_de(raiz)
    entrada = os.path.join(carpeta, "manage.py")
    if not os.path.isfile(entrada):
        return ([Hallazgo(AVISO, carpeta, 0,
                          "no hay plataforma en este repositorio: no se corrió "
                          "su batería. No es lo mismo que estar en verde")], 0)

    try:
        corrida = subprocess.run(
            [sys.executable, "manage.py", "test", "--verbosity", "1"],
            cwd=carpeta, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=900)
    except (OSError, subprocess.SubprocessError) as falla:
        return ([Hallazgo(FALLA, entrada, 0,
                          "no se pudo correr la batería de la plataforma: %s"
                          % falla)], 0)

    salida = (corrida.stdout or "") + (corrida.stderr or "")
    m = _CUANTAS.search(salida)
    cuantas = int(m.group(1)) if m else 0

    hallazgos = []
    # **Cero pruebas es rojo también acá.** Es la misma regla, y por el mismo
    # motivo: una corrida que no corrió nada y termina en verde es un silencio
    # que se lee como éxito.
    if cuantas == 0:
        hallazgos.append(Hallazgo(
            FALLA, carpeta, 0,
            "la batería de la plataforma corrió **0 pruebas** — cero no es "
            "verde: quiere decir que no se comprobó nada (08·T5)"))
        return (hallazgos, 0)

    roto = _FALLAS.search(salida)
    if roto or corrida.returncode != 0:
        detalle = dict((c, int(n)) for c, n in
                       _CUENTA.findall(roto.group(1) if roto else ""))
        hallazgos.append(Hallazgo(
            FALLA, carpeta, 0,
            "la batería de la plataforma falló: %d prueba(s) · %d falla(s) · "
            "%d error(es) — se corre con `python manage.py test` desde "
            "`plataforma/`"
            % (cuantas, detalle.get("failures", 0), detalle.get("errors", 0))))
    return (hallazgos, cuantas)


def validar(raiz=None, solo=None):
    """`[Hallazgo]`, más el resumen como aviso. Para `validar.py`."""
    resultado, hallazgos, corridos = correr(raiz, solo)

    # **La otra batería entra solo en la corrida entera.** Pedir un subconjunto
    # es lo que hace cumplible `02·F5`, y arrastrar 187 pruebas ajenas a una
    # fase que toca dos archivos convertiría esa orden en un peaje.
    de_la_plataforma, cuantas_alla = ([], 0)
    if not solo:
        de_la_plataforma, cuantas_alla = correr_la_plataforma(raiz)
        hallazgos += de_la_plataforma

    if resultado is not None:
        # **Se sella la corrida entera, con su resultado.** Un subconjunto no
        # se sella: diría «esto se comprobó» sobre lo que no se miró, que es el
        # defecto del que sale toda esta pieza.
        if not solo:
            sellar(raiz, len([h for h in hallazgos
                              if h.severidad == FALLA]))
        cuenta = ("%d prueba(s) en %d archivo(s) · %d falla(s) · %d error(es)"
                  % (resultado.testsRun, len(corridos),
                     len(resultado.failures), len(resultado.errors)))
        if not solo:
            # **Las dos baterías se dicen juntas y se cuentan aparte.** Sumarlas
            # en un solo número escondría cuál de las dos se cayó.
            cuenta += " · y %d prueba(s) de la plataforma" % cuantas_alla
        hallazgos.append(Hallazgo(AVISO, carpeta_de(raiz), 0, cuenta))
    return hallazgos


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("corredor")
