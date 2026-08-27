# -*- coding: utf-8 -*-
"""Sabotea el código de la fase G, corre las pruebas, y restaura con copia.

Las cuatro lecciones de las fases anteriores, aplicadas acá:

- Se restaura **con copia**, nunca con el control de versiones (fase B).
- Si un sabotaje pasa en verde, **se corre el escenario y se mira el estado
  final** para saber si el sabotaje era malo o la prueba floja (fases H y C).
- El guion **siempre termina corriendo la suite completa** (fase H).
- **Se declaran y se limpian los rastros que un sabotaje deje fuera del
  archivo saboteado** (fase E).
"""
import io
import os
import re
import shutil
import subprocess
import sys

PY = os.path.abspath("../interfaz/.venv/Scripts/python.exe")
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_fase_g")

SABOTAJES = [
    ("1: cvds/ vuelve a quedarse fuera de lo que se trae",
     "nucleo/importacion/moldes.py",
     '''CARPETAS_DEL_CICLO = ("documentacion", "cvds")''',
     '''CARPETAS_DEL_CICLO = ("documentacion",)'''),

    ("2: el README de una etapa se trata como un indice cualquiera",
     "nucleo/importacion/moldes.py",
     '''    if nombre == "README.md" and relativa:
        partes = relativa.replace("\\\\", "/").split("/")
        if len(partes) >= 2 and partes[-2] in ETAPAS:
            return "etapa del ciclo de vida"''',
     '''    pass'''),

    ("3: una estacion ilegible se cuenta como cerrada",
     "nucleo/proyectos/estado.py",
     '''    numero = _NUMERO.search(linea)
    if not numero:
        return False, False''',
     '''    numero = _NUMERO.search(linea)
    if not numero:
        return False, True'''),

    ("4: el estado se calcula leyendo la carpeta del proyecto",
     "nucleo/proyectos/estado.py",
     '''def _texto(documento):
    """El texto del documento traído, o "" si no se puede leer."""
    completa = os.path.join(str(settings.CARPETA_DATOS),
                            documento.guardado_en.replace("/", os.sep))''',
     '''def _texto(documento):
    """El texto del documento traído, o "" si no se puede leer."""
    from .models import Proyecto
    _p = Proyecto.objects.filter(identificador=documento.proyecto).first()
    completa = os.path.join(_p.ruta_codigo,
                            documento.origen.replace("/", os.sep))'''),

    ("5: las etapas que faltan no se dicen",
     "nucleo/proyectos/estado.py",
     '''    estado.etapas_sin_documento = [e for e in moldes.ETAPAS if e not in con_etapa]''',
     '''    estado.etapas_sin_documento = []'''),

    ("6: un proyecto sin nada no dice que haria falta",
     "nucleo/proyectos/estado.py",
     '''        return ("Para empezar, traer lo que este proyecto ya tenga escrito. Si "
                "todavía no tiene documentación, lo primero es la etapa de "
                "planificación.")''',
     '''        return ""'''),

    ("7: las aprobaciones no se cuentan",
     "nucleo/proyectos/estado.py",
     '''        if _esta_aprobado(documento):
            estado.aprobados += 1''',
     '''        if False:
            estado.aprobados += 1'''),
]


def guardar_copias():
    if os.path.isdir(COPIAS):
        shutil.rmtree(COPIAS)
    os.makedirs(COPIAS)
    for archivo in {s[1] for s in SABOTAJES}:
        shutil.copy2(archivo, os.path.join(COPIAS, archivo.replace("/", "_")))


def restaurar(archivo):
    shutil.copy2(os.path.join(COPIAS, archivo.replace("/", "_")), archivo)


def correr():
    salida = subprocess.run([PY, "manage.py", "test", "nucleo"],
                            capture_output=True, text=True, encoding="utf-8",
                            errors="replace")
    texto = (salida.stdout or "") + (salida.stderr or "")
    return "\n".join(l for l in texto.splitlines()
                     if re.match(r"^(FAIL|ERROR|Ran |FAILED|OK)", l))


guardar_copias()
print("== siete sabotajes, uno por cada cosa que la fase promete ==")
print("== se restauran con copia, nunca con el control de versiones ==")
print()
for titulo, archivo, viejo, nuevo in SABOTAJES:
    t = io.open(archivo, encoding="utf-8").read()
    print("--- %s ---" % titulo)
    if viejo not in t:
        print("NO SE PUDO SABOTEAR: el texto cambio. Revisar el guion.")
        print()
        continue
    io.open(archivo, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))
    print(correr())
    print()
    restaurar(archivo)

# Ninguno de estos sabotajes escribe fuera de su archivo, pero la comprobacion
# se deja igual: es barata, y la fase E demostro que olvidarla cuesta caro.
RASTROS = [os.path.abspath(os.path.join("..", "traido-por-la-plataforma.txt"))]
print("--- se limpian los rastros que los sabotajes pudieron dejar ---")
for rastro in RASTROS:
    if os.path.exists(rastro):
        os.remove(rastro)
        print("    borrado: %s" % rastro)
    else:
        print("    no quedo: %s" % rastro)
print()

print("--- con el codigo restaurado ---")
final = correr()
print(final)
if "OK" not in final:
    print()
    print("ATENCION: la corrida final no salio limpia. Algo quedo saboteado.")
    sys.exit(1)
