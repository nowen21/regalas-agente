#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas de la memoria por señales — vigencia y poda (`pendiente 02`).

Corre sin tocar la base real: cada prueba usa una base temporal.
    python memoria/pruebas.py
"""
import datetime
import os
import sqlite3
import sys
import tempfile
import types
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import memoria  # noqa: E402


def _ns(**kw):
    return types.SimpleNamespace(**kw)


class Vigencia(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = os.path.join(self.tmp.name, "s.db")
        memoria.cmd_init(_ns(db=self.db))

    def _con(self):
        return memoria.conectar(self.db)

    def _add(self, tipo="decision", titulo="t", scope="proyecto:x"):
        memoria.cmd_add(_ns(db=self.db, tipo=tipo, titulo=titulo, what="", why="",
                            learned="", scope=scope, reemplaza=None, autor="test",
                            **{"where": ""}))

    def _envejecer(self, sid, dias):
        d = (datetime.date.today() - datetime.timedelta(days=dias)).isoformat()
        con = self._con()
        con.execute("UPDATE senales SET revisada=? WHERE id=?", (d, sid))
        con.commit(); con.close()

    def _revisada(self, sid):
        con = self._con()
        r = con.execute("SELECT revisada,estado FROM senales WHERE id=?", (sid,)).fetchone()
        con.close(); return r

    # -- helpers puros ----------------------------------------------------
    def test_meses_desde(self):
        hace_un_anio = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
        self.assertGreaterEqual(memoria.meses_desde(hace_un_anio), 11)
        self.assertIsNone(memoria.meses_desde("no-es-fecha"))

    def test_marca_solo_si_esta_vieja(self):
        viejo = (datetime.date.today() - datetime.timedelta(days=240)).isoformat()
        self.assertIn("sin verificar", memoria.marca_vigencia(viejo, 6))
        self.assertEqual(memoria.marca_vigencia(datetime.date.today().isoformat(), 6), "")

    # -- migración --------------------------------------------------------
    def test_migrar_agrega_revisada_y_rellena(self):
        # Base "vieja": sin la columna revisada.
        con = self._con()
        con.execute("DROP TABLE senales")
        con.execute("CREATE TABLE senales(rowid INTEGER PRIMARY KEY, id TEXT, tipo TEXT,"
                    " titulo TEXT, what TEXT, why TEXT, where_ TEXT, learned TEXT,"
                    " scope TEXT, estado TEXT, reemplaza TEXT, creada TEXT, autor TEXT)")
        con.execute("INSERT INTO senales(id,tipo,titulo,scope,estado,creada)"
                    " VALUES('S-001','decision','t','proyecto:x','activa','2024-01-01')")
        con.commit()
        memoria.migrar(con)
        cols = [r[1] for r in con.execute("PRAGMA table_info(senales)")]
        self.assertIn("revisada", cols)
        r = con.execute("SELECT revisada FROM senales WHERE id='S-001'").fetchone()
        con.close()
        self.assertEqual(r[0], "2024-01-01")            # rellena con creada

    # -- ciclo de vida ----------------------------------------------------
    def test_add_nace_revisada_hoy(self):
        self._add()
        self.assertEqual(self._revisada("S-001")[0], datetime.date.today().isoformat())

    def test_revisar_actualiza_la_fecha(self):
        self._add(); self._envejecer("S-001", 300)
        memoria.cmd_revisar(_ns(db=self.db, id="S-001", viejas=False, scope=None,
                                limit=10, meses=6))
        self.assertEqual(self._revisada("S-001")[0], datetime.date.today().isoformat())

    def test_archivar_saca_de_activa(self):
        self._add()
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        self.assertEqual(self._revisada("S-001")[1], "archivada")

    def test_archivada_no_sale_en_search(self):
        self._add(tipo="gotcha", titulo="Redis se cae")
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        con = self._con()
        n = con.execute("SELECT COUNT(*) FROM senales_fts f JOIN senales s ON s.rowid=f.rowid"
                        " WHERE senales_fts MATCH '\"redis\"*' AND s.estado='activa'").fetchone()[0]
        con.close()
        self.assertEqual(n, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
