# -*- coding: utf-8 -*-
"""Cuantos de los 67 archivos de `validadores/tests/` corren, y con que resultado.

La orden que el registro de cambios documenta ---`python -m unittest discover -s
validadores/tests`--- **no funciona**: la carpeta no tiene `__init__.py`, asi que
el descubrimiento se cae antes de correr nada. La pregunta es si los archivos
estan vivos o si es una carpeta que nadie corre hace semanas.

Se corre cada archivo por separado, con `validadores/` en el camino, que es como
lo hace quien lo corre a mano.
"""
import os
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
CARPETA = os.path.join(RAIZ, "validadores", "tests")

entorno = dict(os.environ)
entorno["PYTHONPATH"] = os.path.join(RAIZ, "validadores")

verdes = rojos = mudos = 0
detalle = []
archivos = sorted(n for n in os.listdir(CARPETA) if n.endswith(".py"))
for nombre in archivos:
    r = subprocess.run([sys.executable, os.path.join(CARPETA, nombre)],
                       cwd=os.path.join(RAIZ, "validadores"), env=entorno,
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=300)
    texto = ((r.stdout or "") + (r.stderr or "")).encode("ascii", "replace").decode("ascii")
    ultima = [l.strip() for l in texto.splitlines() if l.strip()]
    resumen = ultima[-1] if ultima else "(sin salida)"
    if r.returncode == 0 and "Ran 0 tests" not in texto:
        verdes += 1
    elif "Ran 0 tests" in texto or not ultima:
        mudos += 1
        detalle.append(("MUDO ", nombre, resumen))
    else:
        rojos += 1
        detalle.append(("ROJO ", nombre, resumen))

for marca, nombre, resumen in detalle:
    print("%s %-58s %s" % (marca, nombre, resumen[:60]))

print("")
print("De %d archivos: %d en verde, %d en rojo, %d sin pruebas." %
      (len(archivos), verdes, rojos, mudos))
