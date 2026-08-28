# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-023, corre las pruebas, y restaura con copia.

Lo aprendido rompiendo, aplicado aca:

- **Se restaura con copia, no con git.**
- **La restauracion va en `try/finally`** (S-060).
- **La salida se limpia antes de imprimirla.**
- **La guardia final exige la linea `OK` sola.**
- **Este guion NO se corre por una tuberia.**

Los cinco sabotajes atacan la mitad que importa: que el rojo NO se cierre solo.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu023a")
ARCHIVO = "validadores/fases.py"

SABOTAJES = [
    ("1: el reemplazo se deduce del orden, sin declararlo",
     '''        if (nombrada and nombrada != nombre and nombrada in fases
                and veredicto_de(os.path.join(ruta_hu, nombre)) == "Cumple"):
            dejados.add(nombrada)''',
     '''        if veredicto_de(os.path.join(ruta_hu, nombre)) == "Cumple":
            for otra in fases:
                if otra < nombre:
                    dejados.add(otra)'''),

    ("2: un rojo puede cerrar otro rojo",
     '''                and veredicto_de(os.path.join(ruta_hu, nombre)) == "Cumple"):''',
     '''                ):'''),

    ("3: una fase se puede cerrar a si misma",
     '''        if (nombrada and nombrada != nombre and nombrada in fases''',
     '''        if (nombrada and nombrada in fases'''),

    ("4: se acepta el nombre de una fase de otra historia",
     '''        if (nombrada and nombrada != nombre and nombrada in fases''',
     '''        if (nombrada and nombrada != nombre'''),

    ("5: el aviso no dice que nombre se escribio",
     '''                    f"declara reemplazar el veredicto de `{nombrada}` y no se "
                    f"aplica: {motivo} \u2014 el veredicto anterior sigue contando "''',
     '''                    f"declara un reemplazo que no se aplica: {motivo} "'''),
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
              "pruebas.UnRojoSeCierraDeclarandolo"])
    salida = subprocess.run(orden, capture_output=True, text=True,
                            encoding="utf-8", errors="replace",
                            cwd=os.path.join(RAIZ, "validadores"))
    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    limpio = "\n".join("    " + l for l in lineas)
    return limpio.encode("ascii", "replace").decode("ascii")


guardar_copia()
print("== cinco sabotajes ==")
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
    try:
        print(correr())
    finally:
        restaurar()
    print()

print("--- rastros fuera del repositorio ---")
print("    uno, declarado: la copia de restauracion, en la carpeta temporal.")
print("    El enganche de la HU-018 lo va a avisar, que es para lo que se hizo.")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
lineas = [l.strip() for l in final.splitlines()]
# `"OK" in lineas` era demasiado estricto: cuando la suite trae pruebas
# marcadas como fallo esperado, unittest no escribe `OK` sino
# `OK (expected failures=4)`, y la guardia daba falsa alarma con la corrida
# limpia. Se acepta `OK` o `OK (...)`, y se sigue rechazando la linea de los
# validadores, que empieza por `OK:`.
limpia = any(l == "OK" or l.startswith("OK (") for l in lineas)
if (not limpia or not any(l.startswith("Ran ") for l in lineas)
        or any(l.startswith("Ran 0 ") for l in lineas)):
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
