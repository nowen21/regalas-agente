#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lo que el proyecto declara de sí mismo en `.agente/`.

Hay reglas de la base que no se pueden comprobar sin saber algo que solo el
proyecto sabe: cuál es su convención de nombres, dónde viven sus módulos, qué
tablas son de dominio y cuáles entidades son inmutables. Sin eso, "sigue la
convención" es una discusión, no un sí/no — y el criterio de los validadores es
que un script no opina.

Este módulo **no comprueba nada**: lee la declaración y se la entrega a los que
sí comprueban (`estructura.py`, `entidades.py`, `flujo.py`).

Dos archivos, y cada uno declara lo suyo:

  `.agente/mapeo-nombres.md`  · la convención — tabla de claves fijas.
  `.agente/dominio.md`        · el dominio — tablas de entidades y de módulos.

**Lo que no se declara no se comprueba.** Una clave en `libre`, una celda sin
llenar o el archivo entero ausente hacen que la comprobación correspondiente se
salte, no que falle: un validador que exige lo que nadie acordó es un validador
que se termina apagando.
"""
import fnmatch
import os

import comun
from comun import AVISO, Hallazgo, filas_de, leer, relativo, valor_limpio

CONVENCIONES = ".agente/mapeo-nombres.md"
DOMINIO = ".agente/dominio.md"

# Las claves de la tabla de convenciones, con qué regla habilita cada una. El
# orden es el de la plantilla; la lista es cerrada a propósito: una clave nueva
# se agrega primero a `plantillas/mapeo-nombres.md`, que es la norma.
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

# `libre` = el proyecto decide no declararlo. No es un valor: es la ausencia.
SIN_DECLARAR = {"libre", "libre.", "—", "-", ""}


class Entidad:
    """Una fila de la tabla de entidades de `dominio.md`."""

    def __init__(self, nombre, tabla, clave_natural, inmutable):
        self.nombre = nombre
        self.tabla = tabla
        self.clave_natural = clave_natural      # lista de columnas
        self.inmutable = inmutable              # bool

    def __repr__(self):
        return f"Entidad({self.nombre!r}, tabla={self.tabla!r})"


class Modulo:
    """Una fila de la tabla de módulos de `dominio.md`."""

    def __init__(self, nombre, carpeta, especificacion):
        self.nombre = nombre
        self.carpeta = carpeta
        self.especificacion = especificacion

    def __repr__(self):
        return f"Modulo({self.nombre!r}, carpeta={self.carpeta!r})"


class Declaracion:
    """Lo que el proyecto declaró, ya limpio. Lo que no declaró, no está."""

    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.convenciones = {}
        self.entidades = []
        self.modulos = []
        self.archivos = {}          # ruta -> si existe

    # ── convención ────────────────────────────────────────────────────────

    def convencion(self, clave):
        """El valor declarado, o "" si el proyecto no lo declaró."""
        return self.convenciones.get(clave, "")

    def lista(self, clave):
        """El valor declarado, partido por comas. [] si no se declaró."""
        valor = self.convencion(clave)
        return [p.strip() for p in valor.split(",") if p.strip()] if valor else []

    def faltan(self):
        """Las claves que el proyecto dejó sin declarar."""
        return [c for c in CLAVES if c not in self.convenciones]

    def ignorado(self, ruta):
        """¿Esta ruta quedó fuera por `legacy.ignorar` (14·EST3)?"""
        ruta = ruta.replace("\\", "/")
        for patron in self.lista("legacy.ignorar"):
            p = patron.replace("\\", "/")
            if fnmatch.fnmatch(ruta, p) or fnmatch.fnmatch(ruta, f"*/{p}"):
                return True
            if p.endswith("/") and ruta.startswith(p):
                return True
        return False

    # ── dominio ───────────────────────────────────────────────────────────

    def entidad_de(self, tabla):
        """La entidad declarada sobre esa tabla, o None."""
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


def _texto(ruta):
    try:
        return leer(ruta)
    except OSError:
        return ""


def _si(celda):
    return valor_limpio(celda).lower() in ("sí", "si", "sí.", "x", "true")


def leer_declaracion(proyecto):
    """La declaración del proyecto. Siempre devuelve un objeto, aunque esté vacío."""
    proyecto = os.path.abspath(proyecto)
    d = Declaracion(proyecto)

    ruta_conv = os.path.join(proyecto, *CONVENCIONES.split("/"))
    d.archivos[CONVENCIONES] = os.path.isfile(ruta_conv)
    for _, fila in filas_de(_texto(ruta_conv), "clave", "valor"):
        clave = valor_limpio(fila["clave"]).lower()
        valor = valor_limpio(fila["valor"])
        if clave in CLAVES and valor.lower() not in SIN_DECLARAR:
            d.convenciones[clave] = valor

    ruta_dom = os.path.join(proyecto, *DOMINIO.split("/"))
    d.archivos[DOMINIO] = os.path.isfile(ruta_dom)
    texto_dom = _texto(ruta_dom)
    for _, fila in filas_de(texto_dom, "entidad", "tabla", "inmutable"):
        nombre = valor_limpio(fila["entidad"])
        if not nombre:
            continue
        clave = [c.strip() for c in
                 valor_limpio(fila.get("clave natural", "")).split(",") if c.strip()]
        d.entidades.append(Entidad(nombre, valor_limpio(fila["tabla"]),
                                   clave, _si(fila["inmutable"])))
    for _, fila in filas_de(texto_dom, "módulo", "carpeta", "especificación"):
        nombre = valor_limpio(fila["módulo"])
        if not nombre:
            continue
        d.modulos.append(Modulo(nombre, valor_limpio(fila["carpeta"]),
                                valor_limpio(fila["especificación"])))
    return d


def validar(proyecto):
    """Qué declaró el proyecto y qué comprobaciones se quedan sin correr.

    Todo **AVISO**: no declarar no es incumplir. Lo que sí importa es que se
    vea, porque cada clave en blanco es una regla que nadie está comprobando.
    """
    d = leer_declaracion(proyecto)
    hallazgos = []

    for ruta, existe in sorted(d.archivos.items()):
        if not existe:
            hallazgos.append(Hallazgo(
                AVISO, os.path.join(proyecto, ruta), 0,
                f"no existe `{ruta}`; sin él no hay contra qué comparar"))

    for clave in d.faltan():
        hallazgos.append(Hallazgo(
            AVISO, os.path.join(proyecto, CONVENCIONES), 0,
            f"`{clave}` sin declarar — no se comprueba {CLAVES[clave]}"))

    if d.archivos.get(DOMINIO) and not d.entidades:
        hallazgos.append(Hallazgo(
            AVISO, os.path.join(proyecto, DOMINIO), 0,
            "la tabla de entidades está vacía — no se comprueba 03·D1 "
            "(auditoría, UNIQUE, índices) ni 15·IM2/IM5"))
    if d.archivos.get(DOMINIO) and not d.modulos:
        hallazgos.append(Hallazgo(
            AVISO, os.path.join(proyecto, DOMINIO), 0,
            "la tabla de módulos está vacía — no se comprueba 14·EST1 "
            "ni el módulo sin especificación de 02·F2"))
    return hallazgos


def resumen(proyecto):
    """Una línea por lo declarado, para el subcomando."""
    d = leer_declaracion(proyecto)
    lineas = [f"{relativo(proyecto)}:"]
    for clave in CLAVES:
        valor = d.convencion(clave) or "(sin declarar)"
        lineas.append(f"  {clave:<22} {valor}")
    lineas.append(f"  {'entidades':<22} {len(d.entidades)} "
                  f"({len(d.inmutables())} inmutables)")
    lineas.append(f"  {'módulos':<22} {len(d.modulos)}")
    return "\n".join(lineas)


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada()
