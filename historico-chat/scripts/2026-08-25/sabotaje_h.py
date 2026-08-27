# -*- coding: utf-8 -*-
"""Sabotea el código de la fase H, corre las pruebas, y restaura con copia.

Restaurar con copia y no con el control de versiones es la lección de la fase B:
estos archivos son recién escritos y todavía no están versionados. Y el guion
termina siempre corriendo la suite completa: si esa última corrida no sale
limpia, algo quedó saboteado.
"""
import io
import os
import re
import shutil
import subprocess
import sys

PY = os.path.abspath("../interfaz/.venv/Scripts/python.exe")
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_fase_h")

SABOTAJES = [
    # El primer intento de este sabotaje borraba la ficha y la reescribia
    # enseguida: no cambiaba nada observable, asi que paso en verde. No era un
    # hueco de las pruebas, era un sabotaje que no saboteaba. Este si: borra la
    # documentacion del proyecto, que es lo que CP-001 promete que no pasa.
    ("1: desconectar borra la documentacion del proyecto",
     "nucleo/proyectos/core.py",
     '''    cuando = timezone.localtime().date().isoformat()
    _reescribir_ficha(proyecto, desconectado=cuando,''',
     '''    cuando = timezone.localtime().date().isoformat()
    import os as _os
    _carpeta = _os.path.dirname(almacen._ruta_real(_ficha(proyecto.identificador)))
    for _n in _os.listdir(_carpeta):
        if _n != "proyecto.md":
            _os.remove(_os.path.join(_carpeta, _n))
    _reescribir_ficha(proyecto, desconectado=cuando,'''),

    ("2: la marca de desconectado no llega a la ficha",
     "nucleo/proyectos/core.py",
     '''           desconectado or "sigue conectado"))''',
     '''           "sigue conectado"))'''),

    ("3: renombrar recalcula el identificador y mueve la carpeta",
     "nucleo/proyectos/core.py",
     '''    return _indexar(proyecto.identificador, nombre_nuevo,''',
     '''    return _indexar(identificador_de(nombre_nuevo), nombre_nuevo,'''),

    ("4: corregir la version acepta cualquier numero",
     "nucleo/proyectos/core.py",
     '''    if not reglas.existe(version):
        raise VersionQueNoExiste(
            "El proyecto declara la versión %s del estándar, y esa versión "
            "nunca se publicó. Se deja la que tenía." % version)''',
     '''    pass'''),

    ("5: los cambios no preguntan antes",
     "nucleo/proyectos/views.py",
     '''    if not request.POST.get("confirmado"):
        return render(request, "proyectos/confirmar.html", dict(
            confirmacion,
            proyecto=proyecto,
            accion=que,
            pide_nombre=(que == "renombrar"),
            campos={}))''',
     '''    pass'''),

    ("6: reconectar crea un proyecto nuevo en vez de reactivar",
     "nucleo/proyectos/core.py",
     '''    dormido = Proyecto.objects.filter(ruta_normalizada=normal).first()
    if dormido:
        return reconectar(dormido, quien=quien, sesion=sesion)''',
     '''    pass'''),
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
    lineas = [l for l in texto.splitlines()
              if re.match(r"^(FAIL|ERROR|Ran |FAILED|OK)", l)]
    return "\n".join(lineas)


guardar_copias()
print("== seis sabotajes, uno por cada cosa que la fase promete ==")
print("== se restauran con copia, nunca con el control de versiones ==")
print()
for titulo, archivo, viejo, nuevo in SABOTAJES:
    t = io.open(archivo, encoding="utf-8").read()
    if viejo not in t:
        print("--- %s ---" % titulo)
        print("NO SE PUDO SABOTEAR: el texto cambió. Revisar el guion.")
        print()
        continue
    io.open(archivo, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))
    print("--- %s ---" % titulo)
    print(correr())
    print()
    restaurar(archivo)

print("--- con el codigo restaurado ---")
final = correr()
print(final)
if "OK" not in final:
    print()
    print("ATENCION: la corrida final no salio limpia. Algo quedo saboteado.")
    sys.exit(1)
