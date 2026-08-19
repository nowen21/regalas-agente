# -*- coding: utf-8 -*-
"""`EP-007 · HU-006 · CA-02` — el registro no gana una entrada vacía.

**El caso está medido.** El 2026-08-18 se puso al día `shopnest-mesa` del
`23.5.0` al `23.10.0`. La instalación escribió su registro y, en la misma
corrida, dijo que faltaba registrarla. Al correrla otra vez —como el propio
mensaje pedía— escribió un segundo registro, siete segundos después, que dice
*«ninguno cambió de huella»*.

**La causa era el orden.** `registros()` ordenaba por `(fecha, sufijo)` y
dejaba la versión fuera del criterio. Los dos registros eran del mismo día, así
que empataban, y el desempate caía en el orden alfabético del nombre — donde
`23.10.0` va **antes** que `23.5.0`, porque el `1` va antes que el `5`.

De ahí salían los dos síntomas a la vez: el checklist leía la versión vieja
como "última" y decía que faltaba; y el instalador, leyendo lo mismo, creía
que la versión había subido y escribía un registro más en cada corrida.

**Por eso los casos usan la misma fecha.** Con fechas distintas el defecto no
aparece, y así fue como pasó las pruebas la primera vez.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import versiones      # noqa: E402


class Base(unittest.TestCase):

    def proyecto(self, *nombres):
        """Un proyecto de mentira con esos registros. Nunca uno real (`00·N4`)."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, *versiones.CARPETA.split(os.sep))
        os.makedirs(carpeta)
        for n in nombres:
            with io.open(os.path.join(carpeta, n), "w", encoding="utf-8") as f:
                f.write(u"# registro\n")
        return tmp.name


class ElOrdenMiraLaVersion(Base):

    def test_el_caso_que_lo_destapo(self):
        """`23.5.0` y `23.10.0` el mismo día: la última es la `23.10.0`."""
        r = self.proyecto("2026-08-18-23.5.0.md", "2026-08-18-23.10.0.md")
        self.assertEqual("23.10.0", versiones.version_registrada(r))

    def test_no_es_el_orden_del_nombre(self):
        """Alfabéticamente `23.10.0` va primero. Numéricamente va última."""
        r = self.proyecto("2026-08-18-23.10.0.md", "2026-08-18-23.5.0.md")
        self.assertEqual("23.10.0", versiones.version_registrada(r))

    def test_dos_digitos_contra_uno_en_el_medio(self):
        r = self.proyecto("2026-08-18-1.2.0.md", "2026-08-18-1.10.0.md")
        self.assertEqual("1.10.0", versiones.version_registrada(r))

    def test_dos_digitos_contra_uno_al_final(self):
        r = self.proyecto("2026-08-18-1.0.9.md", "2026-08-18-1.0.11.md")
        self.assertEqual("1.0.11", versiones.version_registrada(r))

    def test_la_fecha_sigue_mandando_sobre_la_version(self):
        """**Es a propósito.** El registro dice desde cuándo, no cuál es mayor:
        si un proyecto volvió atrás, lo último que hizo es lo que vale."""
        r = self.proyecto("2026-08-18-23.10.0.md", "2026-08-19-23.5.0.md")
        self.assertEqual("23.5.0", versiones.version_registrada(r))

    def test_a_igual_fecha_y_version_manda_el_sufijo(self):
        r = self.proyecto("2026-08-18-9.0.0.md", "2026-08-18-9.0.0-2.md")
        self.assertEqual("2026-08-18-9.0.0-2.md", versiones.registros(r)[-1][0])

    def test_una_version_que_no_es_solo_numeros_no_revienta(self):
        r = self.proyecto("2026-08-18-23.10.0.md", "2026-08-18-23.10.0-beta.md")
        self.assertEqual(2, len(versiones.registros(r)))

    def test_el_orden_completo_de_una_historia_larga(self):
        r = self.proyecto("2026-08-10-9.2.0.md", "2026-08-18-23.5.0.md",
                          "2026-08-18-23.10.0.md", "2026-08-18-23.9.0.md")
        self.assertEqual(["9.2.0", "23.5.0", "23.9.0", "23.10.0"],
                         [v for _, _, v in versiones.registros(r)])


class ElChecklistNoPideLoQueYaEsta(Base):

    def test_lo_registrado_el_mismo_dia_cuenta_como_registrado(self):
        """El síntoma que veía el usuario: escribirlo y decir que falta."""
        r = self.proyecto("2026-08-18-23.5.0.md", "2026-08-18-23.10.0.md")
        self.assertEqual("23.10.0", versiones.version_registrada(r))

    def test_sin_carpeta_de_registros_no_revienta(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], versiones.registros(tmp.name))
        self.assertEqual("", versiones.version_registrada(tmp.name))

    def test_carpeta_vacia_no_revienta(self):
        self.assertEqual("", versiones.version_registrada(self.proyecto()))

    def test_lo_que_no_es_un_registro_se_ignora(self):
        r = self.proyecto("2026-08-18-23.10.0.md", "README.md", "notas.txt")
        self.assertEqual(1, len(versiones.registros(r)))


class ElOrdenDeVersion(unittest.TestCase):
    """La pieza suelta, para que el porqué quede fijado y no solo el efecto."""

    def test_el_diez_va_despues_del_cinco(self):
        self.assertLess(versiones._orden_de_version("23.5.0"),
                        versiones._orden_de_version("23.10.0"))

    def test_el_texto_dice_lo_contrario(self):
        """La comparación que estaba puesta, para que se vea qué se arregló."""
        self.assertLess("23.10.0", "23.5.0")

    def test_lo_que_no_es_numero_va_al_final(self):
        self.assertLess(versiones._orden_de_version("1.0.0"),
                        versiones._orden_de_version("1.0.0rc"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
