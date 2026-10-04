# -*- coding: utf-8 -*-
"""`EP-005 · HU-023 · CA-09`: sin la palabra de `01·C28` el agente no actúa, y
ninguna escritura sale del proyecto.

**Qué protege.** El usuario pidió el 2026-09-29 que, cuando un mensaje no trae
la palabra de `01·C28`, el agente se la recuerde y espere, y que las reglas
salgan de la palabra con que responde, sin que el agente muestre que las lee.
Y el 2026-09-28, que ninguna escritura quede fuera del repositorio.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
HOOK = os.path.join(RAIZ, "adaptadores", "claude-code", "hook_antes.py")
REGLAS = os.path.join(RAIZ, "base", "reglas-por-tarea")
sys.path.insert(0, VALIDADORES)

import recuperar    # noqa: E402


class SinLaPalabraNoSeActua(unittest.TestCase):

    def test_sin_palabra_llega_el_aviso_con_la_lista(self):
        texto = recuperar.como_texto("pero por qué no funciona", RAIZ)
        self.assertIn("NO ABRE CON UNA PALABRA DE `01·C28`", texto)
        for palabra in ("Pregunta", "Hágalo", "aplique", "Suba", "Pare"):
            self.assertIn("«%s»" % palabra, texto)
        self.assertNotIn("Read", texto)

    def test_con_palabra_llegan_las_reglas_y_no_el_aviso(self):
        texto = recuperar.como_texto("Suba", RAIZ)
        self.assertNotIn("NO ABRE CON UNA PALABRA", texto)
        self.assertIn("N2", texto)

    def test_la_palabra_cuenta_con_tilde_o_sin_ella_y_al_abrir_una_frase(self):
        self.assertTrue(recuperar.trae_palabra_clave("hagalo", RAIZ))
        self.assertTrue(recuperar.trae_palabra_clave("Listo. Continúe con eso", RAIZ))
        self.assertFalse(recuperar.trae_palabra_clave("ya lo quité, suba", RAIZ))

    def test_lo_que_agrega_el_editor_no_cuenta_como_palabra(self):
        self.assertFalse(recuperar.trae_palabra_clave(
            "<ide_opened_file>Revise esto</ide_opened_file>ya", RAIZ))

    def test_ningun_bloque_pide_leer_con_la_herramienta(self):
        self.assertNotIn("leerlas con Read", recuperar.como_texto("Hágalo", RAIZ))


class NingunaEscrituraSaleDelProyecto(unittest.TestCase):

    def setUp(self):
        self.proyecto = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.proyecto, ignore_errors=True))

    def correr(self, datos):
        r = subprocess.run([sys.executable, HOOK, "--modo", "accion", "--raiz", self.proyecto],
                           input=json.dumps(datos), capture_output=True,
                           text=True, encoding="utf-8", timeout=60)
        self.assertEqual(0, r.returncode, r.stderr)
        return json.loads(r.stdout) if r.stdout.strip() else {}

    def detenida(self, herramienta, ruta):
        salida = self.correr({"tool_name": herramienta, "tool_input": {"file_path": ruta}})
        return salida.get("hookSpecificOutput", {}).get("permissionDecisionReason", "")

    def test_escribir_fuera_del_proyecto_se_detiene(self):
        motivo = self.detenida("Write", os.path.join(tempfile.gettempdir(), "guion.py"))
        self.assertIn("fuera del proyecto", motivo)          # el freno de EP-023, HU-007 (pendiente 109)
        self.assertIn("historico-chat/scripts/", motivo)

    def test_escribir_dentro_del_proyecto_pasa(self):
        self.assertEqual("", self.detenida(
            "Write", os.path.join(self.proyecto, "historico-chat", "scripts", "g.py")))

    def test_la_carpeta_hermana_con_el_mismo_comienzo_es_afuera(self):
        self.assertIn("fuera del proyecto", self.detenida(
            "Edit", os.path.join(self.proyecto + "-otro", "a.py")))

    def test_un_comando_no_se_detiene(self):
        self.assertEqual({}, self.correr({"tool_name": "Bash",
                                          "tool_input": {"command": "git status"}}))

    def test_el_instalador_pone_el_freno_antes_de_toda_accion(self):
        """Desde EP-023, HU-007, fase B, el freno corre antes de toda herramienta (pendiente 109)."""
        import instalar
        suyos = [e for e in instalar.HOOKS_CLAUDE if e[2] == "hook_antes.py"]
        self.assertEqual([("PreToolUse", None, "--modo accion")],
                         [(e[0], e[1], e[4]) for e in suyos])


class CadaArchivoPorTareaCabeEnUnaLectura(unittest.TestCase):

    def test_ningun_archivo_pasa_de_30000_caracteres(self):
        for nombre in os.listdir(REGLAS):
            with open(os.path.join(REGLAS, nombre), encoding="utf-8") as f:
                self.assertLess(len(f.read()), 30000, nombre)


class LasCopiasPorTareaNoSeCuentanAlGuardar(unittest.TestCase):
    """Las marcas de `base/reglas-por-tarea/` son las de las reglas que copian."""

    def setUp(self):
        self.repo = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.repo, ignore_errors=True))
        for orden in (("init", "-q"), ("config", "user.email", "x@x"),
                      ("config", "user.name", "x"), ("commit", "-q", "--allow-empty", "-m", "x")):
            subprocess.run(("git", "-C", self.repo) + orden, check=True, capture_output=True)

    def preparar(self, rel, texto):
        ruta = os.path.join(self.repo, *rel.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)
        subprocess.run(("git", "-C", self.repo, "add", rel), check=True, capture_output=True)

    def test_la_copia_no_falla_y_la_regla_si(self):
        import marcas
        texto = u"# Regla\n\nUna frase — con raya larga.\n"
        self.preparar("base/reglas-por-tarea/tarea.md", texto)
        self.assertEqual([], marcas.validar_preparados(self.repo))
        self.preparar("base/01-capitulo.md", texto)
        self.assertTrue(marcas.validar_preparados(self.repo))


if __name__ == "__main__":
    unittest.main(verbosity=2)
