# -*- coding: utf-8 -*-
"""La transcripción del histórico **solo crece**: se agrega, no se reescribe.

**De dónde sale.** Del análisis contra `notas/estructura.md` (§8 Auditoría):
un registro de auditoría que se puede reescribir sin que nadie lo note no es
un registro de auditoría. La transcripción la escribe el programa
(`hook_historico.py`) turno a turno; si su pasado cambió, alguien lo editó a
mano — y eso es lo que este validador deja a la vista.

**Cómo lo comprueba.** Para cada transcripción con cambios sin confirmar, el
contenido ya confirmado tiene que ser el **prefijo** del actual: lo nuevo se
agrega al final. La renombrada por `historico.py --renombrar` no aparece —para
el control de versiones es un archivo nuevo— así que la vía sancionada no da
falsos positivos.

**Todo AVISO, no FALLA.** Puede haber una edición legítima —tapar una clave
que se filtró antes de que exista el enganche que la tapa—; la confirma un
humano. Detecta y reporta: no impide.
"""
import os
import re
import subprocess

import comun
from comun import AVISO, Hallazgo, leer

CARPETA = "historico-chat"

# Una transcripción: `AAAA-MM-DD-<tema>.md`, en la raíz de la carpeta.
_TRANSCRIPCION = re.compile(r"^\d{4}-\d{2}-\d{2}.*\.md$")


def _normal(texto):
    """Sin finales de línea de Windows: el control de versiones los cambia."""
    return texto.replace("\r\n", "\n")


def solo_crecio(viejo, nuevo):
    """True si `nuevo` es `viejo` más lo agregado al final (o igual)."""
    return _normal(nuevo).startswith(_normal(viejo))


def _git(raiz, *args):
    """La salida del comando, o "" si el comando no se pudo correr."""
    try:
        r = subprocess.run(["git", "-C", raiz, *args],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
    except OSError:
        return ""
    return r.stdout if r.returncode == 0 else ""


def modificadas(raiz):
    """Las transcripciones ya confirmadas que tienen cambios sin confirmar."""
    salida = []
    estado = _git(raiz, "status", "--porcelain", "--", CARPETA)
    for linea in estado.splitlines():
        if len(linea) < 4 or "M" not in linea[:2]:
            continue
        rel = linea[3:].strip().strip('"')
        nombre = os.path.basename(rel)
        if (os.path.dirname(rel).replace("\\", "/") == CARPETA
                and _TRANSCRIPCION.match(nombre)):
            salida.append(rel.replace("\\", "/"))
    return salida


def validar(raiz=None):
    """Un AVISO por transcripción cuyo pasado confirmado cambió."""
    raiz = raiz or comun.RAIZ
    hallazgos = []
    for rel in modificadas(raiz):
        confirmado = _git(raiz, "show", f"HEAD:{rel}")
        if not confirmado:
            continue
        actual = leer(os.path.join(raiz, rel))
        if not solo_crecio(confirmado, actual):
            hallazgos.append(Hallazgo(
                AVISO, os.path.join(raiz, rel), 0,
                "la transcripción no solo creció: su contenido ya confirmado "
                "cambió. El histórico se agrega, no se reescribe — si la "
                "edición es legítima (tapar una clave filtrada), que quede "
                "dicha en el mensaje del commit"))
    return hallazgos


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("inmutable")
