# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `H-EP-016-HU-002`.

**El caso que decide es el CP-006:** que derogar no borre. Lo que se borra no se
puede volver a leer para entender por qué existía, y su identificador quedaría
libre para que otra regla lo tomara.

**Y el que más cuida de un error humano es el CP-007:** las reglas que se
parecen. Con 248 vigentes nadie las tiene todas en la cabeza.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from . import catalogo, numeracion, parecidas, redaccion

CAPITULO = u"""# 20 · Meta-reglas

Las reglas de este capítulo viven en `reglas/`.
"""

UNA_REGLA = u"""> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M1 · Un tema, un capítulo

Cada tema tiene un capítulo dueño.

```
INCORRECTO: el mismo tema en dos capítulos
CORRECTO:   un tema, un capítulo
```
"""

UNA_DEROGADA = u"""> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M2 · Lo que ya no rige  ·  `[DEROGADA en 4.0.0 → ver M1]`

> **Ya no rige.** Lo que exigía lo exige M1.

El texto original se conserva.
"""


class Base(TestCase):
    """Un cuerpo de reglas de mentiras, con una vigente y una derogada."""

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="prueba-reglas-")
        self.escribir("base/20-meta-reglas/base.md", CAPITULO)
        self.escribir("base/20-meta-reglas/reglas/M1-un-tema-un-capitulo.md",
                      UNA_REGLA)
        self.escribir("base/20-meta-reglas/reglas/M2-lo-que-ya-no-rige.md",
                      UNA_DEROGADA)

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def escribir(self, relativa, texto):
        completa = os.path.join(self.raiz, relativa.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as archivo:
            archivo.write(texto)

    def leer(self, ruta):
        with io.open(ruta, encoding="utf-8", newline="") as archivo:
            return archivo.read()


class CP005SeEscribeUnaReglaNueva(Base):

    def test_queda_guardada_con_su_identificador(self):
        identificador, ruta = redaccion.crear(
            self.raiz, "base/20-meta-reglas", "M", u"Una regla nueva",
            u"20 · Meta-reglas")
        self.assertEqual(identificador, "M3")
        self.assertTrue(os.path.isfile(ruta))
        self.assertIn(u"## M3 · Una regla nueva", self.leer(ruta))

    def test_nace_con_sus_huecos_puestos(self):
        """La regla nace incompleta, y se le nota."""
        _, ruta = redaccion.crear(self.raiz, "base/20-meta-reglas", "M",
                                  u"Otra regla", u"20 · Meta-reglas")
        self.assertIn(redaccion.MARCA_DEL_HUECO, self.leer(ruta))

    def test_el_nombre_del_archivo_sale_del_titulo(self):
        self.assertEqual(
            redaccion.nombre_de_archivo("M3", u"Una regla con tildes: acción"),
            "M3-una-regla-con-tildes-accion.md")

    def test_sale_con_el_formato_canonico(self):
        texto = redaccion.molde("M3", u"Un título", u"20 · Meta-reglas")
        self.assertTrue(texto.startswith(u"> Regla del capítulo"))
        self.assertIn(u"INCORRECTO:", texto)
        self.assertIn(u"CORRECTO:", texto)


class CP006DerogarNoBorra(Base):
    """Lo que se borra no se puede volver a leer para entender por qué existía."""

    def test_la_regla_queda_marcada_y_legible(self):
        ruta = redaccion.derogar(self.raiz, "M1", "5.0.0", "M2",
                                 u"Lo que exigía lo exige M2.")
        texto = self.leer(ruta)
        self.assertIn(u"[DEROGADA en 5.0.0 → ver M2]", texto)
        self.assertIn(u"Cada tema tiene un capítulo dueño.", texto)

    def test_y_dice_por_que(self):
        ruta = redaccion.derogar(self.raiz, "M1", "5.0.0", "M2",
                                 u"Lo que exigía lo exige M2.")
        self.assertIn(u"Ya no rige", self.leer(ruta))

    def test_despues_de_derogar_ya_no_esta_vigente(self):
        redaccion.derogar(self.raiz, "M1", "5.0.0", "M2", u"Porque sí.")
        self.assertEqual([una.id for una in catalogo.vigentes(self.raiz)], [])

    def test_pero_su_identificador_sigue_ocupado(self):
        redaccion.derogar(self.raiz, "M1", "5.0.0", "M2", u"Porque sí.")
        self.assertTrue(numeracion.esta_usado(self.raiz, "M1"))

    def test_una_regla_que_no_existe_lo_dice(self):
        with self.assertRaises(redaccion.NoSePuedeTocar):
            redaccion.derogar(self.raiz, "M9", "5.0.0", "M1", u"Porque sí.")

    def test_una_ya_derogada_lo_dice(self):
        with self.assertRaises(redaccion.NoSePuedeTocar):
            redaccion.derogar(self.raiz, "M2", "5.0.0", "M1", u"Porque sí.")


class CP007LasQueSeParecen(Base):

    def test_encuentra_la_que_habla_de_lo_mismo(self):
        encontradas = parecidas.parecidas_a(self.raiz, u"Un tema, un capítulo",
                                            "M")
        self.assertEqual(encontradas[0][0].id, "M1")

    def test_un_titulo_sin_nada_que_ver_no_encuentra_nada(self):
        self.assertEqual(
            parecidas.parecidas_a(self.raiz, u"Cocinar una arepa"), [])

    def test_no_mira_las_derogadas(self):
        """Una derogada ya no rige: no puede contradecir a nadie."""
        encontradas = parecidas.parecidas_a(self.raiz, u"Lo que ya no rige")
        self.assertEqual([una.id for una, _ in encontradas], [])

    def test_el_aviso_dice_lo_que_esto_no_puede_decir(self):
        """Llamarlo detector de contradicciones sería peor que no tenerlo."""
        self.assertIn(u"contradi", parecidas.aviso([]))
        encontradas = parecidas.parecidas_a(self.raiz, u"Un tema, un capítulo")
        self.assertIn(u"contradi", parecidas.aviso(encontradas))
