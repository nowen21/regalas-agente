# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de las fases `W` y `X` — `F-029` y `F-030`.

**El caso que decide el CP-002 es el que calla:** un aviso atendido no vuelve.
Un aviso que vuelve después de atendido enseña a ignorar la lista entera, y una
lista ignorada es peor que no tenerla.

**Y el que más protege es el CP-005:** que un proyecto sin datos aparezca así y
no en cero. Cero por ciento dice «va mal»; sin datos dice «no se sabe», y son
cosas distintas.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from nucleo.proyectos.models import Proyecto
from . import core, reporte

INVENTARIO = u"""# Inventario

| ID | Nombre | Tipo | Módulo | Prioridad | Estado | Verificado |
|---|---|---|---|---|---|---|
| F-001 | Conectar un proyecto | Obligatoria | Proyectos | Alta | Construida | Sin verificar |
| F-002 | Otra cosa | Obligatoria | Proyectos | Alta | Construida | Verificada |
| F-003 | La que falta | Obligatoria | Proyectos | Alta | Definida | Sin verificar |
"""

FASE = u"""# Estado de fase

| Campo | Valor |
|---|---|
| **Última actualización** | %(cuando)s |

**Estación actual:** 8 · Implementador.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador | contexto | ☑ |
| 2 | Proponente | alcance | ☑ |
| 3 | Épica | épica | ☑ |
| 4 | Historia | HUs | ☑ |
| 5 | Especificación | spec | ☑ |
| 6 | Diseñador | diseño | ☑ |
| 7 | Planificador | planes | ☑ |
| 8 | Implementador | pruebas verdes | %(ocho)s |
| 9 | Verificador | trazabilidad | ☐ |
| 10 | Crítico | hallazgos | ☐ |
| 11 | Cierre | docs | ☐ |
| 12 | Commit | autorizado | ☐ |
| 13 | Publicación | autorizado | N/A |
"""


class Base(TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="prueba-avisos-")

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def escribir(self, relativa, texto):
        completa = os.path.join(self.raiz, *relativa.split("/"))
        carpeta = os.path.dirname(completa)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        with io.open(completa, "w", encoding="utf-8", newline="") as abierto:
            abierto.write(texto)
        return completa

    def fase(self, epica, hu, nombre, cuando="2026-01-01", ocho=u"☐"):
        return self.escribir(
            "documentacion/epicas/%s/%s/%s/estado-fase.md" % (epica, hu, nombre),
            FASE % {"cuando": cuando, "ocho": ocho})

    def historia_sola(self, epica, hu):
        carpeta = os.path.join(self.raiz, "documentacion", "epicas", epica, hu)
        os.makedirs(carpeta, exist_ok=True)
        return carpeta


class CP001LosTresAvisosDicenQueYDonde(Base):
    """`CA-1` y `CA-2` de `F-029`."""

    def test_una_fase_detenida_se_avisa_con_los_dias_que_lleva(self):
        self.fase("EP-001-una", "HU-001-una", "A-EP-001-HU-001-quieta",
                  cuando="2026-01-01")
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        self.assertEqual(1, salida["cuantos"])
        uno = salida["avisos"][0]
        self.assertEqual(core.DETENIDA, uno["clase"])
        self.assertIn("día(s) sin tocarse", uno["que_lo_disparo"])
        self.assertIn("estado-fase.md", uno["donde_mirar"])

    def test_una_historia_sin_fase_se_avisa(self):
        self.historia_sola("EP-001-una", "HU-002-sola")
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        self.assertEqual([core.SIN_FASE],
                         [uno["clase"] for uno in salida["avisos"]])

    def test_lo_construido_sin_verificar_se_avisa_y_lo_definido_no(self):
        self.escribir("cvds/analisis-requisitos/inventario-funcionalidades.md",
                      INVENTARIO)
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        cuales = [uno["sobre_que"] for uno in salida["avisos"]]
        self.assertEqual(["F-001"], cuales)

    def test_todo_aviso_dice_que_lo_disparo_y_donde_mirar(self):
        self.fase("EP-001-una", "HU-001-una", "A-EP-001-HU-001-quieta")
        self.historia_sola("EP-001-una", "HU-002-sola")
        self.escribir("cvds/analisis-requisitos/inventario-funcionalidades.md",
                      INVENTARIO)
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        for uno in salida["avisos"]:
            self.assertTrue(uno["que_lo_disparo"])
            self.assertTrue(uno["donde_mirar"])
            self.assertIn("→", core.linea(uno))

    def test_lo_mas_grave_sale_primero(self):
        self.fase("EP-001-una", "HU-001-una", "A-EP-001-HU-001-quieta")
        self.historia_sola("EP-001-una", "HU-002-sola")
        self.escribir("cvds/analisis-requisitos/inventario-funcionalidades.md",
                      INVENTARIO)
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        self.assertEqual([core.DETENIDA, core.SIN_FASE, core.SIN_VERIFICAR],
                         [uno["clase"] for uno in salida["avisos"]])


class CP002ElAvisoAtendidoNoVuelve(Base):
    """`CA-3` de `F-029`."""

    def test_lo_callado_no_sale_y_se_dice_cuantos_son(self):
        self.historia_sola("EP-001-una", "HU-002-sola")
        self.escribir(".agente/avisos-atendidos.md",
                      u"| Qué | Cuándo | Por qué |\n|---|---|---|\n"
                      u"| HU-002-sola | 2026-09-01 | se escribió para más "
                      u"adelante, a propósito |\n")
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        self.assertEqual(0, salida["cuantos"])
        self.assertEqual(1, salida["callados"])
        self.assertIn("callados a propósito", core.dicho(salida))

    def test_arreglar_la_causa_tambien_lo_calla(self):
        self.historia_sola("EP-001-una", "HU-002-sola")
        self.assertEqual(1, core.de_un_proyecto(self.raiz, "2026-09-01")["cuantos"])
        self.fase("EP-001-una", "HU-002-sola", "A-EP-001-HU-002-ya-tiene",
                  cuando="2026-09-01")
        self.assertEqual(0, core.de_un_proyecto(self.raiz, "2026-09-01")["cuantos"])

    def test_sin_avisos_se_dice_con_palabras(self):
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        self.assertIn("Nada se salió", core.dicho(salida))


class CP003ElRuidoSeControla(Base):
    """Lo que la ficha advierte: demasiados avisos se ignoran completos."""

    def test_una_fase_que_lleva_poco_quieta_no_avisa(self):
        self.fase("EP-001-una", "HU-001-una", "A-EP-001-HU-001-reciente",
                  cuando="2026-08-25")
        self.assertEqual(0, core.de_un_proyecto(self.raiz, "2026-09-01")["cuantos"])

    def test_los_dias_se_pueden_cambiar_al_pedirlo(self):
        self.fase("EP-001-una", "HU-001-una", "A-EP-001-HU-001-reciente",
                  cuando="2026-08-25")
        salida = core.de_un_proyecto(self.raiz, "2026-09-01", dias=3)
        self.assertEqual(1, salida["cuantos"])

    def test_una_fase_terminada_no_avisa_por_mas_vieja_que_sea(self):
        cerrada = (FASE % {"cuando": "2020-01-01", "ocho": u"☑"}).replace(
            u"| ☐ |", u"| ☑ |")
        self.escribir("documentacion/epicas/EP-001-una/HU-001-una/"
                      "A-EP-001-HU-001-cerrada/estado-fase.md", cerrada)
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        detenidas = [uno for uno in salida["avisos"]
                     if uno["clase"] == core.DETENIDA]
        self.assertEqual([], detenidas)

    def test_cuando_recorta_lo_dice(self):
        for numero in range(1, 6):
            self.historia_sola("EP-001-una", "HU-%03d-sola" % numero)
        salida = core.de_un_proyecto(self.raiz, "2026-09-01", tope=2)
        self.assertEqual(5, salida["cuantos"])
        self.assertEqual(2, len(salida["avisos"]))
        self.assertTrue(salida["se_recorto"])

    def test_una_fase_que_no_dice_desde_cuando_no_se_da_por_vencida(self):
        self.escribir(
            "documentacion/epicas/EP-001-una/HU-001-una/A-x/estado-fase.md",
            FASE.replace(u"| **Última actualización** | %(cuando)s |",
                         u"| **Última actualización** | |")
            % {"cuando": "", "ocho": u"☐"})
        salida = core.de_un_proyecto(self.raiz, "2026-09-01")
        detenidas = [uno for uno in salida["avisos"]
                     if uno["clase"] == core.DETENIDA]
        self.assertEqual([], detenidas)


class CP004ElReporteDiceQueMide(Base):
    """`CA-1` y `CA-2` de `F-030`."""

    def test_el_avance_es_fases_cerradas_sobre_el_total(self):
        self.fase("EP-001-una", "HU-001-una", "A-uno", cuando="2026-09-01",
                  ocho=u"☑")
        self.fase("EP-001-una", "HU-001-una", "B-dos", cuando="2026-09-01")
        fila = reporte.de_un_proyecto("de-prueba", self.raiz, "2026-09-01")
        self.assertEqual(2, fila["fases"])
        self.assertEqual(0.0, fila["avance"])

    def test_el_reporte_lleva_encima_que_mide_cada_columna(self):
        fila = reporte.de_un_proyecto("de-prueba", self.raiz, "2026-09-01")
        escrito = reporte.dicho([fila])
        for nombre, _definicion in reporte.QUE_MIDE:
            self.assertIn(nombre, escrito)
        self.assertIn("nunca le puso fecha a una deuda", escrito)

    def test_la_deuda_y_la_vencida_salen_separadas(self):
        self.fase("EP-001-una", "HU-001-una", "A-quieta", cuando="2026-01-01")
        self.historia_sola("EP-001-una", "HU-002-sola")
        fila = reporte.de_un_proyecto("de-prueba", self.raiz, "2026-09-01")
        self.assertEqual(2, fila["deuda"])
        self.assertEqual(1, fila["vencida"])


class CP005SinDatosNoEsCero(Base):
    """`CA-3` de `F-030`: el caso que más protege."""

    def test_un_proyecto_sin_fases_no_dice_cero_por_ciento(self):
        fila = reporte.de_un_proyecto("vacio", self.raiz, "2026-09-01")
        self.assertIsNone(fila["avance"])
        self.assertEqual(reporte.SIN_DATOS,
                         reporte.como_se_escribe(fila["avance"]))

    def test_el_reporte_lo_nombra_aparte(self):
        fila = reporte.de_un_proyecto("vacio", self.raiz, "2026-09-01")
        escrito = reporte.dicho([fila])
        self.assertIn("no es cero", escrito)
        self.assertIn("vacio", escrito)

    def test_los_sin_datos_van_al_final_no_primeros(self):
        Proyecto.objects.create(identificador="vacio", nombre="Vacío",
                                ruta_codigo=self.raiz,
                                ruta_normalizada=self.raiz.lower(),
                                conectado="conectado")
        otro = tempfile.mkdtemp(prefix="prueba-avisos-otro-")
        try:
            carpeta = os.path.join(otro, "documentacion", "epicas",
                                   "EP-001-una", "HU-001-una", "A-uno")
            os.makedirs(carpeta)
            with io.open(os.path.join(carpeta, "estado-fase.md"), "w",
                         encoding="utf-8", newline="") as abierto:
                abierto.write(FASE % {"cuando": "2026-09-01", "ocho": u"☑"})
            Proyecto.objects.create(identificador="con-datos", nombre="Con",
                                    ruta_codigo=otro,
                                    ruta_normalizada=otro.lower(),
                                    conectado="conectado")
            filas = reporte.de_todos("2026-09-01")
            self.assertEqual("vacio", filas[-1]["proyecto"])
        finally:
            shutil.rmtree(otro, ignore_errors=True)

    def test_sin_ningun_proyecto_conectado_se_dice_y_no_se_deja_en_blanco(self):
        self.assertIn("todavía no se ha conectado", reporte.dicho([]))
