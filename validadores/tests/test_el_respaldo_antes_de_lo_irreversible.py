# -*- coding: utf-8 -*-
"""`09·15` · El respaldo se hace antes, y si no se puede no se corre nada.

**`00·N7` exige comprobar que hay de dónde volver antes de lo irreversible**, y
hoy eso lo cumple el agente acordándose. Una regla del núcleo no debería
depender de que alguien se acuerde.

**El límite es la mitad del trabajo, y va escrito en la salida del programa:**
«operación irreversible» en general **no se detecta sin criterio**. Un borrado
escrito a mano, un guion de limpieza propio o un borrado por interfaz no los ve
nadie.

> **Un respaldo automático parcial que se anuncia como total es peor que no
> tenerlo**, porque genera confianza donde no la hay.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import respaldo    # noqa: E402
from comun import RAIZ      # noqa: E402

GUION = os.path.join(VALIDADORES, "respaldo.py")


def proyecto(comando_respaldo=None):
    """Un proyecto con su `.agente/stack.md`, con o sin respaldo declarado."""
    tmp = tempfile.TemporaryDirectory()
    d = os.path.join(tmp.name, ".agente")
    os.makedirs(d)
    filas = u"| Acción | Comando |\n|---|---|\n| Correr las pruebas | `pytest` |\n"
    if comando_respaldo:
        filas += u"| **Respaldo de datos** | `%s` |\n" % comando_respaldo
    else:
        filas += u"| **Respaldo de datos** | `«…»` |\n"
    with io.open(os.path.join(d, "stack.md"), "w", encoding="utf-8") as f:
        f.write(u"# Stack\n\n" + filas)
    return tmp


class SinRespaldoDeclaradoNoCorreNada(unittest.TestCase):
    """**Es la regla entera.** Si no hay red, no se salta."""

    def test_el_marcador_sin_llenar_no_cuenta_como_comando(self):
        tmp = proyecto()
        self.addCleanup(tmp.cleanup)
        self.assertEqual("", respaldo.comando_de_respaldo(tmp.name))

    def test_no_da_el_visto_bueno(self):
        tmp = proyecto()
        self.addCleanup(tmp.cleanup)
        ok, mensaje = respaldo.respaldar(tmp.name, "2026-01-02", escribir=True)
        self.assertFalse(ok)
        self.assertIn("no se corre la operación", mensaje)

    def test_el_programa_sale_con_error(self):
        tmp = proyecto()
        self.addCleanup(tmp.cleanup)
        r = subprocess.run([sys.executable, GUION, "--raiz", tmp.name,
                            "--aplicar", "--", "echo", "peligro"],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        self.assertEqual(1, r.returncode)
        self.assertNotIn("peligro\n", r.stdout.replace("echo peligro", ""))

    def test_no_inventa_el_comando(self):
        """**Adivinar cómo se respalda una base ajena sería equivocarse justo
        antes de lo irreversible.**"""
        tmp = proyecto()
        self.addCleanup(tmp.cleanup)
        _ok, mensaje = respaldo.respaldar(tmp.name, "2026-01-02")
        self.assertIn("no declara", mensaje)


class ConRespaldoDeclarado(unittest.TestCase):

    def test_lee_el_comando(self):
        tmp = proyecto("echo respaldando")
        self.addCleanup(tmp.cleanup)
        self.assertEqual("echo respaldando", respaldo.comando_de_respaldo(tmp.name))

    def test_sin_aplicar_no_corre_nada(self):
        tmp = proyecto("echo respaldando")
        self.addCleanup(tmp.cleanup)
        ok, mensaje = respaldo.respaldar(tmp.name, "2026-01-02", escribir=False)
        self.assertTrue(ok)
        self.assertIn("se correría", mensaje)

    def test_si_el_respaldo_falla_no_se_corre_la_operacion(self):
        """**La otra mitad.** Un respaldo que falló y una operación que corre
        igual es la peor combinación: creer que hay red y no tenerla."""
        tmp = proyecto("exit 1")
        self.addCleanup(tmp.cleanup)
        ok, mensaje = respaldo.respaldar(tmp.name, "2026-01-02", escribir=True)
        self.assertFalse(ok)
        self.assertIn("no se corre la operación", mensaje)

    def test_con_respaldo_bueno_la_operacion_corre(self):
        tmp = proyecto("echo respaldando")
        self.addCleanup(tmp.cleanup)
        r = subprocess.run([sys.executable, GUION, "--raiz", tmp.name,
                            "--aplicar", "--", "echo", "listo"],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        self.assertEqual(0, r.returncode)
        self.assertIn("listo", r.stdout)


class ElLimiteSeDiceCadaVez(unittest.TestCase):
    """**Sin esto el programa sería peligroso**: daría confianza de que cubre
    todo lo destructivo, y cubre solo lo que se le pasa por la mano."""

    def test_la_salida_advierte_lo_que_no_cubre(self):
        tmp = proyecto("echo respaldando")
        self.addCleanup(tmp.cleanup)
        r = subprocess.run([sys.executable, GUION, "--raiz", tmp.name,
                            "--", "echo", "x"],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        self.assertIn("no los ve nadie", r.stdout)

    def test_lo_dice_tambien_cuando_no_hay_declaracion(self):
        tmp = proyecto()
        self.addCleanup(tmp.cleanup)
        r = subprocess.run([sys.executable, GUION, "--raiz", tmp.name,
                            "--", "echo", "x"],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        self.assertIn("no los ve nadie", r.stdout)

    def test_sin_operacion_no_hace_nada_y_dice_como_se_usa(self):
        r = subprocess.run([sys.executable, GUION],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        self.assertEqual(2, r.returncode)
        self.assertIn("Uso:", r.stdout)


class LaPlantillaLoDeclara(unittest.TestCase):

    def test_stack_md_tiene_la_fila_del_respaldo(self):
        with io.open(os.path.join(RAIZ, "plantillas", "stack.md"),
                     encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("Respaldo de datos", texto)

    def test_y_tambien_como_restaurar(self):
        """**Se declara antes del susto, no durante.**"""
        with io.open(os.path.join(RAIZ, "plantillas", "stack.md"),
                     encoding="utf-8") as f:
            self.assertIn("Restaurar un respaldo", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
