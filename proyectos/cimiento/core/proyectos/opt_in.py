# -*- coding: utf-8 -*-
"""`EP-026·HU-009` · Los capítulos opt-in de un proyecto.

Mandan los de la base de Cimiento (análisis 1 del pendiente 132, acuerdo 5). El
`CLAUDE.md` del proyecto, en su punto 5.1, queda para lo que la base no sabe: una
carpeta sin registro, o una base que no responde. Y es de donde sale lo que se
pasa a la base la primera vez, para que nada cambie el día del paso.

**Sin Django**: lo usa el recuperador de reglas, que corre en los enganches.
"""
import os
import re
import unicodedata

from .ajustes import CAPITULOS_OPT_IN, NO, SI, clave_opt_in

# «- **Patrón opt-in `15` (registros inmutables):** no»
_LINEA = re.compile(r"Patr[oó]n opt-in\s*`?(\d{2})`?[^:]*:\**\s*(.+)")


def _sin_tildes(texto):
    texto = unicodedata.normalize("NFKD", texto or "")
    return "".join(c for c in texto if not unicodedata.combining(c)).lower()


def del_texto(texto):
    """`{capítulo: True si está prendido}` de lo que diga el texto de un `CLAUDE.md`."""
    salida = {}
    for linea in (texto or "").splitlines():
        m = _LINEA.search(linea)
        if m:
            salida[m.group(1)] = _sin_tildes(m.group(2)).strip(" *`.«»").startswith("si")
    return salida


def del_claude_md(carpeta, archivos=None):
    """Lo que dice el `CLAUDE.md` de la carpeta; `{}` si no hay archivo o no se lee."""
    ruta = os.path.join(carpeta or "", "CLAUDE.md")
    if not carpeta or not os.path.isfile(ruta):
        return {}
    try:
        if archivos is not None:
            return del_texto(archivos.leer(ruta))
        with open(ruta, encoding="utf-8") as f:
            return del_texto(f.read())
    except Exception:                         # noqa: BLE001: un archivo roto no tumba el turno
        return {}


def apagados_segun(efectivos):
    """Los capítulos opt-in que los ajustes efectivos de un proyecto dejan apagados."""
    return frozenset(c for c in CAPITULOS_OPT_IN if efectivos[clave_opt_in(c)][0] != SI)


def pasar_a_la_base(proyectos, ajustes_del_proyecto):
    """Guarda en la base lo que dice el `CLAUDE.md` de cada proyecto, sin pisar lo
    que la base ya tenga. Recibe los modelos para servirle también a la migración.
    Devuelve cuántos ajustes creó: la segunda vez, ninguno.

    Lo que el archivo no nombra queda en «sí»: así regía antes, y el paso no cambia
    qué reglas llegan."""
    creados = 0
    for proyecto in proyectos.objects.all():
        dice = del_claude_md(proyecto.ruta)
        for capitulo in CAPITULOS_OPT_IN:
            prendido = dice.get(capitulo, True)
            _, nuevo = ajustes_del_proyecto.objects.get_or_create(
                proyecto=proyecto, clave=clave_opt_in(capitulo), defaults={"valor": SI if prendido else NO})
            creados += nuevo
    return creados
