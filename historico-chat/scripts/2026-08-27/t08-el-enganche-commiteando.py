# -*- coding: utf-8 -*-
"""T-08: el enganche corriendo de verdad, con commits reales.

No basta con probar la funcion: la leccion de EP-002-HU-004 es que una
funcionalidad construida y probada puede no estar colgada de nada. Aca se
instala el enganche y se commitea.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

ESTANDAR = r"c:\Ing. Jose\ia\agente"
TMP = tempfile.mkdtemp(prefix="t08_")


def limpio(x):
    """La consola de Windows no sabe escribir todo lo que sale de los archivos.

    Un `print` que revienta a mitad deja el repositorio de prueba sin borrar y
    la medicion sin terminar. Es la leccion de S-060, aplicada aca.
    """
    return str(x).encode("ascii", "replace").decode("ascii")


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=TMP, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def escribir(rel, texto):
    ruta = os.path.join(TMP, *rel.split("/"))
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    return ruta


TABLA = ("# Estado de fase\n\n"
         "| # | Estacion | Puerta | Estado |\n|---|---|---|---|\n"
         "| 11 | Cierre | docs al dia | OK |\n"
         "| 12 | Commit | autorizado |  |\n"
         "| 13 | Publicacion | autorizado |  |\n")

git("init", "-q")
git("config", "user.name", "prueba")
git("config", "user.email", "prueba@local")
git("config", "core.hooksPath", ".githooks")

# El enganche, tal como lo escribe el instalador.
gancho = escribir(".githooks/post-commit",
                  '#!/bin/sh\n'
                  'python "%s/validadores/hook_estacion.py" --raiz "$(pwd)" || true\n'
                  'exit 0\n' % ESTANDAR.replace("\\", "/"))
os.chmod(gancho, 0o755)

BASE = "documentacion/epicas/EP-001-e/HU-001-una"
# 1. Una fase CON fila y con su cierre escrito.
escribir(BASE + "/A-EP-001-HU-001-con-fila/estado-fase.md", TABLA)
escribir(BASE + "/A-EP-001-HU-001-con-fila/funcionalidad_implementada.md",
         "# cierre escrito\n")
# 2. Una fase SIN la fila: no se debe tocar.
SIN_FILA = "# Estado de fase\n\nEsta fase no tiene tabla de estaciones.\n"
escribir(BASE + "/B-EP-001-HU-001-sin-fila/estado-fase.md", SIN_FILA)
escribir(BASE + "/B-EP-001-HU-001-sin-fila/funcionalidad_implementada.md",
         "# cierre escrito\n")

git("add", "-A")
r = git("commit", "-m", "primer commit")
h1 = git("rev-parse", "--short", "HEAD").stdout.strip()

con = io.open(os.path.join(TMP, *(BASE + "/A-EP-001-HU-001-con-fila/estado-fase.md").split("/")),
              encoding="utf-8").read()
sin = io.open(os.path.join(TMP, *(BASE + "/B-EP-001-HU-001-sin-fila/estado-fase.md").split("/")),
              encoding="utf-8").read()

print("CP-001 - el hash se escribe solo")
print("   commit hecho:", r.returncode == 0, "| hash:", h1)
fila = [l for l in con.splitlines() if l.startswith("| 12 ")]
print("   la fila 12 quedo:", limpio(fila[0] if fila else "(no hay)"))
print("   trae el hash del commit:", h1 in con)
print()

print("CP-003 - la fase SIN fila no se toca")
print("   identica:", sin == SIN_FILA)
print()

print("CP-005 / estado del arbol")
print("   git status:", limpio(repr(git("status", "--porcelain").stdout.strip())))
print("   el commit sigue en el log:", h1 in git("log", "--oneline").stdout)
print()

print("CP-002 - no se pisa un hash ya puesto")
git("add", "-A")
git("commit", "-m", "segundo commit")
h2 = git("rev-parse", "--short", "HEAD").stdout.strip()
con2 = io.open(os.path.join(TMP, *(BASE + "/A-EP-001-HU-001-con-fila/estado-fase.md").split("/")),
               encoding="utf-8").read()
print("   segundo hash:", h2)
print("   el documento sigue con el PRIMERO:", h1 in con2, "| trae el segundo:", h2 in con2)
print()

print("CP-005 - el enganche roto no rompe el commit")
io.open(gancho, "w", encoding="utf-8", newline="\n").write(
    '#!/bin/sh\npython "no-existe-este-archivo.py" || true\nexit 0\n')
os.chmod(gancho, 0o755)
escribir(BASE + "/A-EP-001-HU-001-con-fila/otro.md", "# algo\n")
git("add", "-A")
r3 = git("commit", "-m", "con el enganche roto")
print("   commit hecho igual:", r3.returncode == 0)
print("   esta en el log:", len(git("log", "--oneline").stdout.strip().splitlines()), "commits")

shutil.rmtree(TMP, ignore_errors=True)
print()
print("   (repositorio de prueba borrado, sin rastros)")
