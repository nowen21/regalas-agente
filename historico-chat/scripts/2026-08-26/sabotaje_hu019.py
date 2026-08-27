# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-019, corre las pruebas, y restaura con copia.

Las cuatro lecciones de las fases anteriores, aplicadas acá:

- Se restaura **con copia**, nunca con el control de versiones.
- Si un sabotaje pasa en verde, **se corre el escenario y se mira el estado
  final** para saber si el sabotaje era malo o la prueba floja.
- El guion **siempre termina corriendo la suite completa**.
- **Se declaran y se limpian los rastros** que un sabotaje deje fuera del
  archivo saboteado.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu019")

SABOTAJES = [
    ("1: la comprobacion no busca nada",
     "validadores/fases.py",
     '''    r"^\\|\\s*\\*\\*(Total de HU|Completas|Incompletas)\\*\\*\\s*\\|\\s*\\d+\\s*\\|",''',
     '''    r"^ESTO NO APARECE NUNCA$",'''),

    ("2: la comprobacion marca cualquier cifra, no el campo",
     "validadores/fases.py",
     '''    r"^\\|\\s*\\*\\*(Total de HU|Completas|Incompletas)\\*\\*\\s*\\|\\s*\\d+\\s*\\|",''',
     '''    r"(\\d+)",'''),

    ("3: la comprobacion CORRIGE el archivo en vez de reportar",
     "validadores/fases.py",
     '''    campos = CUENTA_A_MANO.findall(_leer(ruta) or "")''',
     '''    _texto = _leer(ruta) or ""
    campos = CUENTA_A_MANO.findall(_texto)
    if campos:
        import io as _io
        _io.open(ruta, "w", encoding="utf-8", newline="\\n").write(
            CUENTA_A_MANO.sub("", _texto))'''),

    ("4: la comprobacion se descuelga de la corrida",
     "validadores/fases.py",
     '''    return (hallazgos + cierre_sin_sello(proyecto)
            + cuenta_escrita_a_mano(proyecto))''',
     '''    return hallazgos + cierre_sin_sello(proyecto)'''),

    ("5: el pendiente vuelve a guardar la cuenta",
     "pendientes/48-inventario-hu.md",
     '''| **Qué pasa** |''',
     '''| **Total de HU** | 113 |
| **Qué pasa** |'''),

    # El sabotaje 6 estaba mal hecho: reemplazaba **una** de las varias veces
    # que el pendiente nombra el comando, asi que el archivo seguia diciendolo
    # y la prueba tenia razon en pasar. El sabotaje no saboteaba. Ahora se
    # quitan todas.
    ("6: el pendiente deja de decir con que comando se saca",
     "pendientes/48-inventario-hu.md",
     None,
     None),
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
    # La corrida completa se lanza como el programa, no con `discover`:
    # `discover` sobre esta carpeta encontraba **cero** pruebas y el guion
    # cantaba OK sin haber corrido nada. Un guion que miente sobre la corrida
    # final es peor que no tenerlo.
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
print("== seis sabotajes, uno por cada cosa que la fase promete ==")
print("== se restauran con copia, nunca con el control de versiones ==")
print()
for titulo, archivo, viejo, nuevo in SABOTAJES:
    completa = os.path.join(RAIZ, archivo)
    t = io.open(completa, encoding="utf-8").read()
    print("--- %s ---" % titulo)
    if viejo is None:
        # Caso especial: se quitan TODAS las menciones del comando.
        roto = t.replace("python validadores/validar.py fases", "se cuenta a ojo")
        roto = roto.replace("validar.py fases", "se cuenta a ojo")
        cuantas = t.count("validar.py fases")
        print("    (se quitan las %d menciones, no una)" % cuantas)
    elif viejo not in t:
        print("    NO SE PUDO SABOTEAR: el texto cambio. Revisar el guion.")
        print()
        continue
    else:
        roto = t.replace(viejo, nuevo, 1)
    io.open(completa, "w", encoding="utf-8", newline="\n").write(roto)
    print(correr())
    print()
    restaurar(archivo)

# Los sabotajes 1 a 4 tocan solo `fases.py`; el 3 escribe sobre el pendiente
# **real** si algo saliera mal, y por eso el pendiente tambien se restaura.
print("--- rastros fuera del archivo saboteado ---")
print("    ninguno: los seis editan un archivo que se restaura con copia")
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
if "OK" not in final or "Ran 0 " in final:
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
