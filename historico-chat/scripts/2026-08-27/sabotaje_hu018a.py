# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-018, corre las pruebas, y restaura con copia.

Lo aprendido rompiendo, aplicado aca:

- **Se restaura con copia, no con git.**
- **La restauracion va en `try/finally`**: el guion de la HU-022 se cayo entre
  romper y restaurar, y dejo el repositorio con el sabotaje puesto (S-060).
- **La salida se limpia antes de imprimirla**, que fue lo que lo tumbo.
- **La guardia final exige la linea `OK` sola**, no que «OK» aparezca en el
  texto: los validadores escriben «OK: sin incumplimientos.».
- **Este guion NO se corre por una tuberia**: el codigo de salida que se leeria
  seria el del ultimo eslabon.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu018a")
ARCHIVOS = ["validadores/rutas_fuera.py", "validadores/instalar.py"]

SABOTAJES = [
    ("1: se compara por prefijo y la carpeta hermana pasa por dentro",
     "validadores/rutas_fuera.py",
     '''    return suya[:len(casa)] == casa''',
     '''    return os.sep.join(suya).startswith(os.sep.join(casa))'''),

    ("2: se compara el texto crudo, sin resolver la ruta",
     "validadores/rutas_fuera.py",
     '''        suya = _partes(os.path.realpath(os.path.abspath(ruta)))
        casa = _partes(os.path.realpath(os.path.abspath(proyecto)))''',
     '''        suya = _partes(ruta)
        casa = _partes(proyecto)'''),

    ("3: ante la duda se acusa en vez de callar",
     "validadores/rutas_fuera.py",
     '''    except (OSError, ValueError, TypeError):
        return True''',
     '''    except (OSError, ValueError, TypeError):
        return False'''),

    ("4: el aviso dice que esta mal pero no donde iba",
     "validadores/rutas_fuera.py",
     '''    return (
        "[AVISO] se escribió fuera del proyecto: %s — los guiones de apoyo van "
        "en `%s`, y se quedan ahí versionados (`04·S9`, EP-005·HU-018). "
        "Leer fuera sí vale; escribir, no." % (ruta, DESTINO))''',
'''    return "[AVISO] se escribio fuera del proyecto: %s" % ruta'''),

    ("5: el enganche existe pero nadie lo cuelga",
     "validadores/instalar.py",
     '''    ("PostToolUse", "Write|Edit", "hook_rutas.py",
     "Mirando dónde quedó lo que se escribió...", ""),''',
     ''''''),
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
              "pruebas.ElGuionSeQuedaEnElRepositorio"])
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
print("    Es lo que la propia regla S18 viene a evitar, y queda anotado.")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
lineas = [l.strip() for l in final.splitlines()]
if ("OK" not in lineas or not any(l.startswith("Ran ") for l in lineas)
        or any(l.startswith("Ran 0 ") for l in lineas)):
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
