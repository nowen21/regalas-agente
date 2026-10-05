"""`13·DOC17` · La línea del índice que falta se escribe, en vez de solo reportarla.

Que falte la línea lo reporta `IndicesDeCarpetas` (en `enlaces.py`), a veces
varios commits después. Acá está lo otro: `CompletadorDeIndices` la escribe, y
`IndicesPorAfinar` avisa de la que escribió y nadie terminó de redactar.

**No se reescribe el índice entero**: las líneas que ya están llevan una
descripción escrita por alguien que el encabezado del archivo no tiene, y
regenerar el bloque la perdería. Se agrega lo que falta con el título como
descripción provisional, dicho que hay que afinarla. Lo que sobra se reporta y
no se borra: quitar una línea puede ser el error, no el archivo que ya no está.
"""
import os
import re

from ..comun import AVISO, Hallazgo, Proyecto
from ..comun.archivos import Archivos
from .base import Validador
from .enlaces import CON_INDICE

_TITULO = re.compile(r"(?m)^#\s+(.+?)\s*$")

# Va al final de la descripción provisional. Quien la afine, la borra. Es texto
# que ya está escrito en los índices: cambiarlo dejaría de reconocerlos.
POR_AFINAR = "— (por describir)"


class CompletadorDeIndices:
    """Agrega a cada índice la línea de los `.md` que no menciona."""

    def __init__(self, proyecto, archivos=None):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)
        self.archivos = archivos or Archivos()

    def titulo_de(self, ruta):
        """El primer encabezado `#` del archivo, o su nombre si no tiene."""
        m = _TITULO.search(self.archivos.leer(ruta))
        return m.group(1).strip() if m else os.path.basename(ruta)[:-3]

    def faltantes(self, carpeta):
        """Los `.md` de la carpeta que su `README.md` no menciona."""
        indice = os.path.join(carpeta, "README.md")
        if not os.path.isfile(indice):
            return []
        texto = self.archivos.leer(indice)
        return [n for n in sorted(os.listdir(carpeta))
                if n.lower().endswith(".md") and n != "README.md"
                and "(%s)" % n not in texto and "/%s)" % n not in texto]

    def _linea(self, carpeta_rel, nombre, ruta):
        """La línea del índice, con el texto que pide `13·DOC14`."""
        return "- [%s/%s](%s) %s %s\n" % (carpeta_rel, nombre, nombre, POR_AFINAR, self.titulo_de(ruta))

    def completar(self, carpetas=None, escribir=False):
        """`[(indice, cuántas)]`. Sin `escribir` solo simula, como el resto de los reparadores."""
        tocados = []
        for rel in (carpetas or CON_INDICE):
            carpeta = os.path.join(self.proyecto.raiz, rel)
            faltan = self.faltantes(carpeta)
            if not faltan:
                continue
            indice = os.path.join(carpeta, "README.md")
            texto = self.archivos.leer(indice)
            nuevas = "".join(self._linea(rel, n, os.path.join(carpeta, n)) for n in faltan)
            if escribir:
                with open(indice, "w", encoding="utf-8", newline="\n") as f:
                    f.write(texto.rstrip() + "\n" + nuevas)
            tocados.append((indice, len(faltan)))
        return tocados


class IndicesPorAfinar(Validador):
    """Avisa de las líneas que escribió el completador y nadie redactó. **No
    repite lo de `IndicesDeCarpetas`**, que ya falla por la línea que falta.

    El subcomando viejo era `indices`, pero ese nombre ya es de
    `IndicesDeCarpetas`: dos validadores no pueden llamarse igual.
    """

    nombre = "indices-por-afinar"
    regla = "13·DOC17"
    descripcion = "las líneas de índice con la descripción provisional"

    def __init__(self, proyecto, archivos=None, carpetas=None):
        super().__init__(proyecto, archivos)
        self.carpetas = carpetas or CON_INDICE

    def validar(self):
        hallazgos = []
        for rel in self.carpetas:
            indice = os.path.join(self.proyecto.raiz, rel, "README.md")
            if not os.path.isfile(indice):
                continue
            cuantas = self.archivos.leer(indice).count(POR_AFINAR)
            if cuantas:
                hallazgos.append(Hallazgo(AVISO, indice, 0, "%d línea(s) con la descripción provisional «%s» — "
                                                            "la puso el generador y hay que reemplazarla por qué "
                                                            "es y para qué sirve" % (cuantas, POR_AFINAR)))
        return hallazgos
