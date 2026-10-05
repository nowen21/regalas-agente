"""Qué fases se reabrieron, y cuántas veces. **Mide retrabajo, no culpa.**

Una fase reabierta y una fase nueva no se distinguían, así que la medida de
retrabajo no existía; y el retrabajo es la señal más directa de que una
especificación salió incompleta.

**Se deriva de la historia del archivo, no de sus palabras.** Las reaperturas
se escriben en prosa y cada una con las suyas; buscar la palabra se pierde unas
y cuenta las que solo *hablan* de reabrir. Lo que no se escribe de dos formas es
**una casilla que estaba marcada y dejó de estarlo**: que una estación de cierre
(7 pruebas, 8 cierre documental, 9 commit) pase de marcada a sin marcar.
"""
import os
import re

from ..comun import AVISO, Git, Hallazgo
from .base import Validador

CIERRE = (7, 8, 9)

_FILA = re.compile(r"(?m)^\|\s*(\d+)\s*\|[^|]*\|[^|]*\|\s*(.*?)\s*\|")


class Reaperturas(Validador):
    """Un aviso por fase reabierta. **Nunca una falla**: reabrir es lo correcto
    cuando lo que falla es ese trabajo y su documentación decía que estaba hecho."""

    nombre = "reaperturas"
    regla = ""
    descripcion = "qué fases volvieron atrás desde su cierre: retrabajo"

    @staticmethod
    def marcadas(texto):
        """`{número de estación: si está marcada}` de la tabla de estaciones."""
        return {int(m.group(1)): "☑" in m.group(2) for m in _FILA.finditer(texto)}

    def versiones(self, rel):
        """`[(commit, texto)]` del archivo en cada commit que lo tocó, del más viejo al más nuevo."""
        git = Git(self.proyecto.raiz)
        return [(commit, git.correr("show", "%s:%s" % (commit, rel)))
                for commit in git.lineas("log", "--reverse", "--format=%h", "--", rel)]

    def reaperturas(self):
        """`[(ruta, [commits donde se reabrió])]` de cada fase que volvió atrás."""
        raiz = self.proyecto.raiz
        base = os.path.join(raiz, "documentacion", "epicas")
        salida = []
        if not os.path.isdir(base):
            return salida
        for carpeta, _sub, archivos in os.walk(base):
            if "estado-fase.md" not in archivos:
                continue
            ruta = os.path.join(carpeta, "estado-fase.md")
            vueltas, antes = [], {}
            for commit, texto in self.versiones(os.path.relpath(ruta, raiz).replace("\\", "/")):
                ahora = self.marcadas(texto)
                if any(antes.get(n) and ahora.get(n) is False for n in CIERRE):
                    vueltas.append(commit)
                antes = ahora or antes
            if vueltas:
                salida.append((ruta, vueltas))
        return salida

    def validar(self):
        return [Hallazgo(AVISO, ruta, 0, "esta fase volvió atrás desde una estación de cierre %d vez(ces) — es "
                                         "retrabajo, y sirve para ver qué parte del flujo lo produce" % len(vueltas))
                for ruta, vueltas in self.reaperturas()]

    def linea_resumen(self):
        """Cuántas fases y cuántas vueltas. Va aunque no haya ninguna."""
        datos = self.reaperturas()
        return "Fases reabiertas: %d · vueltas atrás en total: %d" % (len(datos), sum(len(v) for _r, v in datos))
