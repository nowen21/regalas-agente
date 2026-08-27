# -*- coding: utf-8 -*-
"""Sabotea la fase C de la HU-021, corre las pruebas, y restaura con copia.

Lo aprendido rompiendo, aplicado aca:

- **Se restaura con copia, no con git** (leccion de la fase B de otra HU): el
  archivo puede tener cambios sin guardar que un `checkout` se llevaria.
- **Se limpia despues de CADA sabotaje**, no al final, para que uno no
  contamine al siguiente (S-051).
- **Se declara lo que queda fuera del repositorio**: aca, nada. Los cuatro
  editan un solo archivo versionado.
- **Se cae si la corrida final reporta cero pruebas** (S-044): un guion que
  dice «suite completa OK» sin haber corrido nada ya paso una vez.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu021c")
ARCHIVO = "validadores/fases.py"

SABOTAJES = [
    ("1: el patron nuevo se cae de la cadena",
     '''            or _VEREDICTO_TITULO_SOLO.search(texto))''',
     '''            or None)'''),

    ("2: el titulo se afloja y admite «por criterio»",
     '''    r"^##\\s+\\d+\\.?\\s*Veredicto\\s*$\\n+\\**(No cumple|Cumple)",''',
     '''    r"^##\\s+\\d+\\.?\\s*Veredicto[^\\n]*\\n+\\**(No cumple|Cumple)",'''),

    ("3: se reemplaza en vez de sumar, y se pierden las dos formas viejas",
     '''    dice = (_VEREDICTO.search(texto)
            or _VEREDICTO_BAJO_TITULO.search(texto)
            or _VEREDICTO_TITULO_SOLO.search(texto))''',
     '''    dice = _VEREDICTO_TITULO_SOLO.search(texto)'''),

    ("4: la palabra ya no tiene que ir pegada al encabezado",
     '''    r"^##\\s+\\d+\\.?\\s*Veredicto\\s*$\\n+\\**(No cumple|Cumple)",''',
     '''    r"^##\\s+\\d+\\.?\\s*Veredicto\\s*$[\\s\\S]*?\\**(No cumple|Cumple)",'''),
]


def guardar_copia():
    if os.path.isdir(COPIAS):
        shutil.rmtree(COPIAS)
    os.makedirs(COPIAS)
    shutil.copy2(os.path.join(RAIZ, ARCHIVO),
                 os.path.join(COPIAS, ARCHIVO.replace("/", "_")))


def restaurar():
    shutil.copy2(os.path.join(COPIAS, ARCHIVO.replace("/", "_")),
                 os.path.join(RAIZ, ARCHIVO))


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


guardar_copia()
print("== cuatro sabotajes ==")
print()
completa = os.path.join(RAIZ, ARCHIVO)
for titulo, viejo, nuevo in SABOTAJES:
    t = io.open(completa, encoding="utf-8").read()
    print("--- %s ---" % titulo)
    if viejo not in t:
        print("    NO SE PUDO SABOTEAR: el texto cambio. Revisar el guion.")
        print()
        continue
    io.open(completa, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))
    print(correr())
    restaurar()
    print()

print("--- rastros fuera del archivo saboteado ---")
print("    ninguno: los cuatro editan un archivo versionado, restaurado con copia")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
# `"OK" in final` no alcanza: la salida de los validadores trae
# «OK: sin incumplimientos.», asi que el guion daria por buena una corrida
# con fallas. Se exige la linea que unittest escribe sola: exactamente `OK`.
lineas = [l.strip() for l in final.splitlines()]
if "OK" not in lineas or not any(l.startswith("Ran ") for l in lineas)         or any(l.startswith("Ran 0 ") for l in lineas):
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
