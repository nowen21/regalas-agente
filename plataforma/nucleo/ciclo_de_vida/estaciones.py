# -*- coding: utf-8 -*-
"""En qué estación va cada fase — `F-012`.

**El estado lo fija lo escrito, no lo que la fase dice de sí misma.** Un
`estado-fase.md` trae las dos cosas: una tabla con las trece estaciones marcadas
y una frase que anuncia en cuál va. La tabla manda. Cuando las dos no coinciden
**se dice**, en vez de elegir una en silencio: que no coincidan es justamente la
señal de que alguien avanzó sin marcar.

**Sirve para ver todas las fases a la vez.** Una sola se ve abriendo su
documento; lo que no se puede a mano es mirar doscientas.
"""
import io
import os
import re

# `| 12 | Commit | 👤 autorizado | ☐ |` — el número, el nombre, la puerta y cómo
# quedó. La marca puede traer texto detrás («☑ 2026-09-01: la épica entera»).
_FILA = re.compile(
    r"^\|\s*(\d{1,2})\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$",
    re.M)
# Lo que la fase dice de sí misma. Se lee para poder contrastarlo, no para creerlo.
_DECLARADA = re.compile(r"\*\*Estación actual:\*\*\s*(\d{1,2})")
_ACTUALIZADA = re.compile(
    r"\*\*Última actualización\*\*\s*\|\s*(\d{4}-\d{2}-\d{2})")

# **Dos marcas quieren decir lo mismo, y las dos están en el repositorio.** Las
# fases viejas cierran con `✅` y las nuevas con `☑`. Ninguna se reescribe: el que
# se adapta es el que lee (`S-110`).
CUMPLIDAS = (u"☑", u"✅")
PENDIENTES = (u"☐", u"⬜")
NO_APLICA = "N/A"

# Cuando ninguna estación queda pendiente.
TERMINADA = 0

# El modelo vigente. Las fases viejas traen tablas de once o de menos, y no se
# reescriben: son fases cerradas, y reescribir una fase cerrada es peor que
# tener dos modelos.
TRECE = 13


def _como_quedo(celda):
    """`cumplida`, `pendiente`, `no aplica` o `sin marcar`.

    **«Sin marcar» no es «pendiente», y meterlos en el mismo cajón miente.** Las
    fases más viejas no marcan la casilla: escriben qué pasó con esa estación
    («no se hizo como estación aparte», «pendiente de aprobación»). Decir de esas
    que la puerta está pendiente inventa un estado que el documento no declaró.
    """
    if NO_APLICA in celda:
        return "no aplica"
    if any(marca in celda for marca in CUMPLIDAS):
        return "cumplida"
    if any(marca in celda for marca in PENDIENTES):
        return "pendiente"
    return "sin marcar"


def de_un_texto(texto):
    """Lee un `estado-fase.md` y dice en qué estación va.

    Devuelve `{"estaciones", "actual", "nombre", "puerta", "declarada",
    "coincide", "actualizada", "cuantas_cumplidas"}`.
    """
    estaciones = []
    for numero, nombre, puerta, marca in _FILA.findall(texto):
        # La cabecera de la tabla no trae número, así que no llega acá; una fila
        # de otra tabla que empiece por un número, sí. Se filtran por rango.
        n = int(numero)
        if not 1 <= n <= 13:
            continue
        estaciones.append({"numero": n, "nombre": nombre,
                           "puerta": puerta, "estado": _como_quedo(marca)})
    estaciones.sort(key=lambda una: una["numero"])

    pendientes = [una for una in estaciones
                  if una["estado"] in ("pendiente", "sin marcar")]
    actual = pendientes[0] if pendientes else None
    declarada = _DECLARADA.search(texto)
    numero_declarado = int(declarada.group(1)) if declarada else 0
    actualizada = _ACTUALIZADA.search(texto)

    # **Cuántas estaciones declara la tabla, no cuántas debería.** En este
    # repositorio conviven varios modelos: 102 fases con trece estaciones, 83
    # con once, y 24 con menos o con ninguna. Comparar la frase con la tabla
    # solo tiene sentido cuando las dos hablan del mismo modelo; si no, la
    # estación 12 de una quiere decir otra cosa que la 12 de la otra.
    modelo = len(estaciones)
    comparables = modelo == TRECE

    return {
        "estaciones": estaciones,
        "modelo": modelo,
        "comparable": comparables,
        "actual": actual["numero"] if actual else TERMINADA,
        "nombre": actual["nombre"] if actual else "",
        "puerta": actual["puerta"] if actual else "",
        "como_quedo": actual["estado"] if actual else "cumplida",
        "declarada": numero_declarado,
        "coincide": (not comparables or not numero_declarado or not actual
                     or numero_declarado == actual["numero"]),
        "actualizada": actualizada.group(1) if actualizada else "",
        "cuantas_cumplidas": len([una for una in estaciones
                                  if una["estado"] == "cumplida"]),
        "sin_marcar": len([una for una in estaciones
                           if una["estado"] == "sin marcar"]),
    }


def de_una_fase(ruta):
    """Lo mismo, leyendo el archivo. Devuelve `{}` si no se puede abrir."""
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as abierto:
            texto = abierto.read()
    except OSError:
        return {}
    leido = de_un_texto(texto)
    leido["ruta"] = ruta
    leido["fase"] = os.path.basename(os.path.dirname(ruta))
    return leido


def de_un_proyecto(raiz):
    """Todas las fases del proyecto, de la menos avanzada a la más avanzada.

    Se ordenan así a propósito: lo que hay que mirar primero es lo que lleva más
    tiempo sin moverse, no lo que ya casi está.
    """
    epicas = os.path.join(raiz, "documentacion", "epicas")
    fases = []
    for carpeta, _dirs, archivos in os.walk(epicas):
        if "estado-fase.md" in archivos:
            leida = de_una_fase(os.path.join(carpeta, "estado-fase.md"))
            if leida:
                fases.append(leida)
    fases.sort(key=lambda una: (una["actual"] == TERMINADA,
                                una["actual"], una["fase"]))
    return fases


def detenida_desde(fase, hoy):
    """Cuántos días lleva sin moverse, o `-1` si no lo dice.

    **Una fase detenida tiene que decir desde cuándo**, y la única fecha que un
    `estado-fase.md` guarda es la de su última actualización. No es la fecha en
    que se detuvo: es la última vez que alguien la tocó, que es lo más cercano
    que el texto sabe.
    """
    import datetime
    if not fase.get("actualizada"):
        return -1
    try:
        cuando = datetime.date(*[int(p) for p in fase["actualizada"].split("-")])
        contra = datetime.date(*[int(p) for p in hoy.split("-")])
    except (ValueError, TypeError):
        return -1
    return (contra - cuando).days


def resumen(fases):
    """Cuántas hay, cuántas terminadas, y en cuántas la tabla no coincide."""
    return {
        "cuantas": len(fases),
        "terminadas": len([una for una in fases if una["actual"] == TERMINADA]),
        "sin_coincidir": len([una for una in fases if not una["coincide"]]),
        "con_estaciones_sin_marcar": len([una for una in fases
                                          if una.get("sin_marcar")]),
        "de_otro_modelo": len([una for una in fases
                               if not una.get("comparable")]),
    }


def dicho(fase):
    """La frase para la consola, de una fase."""
    if fase["actual"] == TERMINADA:
        return "%s — las trece estaciones pasadas" % fase["fase"]
    if fase.get("como_quedo") == "sin marcar":
        frase = ("%s — estación %d · %s. **No se marcó**: el documento cuenta "
                 "qué pasó con ella en vez de marcarla, así que no se sabe si "
                 "la puerta «%s» se cumplió" % (
                     fase["fase"], fase["actual"], fase["nombre"],
                     fase["puerta"] or "—"))
    else:
        frase = "%s — estación %d · %s. Falta: %s" % (
            fase["fase"], fase["actual"], fase["nombre"], fase["puerta"] or "—")
    if not fase.get("comparable"):
        frase += (" · su tabla es de %d estaciones, no de trece: no se compara "
                  "con lo que dice la frase" % fase.get("modelo", 0))
    if not fase["coincide"]:
        frase += (" · OJO: el documento dice ir en la %d, y la tabla dice %d. "
                  "Manda la tabla" % (fase["declarada"], fase["actual"]))
    return frase
