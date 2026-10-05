"""`EP-005·HU-012` · Toda regla del núcleo dice quién la hace cumplir.

Una regla escrita **informa**; un programa o un enganche **ejecuta**. Sin la
declaración, una regla del núcleo podía existir sin que nada la hiciera cumplir
y leerse igual que una que sí (el 2026-08-31 eran 14 de 18).

**Qué se comprueba y qué no.** Que la declaración esté, que traiga su motivo
cuando dice que nadie la hace cumplir, y que la pieza nombrada exista. **No que
la pieza de verdad la haga cumplir**: eso se lee, y prometerlo sería un número
que el lector completa con lo que quiere creer.

Solo el capítulo `00`, que es lo que no se relaja.
"""
import os
import re

from ..comun import FALLA, Hallazgo, Proyecto
from .base import Validador
from .metareglas import CuerpoDeReglas

CAPITULO = "00"

# Las dos aperturas, y ninguna más: un campo libre dejaría pasar «pendiente».
_QUIEN = re.compile(r"(?m)^>?\s*\*\*Quién la hace cumplir:\*\*\s*(.+?)\s*$")
_NADIE = re.compile(r"(?m)^>?\s*\*\*Nadie la hace cumplir:\*\*\s*(.+?)\s*$")

# Un motivo más corto que esto es una casilla marcada: «no se puede», «es
# criterio» y «lo lee una persona» caben por debajo, y ninguna dice nada.
MOTIVO_MINIMO = 40

# La pieza se nombra por su ruta desde la raíz, entre comillas invertidas, para
# poder resolverla contra el disco: `marcas.py` aparece en tres carpetas.
_PIEZA = re.compile(r"`([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)`")

# Dónde se escribe, para que el mensaje diga qué hacer y no solo qué falta.
DONDE = ("después del ejemplo y antes del checklist, con una de las dos "
         "aperturas: `**Quién la hace cumplir:**` o `**Nadie la hace "
         "cumplir:**`")


class QuienLaHaceCumplir(Validador):
    """Un hallazgo por regla vigente del núcleo que no dice quién la hace cumplir."""

    nombre = "ejecutable"
    regla = "20·M5"
    descripcion = "qué regla del núcleo declara quien la hace cumplir"

    @staticmethod
    def declaracion(regla):
        """`(clase, texto)` de la regla: `"quien"`, `"nadie"` o `(None, "")`."""
        m = _QUIEN.search(regla.texto)
        if m:
            return "quien", m.group(1).strip()
        m = _NADIE.search(regla.texto)
        if m:
            return "nadie", m.group(1).strip()
        return None, ""

    @staticmethod
    def piezas(texto):
        """Las rutas que la declaración nombra, en el orden en que aparecen."""
        salida = []
        for ruta in _PIEZA.findall(texto):
            if ruta not in salida:
                salida.append(ruta)
        return salida

    def del_nucleo(self):
        """Las reglas vigentes del capítulo `00`. La derogada queda fuera: dejó de regir."""
        return [r for r in CuerpoDeReglas.leer(self.proyecto.raiz, self.archivos)
                if r.capitulo == CAPITULO and not r.derogada]

    def validar(self):
        hallazgos = []
        for regla in self.del_nucleo():
            clase, texto = self.declaracion(regla)
            if clase is None:
                hallazgos.append(Hallazgo(FALLA, regla.archivo, regla.linea,
                                          "`%s` no dice quién la hace cumplir. Se escribe %s"
                                          % (regla.id, DONDE)))
            elif clase == "nadie":
                if len(texto) < MOTIVO_MINIMO:
                    hallazgos.append(Hallazgo(
                        FALLA, regla.archivo, regla.linea,
                        "`%s` declara que nadie la hace cumplir y no dice por qué. Una casilla "
                        "marcada sin motivo no es una decisión" % regla.id))
            elif not self.piezas(texto):
                hallazgos.append(Hallazgo(
                    FALLA, regla.archivo, regla.linea,
                    "`%s` dice que alguien la hace cumplir y no nombra la pieza. Va su ruta desde la "
                    "raíz, entre comillas invertidas — por ejemplo `validadores/marcas.py`" % regla.id))
            else:
                for ruta in self.piezas(texto):
                    if not os.path.exists(self.proyecto.ruta(ruta)):
                        hallazgos.append(Hallazgo(
                            FALLA, regla.archivo, regla.linea,
                            "`%s` declara como pieza `%s`, que no existe en el repositorio"
                            % (regla.id, ruta)))
        return hallazgos

    def cuenta(self):
        """`{"reglas", "con_pieza", "sin_nadie"}`: la foto que abre y cierra la fase."""
        reglas = self.del_nucleo()
        clases = [self.declaracion(r)[0] for r in reglas]
        return {"reglas": len(reglas), "con_pieza": clases.count("quien"),
                "sin_nadie": clases.count("nadie")}

    def como_texto(self):
        """La línea que se lee al cerrar: cuántas manda un programa y cuántas no."""
        c = self.cuenta()
        if not c["reglas"]:
            return ""
        estandar = Proyecto.estandar()
        base = os.path.join(self.proyecto.raiz, "base")
        donde = Proyecto(estandar).mostrar(base) if estandar else base.replace("\\", "/")
        return ("Quién hace cumplir el núcleo (`%s`): %d reglas · %d con pieza que "
                "las ejecuta · %d declaradas sin quien las ejecute\n"
                "  Declararlo no es hacerlas cumplir: que la pieza de verdad las "
                "ejecute lo lee una persona." % (donde, c["reglas"], c["con_pieza"], c["sin_nadie"]))
