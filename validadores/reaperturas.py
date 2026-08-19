# -*- coding: utf-8 -*-
"""`09·10` · Qué fases se reabrieron, y cuántas veces.

**Hoy una fase reabierta y una fase nueva no se distinguen**, así que la medida
de retrabajo no existe. Y el retrabajo es la señal más directa de que una
especificación salió incompleta — no para calificar a nadie, sino **para saber
qué parte del flujo lo produce**.

**Se deriva de la historia del archivo, no de sus palabras.** Las reaperturas se
escriben en prosa y cada una con las suyas —«reabierta», «se reabrió», «vuelta a
cerrar»—; buscar la palabra encuentra unas y se pierde otras, y además cuenta
las que solo *hablan* de reabrir. Lo que no se puede escribir de dos formas es
**una casilla que estaba marcada y dejó de estarlo**.

**Qué cuenta como reapertura:** que una estación de cierre —7 pruebas, 8 cierre
documental, 9 commit— pase de marcada a sin marcar en un guardado posterior.
Volver atrás desde el cierre es reabrir; corregir algo antes de haber cerrado,
no.
"""
import os
import re
import subprocess

import comun
from comun import AVISO, Hallazgo, relativo

# Las tres que solo se marcan al cerrar. Retroceder desde cualquiera de ellas es
# volver sobre trabajo dado por terminado.
CIERRE = (7, 8, 9)

_FILA = re.compile(r"(?m)^\|\s*(\d+)\s*\|[^|]*\|[^|]*\|\s*(.*?)\s*\|")


def _marcadas(texto):
    """`{número de estación: si está marcada}` de la tabla de estaciones."""
    salida = {}
    for m in _FILA.finditer(texto):
        try:
            n = int(m.group(1))
        except ValueError:
            continue
        salida[n] = "☑" in m.group(2)
    return salida


def _versiones(raiz, rel):
    """El archivo en cada commit que lo tocó, del más viejo al más nuevo."""
    r = subprocess.run(["git", "-C", raiz, "log", "--reverse", "--format=%h", "--", rel],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=60)
    if r.returncode:
        return []
    salida = []
    for commit in [c for c in r.stdout.split("\n") if c.strip()]:
        v = subprocess.run(["git", "-C", raiz, "show", "%s:%s" % (commit, rel)],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60)
        if v.returncode == 0:
            salida.append((commit, v.stdout))
    return salida


def reaperturas(raiz=None):
    """`[(ruta, [commits donde se reabrió])]` de cada fase que volvió atrás."""
    raiz = raiz or comun.RAIZ
    salida = []
    base = os.path.join(raiz, "documentacion", "epicas")
    if not os.path.isdir(base):
        return salida

    for carpeta, _sub, archivos in os.walk(base):
        if "estado-fase.md" not in archivos:
            continue
        ruta = os.path.join(carpeta, "estado-fase.md")
        rel = os.path.relpath(ruta, raiz).replace("\\", "/")
        vueltas, antes = [], {}
        for commit, texto in _versiones(raiz, rel):
            ahora = _marcadas(texto)
            for n in CIERRE:
                if antes.get(n) and ahora.get(n) is False:
                    vueltas.append(commit)
                    break
            antes = ahora or antes
        if vueltas:
            salida.append((ruta, vueltas))
    return salida


def validar(raiz=None):
    """Un aviso por fase reabierta. **Nunca una falla.**

    Reabrir una fase **es lo correcto** cuando lo que falla es ese trabajo y su
    documentación decía que estaba hecho: así se hizo con `A-EP-005-HU-008` y
    con `A-EP-007-HU-006`. Lo que se mide no es un incumplimiento — es de dónde
    sale el retrabajo.
    """
    hallazgos = []
    for ruta, vueltas in reaperturas(raiz):
        hallazgos.append(Hallazgo(
            AVISO, ruta, 0,
            f"esta fase volvió atrás desde una estación de cierre "
            f"{len(vueltas)} vez(ces) — es retrabajo, y sirve para ver qué "
            f"parte del flujo lo produce"))
    return hallazgos


def linea_resumen(raiz=None):
    """Cuántas fases y cuántas vueltas. Va aunque no haya ninguna."""
    datos = reaperturas(raiz)
    total = sum(len(v) for _r, v in datos)
    return "Fases reabiertas: %d · vueltas atrás en total: %d" % (len(datos), total)


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("reaperturas")
