"""`EP-023·HU-007` · Lo que una regla autoriza escribir sin que un plan lo nombre.

Hay archivos que se escriben siempre: la transcripción, el resumen, el análisis,
los guiones de apoyo. No los autoriza un plan, los autoriza **la regla que los
pide**, y lo dice en una línea que va después de `**Aplica a:**`:

    **Autoriza escribir:** `historico-chat/resumenes/**` · `historico-chat/*.md`

Se lee de las reglas de `base/` del estándar y de las del proyecto, en
`.agente/reglas-proyecto.md` (análisis 1 del pendiente 103, conclusión 46). En
las rutas, `*` vale por un tramo del nombre y `**` por cualquier cantidad de
carpetas. Lo usan el `pre-commit` (`validar.py plan --preparados`) y el freno.

**Solo autoriza la regla vigente** (análisis 11 del pendiente 103, acuerdos 2 y
3): la derogada lleva `[DEROGADA…]` en su título, y la *opt-in* de un capítulo
que el proyecto apagó no rige. Así una regla entra o sale sin tocar este programa.
"""
import os
import re

from ..comun import Archivos, Markdown, Proyecto
from ..herramientas.recuperar import RecuperadorDeReglas

_LINEA = re.compile(r"^(?:-\s*)?\*\*Autoriza escribir:\*\*(.*)$")
_RUTA = re.compile(r"`([^`]+)`")
_TITULO = re.compile(r"^##\s+([A-Z]{1,4}\d+(?:\.\d+)?)\s+·")
_ID_ARCHIVO = re.compile(r"^([A-Z]{1,4}\d+(?:\.\d+)?)-")
_CAPITULO = re.compile(r"^(\d{2})-")
_ID_PROYECTO = re.compile(r"^#{2,4}\s+(P\d+)\b")

REGLAS_PROYECTO = os.path.join(".agente", "reglas-proyecto.md")

# Lo que escriben las herramientas del estándar en todo proyecto, sin que un
# plan lo nombre: el instalador deja constancia de cada versión adoptada y el
# andamio crea el índice de cada carpeta (análisis 1 del pendiente 110, acuerdo 2).
HERRAMIENTAS = ("las herramientas del estándar (análisis 1 del pendiente 110)",
                ["documentacion/versiones/**", "documentacion/epicas/**/README.md"])


class Autorizaciones:
    """Las rutas que las reglas vigentes dejan escribir. Todo es de lectura."""

    def __init__(self, archivos=None, ajustes=None):
        self.archivos = archivos or Archivos()
        self.ajustes = ajustes      # de la base: las pruebas la cambian

    @staticmethod
    def patron(ruta):
        """La ruta con comodines, como expresión regular de la ruta entera."""
        salida, i = "", 0
        while i < len(ruta):
            if ruta.startswith("**/", i):
                salida += "(?:.*/)?"
                i += 3
            elif ruta.startswith("**", i):
                salida += ".*"
                i += 2
            elif ruta[i] == "*":
                salida += "[^/]*"
                i += 1
            else:
                salida += re.escape(ruta[i])
                i += 1
        return re.compile(salida + r"\Z")

    @staticmethod
    def id_de(titulo, archivo, base):
        """La regla dueña de la línea: el título `## ID ·` anterior, o el archivo.

        El capítulo se busca en la ruta **desde el estándar que se lee**: antes se
        medía desde el estándar instalado aunque se leyera otro.
        """
        if titulo:
            regla = titulo
        else:
            m = _ID_ARCHIVO.match(os.path.basename(archivo))
            regla = m.group(1) if m else os.path.basename(archivo)
        for parte in os.path.relpath(archivo, base).replace("\\", "/").split("/"):
            c = _CAPITULO.match(parte)
            if c:
                return "%s·%s" % (c.group(1), regla)
        return regla

    @staticmethod
    def lineas(texto, titulo=_TITULO):
        """`(id, encabezado, rutas)` de cada línea; la de un bloque de código es un ejemplo."""
        ultimo, encabezado = None, ""
        for _, linea in Markdown.lineas_utiles(texto):
            if linea.startswith("## "):
                encabezado = linea
            t = titulo.match(linea)
            if t:
                ultimo = t.group(1)
            m = _LINEA.match(linea)
            if m:
                rutas = [r.strip().lstrip("./") for r in _RUTA.findall(m.group(1))]
                yield ultimo, encabezado, [r for r in rutas if r]

    @staticmethod
    def vigente(encabezado, capitulo, apagados):
        """¿La regla rige? No si está derogada, ni si es *opt-in* de un capítulo apagado."""
        if "[DEROGADA" in encabezado.upper():
            return False
        return not ("opt-in" in encabezado.lower() and capitulo in apagados)

    def de_la_base(self, estandar=None, proyecto=None):
        """`[(regla, [rutas])]` de toda regla vigente de `base/` que autoriza escribir."""
        raiz = estandar or Proyecto.estandar()
        apagados = RecuperadorDeReglas.opt_in_apagados(proyecto, self.archivos) if proyecto else frozenset()
        # `EP-026·HU-004` · Del estándar en la base. Sin base no se autoriza nada,
        # y el freno ya no deja modificar (análisis 1 del pendiente 132, acuerdo 9).
        from ..estandar.en_base import fuente, recorrer
        from .niveles import BaseSinRespuesta
        try:
            lector = fuente(raiz, self.archivos)
        except BaseSinRespuesta:
            return []
        salida = []
        # Las reglas por tarea son copias de las del capítulo: se leen una vez.
        for archivo in recorrer(lector, raiz, "base", excluir={"reglas-por-tarea"}):
            for titulo, encabezado, rutas in self.lineas(lector.leer(archivo)):
                regla = self.id_de(titulo, archivo, raiz)
                if self.vigente(encabezado, regla.split("·")[0], apagados):
                    salida.append((regla, rutas))
        return salida

    def del_proyecto(self, proyecto):
        """`[(regla, [rutas])]` de las reglas propias del proyecto.

        `EP-027·HU-006` · Si el proyecto tiene sus reglas en la base de Cimiento,
        se leen de ahí; si no, de su archivo, como antes."""
        from .reglas_del_proyecto import ReglasDelProyecto

        en_base = ReglasDelProyecto(proyecto, ajustes=self.ajustes).autorizan()
        if en_base is not None:
            return [(codigo, rutas) for codigo, texto in en_base for _, _, rutas in self.lineas(texto)]
        archivo = os.path.join(proyecto, REGLAS_PROYECTO)
        if not os.path.isfile(archivo):
            return []
        return [(titulo or "reglas-proyecto", rutas)
                for titulo, _, rutas in self.lineas(self.archivos.leer(archivo), _ID_PROYECTO)]

    def reglas(self, proyecto, estandar=None):
        """Lo autorizado para ese proyecto: lo de `base/`, lo suyo y lo que escriben las herramientas."""
        return self.de_la_base(estandar, proyecto) + self.del_proyecto(proyecto) + [HERRAMIENTAS]

    @classmethod
    def quien_autoriza(cls, ruta, autorizadas):
        """La regla que autoriza escribir esa ruta, o `None`."""
        ruta = ruta.replace("\\", "/").lstrip("./")
        for regla, rutas in autorizadas:
            for r in rutas:
                if cls.patron(r).match(ruta):
                    return regla
        return None
