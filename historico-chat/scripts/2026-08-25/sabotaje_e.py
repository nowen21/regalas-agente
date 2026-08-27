# -*- coding: utf-8 -*-
"""Sabotea el código de la fase E, corre las pruebas, y restaura con copia.

Las tres lecciones de las fases anteriores, aplicadas acá:

- Se restaura **con copia**, nunca con el control de versiones (fase B).
- Si un sabotaje pasa en verde, **se corre el escenario y se mira el estado
  final** para saber si el sabotaje era malo o la prueba floja (fases H y C).
- El guion **siempre termina corriendo la suite completa**: si esa corrida no
  sale limpia, algo quedó saboteado.

Y una cuarta, que salió acá: **restaurar el archivo no deshace lo que el
sabotaje escribió fuera de él**. El sabotaje 6 hacía que traer dejara un
archivo dentro del repositorio, y ese archivo se quedó después de restaurar el
código: se descubrió en la corrida real, cuando la comprobación de «no hay
rastro dentro del repositorio» salió en verdadero. Por eso el guion ahora
limpia los rastros conocidos al terminar, y los nombra.
"""
import io
import os
import re
import shutil
import subprocess
import sys

PY = os.path.abspath("../interfaz/.venv/Scripts/python.exe")
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_fase_e")

SABOTAJES = [
    ("1: reconocer acepta cualquier archivo, no solo los moldes",
     "nucleo/importacion/moldes.py",
     '''    return ""''',
     '''    return "documento"'''),

    ("2: traer traduce los saltos de linea de Windows",
     "nucleo/importacion/core.py",
     '''            with io.open(origen, encoding="utf-8", errors="replace",
                         newline="") as abierto:''',
     '''            with io.open(origen, encoding="utf-8",
                         errors="replace") as abierto:'''),

    ("3: traer dos veces duplica",
     "nucleo/importacion/core.py",
     '''            existia = Traido.objects.filter(proyecto=proyecto.identificador,
                                            origen=relativa).first()''',
     '''            existia = None'''),

    ("4: al fallar a mitad, se deja lo que alcanzo a entrar",
     "nucleo/importacion/core.py",
     '''        _deshacer(escritos, anotados)''',
     '''        pass'''),

    ("5: al fallar se borran los archivos pero no las filas del indice",
     "nucleo/importacion/core.py",
     '''    if anotados:
        Traido.objects.filter(pk__in=anotados).delete()''',
     '''    pass'''),

    ("6: traer escribe dentro de la carpeta del proyecto de origen",
     "nucleo/importacion/core.py",
     '''def _donde_queda(proyecto, relativa):
    """Dónde vive dentro de la plataforma un documento traído."""
    return "proyectos/%s/traido/%s" % (proyecto.identificador, relativa)''',
     '''def _donde_queda(proyecto, relativa):
    """Dónde vive dentro de la plataforma un documento traído."""
    import io as _io, os as _os
    _rastro = _os.path.join(proyecto.ruta_codigo, "traido-por-la-plataforma.txt")
    with _io.open(_rastro, "a", encoding="utf-8") as _a:
        _a.write(relativa + "\\n")
    return "proyectos/%s/traido/%s" % (proyecto.identificador, relativa)'''),

    ("7: no se muestra nada antes de traer: se trae de una",
     "nucleo/importacion/views.py",
     '''    if request.method != "POST" or not request.POST.get("confirmado"):''',
     '''    if False:'''),

    ("8: las carpetas que no se miran no se nombran",
     "nucleo/importacion/core.py",
     '''        return [(nombre, porque)
                for nombre, porque in moldes.CARPETAS_QUE_NO_SE_MIRAN
                if os.path.isdir(os.path.join(self.proyecto.ruta_codigo, nombre))]''',
     '''        return []'''),
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
print("== ocho sabotajes, uno por cada cosa que la fase promete ==")
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

# Lo que algun sabotaje pudo dejar escrito FUERA del codigo. Restaurar el
# archivo saboteado no borra esto, y si queda, ensucia el proyecto de verdad.
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
