# -*- coding: utf-8 -*-
"""Sabotea el código de la fase F, corre las pruebas, y restaura con copia.

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
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_fase_f")

SABOTAJES = [
    ("1: el reporte no nombra lo no reconocido, solo lo cuenta",
     "nucleo/importacion/core.py",
     '''        lineas += ["- `%s`" % ruta for ruta in hallazgo.sin_reconocer]''',
     '''        pass'''),

    ("2: el reporte no se escribe cuando no quedo nada afuera",
     "nucleo/importacion/core.py",
     '''    _escribir(donde_el_reporte, _texto_del_reporte(proyecto, hallazgo, nuevos,
                                                  ya_estaban))''',
     '''    if hallazgo.sin_reconocer:
        _escribir(donde_el_reporte,
                  _texto_del_reporte(proyecto, hallazgo, nuevos, ya_estaban))'''),

    ("3: cada traida pisa el reporte anterior",
     "nucleo/importacion/core.py",
     '''    cuando = timezone.localtime().strftime("%Y-%m-%d-%H%M%S")
    return "proyectos/%s/reportes/%s-lo-que-no-entro.md" % (
        proyecto.identificador, cuando)''',
     '''    return "proyectos/%s/reportes/lo-que-no-entro.md" % (
        proyecto.identificador,)'''),

    ("4: el registro de auditoria no enlaza el reporte",
     "nucleo/importacion/core.py",
     '''        que_cambio="%d documento(s) reconocido(s), %d sin reconocer. "
                   "El detalle, en %s"
                   % (hallazgo.cuantos, len(hallazgo.sin_reconocer),
                      donde_el_reporte),''',
     '''        que_cambio="%d documento(s) reconocido(s), %d sin reconocer"
                   % (hallazgo.cuantos, len(hallazgo.sin_reconocer)),'''),

    ("5: el registro repite la lista en vez de enlazarla",
     "nucleo/importacion/core.py",
     '''        que_cambio="%d documento(s) reconocido(s), %d sin reconocer. "
                   "El detalle, en %s"
                   % (hallazgo.cuantos, len(hallazgo.sin_reconocer),
                      donde_el_reporte),''',
     '''        que_cambio="%d documento(s) reconocido(s), %d sin reconocer: %s"
                   % (hallazgo.cuantos, len(hallazgo.sin_reconocer),
                      ", ".join(hallazgo.sin_reconocer)),'''),

    ("6: el reporte no dice que carpetas no se miraron",
     "nucleo/importacion/core.py",
     '''        lineas += ["| `%s/` | %s |" % (nombre, porque)
                   for nombre, porque in carpetas]''',
     '''        pass'''),

    ("7: los reportes no se pueden listar",
     "nucleo/importacion/core.py",
     '''        hallados.append((cuando, "proyectos/%s/reportes/%s"
                         % (proyecto.identificador, nombre)))''',
     '''        pass'''),

    ("8: el reporte se escribe dentro de la carpeta del proyecto",
     "nucleo/importacion/core.py",
     '''def _donde_va_el_reporte(proyecto):''',
     '''def _donde_va_el_reporte(proyecto):
    import io as _io, os as _os
    _rastro = _os.path.join(proyecto.ruta_codigo, "reporte-de-la-plataforma.txt")
    with _io.open(_rastro, "a", encoding="utf-8") as _a:
        _a.write("una traida" + chr(10))'''),
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

# Lo que el sabotaje 8 deja escrito FUERA del archivo saboteado.
RASTROS = [os.path.abspath(os.path.join("..", "reporte-de-la-plataforma.txt")),
           os.path.abspath(os.path.join("..", "traido-por-la-plataforma.txt"))]
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
