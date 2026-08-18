#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas de la memoria por señales — vigencia y poda (`pendiente 02`).

Corre sin tocar la base real: cada prueba usa una base temporal.
    python memoria/pruebas.py
"""
import contextlib
import datetime
import hashlib
import io
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
import types
import unittest

_AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _AQUI)
import memoria  # noqa: E402
import semantica  # noqa: E402


def _ns(**kw):
    return types.SimpleNamespace(**kw)


def _huella(ruta):
    """Huella del archivo, o None si no existe. Sirve para probar que la base
    real quedó intacta: sin esto, una prueba que la tocara pasaría igual."""
    if not os.path.exists(ruta):
        return None
    with open(ruta, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


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

    # -- ciclo de la deuda (03) -------------------------------------------
    def test_migrar_agrega_columnas_de_cierre(self):
        con = self._con()
        memoria.migrar(con)
        cols = [r[1] for r in con.execute("PRAGMA table_info(senales)")]
        con.close()
        self.assertIn("cerrada_en", cols)
        self.assertIn("cierra_ref", cols)

    def test_cerrar_marca_estado_fecha_y_ref(self):
        self._add(tipo="deuda-tecnica", titulo="Falta índice")
        memoria.cmd_cerrar(_ns(db=self.db, id="S-001", ref="F3 / abc123"))
        con = self._con()
        r = con.execute("SELECT estado,cerrada_en,cierra_ref FROM senales WHERE id='S-001'").fetchone()
        con.close()
        self.assertEqual(r["estado"], "cerrada")
        self.assertEqual(r["cerrada_en"], datetime.date.today().isoformat())
        self.assertEqual(r["cierra_ref"], "F3 / abc123")

    def test_pendientes_solo_deuda_y_preguntas_abiertas(self):
        self._add(tipo="deuda-tecnica", titulo="Falta índice")
        self._add(tipo="pregunta-abierta", titulo="¿IVA por línea?")
        self._add(tipo="decision", titulo="Usar Redis")          # no es deuda
        con = self._con()
        abiertas = con.execute(
            "SELECT id FROM senales WHERE estado='activa' AND tipo IN ('deuda-tecnica','pregunta-abierta')"
        ).fetchall()
        con.close()
        self.assertEqual({r["id"] for r in abiertas}, {"S-001", "S-002"})

    def test_cerrada_fuera_de_pendientes(self):
        self._add(tipo="deuda-tecnica", titulo="Falta índice")
        memoria.cmd_cerrar(_ns(db=self.db, id="S-001", ref="x"))
        con = self._con()
        n = con.execute("SELECT COUNT(*) FROM senales WHERE estado='activa'"
                        " AND tipo IN ('deuda-tecnica','pregunta-abierta')").fetchone()[0]
        con.close()
        self.assertEqual(n, 0)


class TiposYAlcances(unittest.TestCase):
    """Qué se guarda, con qué tipo y con qué alcance — EP-006 · HU-001 · CA-02.

    Lo que se vigila: que ninguna señal quede guardada sin saber de qué tipo es
    ni a qué alcanza. El esquema declara `tipo TEXT NOT NULL` sin lista cerrada,
    así que quien rechaza el tipo inventado es `memoria.cmd_add`, no SQLite: si
    alguien inserta por SQL directo, entra. Eso está dicho en el resultado de la
    fase, no tapado acá.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = os.path.join(self.tmp.name, "s.db")
        memoria.cmd_init(_ns(db=self.db))
        # Huella de la base real: ninguna prueba la toca (08·T4).
        self.huella_real = _huella(memoria.DB_DEFAULT)
        self.addCleanup(self._base_real_intacta)

    def _base_real_intacta(self):
        self.assertEqual(_huella(memoria.DB_DEFAULT), self.huella_real,
                         "una prueba tocó la base real")

    def _filas(self):
        con = memoria.conectar(self.db)
        r = con.execute("SELECT id,tipo,titulo,scope,estado FROM senales").fetchall()
        con.close(); return r

    def _cli(self, *args):
        return subprocess.run([sys.executable, os.path.join(_AQUI, "memoria.py"),
                               "--db", self.db, *args],
                              capture_output=True, text=True)

    # -- CP-002 · pasos 1 y 3: sin tipo y con tipo inventado no entran ------
    def test_sin_tipo_no_entra(self):
        r = self._cli("add", "--titulo", "sin tipo")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(len(self._filas()), 0)

    def test_tipo_que_no_existe_no_entra(self):
        with self.assertRaises(SystemExit):
            memoria.cmd_add(_ns(db=self.db, tipo="conclusion", titulo="t", what="",
                                why="", learned="", scope="proyecto:x", reemplaza=None,
                                autor="test", **{"where": ""}))
        self.assertEqual(len(self._filas()), 0)

    # -- CP-002 · paso 2: sin alcance entra con el de proyecto -------------
    def test_sin_alcance_entra_con_el_de_proyecto(self):
        r = self._cli("add", "--tipo", "decision", "--titulo", "sin alcance")
        self.assertEqual(r.returncode, 0, r.stderr)
        filas = self._filas()
        self.assertEqual(len(filas), 1)
        self.assertEqual(filas[0]["scope"], "proyecto")

    # -- CP-002 · paso 4: la completa entra con lo que declaró -------------
    def test_completa_entra_con_lo_que_declaro(self):
        memoria.cmd_add(_ns(db=self.db, tipo="restriccion", titulo="No borrar la base",
                            what="w", why="y", learned="l", scope="modulo:memoria",
                            reemplaza=None, autor="test", **{"where": "memoria/"}))
        filas = self._filas()
        self.assertEqual(len(filas), 1)
        self.assertEqual((filas[0]["tipo"], filas[0]["scope"], filas[0]["estado"]),
                         ("restriccion", "modulo:memoria", "activa"))

    # -- los diez tipos declarados son los diez que acepta ------------------
    def test_los_diez_tipos_declarados_se_aceptan(self):
        self.assertEqual(len(memoria.TIPOS), 10)
        for i, tipo in enumerate(sorted(memoria.TIPOS), start=1):
            memoria.cmd_add(_ns(db=self.db, tipo=tipo, titulo=f"t{i}", what="", why="",
                                learned="", scope="proyecto:x", reemplaza=None,
                                autor="test", **{"where": ""}))
        self.assertEqual(len(self._filas()), 10)


class BusquedaPorPalabra(unittest.TestCase):
    """Buscar por palabra sin instalar nada — EP-006 · HU-003.

    Se corre siempre en modo `--lexica`: lo que esta HU pide es que la búsqueda
    funcione **con lo que la base ya trae**. Mezclarle la semántica probaría otra
    cosa, y encima haría que el resultado dependiera de si el modelo está o no.
    """

    def setUp(self):
        # `ignore_cleanup_errors` por el defecto D-02 de esta fase: cuando la
        # búsqueda no encuentra nada, `cmd_search` imprime y retorna **sin
        # cerrar la conexión**, y en Windows el archivo queda tomado. Sin esto,
        # cinco pruebas revientan al borrar la carpeta y el defecto se leería
        # como un error de las pruebas. Queda probado aparte, no tapado.
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.tmp.cleanup)
        self.db = os.path.join(self.tmp.name, "s.db")
        memoria.cmd_init(_ns(db=self.db))
        self.huella_real = _huella(memoria.DB_DEFAULT)
        self.addCleanup(self._base_real_intacta)

    def _base_real_intacta(self):
        self.assertEqual(_huella(memoria.DB_DEFAULT), self.huella_real,
                         "una prueba tocó la base real")

    def _add(self, tipo="decision", titulo="t", scope="proyecto:x", where="", what=""):
        memoria.cmd_add(_ns(db=self.db, tipo=tipo, titulo=titulo, what=what, why="",
                            learned="", scope=scope, reemplaza=None, autor="test",
                            **{"where": where}))

    def _buscar(self, query, scope=None, tipo=None, limit=10):
        """Devuelve el texto que imprime la búsqueda, en modo léxico."""
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            memoria.cmd_search(_ns(db=self.db, query=query, scope=scope, tipo=tipo,
                                   limit=limit, meses=6, lexica=True))
        return salida.getvalue()

    def _ids(self, texto):
        return set(re.findall(r"^(S-\d+)", texto, re.M))

    # -- CP-001 · la palabra buscada devuelve la señal, con su ubicación ----
    def test_la_palabra_buscada_devuelve_su_senal(self):
        self._add(titulo="Redis se cae", where="infra/redis.conf:12")
        self._add(titulo="Postgres afinado")
        self._add(titulo="Nginx recargado")
        self.assertEqual(self._ids(self._buscar("redis")), {"S-001"})

    def test_la_palabra_que_no_esta_no_devuelve_nada_y_no_falla(self):
        self._add(titulo="Redis se cae")
        salida = self._buscar("cobalto")
        self.assertEqual(self._ids(salida), set())
        self.assertIn("sin señales relevantes", salida)

    @unittest.expectedFailure
    def test_el_resultado_dice_donde_esta_la_senal(self):
        """CP-001 paso 2. **Falla hoy**, y es el hallazgo de la fase: `cmd_search`
        no selecciona ni imprime `where_`, así que el resultado no alcanza para
        abrir lo que se encontró, que es como CA-01 se da por aprobado.

        Va como fallo esperado, no borrada: arreglar `cmd_search` está fuera del
        plan aprobado de esta fase (`02·F8`), y el día que se arregle esta prueba
        pasa a «éxito inesperado» y obliga a volver acá."""
        self._add(titulo="Redis se cae", where="infra/redis.conf:12")
        self.assertIn("infra/redis.conf:12", self._buscar("redis"))

    # -- CP-002 · con acentos y sin ellos, en los dos sentidos -------------
    def test_encuentra_sin_acento_lo_guardado_con_acento(self):
        self._add(titulo="Facturación electrónica")
        self.assertEqual(self._ids(self._buscar("facturacion")), {"S-001"})

    def test_encuentra_con_acento_lo_guardado_sin_acento(self):
        self._add(titulo="Factura de compra")
        self.assertEqual(self._ids(self._buscar("factúra")), {"S-001"})

    def test_los_dos_sentidos_dan_el_mismo_conjunto(self):
        self._add(titulo="Facturación electrónica")
        self._add(titulo="Factura de compra")
        self.assertEqual(self._ids(self._buscar("factura")),
                         self._ids(self._buscar("factúra")))

    # -- CP-003 · los filtros de tipo y de alcance -------------------------
    def test_los_filtros_devuelven_solo_lo_que_corresponde(self):
        self._add(tipo="decision", titulo="Cache con redis", scope="proyecto:a")
        self._add(tipo="gotcha", titulo="Redis se cae", scope="proyecto:a")
        self._add(tipo="decision", titulo="Redis en cola", scope="organizacion")
        self.assertEqual(self._ids(self._buscar("redis")), {"S-001", "S-002", "S-003"})
        self.assertEqual(self._ids(self._buscar("redis", tipo="gotcha")), {"S-002"})
        self.assertEqual(self._ids(self._buscar("redis", scope="organizacion")), {"S-003"})
        self.assertEqual(self._ids(self._buscar("redis", scope="proyecto:a",
                                                tipo="decision")), {"S-001"})

    def test_filtrar_por_un_tipo_sin_senales_devuelve_vacio_sin_error(self):
        self._add(tipo="decision", titulo="Cache con redis")
        salida = self._buscar("redis", tipo="supuesto")
        self.assertEqual(self._ids(salida), set())
        self.assertIn("sin señales relevantes", salida)

    # -- CP-004 · la archivada no aparece, y sigue existiendo --------------
    def test_la_archivada_no_aparece_pero_sigue_en_la_base(self):
        self._add(titulo="Redis viejo")
        self._add(titulo="Redis nuevo")
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        self.assertEqual(self._ids(self._buscar("redis")), {"S-002"})
        con = memoria.conectar(self.db)
        fila = con.execute("SELECT estado FROM senales WHERE id='S-001'").fetchone()
        con.close()
        self.assertIsNotNone(fila, "archivar borró la señal")   # archivar ≠ borrar
        self.assertEqual(fila["estado"], "archivada")

    def test_desarchivada_vuelve_a_aparecer(self):
        self._add(titulo="Redis viejo")
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        con = memoria.conectar(self.db)
        con.execute("UPDATE senales SET estado='activa' WHERE id='S-001'")
        con.commit(); con.close()
        self.assertEqual(self._ids(self._buscar("redis")), {"S-001"})

    # -- CP-005 · el índice está al día -----------------------------------
    def test_la_senal_recien_guardada_ya_se_encuentra(self):
        self._add(titulo="Cobalto en el inventario")
        self.assertEqual(self._ids(self._buscar("cobalto")), {"S-001"})

    def test_el_texto_modificado_se_encuentra_por_la_palabra_nueva(self):
        self._add(titulo="Cobalto en el inventario")
        con = memoria.conectar(self.db)
        con.execute("UPDATE senales SET titulo='Niquel en el inventario' WHERE id='S-001'")
        con.commit(); con.close()
        self.assertEqual(self._ids(self._buscar("niquel")), {"S-001"})
        self.assertEqual(self._ids(self._buscar("cobalto")), set())

    def test_la_senal_borrada_deja_de_encontrarse(self):
        self._add(titulo="Cobalto en el inventario")
        con = memoria.conectar(self.db)
        con.execute("DELETE FROM senales WHERE id='S-001'")
        con.commit(); con.close()
        self.assertEqual(self._ids(self._buscar("cobalto")), set())

    # -- transversales de la HU, que el plan de pruebas no cubrió ----------
    def test_limites_buscar_en_una_memoria_vacia_no_falla(self):
        salida = self._buscar("lo que sea")
        self.assertIn("sin señales relevantes", salida)

    def test_limites_termino_vacio_o_de_solo_signos_no_falla(self):
        self._add(titulo="Redis se cae")
        for query in ("", "   ", "-- \"", "+++"):
            self.assertIn("vacío", self._buscar(query))

    def test_privacidad_la_busqueda_lexica_no_abre_ninguna_conexion(self):
        """El contenido no sale de la máquina para buscar. Se prueba cortando
        el socket: si algo intentara salir, la prueba falla en vez de pasar
        callada."""
        self._add(titulo="Redis se cae")
        import socket
        real = socket.socket

        class SinRed(socket.socket):
            def connect(self, *a, **k):
                raise AssertionError("la búsqueda intentó salir a la red")

        socket.socket = SinRed
        try:
            self.assertEqual(self._ids(self._buscar("redis")), {"S-001"})
        finally:
            socket.socket = real

    def test_inocuidad_buscar_no_modifica_lo_guardado(self):
        self._add(titulo="Redis se cae", where="infra/redis.conf:12")
        antes = _huella(self.db)
        self._buscar("redis")
        self.assertEqual(_huella(self.db), antes)

    @unittest.expectedFailure
    def test_la_busqueda_sin_resultados_cierra_su_conexion(self):
        """CP-005, borde. **Falla hoy** (defecto `D-02` de la fase): el camino
        «(sin señales relevantes)» de `cmd_search` retorna sin `con.close()`.
        Se prueba borrando el archivo: en Windows no se puede borrar lo que
        está tomado, así que el descuido se ve en vez de deducirse.

        Fallo esperado por lo mismo que el de arriba: tocar `memoria.py` está
        fuera del plan aprobado."""
        self._add(titulo="Redis se cae")
        self._buscar("cobalto")                       # no encuentra nada
        os.remove(self.db)                            # falla si quedó tomado


class MarcarLoQueDejoDeAplicar(unittest.TestCase):
    """Marcar sin borrar — EP-006 · HU-007.

    Los cuatro estados que sacan una señal de la búsqueda sin perderla:
    `archivada` (poda), `reemplazada` (llegó una mejor), `cerrada` (la deuda o
    la pregunta se resolvió) y `revertida`. La regla del esquema es que ninguna
    se borra.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.tmp.cleanup)
        self.db = os.path.join(self.tmp.name, "s.db")
        memoria.cmd_init(_ns(db=self.db))
        self.huella_real = _huella(memoria.DB_DEFAULT)
        self.addCleanup(self._base_real_intacta)

    def _base_real_intacta(self):
        self.assertEqual(_huella(memoria.DB_DEFAULT), self.huella_real,
                         "una prueba tocó la base real")

    def _add(self, tipo="decision", titulo="t", scope="proyecto:x"):
        memoria.cmd_add(_ns(db=self.db, tipo=tipo, titulo=titulo, what="", why="",
                            learned="", scope=scope, reemplaza=None, autor="test",
                            **{"where": ""}))

    def _fila(self, sid):
        con = memoria.conectar(self.db)
        r = con.execute("SELECT * FROM senales WHERE id=?", (sid,)).fetchone()
        con.close(); return r

    def _buscar(self, query):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            memoria.cmd_search(_ns(db=self.db, query=query, scope=None, tipo=None,
                                   limit=10, meses=6, lexica=True))
        return set(re.findall(r"^(S-\d+)", salida.getvalue(), re.M))

    # -- CA-01 · queda marcada y visible, y nada se borra ------------------
    def test_reemplazar_marca_la_vieja_y_no_la_borra(self):
        self._add(titulo="Cache en disco")
        self._add(titulo="Cache en memoria")
        memoria.cmd_supersede(_ns(db=self.db, id="S-001", by="S-002"))
        self.assertEqual(self._fila("S-001")["estado"], "reemplazada")
        self.assertIsNotNone(self._fila("S-001"), "reemplazar borró la señal")

    @unittest.expectedFailure
    def test_la_reemplazada_dice_que_la_reemplazo_y_cuando(self):
        """CA-01 pide que la marcada quede «con la fecha y qué lo reemplazó».
        **Falla hoy** (defecto `D-01` de la fase): `cmd_supersede` imprime
        «S-001 marcada reemplazada por S-002» y **no guarda ni el `by` ni la
        fecha** — la columna `reemplaza` se queda en `NULL`. Lo que dice la
        consola se pierde al cerrarla."""
        self._add(titulo="Cache en disco")
        self._add(titulo="Cache en memoria")
        memoria.cmd_supersede(_ns(db=self.db, id="S-001", by="S-002"))
        self.assertEqual(self._fila("S-001")["reemplaza"], "S-002")

    def test_reemplazar_no_baja_el_total_y_desde_la_nueva_se_llega_a_la_vieja(self):
        """CP-001, pasos 1, 3 y 5: el total sube en uno —nada se borró— y la
        nueva enlaza a la vieja por la columna `reemplaza`, que es la que sí
        se llena, porque la pone `add --reemplaza` y no `supersede`."""
        self._add(titulo="Cache en disco")
        con = memoria.conectar(self.db)
        antes = con.execute("SELECT COUNT(*) FROM senales").fetchone()[0]
        con.close()
        memoria.cmd_add(_ns(db=self.db, tipo="decision", titulo="Cache en memoria",
                            what="", why="", learned="", scope="proyecto:x",
                            reemplaza="S-001", autor="test", **{"where": ""}))
        memoria.cmd_supersede(_ns(db=self.db, id="S-001", by="S-002"))
        con = memoria.conectar(self.db)
        despues = con.execute("SELECT COUNT(*) FROM senales").fetchone()[0]
        con.close()
        self.assertEqual(despues, antes + 1)
        self.assertEqual(self._fila("S-002")["reemplaza"], "S-001")

    def test_archivar_conserva_todo_el_contenido(self):
        self._add(titulo="Redis se cae")
        antes = dict(self._fila("S-001"))
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        despues = dict(self._fila("S-001"))
        self.assertEqual(despues["estado"], "archivada")
        for campo in ("titulo", "what", "why", "learned", "tipo", "scope", "creada"):
            self.assertEqual(antes[campo], despues[campo],
                             f"marcar cambió `{campo}`")           # transversal: no regresión

    def test_cerrar_deja_fecha_y_referencia(self):
        self._add(tipo="deuda-tecnica", titulo="Falta índice")
        memoria.cmd_cerrar(_ns(db=self.db, id="S-001", ref="A-EP-006-HU-007"))
        fila = self._fila("S-001")
        self.assertEqual(fila["estado"], "cerrada")
        self.assertEqual(fila["cerrada_en"], datetime.date.today().isoformat())
        self.assertEqual(fila["cierra_ref"], "A-EP-006-HU-007")

    def test_la_archivada_se_puede_seguir_leyendo_a_proposito(self):
        self._add(titulo="Redis se cae")
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            memoria.cmd_list(_ns(db=self.db, scope=None, tipo=None))
        self.assertIn("S-001", salida.getvalue())
        self.assertIn("archivada", salida.getvalue())

    # -- CA-02 · lo marcado no se confunde con lo vigente ------------------
    def test_la_busqueda_deja_fuera_los_cuatro_estados_no_vigentes(self):
        for i, titulo in enumerate(["Redis vigente", "Redis archivada",
                                    "Redis reemplazada", "Redis cerrada",
                                    "Redis revertida"], start=1):
            self._add(titulo=titulo)
        memoria.cmd_archivar(_ns(db=self.db, id="S-002"))
        memoria.cmd_supersede(_ns(db=self.db, id="S-003", by="S-001"))
        memoria.cmd_cerrar(_ns(db=self.db, id="S-004", ref="x"))
        con = memoria.conectar(self.db)
        con.execute("UPDATE senales SET estado='revertida' WHERE id='S-005'")
        con.commit(); con.close()
        self.assertEqual(self._buscar("redis"), {"S-001"})

    def test_la_senal_sin_revisar_hace_meses_se_distingue_de_la_fresca(self):
        self._add(titulo="Redis fresca")
        self._add(titulo="Redis vieja")
        con = memoria.conectar(self.db)
        vieja = (datetime.date.today() - datetime.timedelta(days=300)).isoformat()
        con.execute("UPDATE senales SET revisada=? WHERE id='S-002'", (vieja,))
        con.commit(); con.close()
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            memoria.cmd_search(_ns(db=self.db, query="redis", scope=None, tipo=None,
                                   limit=10, meses=6, lexica=True))
        lineas = {l[:5]: l for l in salida.getvalue().splitlines() if l.startswith("S-")}
        self.assertNotIn("sin verificar", lineas["S-001"])
        self.assertIn("sin verificar", lineas["S-002"])

    def test_revisar_la_vieja_la_vuelve_a_mostrar_como_fresca(self):
        """CP-004, paso 3."""
        self._add(titulo="Redis vieja")
        vieja = (datetime.date.today() - datetime.timedelta(days=300)).isoformat()
        con = memoria.conectar(self.db)
        con.execute("UPDATE senales SET revisada=? WHERE id='S-001'", (vieja,))
        con.commit(); con.close()
        self.assertIn("sin verificar", memoria.marca_vigencia(vieja, 6))
        memoria.cmd_revisar(_ns(db=self.db, id="S-001", viejas=False, scope=None,
                                limit=10, meses=6))
        self.assertEqual(memoria.marca_vigencia(self._fila("S-001")["revisada"], 6), "")

    def test_la_marca_de_vigencia_no_depende_del_huso(self):
        """CP-004, paso 4: `meses_desde` trabaja sobre fechas ISO, no sobre
        instantes, así que el resultado no cambia con la hora ni con el huso."""
        self.assertIsNone(memoria.meses_desde("no-es-fecha"))
        justo = (datetime.date.today() - datetime.timedelta(days=181)).isoformat()
        self.assertIn("sin verificar", memoria.marca_vigencia(justo, 6))
        self.assertEqual(memoria.marca_vigencia(datetime.date.today().isoformat(), 6), "")

    def test_ninguna_se_borra_en_todo_el_recorrido(self):
        """CP-003, paso 5: el total es el mismo antes y después de pasar por
        los cuatro estados que sacan una señal de la búsqueda."""
        for t in ("a", "b", "c", "d"):
            self._add(titulo=f"Redis {t}")
        con = memoria.conectar(self.db)
        antes = con.execute("SELECT COUNT(*) FROM senales").fetchone()[0]
        con.close()
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        memoria.cmd_supersede(_ns(db=self.db, id="S-002", by="S-004"))
        memoria.cmd_cerrar(_ns(db=self.db, id="S-003", ref="x"))
        con = memoria.conectar(self.db)
        despues = con.execute("SELECT COUNT(*) FROM senales").fetchone()[0]
        con.close()
        self.assertEqual(antes, despues)

    # -- transversales de la HU, que el plan de pruebas no cubrió ----------
    def test_trazabilidad_queda_cuando_se_cerro_y_con_que_referencia(self):
        self._add(tipo="pregunta-abierta", titulo="¿IVA por línea?")
        memoria.cmd_cerrar(_ns(db=self.db, id="S-001", ref="F3 / abc123"))
        fila = self._fila("S-001")
        self.assertTrue(fila["cerrada_en"] and fila["cierra_ref"])

    @unittest.expectedFailure
    def test_trazabilidad_queda_cuando_se_archivo(self):
        """El transversal de trazabilidad pide «quién lo marcó y cuándo».
        **Falla hoy** (defecto `D-02`): archivar no deja fecha en ninguna
        columna, así que de una señal archivada no se sabe cuándo se podó."""
        self._add(titulo="Redis se cae")
        memoria.cmd_archivar(_ns(db=self.db, id="S-001"))
        fila = self._fila("S-001")
        self.assertTrue(fila["cerrada_en"], "archivar no dejó fecha")


class BusquedaPorSignificado(unittest.TestCase):
    """Buscar por significado — EP-006 · HU-004.

    Lo que la HU pide no es que el modelo acierte, que eso no se puede fijar en
    una prueba: pide que **encuentre lo escrito con otras palabras** y que
    **sin el modelo la memoria siga sirviendo**. Lo segundo es lo que más
    importa, porque es la promesa de que instalarlo sea opcional de verdad.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.tmp.cleanup)
        self.db = os.path.join(self.tmp.name, "s.db")
        memoria.cmd_init(_ns(db=self.db))
        self.huella_real = _huella(memoria.DB_DEFAULT)
        self.addCleanup(self._base_real_intacta)

    def _base_real_intacta(self):
        self.assertEqual(_huella(memoria.DB_DEFAULT), self.huella_real,
                         "una prueba tocó la base real")

    def _add(self, titulo, what=""):
        memoria.cmd_add(_ns(db=self.db, tipo="aprendizaje", titulo=titulo, what=what,
                            why="", learned="", scope="proyecto:x", reemplaza=None,
                            autor="test", **{"where": ""}))

    def _buscar(self, query, lexica):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            memoria.cmd_search(_ns(db=self.db, query=query, scope=None, tipo=None,
                                   limit=5, meses=6, lexica=lexica))
        texto = salida.getvalue()
        return set(re.findall(r"^(S-\d+)", texto, re.M)), texto

    # -- CA-02 · sin el modelo, la búsqueda sigue funcionando -------------
    def test_sin_las_dependencias_responde_por_palabra_y_lo_dice(self):
        """CP-003. Se simula la ausencia de dependencias apagando
        `semantica.disponible`, que es el único punto donde `cmd_search`
        decide si hay semántica."""
        self._add("Redis se cae al reiniciar")
        real = semantica.disponible
        semantica.disponible = lambda: False
        try:
            ids, texto = self._buscar("redis", lexica=False)
        finally:
            semantica.disponible = real
        self.assertEqual(ids, {"S-001"})                     # responde
        self.assertIn("semántica no instalada", texto)       # y lo dice

    def test_sin_dependencias_da_lo_mismo_que_la_lexica_explicita(self):
        """CP-003, paso 4."""
        self._add("Redis se cae al reiniciar")
        self._add("Postgres afinado")
        real = semantica.disponible
        semantica.disponible = lambda: False
        try:
            sin_deps, _ = self._buscar("redis", lexica=False)
        finally:
            semantica.disponible = real
        self.assertEqual(sin_deps, self._buscar("redis", lexica=True)[0])

    @unittest.expectedFailure
    def test_con_dependencias_pero_sin_el_modelo_la_busqueda_no_se_cae(self):
        """CA-02 dice «**sin el modelo**, la búsqueda sigue funcionando».
        **Falla hoy** (defecto `D-01` de la fase): `semantica.disponible()`
        solo comprueba que `numpy` y `model2vec` **importen**; no comprueba
        que el modelo se pueda cargar. Con las librerías puestas y el modelo
        ausente, `cmd_search` no atrapa el error y se cae entera — se lleva
        por delante hasta la búsqueda por palabra, que no necesita nada."""
        self._add("Redis se cae al reiniciar")
        real_modelo, real_cargado = semantica.MODELO, semantica._modelo
        semantica.MODELO, semantica._modelo = "minishlab/no-existe-este-modelo", None
        try:
            ids, _ = self._buscar("redis", lexica=False)
            self.assertEqual(ids, {"S-001"})
        finally:
            semantica.MODELO, semantica._modelo = real_modelo, real_cargado

    # -- CA-01 y transversales, solo si el modelo está en esta máquina ----
    @unittest.skipUnless(semantica.disponible(), "sin las dependencias opcionales")
    def test_encuentra_lo_escrito_con_otras_palabras(self):
        """CP-001, pasos 1 a 3: la consulta no comparte ninguna palabra con la
        señal. Se comprueba además que la léxica **no** la encontraría — sin
        eso, el caso no diría qué aporta la semántica."""
        self._add("El servidor de correo dejó de responder por falta de memoria")
        self._add("Convención para nombrar las columnas de la base")
        consulta = "cayó la máquina sin RAM"
        self.assertEqual(self._buscar(consulta, lexica=True)[0], set())
        self.assertIn("S-001", self._buscar(consulta, lexica=False)[0])

    @unittest.skipUnless(semantica.disponible(), "sin las dependencias opcionales")
    def test_la_hibrida_no_pierde_lo_que_la_lexica_encontraba(self):
        """CP-002, pasos 1 a 3: la fusión por rango recíproco une las dos
        listas, no las reemplaza."""
        self._add("Redis se cae al reiniciar")
        self._add("Convención para nombrar las columnas")
        lexica, _ = self._buscar("redis", lexica=True)
        hibrida, _ = self._buscar("redis", lexica=False)
        self.assertTrue(lexica)
        self.assertTrue(lexica <= hibrida, f"la híbrida perdió {lexica - hibrida}")

    @unittest.skipUnless(semantica.disponible(), "sin las dependencias opcionales")
    def test_privacidad_el_contenido_de_las_senales_no_sale_de_la_maquina(self):
        """CP-004. Con la red caída, indexar y buscar funcionan igual: los
        vectores se calculan en local y el modelo se lee del disco.

        **Lo que esta prueba no puede afirmar** es que el programa no abra
        ninguna conexión: `from_pretrained` consulta el repositorio del modelo
        al cargarlo. Lo que sí comprueba es que **el texto de las señales no
        viaja** y que sin red el resultado es el mismo. Ver el defecto `D-02`."""
        self._add("El servidor de correo dejó de responder")
        con_red, _ = self._buscar("cayó la máquina", lexica=False)

        import socket
        real = socket.socket

        class RedCaida(socket.socket):
            def connect(self, *a, **k):
                raise OSError("red caída")

        socket.socket = RedCaida
        try:
            sin_red, _ = self._buscar("cayó la máquina", lexica=False)
        finally:
            socket.socket = real
        self.assertEqual(con_red, sin_red)

    @unittest.skipUnless(semantica.disponible(), "sin las dependencias opcionales")
    def test_indexar_no_recalcula_lo_que_no_cambio(self):
        """RNF de rendimiento: el costo se paga una vez. `indexar` compara por
        hash del texto, así que la segunda pasada no embebe nada."""
        self._add("El servidor de correo dejó de responder")
        con = memoria.conectar(self.db)
        primera = semantica.indexar(con)
        segunda = semantica.indexar(con)
        con.close()
        self.assertEqual(primera, 1)
        self.assertEqual(segunda, 0)


class Semantica(unittest.TestCase):
    """Búsqueda semántica (05). Núcleo puro, sin base ni modelo."""

    def test_rrf_fusiona_por_rango(self):
        # b aparece bien rankeada en ambas listas -> gana; c solo en una.
        orden = memoria._rrf([["a", "b", "c"], ["b", "d", "a"]])
        self.assertEqual(orden[0], "b")
        self.assertIn("a", orden[:3])

    def test_rrf_lista_unica_conserva_orden(self):
        self.assertEqual(memoria._rrf([["x", "y", "z"]]), ["x", "y", "z"])

    def test_ranking_ordena_por_coseno(self):
        import numpy as np
        matriz = np.array([[1, 0, 0], [0, 1, 0], [0.9, 0.1, 0]], dtype="float32")
        res = semantica.ranking(np.array([1, 0, 0], dtype="float32"),
                                [10, 20, 30], matriz)
        self.assertEqual(res[0][0], 10)      # idéntico primero
        self.assertEqual(res[1][0], 30)      # casi paralelo segundo

    def test_ranking_vacio(self):
        import numpy as np
        self.assertEqual(semantica.ranking(np.zeros(3, "float32"), [],
                                           np.zeros((0, 3), "float32")), [])

    def test_disponible_es_bool(self):
        self.assertIsInstance(semantica.disponible(), bool)


if __name__ == "__main__":
    unittest.main(verbosity=2)
