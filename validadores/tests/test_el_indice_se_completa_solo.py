# -*- coding: utf-8 -*-
"""`09·14` · La línea del índice que falta se escribe, no solo se reporta.

**El validador la detecta después; nadie la evita antes.** Hoy mismo se olvidó
dos veces el índice de `notas/`, y las dos las cazó `validar.py estandar`
—commits más tarde—, no la mano.

**No regenera el índice entero, y ahí está la decisión.** Las líneas que ya
están llevan una descripción escrita por alguien, que el encabezado del archivo
no tiene. Regenerar cambiaría eso por el título y perdería lo único que hacía
útil el índice.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import indices     # noqa: E402
from comun import RAIZ      # noqa: E402


def carpeta(indice, *archivos):
    """Una carpeta con su `README.md` y los `.md` que se le den."""
    tmp = tempfile.TemporaryDirectory()
    d = os.path.join(tmp.name, "notas")
    os.makedirs(d)
    with io.open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
        f.write(indice)
    for nombre, contenido in archivos:
        with io.open(os.path.join(d, nombre), "w", encoding="utf-8") as f:
            f.write(contenido)
    return tmp


INDICE = u"""# Notas

- [notas/vieja.md](vieja.md) — la que ya estaba, con su descripción cuidada.
"""


class EscribeLoQueFalta(unittest.TestCase):

    def test_ve_el_archivo_sin_su_linea(self):
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"), ("nueva.md", u"# La nueva\n"))
        self.addCleanup(tmp.cleanup)
        self.assertEqual(["nueva.md"],
                         indices.faltantes(os.path.join(tmp.name, "notas")))

    def test_sin_aplicar_no_toca_el_archivo(self):
        """**Ver antes de tocar**, como el resto de los reparadores."""
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"), ("nueva.md", u"# La nueva\n"))
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=False)
        with io.open(os.path.join(tmp.name, "notas", "README.md"), encoding="utf-8") as f:
            self.assertNotIn("nueva.md", f.read())

    def test_con_aplicar_escribe_la_linea(self):
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"), ("nueva.md", u"# La nueva\n"))
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        with io.open(os.path.join(tmp.name, "notas", "README.md"), encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("nueva.md", texto)
        self.assertIn("La nueva", texto)

    def test_usa_el_titulo_del_archivo_no_su_nombre(self):
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"),
                      ("x.md", u"# Cómo se guarda la historia de un valor\n"))
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        with io.open(os.path.join(tmp.name, "notas", "README.md"), encoding="utf-8") as f:
            self.assertIn("Cómo se guarda la historia", f.read())

    def test_el_texto_del_enlace_dice_donde_vive(self):
        """`13·DOC14`: el texto del enlace lleva la ruta desde la raíz."""
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"), ("nueva.md", u"# La nueva\n"))
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        with io.open(os.path.join(tmp.name, "notas", "README.md"), encoding="utf-8") as f:
            self.assertIn("[notas/nueva.md](nueva.md)", f.read())


class NoPisaLoQueYaEstaba(unittest.TestCase):
    """**Es la mitad que importa.** Un generador que regenera destruye trabajo."""

    def test_la_descripcion_cuidada_sobrevive(self):
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"), ("nueva.md", u"# La nueva\n"))
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        with io.open(os.path.join(tmp.name, "notas", "README.md"), encoding="utf-8") as f:
            self.assertIn("con su descripción cuidada", f.read())

    def test_correrlo_dos_veces_no_duplica(self):
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"), ("nueva.md", u"# La nueva\n"))
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        with io.open(os.path.join(tmp.name, "notas", "README.md"), encoding="utf-8") as f:
            self.assertEqual(1, f.read().count("nueva.md]"))

    def test_no_borra_la_linea_de_un_archivo_que_ya_no_esta(self):
        """**Quitar la línea puede ser el error, no el archivo que falta.**"""
        tmp = carpeta(INDICE)          # `vieja.md` no existe
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        with io.open(os.path.join(tmp.name, "notas", "README.md"), encoding="utf-8") as f:
            self.assertIn("vieja.md", f.read())


class LaDescripcionProvisionalSeAvisa(unittest.TestCase):
    """Sin esto, «(por describir)» se queda para siempre."""

    def test_avisa_de_la_linea_sin_afinar(self):
        tmp = carpeta(INDICE, ("vieja.md", u"# Vieja\n"), ("nueva.md", u"# La nueva\n"))
        self.addCleanup(tmp.cleanup)
        indices.completar(tmp.name, carpetas=["notas"], escribir=True)
        self.assertEqual(1, len(indices.validar(tmp.name, carpetas=["notas"])))

    def test_el_estandar_no_tiene_ninguna_sin_afinar(self):
        self.assertEqual([], indices.validar(RAIZ))

    def test_sin_indice_no_revienta(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], indices.completar(tmp.name, carpetas=["notas"]))
        self.assertEqual([], indices.validar(tmp.name, carpetas=["notas"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
