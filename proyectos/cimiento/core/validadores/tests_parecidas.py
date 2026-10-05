"""`20·M12` · `EP-004·HU-027` · Las reglas parecidas se avisan al escribir una.

Los casos del plan de pruebas de la fase `A-EP-004-HU-027`. Los que necesitan la
búsqueda por significado se saltan, diciéndolo, donde no está instalada.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

from core.comun import AVISO, Proyecto
from core.validadores.parecidas import APAGADA, ReglasParecidas
from core.validadores.relacionadas import ReglasRelacionadas

ESTANDAR = Proyecto.estandar()
F25 = os.path.join(ESTANDAR, "base", "02-flujo-de-trabajo", "reglas", "F25-autorizar-el-arranque-no-aprueba-el-plan.md")
ENGANCHE = os.path.join(ESTANDAR, "adaptadores", "claude-code", "hook_relacionadas.py")
VALIDAR = os.path.join(ESTANDAR, "validadores", "validar.py")
ENTORNO = dict(os.environ, PYTHONIOENCODING="utf-8")


def correr(orden, entrada=None, donde=ESTANDAR):
    return subprocess.run([sys.executable] + orden, input=entrada, capture_output=True, text=True,
                          encoding="utf-8", cwd=donde, env=ENTORNO)


class ConBusqueda(unittest.TestCase):

    def setUp(self):
        if ReglasParecidas(ESTANDAR).busqueda() is None:
            self.skipTest("la búsqueda por significado de memoria/ no está instalada")


class CP001AlEscribirF25LlegaF4(ConBusqueda):

    def test_el_enganche_la_nombra_sin_detener_y_a_tiempo(self):
        ReglasParecidas(ESTANDAR).de(["F25"])           # que la tabla quede armada antes de medir
        entrada = json.dumps({"session_id": "prueba-%f" % time.time(), "tool_input": {"file_path": F25}})
        inicio = time.time()
        resultado = correr([ENGANCHE], entrada)
        tardo = time.time() - inicio
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("Las que se le parecen por significado", resultado.stdout)
        self.assertIn("`02·F4`", resultado.stdout)
        self.assertLess(tardo, 3, "RNF-01")

    def test_la_tabla_traduce_igual_que_la_libreria(self):
        import numpy as np
        validador = ReglasParecidas(ESTANDAR)
        from core.validadores.metareglas import CuerpoDeReglas
        textos = [ReglasParecidas.texto(r) for r in CuerpoDeReglas.leer(ESTANDAR) if not r.derogada]
        tabla = validador.busqueda().traducir(textos)
        libreria = np.asarray(validador.busqueda().semantica.embed(textos), dtype=float)
        libreria /= np.linalg.norm(libreria, axis=1, keepdims=True)
        self.assertLess(float(np.abs(tabla - libreria).max()), 1e-5)


class CP002PorReglaYPorCommit(ConBusqueda):

    def test_por_regla(self):
        resultado = correr([VALIDAR, "parecidas", "--regla", "F25"])
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("`02·F25` se parece a `02·F4`", resultado.stdout)

    def test_por_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(os.path.join(ESTANDAR, "base"), os.path.join(tmp, "base"))
            for orden in (("init", "-q"), ("config", "user.email", "p@e"), ("config", "user.name", "P"),
                          ("add", "."), ("commit", "-q", "-m", "base", "--no-verify")):
                subprocess.run(("git", "-C", tmp) + orden, capture_output=True, check=True)
            self.assertEqual(ReglasParecidas(tmp, solo_preparados=True).validar(), [])
            copia = os.path.join(tmp, os.path.relpath(F25, ESTANDAR))
            with open(copia, "a", encoding="utf-8") as f:
                f.write("\nUna línea más.\n")
            subprocess.run(("git", "-C", tmp, "add", "."), capture_output=True, check=True)
            avisos = ReglasParecidas(tmp, solo_preparados=True).validar()
            self.assertEqual(len(avisos), 1)
            self.assertIn("`02·F25` se parece a", avisos[0].mensaje)


class CP003SinLaBusquedaLoDice(unittest.TestCase):

    def test_el_subcomando_avisa_que_no_pudo(self):
        avisos = ReglasParecidas(ESTANDAR, ids=["F25"], busqueda=APAGADA).validar()
        self.assertEqual(len(avisos), 1)
        self.assertEqual(avisos[0].severidad, AVISO)
        self.assertIn("no se pudo buscar por significado", avisos[0].mensaje)
        self.assertNotIn("se parece a", avisos[0].mensaje)

    def test_el_enganche_avisa_que_no_pudo(self):
        self.assertIsNone(ReglasParecidas(ESTANDAR, busqueda=APAGADA).de(["F25"]))
        rel = ReglasRelacionadas(ESTANDAR).de(F25)
        rel["parecidas"] = None
        texto = ReglasRelacionadas.como_texto(rel)
        self.assertIn("no se pudieron buscar", texto)
        self.assertNotIn("Las que se le parecen", texto)


if __name__ == "__main__":
    unittest.main()
