# -*- coding: utf-8 -*-
"""`84` · La clave que teclea una persona, no la que escribe un programa.

`enmascarar.py` reusaba el patrón con que `secretos.py` busca claves **en
código fuente**, donde el valor va entre comillas. En un chat nadie las
escribe, así que `API_KEY=secreto` pasaba en claro a la transcripción, **que se
versiona**. Es núcleo blindado: `00·N6` dice que una credencial no se escribe,
no se registra y no se guarda.

**La mitad de estas pruebas son de lo que NO hay que tapar**, y acá esa mitad
decide si esto sirve: un enmascarador que tapa de más convierte la
transcripción en un texto lleno de huecos, y entonces deja de servir para lo
único que tiene que servir.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import enmascarar                  # noqa: E402


class LaClaveSinComillas(unittest.TestCase):

    def tapa(self, texto):
        salida, cuantas = enmascarar.enmascarar(texto)
        return cuantas, salida

    # ── lo que sí hay que tapar ──────────────────────────────────────────

    def test_la_asignacion_sin_comillas_se_tapa(self):
        n, t = self.tapa(u"API_KEY=supersecreto123456")
        self.assertEqual(1, n)
        self.assertIn(enmascarar.MARCA, t)
        self.assertIn(u"API_KEY", t, "se tapa el valor, no la variable")

    def test_los_dos_puntos_tambien(self):
        n, t = self.tapa(u"password: MiClave123456")
        self.assertEqual(1, n)
        self.assertNotIn(u"MiClave123456", t)

    def test_la_palabra_en_espanol_tambien(self):
        """`clave` y `contraseña` son las que se dicen hablando."""
        n, t = self.tapa(u"la contraseña: Patito2026")
        self.assertEqual(1, n)
        self.assertNotIn(u"Patito2026", t)

    def test_un_valor_largo_sin_numeros_tambien(self):
        n, _ = self.tapa(u"secret=abcdefghijklmnop")
        self.assertEqual(1, n)

    # ── lo que NO hay que tapar ──────────────────────────────────────────

    def test_el_codigo_pegado_en_el_chat_no_se_tapa(self):
        """`clave = h.regla` es código, no una credencial.

        Es el único falso positivo que quedaba al medir el patrón contra este
        repositorio, y es el que obligó a pedir un número o una longitud.
        """
        n, t = self.tapa(u"clave = h.regla or algo")
        self.assertEqual(0, n)
        self.assertIn(u"h.regla", t)

    def test_un_valor_corto_y_sin_numeros_no_se_tapa(self):
        n, _ = self.tapa(u"token: xyz")
        self.assertEqual(0, n)

    def test_lo_que_lee_del_entorno_no_se_tapa(self):
        """No hay secreto que tapar: la línea dice de dónde sale."""
        n, t = self.tapa(u"API_KEY=os.environ['MI_CLAVE_LARGA']")
        self.assertEqual(0, n)

    def test_el_molde_no_se_tapa(self):
        n, t = self.tapa(u"password: changeme")
        self.assertEqual(0, n, "tapar un molde empeora el texto sin proteger nada")

    def test_una_frase_normal_no_se_toca(self):
        texto = u"La clave del asunto es que el proceso sirva antes de automatizarlo."
        n, t = self.tapa(texto)
        self.assertEqual(0, n)
        self.assertEqual(texto, t)

    # ── que lo de antes siga funcionando ─────────────────────────────────

    def test_las_formas_de_proveedor_siguen_tapandose(self):
        for clave in (u"AKIA1234567890ABCDEF",
                      u"ghp_abcdefghijklmnopqrstuvwxyz12"):
            n, t = self.tapa(u"la clave es %s, guardala" % clave)
            self.assertEqual(1, n, clave)
            self.assertNotIn(clave, t)

    def test_la_asignacion_con_comillas_sigue_tapandose(self):
        n, t = self.tapa(u'API_KEY="supersecreto123456"')
        self.assertEqual(1, n)
        self.assertNotIn(u"supersecreto123456", t)

    def test_el_texto_no_cambia_de_forma(self):
        """Un enmascarado que reescribe de más deja de ser transcripción."""
        texto = u"primera línea\nAPI_KEY=supersecreto123456\ntercera línea\n"
        _, t = self.tapa(texto)
        self.assertEqual(3, len(t.splitlines()))
        self.assertTrue(t.startswith(u"primera línea\n"))
        self.assertTrue(t.endswith(u"tercera línea\n"))


if __name__ == "__main__":
    unittest.main()
