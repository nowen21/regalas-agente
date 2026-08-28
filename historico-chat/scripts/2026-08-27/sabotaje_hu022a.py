# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-022, corre las pruebas, y restaura con copia.

Lo aprendido rompiendo, aplicado aca:

- **Se restaura con copia, no con git**: el archivo puede tener cambios sin
  guardar que un `checkout` se llevaria.
- **Se limpia despues de CADA sabotaje**, no al final (S-051).
- **La guardia final exige la linea `OK` sola**, no que «OK» aparezca en el
  texto: la salida de los validadores trae «OK: sin incumplimientos.» y por eso
  el guion de la fase C dio por buena una corrida con tres fallas.
- **Se declara lo que queda fuera del repositorio**: la copia de restauracion
  vive en la carpeta temporal del sistema, que es el resto anotado en el
  pendiente 89.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu022a")
ARCHIVO = "validadores/fases.py"

SABOTAJES = [
    ("1: vuelve a bastar con que el documento exista",
     '''    if not all(os.path.isfile(os.path.join(ruta_fase, d)) for d in DOCUMENTOS):
        return False
    return not moldes_sin_llenar(ruta_fase, de_cada_uno)''',
     '''    return all(os.path.isfile(os.path.join(ruta_fase, d))
               for d in DOCUMENTOS)'''),

    ("2: se cuenta cuantos marcadores hay, no cuantos son del molde",
     '''    quedan = _marcadores(_leer(ruta_documento)) & propios_del_molde''',
     '''    quedan = _marcadores(_leer(ruta_documento))'''),

    ("3: el corte baja a uno y la prosa con comillas cae",
     '''MARCADORES_DEL_MOLDE_MINIMO = 3''',
     '''MARCADORES_DEL_MOLDE_MINIMO = 1'''),

    ("4: sin plantilla se supone una lista de reserva",
     '''        suyos = _marcadores(_leer(os.path.join(raiz, molde)))
        if suyos:
            de_cada_uno[documento] = suyos''',
     '''        suyos = _marcadores(_leer(os.path.join(raiz, molde)))
        de_cada_uno[documento] = suyos or {"AAAA-MM-DD", "\u00abM\u00bb",
                                           "\u00abA-EP01-HU03-Descripci\u00f3n\u00bb"}'''),

    ("5: el aviso dice cuantos pero no cuales",
     '''                        f"sigue siendo la plantilla: conserva {len(quedan)} de "
                        f"sus marcadores, por ejemplo `{ejemplo}` \u2014 la fase no "''',
     '''                        f"sigue siendo la plantilla: conserva {len(quedan)} de "
                        f"sus marcadores \u2014 la fase no "'''),

    ("6: la comprobacion se desconecta de validar()",
     '''            + documentos_que_siguen_siendo_el_molde(proyecto))''',
     '''            )'''),
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
              "pruebas.ElMoldeSinLlenarNoCuenta"])
    salida = subprocess.run(orden, capture_output=True, text=True,
                            encoding="utf-8", errors="replace",
                            cwd=os.path.join(RAIZ, "validadores"))
    texto = (salida.stdout or "") + (salida.stderr or "")
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL:|ERROR:|Ran |OK|FAILED)", l)]
    salida_limpia = "\n".join("    " + l for l in lineas)
    # La consola de Windows no sabe escribir todo lo que unittest devuelve, y
    # un `print` que revienta entre el sabotaje y la restauracion deja el
    # repositorio roto. Se limpia antes de imprimir.
    return salida_limpia.encode("ascii", "replace").decode("ascii")


guardar_copia()
print("== seis sabotajes ==")
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
        # Pase lo que pase. Sin esto, un `print` que revienta deja el
        # repositorio con el sabotaje puesto — y ya paso una vez.
        restaurar()
    print()

print("--- rastros fuera del repositorio ---")
print("    uno, declarado: la copia de restauracion, en la carpeta temporal")
print("    del sistema. Es el resto anotado en el pendiente 89.")
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
