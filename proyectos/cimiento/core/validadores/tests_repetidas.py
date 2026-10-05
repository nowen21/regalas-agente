"""`07·Q4` · `EP-004·HU-026` · La función que hace lo mismo que otra se avisa.

Los casos del plan de pruebas de la fase `A-EP-004-HU-026`.
"""
import io
import os
import subprocess
import tempfile
import time
import unittest

from core.comun import AVISO, Proyecto
from core.validadores.calidad import FuncionesLargas
from core.validadores.codigo import Funciones
from core.validadores.repetidas import Firma, FuncionesRepetidas

LEER = '''
def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            texto = f.read()
    except OSError:
        return ""
    if texto.startswith("\\ufeff"):
        texto = texto[1:]
    return texto.replace("\\r\\n", "\\n")
'''

# La misma lógica con otros nombres y otros textos.
LEER_ARCHIVO = '''
def leer_archivo(camino):
    try:
        with open(camino, encoding="latin-1", errors="ignore") as manejador:
            contenido = manejador.read()
    except OSError:
        return "vacío"
    if contenido.startswith("x"):
        contenido = contenido[1:]
    return contenido.replace("a", "b")
'''

# Mismo nombre, otra cosa.
LEER_OTRO = '''
def _leer(ruta):
    filas = []
    for numero, linea in enumerate(ruta.splitlines(), 1):
        if linea.strip() and not linea.startswith("#"):
            filas.append((numero, linea.split("|")))
    return sorted(filas, key=lambda f: (len(f[1]), f[0]), reverse=True)
'''

CORTA = "\ndef a(x):\n    return x + 1\n"
CORTA_2 = "\ndef b(y):\n    return y + 1\n"

PHP = '''<?php
class A {
    public function total($items) {
        $suma = 0;
        foreach ($items as $item) {
            if ($item->activo) { $suma += $item->precio * $item->cantidad; }
        }
        return round($suma, 2);
    }
}
'''
PHP_COPIA = PHP.replace("class A", "class B").replace("total", "sumar").replace("$items", "$lineas").replace(
    "$item", "$linea").replace("$suma", "$acumulado")


class Repo(unittest.TestCase):
    """Un repositorio git de mentira con los archivos versionados que haga falta."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.raiz = os.path.realpath(tmp.name)
        for orden in (("init", "-q"), ("config", "user.email", "p@e"), ("config", "user.name", "P")):
            self.git(*orden)

    def git(self, *argumentos):
        subprocess.run(("git", "-C", self.raiz) + argumentos, capture_output=True, check=True)

    def escribir(self, relativa, texto, preparar=True):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        if preparar:
            self.git("add", relativa)

    def commitear(self):
        self.git("commit", "-q", "-m", "base", "--no-verify")

    def avisos(self, **kw):
        return FuncionesRepetidas(self.raiz, **kw).validar()


class CP001LaSeparacionVivaUnaSolaVez(unittest.TestCase):

    def test_las_dos_formas_y_el_largo_de_07q3(self):
        texto = "function f($a) {\n  return $a;\n}\n" + LEER
        funciones = Funciones.de(texto)
        self.assertEqual([(n, f) for n, _, _, f in funciones], [("f", "llaves"), ("_leer", "sangria")])
        self.assertEqual(Funciones.largo(funciones[0][2], funciones[0][3]), 1)

    def test_calidad_sigue_avisando_lo_mismo(self):
        larga = "def larga():\n" + "".join("    x%d = %d\n" % (i, i) for i in range(70))
        validador = FuncionesLargas(tempfile.gettempdir())
        self.assertEqual([h.linea for h in validador.revisar_texto(larga, "a.py")], [1])


class CP002LaCopiaConOtrosNombresSeAvisa(Repo):

    def test_python_y_php(self):
        self.escribir("a.py", LEER)
        self.escribir("b.py", LEER_ARCHIVO)
        self.escribir("x.php", PHP)
        self.escribir("y.php", PHP_COPIA)
        avisos = self.avisos()
        self.assertEqual(sorted(os.path.basename(h.archivo) for h in avisos), ["b.py", "y.php"])
        self.assertTrue(all(h.severidad == AVISO and "07·Q4" in h.mensaje for h in avisos))
        self.assertIn("`_leer` (a.py:2)", [h.mensaje for h in avisos if h.archivo.endswith("b.py")][0])

    def test_ocho_copias_son_siete_avisos_y_nombran_la_primera(self):
        for i in range(8):
            self.escribir("m%d.py" % i, LEER)
        avisos = self.avisos()
        self.assertEqual(len(avisos), 7)
        self.assertTrue(all("(m0.py:2) y 6 copia(s) más" in h.mensaje for h in avisos))


class CP003LoQueNoEsCopiaNoSeAvisa(Repo):

    def test_mismo_nombre_otro_cuerpo_y_las_cortas(self):
        self.escribir("a.py", LEER)
        self.escribir("b.py", LEER_OTRO)
        self.escribir("c.py", CORTA)
        self.escribir("d.py", CORTA_2)
        self.assertEqual(self.avisos(), [])

    def test_la_normalizacion_iguala_nombres_y_textos(self):
        cuerpo_a = Funciones.de(LEER)[0][2]
        cuerpo_b = Funciones.de(LEER_ARCHIVO)[0][2]
        self.assertEqual(Firma.normalizar(cuerpo_a), Firma.normalizar(cuerpo_b))


class CP004AlGuardarSoloLaNueva(Repo):

    def test_avisa_la_nueva_y_no_las_que_ya_estaban(self):
        self.escribir("a.py", LEER)
        self.escribir("b.py", LEER_ARCHIVO)
        self.commitear()
        self.assertEqual(self.avisos(solo_preparados=True), [])
        self.escribir("c.py", LEER.replace("_leer", "abrir"))
        avisos = self.avisos(solo_preparados=True)
        self.assertEqual([os.path.basename(h.archivo) for h in avisos], ["c.py"])
        self.assertIn("(a.py:2)", avisos[0].mensaje)


class CP005EnOtroProyectoYATiempo(unittest.TestCase):

    def test_sobre_cimiento_en_menos_de_30_segundos(self):
        inicio = time.time()
        FuncionesRepetidas(Proyecto.estandar()).validar()
        self.assertLess(time.time() - inicio, 30)

    def test_solo_revisa_el_proyecto_que_se_le_pasa(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(("git", "-C", tmp, "init", "-q"), check=True, capture_output=True)
            for nombre in ("a.py", "b.py"):
                with io.open(os.path.join(tmp, nombre), "w", encoding="utf-8") as f:
                    f.write(LEER)
                subprocess.run(("git", "-C", tmp, "add", nombre), check=True, capture_output=True)
            avisos = FuncionesRepetidas(tmp).validar()
            raiz = os.path.realpath(tmp)
            self.assertEqual(len(avisos), 1)
            self.assertTrue(os.path.realpath(avisos[0].archivo).startswith(raiz))


if __name__ == "__main__":
    unittest.main()
