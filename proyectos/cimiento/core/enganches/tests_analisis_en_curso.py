"""Pruebas del análisis en curso: un estado por sesión (sesión del 2026-10-04).

Cimiento tiene que poder abrir otro análisis en otra sesión mientras uno se
construye; lo único que no se deja es prender dos veces el mismo pendiente, o
dos análisis sin aprobar en la misma sesión.
"""
import os
import shutil
import tempfile
import unittest

from .analisis_en_curso import ESTADO, ESTADOS, AnalisisEnCurso

APROBADO = "> **Aprobado** por el usuario el 2026-10-04, en el turno 3.\n"


class AnalisisPorSesion(unittest.TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        for numero in (7, 8):
            carpeta = os.path.join(self.raiz, "pendientes", "%d-algo" % numero)
            os.makedirs(carpeta)
            with open(os.path.join(carpeta, "pendiente.md"), "w", encoding="utf-8") as f:
                f.write("# Pendiente %d\n" % numero)
        carpeta = os.path.join(self.raiz, "historico-chat")
        os.makedirs(carpeta)
        self.a = os.path.join(carpeta, "2026-10-04-sesion-a.md")
        self.b = os.path.join(carpeta, "2026-10-04-sesion-b.md")
        for ruta in (self.a, self.b):
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("### 1 · Usuario, 10:00\n\nhola\n")

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def _aprobar(self, curso):
        ruta = curso.leer_estado()["analisis"]
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
        primera, _, resto = texto.partition("\n")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(primera + "\n\n" + APROBADO + resto)

    def test_cada_sesion_guarda_su_estado_aparte(self):
        a, b = AnalisisEnCurso(self.raiz, self.a), AnalisisEnCurso(self.raiz, self.b)
        self.assertTrue(a.prender(7, self.a, 1)[0])
        self.assertTrue(b.prender(8, self.b, 1)[0])
        self.assertIn("7-algo", a.leer_estado()["analisis"])
        self.assertIn("8-algo", b.leer_estado()["analisis"])
        self.assertTrue(os.path.isfile(os.path.join(self.raiz, ESTADOS, "2026-10-04-sesion-a.txt")))

    def test_un_analisis_sin_aprobar_no_bloquea_otra_sesion(self):
        AnalisisEnCurso(self.raiz, self.a).prender(7, self.a, 1)
        self.assertTrue(AnalisisEnCurso(self.raiz, self.b).prender(8, self.b, 1)[0])

    def test_el_mismo_pendiente_no_se_prende_en_dos_sesiones(self):
        AnalisisEnCurso(self.raiz, self.a).prender(7, self.a, 1)
        prendido, porque = AnalisisEnCurso(self.raiz, self.b).prender(7, self.b, 1)
        self.assertFalse(prendido)
        self.assertIn("2026-10-04-sesion-a.md", porque)

    def test_la_misma_sesion_no_prende_dos_sin_aprobar(self):
        a = AnalisisEnCurso(self.raiz, self.a)
        a.prender(7, self.a, 1)
        prendido, porque = a.prender(8, self.a, 2)
        self.assertFalse(prendido)
        self.assertIn("sin aprobar", porque)

    def test_un_analisis_aprobado_con_hu_por_construir_no_bloquea(self):
        a = AnalisisEnCurso(self.raiz, self.a)
        a.prender(7, self.a, 1)
        self._aprobar(a)
        with open(a.leer_estado()["analisis"], "a", encoding="utf-8") as f:
            f.write("\n## Lo que se tiene que hacer\n\n| 2 | algo | 1 | `EP-004` HU-026 |\n")
        self.assertTrue(AnalisisEnCurso(self.raiz, self.b).prender(7, self.b, 1)[0])
        self.assertTrue(a.prender(8, self.a, 4)[0])

    def test_el_archivo_unico_de_antes_sigue_siendo_de_su_sesion(self):
        os.makedirs(os.path.dirname(os.path.join(self.raiz, ESTADO)))
        with open(os.path.join(self.raiz, ESTADO), "w", encoding="utf-8") as f:
            f.write("analisis=pendientes/7-algo/analisis-1.md\n"
                    "transcripcion=historico-chat/2026-10-04-sesion-a.md\ndesde=1\npausa=5\n")
        a, b = AnalisisEnCurso(self.raiz, self.a), AnalisisEnCurso(self.raiz, self.b)
        self.assertEqual(a.ruta_estado(), os.path.join(self.raiz, ESTADO))
        self.assertEqual(a.leer_estado()["pausa"], 5)
        self.assertIsNone(b.leer_estado())
        self.assertIsNotNone(AnalisisEnCurso(self.raiz).leer_estado())

    def test_el_aviso_de_una_sesion_no_muestra_el_de_otra(self):
        AnalisisEnCurso(self.raiz, self.a).prender(7, self.a, 1)
        self.assertIn("Ningún análisis", AnalisisEnCurso(self.raiz, self.b).aviso())


if __name__ == "__main__":
    unittest.main()
