# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `V-EP-008-HU-005` — `F-004`.

**El caso que decide es el CP-002:** que una regla obligatoria no se pueda
apagar. Sin eso, «configurable» quiere decir «el estándar rige cuando conviene»,
que es no tener estándar.

**Y el que salió de correrlo contra el estándar real es el CP-004:** buscar
`*opt-in*` en todo el archivo marcaba **52** reglas como opcionales, y entre
ellas `02·F0`, que es la cadena entera del flujo de trabajo. La marca tiene que
estar en la línea de la regla, no en cualquier parte del archivo que la contiene.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from . import configuracion

CAPITULO_OBLIGATORIO = u"""# 02 · Flujo de trabajo  ·  `[CAPA 2]`

Una línea cualquiera que menciona *opt-in* al pasar, hablando de otra cosa.

## F0 · Ningún eslabón se salta

Lo que exige.

## F5 · Corre solo las suites que la fase toca

Lo que exige.
"""

CAPITULO_OPCIONAL = u"""# 15 · Registros inmutables (patrón opt-in)  ·  `[CAPA 2 · opt-in]`

Lo que trae el capítulo.

## RI1 · Nada se borra

Lo que exige.

## RI2 · Lo que deja de valer se marca

Lo que exige.
"""

REGLA_SUELTA = u"""# 13 · Documentación  ·  `[CAPA 2]`

## DOC5 · Registra como señal lo que no se recupera del código — *opt-in*

Lo que exige.

## DOC1 · Persiste el trabajo de cada unidad completada

Lo que exige.
"""


class Base(TestCase):

    def setUp(self):
        self.estandar = tempfile.mkdtemp(prefix="prueba-config-estandar-")
        self.proyecto = tempfile.mkdtemp(prefix="prueba-config-proy-")
        base = os.path.join(self.estandar, "base")
        os.makedirs(base)
        for nombre, texto in (("02-flujo.md", CAPITULO_OBLIGATORIO),
                              ("15-registros.md", CAPITULO_OPCIONAL),
                              ("13-documentacion.md", REGLA_SUELTA)):
            with io.open(os.path.join(base, nombre), "w", encoding="utf-8",
                         newline="") as abierto:
                abierto.write(texto)

    def tearDown(self):
        for carpeta in (self.estandar, self.proyecto):
            shutil.rmtree(carpeta, ignore_errors=True)


class CP001LoOpcionalSePrendeYSeApaga(Base):
    """`CA-1`: una regla opcional se activa y desactiva por proyecto."""

    def test_de_fabrica_lo_opcional_viene_apagado(self):
        rige, porque = configuracion.rige(self.proyecto, "DOC5", self.estandar)
        self.assertFalse(rige)
        self.assertIn("no la encendió", porque)

    def test_encender_y_apagar_queda_escrito_con_fecha_y_quien(self):
        configuracion.poner(self.proyecto, "DOC5", configuracion.ENCENDIDA,
                            self.estandar, "2026-09-01", "Ing. José")
        rige, porque = configuracion.rige(self.proyecto, "DOC5", self.estandar)
        self.assertTrue(rige)
        self.assertIn("2026-09-01", porque)
        self.assertIn("Ing. José", porque)

        configuracion.poner(self.proyecto, "DOC5", configuracion.APAGADA,
                            self.estandar, "2026-09-02", "Ing. José")
        rige, porque = configuracion.rige(self.proyecto, "DOC5", self.estandar)
        self.assertFalse(rige)
        self.assertIn("2026-09-02", porque)

    def test_cambiar_de_estado_no_deja_dos_filas_de_la_misma_regla(self):
        for cuando in ("2026-09-01", "2026-09-02", "2026-09-03"):
            configuracion.poner(self.proyecto, "DOC5", configuracion.ENCENDIDA,
                                self.estandar, cuando)
        puesto = configuracion.de_un_proyecto(self.proyecto)
        self.assertEqual("2026-09-03", puesto["DOC5"]["desde"])
        with io.open(os.path.join(self.proyecto, configuracion.CARPETA,
                                  configuracion.ARCHIVO),
                     encoding="utf-8") as abierto:
            self.assertEqual(1, abierto.read().count("| `DOC5` |"))

    def test_un_estado_que_no_existe_se_rechaza(self):
        with self.assertRaises(configuracion.NoSePuedeApagar):
            configuracion.poner(self.proyecto, "DOC5", "a medias",
                                self.estandar, "2026-09-01")


class CP002LoObligatorioNoSeApaga(Base):
    """`CA-2`: una obligatoria no se puede desactivar, y se dice por qué."""

    def test_apagar_una_obligatoria_no_se_hace(self):
        with self.assertRaises(configuracion.NoSePuedeApagar) as fallo:
            configuracion.poner(self.proyecto, "F0", configuracion.APAGADA,
                                self.estandar, "2026-09-01")
        self.assertIn("no es opcional", str(fallo.exception))
        self.assertIn("sugerencia", str(fallo.exception))

    def test_encenderla_tampoco_tiene_sentido_y_se_rechaza_igual(self):
        with self.assertRaises(configuracion.NoSePuedeApagar):
            configuracion.poner(self.proyecto, "F0", configuracion.ENCENDIDA,
                                self.estandar, "2026-09-01")

    def test_una_obligatoria_rige_siempre_aunque_no_se_configure(self):
        rige, porque = configuracion.rige(self.proyecto, "F0", self.estandar)
        self.assertTrue(rige)
        self.assertIn("obligatoria", porque)

    def test_una_regla_que_no_existe_se_trata_como_obligatoria(self):
        """Ante la duda, no se puede apagar: es la respuesta segura."""
        rige, _porque = configuracion.rige(self.proyecto, "XX99", self.estandar)
        self.assertTrue(rige)


class CP003CadaProyectoRecibeLoSuyo(Base):
    """`CA-3`: el agente recibe lo configurado allá, no lo de otro proyecto."""

    def test_lo_de_un_proyecto_no_llega_al_otro(self):
        otro = tempfile.mkdtemp(prefix="prueba-config-otro-")
        try:
            configuracion.poner(self.proyecto, "DOC5",
                                configuracion.ENCENDIDA, self.estandar,
                                "2026-09-01")
            mio = configuracion.para_el_agente(self.proyecto, self.estandar)
            ajeno = configuracion.para_el_agente(otro, self.estandar)
            self.assertIn("DOC5", mio["encendidas"])
            self.assertEqual([], ajeno["encendidas"])
            self.assertIn("DOC5", ajeno["apagadas"])
        finally:
            shutil.rmtree(otro, ignore_errors=True)

    def test_un_proyecto_sin_configurar_se_dice_asi_y_no_en_cero(self):
        entregado = configuracion.para_el_agente(self.proyecto, self.estandar)
        self.assertFalse(entregado["configuro"])
        self.assertIn("no configuró nada", configuracion.dicho(entregado))
        self.assertEqual(3, entregado["cuantas_opcionales"])


class CP004LaMarcaVaEnLaLineaDeLaRegla(Base):
    """Lo que salió al correrlo contra el estándar real."""

    def test_la_palabra_suelta_en_el_archivo_no_vuelve_opcional_al_capitulo(self):
        sueltas = configuracion.opcionales(self.estandar)
        self.assertNotIn("F0", sueltas)
        self.assertNotIn("F5", sueltas)

    def test_la_cabecera_del_capitulo_rige_a_todas_sus_reglas(self):
        sueltas = configuracion.opcionales(self.estandar)
        self.assertIn("RI1", sueltas)
        self.assertIn("RI2", sueltas)

    def test_la_marca_en_la_linea_de_la_regla_vale_solo_para_esa(self):
        sueltas = configuracion.opcionales(self.estandar)
        self.assertIn("DOC5", sueltas)
        self.assertNotIn("DOC1", sueltas)

    def test_son_tres_y_no_mas(self):
        self.assertEqual({"RI1", "RI2", "DOC5"},
                         configuracion.opcionales(self.estandar))
