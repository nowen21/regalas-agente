# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `G-EP-016-HU-001`.

**El caso que decide es el CP-004:** que ningún identificador se reutilice, ni
el de una regla derogada. Reutilizar uno hace que toda cita escrita antes apunte
a otra cosa, **y no se ve leyendo**: la cita sigue viéndose bien.

Lo de escribir y derogar está en `tests_redaccion.py`, que es la otra fase.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from . import catalogo, numeracion

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


class CP001SeLeenLasReglas(Base):

    def test_se_leen_las_dos(self):
        self.assertEqual(len(catalogo.todas(self.raiz)), 2)

    def test_la_derogada_no_esta_entre_las_vigentes(self):
        vigentes = [una.id for una in catalogo.vigentes(self.raiz)]
        self.assertEqual(vigentes, ["M1"])

    def test_pero_si_esta_entre_todas(self):
        """Su identificador sigue ocupado, y por eso tiene que salir."""
        self.assertIn("M2", [una.id for una in catalogo.todas(self.raiz)])

    def test_el_resumen_cuenta_las_dos_clases(self):
        cuenta = catalogo.resumen(self.raiz)
        self.assertEqual(cuenta["todas"], 2)
        self.assertEqual(cuenta["vigentes"], 1)
        self.assertEqual(cuenta["derogadas"], 1)

    def test_sin_validadores_lo_dice_en_vez_de_devolver_vacio(self):
        with override_settings(CARPETA_VALIDADORES="/no/existe/en/ningun/lado"):
            with self.assertRaises(catalogo.NoHayCuerpoDeReglas):
                catalogo.todas(self.raiz)


class CP002ElSiguienteIdentificador(Base):

    def test_toma_el_que_sigue_al_mayor(self):
        self.assertEqual(numeracion.siguiente_libre(self.raiz, "M"), "M3")

    def test_un_prefijo_sin_reglas_empieza_en_uno(self):
        self.assertEqual(numeracion.siguiente_libre(self.raiz, "ZZ"), "ZZ1")

    def test_los_usados_incluyen_el_de_la_derogada(self):
        self.assertEqual(numeracion.usados(self.raiz, "M"), [1, 2])


class CP003NoSeGuardaConUnIdentificadorUsado(Base):

    def test_un_identificador_vigente_esta_usado(self):
        self.assertTrue(numeracion.esta_usado(self.raiz, "M1"))

    def test_uno_que_no_existe_no_lo_esta(self):
        self.assertFalse(numeracion.esta_usado(self.raiz, "M9"))

    def test_comprobar_libre_revienta_con_uno_usado(self):
        with self.assertRaises(numeracion.IdentificadorYaUsado):
            numeracion.comprobar_libre(self.raiz, "M1")

    def test_y_deja_pasar_uno_libre(self):
        numeracion.comprobar_libre(self.raiz, "M9")


class CP004ElDeUnaDerogadaNoSeReasigna(Base):
    """**El caso que decide.** Una cita vieja apuntaría a otra cosa."""

    def test_el_identificador_de_una_derogada_sigue_usado(self):
        self.assertTrue(numeracion.esta_usado(self.raiz, "M2"))

    def test_y_no_se_puede_volver_a_usar(self):
        with self.assertRaises(numeracion.IdentificadorYaUsado):
            numeracion.comprobar_libre(self.raiz, "M2")

    def test_el_siguiente_no_rellena_el_hueco_de_una_derogada(self):
        """Rellenar huecos es la única forma de reutilizar sin darse cuenta."""
        self.escribir("base/20-meta-reglas/reglas/M5-otra.md",
                      UNA_REGLA.replace("M1 ·", "M5 ·"))
        self.assertEqual(numeracion.siguiente_libre(self.raiz, "M"), "M6")
        self.assertEqual(numeracion.huecos(self.raiz, "M"), [3, 4])
