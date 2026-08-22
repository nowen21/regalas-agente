# -*- coding: utf-8 -*-
"""`EP-004 · HU-016` · Un pendiente dice de dónde viene y en qué fase se hizo.

**Las dos direcciones de la misma trazabilidad.** Hacia arriba: un pendiente
abierto nombra la historia a la que baja, porque `02·F23` manda construirlo como
fase de una historia y sin ella nadie sabe de cuál. Hacia abajo: un pendiente
cerrado dice **en qué fase** se hizo, o el trabajo queda sin rastro.

**Por qué una falla y el otro avisa.** El abierto sin historia **no se puede
ejecutar**: es un impedimento. El cerrado sin fase ya no rompe nada, solo cortó
su rastro. Detener la corrida por un pendiente viejo sería un obstáculo
permanente, y un obstáculo permanente se apaga.

**Y por qué no se exige hacia atrás:** la exigencia nació el 2026-08-16
(decisión 26 del pendiente 59). Lo cerrado antes queda de su lado, igual que
`20·M10` hace con cualquier norma nueva.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pendientes                  # noqa: E402
from comun import AVISO, FALLA     # noqa: E402

FICHA = (u"# Pendiente · %s\n\n**Estado:** %s\n\n| | |\n|---|---|\n%s\n\n"
         u"## El problema\n\nTexto.\n")


class PendienteTrazable(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "pendientes", "hecho"))
        # una fase de verdad, para poder comprobar que la citada existe
        self.fase = os.path.join(self.tmp, "documentacion", "epicas", "EP-001-x",
                                 "HU-001-y", "A-EP-001-HU-001-la-fase")
        os.makedirs(self.fase)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def escribir(self, rel, texto):
        ruta = os.path.join(self.tmp, *rel.split("/"))
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    # ── hacia arriba: el abierto nombra su historia ──────────────────────

    def test_cp001_el_abierto_sin_la_fila_se_reporta(self):
        self.escribir("pendientes/77-algo.md",
                      FICHA % (u"Algo", u"abierto", u"| **Tamaño** | chico |"))
        h = pendientes.abierto_nombra_su_historia(self.tmp)
        self.assertEqual(1, len(h))
        self.assertEqual(FALLA, h[0].severidad, "un abierto sin historia no se puede ejecutar")

    def test_cp003_el_tema_declarado_pasa_y_la_fila_vacia_no(self):
        """No toda idea tiene historia todavía, y decirlo es una respuesta."""
        self.escribir("pendientes/77-libreta.md", FICHA % (
            u"Libreta", u"abierto",
            u"| **Historia de usuario** | No es un ítem, es la libreta: cada idea "
            u"nombra la suya al promoverse |"))
        self.assertEqual([], pendientes.abierto_nombra_su_historia(self.tmp))

        self.escribir("pendientes/78-vacio.md", FICHA % (
            u"Vacío", u"abierto", u"| **Historia de usuario** |  |"))
        h = pendientes.abierto_nombra_su_historia(self.tmp)
        self.assertTrue(any("vacía" in x.mensaje for x in h))

    def test_cp006_lo_que_no_es_un_pendiente_numerado_no_cuenta(self):
        """El índice de la carpeta no es un pendiente."""
        self.escribir("pendientes/README.md", u"# Índice\n\nnada.\n")
        self.assertEqual([], pendientes.abierto_nombra_su_historia(self.tmp))

    # ── hacia abajo: el cerrado declara su fase ──────────────────────────

    def test_cp001b_el_cerrado_sin_fase_se_reporta_y_el_que_la_nombra_no(self):
        self.escribir("pendientes/hecho/sin-fase.md", FICHA % (
            u"Sin fase", u"✅ **hecho** el 2026-08-20", u"| **Tamaño** | chico |"))
        h = pendientes.cerrado_declara_su_fase(self.tmp)
        self.assertEqual(1, len(h))
        self.assertEqual(AVISO, h[0].severidad, "no rompe nada hoy: informa")

        self.escribir("pendientes/hecho/con-fase.md", FICHA % (
            u"Con fase", u"✅ **hecho** el 2026-08-20, en la fase "
            u"`A-EP-001-HU-001-la-fase`", u"| **Tamaño** | chico |"))
        mensajes = [x.archivo for x in pendientes.cerrado_declara_su_fase(self.tmp)]
        self.assertFalse(any("con-fase" in m for m in mensajes))

    def test_cp002_la_fase_inventada_se_reporta(self):
        self.escribir("pendientes/hecho/inventada.md", FICHA % (
            u"Inventada", u"✅ **hecho** el 2026-08-20, en la fase "
            u"`Z-EP-999-HU-999-no-existe`", u"| **Tamaño** | chico |"))
        h = pendientes.cerrado_declara_su_fase(self.tmp)
        self.assertTrue(any("no existe" in x.mensaje for x in h))

    def test_cp003b_el_cerrado_por_decision_no_se_reporta(self):
        """No hubo desarrollo, así que no hay fase que nombrar."""
        self.escribir("pendientes/hecho/por-decision.md", FICHA % (
            u"Por decisión", u"✅ **hecho** el 2026-08-20 · cerrado por decisión "
            u"del usuario: no hubo que construir nada", u"| **Tamaño** | chico |"))
        self.assertEqual([], pendientes.cerrado_declara_su_fase(self.tmp))

    def test_cp004_lo_cerrado_antes_del_corte_queda_de_su_lado(self):
        """La norma nació el 2026-08-16 y no se aplica hacia atrás."""
        self.escribir("pendientes/hecho/viejo.md", FICHA % (
            u"Viejo", u"cerrado el 2026-08-06", u"| **Tamaño** | chico |"))
        self.assertEqual([], pendientes.cerrado_declara_su_fase(self.tmp))

    def test_cp005_sin_fecha_declarada_tampoco_se_exige(self):
        """Los viejos no declaran fecha; treinta avisos que nunca se van apagan
        la comprobación entera."""
        self.escribir("pendientes/hecho/sin-fecha.md",
                      u"# Hecho · Algo viejo\n\nTexto sin ficha ni fecha.\n")
        self.assertEqual([], pendientes.cerrado_declara_su_fase(self.tmp))


if __name__ == "__main__":
    unittest.main()
