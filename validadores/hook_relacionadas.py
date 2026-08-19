# -*- coding: utf-8 -*-
"""`EP-005 · HU-010` · Al escribir, llegan las reglas relacionadas.

Se engancha a `PostToolUse` sobre `Write|Edit`. Cuando lo que se escribió es un
documento que un capítulo gobierna, entrega **lo que se relaciona con él**: las
reglas que dependen de lo que se está tocando, sus dependencias declaradas y lo
que cita.

**Por qué al escribir y no al abrir la sesión.** Al abrir llega el índice y eso
basta para orientarse; el choque aparece **en el momento de escribir**, y una
regla que llegó hace cuarenta turnos ya no está delante.

**Una vez por archivo y por sesión** (`CA-02`). Repetirlo en cada edición del
mismo archivo lo vuelve ruido, y el ruido se deja de leer — que es como muere
un aviso.

**Y nunca detiene.** Es información para decidir mejor, no una comprobación: lo
que se comprueba tiene su validador. Sale siempre con 0.
"""
import json
import os
import sys

import comun
import relacionadas
from comun import RAIZ, preparar_salida

# Dónde se recuerda qué se avisó ya. Es estado de una sesión, no del
# repositorio, así que nunca se versiona.
MARCA = os.path.join(".agente", "avisado-relacionadas.txt")


def _donde_recordar(raiz):
    """El archivo donde se anota lo ya avisado.

    En `.agente/` si el proyecto la tiene. **El estándar no se instala a sí
    mismo**, así que ahí no existe: se cae a la carpeta temporal del sistema,
    con la raíz en el nombre para no mezclar dos proyectos.
    """
    if os.path.isdir(os.path.join(raiz, ".agente")):
        return os.path.join(raiz, MARCA)
    import hashlib
    import tempfile
    huella = hashlib.sha1(raiz.encode("utf-8")).hexdigest()[:12]
    return os.path.join(tempfile.gettempdir(),
                        "agente-avisado-relacionadas-%s.txt" % huella)


def raiz_pedida(argv):
    for i, a in enumerate(argv):
        if a == "--raiz" and i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(RAIZ)


def archivo_editado(datos):
    entrada = (datos or {}).get("tool_input") or {}
    return entrada.get("file_path") or entrada.get("filePath") or ""


def _ya_se_aviso(raiz, sesion, rel):
    """Si ya se avisó de este archivo en esta sesión. Lo anota si no."""
    marca = _donde_recordar(raiz)
    clave = "%s\t%s" % (sesion, rel)
    try:
        if os.path.isfile(marca):
            with open(marca, encoding="utf-8") as f:
                if clave in f.read().splitlines():
                    return True
        with open(marca, "a", encoding="utf-8") as f:
            f.write(clave + "\n")
    except OSError:
        return False                    # no poder recordarlo no calla el aviso
    return False


def main():
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:])

    try:
        datos = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    ruta = archivo_editado(datos)
    if not ruta or not ruta.lower().endswith(".md"):
        return 0
    try:
        if os.path.commonpath([os.path.abspath(ruta), raiz]) != raiz:
            return 0
    except ValueError:                  # otra unidad en Windows
        return 0

    rel = relacionadas.relacionadas(ruta, raiz)
    texto = relacionadas.como_texto(rel, raiz)
    if not texto:
        return 0                        # `CA-03`: lo que no le toca, silencio

    if _ya_se_aviso(raiz, (datos or {}).get("session_id") or "",
                    os.path.relpath(os.path.abspath(ruta), raiz)):
        return 0

    print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
