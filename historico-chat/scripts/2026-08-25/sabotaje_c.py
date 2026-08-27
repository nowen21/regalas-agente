# -*- coding: utf-8 -*-
"""Sabotea el código de la fase C, corre las pruebas, y restaura con copia.

Dos lecciones de las fases anteriores, aplicadas acá:

- **Se restaura con copia, nunca con el control de versiones**: lo que se
  saboteó es código recién escrito y puede no estar versionado (fase B).
- **Un sabotaje tiene que cambiar algo observable.** Si pasa en verde, la
  primera pregunta es si de verdad saboteaba, no si falta una prueba (fase H).
"""
import io
import os
import re
import shutil
import subprocess
import sys

PY = os.path.abspath("../interfaz/.venv/Scripts/python.exe")
COPIAS = os.path.join(os.environ.get("TEMP", "."), "copias_fase_c")

SABOTAJES = [
    ("1: el aviso no dice que ruta se busco",
     "nucleo/proyectos/core.py",
     '''            "La carpeta de su código ya no está donde estaba. Se buscó en "
            "«%s». Su documentación sigue guardada acá." % ruta)''',
     '''            "La carpeta de su código ya no está donde estaba.")'''),

    ("2: corregir la ruta no comprueba que exista",
     "nucleo/proyectos/core.py",
     '''    if not os.path.isdir(pedida):
        raise RutaQueNoExiste(
            "No existe la carpeta «%s». Se deja la ruta que tenía." % pedida)''',
     '''    pass'''),

    ("3: corregir la ruta no comprueba el duplicado",
     "nucleo/proyectos/core.py",
     '''    if ya:
        raise RutaYaRegistrada(
            "Esa carpeta ya está registrada por el proyecto «%s». Se deja la "
            "ruta que tenía." % ya.nombre)''',
     '''    pass'''),

    ("4: corregir la ruta deja la version vieja",
     "nucleo/proyectos/core.py",
     '''    _reescribir_ficha(proyecto, ruta=pedida, version=version,
                      que_se_hizo="corregir la ruta de un proyecto",''',
     '''    _reescribir_ficha(proyecto, ruta=pedida,
                      que_se_hizo="corregir la ruta de un proyecto",'''),

    ("5: corregir la ruta mueve el codigo de una carpeta a la otra",
     "nucleo/proyectos/core.py",
     '''    vieja = proyecto.ruta_codigo
    _reescribir_ficha(proyecto, ruta=pedida, version=version,''',
     '''    vieja = proyecto.ruta_codigo
    import shutil as _sh
    for _n in os.listdir(vieja):
        _origen = os.path.join(vieja, _n)
        if os.path.isfile(_origen):
            _sh.move(_origen, os.path.join(pedida, _n))
    _reescribir_ficha(proyecto, ruta=pedida, version=version,'''),

    ("6: corregir la ruta no pregunta antes",
     "nucleo/proyectos/views.py",
     '''    if not request.POST.get("confirmado"):
        return render(request, "proyectos/confirmar.html", dict(''',
     '''    if False:
        return render(request, "proyectos/confirmar.html", dict('''),
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
print("== seis sabotajes, uno por cada cosa que la fase promete ==")
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

print("--- con el codigo restaurado ---")
final = correr()
print(final)
if "OK" not in final:
    print()
    print("ATENCION: la corrida final no salio limpia. Algo quedo saboteado.")
    sys.exit(1)
