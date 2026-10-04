# -*- coding: utf-8 -*-
"""`EP-023 · HU-003 · fase A` · El hallazgo y el pendiente tienen solo lo que les corresponde.

Los casos CP-003 a CP-008 del plan de pruebas de la fase, sobre un proyecto de
prueba en una carpeta temporal.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import fases        # noqa: E402
import pendientes   # noqa: E402
import resumen      # noqa: E402
from comun import FALLA   # noqa: E402

EPICA = "documentacion/epicas/EP-009-algo"
HU = EPICA + "/HU-001-una-cosa"
PENDIENTE = ("# Pendiente: algo falla\n\n| | |\n|---|---|\n| **De dónde sale** | {origen} |\n\n"
             "## El problema\n\nAlgo.\n\n## Por qué importa\n\nAlgo.\n")
ANALISIS = ("# Análisis 1: algo\n\n{marca}## Lo que se tiene que hacer\n\n"
            "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
            "| 1 | Hacer algo | 1 | {paso} |\n")
MARCA = "> **Aprobado** por el usuario el 2026-10-02, en el turno 3.\n\n"
HU_MD = "# HU-001 · Una cosa\n\n| Campo | Valor |\n|---|---|\n| **Estado** | {estado} |\n"


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Lista"))
        self.carpeta = os.path.join(self.raiz, *(EPICA + "/pendientes/110-algo-falla").split("/"))

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, relativa, texto):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def pendiente(self, origen="algo", marca=MARCA, paso="[HU-001](../../HU-001-una-cosa/HU-001-una-cosa.md)"):
        self.escribir(EPICA + "/pendientes/110-algo-falla/pendiente.md", PENDIENTE.format(origen=origen))
        if marca is not None:
            self.escribir(EPICA + "/pendientes/110-algo-falla/analisis-1.md",
                          ANALISIS.format(marca=marca, paso=paso))


class CP003LoNuevoPasa(Base):

    def test_el_pendiente_con_sus_tres_partes_pasa(self):
        self.pendiente()
        self.assertEqual([], [h for h in pendientes.validar(self.raiz) if h.severidad == FALLA])

    def test_al_que_le_falta_una_parte_se_le_nombra(self):
        self.escribir(EPICA + "/pendientes/110-algo-falla/pendiente.md", "# Pendiente: algo\n\n## El problema\n\nAlgo.\n")
        fallas = [h.mensaje for h in pendientes.validar(self.raiz) if h.severidad == FALLA]
        self.assertEqual(1, len(fallas))
        self.assertIn("«De dónde sale»", fallas[0])
        self.assertIn("«Por qué importa»", fallas[0])


class CP004ElCierreLoMarcaElPlan(Base):

    def test_sin_analisis_aprobado_esta_abierto(self):
        self.pendiente(marca="")
        self.assertEqual("abierto", pendientes.estado(self.carpeta, self.raiz))

    def test_con_su_hu_sin_terminar_esta_abierto(self):
        self.pendiente()
        self.assertEqual("abierto", pendientes.estado(self.carpeta, self.raiz))

    def test_con_su_hu_terminada_esta_cerrado_y_su_archivo_no_cambia(self):
        self.pendiente()
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada el 2026-10-02"))
        ruta = os.path.join(self.carpeta, "pendiente.md")
        antes = io.open(ruta, encoding="utf-8").read()
        self.assertEqual("cerrado", pendientes.estado(self.carpeta, self.raiz))
        self.assertEqual(antes, io.open(ruta, encoding="utf-8").read())

    def test_la_hu_nombrada_sin_enlace_tambien_cuenta(self):
        self.pendiente(paso="EP-009, HU-001, fase A")
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"))
        self.assertEqual("cerrado", pendientes.estado(self.carpeta, self.raiz))

    def test_la_hu_escrita_con_espacio_tambien_cuenta(self):
        self.pendiente(paso="EP-009, HU 1")
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"))
        self.assertEqual("cerrado", pendientes.estado(self.carpeta, self.raiz))

    def test_la_fila_de_la_epica_espera_a_que_la_epica_termine(self):
        self.pendiente(paso="EP-009, la épica")
        self.assertEqual("abierto", pendientes.estado(self.carpeta, self.raiz))
        self.escribir(EPICA + "/epica.md", HU_MD.format(estado="Terminada el 2026-10-03"))
        self.assertEqual("cerrado", pendientes.estado(self.carpeta, self.raiz))

    def test_lo_hecho_en_el_mismo_analisis_no_espera_nada(self):
        self.pendiente(paso="Este análisis, de una y sin fase")
        self.assertEqual("cerrado", pendientes.estado(self.carpeta, self.raiz))


class CP005ElHallazgoCalculaSuEstado(Base):

    def resumen(self, fila):
        return self.escribir("historico-chat/resumenes/2026-10-02/sesion.md",
                             "# Sesión\n\n### H-1 · Algo falla\n\n| Campo | Valor |\n|---|---|\n"
                             "| Qué pasó | Algo. |\n| Por qué importa | Algo. |\n" + fila)

    def test_sin_pendiente(self):
        ruta = self.resumen("")
        self.assertEqual([("H-1", "Algo falla", "abierto, sin pendiente")], resumen.hallazgos(ruta))

    def test_anotado_y_se_retoma_por_el_ultimo_analisis(self):
        self.pendiente()
        ruta = self.resumen("| Pendiente | [110](../../../%s/pendientes/110-algo-falla/pendiente.md) |\n" % EPICA)
        self.assertEqual("abierto, anotado", resumen.hallazgos(ruta)[0][2])
        self.assertTrue(resumen._retoma(ruta, "H-1").endswith("analisis-1.md"))
        self.assertEqual([("H-1", "Algo falla")], resumen.sin_resolver(ruta))

    def test_resuelto_cuando_su_plan_se_cumplio(self):
        self.pendiente()
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"))
        ruta = self.resumen("| Pendiente | [110](../../../%s/pendientes/110-algo-falla) |\n" % EPICA)
        self.assertEqual("resuelto", resumen.hallazgos(ruta)[0][2])
        self.assertEqual([], resumen.sin_resolver(ruta))

    def test_corregido_con_corrija_queda_resuelto(self):
        """`02·F8`, excepción: corregido con «Corrija» sin abrir análisis (2026-10-04)."""
        ruta = self.resumen("| Corregido con «Corrija» | El 2026-10-04: se corrigió el freno. |\n")
        self.assertEqual("resuelto", resumen.hallazgos(ruta)[0][2])

    def test_el_resumen_viejo_se_lee_como_siempre(self):
        ruta = self.resumen("| Estado | resuelto acá |\n")
        self.assertEqual("resuelto acá", resumen.hallazgos(ruta)[0][2])


class CP006ElSeguimientoCierraConSuPadre(Base):

    def test_toma_el_estado_de_su_padre(self):
        self.pendiente()
        hijo = os.path.join(self.raiz, "historico-chat", "resumenes", "2026-10-02", "pendientes", "111-espera")
        self.escribir("historico-chat/resumenes/2026-10-02/pendientes/111-espera/pendiente.md",
                      PENDIENTE.format(origen="[el del estándar](../../../../../%s/pendientes/110-algo-falla/pendiente.md)" % EPICA))
        self.assertEqual("abierto", pendientes.estado(hijo, self.raiz))
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"))
        self.assertEqual("abierto", pendientes.estado(hijo, self.raiz))      # falta comprobar (HU-003, CA-11)
        self.escribir("historico-chat/resumenes/2026-10-02/pendientes/111-espera/aviso-resuelto.md",
                      "**Comprobado:** 2026-10-03\n")
        self.assertEqual("cerrado", pendientes.estado(hijo, self.raiz))


class CP008LaCarpetaPendientes(Base):

    def test_el_validador_de_fases_acepta_pendientes_en_la_epica_y_en_la_hu(self):
        self.pendiente()
        self.escribir(HU + "/pendientes/112-otro/pendiente.md", PENDIENTE.format(origen="algo"))
        fallas = [h for h in fases.validar(self.raiz) if h.severidad == FALLA and "pendientes" in h.archivo]
        self.assertEqual([], fallas)

    def test_el_proximo_numero_cuenta_todas_las_carpetas(self):
        self.pendiente()
        self.escribir("historico-chat/resumenes/2026-10-02/pendientes/115-suelto/pendiente.md",
                      PENDIENTE.format(origen="algo"))
        self.escribir("pendientes/90-viejo.md", "# Pendiente · viejo\n")
        self.assertEqual(116, pendientes.proximo_libre(self.raiz))

    def test_el_mismo_numero_en_dos_carpetas_falla(self):
        self.pendiente()
        self.escribir("historico-chat/resumenes/2026-10-02/pendientes/110-otro/pendiente.md",
                      PENDIENTE.format(origen="algo"))
        fallas = [h.mensaje for h in pendientes.validar(self.raiz) if h.severidad == FALLA]
        self.assertTrue(any("el número 110" in f for f in fallas))

    def test_el_que_paso_a_la_forma_nueva_no_choca_con_su_archivo_viejo(self):
        self.pendiente()
        self.escribir("pendientes/110-algo-falla.md", "# Pendiente · algo falla\n")
        self.assertEqual([], [h for h in pendientes.validar(self.raiz)
                              if h.severidad == FALLA and "110" in h.mensaje])

    def test_el_indice_lista_todos_con_donde_viven_y_su_estado(self):
        self.pendiente()
        self.escribir("pendientes/90-viejo.md", "# Pendiente · viejo\n\n**Estado:** abierto.\n")
        ruta = pendientes.escribir_indice(self.raiz)
        texto = io.open(ruta, encoding="utf-8").read()
        self.assertEqual(os.path.join(self.raiz, "documentacion", "pendientes.md"), ruta)
        self.assertIn("| 90 | [viejo](../pendientes/90-viejo.md) | `pendientes/`, forma anterior | abierto |", texto)
        self.assertIn("| 110 | [algo falla](epicas/EP-009-algo/pendientes/110-algo-falla/pendiente.md) "
                      "| `documentacion/epicas/EP-009-algo/pendientes/110-algo-falla` | abierto |", texto)


if __name__ == "__main__":
    unittest.main()
