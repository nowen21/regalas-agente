# -*- coding: utf-8 -*-
"""`EP-005 · HU-010` · Qué reglas se relacionan con lo que se está escribiendo.

**El defecto que esto cierra pasó el mismo día que se construyó.** Se escribió
una frase en `02·F2` que chocaba con `02·F0` — la regla que `F2` cita en su
propio texto, dos archivos más allá. El checklist tiene una fila para eso, la
17, y se selló en verde sin mirar.

**No es un problema de cargar contexto: es de buscar.** Mandar el capítulo
entero son 98 KB y obliga a encontrar la relación uno mismo, que es justo lo
que falla. Lo que hace falta es contestar una pregunta: **¿qué se relaciona con
esto?**

Y la respuesta ya está en el repositorio, sin base de datos de por medio:

- `citas.py` sabe dónde vive cada regla.
- `metareglas.py` lee las dependencias declaradas — `extiende`, `depende de`,
  `deroga`.
- `20·M15` obliga a que toda cita lleve su enlace, así que **quién cita a quién
  está escrito y es seguible**.

**Las que la citan pesan más que las que ella cita**, y por eso van primero:
cambiar una regla rompe a quien dependía de ella, y ese es el lado que no se
mira. Lo que ella cita al menos está delante mientras se escribe.
"""
import os
import re

import citas
import comun
import metareglas
from comun import RAIZ, leer, relativo

# `[`02·F0`](…)` o `02·F0` suelto — lo que `M15` pide y lo que se escribe igual.
_CITA = re.compile(r"(?:(\d{2})·)?\b([A-Z]{1,4}\d+(?:\.\d+)?)\b")


def _capitulo_de(ruta, raiz):
    """El capítulo dueño de un archivo, por su carpeta. `None` si no lo gobierna
    ninguno.

    **Por carpeta y no por tipo de documento** (duda 41): el tipo hay que
    adivinarlo; la carpeta se lee de la ruta, que es lo mismo que ya hace
    `cargador.py` al repartir las reglas al arrancar.
    """
    rel = os.path.relpath(os.path.abspath(ruta), raiz).replace("\\", "/")
    tramos = rel.split("/")
    if tramos[0] == "base":
        return "20"                     # escribir una regla lo gobierna el 20
    if tramos[0] == "documentacion" and len(tramos) > 1 and tramos[1] == "epicas":
        return "02"                     # la cadena y las fases
    if tramos[0] == "pendientes":
        return "02"                     # `F23`: el pendiente se ejecuta como fase
    if tramos[0] == "plantillas":
        return "13"                     # los modelos de documento
    return None


def _reglas_del_archivo(ruta, catalogo):
    """Las reglas que **viven** en el archivo que se está escribiendo."""
    ruta = os.path.abspath(ruta)
    return [r for r in catalogo if os.path.abspath(r.archivo) == ruta]


def _citadas(regla, indice):
    """Los IDs que la regla nombra en su cuerpo y que existen."""
    cuerpo = " ".join(t for _, t in regla.cuerpo)
    salida = []
    for m in _CITA.finditer(cuerpo):
        id = m.group(2)
        if id != regla.id and id in indice and id not in salida:
            salida.append(id)
    return salida


def _citan_a(ids, catalogo):
    """Qué reglas citan a alguna de `ids`. `{id_citado: [ids que la citan]}`.

    **Es el lado que no se mira.** Cambiar una regla rompe a quien dependía de
    ella, y eso no se ve leyendo la regla que se cambia.
    """
    salida = {}
    for r in catalogo:
        cuerpo = " ".join(t for _, t in r.cuerpo)
        for m in _CITA.finditer(cuerpo):
            id = m.group(2)
            if id in ids and id != r.id:
                salida.setdefault(id, [])
                if r.id not in salida[id]:
                    salida[id].append(r.id)
    return salida


def relacionadas(ruta, raiz=None):
    """Lo que hay que mirar antes de tocar `ruta`.

    Devuelve `{"capitulo", "propias", "citadas", "citan"}`, o `{}` si el
    archivo no lo gobierna ningún capítulo — el que trabaja en otra cosa no
    recibe reglas que no le tocan.
    """
    raiz = os.path.abspath(raiz or RAIZ)
    capitulo = _capitulo_de(ruta, raiz)
    if not capitulo:
        return {}

    catalogo = metareglas.reglas(raiz)
    indice = {r.id: r for r in catalogo}
    propias = _reglas_del_archivo(ruta, catalogo)

    citadas, dependencias = [], []
    for r in propias:
        for forma, id in metareglas._dependencias(r):
            if id in indice and (forma, id) not in dependencias:
                dependencias.append((forma, id))
        for id in _citadas(r, indice):
            if id not in citadas:
                citadas.append(id)

    return {
        "capitulo": capitulo,
        "propias": [r.id for r in propias],
        "dependencias": dependencias,
        "citadas": citadas,
        "citan": _citan_a([r.id for r in propias], catalogo),
        "indice": indice,
    }


def como_texto(rel, raiz=None):
    """El aviso que se le entrega al agente. `""` si no hay nada que decir."""
    if not rel or not rel.get("propias"):
        return ""
    raiz = os.path.abspath(raiz or RAIZ)
    indice = rel["indice"]

    def linea(id):
        r = indice[id]
        cuerpo = " ".join(t for _, t in r.cuerpo)
        return "  `%s·%s` — %s" % (r.capitulo, id, cuerpo[:110].strip())

    partes = ["[LO QUE SE RELACIONA CON LO QUE ESTÁ ESCRIBIENDO]",
              "Antes de sellar la fila 17 del checklist —«no choca con ninguna "
              "regla vigente»— hay que haber mirado esto.", ""]

    if rel["citan"]:
        partes.append("**Las que dependen de lo que está tocando.** Si cambia lo "
                      "que dicen, estas se rompen sin avisar:")
        for id, quienes in sorted(rel["citan"].items()):
            for q in quienes:
                partes.append(linea(q))
        partes.append("")

    if rel["dependencias"]:
        partes.append("**Dependencias declaradas:**")
        for forma, id in rel["dependencias"]:
            partes.append("  %s `%s`" % (forma, id))
        partes.append("")

    otras = [i for i in rel["citadas"]
             if i not in [d for _, d in rel["dependencias"]]]
    if otras:
        partes.append("**Citadas en el texto:**")
        partes.extend(linea(i) for i in otras)
        partes.append("")

    partes.append("El capítulo dueño de lo que se escribe acá es el `%s`."
                  % rel["capitulo"])
    return "\n".join(partes)


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("estandar")
