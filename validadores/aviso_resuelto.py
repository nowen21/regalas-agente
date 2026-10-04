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
aviso llega con «Comprobado» lleno: Cimiento ya probó la corrección en el proyecto (análisis 1 del pendiente 110, acuerdo 7).

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

Lo escribió `validadores/aviso_resuelto.py` el {fecha}. No se edita.

| | |
|---|---|
| **Pendiente del estándar** | `{pendiente}` |
| **Versión que trae la corrección** | {version} |

## Cómo lo comprobó Cimiento

Cimiento reprodujo el caso en una copia de este proyecto, en el escenario donde se presentó, y comprobó que la corrección funciona antes de avisar (`02·F29`).

{prueba}

## Qué hacer con esto

Actualizar el estándar en este proyecto y seguir con el trabajo. El pendiente de seguimiento de esta carpeta queda cerrado.

**Comprobado:** {fecha}
"""

# `02·F29` · Lo que Cimiento comprobó en el proyecto que reportó, antes de avisar.
PRUEBA = "prueba-en-el-proyecto.md"
_RESULTADO = re.compile(r"^\*\*Resultado:\*\*\s*(pasa|falla)\s*$", re.M)


def anotar_prueba(carpeta, fecha, escenario, casos):
    """Escribe `prueba-en-el-proyecto.md` en la carpeta del reporte.

    `casos`: `[(qué se probó, cómo, pasó)]`. Pasa solo si pasan todos."""
    paso = bool(casos) and all(c[2] for c in casos)
    filas = "\n".join("| %s | %s | %s |" % (q, c, "Pasa" if p else "Falla") for q, c, p in casos)
    texto = ("# Prueba en el proyecto que reportó\n\n"
             "Hecha por Cimiento el %s, en %s (`02·F29`).\n\n"
             "| Qué se probó | Cómo | Resultado |\n|---|---|---|\n%s\n\n"
             "**Resultado:** %s\n" % (fecha, escenario, filas, "pasa" if paso else "falla"))
    with open(os.path.join(carpeta, PRUEBA), "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    return paso


def prueba_paso(carpeta):
    """Si Cimiento ya comprobó la corrección en el proyecto y pasó."""
    m = _RESULTADO.search(comun.leer(os.path.join(carpeta, PRUEBA)))
    return bool(m) and m.group(1) == "pasa"


def _tabla_de_la_prueba(carpeta):
    texto = comun.leer(os.path.join(carpeta, PRUEBA))
    m = re.search(r"(?ms)^\| Qué se probó.*?(?=^\*\*Resultado)", texto)
    return m.group(0).strip() if m else ""


def _destino(enlace, desde):
    return os.path.normpath(os.path.join(os.path.dirname(desde), enlace.replace("/", os.sep)))


def _bloque_del_hallazgo(texto, h):
    """El texto del hallazgo `### H-N` hasta el siguiente encabezado o raya."""
    m = re.search(r"^### %s\b.*$" % re.escape(h), texto, re.M)
    if not m:
        return ""
    fin = re.search(r"^(#{2,3} |---\s*$)", texto[m.end():], re.M)
    return texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]


def _seguimiento_directo(ruta, fila):
    """La carpeta del seguimiento que el reporte enlaza directo, fuera del
    estándar, o "" (análisis 1 del pendiente 110, acuerdo 5)."""
    raiz = os.path.normcase(os.path.abspath(comun.RAIZ)) + os.sep
    for enlace in _ENLACE.findall(fila):
        destino = _destino(enlace, ruta)
        if os.path.basename(destino) == "pendiente.md":
            destino = os.path.dirname(destino)
        if os.path.normcase(destino).startswith(raiz):
            continue
        if os.path.isfile(os.path.join(destino, "pendiente.md")):
            return destino
    return ""


def seguimiento_de(carpeta):
    """`(carpeta del seguimiento, "")` o `("", por qué no se encontró)`.

    Primero por el enlace directo que trae el reporte; si no lo trae, siguiendo
    el hallazgo del proyecto hasta su pendiente (análisis 1 del pendiente 110,
    acuerdo 5)."""
    ruta = os.path.join(carpeta, "pendiente.md")
    fila = _DE_DONDE.search(comun.leer(ruta)) if os.path.isfile(ruta) else None
    if not fila:
        return "", "el pendiente no tiene «De dónde sale»"
    directo = _seguimiento_directo(ruta, fila.group(1))
    if directo:
        return directo, ""
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
    # O enlaza directo su seguimiento en el proyecto (análisis 1 del pendiente 110, acuerdo 5).
    for enlace in _ENLACE.findall(fila.group(1) if fila else ""):
        destino = _destino(enlace, ruta)
        if destino.endswith("pendiente.md") and not os.path.normcase(destino).startswith(raiz):
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
        if not prueba_paso(carpeta):
            sin_entregar.append((carpeta, "Cimiento todavía no comprobó la corrección en el proyecto "
                                          "(falta %s con resultado «pasa»)" % PRUEBA))
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
                f.write(PLANTILLA.format(fecha=fecha, version=version, prueba=_tabla_de_la_prueba(carpeta),
                                         pendiente=os.path.relpath(carpeta, estandar).replace(os.sep, "/")))
        escritos.append(aviso)
    return escritos, sin_entregar


if __name__ == "__main__":
    comun.no_es_punto_de_entrada(la_corre="adaptadores/claude-code/hook_estacion.py")
