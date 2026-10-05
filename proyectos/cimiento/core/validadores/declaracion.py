"""Lo que el proyecto declara de sí mismo en `.agente/`.

Hay reglas que no se pueden comprobar sin saber algo que solo el proyecto sabe:
su convención de nombres, dónde viven sus módulos, qué tablas son de dominio y
qué entidades son inmutables. Dos archivos lo declaran:

  `.agente/mapeo-nombres.md` · la convención, en una tabla de claves fijas.
  `.agente/dominio.md`       · el dominio: tablas de entidades y de módulos.

**Lo que no se declara no se comprueba.** Una clave en `libre`, una celda sin
llenar o el archivo ausente hacen que la comprobación se salte, no que falle:
un validador que exige lo que nadie acordó se termina apagando.
"""
import fnmatch
import os

from ..comun import AVISO, Hallazgo, Markdown
from .base import Validador

CONVENCIONES = ".agente/mapeo-nombres.md"
DOMINIO = ".agente/dominio.md"

# La lista es cerrada a propósito: una clave nueva se agrega primero a
# `plantillas/mapeo-nombres.md`, que es la norma.
CLAVES = {
    "modulos.ruta": "14·EST1 · dónde vive cada módulo",
    "tablas.caso": "14·EST2 · nombres de tabla",
    "columnas.caso": "14·EST2 · nombres de columna",
    "clases.caso": "14·EST2 · nombres de clase",
    "fk.sufijo": "14·EST2 · claves foráneas",
    "booleanos.prefijo": "14·EST2 · columnas booleanas",
    "timestamps.sufijo": "14·EST2 · fechas de evento",
    "permisos.formato": "04·S1 · forma de un permiso",
    "auditoria.columnas": "03·D1 · auditoría de toda tabla de dominio",
    "inmutables.estados": "15·IM2 · los tres estados",
    "inmutables.anulacion": "15·IM2 · campos de anulación",
    "inmutables.permiso": "15·IM5 · permiso propio de anular",
    "legacy.ignorar": "14·EST3 · lo que quedó fuera de la convención",
}

# `libre` es la ausencia de valor: el proyecto decide no declararlo.
SIN_DECLARAR = {"libre", "libre.", "—", "-", ""}


class Entidad:
    """Una fila de la tabla de entidades de `dominio.md`."""

    def __init__(self, nombre, tabla, clave_natural, inmutable):
        self.nombre = nombre
        self.tabla = tabla
        self.clave_natural = clave_natural      # lista de columnas
        self.inmutable = inmutable

    def __repr__(self):
        return "Entidad(%r, tabla=%r)" % (self.nombre, self.tabla)


class Modulo:
    """Una fila de la tabla de módulos de `dominio.md`."""

    def __init__(self, nombre, carpeta, especificacion):
        self.nombre = nombre
        self.carpeta = carpeta
        self.especificacion = especificacion

    def __repr__(self):
        return "Modulo(%r, carpeta=%r)" % (self.nombre, self.carpeta)


class Declaracion:
    """Lo que el proyecto declaró, ya limpio. Lo que no declaró, no está."""

    def __init__(self, raiz):
        self.raiz = raiz
        self.convenciones = {}
        self.entidades = []
        self.modulos = []
        self.archivos = {}          # ruta declarada -> si existe

    @classmethod
    def leer(cls, proyecto, archivos):
        """La declaración de `proyecto`. Siempre devuelve una, aunque esté vacía."""
        d = cls(proyecto.raiz)
        ruta = proyecto.ruta(CONVENCIONES)
        d.archivos[CONVENCIONES] = os.path.isfile(ruta)
        for _, fila in Markdown.filas_de(archivos.leer(ruta) if d.archivos[CONVENCIONES] else "",
                                         "clave", "valor"):
            clave = Markdown.valor_limpio(fila["clave"]).lower()
            valor = Markdown.valor_limpio(fila["valor"])
            if clave in CLAVES and valor.lower() not in SIN_DECLARAR:
                d.convenciones[clave] = valor

        ruta = proyecto.ruta(DOMINIO)
        d.archivos[DOMINIO] = os.path.isfile(ruta)
        texto = archivos.leer(ruta) if d.archivos[DOMINIO] else ""
        for _, fila in Markdown.filas_de(texto, "entidad", "tabla", "inmutable"):
            nombre = Markdown.valor_limpio(fila["entidad"])
            if nombre:
                clave = [c.strip() for c in Markdown.valor_limpio(
                    fila.get("clave natural", "")).split(",") if c.strip()]
                d.entidades.append(Entidad(nombre, Markdown.valor_limpio(fila["tabla"]), clave,
                                           cls._si(fila["inmutable"])))
        for _, fila in Markdown.filas_de(texto, "módulo", "carpeta", "especificación"):
            nombre = Markdown.valor_limpio(fila["módulo"])
            if nombre:
                d.modulos.append(Modulo(nombre, Markdown.valor_limpio(fila["carpeta"]),
                                        Markdown.valor_limpio(fila["especificación"])))
        return d

    @staticmethod
    def _si(celda):
        return Markdown.valor_limpio(celda).lower() in ("sí", "si", "sí.", "x", "true")

    def convencion(self, clave):
        """El valor declarado, o `""` si no se declaró."""
        return self.convenciones.get(clave, "")

    def lista(self, clave):
        """El valor declarado partido por comas; `[]` si no se declaró."""
        valor = self.convencion(clave)
        return [p.strip() for p in valor.split(",") if p.strip()] if valor else []

    def faltan(self):
        return [c for c in CLAVES if c not in self.convenciones]

    def ignorado(self, ruta):
        """¿La ruta quedó fuera por `legacy.ignorar` (`14·EST3`)?"""
        ruta = ruta.replace("\\", "/")
        for patron in self.lista("legacy.ignorar"):
            p = patron.replace("\\", "/")
            if fnmatch.fnmatch(ruta, p) or fnmatch.fnmatch(ruta, "*/" + p):
                return True
            if p.endswith("/") and ruta.startswith(p):
                return True
        return False

    def entidad_de(self, tabla):
        for e in self.entidades:
            if e.tabla and e.tabla.lower() == tabla.lower():
                return e
        return None

    def tablas_de_dominio(self):
        return [e for e in self.entidades if e.tabla]

    def inmutables(self):
        return [e for e in self.entidades if e.inmutable and e.tabla]

    def hay_algo(self):
        return bool(self.convenciones or self.entidades or self.modulos)


class DeclaracionDelProyecto(Validador):
    """Qué declaró el proyecto y qué comprobaciones se quedan sin correr.

    Todo es aviso: no declarar no es incumplir, pero cada clave en blanco es una
    regla que nadie está comprobando, y eso tiene que verse.
    """

    nombre = "declaracion"
    regla = "14·EST1, 14·EST2, 03·D1, 15·IM2, 15·IM5"
    descripcion = "lo que el proyecto declara en .agente/"

    def validar(self):
        d = Declaracion.leer(self.proyecto, self.archivos)
        hallazgos = [Hallazgo(AVISO, self.proyecto.ruta(ruta), 0,
                              "no existe `%s`; sin él no hay contra qué comparar" % ruta)
                     for ruta, existe in sorted(d.archivos.items()) if not existe]
        hallazgos += [Hallazgo(AVISO, self.proyecto.ruta(CONVENCIONES), 0,
                               "`%s` sin declarar — no se comprueba %s" % (clave, CLAVES[clave]))
                      for clave in d.faltan()]
        if d.archivos.get(DOMINIO) and not d.entidades:
            hallazgos.append(Hallazgo(AVISO, self.proyecto.ruta(DOMINIO), 0,
                                      "la tabla de entidades está vacía — no se comprueba 03·D1 "
                                      "(auditoría, UNIQUE, índices) ni 15·IM2/IM5"))
        if d.archivos.get(DOMINIO) and not d.modulos:
            hallazgos.append(Hallazgo(AVISO, self.proyecto.ruta(DOMINIO), 0,
                                      "la tabla de módulos está vacía — no se comprueba 14·EST1 "
                                      "ni el módulo sin especificación de 02·F2"))
        return hallazgos
