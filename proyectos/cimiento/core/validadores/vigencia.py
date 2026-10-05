"""`EP-001·HU-007·CA-04` · Qué reglas llevan más tiempo sin que nadie las mire.

**Una regla equivocada se comporta igual que una correcta.** Sigue pasando su
checklist de forma mientras cambia la herramienta que nombraba o deja de
ocurrir el problema que venía a evitar.

**Dos fechas distintas.** La del sello dice que se le aplicó el molde; la de
vigencia, que alguien volvió a preguntarse si la regla sigue sirviendo. Sin
fecha de vigencia se ordena por la del sello y no por la de `git`: la limpieza
tipográfica de un día tocó las 245 reglas y todas parecían recién escritas.

**No hay umbral.** Uno inventado produce una alarma que se aprende a ignorar:
se ordena y se muestra, y cada cuánto revisar se decide después de mirar la
lista. Por eso `validar()` nunca falla.
"""
import argparse
import os
import re

from ..comun import AVISO, Hallazgo, Proyecto
from ..comun.consola import preparar_salida
from .base import Validador
from .metareglas import CuerpoDeReglas, Metareglas

# La línea que se agrega al sello cuando alguien revisa la regla de fondo. Es
# opcional y arranca ausente: lo que la lista muestra es cuáles no la tienen.
_VIGENCIA = re.compile(r"(?m)^>?\s*Revisada contra la realidad el (\d{4}-\d{2}-\d{2})")
_SELLO_FECHA = re.compile(r"Aplicado el \[checklist.*?el \*\*(\d{4}-\d{2}-\d{2})\*\*")

MOLDE = "> Revisada contra la realidad el AAAA-MM-DD."


class Vigencia(Validador):
    """Un aviso, uno solo, por las reglas que nadie ha revisado de fondo."""

    nombre = "vigencia"
    regla = ""          # no comprueba una regla: ordena las que hay por antigüedad
    descripcion = "reglas que nadie ha revisado de fondo"

    @staticmethod
    def revisada(regla):
        """`AAAA-MM-DD` de la última revisión de fondo, o `""` si nunca."""
        m = _VIGENCIA.search(regla.texto or "")
        return m.group(1) if m else ""

    @staticmethod
    def fecha_del_sello(regla):
        """`AAAA-MM-DD` del día que se le aplicó el checklist, o `""`."""
        m = _SELLO_FECHA.search(regla.texto or "")
        return m.group(1) if m else ""

    def hallazgos_por_regla(self):
        """`{id: cuántos}` incumplimientos que hoy produce cada regla. Una vieja que
        falla todo el tiempo se revisa primero; una que no falla nunca, también:
        puede que ya nadie la aplique."""
        cuenta = {}
        for h in Metareglas(self.proyecto, self.archivos).validar():
            for m in re.finditer(r"`([A-Z]{1,3}\d+(?:\.\d+)?)`", h.mensaje):
                cuenta[m.group(1)] = cuenta.get(m.group(1), 0) + 1
        return cuenta

    def listado(self):
        """`[(regla, revisada, fecha del sello, hallazgos)]`, de la más vieja a la más nueva.

        Sin fecha de vigencia va primero (un `""` ordena antes que cualquier
        fecha) y, entre esas, la del sello más viejo.
        """
        fallas = self.hallazgos_por_regla()
        salida = [(r, self.revisada(r), self.fecha_del_sello(r), fallas.get(r.id, 0))
                  for r in CuerpoDeReglas.leer(self.proyecto.raiz, self.archivos)]
        return sorted(salida, key=lambda x: (x[1] or "", x[2] or ""))

    def validar(self):
        """Uno solo y no uno por regla: doscientos avisos idénticos entierran
        los hallazgos que sí piden acción."""
        datos = self.listado()
        sin_revisar = [d for d in datos if not d[1]]
        if not sin_revisar:
            return []
        viejas = ", ".join("`%s`" % d[0].id for d in sin_revisar[:5])
        return [Hallazgo(
            AVISO, os.path.join(self.proyecto.raiz, "base"), 0,
            "%d de %d reglas no dicen cuándo se revisó **si siguen sirviendo** — el sello responde "
            "por la forma, no por si el problema que evitan todavía existe. Las del sello más "
            "antiguo: %s. La lista completa: `python validadores/vigencia.py`"
            % (len(sin_revisar), len(datos), viejas))]

    def linea_resumen(self):
        """Cuántas tienen fecha de vigencia y cuántas no."""
        datos = self.listado()
        return "Reglas revisadas contra la realidad: %d de %d" % (len([d for d in datos if d[1]]), len(datos))


def main(argv=None):
    """La lista completa, de la más vieja a la más nueva."""
    preparar_salida()
    p = argparse.ArgumentParser(
        description="Lista las reglas por cuánto llevan sin que nadie se pregunte si siguen "
                    "sirviendo. No hay umbral: se mira la lista y después se decide cada cuánto revisar.")
    p.add_argument("--raiz", default=Proyecto.estandar())
    p.add_argument("--cuantas", type=int, default=25,
                   help="cuántas reglas listar, de la más vieja a la más nueva")
    a = p.parse_args(argv)

    datos = Vigencia(a.raiz).listado()
    sin = len([d for d in datos if not d[1]])
    print("== Vigencia de las reglas ==\n")
    print("%d reglas · %d sin revisar de fondo · %d con fecha\n" % (len(datos), sin, len(datos) - sin))
    print("Las tres preguntas de la revisión están en `base/20-meta-reglas/revision-de-vigencia.md`.\n")
    print("%-8s %-12s %-12s %s" % ("REGLA", "REVISADA", "SELLO DE", "FALLA HOY"))
    for regla, rev, sello, fallas in datos[:a.cuantas]:
        print("%-8s %-12s %-12s %s" % (regla.id, rev or "nunca", sello or "sin sello", fallas if fallas else ""))
    if len(datos) > a.cuantas:
        print("\n... y %d más. Se listan con --cuantas." % (len(datos) - a.cuantas))
    print("\nQuien revise una regla le agrega esta línea a su sello:")
    print("  %s" % MOLDE)
    return 0
