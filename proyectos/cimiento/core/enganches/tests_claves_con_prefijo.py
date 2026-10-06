# -*- coding: utf-8 -*-
"""`EP-005·HU-002`, fase C: las claves de Anthropic y las variables con prefijo se tapan.

Las claves se arman al correr, y las pruebas comparan con `assertFalse(... in ...)`
y un mensaje propio: `assertNotIn` repite la clave al fallar, y así terminó una
en el registro de la sesión (señal S-315).
"""
from django.test import SimpleTestCase

from core.enganches.enmascarar import MARCA, Enmascarador
from core.validadores.secretos import SecretosEnElCodigo


def clave_anthropic():
    return "sk-" + "ant-" + "api03-" + "q7Rb2LmX9vTz4KpW8nHc3YdF6gJs"


def valor():
    return "q7Rb2LmX9vTz" + "4KpW8nHc"


class LasFormasNuevasSeTapan(SimpleTestCase):
    """CP-001 y CP-002."""

    def tapa(self, texto):
        return Enmascarador.enmascarar(texto)

    def assertTapada(self, texto, secreto):
        salida, cuantas = self.tapa(texto)
        self.assertEqual(1, cuantas, "no se tapó: %s" % texto[:20])
        self.assertFalse(secreto in salida, "la clave quedó en claro")
        self.assertIn(MARCA, salida)
        return salida

    def test_la_clave_de_anthropic(self):
        self.assertTapada("la clave es " + clave_anthropic() + " y listo", clave_anthropic())

    def test_la_variable_con_prefijo_sin_comillas(self):
        salida = self.assertTapada("ANTHROPIC_API_KEY=" + valor(), valor())
        self.assertIn("ANTHROPIC_API_KEY", salida, "se tapa el valor, no la variable")
        self.assertTapada("OPENAI_API_KEY: " + valor(), valor())

    def test_la_variable_con_prefijo_con_comillas(self):
        for nombre in ("GITHUB_TOKEN", "DB_PASSWORD", "APP_SECRET"):
            with self.subTest(nombre=nombre):
                self.assertTapada('%s="%s"' % (nombre, valor()), valor())


class LoQueNoEsClaveNoSeTapa(SimpleTestCase):
    """CP-003."""

    def test_lo_que_lee_del_entorno_el_molde_y_el_nombre_solo(self):
        for texto in ('ANTHROPIC_API_KEY=os.environ["ANTHROPIC_API_KEY"]', 'MY_API_KEY="your_api_key"',
                      "se llama ANTHROPIC_API_KEY y va en el entorno", "max_tokens=4096"):
            with self.subTest(texto=texto):
                self.assertEqual((texto, 0), Enmascarador.enmascarar(texto))


class ElValidadorLasSenala(SimpleTestCase):
    """CP-004, pasos 1 y 2."""

    def test_la_clave_de_anthropic_en_el_codigo(self):
        hallazgos = SecretosEnElCodigo(".").revisar_texto('CLIENTE = "%s"\n' % clave_anthropic(), "x.py")
        self.assertEqual(1, len(hallazgos))
        self.assertIn("Anthropic", hallazgos[0].mensaje)
        self.assertFalse(clave_anthropic() in hallazgos[0].mensaje, "el hallazgo repite la clave")

    def test_la_variable_con_prefijo_en_el_codigo(self):
        hallazgos = SecretosEnElCodigo(".").revisar_texto('ANTHROPIC_API_KEY = "%s"\n' % valor(), "x.py")
        self.assertEqual(1, len(hallazgos))
