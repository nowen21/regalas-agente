# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-021, corre las pruebas, y restaura con copia."""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu021")

SABOTAJES = [
    ("1: lo ilegible se reparte entre las que cumplen",
     "validadores/fases.py",
     '''            if any(v is None for v in dichos):
                sin_veredicto += 1
            elif any(v == "No cumple" for v in dichos):''',
     '''            if False:
                sin_veredicto += 1
            elif any(v == "No cumple" for v in dichos):'''),

    ("2: basta una que cumpla, en vez de todas",
     "validadores/fases.py",
     '''            elif any(v == "No cumple" for v in dichos):''',
     '''            elif all(v == "No cumple" for v in dichos):'''),

    ("3: cuenta tambien las historias a medias",
     "validadores/fases.py",
     '''            if not (fases and all(
                    all(os.path.isfile(os.path.join(ruta_hu, f, d))
                        for d in DOCUMENTOS)
                    for f in fases)):
                continue                    # no está terminada: no se cuenta''',
     '''            if not fases:
                continue'''),

    ("4: el veredicto se lee del cierre, no del resultado",
     "validadores/fases.py",
     '''    texto = _leer(os.path.join(ruta_fase, "resultado_pruebas.md"))''',
     '''    texto = _leer(os.path.join(ruta_fase, "funcionalidad_implementada.md"))'''),

    ("5: la linea vuelve a decir «completas»",
     "validadores/fases.py",
     '''    return (f"HU: {total} en total · {incompletas} sin terminar · "
            f"{completas} terminadas, de las cuales {cumplen} cumplen, "
            f"{no_cumplen} no cumplen y {sin_veredicto} no dicen si cumplen "
            f"(F12.2)")''',
     '''    return (f"HU: {total} en total · {completas} completas · "
            f"{incompletas} incompletas (F12.2)")'''),

    ("6: el molde del cierre vuelve a ofrecer un tercer valor",
     "plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md",
     '''| **Veredicto** | «Cumple» o «No cumple», **copiado del §6 del resultado**''',
     '''| **Veredicto** | «Cumple / Cumple con observaciones», a criterio de quien cierra'''),
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
              "pruebas.LaCuentaMiraElVeredicto", "pruebas.InventarioDeHU"])
    salida = subprocess.run(orden, capture_output=True, text=True,
                            encoding="utf-8", errors="replace",
                            cwd=os.path.join(RAIZ, "validadores"))
    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    return "\n".join("    " + l for l in lineas)


guardar_copias()
print("== seis sabotajes ==")
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
print("    ninguno: los seis editan un archivo que se restaura con copia,")
print("    y las pruebas escriben solo en carpeta temporal")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
if "OK" not in final or "Ran 0 " in final:
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
