# -*- coding: utf-8 -*-
"""Análisis 1 del pendiente 110 · Lo que un proyecto reporta se corrige para todos.

Cada caso corre desde un proyecto de prueba que no es Cimiento, en una carpeta
temporal: lo que scilit reportó le pasa a cualquier proyecto.
"""
import io
import os
import re
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import andamio          # noqa: E402
import autorizado       # noqa: E402
import aviso_resuelto   # noqa: E402
import comun            # noqa: E402
import freno            # noqa: E402
import instalar         # noqa: E402
import pendientes       # noqa: E402

ADAPTADORES = os.path.join(os.path.dirname(VALIDADORES), "adaptadores", "claude-code")


class Proyecto(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = os.path.realpath(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, relativa, texto="x\n"):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def rotos(self, archivo):
        texto = io.open(archivo, encoding="utf-8").read()
        enlaces = [e for e in re.findall(r"\]\(([^)]+)\)", texto)
                   if not e.startswith("http") and "«" not in e]
        base = os.path.dirname(archivo)
        return [e for e in enlaces if not os.path.exists(os.path.join(base, e.split("#")[0]))]


class Causa1LasHerramientasSirvenDesdeUnProyecto(Proyecto):
    """Pendientes 110 y 114."""

    def test_el_andamio_crea_la_historia_con_las_plantillas_del_estandar(self):
        self.escribir("documentacion/epicas/EP-001-algo/epica.md", "# EP-001 · Algo\n\n## 9. Historias\n\n| a |\n|---|\n")
        destino, _ = andamio.crear_hu(self.raiz, "EP-001-algo", "una-cosa", escribir=True)
        hu = os.path.join(destino, os.path.basename(destino) + ".md")
        self.assertTrue(os.path.isfile(hu))
        self.assertEqual([], self.rotos(hu))

    def test_el_pendiente_puede_vivir_en_una_epica(self):
        self.escribir("documentacion/epicas/EP-001-algo/epica.md", "# EP-001 · Algo\n")
        destino, _ = andamio.crear_pendiente(self.raiz, "algo-falla", "EP-001-algo", escribir=True)
        self.assertIn(os.path.join("EP-001-algo", "pendientes"), destino)
        self.assertEqual([], self.rotos(destino))

    def test_stack_md_nace_y_se_repara_sin_enlaces_rotos(self):
        instalar.instalar_agente_config(self.raiz, True)
        stack = os.path.join(self.raiz, ".agente", "stack.md")
        self.assertEqual([], self.rotos(stack))
        self.escribir(".agente/stack.md", "[ID8](../base/00-identidad-y-rol/x.md) y [mío](../LEEME.md)\n")
        self.escribir("LEEME.md")
        instalar._reparar_marcadores(stack, self.raiz, True, "stack")
        texto = io.open(stack, encoding="utf-8").read()
        self.assertIn("](%s/base/" % comun.RAIZ.replace("\\", "/"), texto)
        self.assertIn("[mío](../LEEME.md)", texto)


class Causa2LosControlesConocenLoQueEscribenLasHerramientas(Proyecto):
    """Pendientes 112 y 113."""

    def test_lo_que_escriben_el_instalador_y_el_andamio_esta_autorizado(self):
        autorizadas = [autorizado.HERRAMIENTAS]
        self.assertTrue(autorizado.quien_autoriza("documentacion/versiones/2026-10-04-53.2.0.md", autorizadas))
        self.assertTrue(autorizado.quien_autoriza("documentacion/epicas/EP-001-x/HU-001-y/README.md", autorizadas))
        self.assertIsNone(autorizado.quien_autoriza("src/app.py", autorizadas))

    def test_la_carpeta_de_un_archivo_declarado_se_puede_crear(self):
        permitido = {"fases": [("documentacion/epicas/EP-1/HU-1/A", True, {"templates/registration/login.html"})],
                     "reglas": [], "de_una": set(), "corrija": False}
        self.assertIsNone(freno.motivo(self.raiz, os.path.join(self.raiz, "templates", "registration"), permitido))
        self.assertIsNotNone(freno.motivo(self.raiz, os.path.join(self.raiz, "templates", "otra"), permitido))


    def test_instalar_en_el_entorno_del_proyecto_se_deja(self):
        """Pendiente 115; acuerdo 8: el entorno `venv/` está dentro del proyecto."""
        app = os.path.join(self.raiz, "proyectos", "app")
        self.assertIsNone(freno.nunca("venv/Scripts/python.exe -m pip install paquete==1.0", False, self.raiz, app))
        self.assertIsNone(freno.nunca(".venv/bin/pip install paquete", False, self.raiz, self.raiz))

    def test_lo_que_nunca_se_deja_no_lee_el_texto_de_un_heredoc(self):
        self.assertIsNone(freno.nunca("python - <<'EOF'\nprint('pip install x')\nEOF", False, self.raiz, self.raiz))

    def test_instalar_fuera_del_proyecto_sigue_detenido(self):
        self.assertIsNotNone(freno.nunca("pip install paquete", False, self.raiz, self.raiz))
        self.assertIsNotNone(freno.nunca("python -m pip install paquete", False, self.raiz, self.raiz))
        self.assertIsNotNone(freno.nunca("C:/Python311/python.exe -m pip install paquete", False, self.raiz, self.raiz))
        self.assertIsNotNone(freno.nunca("venv/Scripts/pip install a && npm install -g b", False, self.raiz, self.raiz))

    def test_el_dispositivo_nulo_dentro_de_una_sustitucion_no_es_un_archivo(self):
        self.assertEqual([], freno.destinos('x=$(python a.py 2>&1 >/dev/null)'))

    def test_el_indice_escrito_como_lista_recibe_la_historia(self):
        self.escribir("documentacion/epicas/EP-001-algo/epica.md", "# EP-001 · Algo\n\n## 9. Historias\n\n| a |\n|---|\n")
        readme = self.escribir("documentacion/epicas/EP-001-algo/README.md", "# EP-001\n\n- [epica.md](epica.md) — la épica.\n")
        andamio.crear_hu(self.raiz, "EP-001-algo", "una-cosa", escribir=True)
        self.assertIn("- [", io.open(readme, encoding="utf-8").read().splitlines()[-1])


class Causa3LosEnganchesLeenEnUtf8(Proyecto):
    """Pendiente 111."""

    def test_la_i_tildada_no_llega_partida(self):
        programa = "import sys; sys.path.insert(0, %r); import comun; print(ascii(comun.entrada_json()['t']))" % VALIDADORES
        r = subprocess.run([sys.executable, "-c", programa], input='{"t": "aquí"}'.encode("utf-8"),
                           capture_output=True)
        self.assertEqual("'aqu\\xed'", r.stdout.decode().strip())

    def test_ningun_enganche_lee_la_entrada_con_la_codificacion_de_la_consola(self):
        for nombre in os.listdir(ADAPTADORES):
            if nombre.endswith(".py"):
                with self.subTest(enganche=nombre):
                    codigo = comun.leer(os.path.join(ADAPTADORES, nombre))
                    self.assertIsNone(re.search(r"=\s*json\.load\(sys\.stdin\)", codigo))


class ElAvisoLlegaPorElEnlaceDirecto(Proyecto):
    """Acuerdos 4 y 5: el reporte enlaza su seguimiento, y los que se reúnen toman su estado."""

    def test_el_aviso_sigue_el_enlace_directo_al_seguimiento(self):
        seguimiento = os.path.dirname(self.escribir("proyecto/resumenes/pendientes/5-espera/pendiente.md", "# P\n"))
        reporte = self.escribir("estandar/pendientes/110-algo/pendiente.md",
                                "| | |\n|---|---|\n| **De dónde sale** | [su seguimiento](%s) |\n"
                                % os.path.join(seguimiento, "pendiente.md").replace("\\", "/"))
        self.assertEqual((seguimiento, ""), aviso_resuelto.seguimiento_de(os.path.dirname(reporte)))

    def test_el_aviso_sale_en_todo_commit_del_estandar_y_no_en_un_proyecto(self):
        """Acuerdo 6: no depende de que el commit anote una fase."""
        codigo = comun.leer(os.path.join(ADAPTADORES, "hook_estacion.py"))
        bloque = codigo[codigo.index("aviso_resuelto.avisar") - 900:codigo.index("aviso_resuelto.avisar")]
        self.assertNotIn("if tocadas:", bloque)
        self.assertIn("comun.RAIZ", bloque)

    def test_el_pendiente_reunido_toma_el_estado_del_que_lo_reune(self):
        self.escribir("p/110-a/pendiente.md", "# P\n")
        reunido = os.path.dirname(self.escribir(
            "p/111-b/pendiente.md", "# P\n\nSe resuelve en el [análisis 1 del 110](../110-a/analisis-1.md).\n"))
        self.assertTrue(pendientes.resuelto_en(reunido).endswith("110-a"))


if __name__ == "__main__":
    unittest.main()
