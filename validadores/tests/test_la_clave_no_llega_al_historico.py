# -*- coding: utf-8 -*-
"""`EP-005 · HU-002` · La clave se tapa antes de escribirse en el histórico.

**El daño estaba medido, no supuesto.** La fase `A-EP-005-HU-001` comprobó que
una clave pegada en el chat queda escrita en claro en la transcripción — y la
transcripción se versiona, así que de ahí no se borra.

**Por eso se tapa antes de escribir y no después.** Un enmascarado que corre
sobre el archivo ya escrito llega tarde: el valor estuvo en disco, y si hubo
un guardado en medio, en el historial para siempre.

**Y la mitad del trabajo es no tapar de más.** Un molde (`tu-clave`,
`changeme`) tapado vuelve ilegible un ejemplo, y una línea que lee del entorno
es justamente la forma correcta: taparla enseñaría lo contrario de lo que el
estándar pide.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import enmascarar   # noqa: E402
import historico    # noqa: E402

MARCA = u"«enmascarado»"


class SeTapaLoQueEsUnaClave(unittest.TestCase):

    def test_las_formas_que_delatan_un_proveedor(self):
        """Ocho formas que `secretos.py` ya reconoce. No se duplica la lista."""
        for clave in (u"AKIA1234567890ABCDEF",
                      u"ghp_abcdefghijklmnopqrstuvwxyz012345",
                      u"xoxb-1234567890-abcdefghij",
                      u"sk_live_abcdefghijklmnop1234"):
            with self.subTest(clave=clave[:12]):
                t, n = enmascarar.enmascarar(u"pegá esto: %s y listo" % clave)
                self.assertEqual(1, n)
                self.assertNotIn(clave, t)
                self.assertIn(MARCA, t)

    def test_la_variable_con_pinta_de_clave(self):
        t, n = enmascarar.enmascarar(u'password: "S3creto-de-verdad"')
        self.assertEqual(1, n)
        self.assertNotIn(u"S3creto", t)

    def test_se_tapa_el_valor_y_no_la_variable(self):
        """Quien lea la transcripción tiene que seguir entendiendo de qué se
        hablaba. Tapar la línea entera pierde el hilo de la conversación."""
        t, _ = enmascarar.enmascarar(u'password: "S3creto-de-verdad"')
        self.assertIn(u"password", t)

    def test_varias_lineas(self):
        t, n = enmascarar.enmascarar(u"uno\nAKIA1234567890ABCDEF\ntres")
        self.assertEqual(1, n)
        self.assertIn(u"uno", t)
        self.assertIn(u"tres", t)


class NoSeTapaLoQueNoEsUnaClave(unittest.TestCase):
    """La mitad del trabajo, y la que se borra si nadie la escribe."""

    def test_el_molde_no_se_tapa(self):
        """`tu-clave`, `changeme`, `<...>`: taparlos vuelve ilegible un ejemplo."""
        for molde in (u"tu-clave-aqui", u"changeme", u"your_api_key", u"<TU-CLAVE>"):
            with self.subTest(molde=molde):
                t, n = enmascarar.enmascarar(u'password: "%s"' % molde)
                self.assertEqual(0, n)
                self.assertIn(molde, t)

    def test_leer_del_entorno_no_se_tapa(self):
        """Es la forma correcta. Taparla enseñaría lo contrario de lo que se pide."""
        for linea in (u'password: os.environ["X"]',
                      u'api_key = env("CLAVE")',
                      u'secret: process.env.TOKEN'):
            with self.subTest(linea=linea):
                self.assertEqual(0, enmascarar.enmascarar(linea)[1])

    def test_el_texto_sin_claves_no_se_toca(self):
        original = u"esto es un mensaje normal\ncon dos líneas\n"
        self.assertEqual((original, 0), enmascarar.enmascarar(original))

    def test_no_reescribe_de_mas(self):
        """Un enmascarado que cambia el orden o los saltos deja de ser fiable
        como transcripción, que es lo único que ese archivo tiene que ser."""
        t, _ = enmascarar.enmascarar(u"uno\n\ndos\nAKIA1234567890ABCDEF\n")
        self.assertEqual(4, len(t.splitlines()))
        self.assertTrue(t.endswith(u"\n"))


class NoLlegaAlArchivo(unittest.TestCase):
    """De punta a punta: por el camino real, no llamando al enmascarado."""

    def repo(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, "historico-chat"))
        return tmp.name

    def test_el_mensaje_del_usuario_llega_tapado(self):
        raiz = self.repo()
        ruta = historico.anotar_usuario(
            raiz, "s-1", u"la clave es AKIA1234567890ABCDEF, guardala")
        with io.open(ruta, encoding="utf-8") as f:
            escrito = f.read()
        self.assertNotIn(u"AKIA1234567890ABCDEF", escrito)
        self.assertIn(MARCA, escrito)

    def test_el_resto_del_mensaje_sigue_ahi(self):
        raiz = self.repo()
        ruta = historico.anotar_usuario(
            raiz, "s-1", u"la clave es AKIA1234567890ABCDEF, guardala")
        with io.open(ruta, encoding="utf-8") as f:
            escrito = f.read()
        self.assertIn(u"guardala", escrito)

    def test_se_tapa_antes_de_escribir_no_despues(self):
        """El archivo **nunca** contiene el valor, ni un instante.

        No hay forma de comprobar «ni un instante» leyendo el resultado, así
        que lo que se fija es dónde vive la llamada: dentro de `anotar_usuario`,
        antes del `_anotar`. Si alguien la mueve después, este caso no se cae
        — pero el de arriba sí, y por eso están los dos.
        """
        import inspect
        fuente = inspect.getsource(historico.anotar_usuario)
        self.assertIn("enmascarar.enmascarar(mensaje)", fuente)
        self.assertLess(fuente.index("enmascarar.enmascarar"),
                        fuente.index("_anotar("))


if __name__ == "__main__":
    unittest.main()
