# -*- coding: utf-8 -*-
"""`EP-023 · HU-003 · CA-11` · El proyecto se entera cuando su pendiente se resuelve.

**Qué resuelve.** Un proyecto que encuentra un defecto del estándar lo reporta
con un pendiente allá y deja otro de seguimiento acá (`02·F24`). Con la forma
vieja, el aviso de vuelta lo escribía `cerrar.py` al mover el pendiente a
`pendientes/hecho/`, en la carpeta `pendientes/` del proyecto. La forma nueva no
mueve nada, y esa carpeta ya no se crea: el aviso no llegaba a nadie.

**Cómo lo resuelve** (análisis 13 del pendiente 103, acuerdos 3 y 4). Cuando la
fase que cumple el plan del pendiente anota su commit, para cada pendiente
reportado que quedó cerrado sigue los enlaces hasta el seguimiento del
proyecto: el pendiente del estándar enlaza el hallazgo del proyecto, y ese
hallazgo enlaza su pendiente. Ahí deja `aviso-resuelto.md`, una sola vez. El
seguimiento cierra cuando el proyecto pone la fecha en su línea «Comprobado».

**Lo que no hace, y se declara.** No toca el código ni el pendiente del
proyecto: solo escribe el aviso. Si un enlace falta o lleva a otra parte, no
escribe y dice cuál.
"""
import os
import re

import comun
import pendientes

AVISO = "aviso-resuelto.md"
COMPROBADO = pendientes._COMPROBADO

_DE_DONDE = re.compile(r"^\|\s*\*\*De dónde sale\*\*\s*\|(.+?)\|\s*$", re.M)
_ENLACE_H = re.compile(r"\[[^\]]*?(H-\d+)[^\]]*\]\(([^)#\s]+)")
_FILA_PENDIENTE = re.compile(r"^\|\s*Pendiente\s*\|(.*)\|\s*$", re.M)
_ENLACE = re.compile(r"\]\(([^)#\s]+)")

PLANTILLA = """# Aviso: el estándar resolvió el pendiente que este proyecto reportó

Lo escribió `validadores/aviso_resuelto.py` el {fecha}. No se edita, salvo la línea «Comprobado».

| | |
|---|---|
| **Pendiente del estándar** | `{pendiente}` |
| **Versión que trae la corrección** | {version} |

## Qué hacer con esto

1. Actualizar el estándar en este proyecto.
2. Comprobar la corrección con lo que dice el pendiente de seguimiento de esta carpeta.
3. Poner la fecha en la línea de abajo. Desde ahí el seguimiento queda cerrado.

**Comprobado:** no
"""


def _destino(enlace, desde):
    return os.path.normpath(os.path.join(os.path.dirname(desde), enlace.replace("/", os.sep)))


def _bloque_del_hallazgo(texto, h):
    """El texto del hallazgo `### H-N` hasta el siguiente encabezado o raya."""
    m = re.search(r"^### %s\b.*$" % re.escape(h), texto, re.M)
    if not m:
        return ""
    fin = re.search(r"^(#{2,3} |---\s*$)", texto[m.end():], re.M)
    return texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]


def seguimiento_de(carpeta):
    """`(carpeta del seguimiento, "")` o `("", por qué no se encontró)`."""
    ruta = os.path.join(carpeta, "pendiente.md")
    fila = _DE_DONDE.search(comun.leer(ruta)) if os.path.isfile(ruta) else None
    if not fila:
        return "", "el pendiente no tiene «De dónde sale»"
    for h, enlace in _ENLACE_H.findall(fila.group(1)):
        resumen = _destino(enlace, ruta)
        if not os.path.isfile(resumen):
            return "", "el hallazgo %s apunta a %s, que no existe" % (h, enlace)
        bloque = _bloque_del_hallazgo(comun.leer(resumen), h)
        fila_p = _FILA_PENDIENTE.search(bloque)
        if not fila_p:
            return "", "el hallazgo %s no enlaza su pendiente" % h
        for e in _ENLACE.findall(fila_p.group(1)):
            destino = _destino(e, resumen)
            if os.path.basename(destino) == "pendiente.md":
                destino = os.path.dirname(destino)
            if os.path.isfile(os.path.join(destino, "pendiente.md")):
                return destino, ""
        return "", "el pendiente que enlaza el hallazgo %s no existe" % h
    return "", "«De dónde sale» no enlaza un hallazgo"


def reportado(carpeta, estandar):
    """`True` si el pendiente enlaza un hallazgo que está fuera del estándar."""
    ruta = os.path.join(carpeta, "pendiente.md")
    fila = _DE_DONDE.search(comun.leer(ruta)) if os.path.isfile(ruta) else None
    raiz = os.path.normcase(os.path.abspath(estandar)) + os.sep
    for _, enlace in _ENLACE_H.findall(fila.group(1) if fila else ""):
        if not os.path.normcase(_destino(enlace, ruta)).startswith(raiz):
            return True
    return False


def comprobado(carpeta):
    """`True` si el aviso de la carpeta del seguimiento ya tiene fecha de comprobado."""
    ruta = os.path.join(carpeta, AVISO)
    return os.path.isfile(ruta) and bool(COMPROBADO.search(comun.leer(ruta)))


def avisar(estandar, fecha, version, escribir=True):
    """`(escritos, sin_entregar)`: rutas de los avisos, y `(pendiente, por qué)` de los que no llegaron."""
    estandar = os.path.abspath(estandar)
    escritos, sin_entregar = [], []
    for carpeta in pendientes.carpetas(estandar):
        if not reportado(carpeta, estandar) or pendientes.estado(carpeta, estandar) != "cerrado":
            continue
        destino, porque = seguimiento_de(carpeta)
        if not destino:
            sin_entregar.append((carpeta, porque))
            continue
        aviso = os.path.join(destino, AVISO)
        if os.path.exists(aviso):
            continue                    # una sola vez
        if escribir:
            with open(aviso, "w", encoding="utf-8", newline="\n") as f:
                f.write(PLANTILLA.format(fecha=fecha, version=version,
                                         pendiente=os.path.relpath(carpeta, estandar).replace(os.sep, "/")))
        escritos.append(aviso)
    return escritos, sin_entregar


if __name__ == "__main__":
    comun.no_es_punto_de_entrada(la_corre="adaptadores/claude-code/hook_estacion.py")
