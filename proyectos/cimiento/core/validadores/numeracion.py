"""`EP-002·HU-006` · Una sola numeración, aunque haya dos sesiones.

El 2026-08-14 dos sesiones sobre el mismo repositorio dejaron dos numeraciones
vivas, y al final del día había entradas del registro escritas por las dos. La
decisión del pendiente 22: **el número lo pone quien guarda, no quien edita.**

Al guardar se comprueba que el número de `VERSION` **avanza** desde el guardado,
que **tiene su entrada** en el registro y que **no repite** uno ya usado. No se
mira el reloj ni quién escribió, porque no hay forma fiable de saberlo: se miran
los números, que es lo que se rompe.

Corre dentro del subcomando `versionado` de `validar.py`.
"""
import os
import re

from ..comun import AVISO, FALLA, Git, Hallazgo
from .base import Validador

_VERSION = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
_ENTRADA = re.compile(r"(?m)^## (\d+\.\d+\.\d+)\b(.*)$")
_RECONOCIDO = "número repetido"


class Numeracion(Validador):
    """Los hallazgos de la numeración de `VERSION` contra el registro de cambios."""

    nombre = "numeracion"
    regla = "20·M18, 20·M10"
    descripcion = "una sola numeración de versiones, aunque haya dos sesiones"

    @staticmethod
    def tupla(v):
        m = _VERSION.match((v or "").strip())
        return tuple(int(x) for x in m.groups()) if m else None

    @staticmethod
    def guardada(raiz, revision="HEAD"):
        """El número de `VERSION` **en lo ya guardado**, o `None`. Sin control de
        versiones no hay con qué comparar, y eso no es un fallo."""
        salida = Git(raiz, espera=30).correr("show", "%s:VERSION" % revision)
        return salida.strip() if salida else None

    def validar(self):
        raiz = self.proyecto.raiz
        archivo = os.path.join(raiz, "VERSION")
        registro = os.path.join(raiz, "CHANGELOG.md")
        # Sin los dos archivos no hay nada que decir: un proyecto que no lleva
        # numeración no puede quedar con una falla que le rechace los commits.
        if not (os.path.isfile(archivo) and os.path.isfile(registro)):
            return []

        ahora = self.archivos.leer(archivo).strip()
        t_ahora = self.tupla(ahora)
        if not t_ahora:
            return [Hallazgo(FALLA, archivo, 1, "`VERSION` no tiene la forma `MAYOR.MENOR.PARCHE`")]

        filas = _ENTRADA.findall(self.archivos.leer(registro))
        entradas = [v for v, _ in filas]
        # Un duplicado que el registro ya reconoce en su título no se renumera:
        # alguien pudo haber adoptado ese número. Sigue a la vista, como aviso.
        reconocidas = {v for v, resto in filas if _RECONOCIDO in resto}
        hallazgos = []

        # 1 · No se quedó atrás. Igual no es falla: recién guardado, coinciden.
        antes = self.guardada(raiz)
        t_antes = self.tupla(antes)
        if t_antes and t_ahora < t_antes:
            hallazgos.append(Hallazgo(
                FALLA, archivo, 1,
                "`VERSION` dice %s y lo guardado ya está en %s — otra sesión guardó primero y este "
                "número quedó viejo. El número lo pone quien guarda" % (ahora, antes)))

        # 2 · Tiene su entrada.
        if ahora not in entradas:
            hallazgos.append(Hallazgo(FALLA, registro, 0,
                                      "`VERSION` dice %s y el registro no tiene su entrada" % ahora))

        # 3 · No repite.
        for v in sorted({v for v in entradas if entradas.count(v) > 1}):
            conocida = v in reconocidas
            hallazgos.append(Hallazgo(
                AVISO if conocida else FALLA, registro, 0,
                "el registro tiene %d entradas para la %s — dos sesiones numeraron a la vez%s"
                % (entradas.count(v), v, " (ya reconocido en el registro; no se renumera)" if conocida else "")))

        # Y el hueco: una versión puede saltarse a propósito, pero casi siempre
        # es la marca de dos sesiones. Se avisa.
        numeros = sorted({self.tupla(v) for v in entradas if self.tupla(v)})
        for a, b in zip(numeros, numeros[1:]):
            if b[0] == a[0] and b[1] == a[1] and b[2] > a[2] + 1:
                hallazgos.append(Hallazgo(
                    AVISO, registro, 0,
                    "hueco entre la %s y la %s — puede ser a propósito, o dos sesiones numerando"
                    % (".".join(map(str, a)), ".".join(map(str, b)))))
        return hallazgos
