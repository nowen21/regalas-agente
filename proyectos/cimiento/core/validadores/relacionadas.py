"""`EP-005·HU-010` · Qué reglas se relacionan con lo que se está escribiendo.

Se escribió una frase en `02·F2` que chocaba con `02·F0`, la regla que `F2` cita
en su propio texto, y la fila 17 del checklist se selló en verde sin mirar. **No
es un problema de cargar contexto sino de buscar**: mandar el capítulo entero
obliga a encontrar la relación uno mismo, que es justo lo que falla.

La respuesta ya está escrita en el repositorio: el cuerpo de reglas sabe dónde
vive cada una y qué dependencias declara, y `20·M15` obliga a que toda cita
lleve su enlace. **Las que la citan van primero**: cambiar una regla rompe a
quien dependía de ella, y ese es el lado que no se mira.

No es una comprobación: lo usa el enganche que avisa al escribir.
"""
import re

from ..comun import Archivos, Proyecto
from .metareglas import CuerpoDeReglas

# `[`02·F0`](…)` o `02·F0` suelto: lo que `M15` pide y lo que se escribe igual.
_CITA = re.compile(r"(?:(\d{2})·)?\b([A-Z]{1,4}\d+(?:\.\d+)?)\b")


class ReglasRelacionadas:
    """Lo que hay que mirar antes de tocar un archivo del estándar."""

    def __init__(self, raiz=None, archivos=None):
        self.proyecto = Proyecto(raiz or Proyecto.estandar())
        self.archivos = archivos or Archivos()

    @staticmethod
    def capitulo_de(ruta, raiz):
        """El capítulo dueño de un archivo, por su carpeta; `None` si no lo
        gobierna ninguno. Por carpeta y no por tipo de documento (duda 41): el
        tipo hay que adivinarlo, la carpeta se lee de la ruta.

        Un archivo fuera de `raiz` (o en otra unidad, donde el viejo reventaba
        con `ValueError`) no lo gobierna ninguno.
        """
        rel = Proyecto(raiz).relativa(ruta)
        if rel is None:
            return None
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

    @staticmethod
    def citadas(regla, indice):
        """Los IDs que la regla nombra en su cuerpo y que existen."""
        salida = []
        for m in _CITA.finditer(" ".join(t for _, t in regla.cuerpo)):
            id_ = m.group(2)
            if id_ != regla.id and id_ in indice and id_ not in salida:
                salida.append(id_)
        return salida

    @staticmethod
    def citan_a(ids, catalogo):
        """`{id citado: [ids que la citan]}`: el lado que no se mira."""
        salida = {}
        for r in catalogo:
            for m in _CITA.finditer(" ".join(t for _, t in r.cuerpo)):
                id_ = m.group(2)
                if id_ in ids and id_ != r.id:
                    salida.setdefault(id_, [])
                    if r.id not in salida[id_]:
                        salida[id_].append(r.id)
        return salida

    def de(self, ruta):
        """`{"capitulo", "propias", "dependencias", "citadas", "citan", "indice"}`,
        o `{}` si el archivo no lo gobierna ningún capítulo: quien trabaja en otra
        cosa no recibe reglas que no le tocan."""
        capitulo = self.capitulo_de(ruta, self.proyecto.raiz)
        if not capitulo:
            return {}
        catalogo = CuerpoDeReglas.leer(self.proyecto.raiz, self.archivos)
        indice = {r.id: r for r in catalogo}
        destino = Proyecto.ruta_real(ruta, self.proyecto.raiz)
        propias = [r for r in catalogo if Proyecto.ruta_real(r.archivo, self.proyecto.raiz) == destino]

        citadas, dependencias = [], []
        for r in propias:
            for forma, id_ in CuerpoDeReglas.dependencias(r):
                if id_ in indice and (forma, id_) not in dependencias:
                    dependencias.append((forma, id_))
            for id_ in self.citadas(r, indice):
                if id_ not in citadas:
                    citadas.append(id_)
        return {"capitulo": capitulo, "propias": [r.id for r in propias], "dependencias": dependencias,
                "citadas": citadas, "citan": self.citan_a([r.id for r in propias], catalogo),
                "indice": indice}

    @staticmethod
    def como_texto(rel):
        """El aviso que se le entrega al agente. `""` si no hay nada que decir."""
        if not rel or not rel.get("propias"):
            return ""
        indice = rel["indice"]

        def linea(id_):
            r = indice[id_]
            cuerpo = " ".join(t for _, t in r.cuerpo)
            return "  `%s·%s` — %s" % (r.capitulo, id_, cuerpo[:110].strip())

        partes = ["[LO QUE SE RELACIONA CON LO QUE ESTÁ ESCRIBIENDO]",
                  "Antes de sellar la fila 17 del checklist —«no choca con ninguna "
                  "regla vigente»— hay que haber mirado esto.", ""]
        if rel["citan"]:
            partes.append("**Las que dependen de lo que está tocando.** Si cambia lo "
                          "que dicen, estas se rompen sin avisar:")
            for _, quienes in sorted(rel["citan"].items()):
                partes.extend(linea(q) for q in quienes)
            partes.append("")
        if rel["dependencias"]:
            partes.append("**Dependencias declaradas:**")
            partes.extend("  %s `%s`" % (forma, id_) for forma, id_ in rel["dependencias"])
            partes.append("")
        declaradas = [d for _, d in rel["dependencias"]]
        otras = [i for i in rel["citadas"] if i not in declaradas]
        if otras:
            partes.append("**Citadas en el texto:**")
            partes.extend(linea(i) for i in otras)
            partes.append("")
        if "parecidas" in rel:
            partes.extend(ReglasRelacionadas._parecidas(rel["parecidas"], linea))
        partes.append("El capítulo dueño de lo que se escribe acá es el `%s`." % rel["capitulo"])
        return "\n".join(partes)

    @staticmethod
    def _parecidas(parecidas, linea):
        """`20·M12` · `EP-004·HU-027`: las que dicen algo parecido aunque no se
        citen. `None` es que no se pudo buscar, y se dice."""
        if parecidas is None:
            return ["**Las parecidas por significado no se pudieron buscar**: falta la búsqueda "
                    "de `memoria/` (numpy y model2vec).", ""]
        ids = []
        for lista in parecidas.values():
            for i, _ in lista:
                if i not in ids:
                    ids.append(i)
        if not ids:
            return []
        return (["**Las que se le parecen por significado** (`20·M12`). Antes de crear o cambiar "
                 "una regla, ver si una de estas ya lo dice:"] + [linea(i) for i in ids] + [""])
