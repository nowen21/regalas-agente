# -*- coding: utf-8 -*-
"""`EP-028·HU-005` · Cada formulario de Cimiento trae su ayuda: CP-001 y CP-002.

Lee las plantillas: cada campo visible con su «?» y cada pantalla con su ayuda de
pantalla. Que toda clave tenga texto lo exige `core/ayuda/tests.py`.
"""
import os

from django.test import SimpleTestCase

from .textos import CAMPOS, PANTALLAS

CORE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# plantilla → (pantalla, claves de sus campos)
FORMULARIOS = {
    "cuentas/templates/cuentas/entrar.html": (None, ["entrar.usuario", "entrar.clave"]),
    "consumo/templates/consumo/tablero.html": ("gasto", ["gasto.proyecto", "gasto.dias"]),
    "estandar/templates/estandar/documento.html": ("documento", ["documento.ruta", "documento.texto"]),
    "estandar/templates/estandar/git.html": ("git", ["git.asunto", "git.idea", "git.hecho", "git.subir"]),
    "estandar/templates/estandar/lista.html": ("estandar", ["estandar.buscar"]),
    "estandar/templates/estandar/recuerdo.html": ("recuerdo", ["recuerdo.nombre", "recuerdo.texto"]),
    "estandar/templates/estandar/reportes.html": ("reportes", ["reporte.proyecto", "reporte.titulo", "reporte.regla",
                                                                "reporte.texto", "reporte.version", "reporte.motivo"]),
    "estandar/templates/estandar/vista_previa.html": ("vista_previa", ["vista_previa.proyecto", "vista_previa.mensaje"]),
    "estandar/templates/estandar/propuestas.html": ("propuestas", ["propuesta.rechazo"]),
    "historia/templates/historia/lista.html": ("historia", ["historia.tabla", "historia.accion"]),
    "historia/templates/historia/versiones.html": ("versiones", ["versiones.proyecto"]),
    "niveles/templates/niveles/reglas.html": ("reglas", ["nivel.regla"]),
    "proyectos/templates/proyectos/formulario.html": ("proyecto", []),
    "proyectos/templates/proyectos/configuracion.html": ("configuracion", []),
    "proyectos/templates/proyectos/suspensiones.html": ("suspensiones", []),
}


def _leer(rel):
    with open(os.path.join(CORE, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


class LaAyudaDeLosFormularios(SimpleTestCase):

    def test_cp001_cada_campo_tiene_su_ayuda_con_texto(self):
        for rel, (_, claves) in FORMULARIOS.items():
            texto = _leer(rel)
            for clave in claves:
                self.assertIn('{%% ayuda_campo "%s" %%}' % clave, texto, rel)
                self.assertIn(clave, CAMPOS, clave)
        parcial = _leer("proyectos/templates/proyectos/_ayuda_del_campo.html")
        self.assertIn('"proyecto."|add:campo.name', parcial)
        for clave in ("proyecto.nombre", "proyecto.ruta", "proyecto.activo"):
            self.assertIn(clave, CAMPOS)

    def test_cp002_cada_pantalla_con_formulario_dice_para_que_sirve(self):
        for rel, (pantalla, _) in FORMULARIOS.items():
            if pantalla is None:
                continue            # entrar: antes de la cuenta no hay botón de ayuda
            self.assertIn('{%% ayuda_pantalla "%s" %%}' % pantalla, _leer(rel), rel)
            self.assertIn("para_que", PANTALLAS[pantalla], pantalla)
