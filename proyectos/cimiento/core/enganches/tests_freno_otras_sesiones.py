"""`EP-023·HU-009` · El freno no detiene lo que hizo otra sesión ni lo que lee mal de una orden.

Plan de pruebas: `PP-EP023-HU009-A`.
"""
import io
import json
import os
import shutil
import tempfile
import time
import unittest

from .freno import OTRA_SESION_SEGUNDOS, Freno


def escribir(ruta, texto, hace=0):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    if hace:
        cuando = time.time() - hace
        os.utime(ruta, (cuando, cuando))


def linea_de_escritura(ruta):
    """Una línea de transcripción de Claude Code con una escritura, como la guarda él."""
    return json.dumps({"type": "assistant", "message": {"content": [
        {"type": "tool_use", "name": "Edit", "input": {"file_path": ruta}}]}}) + "\n"


class ConDosSesiones(unittest.TestCase):
    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        self.carpeta = os.path.join(self.raiz, "transcripciones")
        self.propia = os.path.join(self.carpeta, "propia.jsonl")
        escribir(self.propia, "")

    def freno(self):
        return Freno(self.raiz, niveles=object(), transcripcion_cc=self.propia)


class CP001OtraSesionActivaEscribioElArchivo(ConDosSesiones):
    def test_no_se_le_carga_a_esta(self):
        escribir(os.path.join(self.carpeta, "otra.jsonl"),
                 linea_de_escritura("C:\\Ing. Jose\\proyecto\\.gitignore"))
        self.assertTrue(self.freno().de_otra_sesion(".gitignore"))


class CP002NadieMasLoNombra(ConDosSesiones):
    def test_ninguna_otra_lo_nombra(self):
        escribir(os.path.join(self.carpeta, "otra.jsonl"), linea_de_escritura("C:/otro/archivo.md"))
        self.assertFalse(self.freno().de_otra_sesion(".gitignore"))

    def test_la_otra_es_vieja(self):
        escribir(os.path.join(self.carpeta, "otra.jsonl"), linea_de_escritura("C:/p/.gitignore"),
                 hace=OTRA_SESION_SEGUNDOS + 60)
        self.assertFalse(self.freno().de_otra_sesion(".gitignore"))

    def test_solo_la_propia_lo_nombra(self):
        escribir(self.propia, linea_de_escritura("C:/p/.gitignore"))
        self.assertFalse(self.freno().de_otra_sesion(".gitignore"))

    def test_sin_transcripcion_propia(self):
        escribir(os.path.join(self.carpeta, "otra.jsonl"), linea_de_escritura("C:/p/.gitignore"))
        self.assertFalse(Freno(self.raiz, niveles=object()).de_otra_sesion(".gitignore"))


class CP003LaTablaDentroDeUnSed(unittest.TestCase):
    def test_solo_el_archivo_del_final(self):
        orden = "sed -i 's/^| a | vuelve después de un resumen | b |$/| c |/' x.md"
        self.assertEqual(["x.md"], Freno.destinos(orden))

    def test_partes_no_corta_dentro_de_comillas(self):
        self.assertEqual(["sed -i 's/a | b; c/d/' x.md"], Freno.partes("sed -i 's/a | b; c/d/' x.md"))


class CP004LosSeparadoresDeFuera(unittest.TestCase):
    def test_se_siguen_partiendo(self):
        orden = 'rm a.txt; touch b.txt && echo "x;y" | tee c.txt'
        destinos = Freno.destinos(orden)
        self.assertEqual({"a.txt", "b.txt", "c.txt"}, set(destinos))

    def test_doble_barra(self):
        self.assertEqual(["true", "rm z.txt"], Freno.partes("true || rm z.txt"))


if __name__ == "__main__":
    unittest.main()
