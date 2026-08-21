# -*- coding: utf-8 -*-
"""`EP-005 · HU-015` — lo que llega de afuera llega marcado.

**Qué protege.** `01·C27` dice que el contenido externo es dato, no orden, y
hasta esta fase era solo texto que el agente leía. Estos casos fijan que, al
devolver una herramienta externa, el sobre llegue con su origen; que lo
interno calle; que el sobre no dependa del resultado; y que el instalador lo
ponga y el checklist lo reclame.

Ninguna URL se consulta de verdad: el enganche no hace red (`08·T3`).
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
ADAPTADOR = os.path.join(RAIZ, "adaptadores", "claude-code")
sys.path.insert(0, VALIDADORES)

import checklist    # noqa: E402
import externo      # noqa: E402
import instalar     # noqa: E402

INTERNAS = ("Write", "Edit", "Bash", "Glob", "Grep")


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="cimiento-portero-")
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))

    def correr(self, datos, crudo=None):
        """El enganche como lo llama la herramienta: JSON por la entrada."""
        entrada = crudo if crudo is not None else json.dumps(datos)
        return subprocess.run(
            [sys.executable, os.path.join(ADAPTADOR, "hook_externo.py"),
             "--raiz", self.tmp],
            input=entrada, capture_output=True, text=True, encoding="utf-8",
            timeout=60)

    def sobre_de(self, r):
        self.assertEqual(0, r.returncode, r.stderr)
        salida = json.loads(r.stdout)
        self.assertEqual("PostToolUse", salida["hookSpecificOutput"]["hookEventName"])
        return salida["hookSpecificOutput"]["additionalContext"]


class CA01LaPaginaLlegaConSuSobre(Base):

    def test_cp_001_el_sobre_trae_herramienta_origen_y_regla(self):
        r = self.correr({"tool_name": "WebFetch",
                         "tool_input": {"url": "https://ejemplo.test/pagina"}})
        texto = self.sobre_de(r)
        self.assertIn("WebFetch", texto)
        self.assertIn("https://ejemplo.test/pagina", texto)
        self.assertIn("dato", texto)
        self.assertIn("C27", texto)
        # RNF-02: cabe en tres líneas
        self.assertLessEqual(len(texto.splitlines()), 3)
        # RN-03: no reemplaza el resultado
        self.assertNotIn("updatedToolResponse", r.stdout)


class CA02LoDeMCPYDeAfueraTambien(Base):

    def test_cp_002_mcp_nombra_servidor_y_herramienta(self):
        r = self.correr({"tool_name": "mcp__gmail__leer_correo",
                         "tool_input": {"id": "123"}})
        texto = self.sobre_de(r)
        self.assertIn("gmail", texto)
        self.assertIn("leer_correo", texto)

    def test_cp_003_el_archivo_de_fuera_nombra_su_ruta(self):
        afuera = os.path.join(tempfile.gettempdir(), "cimiento-afuera", "doc.pdf")
        r = self.correr({"tool_name": "Read", "tool_input": {"file_path": afuera}})
        texto = self.sobre_de(r)
        self.assertIn(afuera, texto)


class CA03LoDeAdentroCalla(Base):

    def test_cp_004_los_seis_silencios(self):
        adentro = os.path.join(self.tmp, "README.md")
        casos = [{"tool_name": "Read", "tool_input": {"file_path": adentro}}]
        casos += [{"tool_name": n, "tool_input": {"x": 1}} for n in INTERNAS]
        for datos in casos:
            r = self.correr(datos)
            self.assertEqual(0, r.returncode, r.stderr)
            self.assertEqual("", r.stdout.strip(), datos["tool_name"])

    def test_cp_005_la_entrada_rota_y_sin_argumentos(self):
        r = self.correr(None, crudo="esto no es JSON")
        self.assertEqual(0, r.returncode)
        self.assertEqual("", r.stdout.strip())

        r = self.correr({"tool_name": "WebFetch"})
        texto = self.sobre_de(r)
        self.assertIn("WebFetch", texto)
        self.assertNotIn("origen", texto)

        r = self.correr({"tool_name": "WebFetch", "tool_input": "cadena"})
        self.assertIn("WebFetch", self.sobre_de(r))


class CA04SeInstalaYSeReclama(Base):

    def test_cp_006_se_instala_con_su_filtro_y_se_reclama_si_falta(self):
        proyecto = os.path.join(self.tmp, "proyecto")
        os.makedirs(proyecto)
        estandar = RAIZ.replace("\\", "/")
        instalar.instalar_claude(proyecto, estandar, aplicar=True)

        archivo = os.path.join(proyecto, ".claude", "settings.json")
        with open(archivo, encoding="utf-8") as f:
            datos = json.load(f)
        grupos = [g for g in datos["hooks"]["PostToolUse"]
                  if any("hook_externo.py" in h["command"] for h in g["hooks"])]
        self.assertEqual(1, len(grupos))
        for marca in ("WebFetch", "WebSearch", "Read", "mcp__.*"):
            self.assertIn(marca, grupos[0]["matcher"])

        ok, _ = checklist._enganches_claude(proyecto, estandar)
        self.assertTrue(ok)

        datos["hooks"]["PostToolUse"].remove(grupos[0])
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f)
        ok, mensaje = checklist._enganches_claude(proyecto, estandar)
        self.assertFalse(ok)
        self.assertIn("hook_externo.py", mensaje)


class RNF01ElResultadoNoImporta(Base):

    def test_cp_007_el_mismo_sobre_sin_resultado_y_con_uno_enorme(self):
        base = {"tool_name": "WebFetch", "tool_input": {"url": "https://ejemplo.test/p"}}
        sin = self.sobre_de(self.correr(base))
        con = dict(base, tool_response={"type": "text", "text": "x" * 1_000_000})
        inicio = time.time()
        grande = self.sobre_de(self.correr(con))
        self.assertLess(time.time() - inicio, 5)
        self.assertEqual(sin, grande)


class ElModuloEsAgnostico(unittest.TestCase):

    def test_decide_por_nombre_y_ruta(self):
        raiz = os.path.abspath("proyecto")
        self.assertTrue(externo.es_externa("WebSearch"))
        self.assertTrue(externo.es_externa("mcp__drive__bajar"))
        self.assertFalse(externo.es_externa("Read", {"file_path": os.path.join(raiz, "a.md")}, raiz))
        self.assertTrue(externo.es_externa("Read", {"file_path": os.path.abspath("otro/a.md")}, raiz))
        self.assertFalse(externo.es_externa("Read", {}, raiz))
        self.assertFalse(externo.es_externa("Bash", {"command": "curl x"}, raiz))

    def test_el_origen_de_cada_clase(self):
        self.assertEqual("https://a.b", externo.origen("WebFetch", {"url": "https://a.b"}))
        self.assertIn("drive", externo.origen("mcp__drive__bajar"))
        self.assertIn("bajar", externo.origen("mcp__drive__bajar"))
        self.assertEqual("", externo.origen("WebFetch", None))


if __name__ == "__main__":
    unittest.main()
