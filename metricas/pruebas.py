#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas de las métricas del proceso (pendiente 06). Núcleo puro, sin base.

    python metricas/pruebas.py
"""
import datetime
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import metricas  # noqa: E402


def _f(tipo, estado, revisada=None):
    return {"tipo": tipo, "estado": estado, "revisada": revisada}


class Resumen(unittest.TestCase):

    def test_cuenta_por_estado_y_tipo(self):
        m = metricas.resumen([_f("decision", "activa"), _f("gotcha", "activa"),
                              _f("decision", "reemplazada")])
        self.assertEqual(m["total"], 3)
        self.assertEqual(m["por_estado"], {"activa": 2, "reemplazada": 1})
        self.assertEqual(m["por_tipo"], {"decision": 2, "gotcha": 1})

    def test_deuda_abierta_vs_cerrada(self):
        filas = [_f("deuda-tecnica", "activa"), _f("pregunta-abierta", "activa"),
                 _f("deuda-tecnica", "cerrada"), _f("decision", "activa")]
        m = metricas.resumen(filas)
        self.assertEqual(m["deuda_abierta"], 2)
        self.assertEqual(m["deuda_cerrada"], 1)     # la decision no cuenta como deuda

    def test_sin_verificar_solo_activas_y_viejas(self):
        viejo = (datetime.date.today() - datetime.timedelta(days=240)).isoformat()
        hoy = datetime.date.today().isoformat()
        filas = [_f("decision", "activa", viejo),        # cuenta
                 _f("decision", "activa", hoy),          # fresca: no
                 _f("gotcha", "archivada", viejo)]       # no activa: no
        m = metricas.resumen(filas, meses=6)
        self.assertEqual(m["sin_verificar"], 1)

    def test_reporte_no_revienta_con_base_vacia(self):
        # Regresión: divisiones por cero al no haber deuda ni activas.
        texto = metricas.reportar(metricas.resumen([]), 6)
        self.assertIn("Señales: 0", texto)


if __name__ == "__main__":
    unittest.main(verbosity=2)
