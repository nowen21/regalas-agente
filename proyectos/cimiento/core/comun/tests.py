"""Lo común: rutas, git, lectura de archivos y hallazgos."""
import os
import subprocess
import tempfile
import unittest

from core.comun import AVISO, FALLA, Archivos, Git, Hallazgo, Proyecto


class ElProyectoSabeQueQuedaAdentro(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = os.path.join(self.tmp.name, "agente")
        os.makedirs(os.path.join(self.raiz, "docs"))
        os.makedirs(os.path.join(self.tmp.name, "agente-viejo"))
        self.proyecto = Proyecto(self.raiz)

    def tearDown(self):
        self.tmp.cleanup()

    def test_lo_de_adentro_da_su_ruta_con_barra(self):
        self.assertEqual(self.proyecto.relativa(os.path.join(self.raiz, "docs", "a.md")), "docs/a.md")

    def test_la_ruta_relativa_se_lee_desde_la_raiz(self):
        self.assertEqual(self.proyecto.relativa("docs/a.md"), "docs/a.md")

    def test_la_carpeta_vecina_con_el_mismo_comienzo_queda_afuera(self):
        self.assertIsNone(self.proyecto.relativa(os.path.join(self.tmp.name, "agente-viejo", "x")))

    def test_salir_con_dos_puntos_queda_afuera(self):
        self.assertFalse(self.proyecto.contiene("../agente-viejo/x"))

    @unittest.skipUnless(os.name == "nt", "la ruta /c/ solo existe en Windows")
    def test_la_ruta_de_la_consola_de_git_es_la_misma(self):
        unidad = self.raiz[0].lower()
        estilo_git = "/%s%s" % (unidad, self.raiz[2:].replace("\\", "/"))
        self.assertEqual(self.proyecto.relativa(estilo_git + "/docs/a.md"), "docs/a.md")

    def test_la_raiz_sale_de_la_orden_o_del_valor_por_defecto(self):
        self.assertEqual(Proyecto.desde_argumentos(["x", "--raiz", self.raiz], "/otra").raiz,
                         os.path.realpath(self.raiz))
        self.assertEqual(Proyecto.desde_argumentos(["x"], self.raiz).raiz, os.path.realpath(self.raiz))


class LosArchivosSeLeenSinReventar(unittest.TestCase):

    def test_el_que_no_esta_da_vacio_y_queda_anotado(self):
        archivos = Archivos()
        self.assertEqual(archivos.leer("no-existe.md"), "")
        self.assertEqual([h.severidad for h in archivos.ilegibles()], [AVISO])

    def test_el_que_no_es_utf8_se_lee_a_medias_y_queda_anotado(self):
        with tempfile.NamedTemporaryFile("wb", suffix=".md", delete=False) as f:
            f.write(b"bien \xff mal")
        try:
            archivos = Archivos()
            self.assertIn("bien", archivos.leer(f.name))
            self.assertEqual(len(archivos.ilegibles()), 1)
        finally:
            os.unlink(f.name)


class GitCorreEnSuRepositorio(unittest.TestCase):

    def test_lista_lo_versionado_y_calla_si_no_es_repositorio(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(Git(tmp).versionados(), [])
            subprocess.run(["git", "init", "-q", tmp], check=True)
            with open(os.path.join(tmp, "a.py"), "w") as f:
                f.write("x = 1\n")
            subprocess.run(["git", "-C", tmp, "add", "a.py"], check=True)
            self.assertTrue(Git.es_repositorio(tmp))
            self.assertEqual(Git(tmp).versionados(), ["a.py"])


class ElHallazgoDiceSuRegla(unittest.TestCase):

    def test_la_regla_con_capitulo_gana(self):
        self.assertEqual(Hallazgo(FALLA, "a", 1, "falta (Q3) y 07·Q3").regla, "07·Q3")

    def test_la_declarada_manda(self):
        self.assertEqual(Hallazgo(AVISO, "a", 1, "02·F8", regla="07·Q3").regla, "07·Q3")


if __name__ == "__main__":
    unittest.main()
