# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-020, corre las pruebas, y restaura con copia.

Lo que se aprendió rompiéndolo, aplicado acá:

- Se restaura **con copia**, nunca con el control de versiones.
- Si un sabotaje pasa en verde, **se corre el escenario y se mira el estado
  final**: puede ser que el sabotaje no saboteara.
- La corrida final es la suite **completa**, lanzada como programa, y el guion
  **se cae si corre cero pruebas**: `Ran 0 tests` sale con el mismo OK que una
  corrida buena.
- **Se declaran y se limpian los rastros** fuera del archivo saboteado.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu020")

SABOTAJES = [
    ("1: la busqueda vuelve a una ruta fija",
     "validadores/fases.py",
     '''    for relativa, ruta in _donde_puede_estar_el_inventario(proyecto):''',
     '''    for relativa, ruta in [("pendientes/48-inventario-hu.md",
                           os.path.join(proyecto, "pendientes",
                                        "48-inventario-hu.md"))]:'''),

    ("2: la busqueda recorre el arbol entero, no el primer nivel",
     "validadores/fases.py",
     '''        for nombre in sorted(os.listdir(completa)):
            if not nombre.lower().endswith(".md"):
                continue
            ruta = os.path.join(completa, nombre)
            if os.path.isfile(ruta):
                yield carpeta + "/" + nombre, ruta''',
     '''        for base, _sub, archivos in os.walk(completa):
            for nombre in sorted(archivos):
                if not nombre.lower().endswith(".md"):
                    continue
                ruta = os.path.join(base, nombre)
                yield os.path.relpath(ruta, proyecto).replace(os.sep, "/"), ruta'''),

    ("3: el aviso nombra una ruta fija en vez de la que encontro",
     "validadores/fases.py",
     '''                AVISO, relativa, 0,''',
     '''                AVISO, "pendientes/48-inventario-hu.md", 0,'''),

    ("4: la comprobacion se descuelga de la corrida",
     "validadores/fases.py",
     '''    return (hallazgos + cierre_sin_sello(proyecto)
            + cuenta_escrita_a_mano(proyecto))''',
     '''    return hallazgos + cierre_sin_sello(proyecto)'''),

    ("5: la plantilla vuelve a pedir la cuenta a mano",
     "plantillas/inventario-hu.md",
     '''| **Qué pasa** |''',
     '''| **Total de HU** | «N» |
| **Qué pasa** |'''),

    ("6: la plantilla vuelve a traer la tabla de una fila por historia",
     "plantillas/inventario-hu.md",
     '''## Qué clase de trabajo es''',
     '''| Épica | HU | Fase | `plan_trabajo` |
|---|---|:--:|:--:|
| EP-000 | HU-000 | ☐ | ☐ |

## Qué clase de trabajo es'''),

    ("7: el comando de la plantilla pierde las comillas",
     "plantillas/inventario-hu.md",
     '''python "«RUTA-ESTANDAR»/validadores/validar.py" fases --raiz .''',
     '''python «RUTA-ESTANDAR»/validadores/validar.py fases --raiz .'''),
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
             [sys.executable, "-m", "unittest", "pruebas.InventarioDeHU"])
    salida = subprocess.run(orden, capture_output=True, text=True,
                            encoding="utf-8", errors="replace",
                            cwd=os.path.join(RAIZ, "validadores"))
    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    return "\n".join("    " + l for l in lineas)


guardar_copias()
print("== siete sabotajes, uno por cada cosa que la fase promete ==")
print("== se restauran con copia, nunca con el control de versiones ==")
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
    print()
    restaurar(archivo)

print("--- rastros fuera del archivo saboteado ---")
print("    ninguno: los siete editan un archivo que se restaura con copia,")
print("    y las pruebas escriben solo en carpeta temporal")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
if "OK" not in final or "Ran 0 " in final:
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
