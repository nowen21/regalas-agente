"""`EP-005·HU-011` · El mapa del amarre a la herramienta no envejece en silencio.

**Qué contesta el mapa**: si mañana el usuario trabaja con otro agente, qué se
queda y qué hay que rehacer. Vive en `anatomia/que-esta-amarrado-a-la-herramienta.md`
y se escribe a mano, así que envejece: un programa nuevo no aparece ahí hasta
que alguien se acuerde.

**Se mira por los dos lados**: la pieza que existe y el mapa no clasifica, y la
que el mapa nombra y ya no existe. **Lo que no se comprueba** es si la
clasificación es la correcta: eso se lee.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo
from .base import Validador

MAPA = os.path.join("anatomia", "que-esta-amarrado-a-la-herramienta.md")

# La **misma** lista con que se escribió el mapa: si dijera otra cosa, el
# programa y el mapa medirían distinto y nadie lo notaría (riesgo `R-01`).
MARCA = re.compile(
    r"\.claude\b|CLAUDE\.md|settings\.json|hook[s]?_|PostToolUse|UserPromptSubmit|"
    r"SessionStart|\bStop\b|claude_code|CLAUDE_", re.I)

# El medidor nombra la herramienta porque **la mide**: lo que existe para
# hablar de algo no es una instancia de ese algo.
EXENTOS = ("amarre.py",)

# Las dos carpetas donde hay código. Mirar solo `validadores/` dejaría fuera los
# enganches que se mudaron al adaptador, y el mapa sonaría a mejora cuando lo
# que hubo fue una mudanza.
CARPETAS = (os.path.join("validadores"),
            os.path.join("adaptadores", "claude-code"))

# `EP-005·HU-023` · Una línea que no dice nada más que nombres: la lista de libres.
_SOLO_NOMBRES = re.compile(r"^(`[\w.]+`[\s·,.]*)+$")


class MapaDelAmarre(Validador):
    """Las dos formas de envejecer del mapa del amarre."""

    nombre = "amarre"
    regla = "EP-005·HU-011"
    descripcion = "qué piezas están atadas a la herramienta: el mapa no envejece"

    @property
    def mapa(self):
        return os.path.join(self.proyecto.raiz, *MAPA.split(os.sep))

    def piezas(self):
        """`{nombre: cuántas marcas}` de cada programa, en las dos carpetas."""
        salida = {}
        for rel in CARPETAS:
            carpeta = os.path.join(self.proyecto.raiz, rel)
            if not os.path.isdir(carpeta):
                continue
            for nombre in sorted(os.listdir(carpeta)):
                if nombre.endswith(".py") and nombre not in EXENTOS:
                    salida[nombre] = len(MARCA.findall(self.archivos.leer(os.path.join(carpeta, nombre))))
        return salida

    @staticmethod
    def clasificacion(texto):
        """Solo las líneas que clasifican: filas de tabla y listas de nombres.

        Nombrar una pieza en una frase no dice en qué columna va: una frase que
        decía «estas dos siguen sin clasificar», nombrándolas, las daba por
        clasificadas (`EP-005·HU-023`, CA-06).
        """
        return "\n".join(l.strip() for l in texto.splitlines()
                         if l.strip().startswith("|") or _SOLO_NOMBRES.match(l.strip()))

    @staticmethod
    def clasificada(nombre, clasificacion):
        """Si la pieza aparece entre comillas invertidas en una línea que
        clasifica, con `.py` o sin él: los enganches van a veces sin la extensión."""
        return re.search(r"`%s(\.py)?`" % re.escape(nombre[:-3]), clasificacion) is not None

    def validar(self):
        archivo = self.mapa
        texto = self.archivos.leer(archivo) if os.path.isfile(archivo) else ""
        if not texto:
            return [Hallazgo(FALLA, archivo, 0, "falta el mapa del amarre — sin él nadie sabe qué se cae si "
                                                "mañana el agente es otro")]
        encontradas = self.piezas()
        clasificacion = self.clasificacion(texto)
        hallazgos = [Hallazgo(FALLA, archivo, 0, "`%s` no está en el mapa — nadie sabe si se queda o hay que "
                                                 "rehacerla el día que cambie el agente" % nombre)
                     for nombre in sorted(encontradas) if not self.clasificada(nombre, clasificacion)]
        # El otro lado: el mapa que promete clasificar algo que no está.
        return hallazgos + [Hallazgo(AVISO, archivo, 0, "el mapa nombra `%s`, que ya no existe — se movió o se "
                                                        "borró, y el mapa promete clasificar algo que no está"
                                     % citada)
                            for citada in sorted(set(re.findall(r"`([a-z_]+\.py)`", texto)))
                            if citada not in encontradas and citada not in EXENTOS]

    def linea_resumen(self):
        """El recuento, para poder compararlo con lo que el mapa dice."""
        encontradas = self.piezas()
        if not encontradas:
            return ""
        amarradas = sum(1 for n in encontradas.values() if n > 0)
        return ("Piezas de `validadores/`: %d · amarradas a la herramienta: %d · libres: %d"
                % (len(encontradas), amarradas, len(encontradas) - amarradas))
