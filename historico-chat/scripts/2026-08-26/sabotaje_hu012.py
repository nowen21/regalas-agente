# -*- coding: utf-8 -*-
"""Sabotea la fase A de la HU-012, corre las pruebas, y restaura con copia.

Lo aprendido rompiéndolo, aplicado acá:

- Se restaura **con copia**, nunca con el control de versiones.
- Si un sabotaje pasa en verde, **se corre el escenario y se mira el estado
  final**: puede ser que el sabotaje no saboteara.
- La corrida final es la suite **completa**, lanzada como programa, y el guion
  **se cae si corre cero pruebas**.
- **Se declaran y se limpian los rastros** fuera del archivo saboteado.
"""
import io
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_hu012")

SABOTAJES = [
    ("1: el vocabulario se escribe en el codigo, no sale del glosario",
     "validadores/fases.py",
     '''    validos = vocabulario_de_estados().get("Historia de usuario")''',
     '''    validos = {"Pendiente", "Lista", "En curso", "En prueba", "Terminada"}'''),

    ("2: la comprobacion se descuelga de la corrida",
     "validadores/fases.py",
     '''    return (hallazgos + cierre_sin_sello(proyecto)
            + cuenta_escrita_a_mano(proyecto)
            + estado_fuera_del_vocabulario(proyecto))''',
     '''    return (hallazgos + cierre_sin_sello(proyecto)
            + cuenta_escrita_a_mano(proyecto))'''),

    ("3: se compara la frase entera, no con que palabra empieza",
     "validadores/fases.py",
     '''            if any(valor.startswith(v) for v in validos):''',
     '''            if valor in validos:'''),

    ("4: el aviso no dice cuales valen",
     "validadores/fases.py",
     '''                "declara el estado «%s», que el glosario no define. Los que "
                "valen para una historia: %s (EP-003·HU-012)"
                % (valor.split("—")[0].split(".")[0].strip()[:34],
                   " · ".join(sorted(validos)))))''',
     '''                "declara un estado que el glosario no define "
                "(EP-003·HU-012)"))'''),

    ("5: la comprobacion CORRIGE el archivo",
     "validadores/fases.py",
     '''            valor = dice.group(1).strip().lstrip("*")''',
     '''            valor = dice.group(1).strip().lstrip("*")
            if valor and not any(valor.startswith(v) for v in validos):
                import io as _io
                _ruta = os.path.join(ruta_epica, nombre_hu, "%s.md" % nombre_hu)
                _io.open(_ruta, "w", encoding="utf-8", newline="\\n").write(
                    texto.replace(valor, "Pendiente", 1))'''),

    ("6: el glosario deja de definir «Terminada» para las tres",
     "base/glosario.md",
     '''| **Tarea** de un plan | Pendiente · En curso · Terminada · Bloqueada |''',
     '''| **Tarea** de un plan | Pendiente · En curso · Hecha · Bloqueada |'''),

    ("7: un molde vuelve a listar los estados por su cuenta",
     "plantillas/ciclo-vida-proyectos/04-HU.md",
     '''| **Estado** | Uno de [los estados del glosario]''',
     '''| **Estado** | Backlog / Ready / En curso / En QA / Done | «sobra» [los estados del glosario]'''),
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
              "pruebas.VocabularioDeEstados"])
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

# El sabotaje 5 escribe sobre las historias del arbol real si algo sale mal.
print("--- rastros fuera del archivo saboteado ---")
salida = subprocess.run(["git", "-C", RAIZ, "status", "--porcelain",
                         "documentacion/epicas"],
                        capture_output=True, text=True, encoding="utf-8",
                        errors="replace")
sucios = [l for l in (salida.stdout or "").splitlines()
          if "HU-0" in l and l.strip().startswith("M")]
print("    historias del arbol modificadas por los sabotajes: %d" % len(sucios))
for l in sucios[:5]:
    print("       %s" % l[:96])
print()

print("--- con todo restaurado: la suite COMPLETA ---")
final = correr(completa=True)
print(final)
if "OK" not in final or "Ran 0 " in final:
    print()
    print("ATENCION: la corrida final no salio limpia, o no corrio nada.")
    sys.exit(1)
