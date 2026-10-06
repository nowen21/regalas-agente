# -*- coding: utf-8 -*-
"""`EP-025·HU-013` · Lo que vale cada ajuste en un proyecto, leído sin Django.

El del proyecto, si no el de la base de Cimiento, si no el de fábrica. Sin
base, el de fábrica: lo que lee esto informa o muestra, y no puede callarse
porque la base no responde. Una conexión para todo.

**Sin registro, todo de fábrica** (`EP-025·HU-014`): la base de Cimiento es de
los proyectos que administra. Así una carpeta temporal de una prueba no cambia
según lo que tenga guardado la máquina donde corre.
"""
from ..proyectos import ajustes as catalogo
from .niveles import BaseSinRespuesta, NivelesDelProyecto

_REGISTRADO = "SELECT id FROM proyectos_proyecto WHERE activo = 1 AND LOWER(ruta) = LOWER(%s)"
_BASE = "SELECT clave, valor FROM proyectos_ajustebase"
_DEL_PROYECTO = ("SELECT a.clave, a.valor FROM proyectos_ajustedelproyecto a "
                 "JOIN proyectos_proyecto p ON p.id = a.proyecto_id "
                 "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s)")


class ConfiguracionDelProyecto(NivelesDelProyecto):
    """Los ajustes del proyecto en `raiz`, con la capa de donde sale cada uno."""

    def __init__(self, raiz, estandar=None, ajustes=None):
        super().__init__(raiz, estandar, ajustes)
        self._efectivos = None

    def efectivos(self):
        """`{clave: (valor, capa)}`."""
        if self._efectivos is None:
            try:
                registrado, base, propios = self.consultar_juntas((_REGISTRADO, None), (_BASE, []),
                                                                  (_DEL_PROYECTO, None))
            except BaseSinRespuesta:
                registrado, base, propios = (), (), ()
            self._efectivos = catalogo.efectivos(dict(base), dict(propios)) if registrado \
                else catalogo.efectivos()
        return self._efectivos

    def valor(self, clave):
        return self.efectivos()[clave][0]
