"""Trazabilidad de la documentación de fases: `02·F4` y `13·DOC`.

Comprueba lo que se puede sin criterio:

  DOC16 — enlace en los dos sentidos: cada HU declara su épica y la épica lista sus HU.
  DOC12 — el `plan_trabajo` de cada fase declara ORIGEN.
  DOC3/DOC11 — la `funcionalidad_implementada` trae la tabla de trazabilidad, y
               los ítems ❌ se marcan para que una persona confirme su justificación.

Casi todo es **AVISO**: un documento recién abierto todavía no tiene todo, y un
validador que grita por cada archivo en curso se termina ignorando.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Markdown
from .base import Validador
from .epicas import CARPETA, Epicas

# Mayúscula a propósito: es el nombre del campo; en minúscula encontraría prosa.
_ORIGEN = re.compile(r"\bORIGEN\b")


class TrazabilidadDeFases(Validador):

    nombre = "trazabilidad"
    regla = "13·DOC16"
    descripcion = "enlaces épica–HU, ORIGEN del plan y tabla de trazabilidad"

    @staticmethod
    def menciona(texto, prefijo, numero):
        """¿El texto nombra `EP-2`, `EP-002` o `EP2` (o `HU-…`)? El ancho no importa."""
        return re.search(r"%s-?0*%d\b" % (prefijo, numero), texto) is not None

    def _leer(self, ruta):
        return self.archivos.leer(ruta) if ruta and os.path.isfile(ruta) else ""

    def _sin_codigo(self, ruta):
        """El cuerpo sin los bloques ```: un ejemplo no cuenta como contenido."""
        return "\n".join(l for _, l in Markdown.lineas_utiles(self._leer(ruta)))

    def validar(self):
        arbol = Epicas(self.proyecto)
        if not arbol.existe():
            return [Hallazgo(FALLA, self.proyecto.raiz, 0, "no existe `%s` (F12.13)" % CARPETA)]
        hallazgos = []
        for epica in arbol.epicas():
            doc_epica = self._sin_codigo(arbol.documento_de_la_epica(epica))
            for hu in arbol.historias(epica):
                hallazgos += self._revisar_historia(arbol, epica, hu, doc_epica)
        return hallazgos

    def _revisar_historia(self, arbol, epica, hu, doc_epica):
        hallazgos = []
        doc_hu = self._sin_codigo(hu.documento(hu.nombre + ".md"))
        if doc_hu and not self.menciona(doc_hu, "EP", epica.numero):
            hallazgos.append(Hallazgo(AVISO, hu.donde, 0, "la HU no declara su épica EP-%d "
                                                          "(DOC16 · enlace bidireccional)" % epica.numero))
        if doc_epica and not self.menciona(doc_epica, "HU", hu.numero):
            hallazgos.append(Hallazgo(AVISO, epica.donde, 0,
                                      "la épica no lista la HU-%d que cuelga de ella (DOC16)" % hu.numero))
        for fase in arbol.fases(hu):
            plan = self._leer(fase.documento("plan_trabajo.md"))
            if plan and not _ORIGEN.search(plan):
                hallazgos.append(Hallazgo(AVISO, fase.donde, 0, "el plan_trabajo no declara ORIGEN (DOC12)"))
            fi = self._leer(fase.documento("funcionalidad_implementada.md"))
            if fi and "|" not in fi:
                hallazgos.append(Hallazgo(AVISO, fase.donde, 0, "la funcionalidad_implementada no trae "
                                                                "tabla de trazabilidad (DOC11)"))
            elif "❌" in fi:
                hallazgos.append(Hallazgo(AVISO, fase.donde, 0, "hay ítems ❌ en la trazabilidad — confirmar "
                                                                "que estén justificados (DOC11)"))
        return hallazgos
