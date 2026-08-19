# -*- coding: utf-8 -*-
"""`61` · El que revisa un proyecto no revisa el estándar creyendo que es él.

**Lo reportó `rni-dp` el 2026-08-18.** Corrió `validar.py secretos` desde la
raíz de su proyecto y le devolvió **10 fallas y 8 avisos** sobre archivos de
`validadores/` — una carpeta que ese proyecto no tiene. Eran los del estándar,
y lo que encontraba eran las **claves falsas puestas a propósito** para
comprobar que el detector detecta.

**La causa no era el recorrido: era el valor por defecto.** `--raiz` caía en
`RAIZ`, que es la carpeta del propio estándar. Correrlo sin `--raiz` desde
cualquier sitio revisaba el estándar y decía que había revisado.

**Y lo grave no es el ruido.** Un detector de secretos que siempre falla deja
de servir para ver lo nuevo, y lo nuevo aquí son credenciales: en ese proyecto
esto bloqueaba el cierre de un pendiente de seguridad, porque la herramienta con
la que se comprobaría no distinguía lo suyo de lo ajeno.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import secretos    # noqa: E402
from comun import FALLA, RAIZ      # noqa: E402

VALIDAR = os.path.join(VALIDADORES, "validar.py")


class LaRaizPorDefectoEsDondeEstaElUsuario(unittest.TestCase):

    def _correr(self, cwd):
        return subprocess.run([sys.executable, VALIDAR, "secretos"],
                              cwd=cwd, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")

    def test_desde_una_carpeta_sin_git_no_revisa_el_estandar(self):
        """**El caso reportado.** Antes salían las fallas del estándar."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        salida = self._correr(tmp.name)
        self.assertNotIn("validadores/tests/", salida.stdout)

    def test_dice_que_no_hay_repositorio_en_vez_de_revisar_otro(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertIn("no hay repositorios git", self._correr(tmp.name).stdout)

    def test_el_ayudante_devuelve_donde_se_esta_parado(self):
        import validar
        self.assertEqual(os.getcwd(), validar.raiz_del_proyecto())

    def test_no_devuelve_la_carpeta_del_estandar(self):
        """Fijado a propósito: es el defecto exacto que se corrigió."""
        import validar
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        antes = os.getcwd()
        os.chdir(tmp.name)
        self.addCleanup(os.chdir, antes)
        self.assertNotEqual(os.path.normcase(RAIZ),
                            os.path.normcase(validar.raiz_del_proyecto()))


class LosDatosDePruebaDelDetectorNoSeReportan(unittest.TestCase):
    """`61` · Lo que existe para probar el detector lo dispara siempre."""

    def test_el_archivo_de_prueba_esta_exento(self):
        self.assertIn("validadores/tests/test_la_clave_no_llega_al_historico.py",
                      secretos.EXENTOS)

    def test_la_exencion_nombra_archivos_no_carpetas(self):
        """**Exceptuar `tests/` entero dejaría ciego al detector** sobre todo lo
        que se escriba ahí mañana, que es el agujero por el que se cuela una
        clave real. Por eso se nombran uno por uno."""
        for e in secretos.EXENTOS:
            self.assertTrue(e.endswith(".py"), e)

    def test_el_estandar_no_se_reporta_a_si_mismo(self):
        hallazgos = [h for h in secretos.validar(RAIZ) if h.severidad == FALLA]
        self.assertEqual([], hallazgos,
                         "el detector reporta el estándar: "
                         + "; ".join(h.mensaje for h in hallazgos))

    def test_una_clave_de_verdad_sigue_saliendo(self):
        """**La exención no puede apagar el detector.** Un archivo que no está
        en la lista y trae una clave se sigue reportando."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        subprocess.run(["git", "init", "-q", tmp.name], capture_output=True)
        ruta = os.path.join(tmp.name, "config.py")
        with io.open(ruta, "w", encoding="utf-8") as f:
            f.write(u'CLAVE = "AKIAIOSFODNN7EXAMPLE"\n')
        subprocess.run(["git", "-C", tmp.name, "add", "-A"], capture_output=True)
        hallazgos = secretos.validar(tmp.name)
        self.assertTrue([h for h in hallazgos if h.severidad == FALLA])


class LosTresValidadoresDelProyectoTienenPuerta(unittest.TestCase):
    """`01` · Un validador escrito y sin subcomando no lo corre nadie.

    **`estructura.py`, `entidades.py` y `cruces.py` existían y no eran
    alcanzables**: el pendiente 01 los daba por «lo que falta construir» y ya
    estaban construidos — lo que faltaba era la puerta.

    Es la tercera vez que este repositorio tropieza con lo mismo: `avisar()`
    escrita y nunca llamada, `metareglas.py` sin subcomando, y estos tres.
    **Una pieza que no se puede correr figura como cobertura y no cubre nada.**
    """

    def _correr(self, subcomando):
        return subprocess.run([sys.executable, VALIDAR, subcomando, "--raiz", RAIZ],
                              capture_output=True, text=True,
                              encoding="utf-8", errors="replace")

    def test_estructura_tiene_su_subcomando(self):
        self.assertEqual(0, self._correr("estructura").returncode)

    def test_entidades_tiene_su_subcomando(self):
        self.assertEqual(0, self._correr("entidades").returncode)

    def test_cruces_tiene_su_subcomando(self):
        self.assertEqual(0, self._correr("cruces").returncode)

    def test_sin_declaracion_no_inventan_nada(self):
        """**Lo que no se declara no se comprueba, y se dice cuál se saltó.**

        Un validador que exige lo que nadie acordó se termina apagando — y
        apagado figura como cubierto, que es peor que no tenerlo.
        """
        for sub in ("estructura", "entidades", "cruces"):
            salida = self._correr(sub).stdout
            self.assertIn("no declara", salida, sub)
            self.assertIn("0 falla(s)", salida, sub)


if __name__ == "__main__":
    unittest.main(verbosity=2)
