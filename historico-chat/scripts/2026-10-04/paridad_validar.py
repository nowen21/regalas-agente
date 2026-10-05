# -*- coding: utf-8 -*-
"""Compara `validadores/validar.py` viejo (el de `HEAD`, que llamaba a los
módulos de `validadores/`) con el nuevo (`core/herramientas/validar.py`, por
la puerta que quedó en `validadores/validar.py`), subcomando por subcomando
(sesión del 2026-10-04, análisis 1 del pendiente 116).

    python paridad_validar.py [--partes estandar,fases,...] [--raices R1,R2] [--hilos N] [--rapido]

Cada subcomando se corre dos veces, en procesos aparte y parados en la raíz del
estándar: el viejo, sacado de `git show HEAD:validadores/validar.py` a una
carpeta temporal y corrido contra los módulos viejos que siguen en disco, y el
nuevo. Se comparan la salida estándar, la de errores y el código de salida.

Se dejan fuera los que escriben, salen a la red o tardan: `linter`, `suite`,
`internas`, `audit`, `temas --aplicar`, `indices --aplicar`, `pendientes
--indice` y `traza --escribir`. `todo` se compara al final. **No escribe en
ningún proyecto**: el conteo por regla que `todo` anota se apaga en los dos
lados, y al terminar se comprueba con `git status` que ningún proyecto cambió.
"""
import argparse
import concurrent.futures
import difflib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VALIDADORES = os.path.join(RAIZ, "validadores")
CIMIENTO = os.path.join(RAIZ, "proyectos", "cimiento")
PUERTA = os.path.join(VALIDADORES, "validar.py")
RAICES = ["C:/Ing. Jose/ia/agente", "c:/wamp64/www/proyectos/personales/agro-system"]
LINEAS_DE_DIFERENCIA = 40

VIEJO = r'''
import runpy, sys
sys.path.insert(0, %r)
import conteo
conteo.anotar = lambda *a, **k: None
if %r:
    import reaperturas
    reaperturas.reaperturas = lambda *a, **k: []
sys.argv = [%r] + sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
'''

NUEVO = r'''
import runpy, sys
sys.path.insert(0, %r)
from core.validadores.conteo import ConteoPorRegla
ConteoPorRegla.anotar = lambda self, *a, **k: None
if %r:
    from core.validadores.reaperturas import Reaperturas
    Reaperturas.reaperturas = lambda self: []
sys.argv = [%r] + sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
'''

# Lo único que cambia por la hora: la fecha y la hora de una corrida.
_HORA = re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(:\d{2})?")


def normalizar(texto):
    return _HORA.sub("<hora>", texto.replace("\r\n", "\n"))


def correr(codigo, args):
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, "-c", codigo] + list(args), cwd=RAIZ, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=entorno, timeout=1800)
    return normalizar(r.stdout), normalizar(r.stderr), r.returncode


def preparar(tmp):
    """El viejo, la transcripción de `traza` y los mensajes de `commit`, en `tmp`."""
    viejo = os.path.join(tmp, "validar.py")
    fuente = subprocess.run(["git", "show", "HEAD:validadores/validar.py"], cwd=RAIZ, capture_output=True,
                            check=True).stdout
    with open(viejo, "wb") as f:
        f.write(fuente)
    base = "2026-08-20T10:00:%02d.000Z"
    lineas = []
    for id_, nombre, entrada, inicio, fin, error in (("t1", "Read", {"file_path": "a.md"}, 0, 2, False),
                                                     ("t2", "Bash", {"command": "python x.py"}, 10, 15, True)):
        lineas.append({"type": "assistant", "timestamp": base % inicio, "message": {"content": [
            {"type": "tool_use", "id": id_, "name": nombre, "input": entrada}]}})
        lineas.append({"type": "user", "timestamp": base % fin, "message": {"content": [
            {"type": "tool_result", "tool_use_id": id_, "is_error": error, "content": "x"}]}})
    traza = os.path.join(tmp, "abc.jsonl")
    with io.open(traza, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(json.dumps(l) for l in lineas) + "\n")
    mensajes = []
    for nombre, texto in (("malo.txt", "arreglos.\n"),
                          ("bueno.txt", "feat(x): el validador dice qué miró\n\nPorque un cero sin alcance engaña.\n")):
        ruta = os.path.join(tmp, nombre)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        mensajes.append(ruta)
    return viejo, traza, mensajes


def un_documento(raiz):
    """Un plan de trabajo de la raíz, para `plantilla`."""
    for actual, carpetas, archivos in os.walk(os.path.join(raiz, "documentacion", "epicas")):
        carpetas.sort()
        if "plan_trabajo.md" in archivos:
            return os.path.join(actual, "plan_trabajo.md")
    return None


def casos(traza, mensajes):
    """`[(parte, args)]`: cada subcomando que solo lee, en cada raíz."""
    salida = [("ayuda", ["--help"]), ("ayuda", []), ("ayuda", ["fases", "--help"]),
              ("traza", ["traza", traza]), ("traza", ["traza", os.path.join(RAIZ, "no-existe.jsonl")]),
              ("plantilla", ["plantilla", os.path.join(RAIZ, "README.md")]),
              ("plantilla", ["plantilla", os.path.join(RAIZ, "no-existe.md")]),
              ("commit", ["commit", "--revision", "HEAD"]),
              ("plan", ["plan", "--raiz", RAICES[0], "--rango", "HEAD~3..HEAD"])]
    salida += [("commit", ["commit", "--archivo", m]) for m in mensajes]
    simples = ["estandar", "fases", "pendientes", "trazabilidad", "versionado", "metareglas", "ejecutable",
               "reaperturas", "indices", "sesiones", "marcas", "expediente", "vigencia", "acciones", "amarre",
               "tareas", "plan", "temas", "analisis", "origen", "sitio", "inmutable", "brevedad", "estructura",
               "entidades", "cruces", "secretos", "dependencias", "rama", "migraciones", "errores",
               "rendimiento", "esquema", "flujo", "seguridad", "calidad", "ci", "aislamiento", "version",
               "checklist", "versiones"]
    for raiz in RAICES:
        salida += [(s, [s, "--raiz", raiz]) for s in simples]
        salida += [(s, [s, "--raiz", raiz, "--preparados"]) for s in ("versionado", "marcas", "plan")]
        salida.append(("metareglas", ["metareglas", "--raiz", RAICES[0], "--catalogo", raiz]))
        documento = un_documento(raiz)
        if documento:
            salida.append(("plantilla", ["plantilla", documento]))
    return salida


def estado_git(raiz):
    return subprocess.run(["git", "status", "--porcelain"], cwd=raiz, capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


# `--rapido` · Recorrer la historia de cada fase tarda casi siete minutos en
# este repositorio, y `todo` la recorre otra vez. Con `--rapido` las dos
# versiones dan la lista de reaperturas vacía dentro de `todo`; la lista misma
# se compara aparte, con `--partes reaperturas`.
RAPIDO = []


def comparar(viejo, args):
    rapido = bool(RAPIDO) and args[:1] == ["todo"]
    a = correr(VIEJO % (VALIDADORES, rapido, viejo), args)
    b = correr(NUEVO % (CIMIENTO, rapido, PUERTA), args)
    return a, b


def resumen_de_todo(salida):
    """Los títulos de cada comprobación y las líneas del final: la forma de la corrida."""
    lineas = salida.splitlines()
    fin = next((i for i, l in enumerate(lineas) if l.startswith("== Corrida completa")), len(lineas))
    return [l for l in lineas[:fin] if l.startswith("== ")] + lineas[fin:]


def mostrar_diferencia(a, b):
    for nombre, x, y in (("salida", a[0], b[0]), ("errores", a[1], b[1])):
        if x != y:
            print("     %s:" % nombre)
            cambios = [l for l in difflib.unified_diff(x.splitlines(), y.splitlines(), "viejo", "nuevo",
                                                       n=0, lineterm="") if l[:1] in "+-" and l[:3] not in ("---", "+++")]
            for linea in cambios[:LINEAS_DE_DIFERENCIA]:
                print("       " + linea[:300])
            if len(cambios) > LINEAS_DE_DIFERENCIA:
                print("       (y %d línea(s) más)" % (len(cambios) - LINEAS_DE_DIFERENCIA))
    if a[2] != b[2]:
        print("     código: viejo %s · nuevo %s" % (a[2], b[2]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--partes", help="subcomandos a comparar, separados por coma; `todo` incluido")
    p.add_argument("--raices", help="raíces, separadas por coma")
    p.add_argument("--hilos", type=int, default=6)
    p.add_argument("--rapido", action="store_true", help="dentro de `todo`, sin recorrer las reaperturas")
    a = p.parse_args()
    if a.rapido:
        RAPIDO.append(True)
    if a.raices:
        RAICES[:] = a.raices.split(",")
    partes = set(a.partes.split(",")) if a.partes else None

    antes = {r: estado_git(r) for r in RAICES}
    tmp = tempfile.mkdtemp(prefix="paridad-validar-")
    viejo, traza, mensajes = preparar(tmp)
    lista = [(parte, args) for parte, args in casos(traza, mensajes) if partes is None or parte in partes]
    if partes is None or "todo" in partes:
        lista += [("todo", ["todo", "--raiz", r]) for r in RAICES]

    iguales, distintos = 0, []
    inicio = time.time()
    with concurrent.futures.ThreadPoolExecutor(a.hilos) as hilos:
        futuros = [(parte, args, hilos.submit(comparar, viejo, args)) for parte, args in lista]
        for parte, args, futuro in futuros:
            x, y = futuro.result()
            if x != y:
                # Dos `git` a la vez pueden tropezar con el candado del índice:
                # lo distinto se corre otra vez, solo.
                x, y = comparar(viejo, args)
            igual = x == y
            iguales += igual
            print("%-8s %-60s código %s" % ("IGUAL" if igual else "DISTINTO", " ".join(args)[:60], x[2]))
            if not igual:
                distintos.append(args)
                mostrar_diferencia(x, y)
                if args[0] == "todo":
                    forma = resumen_de_todo(x[0]) == resumen_de_todo(y[0])
                    print("     títulos y resumen final: %s" % ("IGUALES" if forma else "DISTINTOS"))
                    if not forma:
                        for l in difflib.unified_diff(resumen_de_todo(x[0]), resumen_de_todo(y[0]), n=0,
                                                      lineterm=""):
                            print("       " + l[:300])

    cambiados = [r for r in RAICES if estado_git(r) != antes[r]]
    print("\n%d casos · %d iguales · %d distintos · %.0f s" % (len(lista), iguales, len(distintos),
                                                             time.time() - inicio))
    if cambiados:
        print("OJO: cambió el `git status` de: " + ", ".join(cambiados))
    print("PARIDAD COMPLETA" if not distintos else "HAY DIFERENCIAS")
    return 0 if not distintos else 1


if __name__ == "__main__":
    sys.exit(main())
