# -*- coding: utf-8 -*-
"""`EP-025·HU-017`: el freno no deja escribir un guion para lo que Cimiento ya
hace, y avisa cuando un guion se parece a uno anterior.

Sin Django: corren desde `proyectos/cimiento/` importando `core.validadores`
primero, como `tests_freno`.
"""
import io
import os
import shutil
import tempfile
import time
import unittest

from . import guiones
from .freno import Freno

ANTERIOR = '''"""Mide cuántas reglas se parecen entre sí."""
import os

def contar(carpeta):
    total = 0
    for nombre in os.listdir(carpeta):
        if nombre.endswith(".md"):
            total += 1
    return total

print(contar("base"))
'''


class SinBase:
    def todos(self):
        return {}

    def consultar(self, *args, **kwargs):
        raise RuntimeError("sin base")


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


class LosGuionesRepetidos(unittest.TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        _escribir(os.path.join(self.raiz, "historico-chat", "scripts", "2026-10-05", "medir_reglas_1.py"), ANTERIOR)
        self.freno = Freno(self.raiz, niveles=SinBase())

    def guion(self, nombre, texto, dia="2026-10-06"):
        ruta = os.path.join(self.raiz, "historico-chat", "scripts", dia, nombre)
        return self.freno.guion_repetido(ruta, {"file_path": ruta, "content": texto})

    # CP-001 · Detener
    def test_lo_que_cimiento_hace_se_detiene_con_su_orden(self):
        casos = {
            "escribe estado-fase.md y resultado_pruebas.md": "cerrar_fase",
            "lee historico-chat/.tocado para separar": "cambios_por_sesion",
            "mueve el pendiente a pendientes/hecho/": "cerrar.py",
            "copia plantillas/ciclo-vida-proyectos/04-HU.md": "andamio.py",
            "escribe .githooks/pre-commit": "instalar.py",
            "suma cache_read_input_tokens del .jsonl": "vigilar_consumo",
        }
        for texto, orden in casos.items():
            with self.subTest(texto=texto):
                decision, porque, ruta = self.guion("tarea.py", "# %s\n" % texto)
                self.assertEqual("detiene", decision)
                self.assertIn(orden, porque)
                self.assertEqual("historico-chat/scripts/2026-10-06/tarea.py", ruta)
                self.assertEqual("04·S18", Freno.regla_de(porque))

    def test_fuera_de_la_carpeta_de_guiones_no_se_mira(self):
        ruta = os.path.join(self.raiz, "otra", "tarea.py")
        self.assertIsNone(self.freno.guion_repetido(ruta, {"content": "# estado-fase.md\n"}))
        self.assertIsNone(self.freno.guion_repetido(ruta.replace(".py", ".md"), {"content": "estado-fase.md"}))

    # CP-002 · Avisar
    def test_el_mismo_nombre_con_otro_numero_avisa(self):
        decision, porque, _ruta = self.guion("medir_reglas_2.py", "print('otra cosa')\n")
        self.assertEqual("avisa", decision)
        self.assertIn("medir_reglas_1.py", porque)
        aviso = Freno.aviso_de_nivel(porque, "x.py")
        self.assertIn("No se detiene", aviso)
        self.assertNotIn("está en «avisa»", aviso)

    def test_casi_el_mismo_texto_avisa(self):
        decision, porque, _ruta = self.guion("contar_capitulos.py", ANTERIOR.replace('"base"', '"plantillas"'))
        self.assertEqual("avisa", decision)
        self.assertIn("2026-10-05/medir_reglas_1.py", porque)

    def test_la_mitad_de_las_lineas_iguales_avisa(self):
        # Calibrado con los 105 guiones de scilit (2026-10-08): el par menos parecido
        # de los que antes se avisaban comparte 0,40 de sus líneas.
        lineas = ANTERIOR.splitlines()
        texto = "\n".join(lineas[:len(lineas) // 2] + ["x = %d" % i for i in range(len(lineas) // 2)])
        decision, _porque, _ruta = self.guion("otra_tarea.py", texto)
        self.assertEqual("avisa", decision)

    def test_un_guion_grande_se_compara_rapido(self):
        grande = "\n".join("valor_%d = %d" % (i, i) for i in range(800))
        _escribir(os.path.join(self.raiz, "historico-chat", "scripts", "2026-10-05", "grande.py"), grande)
        inicio = time.monotonic()
        decision, porque, _ruta = self.guion("copia.py", grande)
        self.assertLess(time.monotonic() - inicio, 2)
        self.assertEqual("avisa", decision)
        self.assertIn("grande.py", porque)

    def test_uno_distinto_pasa(self):
        self.assertIsNone(self.guion("migrar_fechas.py", "import datetime\nprint(datetime.date.today())\n"))

    def test_el_mismo_archivo_no_se_compara_consigo(self):
        self.assertIsNone(self.guion("medir_reglas_1.py", ANTERIOR, dia="2026-10-05"))

    def test_las_raices_del_nombre(self):
        self.assertEqual(guiones._raiz_del_nombre("cerrar_hu_006.py"), guiones._raiz_del_nombre("cerrar_hu_010.py"))


if __name__ == "__main__":
    unittest.main()
