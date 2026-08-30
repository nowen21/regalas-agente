# -*- coding: utf-8 -*-
"""Mide si los cinco rojos con fase posterior ya se cumplen hoy.

Son las cinco historias terminadas que arrastran un «No cumple» y que tienen
una fase posterior que **no declaro** el reemplazo (`EP-004·HU-023`). El script
no lee documentos: **ejecuta la comprobacion del criterio que quedo en rojo** y
dice que salio.

**El criterio de suspension va adentro.** La fase de cierre de una historia solo
se escribe si su medicion sale CUMPLE. La que salga NO CUMPLE no se cierra: se
queda en rojo, que es lo que es.

**Se corre antes de escribir ninguna fase**, porque abrir la carpeta ya mueve el
numero.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import version as V                                          # noqa: E402
from comun import FALLA, AVISO                               # noqa: E402

CLAUDE = u"# Proyecto de prueba\n\n- **Version del estandar adoptada:** `%s`\n"


def _proyecto_temporal(numero):
    carpeta = tempfile.mkdtemp(prefix="medir-rojo-")
    with io.open(os.path.join(carpeta, "CLAUDE.md"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(CLAUDE % numero)
    return carpeta


def ep002_hu003():
    """CA-02 · Una version que no existe se detecta.

    En rojo el 2026-08-22: `99.9.9` pasaba en silencio y, por ser mayor que la
    vigente, **apagaba el aviso de desfase**.
    """
    carpeta = _proyecto_temporal("99.9.9")
    try:
        hallazgos = V.validar(carpeta)
        fallas = [h for h in hallazgos if h.severidad == FALLA]
        return (bool(fallas),
                fallas[0].mensaje if fallas else "sigue pasando en silencio")
    finally:
        shutil.rmtree(carpeta, ignore_errors=True)


def ep002_hu004():
    """CA-01 · El proyecto atrasado recibe el aviso al abrir sesion.

    En rojo el 2026-08-22: el aviso existia, pero **nadie lo entregaba al
    abrir**. Se mide en dos mitades, y hacen falta las dos: que el aviso salga,
    y que el camino de la apertura pase por el.
    """
    carpeta = _proyecto_temporal("1.0.0")
    try:
        avisos = [h for h in V.validar(carpeta)
                  if h.severidad == AVISO and "el estandar va en" in
                  h.mensaje.replace("estándar", "estandar")]
        sale = bool(avisos)
    finally:
        shutil.rmtree(carpeta, ignore_errors=True)

    def _tiene(ruta, aguja):
        with io.open(os.path.join(RAIZ, ruta), encoding="utf-8") as f:
            return aguja in f.read()

    enganchado = (_tiene("validadores/sesion.py", "version.validar(proyecto)")
                  and _tiene("adaptadores/claude-code/hook_sesion.py",
                             "sesion.revisar("))
    if not sale:
        return (False, "el aviso de desfase no sale")
    if not enganchado:
        return (False, "el aviso sale, pero la apertura no pasa por el")
    return (True, "sale, y `hook_sesion` -> `sesion.revisar` -> `version.validar`")


def ep004_hu003():
    """Transversal de errores · Un `.md` ilegible no tumba la corrida.

    En rojo el 2026-08-17: un archivo que no se podia decodificar terminaba la
    corrida con un volcado de Python. **No basta con que no se caiga**: tiene que
    seguir contando lo que si pudo leer, o «no se cayo» seria «no miro nada».
    """
    carpeta = tempfile.mkdtemp(prefix="medir-rojo-")
    try:
        with open(os.path.join(carpeta, "ilegible.md"), "wb") as f:
            f.write(b"# Roto\n\n\xff\xfe\x00\x80\x81 bytes que no son UTF-8\n")
        with io.open(os.path.join(carpeta, "con-marca.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(u"# Con marca\n\nUna frase — con raya larga — en prosa.\n")

        corrida = subprocess.Popen(
            [sys.executable, os.path.join(RAIZ, "validadores", "marcas.py"),
             "--raiz", carpeta],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        salida = corrida.communicate()[0].decode("utf-8", "replace")
    finally:
        shutil.rmtree(carpeta, ignore_errors=True)

    if corrida.returncode != 0 or "Traceback" in salida:
        return (False, "la corrida se cae con el archivo ilegible")
    if "raya larga" not in salida:
        return (False, "no se cae, pero deja de contar lo que si podia leer")
    return (True, "termina en 0, sin volcado, y cuenta las 2 marcas del legible")


def ep005_hu003():
    """CA-03 · El hallazgo grave detiene, y el resto avisa.

    En rojo el 2026-08-17: **todo avisaba**. Se mide corriendo el enganche de
    escritura dos veces, y las dos respuestas tienen que ser distintas.
    """
    def _corrida(cuerpo):
        carpeta = tempfile.mkdtemp(prefix="medir-rojo-")
        try:
            ruta = os.path.join(carpeta, "doc.md")
            with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
                f.write(cuerpo)
            entrada = json.dumps({"session_id": "medicion",
                                  "tool_input": {"file_path": ruta}})
            enganche = subprocess.Popen(
                [sys.executable,
                 os.path.join(RAIZ, "adaptadores", "claude-code", "hook_md.py"),
                 "--raiz", carpeta],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            enganche.communicate(entrada.encode("utf-8"))
            return enganche.returncode
        finally:
            shutil.rmtree(carpeta, ignore_errors=True)

    grave = _corrida(u"# Doc\n\nUn enlace roto: [no existe](no-existe.md)\n")
    sano = _corrida(u"# Doc\n\nTexto sin enlaces.\n")

    if grave != 2:
        return (False, "el hallazgo grave no detiene: devolvio %d" % grave)
    if sano != 0:
        return (False, "lo sano tambien detiene: devolvio %d" % sano)
    return (True, "el enlace roto devuelve 2 y el documento sano devuelve 0")


def ep005_hu008():
    """Criterio de salida · La comprobacion en una sesion real.

    En rojo el 2026-08-22 por lo unico que un programa no puede firmar solo:
    faltaba correrlo en una sesion de verdad. Este script mide **lo que si es
    medible** (que el enganche este colgado y que renombrar deje el indice sin
    enlaces rotos) y deja dicho que la mitad manual la atestigua la sesion
    `2026-08-28-plantilla-manual-instalacion`.
    """
    ajustes = os.path.join(RAIZ, ".claude", "settings.json")
    if not os.path.isfile(ajustes):
        return (False, "no hay .claude/settings.json donde mirar el enganche")
    with io.open(ajustes, encoding="utf-8") as f:
        colgado = "hook_resumen" in f.read()
    if not colgado:
        return (False, "el enganche del resumen no esta colgado")

    dia = os.path.join(RAIZ, "historico-chat", "resumenes", "2026-08-28")
    resumen = os.path.join(dia, "plantilla-manual-instalacion.md")
    indice = os.path.join(dia, "README.md")
    if not (os.path.isfile(resumen) and os.path.isfile(indice)):
        return (False, "la sesion real no dejo resumen ni indice")
    with io.open(indice, encoding="utf-8") as f:
        apunta = "plantilla-manual-instalacion.md" in f.read()
    if not apunta:
        return (False, "el indice no apunta al resumen que quedo")
    return (True, "colgado, y la sesion real dejo resumen e indice coherentes "
                  "tras renombrar")


LOS_CINCO = (
    ("EP-002 / HU-003 · version adoptada por el proyecto",
     "A-EP-002-HU-003-retrodocumentar-la-version-adoptada",
     "CA-02 · una version que no existe se detecta", ep002_hu003),
    ("EP-002 / HU-004 · aviso al quedar atras",
     "A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase",
     "CA-01 · el aviso llega al abrir sesion", ep002_hu004),
    ("EP-004 / HU-003 · formato del hallazgo",
     "A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo",
     "transversal de errores · el ilegible no tumba la corrida", ep004_hu003),
    ("EP-005 / HU-003 · disparo al escribir un archivo",
     "A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir",
     "CA-03 · el grave detiene, el resto avisa", ep005_hu003),
    ("EP-005 / HU-008 · enganche del resumen",
     "A-EP-005-HU-008-enganche-del-resumen",
     "criterio de salida · corrida en una sesion real", ep005_hu008),
)


def main():
    print("MEDICION DE LOS CINCO ROJOS CON FASE POSTERIOR")
    print("Se ejecuta el criterio, no se lee el documento.\n")
    cerrables, siguen = [], []
    for titulo, roja, criterio, medir in LOS_CINCO:
        try:
            cumple, evidencia = medir()
        except Exception as e:                    # una medicion rota no afirma
            cumple, evidencia = False, "la medicion fallo: %r" % (e,)
        print("%-12s %s" % ("CUMPLE" if cumple else "NO CUMPLE", titulo))
        print("             roja:      %s" % roja)
        print("             criterio:  %s" % criterio)
        print("             evidencia: %s\n" % evidencia)
        (cerrables if cumple else siguen).append(titulo)

    print("-" * 72)
    print("Se pueden cerrar declarando: %d" % len(cerrables))
    print("Siguen en rojo:              %d" % len(siguen))
    for t in siguen:
        print("  - %s" % t)
    return 0 if not siguen else 1


if __name__ == "__main__":
    sys.exit(main())
