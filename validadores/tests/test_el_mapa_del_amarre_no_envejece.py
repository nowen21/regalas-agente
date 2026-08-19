# -*- coding: utf-8 -*-
"""`EP-005 · HU-011 · CA-03` — el mapa del amarre no envejece en silencio.

**Qué protege.** Si mañana el usuario trabaja con otro agente, lo que sobrevive
son las reglas escritas; **lo que las hace cumplir, no**. El mapa dice cuál es
cuál, y **todo mapa escrito a mano envejece**: un archivo nuevo no aparece ahí
hasta que alguien se acuerde.

**El caso que decide es `CP-005`.** Después de clasificar la pieza, la
comprobación tiene que **callarse**. Sin él, `CP-004` pasaría con un programa
que reporta siempre — y uno que reporta siempre se apaga a la semana, que es el
patrón que ya apareció cuatro veces en este repositorio.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import amarre     # noqa: E402
from comun import AVISO, FALLA, RAIZ      # noqa: E402

MAPA = os.path.join(RAIZ, *amarre.MAPA.split(os.sep))


def arbol():
    """Copia del mapa y de `validadores/` en una carpeta temporal."""
    tmp = tempfile.TemporaryDirectory()
    os.makedirs(os.path.join(tmp.name, "anatomia"))
    shutil.copy(MAPA, os.path.join(tmp.name, *amarre.MAPA.split(os.sep)))
    destino = os.path.join(tmp.name, "validadores")
    os.makedirs(destino)
    origen = os.path.join(RAIZ, "validadores")
    for n in os.listdir(origen):
        if n.endswith(".py"):
            shutil.copy(os.path.join(origen, n), os.path.join(destino, n))
    return tmp


class CA01YCA02ElMapaEstaCompleto(unittest.TestCase):

    def test_ninguna_pieza_queda_sin_columna(self):
        """`CP-001` — hoy son 54; el número lo dice el programa, no la prueba."""
        self.assertEqual([], [h for h in amarre.validar(RAIZ)
                              if h.severidad == FALLA])

    def test_el_recuento_del_programa_coincide_con_el_del_mapa(self):
        """`CP-002` · **si difieren, el mapa miente aunque esté completo.**

        Es el riesgo `R-01` del plan: que el programa y el mapa midan distinto y
        nadie lo note. Por eso los dos usan la misma lista de marcas.
        """
        p = amarre.piezas(RAIZ)
        amarradas = sum(1 for n in p.values() if n > 0)
        with io.open(MAPA, encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("%d amarrados de %d" % (amarradas, len(p)), texto)

    def test_las_libres_van_por_su_nombre(self):
        """`CP-001` · **antes iban solo por su total**, y así una pieza nueva
        entraba en el recuento sin que nadie la hubiera mirado."""
        with io.open(MAPA, encoding="utf-8") as f:
            texto = f.read()
        libres = [n for n, c in amarre.piezas(RAIZ).items() if c == 0]
        for n in libres:
            self.assertIn("`%s`" % n, texto, n)

    def test_cada_amarrada_dice_que_se_pierde(self):
        """`CP-003`."""
        with io.open(MAPA, encoding="utf-8") as f:
            texto = f.read()
        for marca in ("el amarre grande", "son la definición de adaptador",
                      "a medias"):
            self.assertIn(marca, texto)


class CA03ElMapaSeQuedaViejoYSeNota(unittest.TestCase):

    def _pieza(self, tmp, nombre, contenido):
        with io.open(os.path.join(tmp.name, "validadores", nombre),
                     "w", encoding="utf-8") as f:
            f.write(contenido)

    def test_una_pieza_nueva_sin_clasificar_se_reporta(self):
        """`CP-004` — el criterio literal de la historia."""
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        self._pieza(tmp, "zzz_prueba.py", u"# usa CLAUDE.md\n")
        hallazgos = [h for h in amarre.validar(tmp.name) if h.severidad == FALLA]
        self.assertTrue(hallazgos)
        self.assertIn("zzz_prueba.py", hallazgos[0].mensaje)

    def test_clasificarla_la_calla(self):
        """`CP-005` · **el que decide.** Sin él, el anterior pasaría con un
        programa que reporta siempre — y uno que reporta siempre se apaga."""
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        self._pieza(tmp, "zzz_prueba.py", u"# usa CLAUDE.md\n")
        ruta = os.path.join(tmp.name, *amarre.MAPA.split(os.sep))
        with io.open(ruta, "a", encoding="utf-8") as f:
            f.write(u"\n\n`zzz_prueba.py` — clasificada.\n")
        self.assertEqual([], [h for h in amarre.validar(tmp.name)
                              if h.severidad == FALLA])

    def test_una_pieza_que_el_mapa_nombra_y_ya_no_existe_se_reporta(self):
        """`CP-006` · **el mapa envejece por los dos lados**, y la historia solo
        nombra uno. Uno que promete clasificar algo que no está miente igual."""
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        os.remove(os.path.join(tmp.name, "validadores", "citas.py"))
        hallazgos = [h for h in amarre.validar(tmp.name) if h.severidad == AVISO]
        self.assertTrue([h for h in hallazgos if "citas.py" in h.mensaje])

    def test_la_que_no_toca_la_herramienta_tambien_tiene_que_estar(self):
        """Una pieza **libre** sin clasificar también se reporta: el mapa
        clasifica las 54, no solo las amarradas."""
        tmp = arbol()
        self.addCleanup(tmp.cleanup)
        self._pieza(tmp, "zzz_libre.py", u"# solo lee archivos\n")
        self.assertTrue([h for h in amarre.validar(tmp.name)
                         if "zzz_libre.py" in h.mensaje])


class Bordes(unittest.TestCase):

    def test_sin_mapa_se_reporta_y_no_revienta(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        hallazgos = amarre.validar(tmp.name)
        self.assertEqual(1, len(hallazgos))
        self.assertEqual(FALLA, hallazgos[0].severidad)

    def test_el_propio_medidor_no_se_reporta_a_si_mismo(self):
        """**Nombra la herramienta porque la mide.** Exceptuarlo por nombre, como
        los datos de prueba del detector de secretos: lo que existe para hablar
        de algo no es una instancia de ese algo."""
        self.assertNotIn("amarre.py", amarre.piezas(RAIZ))

    def test_el_resumen_dice_los_tres_numeros(self):
        linea = amarre.linea_resumen(RAIZ)
        for palabra in ("Piezas", "amarradas", "libres"):
            self.assertIn(palabra, linea)

    def test_no_es_punto_de_entrada(self):
        with io.open(os.path.join(VALIDADORES, "amarre.py"),
                     encoding="utf-8") as f:
            self.assertIn("no_es_punto_de_entrada", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
