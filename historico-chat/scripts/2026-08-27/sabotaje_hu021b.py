# -*- coding: utf-8 -*-
"""Sabotea la fase B de la HU-021, corre las pruebas, y restaura con copia."""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu021b")

SABOTAJES = [
    ("1: la tercera forma vuelve a no leerse",
     "validadores/fases.py",
     '''    dice = _VEREDICTO.search(texto) or _VEREDICTO_BAJO_TITULO.search(texto)''',
     '''    dice = _VEREDICTO.search(texto)'''),

    ("2: el lector se afloja y no exige el encabezado",
     "validadores/fases.py",
     '''    r"^##\\s+\\d+\\.?\\s*Veredicto de la fase[^\\n]*\\n+\\**(No cumple|Cumple)",
    re.MULTILINE | re.IGNORECASE)''',
     '''    r"\\**(No cumple|Cumple)",
    re.MULTILINE | re.IGNORECASE)'''),

    ("3: se pierde la forma vieja al agregar la nueva",
     "validadores/fases.py",
     '''    dice = _VEREDICTO.search(texto) or _VEREDICTO_BAJO_TITULO.search(texto)''',
     '''    dice = _VEREDICTO_BAJO_TITULO.search(texto)'''),

    ("4: toma el primer grupo aunque este vacio",
     "validadores/fases.py",
     '''    palabra = next(g for g in dice.groups() if g)''',
     '''    palabra = dice.groups()[0] or "Cumple"'''),
]


def guardar_copias():
    if os.path.isdir(COPIAS):
        shutil.rmtree(COPIAS)
    os.makedirs(COPIAS)
    for archivo in {s[1] for s in SABOTAJES}:
        shutil.copy2(os.path.join(RAIZ, archivo),
                     os.path.join(COPIAS, archivo.replace("/", "_")))


def restaurar(archivo):
    shutil.copy2(os.path.join(COPIAS, archivo.replace("/", "_")),
                 os.path.join(RAIZ, archivo))


def correr(completa=False):
    orden = ([sys.executable, "pruebas.py"] if completa else
             [sys.executable, "-m", "unittest",
              "pruebas.LaCuentaMiraElVeredicto"])
    salida = subprocess.run(orden, capture_output=True, text=True,
                            encoding="utf-8", errors="replace",
                            cwd=os.path.join(RAIZ, "validadores"))
    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    return "\n".join("    " + l for l in lineas)


guardar_copias()
print("== cuatro sabotajes ==")
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
    print(correr())
    restaurar(archivo)
    print()

print("--- rastros fuera del archivo saboteado ---")
print("    ninguno: los cuatro editan un archivo que se restaura con copia")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
if "OK" not in final or "Ran 0 " in final:
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
