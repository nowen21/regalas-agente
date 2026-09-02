# -*- coding: utf-8 -*-
"""Los casos de las cinco pantallas nuevas — fase `Z-EP-021-HU-001`.

**El caso que decide es el CP-002:** que una pantalla vacía diga que está vacía.
Una pantalla en blanco se lee como un error de la plataforma, y casi nunca lo es.

**Y el que más protege es el CP-003:** que ninguna pantalla convierta un «no se
sabe» en un cero. Cero por ciento dice «va mal»; sin datos dice otra cosa.
"""
import io
import os
import shutil
import tempfile

from django.test import Client, TestCase

from nucleo.aprobaciones.models import Aprobacion
from nucleo.proyectos.models import Proyecto

FASE = u"""# Estado de fase

| Campo | Valor |
|---|---|
| **Última actualización** | 2026-01-01 |

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
| 8 | Implementador | pruebas verdes | ☐ |
| 9 | Verificador | trazabilidad | ☐ |
| 10 | Crítico | hallazgos | ☐ |
| 11 | Cierre | docs | ☐ |
| 12 | Commit | autorizado | ☐ |
| 13 | Publicación | autorizado | N/A |
"""

INVENTARIO = u"""# Inventario

### Una
| Campo | Valor |
|---|---|
| **Identificador** | `F-001` |
"""


class Base(TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="prueba-pantallas-")
        self.proyecto = Proyecto.objects.create(
            identificador="de-prueba", nombre="De prueba",
            ruta_codigo=self.raiz, ruta_normalizada=self.raiz.lower(),
            conectado="conectado")
        self.cliente = Client()

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def escribir(self, relativa, texto):
        completa = os.path.join(self.raiz, *relativa.split("/"))
        carpeta = os.path.dirname(completa)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        with io.open(completa, "w", encoding="utf-8", newline="") as abierto:
            abierto.write(texto)


class CP001LasCincoPantallasResponden(Base):
    """Que existan, que devuelvan 200 y que se pueda llegar a ellas."""

    def test_las_cinco_responden(self):
        for ruta in ("/tablero/",
                     "/proyecto/de-prueba/fases/",
                     "/proyecto/de-prueba/funcionalidades/",
                     "/proyecto/de-prueba/aprobaciones/",
                     "/proyecto/de-prueba/memoria/"):
            respuesta = self.cliente.get(ruta)
            self.assertEqual(200, respuesta.status_code, ruta)

    def test_a_las_cuatro_de_un_proyecto_se_llega_desde_su_ficha(self):
        cuerpo = self.cliente.get("/proyecto/de-prueba/").content.decode("utf-8")
        for ruta in ("/proyecto/de-prueba/fases/",
                     "/proyecto/de-prueba/funcionalidades/",
                     "/proyecto/de-prueba/aprobaciones/",
                     "/proyecto/de-prueba/memoria/"):
            self.assertIn(ruta, cuerpo)

    def test_al_tablero_se_llega_desde_cualquier_pantalla(self):
        cuerpo = self.cliente.get("/").content.decode("utf-8")
        self.assertIn("/tablero/", cuerpo)

    def test_un_proyecto_que_no_existe_da_404_y_no_revienta(self):
        for cual in ("fases", "funcionalidades", "aprobaciones", "memoria"):
            respuesta = self.cliente.get("/proyecto/ninguno/%s/" % cual)
            self.assertEqual(404, respuesta.status_code, cual)


class CP002LoVacioSeDice(Base):
    """**El caso que decide.** Una pantalla en blanco se lee como una falla."""

    def test_sin_fases_se_dice_que_no_hay(self):
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/fases/").content.decode("utf-8")
        self.assertIn("no tiene ninguna fase", cuerpo)
        self.assertIn("No es un error", cuerpo)

    def test_sin_aprobaciones_se_dice_que_no_hay_ninguna_registrada(self):
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/aprobaciones/").content.decode("utf-8")
        self.assertIn("registrado ninguna", cuerpo)
        self.assertIn("No es que estén todos sin aprobar", cuerpo)

    def test_sin_memoria_se_dice_lo_que_pasa_y_no_se_revienta(self):
        respuesta = self.cliente.get("/proyecto/de-prueba/memoria/")
        self.assertEqual(200, respuesta.status_code)
        self.assertIn("memoria", respuesta.content.decode("utf-8").lower())

    def test_sin_inventario_se_dice_que_no_hay_que_contar(self):
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/funcionalidades/").content.decode("utf-8")
        self.assertIn("no hay qué contar", cuerpo)


class CP003NingunaPantallaConvierteUnNoSeSabeEnCero(Base):
    """`CA-3` de `F-030`, llevado a la pantalla."""

    def test_el_tablero_escribe_sin_datos_y_no_cero(self):
        cuerpo = self.cliente.get("/tablero/").content.decode("utf-8")
        self.assertIn("sin datos", cuerpo)
        self.assertIn("Sin datos no es cero", cuerpo)

    def test_una_fase_sin_fecha_dice_que_no_lo_dice(self):
        sin_fecha = FASE.replace(
            u"| **Última actualización** | 2026-01-01 |",
            u"| **Última actualización** | |")
        self.escribir("documentacion/epicas/EP-001-x/HU-001-y/A-x/estado-fase.md",
                      sin_fecha)
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/fases/").content.decode("utf-8")
        self.assertIn("no lo dice", cuerpo)

    def test_la_pantalla_de_funcionalidades_separa_los_tres_estados(self):
        self.escribir("cvds/analisis-requisitos/inventario-funcionalidades.md",
                      INVENTARIO)
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/funcionalidades/").content.decode("utf-8")
        self.assertIn("Sin verificar no es lo mismo que no cumple", cuerpo)


class CP004CadaPantallaDiceQueNoMuestra(Base):
    """Lo que una pantalla calla se lee como que no existe."""

    def test_las_fases_de_otro_modelo_se_avisan(self):
        de_once = u"""# Estado

**Estación actual:** 12 · Commit.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Una | x | ☑ |
| 2 | Otra | x | ☐ |
"""
        self.escribir("documentacion/epicas/EP-001-x/HU-001-y/A-x/estado-fase.md",
                      de_once)
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/fases/").content.decode("utf-8")
        self.assertIn("no se compara", cuerpo)

    def test_las_aprobaciones_dicen_que_no_son_todos_los_documentos(self):
        self.escribir("documentacion/x.md", u"# Uno\n")
        Aprobacion.objects.create(
            proyecto="de-prueba", documento="documentacion/x.md",
            quien="Ing. José", cuando="2026-09-01", huella="x", tamano=7)
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/aprobaciones/").content.decode("utf-8")
        self.assertIn("No son todos los del proyecto", cuerpo)

    def test_el_tablero_dice_que_vencida_es_un_numero_puesto_aca(self):
        cuerpo = self.cliente.get("/tablero/").content.decode("utf-8")
        self.assertIn("nunca le puso fecha a una deuda", cuerpo)

    def test_la_memoria_dice_que_lo_de_baja_no_se_borra(self):
        carpeta = os.path.join(self.raiz, "historico-chat", "memory")
        os.makedirs(carpeta)
        with io.open(os.path.join(carpeta, "uno.md"), "w",
                     encoding="utf-8", newline="") as abierto:
            abierto.write(u"# Un recuerdo\n\nLo que sea.\n")
        cuerpo = self.cliente.get(
            "/proyecto/de-prueba/memoria/").content.decode("utf-8")
        self.assertIn("no se borra", cuerpo)
        self.assertIn("Un recuerdo", cuerpo)
