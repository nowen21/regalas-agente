# -*- coding: utf-8 -*-
"""Pendiente 15 · `EP-005·HU-011·CA-04` y `CA-05` — dónde termina el estándar.

**Las reglas son texto y sirven en cualquier parte. Lo que las hace cumplir,
no.** Hasta el 2026-08-19 los ocho enganches vivían mezclados con los cincuenta
y un programas agnósticos, y por eso nadie sabía de qué tamaño era el amarre.

**Lo que estas pruebas fijan es la frontera, no el conteo.** El conteo lo lleva
`amarre.py`. Acá se comprueba lo que una mudanza deshace sola con el tiempo:
que no vuelva a aparecer un enganche en `validadores/`, y que el adaptador siga
siendo lo único que la instalación enchufa.
"""
import json
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
ADAPTADOR = os.path.join(RAIZ, "adaptadores", "claude-code")
sys.path.insert(0, VALIDADORES)

import amarre      # noqa: E402
import instalar    # noqa: E402
from comun import leer   # noqa: E402


def _es_puente(ruta):
    """Los `validadores/hook_*.py` de la 26.0.1 reenvían al adaptador: no son
    enganches, son lo que evita que una instalación rezagada se bloquee. La
    prueba los dejó en rojo desde el 2026-08-19 sin que nadie la corriera."""
    return "Puente a la ruta nueva" in leer(ruta)[:200]


class LaFronteraSeSostiene(unittest.TestCase):

    def test_no_queda_ningun_enganche_en_validadores(self):
        """`validadores/` es lo que sirve con cualquier agente.

        Un enganche ahí no rompe nada hoy — y ese es el problema: vuelve a
        crecer el amarre sin que nadie lo note, que es lo que este pendiente
        vino a evitar.
        """
        sueltos = [f for f in os.listdir(VALIDADORES)
                   if f.startswith("hook_") and f.endswith(".py")
                   and not _es_puente(os.path.join(VALIDADORES, f))]
        self.assertEqual([], sueltos,
                         "estos van en adaptadores/claude-code/: %s" % sueltos)

    def test_los_enganches_del_adaptador_son_los_que_la_instalacion_enchufa(self):
        """Eran ocho el 2026-08-19 y el número se escribió acá; la 27.0.0 agregó
        uno sin tocarlo y la prueba quedó en rojo sin que nadie la corriera.
        Se cuenta contra la lista del instalador: la frontera es que no haya
        un enganche que nadie enchufa, ni un enchufe a un enganche que no está."""
        hay = sorted(f for f in os.listdir(ADAPTADOR)
                     if f.startswith("hook_") and f.endswith(".py"))
        enchufados = sorted({g for _e, _m, g, _msg, _a in instalar.HOOKS_CLAUDE})
        self.assertEqual(enchufados, hay)

    def test_la_instalacion_apunta_al_adaptador(self):
        """Si esto se separa, el enganche instalado apunta a un archivo que no
        existe — y deja de correr **en silencio**."""
        cmd = instalar._hook_claude("/estandar", "/proyecto",
                                    "hook_md.py", "mensaje")["command"]
        self.assertIn("adaptadores/claude-code/hook_md.py", cmd)
        self.assertNotIn("validadores/hook_", cmd)

    def test_cada_guion_de_la_lista_existe_donde_dice(self):
        """La lista de eventos y los archivos son dos cosas que se separan."""
        for _evento, _m, guion, _msg, _args in instalar.HOOKS_CLAUDE:
            with self.subTest(guion=guion):
                self.assertTrue(os.path.isfile(os.path.join(ADAPTADOR, guion)),
                                "%s no está en el adaptador" % guion)


class ElMapaSigueViendoElAmarre(unittest.TestCase):
    """La mudanza pudo dejar el amarre fuera del recuento, y eso era peor."""

    def test_el_recuento_incluye_las_dos_carpetas(self):
        """Mirando solo `validadores/` diría «10 de 51» y sonaría a mejora.

        Lo que hubo fue una mudanza. Un mapa que mejora solo porque el código
        se movió es un mapa que miente.
        """
        piezas = amarre.piezas(RAIZ)
        self.assertIn("hook_md.py", piezas,
                      "el adaptador quedó fuera del recuento")
        self.assertIn("enlaces.py", piezas)

    def test_los_enganches_cuentan_como_amarrados(self):
        piezas = amarre.piezas(RAIZ)
        for guion in ("hook_md.py", "hook_sesion.py"):
            with self.subTest(guion=guion):
                self.assertGreater(piezas.get(guion, 0), 0,
                                   "%s no nombra la herramienta?" % guion)


class ElContratoEstaEscrito(unittest.TestCase):
    """`CA-05`: soportar otro agente tiene que ser llenar un formulario."""

    RUTA = os.path.join(RAIZ, "adaptadores", "contrato.md")

    def test_existe(self):
        self.assertTrue(os.path.isfile(self.RUTA))

    def test_dice_las_cinco_capacidades(self):
        texto = leer(self.RUTA)
        for pieza in ("Inyectar texto", "escribe un archivo",
                      "manda un mensaje", "termina de responder",
                      "commit"):
            with self.subTest(pieza=pieza):
                self.assertIn(pieza, texto)

    def test_dice_tambien_lo_que_NO_necesita(self):
        """**Es la mitad que se olvida**, y la que decide si otro agente sirve.

        Sin ella, quien evalúe una herramienta nueva no sabe qué puede
        descartar, y termina exigiendo de más.
        """
        self.assertIn("NO necesita", leer(self.RUTA))


if __name__ == "__main__":
    unittest.main()
