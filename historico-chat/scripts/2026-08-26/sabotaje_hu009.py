# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-009, corre las pruebas, y restaura con copia."""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu009")

SABOTAJES = [
    ("1: el instalador no pone el ajuste",
     "validadores/instalar.py",
     '''    pasos += _rutas_largas(ruta, aplicar)''',
     '''    pasos += []'''),

    ("2: pisa un «false» puesto a mano",
     "validadores/instalar.py",
     '''    if actual == "false":''',
     '''    if False:'''),

    ("3: el modo que muestra tambien escribe",
     "validadores/instalar.py",
     '''    pasos = ["git config core.longpaths true"]
    if aplicar:
        _mandar_git(ruta, "config", "core.longpaths", "true")''',
     '''    pasos = ["git config core.longpaths true"]
    _mandar_git(ruta, "config", "core.longpaths", "true")'''),

    ("4: toca la configuracion GLOBAL de la maquina",
     "validadores/instalar.py",
     '''        _mandar_git(ruta, "config", "core.longpaths", "true")''',
     '''        _mandar_git(ruta, "config", "--global", "core.longpaths", "true")'''),

    ("5: el instalador no dice que lo puso",
     "validadores/instalar.py",
     '''    pasos = ["git config core.longpaths true"]''',
     '''    pasos = ["se ajusta el control de versiones"]'''),

    ("6: el documento de despliegue no dice por que no viaja",
     "cvds/despliegue/README.md",
     '''**no viaja al clonar**''',
     '''**no se copia**'''),

    ("7: el documento no dice el comando global",
     "cvds/despliegue/README.md",
     '''git config --global core.longpaths true''',
     '''(no hay forma de que valga para todo)'''),
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


def global_ahora():
    return subprocess.run(
        ["git", "config", "--global", "--get", "core.longpaths"],
        capture_output=True, text=True, timeout=30).stdout.strip()


def correr(completa=False):
    orden = ([sys.executable, "pruebas.py"] if completa else
             [sys.executable, "-m", "unittest", "pruebas.RutasLargas"])
    salida = subprocess.run(orden, capture_output=True, text=True,
                            encoding="utf-8", errors="replace",
                            cwd=os.path.join(RAIZ, "validadores"))
    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    return "\n".join("    " + l for l in lineas)


# **El sabotaje 4 escribe en la configuracion GLOBAL de esta maquina.** Se
# anota antes y se restaura despues: es el rastro mas caro de esta fase, porque
# queda fuera del repositorio y ningun `git status` lo muestra.
GLOBAL_ANTES = global_ahora()

guardar_copias()
print("== siete sabotajes ==")
print("== la configuracion global se anota antes y se restaura despues ==")
print("   valor global al empezar: %s" % (GLOBAL_ANTES or "(sin poner)"))
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
    # **El rastro se limpia despues de CADA sabotaje, no al final.** El 4
    # escribe en la configuracion global, y dejarla puesta contamina los
    # siguientes: sus fallas se leen como «cazado» y son del rastro anterior.
    # Es la leccion de `S-035` un nivel mas arriba — aca el rastro queda
    # **fuera del repositorio**, donde ningun `git status` lo muestra.
    if global_ahora() != GLOBAL_ANTES:
        print("    (dejo la configuracion global puesta: se restaura)")
        if GLOBAL_ANTES:
            subprocess.run(["git", "config", "--global", "core.longpaths",
                            GLOBAL_ANTES], capture_output=True, timeout=30)
        else:
            subprocess.run(["git", "config", "--global", "--unset",
                            "core.longpaths"], capture_output=True, timeout=30)
    print()

print("--- rastros fuera del archivo saboteado ---")
ahora = global_ahora()
if ahora != GLOBAL_ANTES:
    print("    la configuracion GLOBAL cambio: «%s» -> «%s». Se restaura."
          % (GLOBAL_ANTES or "(sin poner)", ahora))
    if GLOBAL_ANTES:
        subprocess.run(["git", "config", "--global", "core.longpaths",
                        GLOBAL_ANTES], capture_output=True, timeout=30)
    else:
        subprocess.run(["git", "config", "--global", "--unset",
                        "core.longpaths"], capture_output=True, timeout=30)
    print("    valor restaurado: %s" % (global_ahora() or "(sin poner)"))
else:
    print("    la configuracion global quedo intacta")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
if "OK" not in final or "Ran 0 " in final:
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
