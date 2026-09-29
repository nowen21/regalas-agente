# -*- coding: utf-8 -*-
"""`EP-004 · HU-012 · CA-05`: lo que el agente escribe se mide al escribirlo.

**Qué protege.** Las marcas de redacción de un documento solo se contaban al
guardar, en el `pre-commit`, cuando el documento ya se había entregado. El
resumen de la sesión del 2026-09-28 llegó a 39 líneas con marcas sin que el
agente se enterara. Estos casos comprueban que el enganche de escritura se las
devuelve en el mismo turno, y solo por lo recién escrito.
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
HOOK = os.path.join(RAIZ, "adaptadores", "claude-code", "hook_md.py")
sys.path.insert(0, VALIDADORES)

import marcas      # noqa: E402

RAYA = "—"
CON_MARCAS = f"# Nota\n\nUn texto {RAYA}con inciso{RAYA} y más.\n\n- **Qué pasó:** algo pasó\n"


def correr(raiz, entrada):
    r = subprocess.run([sys.executable, HOOK, "--raiz", raiz],
                       input=json.dumps(entrada), capture_output=True,
                       text=True, encoding="utf-8", timeout=120)
    contexto = ""
    if r.stdout.strip():
        contexto = json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]
    return r, contexto


class CP001AlEscribirLleganLasMarcas(unittest.TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.raiz, ignore_errors=True))
        self.ruta = os.path.join(self.raiz, "nota.md")

    def escribir(self, texto):
        with open(self.ruta, "w", encoding="utf-8") as f:
            f.write(texto)

    def test_write_con_marcas_las_devuelve_sin_detener(self):
        self.escribir(CON_MARCAS)
        r, contexto = correr(self.raiz, {"session_id": "p", "tool_name": "Write",
                                         "tool_input": {"file_path": self.ruta,
                                                        "content": CON_MARCAS}})
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("MARCA(S) DE `00·ID8`", contexto)
        self.assertIn("raya larga", contexto)
        self.assertIn("viñeta que abre con negrita", contexto)
        self.assertIn("en su lugar", contexto)

    def test_edit_sin_marcas_no_repite_las_viejas(self):
        self.escribir(CON_MARCAS + "\nOtra línea limpia.\n")
        r, contexto = correr(self.raiz, {"session_id": "p", "tool_name": "Edit",
                                         "tool_input": {"file_path": self.ruta,
                                                        "old_string": "x",
                                                        "new_string": "Otra línea limpia."}})
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertEqual("", contexto)

    def test_un_archivo_que_no_es_md_no_trae_nada(self):
        ruta = os.path.join(self.raiz, "algo.py")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(f"# {RAYA} comentario\n")
        r, contexto = correr(self.raiz, {"session_id": "p", "tool_name": "Write",
                                         "tool_input": {"file_path": ruta,
                                                        "content": f"# {RAYA} x"}})
        self.assertEqual(0, r.returncode)
        self.assertEqual("", contexto)

    def test_con_enlace_roto_detiene_y_nombra_las_marcas(self):
        texto = CON_MARCAS + "\n[roto](no-existe.md)\n"
        self.escribir(texto)
        r, _ = correr(self.raiz, {"session_id": "p", "tool_name": "Write",
                                  "tool_input": {"file_path": self.ruta,
                                                 "content": texto}})
        self.assertEqual(2, r.returncode)
        self.assertIn("enlaces rotos", r.stderr)
        self.assertIn("MARCA(S) DE `00·ID8`", r.stderr)

    def test_la_marca_dentro_de_codigo_no_cuenta(self):
        texto = f"# Nota\n\n```\nx {RAYA}y{RAYA} z\n```\n"
        self.assertEqual([], marcas.medir_texto(texto))

    def test_el_espacio_duro_dice_con_que_se_reemplaza(self):
        [(n, _c, _nombre, lugar)] = marcas.medir_texto("Una cosa.")
        self.assertEqual(1, n)
        self.assertEqual("un espacio normal", lugar)


MOLDE = os.path.join(RAIZ, "plantillas", "sesion.md")

HALLAZGO_TABLA = """### H-1 · el hueco

| Campo | Valor |
|---|---|
| Qué pasó | el usuario preguntó por qué el agente olvida las reglas |
| Qué lo soluciona | **EP-005 · HU nueva — que lleguen**<br>Como agente<br>Quiero las reglas<br>Para cumplirlas<br>Contexto: hoy llegan cortadas |
| Estado | abierto |
| Nace en | 2026-09-28 · por qué el agente olvida las reglas |
| Con qué se retoma | ¿cuál es el tope? |
"""

HALLAZGO_VINETA = """### H-2 · el viejo

- **Estado:** resuelto acá
- **Con qué se retoma:** —
"""


class CP002ElMoldeLlenoNoSumaMarcas(unittest.TestCase):

    def setUp(self):
        import resumen
        self.resumen = resumen
        self.dir = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.dir, ignore_errors=True))

    def guardar(self, nombre, texto):
        ruta = os.path.join(self.dir, nombre)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)
        return ruta

    def test_el_molde_vacio_no_tiene_marcas(self):
        with open(MOLDE, encoding="utf-8") as f:
            self.assertEqual([], marcas.medir_texto(f.read()))

    def test_un_hallazgo_lleno_en_tabla_no_tiene_marcas(self):
        self.assertEqual([], marcas.medir_texto(HALLAZGO_TABLA))

    def test_resumen_lee_el_estado_en_la_tabla(self):
        ruta = self.guardar("nuevo.md", HALLAZGO_TABLA)
        self.assertEqual([("H-1", "el hueco", "abierto")],
                         self.resumen.hallazgos(ruta))
        self.assertEqual("¿cuál es el tope?", self.resumen._retoma(ruta, "H-1"))

    def test_resumen_sigue_leyendo_la_forma_vieja(self):
        ruta = self.guardar("viejo.md", HALLAZGO_VINETA)
        self.assertEqual([("H-2", "el viejo", "resuelto acá")],
                         self.resumen.hallazgos(ruta))
        self.assertEqual("—", self.resumen._retoma(ruta, "H-2"))

    def test_viene_de_se_lee_en_la_tabla_y_en_la_forma_vieja(self):
        nuevo = self.guardar("a.md", "| Campo | Valor |\n|---|---|\n"
                                     "| Viene de | 2026-09-28 · sesion · H-1 |\n")
        viejo = self.guardar("b.md", "**Viene de:** 2026-09-28 · sesion · H-1\n")
        vacio = self.guardar("c.md", "| Campo | Valor |\n|---|---|\n| Viene de | «...» |\n")
        self.assertEqual("2026-09-28 · sesion · H-1", self.resumen.viene_de(nuevo))
        self.assertEqual("2026-09-28 · sesion · H-1", self.resumen.viene_de(viejo))
        self.assertEqual("", self.resumen.viene_de(vacio))


if __name__ == "__main__":
    unittest.main(verbosity=2)
