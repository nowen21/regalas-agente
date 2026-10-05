"""El árbol de `documentacion/epicas/`: épicas, historias y fases por su nombre.

Lo leían `fases.py` y `trazabilidad.py` cada uno a su modo, con las mismas
expresiones copiadas. Acá están una vez: quien recorre el árbol lo pide a
`Epicas` y no vuelve a escribir cómo se llama una carpeta de fase.
"""
import os
import re

CARPETA = "documentacion/epicas"

# F12.13 · los cinco documentos de una fase.
DOCUMENTOS = ["plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
              "funcionalidad_implementada.md", "estado-fase.md"]

# `EP-023·HU-003·CA-08` · La carpeta de los pendientes de una épica o de una HU:
# no es una HU ni una fase, y la revisa `validar.py pendientes`.
PENDIENTES = "pendientes"

_EPICA = re.compile(r"^EP-(\d+)-(.+)$")
_HU = re.compile(r"^HU-(\d+)-(.+)$")

# F12.6  ·  [consecutivo]-EP-[nnn]-HU-[nnn]-[descripción]
# F12.12 ·  [consecutivo]-[consecutivo-que-complementa]-EP-[nnn]-HU-[nnn]-[desc]
_FASE = re.compile(
    r"^(?P<consecutivo>[A-Z]{1,3})"
    r"(?:-(?P<complementa>[A-Z]{1,3}))?"
    r"-EP-(?P<epica>\d+)"
    r"-HU-(?P<hu>\d+)"
    r"-(?P<descripcion>.+)$")


class Nodo:
    """Una carpeta del árbol: épica, historia o fase."""

    def __init__(self, nombre, ruta, numero=None, donde=""):
        self.nombre = nombre
        self.ruta = ruta
        self.numero = numero    # `002` y `2` son el mismo: se guarda el entero
        self.donde = donde      # cómo se nombra en un hallazgo, desde la raíz

    def documento(self, nombre):
        return os.path.join(self.ruta, nombre)


class Epicas:
    """Recorre las épicas de un proyecto. Las carpetas con nombre inválido se
    saltan: reportarlas es trabajo de `fases`, y acá se contarían dos veces."""

    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.raiz = proyecto.ruta(CARPETA)

    def existe(self):
        return os.path.isdir(self.raiz)

    @staticmethod
    def epica(nombre):
        """El número de la épica si el nombre es `EP-<n>-<slug>`, o `None`."""
        m = _EPICA.match(nombre)
        return int(m.group(1)) if m else None

    @staticmethod
    def historia(nombre):
        """El número de la HU si el nombre es `HU-<n>-<slug>`, o `None`."""
        m = _HU.match(nombre)
        return int(m.group(1)) if m else None

    @staticmethod
    def fase(nombre):
        """Las partes del nombre de una fase (`consecutivo`, `epica`, `hu`…), o `None`."""
        m = _FASE.match(nombre)
        return m.groupdict() if m else None

    @staticmethod
    def orden_letras(letras):
        """A=1, B=2, …, Z=26, AA=27 (base 26 biyectiva): ordena el consecutivo."""
        n = 0
        for c in letras.upper():
            n = n * 26 + (ord(c) - ord("A") + 1)
        return n

    @staticmethod
    def subcarpetas(ruta):
        if not os.path.isdir(ruta):
            return []
        return sorted(n for n in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, n)))

    def epicas(self):
        for nombre in self.subcarpetas(self.raiz):
            m = _EPICA.match(nombre)
            if m:
                yield Nodo(nombre, os.path.join(self.raiz, nombre), int(m.group(1)),
                           "%s/%s" % (CARPETA, nombre))

    def historias(self, epica):
        for nombre in self.subcarpetas(epica.ruta):
            m = _HU.match(nombre)
            if m:
                yield Nodo(nombre, os.path.join(epica.ruta, nombre), int(m.group(1)),
                           "%s/%s" % (epica.donde, nombre))

    def fases(self, historia):
        for nombre in self.subcarpetas(historia.ruta):
            if _FASE.match(nombre):
                yield Nodo(nombre, os.path.join(historia.ruta, nombre), donde="%s/%s" % (historia.donde, nombre))

    @staticmethod
    def documento_de_la_epica(epica):
        """`epica.md`, o el que se llama como su carpeta; `None` si no tiene."""
        for nombre in ("epica.md", epica.nombre + ".md"):
            ruta = epica.documento(nombre)
            if os.path.isfile(ruta):
                return ruta
        return None
