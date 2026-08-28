# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-019, corre las pruebas, y restaura con copia.

Lo aprendido rompiendo, aplicado aca:

- **Se restaura con copia, no con git**, y en `try/finally` (S-060).
- **La salida se limpia antes de imprimirla.**
- **La guardia acepta `OK` y `OK (...)`**, y sigue rechazando `OK:`, que es la
  linea de los validadores. Las dos formas del defecto pasaron el mismo dia.
- **Este guion NO se corre por una tuberia.**

Los cinco sabotajes atacan lo que importa: que NO escriba donde no debe, y que
un fallo suyo no toque el commit.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu019a")
ARCHIVOS = ["validadores/estacion_commit.py", "validadores/hook_estacion.py",
            "validadores/instalar.py"]

SABOTAJES = [
    ("1: inventa la fila donde no hay tabla",
     "validadores/estacion_commit.py",
     '''    if not tiene_fila_de_estacion(texto) or ya_esta_marcada(texto):
        return None''',
     '''    if ya_esta_marcada(texto):
        return None
    if not tiene_fila_de_estacion(texto):
        return texto + "\\n| 12 | Commit | autorizado | %s |\\n" % hash_corto'''),

    ("2: pisa el hash ya puesto",
     "validadores/estacion_commit.py",
     '''    if not tiene_fila_de_estacion(texto) or ya_esta_marcada(texto):''',
     '''    if not tiene_fila_de_estacion(texto):'''),

    ("3: marca aunque el cierre no este en git",
     "validadores/estacion_commit.py",
     '''        if not os.path.isfile(estado) or not cerrada_en_git(cierre):''',
     '''        if not os.path.isfile(estado):'''),

    ("4: el enganche deja de callar y revienta",
     "validadores/hook_estacion.py",
     '''    except Exception:       # noqa: BLE001
        # Deliberado y declarado: el commit ya está hecho. Nada que pase acá
        # justifica alarmar a quien acaba de commitear bien.
        sys.exit(0)''',
'''    except Exception:       # noqa: BLE001
        raise'''),

    ("5: el instalador deja de colgar el enganche",
     "validadores/instalar.py",
     '''    ("post-commit", PLANTILLA_POST_COMMIT,''',
     '''    ("no-se-cuelga", PLANTILLA_POST_COMMIT,'''),
]


def guardar_copias():
    if os.path.isdir(COPIAS):
        shutil.rmtree(COPIAS)
    os.makedirs(COPIAS)
    for archivo in ARCHIVOS:
        shutil.copy2(os.path.join(RAIZ, archivo),
                     os.path.join(COPIAS, archivo.replace("/", "_")))


def restaurar(archivo):
    shutil.copy2(os.path.join(COPIAS, archivo.replace("/", "_")),
                 os.path.join(RAIZ, archivo))


def correr(completa=False):
    orden = ([sys.executable, "pruebas.py"] if completa else
             [sys.executable, "-m", "unittest",
              "pruebas.ElHashDelCommitSeAnotaSolo"])
    salida = subprocess.run(orden, capture_output=True, text=True,
                            encoding="utf-8", errors="replace",
                            cwd=os.path.join(RAIZ, "validadores"))
    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    limpio = "\n".join("    " + l for l in lineas)
    return limpio.encode("ascii", "replace").decode("ascii")


guardar_copias()
print("== cinco sabotajes ==")
print()
for titulo, archivo, viejo, nuevo in SABOTAJES:
    completa = os.path.join(RAIZ, archivo)
    t = io.open(completa, encoding="utf-8").read()
    print("--- %s ---" % titulo)
    if viejo not in t:
        print("    NO SE PUDO SABOTEAR: el texto cambio. Revisar el guion.")
        print()
        continue
    io.open(completa, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))
    try:
        print(correr())
    finally:
        restaurar(archivo)
    print()

print("--- rastros fuera del repositorio ---")
print("    uno, declarado: la copia de restauracion, en la carpeta temporal.")
print("    El enganche de la HU-018 lo avisa.")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
lineas = [l.strip() for l in final.splitlines()]
limpia = any(l == "OK" or l.startswith("OK (") for l in lineas)
if (not limpia or not any(l.startswith("Ran ") for l in lineas)
        or any(l.startswith("Ran 0 ") for l in lineas)):
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
