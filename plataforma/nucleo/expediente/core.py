# -*- coding: utf-8 -*-
"""Arma el expediente de un proyecto. **Solo lee; no guarda nada.**

El expediente **se calcula al pedirlo**, leyendo lo que Importación ya trajo.
Guardarlo crearía una segunda verdad que envejece, que es lo que `DA-01` viene a
evitar.

**Lo que entrega no es un archivo**: es el conjunto ordenado y, sobre todo, las
tres listas que dicen en qué estado está.

- **Lo que falta**, con su nombre. Un expediente que no dice qué le falta es
  peor que no tenerlo: se entrega incompleto sin que nadie lo note.
- **Lo incompleto**, con cuántos huecos sin llenar conserva.
- **Lo que no encaja**, que no se acomoda al grupo más parecido.

**La auditoría y la memoria no entran**, por decisión escrita del 2026-08-31.
"""
import io
import os
import re

from django.conf import settings

from nucleo.importacion.models import Traido
from . import orden

# **El hueco sin llenar es la marca de la casa, y solo esa.** `13·DOC19` fija
# `«…»` como la marca de todos los modelos, y eso es lo que se cuenta.
#
# **Lo que no se cuenta, y se dice:** un hueco escrito con texto adentro no se
# distingue de una cita sin leer. En esta casa se cita con esas mismas comillas
# todo el tiempo, así que contarlas daría por incompleto cualquier documento
# bien escrito.
MARCA_DEL_HUECO = u"«…»"

# Una fase se reconoce por su carpeta: `A-EP-005-HU-012-lo-que-sea`.
_FASE = re.compile(r"(?:^|/)([A-Z]-EP-\d+-HU-\d+-[^/]+)/")


def _texto_de(traido):
    """El texto guardado de un documento, o `""` si no se puede leer."""
    ruta = os.path.join(str(settings.CARPETA_DATOS),
                        traido.guardado_en.replace("/", os.sep))
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as abierto:
            return abierto.read()
    except OSError:
        return ""


def huecos_de(texto):
    """Cuántos espacios por llenar conserva un documento.

    Cuenta la marca de la casa. Un hueco escrito con texto adentro no se
    cuenta, y el porqué está arriba: no se distingue de una cita.
    """
    return (texto or "").count(MARCA_DEL_HUECO)


def fase_de(origen):
    """La carpeta de la fase a la que pertenece ese documento, o `""`."""
    m = _FASE.search((origen or "").replace("\\", "/"))
    return m.group(1) if m else ""


def _fases_de(documentos):
    """Las fases que aparecen, en orden de nombre. Su letra dice cuál va antes."""
    return sorted({fase_de(d.origen) for d in documentos if fase_de(d.origen)})


def armar(proyecto, hasta=None):
    """El expediente de un proyecto. `{"grupos","falta","incompletos","sin_encajar","fuera_del_alcance"}`.

    `hasta` es el nombre de una fase: se incluye lo que llega hasta ella, y lo
    que queda fuera **se dice**. Recortar en silencio es lo mismo que perder.
    """
    traidos = list(Traido.objects.filter(proyecto=proyecto))

    expediente = {"grupos": [], "falta": [], "incompletos": [],
                  "sin_encajar": [], "fuera_del_alcance": []}
    if not traidos:
        return expediente

    fases = _fases_de(traidos)
    if hasta:
        # Se corta por el nombre de la fase, que empieza con su letra: la `A`
        # va antes que la `B` porque así se nombran (`02·F12`).
        adentro = {f for f in fases if f <= hasta}
    else:
        adentro = set(fases)

    por_grupo = {}
    for traido in traidos:
        if not orden.entra(traido.tipo):
            if not traido.tipo:
                # **Lo que Importación no reconoció se dice.** Saltarlo en
                # silencio es perder sin que nadie se entere.
                expediente["sin_encajar"].append(
                    {"origen": traido.origen, "tipo": ""})
            continue

        grupo = orden.grupo_de(traido.tipo)
        if not grupo:
            expediente["sin_encajar"].append(
                {"origen": traido.origen, "tipo": traido.tipo})
            continue

        fase = fase_de(traido.origen)
        if fase and fase not in adentro:
            expediente["fuera_del_alcance"].append(
                {"origen": traido.origen, "fase": fase})
            continue

        por_grupo.setdefault(grupo, []).append(traido)

    for nombre, _tipos in orden.GRUPOS:
        documentos = por_grupo.get(nombre, [])
        if not documentos:
            continue
        # **Dentro del grupo, también el orden del ciclo.** Por nombre de
        # archivo, los cinco de una fase saldrían al revés: el cierre antes
        # que el plan. La fase se agrupa por su carpeta, y adentro va el orden.
        documentos.sort(key=lambda d: (fase_de(d.origen),
                                       orden.posicion_en_grupo(d.tipo),
                                       d.origen))
        expediente["grupos"].append({"grupo": nombre, "documentos": documentos})

    expediente["falta"] = _lo_que_falta(traidos, adentro)
    expediente["incompletos"] = _lo_incompleto(por_grupo)
    return expediente


def _lo_que_falta(traidos, adentro):
    """Los documentos que el ciclo espera y no están, con su nombre.

    **Se calcula contra lo que el ciclo espera de verdad**, no contra una lista
    escrita al lado: los cinco documentos de una fase ya están escritos en el
    estándar, y una lista aparte envejecería con el proyecto (`S-091`).

    **Nunca se inventa un documento ausente:** lo que falta se nombra, y no
    aparece en el expediente como si existiera.
    """
    falta = []
    por_fase = {}
    for traido in traidos:
        fase = fase_de(traido.origen)
        if fase and fase in adentro:
            por_fase.setdefault(fase, set()).add(traido.tipo)

    for fase in sorted(por_fase):
        for tipo in orden.DE_UNA_FASE:
            if tipo not in por_fase[fase]:
                falta.append({"donde": fase, "que": tipo})
    return falta


def _lo_incompleto(por_grupo):
    """Los documentos que conservan huecos sin llenar, con cuántos.

    Se cuenta **leyendo el texto guardado**: el índice no guarda el contenido, y
    dar por completo un documento sin abrirlo es la clase de suposición que este
    módulo existe para no hacer.
    """
    incompletos = []
    for documentos in por_grupo.values():
        for traido in documentos:
            cuantos = huecos_de(_texto_de(traido))
            if cuantos:
                incompletos.append({"origen": traido.origen,
                                    "tipo": traido.tipo,
                                    "huecos": cuantos})
    incompletos.sort(key=lambda d: (-d["huecos"], d["origen"]))
    return incompletos


def cuantos_documentos(expediente):
    """Cuántos documentos entraron al expediente."""
    return sum(len(g["documentos"]) for g in expediente["grupos"])
