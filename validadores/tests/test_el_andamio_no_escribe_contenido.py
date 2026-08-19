# -*- coding: utf-8 -*-
"""`09·12` · El andamio crea la estructura y **nada de contenido**.

**Es donde se cometen los errores que otros validadores detectan después:** el
consecutivo repetido, el nombre fuera del molde, el enlace que falta en uno de
los dos lados. La estructura se corrige en vez de nacer bien.

**Y la advertencia que trae el propio pendiente es la parte más importante:**

> *Un generador que además rellena texto produce documentos que pasan el
> validador sin decir nada, que es la peor combinación posible.*

Es el patrón del día visto del otro lado. Todo el día apareció «una comprobación
que pasa sin comprobar»; esto sería **un documento que cumple sin decir nada**.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import andamio     # noqa: E402
from comun import RAIZ      # noqa: E402


def arbol(*fases):
    """Una HU con las fases que se le den, y las plantillas reales."""
    tmp = tempfile.TemporaryDirectory()
    hu = os.path.join(tmp.name, andamio.CARPETA, "EP-001-cuerpo", "HU-003-nucleo")
    os.makedirs(hu)
    for f in fases:
        os.makedirs(os.path.join(hu, f))
    for _archivo, plantilla in andamio.DOCUMENTOS:
        origen = os.path.join(RAIZ, plantilla)
        destino = os.path.join(tmp.name, plantilla)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with io.open(origen, encoding="utf-8") as f:
            texto = f.read()
        with io.open(destino, "w", encoding="utf-8") as f:
            f.write(texto)
    return tmp


class ElConsecutivoSeCalculaLeyendo(unittest.TestCase):

    def test_la_primera_fase_es_A(self):
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        destino, _ = andamio.crear(tmp.name, "EP-001-cuerpo", "HU-003-nucleo", "algo")
        self.assertIn("A-EP-001-HU-003-algo", destino)

    def test_con_A_la_siguiente_es_B(self):
        tmp = arbol("A-EP-001-HU-003-lo-primero")
        self.addCleanup(tmp.cleanup)
        destino, _ = andamio.crear(tmp.name, "EP-001-cuerpo", "HU-003-nucleo", "algo")
        self.assertIn("B-EP-001-HU-003-algo", destino)

    def test_con_un_hueco_no_lo_rellena(self):
        """**Se lee lo que hay, no se cuenta cuántas hay.** Si existen `A` y `C`
        porque la `B` se renombró, contar daría `C` y **pisaría una fase viva**."""
        tmp = arbol("A-EP-001-HU-003-una", "C-EP-001-HU-003-otra")
        self.addCleanup(tmp.cleanup)
        destino, _ = andamio.crear(tmp.name, "EP-001-cuerpo", "HU-003-nucleo", "algo")
        self.assertIn("B-EP-001-HU-003-algo", destino)

    def test_despues_de_la_Z_sigue_AA(self):
        self.assertEqual("AA", andamio._letras(27))
        self.assertEqual("Z", andamio._letras(26))


class NoEscribeContenido(unittest.TestCase):
    """**La mitad que decide si esto sirve o hace daño.**"""

    def _crear(self, tmp):
        andamio.crear(tmp.name, "EP-001-cuerpo", "HU-003-nucleo", "algo", escribir=True)
        d = os.path.join(tmp.name, andamio.CARPETA, "EP-001-cuerpo",
                         "HU-003-nucleo", "A-EP-001-HU-003-algo")
        textos = {}
        for archivo, _p in andamio.DOCUMENTOS:
            ruta = os.path.join(d, archivo)
            if os.path.isfile(ruta):
                with io.open(ruta, encoding="utf-8") as f:
                    textos[archivo] = f.read()
        return textos

    def test_los_marcadores_de_contenido_quedan_intactos(self):
        """Si los rellenara, el documento pasaría el validador de plantillas
        **sin decir nada** — que es peor que no tenerlo."""
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        textos = self._crear(tmp)
        self.assertTrue(any("«" in t for t in textos.values()),
                        "el andamio no puede dejar los documentos sin marcadores")

    def test_crea_los_cinco_documentos(self):
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(5, len(self._crear(tmp)))

    def test_sin_aplicar_no_crea_nada(self):
        """**Ver antes de tocar**, como el resto de los que escriben."""
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        destino, _ = andamio.crear(tmp.name, "EP-001-cuerpo", "HU-003-nucleo", "algo")
        self.assertFalse(os.path.isdir(destino))


class Bordes(unittest.TestCase):

    def test_una_HU_que_no_existe_se_dice(self):
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        with self.assertRaises(ValueError):
            andamio.crear(tmp.name, "EP-001-cuerpo", "HU-999-no-existe", "algo")

    def test_una_epica_fuera_del_molde_se_dice(self):
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, andamio.CARPETA, "epica-rara", "HU-003-x"))
        with self.assertRaises(ValueError):
            andamio.crear(tmp.name, "epica-rara", "HU-003-x", "algo")


if __name__ == "__main__":
    unittest.main(verbosity=2)
