# -*- coding: utf-8 -*-
"""`EP-004·HU-024` · Un cero dice sobre qué corrió, o no dice nada.

**El caso que lo hizo falta.** El 2026-08-30 el agente corrió `validar.py
marcas` sobre veinticinco documentos de `documentacion/`, obtuvo cero, y
escribió en el cuerpo de un commit que estaban limpios. El enganche del commit
encontró trece avisos en esos mismos archivos: el cero salía de **no mirar**.

Lo que estas pruebas fijan no es el texto exacto, que se puede reescribir: es
que el alcance **salga de lo que la corrida recorrió** y no de una frase escrita
aparte. Una frase aparte envejece sin avisar, y este defecto nació de creerle a
un número.
"""
import io
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import marcas          # noqa: E402


class ElAlcanceSaleDeLoQueSeRecorrio(unittest.TestCase):

    def _arbol(self, archivos):
        """Un árbol con los archivos que se le pidan: `{ruta: contenido}`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for ruta, cuerpo in archivos.items():
            destino = os.path.join(tmp.name, *ruta.split("/"))
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with io.open(destino, "w", encoding="utf-8", newline="\n") as f:
                f.write(cuerpo)
        return tmp.name

    def test_dice_cuantos_archivos_miro(self):
        raiz = self._arbol({"base/uno.md": u"# Uno\n\nTexto.\n",
                            "plantillas/dos.md": u"# Dos\n\nTexto.\n"})
        marcas.validar(raiz)
        donde, _ = marcas.alcance(raiz, marcas.MIRADOS)
        self.assertIn("2 archivos", donde)

    def test_no_cuenta_los_que_estan_fuera_de_su_alcance(self):
        """**La prueba que importa.** Un archivo de `documentacion/` con una
        marca no se reporta, y el alcance tiene que dejar claro que no se miró:
        ese es exactamente el cero que se leyó como aprobado."""
        raiz = self._arbol({
            "base/uno.md": u"# Uno\n\nTexto limpio.\n",
            "documentacion/tres.md": u"# Tres\n\nUna frase — con raya — acá.\n"})
        hallazgos = marcas.validar(raiz)
        self.assertEqual([], hallazgos, "se reportó algo fuera del alcance")
        donde, _ = marcas.alcance(raiz, marcas.MIRADOS)
        self.assertIn("1 archivos", donde)
        for carpeta in marcas.HEREDADAS:
            self.assertIn(carpeta, donde)
        self.assertNotIn("documentacion", donde)

    def test_el_arbol_sin_nada_que_mirar_lo_dice(self):
        """CA-03: «no encontré nada que revisar» y «no hay marcas» son dos
        respuestas distintas, y las dos imprimían el mismo cero."""
        raiz = self._arbol({"notas/algo.md": u"# Algo\n"})
        marcas.validar(raiz)
        donde, _ = marcas.alcance(raiz, marcas.MIRADOS)
        self.assertIn("no se miró ningún archivo", donde)

    def test_dice_que_partes_no_cuenta(self):
        raiz = self._arbol({"base/uno.md": u"# Uno\n"})
        marcas.validar(raiz)
        _, sin_contar = marcas.alcance(raiz, marcas.MIRADOS)
        self.assertTrue(sin_contar.strip(),
                        "no dice nada de lo que deja sin contar")
        self.assertIn("leer", sin_contar)

    def test_el_alcance_nombra_las_carpetas_que_el_programa_recorre(self):
        """La frase y el recorrido salen del mismo sitio. Si alguien amplía el
        alcance y no toca la frase, esta prueba se cae en vez de dejar que el
        reporte mienta."""
        raiz = self._arbol({"base/uno.md": u"# Uno\n"})
        marcas.validar(raiz)
        donde, _ = marcas.alcance(raiz, marcas.MIRADOS)
        for carpeta in marcas.HEREDADAS:
            self.assertIn(carpeta, donde)


if __name__ == "__main__":
    unittest.main(verbosity=2)
