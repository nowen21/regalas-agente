"""Lo común: rutas, git, lectura de archivos y hallazgos."""
import os
import subprocess
import tempfile
import unittest

from core.comun import AVISO, FALLA, Archivos, Git, Hallazgo, Markdown, Proyecto


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

    def test_el_recorrido_de_md_salta_lo_excluido(self):
        for relativa in ("docs/a.md", "proyectos/x/b.md", "node_modules/c.md", "docs/d.txt"):
            ruta = os.path.join(self.raiz, *relativa.split("/"))
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            open(ruta, "w").close()
        self.assertEqual([self.proyecto.relativa(r) for r in self.proyecto.recorrer_md()], ["docs/a.md"])

    def test_el_estandar_se_encuentra_subiendo(self):
        self.assertTrue(os.path.isfile(os.path.join(Proyecto.estandar(), "base", "00-nucleo-blindado.md")))

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


class LasTablasMarkdownSeLeenPorNombre(unittest.TestCase):

    TEXTO = ("| Clave | Valor | Nota |\n|---|---|---|\n| `a` | uno | x |\n| b | «…» | |\n\n"
             "```\n| Clave | Valor |\n|---|---|\n| falsa | no |\n```\n")

    def test_la_fila_se_lee_por_columna_y_no_por_posicion(self):
        filas = Markdown.filas_de(self.TEXTO, "valor", "clave")
        self.assertEqual([f["clave"] for _, f in filas], ["`a`", "b"])

    def test_la_tabla_dentro_de_un_bloque_de_codigo_no_cuenta(self):
        self.assertEqual(len(Markdown.tablas(self.TEXTO)), 1)

    def test_los_enlaces_de_muestra_no_cuentan(self):
        texto = "[a](a.md) y `[b](b.md)`\n```\n[c](c.md)\n```\n"
        self.assertEqual(Markdown.enlaces(texto), [(1, "a", "a.md")])

    def test_encabezados_sin_el_h1_y_marcadores_sin_casillas(self):
        texto = "# Título\n## Uno\n- [x] hecho\n[por llenar] y [enlace](a.md)\n"
        self.assertEqual(Markdown.encabezados(texto), [(2, "Uno")])
        self.assertEqual(Markdown.marcadores(texto), [(4, "[por llenar]")])

    def test_la_celda_sin_llenar_vale_vacio(self):
        self.assertEqual(Markdown.valor_limpio("`a`"), "a")
        self.assertEqual(Markdown.valor_limpio("«…»"), "")
        self.assertEqual(Markdown.valor_limpio("—"), "")


class LosEnganchesLeenLaRaizYElArchivoIgual(unittest.TestCase):
    """Análisis 1 del pendiente 116, fila 4: las once copias de los enganches."""

    def test_la_raiz_pedida_o_la_que_dice_el_enganche(self):
        from core.comun.consola import raiz_pedida
        self.assertEqual(raiz_pedida(["--raiz", "x"], "y"), os.path.abspath("x"))
        self.assertEqual(raiz_pedida(["--raiz"], "y"), os.path.abspath("y"))
        self.assertEqual(raiz_pedida([], "y"), os.path.abspath("y"))

    def test_el_archivo_de_la_entrada_y_si_no_el_de_la_respuesta(self):
        from core.comun.consola import archivo_editado
        self.assertEqual(archivo_editado({"tool_input": {"file_path": "a"}, "tool_response": {"filePath": "b"}}), "a")
        self.assertEqual(archivo_editado({"tool_input": {"filePath": "c"}}), "c")
        self.assertEqual(archivo_editado({"tool_response": {"file_path": "d"}}), "d")
        self.assertEqual(archivo_editado(None), "")



class ElCatalogoDeEnganchesNoArmaCiclos(unittest.TestCase):
    """Análisis 1 del pendiente 116, fila 23: cada módulo carga solo, en un
    proceso nuevo, sin depender de que otro se haya cargado antes."""

    def test_cada_modulo_carga_por_su_cuenta(self):
        import sys
        cimiento = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        for modulo in ("core.herramientas.instalar", "core.enganches.sesion", "core.validadores.checklist",
                       "core.validadores.herramientas", "core.validadores"):
            corrida = subprocess.run([sys.executable, "-c", "import " + modulo], cwd=cimiento,
                                     capture_output=True, text=True)
            self.assertEqual(0, corrida.returncode, "%s no carga solo: %s" % (modulo, corrida.stderr[-300:]))

    def test_el_instalador_y_el_catalogo_nombran_los_mismos_enganches(self):
        from core.comun.enganches import ENGANCHES_GIT, HOOKS_CLAUDE, NO_SE_SUSPENDEN
        from core.herramientas.instalar import HOOKS
        self.assertEqual(ENGANCHES_GIT, tuple(nombre for nombre, _, _ in HOOKS))
        guiones = {guion for _, _, guion, _, _ in HOOKS_CLAUDE}
        self.assertTrue(set(NO_SE_SUSPENDEN) <= guiones)

if __name__ == "__main__":
    unittest.main()
