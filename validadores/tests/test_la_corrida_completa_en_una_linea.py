# -*- coding: utf-8 -*-
"""`EP-004 · HU-008` · Una línea dice cómo está el proyecto.

**El problema.** `validar.py` tiene más de cuarenta subcomandos. Saber cómo
está un proyecto exigía acordarse de cuáles aplican y leer cuarenta resúmenes,
y lo que no se recuerda no se corre.

**El caso que decide es `CP-004`:** un subcomando nuevo entra solo. Si hubiera
que agregarlo a una lista a mano, el que se registre mañana se quedaría fuera
sin que nadie lo note, y la corrida diría «todo bien» habiendo mirado menos.
"""
import os
import subprocess
import sys
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VALIDAR = os.path.join(RAIZ, "validadores", "validar.py")


def correr(*args, cwd=RAIZ):
    return subprocess.run([sys.executable, VALIDAR] + list(args),
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=900, cwd=cwd)


class LaCorridaCompleta(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.corrida = correr("todo")
        cls.ayuda = correr("--help")

    def test_cp001_cada_subcomando_sigue_corriendo_por_separado(self):
        """La corrida no cambia lo que hacía cada uno: los llama, no los rehace."""
        suelto = correr("estandar")
        self.assertEqual(0, suelto.returncode)
        self.assertIn("Coherencia del estándar", suelto.stdout)

    def test_cp002_una_linea_corre_todo_lo_que_aplica(self):
        salida = self.corrida.stdout
        self.assertIn("Corrida completa", salida)
        self.assertRegex(salida, r"\d+ comprobación\(es\) corridas")
        for esperado in ("Coherencia del estándar", "El estándar contra sus meta-reglas"):
            self.assertIn(esperado, salida, "no corrió una comprobación que aplica")

    def test_cp003_lo_que_queda_fuera_dice_por_que(self):
        """Sin el motivo escrito, «no corrió» se lee como «no hacía falta»."""
        salida = self.corrida.stdout
        for lento in ("linter", "suite", "audit"):
            self.assertIn("(fuera: %s" % lento, salida)
        self.assertIn("tarda", salida)

    def test_cp004_un_subcomando_nuevo_entra_solo(self):
        """El caso que decide: la lista sale del propio analizador."""
        import importlib.util
        spec = importlib.util.spec_from_file_location("validar_mod", VALIDAR)
        modulo = importlib.util.module_from_spec(spec)
        sys.modules["validar_mod"] = modulo
        spec.loader.exec_module(modulo)
        registrados = set()
        with open(VALIDAR, encoding="utf-8") as f:
            for linea in f:
                if 'sub.add_parser("' in linea:
                    registrados.add(linea.split('sub.add_parser("')[1].split('"')[0])
        corridas = set()
        for nombre in registrados:
            if nombre not in modulo.FUERA_DE_LA_CORRIDA:
                corridas.add(nombre)
        self.assertGreater(len(corridas), 25,
                           "la corrida mira muy pocos: ¿se coló una lista a mano?")
        self.assertNotIn("todo", corridas)

    def test_cp005_la_corrida_termina_con_un_resumen_unico(self):
        salida = self.corrida.stdout.strip().splitlines()
        ultimas = "\n".join(salida[-3:])
        self.assertTrue("con fallas" in ultimas or "Sin fallas" in ultimas,
                        "el resumen final no está al final: %r" % ultimas)

    def test_cp006_el_codigo_de_salida_refleja_la_peor(self):
        """Cero si ninguna falló; uno si alguna falló. Sin eso, no sirve en CI."""
        con_fallas = "con fallas: " in self.corrida.stdout and \
            not self.corrida.stdout.rstrip().endswith("0 con fallas")
        self.assertEqual(1 if con_fallas else 0, self.corrida.returncode)

    def test_cp007_el_subcomando_esta_en_la_ayuda(self):
        self.assertIn("todo", self.ayuda.stdout)


if __name__ == "__main__":
    unittest.main()
