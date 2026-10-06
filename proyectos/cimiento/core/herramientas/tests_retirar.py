"""Análisis 1 del pendiente 116, acuerdo 15 · Lo que se retira no deja enlaces rotos."""
import io
import os
import tempfile
import unittest

from core.herramientas.retirar import Retiro


class LoRetiradoNoDejaEnlacesRotos(unittest.TestCase):

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.raiz = os.path.realpath(tmp.name)
        self.escribir("docs/ficha.md", "# Ficha\n")
        self.escribir("docs/otra.md", "# Otra\n")

    def escribir(self, relativa, texto):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def leer(self, relativa):
        with io.open(os.path.join(self.raiz, *relativa.split("/")), encoding="utf-8") as f:
            return f.read()

    def retirar(self, aplicar=True):
        return Retiro(self.raiz).retirar([os.path.join(self.raiz, "docs", "ficha.md")], aplicar=aplicar)

    def test_el_enlace_pasa_a_texto_y_el_archivo_se_borra(self):
        self.escribir("fase/plan.md", "Ver [la ficha](../docs/ficha.md) y [la otra](../docs/otra.md).\n")
        cambios, faltan = self.retirar()
        self.assertEqual([], faltan)
        self.assertEqual(1, cambios[0][1])
        self.assertEqual("Ver la ficha y [la otra](../docs/otra.md).\n", self.leer("fase/plan.md"))
        self.assertFalse(os.path.exists(os.path.join(self.raiz, "docs", "ficha.md")))

    def test_sin_aplicar_no_toca_nada(self):
        original = "Ver [la ficha](../docs/ficha.md).\n"
        self.escribir("fase/plan.md", original)
        cambios, _ = self.retirar(aplicar=False)
        self.assertEqual(1, len(cambios))
        self.assertEqual(original, self.leer("fase/plan.md"))
        self.assertTrue(os.path.exists(os.path.join(self.raiz, "docs", "ficha.md")))

    def test_el_codigo_y_los_bloques_no_son_enlaces(self):
        texto = "`[la ficha](../docs/ficha.md)`\n```\n[la ficha](../docs/ficha.md)\n```\n"
        self.escribir("fase/plan.md", texto)
        self.retirar()
        self.assertEqual(texto, self.leer("fase/plan.md"))

    def test_la_conversacion_de_un_analisis_no_se_edita(self):
        texto = ("# Análisis\n\n## Conversación\n\nSe dijo [la ficha](../docs/ficha.md).\n\n"
                 "## Lo acordado\n\nQueda [la ficha](../docs/ficha.md).\n")
        self.escribir("p/analisis-1.md", texto)
        self.retirar()
        nuevo = self.leer("p/analisis-1.md")
        self.assertIn("Se dijo [la ficha](../docs/ficha.md).", nuevo)
        self.assertIn("Queda la ficha.", nuevo)

    def test_la_ruta_que_no_existe_se_dice(self):
        _, faltan = Retiro(self.raiz).retirar([os.path.join(self.raiz, "docs", "no.md")])
        self.assertEqual(1, len(faltan))


if __name__ == "__main__":
    unittest.main()
