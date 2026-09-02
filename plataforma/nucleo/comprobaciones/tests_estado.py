# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `E-EP-015-HU-002`.

**El caso que decide es el CP-002:** que sin prueba quede «sin verificar» y no
se pueda cerrar. Es lo que impide que el estado lo ponga quien escribe.

**Y el que más protege es el CP-004:** que las dos formas de escribir un
veredicto se lean las dos. El molde cambió entre la versión 1 y hoy, y una fase
cerrada no se reescribe.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from . import estado

INVENTARIO = u"""# Inventario

## Las funcionalidades, una por una

### Una
| Campo | Valor |
|---|---|
| **Identificador** | `F-001` |

### Otra
| Campo | Valor |
|---|---|
| **Identificador** | `F-002` |
"""

SPEC = u"""# Especificación

## 13. Trazabilidad

| Funcionalidad | Requisito | Fase que lo construye |
|---|---|---|
| F-001 | RF-01 | `A-EP-001-HU-001-la-primera` |
"""

CONCEPTO = u"""# Estado de fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
"""

VEREDICTO_VIEJO = u"""# Estado de fase

| Campo | Valor |
|---|---|
| **Veredicto de las pruebas** | Cumple. 9 de 9 casos aprobados |
"""

NO_CUMPLE = u"""# Estado de fase

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
"""


class Base(TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="prueba-estado-")
        self.escribir("cvds/analisis-requisitos/inventario-funcionalidades.md",
                      INVENTARIO)

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def escribir(self, relativa, texto):
        completa = os.path.join(self.raiz, relativa.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as archivo:
            archivo.write(texto)

    def fase(self, nombre, texto=CONCEPTO,
             donde="documentacion/epicas/EP-001-x/HU-001-y"):
        self.escribir("%s/%s/estado-fase.md" % (donde, nombre), texto)

    def de(self, funcionalidad):
        for uno in estado.estado_de_todas(self.raiz):
            if uno["funcionalidad"] == funcionalidad:
                return uno
        return None


class CP001ConPruebaQuedaVerificado(Base):

    def test_una_fase_que_cumple_deja_la_funcionalidad_verificada(self):
        self.escribir("documentacion/uno/spec.md", SPEC)
        self.fase("A-EP-001-HU-001-la-primera")
        uno = self.de("F-001")
        self.assertEqual(uno["estado"], estado.VERIFICADO)
        self.assertTrue(estado.se_puede_cerrar(uno))

    def test_el_estado_dice_de_donde_sale(self):
        """No se lee de ninguna parte: se deriva, y se explica."""
        self.escribir("documentacion/uno/spec.md", SPEC)
        self.fase("A-EP-001-HU-001-la-primera")
        self.assertIn("fase", self.de("F-001")["porque"])


class CP002SinPruebaNoSeCierra(Base):
    """**El caso que decide.** El estado no lo pone quien escribe."""

    def test_sin_fase_queda_sin_verificar(self):
        uno = self.de("F-002")
        self.assertEqual(uno["estado"], estado.SIN_VERIFICAR)
        self.assertFalse(estado.se_puede_cerrar(uno))

    def test_con_fase_declarada_pero_sin_veredicto_tampoco_se_cierra(self):
        self.escribir("documentacion/uno/spec.md", SPEC)
        self.fase("A-EP-001-HU-001-la-primera", texto=u"# Sin veredicto\n")
        uno = self.de("F-001")
        self.assertEqual(uno["estado"], estado.SIN_VERIFICAR)
        self.assertFalse(estado.se_puede_cerrar(uno))

    def test_con_una_fase_que_no_existe_tampoco(self):
        self.escribir("documentacion/uno/spec.md", SPEC)
        self.assertEqual(self.de("F-001")["estado"], estado.SIN_VERIFICAR)


class CP003ConPruebaFallidaNoCumple(Base):

    def test_una_fase_que_no_cumple_deja_la_funcionalidad_en_no_cumple(self):
        self.escribir("documentacion/uno/spec.md", SPEC)
        self.fase("A-EP-001-HU-001-la-primera", texto=NO_CUMPLE)
        uno = self.de("F-001")
        self.assertEqual(uno["estado"], estado.NO_CUMPLE)
        self.assertFalse(estado.se_puede_cerrar(uno))

    def test_y_dice_cual_fase_fue(self):
        self.escribir("documentacion/uno/spec.md", SPEC)
        self.fase("A-EP-001-HU-001-la-primera", texto=NO_CUMPLE)
        self.assertIn("A-EP-001-HU-001-la-primera", self.de("F-001")["porque"])

    def test_no_cumple_no_es_lo_mismo_que_sin_verificar(self):
        """Una es que se comprobó y salió mal; la otra, que nadie comprobó."""
        self.assertNotEqual(estado.NO_CUMPLE, estado.SIN_VERIFICAR)


class CP004LasDosFormasDeVeredicto(Base):
    """El molde cambió, y una fase cerrada no se reescribe."""

    def test_la_forma_de_la_version_uno_tambien_se_lee(self):
        self.escribir("documentacion/uno/spec.md", SPEC)
        self.fase("A-EP-001-HU-001-la-primera", texto=VEREDICTO_VIEJO)
        self.assertEqual(self.de("F-001")["estado"], estado.VERIFICADO)


class CP005SobreLoReal(TestCase):
    """La cuenta de este repositorio, que es de donde salió todo esto."""

    def test_el_inventario_de_este_repositorio_tiene_sus_funcionalidades(self):
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))
        cuantas = len(estado.funcionalidades_del_inventario(raiz))
        self.assertGreater(cuantas, 30)

    def test_el_resumen_cuenta_los_tres_estados(self):
        cuenta = estado.resumen([
            {"estado": estado.VERIFICADO}, {"estado": estado.VERIFICADO},
            {"estado": estado.SIN_VERIFICAR}])
        self.assertEqual(cuenta[estado.VERIFICADO], 2)
        self.assertEqual(cuenta[estado.SIN_VERIFICAR], 1)
        self.assertEqual(cuenta[estado.NO_CUMPLE], 0)


class CP007LaFilaSeLeeEnSusFormas(Base):
    """Lo que salió al preguntarle al módulo por las once especificaciones.

    **Cuatro funcionalidades construidas y probadas el mismo día salían como si
    nadie las hubiera construido.** El lector exigía la columna del requisito y
    el identificador sin comillas, y dos de las once especificaciones no lo
    traían así. El módulo lo decía como un hecho del proyecto —«ninguna fase la
    construye»— cuando lo que pasaba era que no supo leer.
    """

    def test_la_fila_sin_la_columna_del_requisito_tambien_se_lee(self):
        self.escribir("documentacion/uno/spec.md", u"""# Especificación

## 13. Trazabilidad

| Funcionalidad | Fase | Estado |
|---|---|---|
| F-001 | `A-EP-001-HU-001-la-primera` | Cerrada |
""")
        self.fase("A-EP-001-HU-001-la-primera")
        self.assertEqual(estado.VERIFICADO, self.de("F-001")["estado"])

    def test_el_identificador_entre_comillas_tambien_se_lee(self):
        self.escribir("documentacion/uno/spec.md", u"""# Especificación

## 13. Trazabilidad

| Funcionalidad | Fase | Estado |
|---|---|---|
| `F-001` | `A-EP-001-HU-001-la-primera` | Cerrada |
""")
        self.fase("A-EP-001-HU-001-la-primera")
        self.assertEqual(estado.VERIFICADO, self.de("F-001")["estado"])

    def test_una_fila_que_no_dice_quien_la_construye_no_cuenta(self):
        """Una fila cualquiera que empiece por un identificador no es traza."""
        self.escribir("documentacion/uno/spec.md", u"""# Especificación

## 12. Decisiones

| Funcionalidad | Por qué |
|---|---|
| F-001 | porque sí |
""")
        self.assertEqual(estado.SIN_VERIFICAR, self.de("F-001")["estado"])

    def test_no_supe_leer_se_dice_distinto_de_no_existe(self):
        """**El defecto que se leía como un hecho del proyecto.**"""
        self.escribir("documentacion/uno/spec.md", u"""# Especificación

## 12. Decisiones

| Funcionalidad | Por qué |
|---|---|
| F-001 | porque sí |
""")
        nombrada = self.de("F-001")
        sin_nombrar = self.de("F-002")
        self.assertEqual(estado.SIN_VERIFICAR, nombrada["estado"])
        self.assertIn("no se pudo leer", nombrada["porque"])
        self.assertIn("ninguna fase la construye", sin_nombrar["porque"])
        self.assertNotEqual(nombrada["porque"], sin_nombrar["porque"])
