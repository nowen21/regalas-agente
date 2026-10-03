# -*- coding: utf-8 -*-
"""Fase A de la HU-003, T-16: el pendiente 103 pasa a `EP-023/pendientes/`.

Su dueño es EP-023 y el análisis 8 (punto 15 de «Lo acordado») pide la carpeta `pendientes/` y nada más.
El guion mueve la carpeta con `git mv`, corrige los enlaces relativos de sus propios archivos (un nivel
más) y los enlaces que la nombran desde otros archivos. Solo cambia la ruta: el texto no se toca.
No toca las transcripciones (`historico-chat/AAAA-MM-DD-*.md`), que son el registro literal, ni las
copias de otros repositorios en `plataforma/datos/`.
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EPICA = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo")
NOMBRE = "103-cada-documento-de-la-cadena-sale-del-anterior"
ORIGEN = os.path.join(EPICA, NOMBRE)
DESTINO = os.path.join(EPICA, "pendientes", NOMBRE)

FUERA = {".git", ".venv", "venv", "__pycache__", "node_modules", "terceros"}
_ENLACE = re.compile(r"(\]\()([^)\s#]+)((?:#[^)\s]*)?\))")
_TRANSCRIPCION = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")


def _dentro(ruta, carpeta):
    ruta, carpeta = os.path.normcase(ruta), os.path.normcase(carpeta)
    return ruta == carpeta or ruta.startswith(carpeta + os.sep)


def _archivos():
    for actual, subcarpetas, archivos in os.walk(RAIZ):
        subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
        rel = os.path.relpath(actual, RAIZ).replace(os.sep, "/")
        if rel.startswith("plataforma/datos"):
            subcarpetas[:] = []
            continue
        for nombre in archivos:
            if not nombre.endswith(".md"):
                continue
            if rel == "historico-chat" and _TRANSCRIPCION.match(nombre):
                continue
            yield os.path.join(actual, nombre)


def _nuevo_destino(objetivo):
    """Si el enlace apunta dentro de la carpeta vieja, la ruta equivalente en la nueva."""
    if _dentro(objetivo, ORIGEN):
        return os.path.join(DESTINO, os.path.relpath(objetivo, ORIGEN))
    return objetivo


def _corregir(texto, viejo_lugar, nuevo_lugar):
    """Reescribe cada enlace relativo para que siga llevando al mismo archivo."""
    cambios = [0]

    def uno(m):
        enlace = m.group(2)
        if re.match(r"^[a-z]+:", enlace) or enlace.startswith("/"):
            return m.group(0)
        objetivo = os.path.normpath(os.path.join(os.path.dirname(viejo_lugar), enlace.replace("/", os.sep)))
        if viejo_lugar == nuevo_lugar and not _dentro(objetivo, ORIGEN):
            return m.group(0)           # archivo que no se mueve y enlace que no apunta al 103
        objetivo = _nuevo_destino(objetivo)
        nuevo = os.path.relpath(objetivo, os.path.dirname(nuevo_lugar)).replace(os.sep, "/")
        if nuevo == enlace:
            return m.group(0)
        cambios[0] += 1
        return m.group(1) + nuevo + m.group(3)

    return _ENLACE.sub(uno, texto), cambios[0]


def main():
    assert os.path.isdir(ORIGEN) and not os.path.exists(DESTINO)
    textos = {}
    for ruta in _archivos():
        with open(ruta, encoding="utf-8") as f:
            textos[ruta] = f.read()
    total = 0
    nuevos = {}
    for ruta, texto in textos.items():
        nuevo_lugar = _nuevo_destino(ruta)
        corregido, n = _corregir(texto, ruta, nuevo_lugar)
        if n:
            nuevos[nuevo_lugar] = corregido
            total += n
    os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
    subprocess.run(["git", "mv", ORIGEN, DESTINO], cwd=RAIZ, check=True)
    for ruta, texto in nuevos.items():
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
    print("enlaces corregidos: %d, en %d archivos" % (total, len(nuevos)))
    for ruta in sorted(nuevos):
        print("  " + os.path.relpath(ruta, RAIZ))


if __name__ == "__main__":
    sys.exit(main())
