# -*- coding: utf-8 -*-
"""`EP-025·HU-024`: el aviso del freno dice cómo salir, el freno lee el análisis
de su propia sesión y resuelve las rutas después del `cd` de una orden.

Sin Django: corren desde `proyectos/cimiento/` importando `core.validadores`
primero, como `tests_freno`.
"""
import io
import os
import shutil
import tempfile
import unittest

from .freno import Freno
from .niveles import BaseSinRespuesta


class SinBase:
    """Niveles de mentira: ninguna regla cambiada, y sin base para la dirección."""

    def todos(self):
        return {}

    def consultar(self, *args, **kwargs):
        raise BaseSinRespuesta("sin base")


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _analisis(numero, ruta_de_una):
    return ("# Análisis 1\n\n## Conversación\n\n> acá termina la conversación\n\n"
            "## Lo que se tiene que hacer\n\n| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n"
            "|---|---|---|---|\n| 2 | Escribir el archivo | 1 | Este análisis, de una y sin fase: `%s` |\n" % ruta_de_una)


class ConDosSesiones(unittest.TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        for letra, numero in (("a", 7), ("b", 8)):
            transcripcion = os.path.join(self.raiz, "historico-chat", "2026-10-05-%s.md" % letra)
            _escribir(transcripcion, "<!-- sesion: s-%s -->\n\n# Sesión\n\n### 1 · Usuario, 10:00\n\nhola\n" % letra)
            carpeta = os.path.join(self.raiz, "pendientes", "%d-algo" % numero)
            _escribir(os.path.join(carpeta, "pendiente.md"), "# Pendiente %d\n" % numero)
            _escribir(os.path.join(carpeta, "analisis-1.md"), _analisis(numero, "nuevo/%s.py" % letra))
            from .analisis_en_curso import AnalisisEnCurso
            self.assertTrue(AnalisisEnCurso(self.raiz, transcripcion, base=False).prender(numero, transcripcion, 1)[0])

    def freno(self, sesion=""):
        return Freno(self.raiz, niveles=SinBase(), sesion=sesion)

    def escribir(self, freno, archivo):
        return freno.revisar("Write", {"file_path": os.path.join(self.raiz, "nuevo", archivo)})[0]


class ElAnalisisDeLaPropiaSesion(ConDosSesiones):
    """CP-002."""

    def test_cada_sesion_ve_su_analisis(self):
        self.assertEqual("deja", self.escribir(self.freno("s-a"), "a.py"))
        self.assertEqual("detiene", self.escribir(self.freno("s-a"), "b.py"))
        self.assertEqual("deja", self.escribir(self.freno("s-b"), "b.py"))
        self.assertEqual("detiene", self.escribir(self.freno("s-b"), "a.py"))

    def test_el_archivo_nuevo_que_nombra_el_analisis_pasa(self):
        self.assertFalse(os.path.exists(os.path.join(self.raiz, "nuevo", "a.py")))
        self.assertEqual({"nuevo/a.py"}, self.freno("s-a").de_una())

    def test_la_transcripcion_se_halla_por_la_primera_linea(self):
        self.assertTrue(self.freno().transcripcion_de("s-b").endswith("2026-10-05-b.md"))
        self.assertEqual("", self.freno().transcripcion_de("s-z"))


class ElAvisoDiceLaSalida(ConDosSesiones):
    """CP-001."""

    def test_la_salida_nombra_las_contrarias_y_la_suspension(self):
        salida = self.freno("s-a").salida("el plan no lo declara (02·F8)")
        for pedazo in ("andamio.py quitar", "cerrar.py reabrir", "reabrir_fase", "--desinstalar",
                       "suspender `02·F8`", "Suspensiones"):
            self.assertIn(pedazo, salida)

    def test_el_nucleo_no_se_suspende(self):
        salida = self.freno().salida("una clave quedaría escrita (00·N6)")
        self.assertIn("es del núcleo y no se suspende", salida)
        self.assertNotIn("suspender `00·N6`", salida)

    def test_el_aviso_la_trae(self):
        aviso = Freno.aviso("el plan no lo declara (02·F8)", "x.py", False, False, "Cómo salir: algo.")
        self.assertTrue(aviso.endswith("\nCómo salir: algo."))
        self.assertNotIn("Cómo salir", Freno.aviso("el plan no lo declara (02·F8)", "x.py", False))


class ElCdDeUnaOrden(ConDosSesiones):
    """CP-003."""

    def test_rm_despues_del_cd(self):
        sub = os.path.join(self.raiz, "sub")
        os.makedirs(sub)
        self.assertEqual([("x.txt", os.path.realpath(sub))],
                         Freno.destinos_con_carpeta("cd sub && rm x.txt", self.raiz))
        decision, _porque, ruta = self.freno("s-a").revisar("Bash", {"command": "cd sub && rm x.txt"}, self.raiz)
        self.assertEqual(("detiene", "sub/x.txt"), (decision, ruta))

    def test_cd_a_otra_carpeta_y_volver(self):
        sub = os.path.join(self.raiz, "sub")
        os.makedirs(os.path.join(sub, "hondo"))
        destinos = Freno.destinos_con_carpeta('cd "%s" && cd hondo && cd .. && touch y.txt' % sub, self.raiz)
        self.assertEqual([("y.txt", os.path.realpath(sub))], destinos)

    def test_el_archivo_que_el_analisis_nombra_pasa_despues_del_cd(self):
        os.makedirs(os.path.join(self.raiz, "nuevo"))
        orden = "cd nuevo && touch a.py"
        self.assertEqual("deja", self.freno("s-a").revisar("Bash", {"command": orden}, self.raiz)[0])

    def test_lo_que_va_entre_comillas_no_se_parte(self):
        """H-10 · Un `v>0` dentro del código de `python -c "…"` no es una redirección."""
        orden = 'cd sub && python -c "\nimport x\nprint(sum(1 for v in p if v>0), len(p))\n"'
        os.makedirs(os.path.join(self.raiz, "sub"))
        self.assertEqual([], Freno.destinos_con_carpeta(orden, self.raiz))
        self.assertEqual(["cd sub", 'python -c "\nimport x\nprint(sum(1 for v in p if v>0), len(p))\n"'],
                         Freno.partes_fuera_de_comillas(orden))
        self.assertEqual("deja", self.freno("s-a").revisar("Bash", {"command": orden}, self.raiz)[0])

    def test_sin_cd_como_antes(self):
        self.assertEqual([("z.txt", self.raiz)], Freno.destinos_con_carpeta('echo "a; b" > z.txt', self.raiz))


if __name__ == "__main__":
    unittest.main()
