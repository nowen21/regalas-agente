# -*- coding: utf-8 -*-
"""Las reglas que rigen en un proyecto, listas para que el agente las reciba.

**Lo que se entrega es el texto, no un resumen.** Un resumen de una regla es
otra regla, y la que el agente obedecería sería la del resumen. Se entregan los
capítulos como están escritos.

**Y si esto no responde, la fuente sigue ahí.** El cuerpo de reglas son archivos
en el proyecto: quien no pueda usar la plataforma los lee y trabaja igual. Esta
pieza acelera y ordena; no es un intermediario sin el cual no se puede.

Por eso, cuando algo falla, **se dice dónde está la fuente** en vez de devolver
una lista vacía. Una lista vacía se leería como «este proyecto no tiene reglas»,
que es la peor respuesta posible.
"""
import io
import os
import time

from . import catalogo

# El orden en que se leen los capítulos: el número que llevan en el nombre.
# **No es alfabético**: `02` va antes que `13`, y alfabéticamente también, pero
# `9` iría después de `13` si alguien numera sin cero delante.


def _capitulos(raiz):
    """Los archivos del cuerpo de reglas, en el orden de sus números."""
    base = os.path.join(raiz, "base")
    if not os.path.isdir(base):
        return []
    encontrados = []
    for actual, carpetas, archivos in os.walk(base):
        carpetas.sort()
        for nombre in sorted(archivos):
            if nombre.endswith(".md"):
                encontrados.append(os.path.join(actual, nombre))
    return encontrados


def entregar(raiz, version_que_rige=""):
    """El cuerpo de reglas de ese proyecto, para dárselo al agente.

    Devuelve `{"se_pudo", "porque", "version", "capitulos", "vigentes",
    "caracteres", "segundos", "donde_esta_la_fuente"}`.

    **`donde_esta_la_fuente` va siempre**, se haya podido o no: es lo que
    permite trabajar sin esto.
    """
    empezo = time.time()
    fuente = os.path.join(raiz, "base")

    if not os.path.isdir(fuente):
        return {"se_pudo": False,
                "porque": "este proyecto no tiene cuerpo de reglas en %s"
                          % fuente,
                "version": version_que_rige, "capitulos": [], "vigentes": 0,
                "caracteres": 0, "segundos": time.time() - empezo,
                "donde_esta_la_fuente": fuente}

    try:
        vigentes = len(catalogo.vigentes(raiz))
    except catalogo.NoHayCuerpoDeReglas as porque:
        return {"se_pudo": False, "porque": str(porque),
                "version": version_que_rige, "capitulos": [], "vigentes": 0,
                "caracteres": 0, "segundos": time.time() - empezo,
                "donde_esta_la_fuente": fuente}

    capitulos, caracteres = [], 0
    for ruta in _capitulos(raiz):
        try:
            with io.open(ruta, encoding="utf-8", errors="replace") as archivo:
                texto = archivo.read()
        except OSError:
            continue
        capitulos.append({"ruta": os.path.relpath(ruta, raiz).replace(os.sep, "/"),
                          "texto": texto})
        caracteres += len(texto)

    return {"se_pudo": True, "porque": "", "version": version_que_rige,
            "capitulos": capitulos, "vigentes": vigentes,
            "caracteres": caracteres, "segundos": time.time() - empezo,
            "donde_esta_la_fuente": fuente}


def encabezado(entrega):
    """La línea que le dice al agente qué está recibiendo y bajo qué versión."""
    if not entrega["se_pudo"]:
        return ("No se pudieron entregar las reglas: %s. **La fuente sigue "
                "siendo legible en %s**, y con eso se puede trabajar."
                % (entrega["porque"], entrega["donde_esta_la_fuente"]))
    return ("Reglas vigentes: %d, en %d capítulo(s)%s. Entregadas en %.2f s."
            % (entrega["vigentes"], len(entrega["capitulos"]),
               (", bajo la versión %s" % entrega["version"])
               if entrega["version"] else "",
               entrega["segundos"]))
