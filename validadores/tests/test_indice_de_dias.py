# -*- coding: utf-8 -*-
"""Pendiente 32 · La carpeta del día nace con su línea en el índice.

`hook_resumen.py` creaba la carpeta del día y el resumen con el modelo puesto,
y no tocaba ninguno de los dos índices. El del día se arregló antes; el de días
faltaba, y por eso el 2026-08-15 tuvo dos resúmenes que nadie nombraba — y
después el 16 y el 17, con trece más.

**Un resumen que no está en el índice es un resumen que nadie va a abrir.** Es
exactamente el defecto que el resumen existe para arreglar.

Se arregla por los dos lados, como pedía el pendiente: el enganche **escribe**
la línea, y un validador **rompe** si falta. Lo segundo importa tanto como lo
primero — el enganche solo cubre lo que nace de aquí en adelante.
"""
import os
import shutil
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import enlaces    # noqa: E402
import resumen    # noqa: E402

RAIZ = os.path.dirname(VALIDADORES)


class ElEngancheEscribeLaLinea(unittest.TestCase):
    """Lo que nace de aquí en adelante nace dentro del índice."""

    def _proyecto(self, con_indice=True):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name
        dia = os.path.join(raiz, resumen.CARPETA, resumen.RESUMENES)
        os.makedirs(dia)
        if con_indice:
            with open(os.path.join(dia, "README.md"), "w", encoding="utf-8") as f:
                f.write("# Resúmenes\n\n## Días\n\n- [2026-01-01/](2026-01-01/) — algo.\n")
        # La transcripción, que es de donde sale el nombre del resumen.
        with open(os.path.join(raiz, resumen.CARPETA,
                               "2026-03-04-un-tema.md"), "w", encoding="utf-8") as f:
            f.write("# sesión\n")
        # El modelo lo trae el estándar.
        shutil.copy(os.path.join(RAIZ, resumen.MODELO.replace("/", os.sep)),
                    os.path.join(raiz, "sesion.md"))
        return raiz

    def _crear(self, raiz):
        return resumen.crear(raiz, "2026-03-04-un-tema.md", estandar=RAIZ)

    def _indice(self, raiz):
        ruta = os.path.join(raiz, resumen.CARPETA, resumen.RESUMENES, "README.md")
        with open(ruta, encoding="utf-8") as f:
            return f.read()

    def test_el_dia_nuevo_queda_anotado(self):
        raiz = self._proyecto()
        self.assertTrue(self._crear(raiz), "no se creó el resumen")
        self.assertIn("(2026-03-04/)", self._indice(raiz))

    def test_no_pisa_los_dias_que_ya_estaban(self):
        raiz = self._proyecto()
        self._crear(raiz)
        self.assertIn("(2026-01-01/)", self._indice(raiz))

    def test_no_duplica_la_linea_al_correr_dos_veces(self):
        raiz = self._proyecto()
        self._crear(raiz)
        self._crear(raiz)
        self.assertEqual(1, self._indice(raiz).count("(2026-03-04/)"))

    def test_sin_indice_no_se_cae(self):
        """Un proyecto que no lleva índice de días no se ve afectado."""
        raiz = self._proyecto(con_indice=False)
        self.assertTrue(self._crear(raiz), "se cayó por no haber índice")

    def test_el_indice_del_dia_sigue_escribiendose(self):
        """La mitad que ya estaba hecha no se rompió."""
        raiz = self._proyecto()
        ruta = self._crear(raiz)
        with open(os.path.join(os.path.dirname(ruta), "README.md"),
                  encoding="utf-8") as f:
            self.assertIn(os.path.basename(ruta), f.read())


class ElValidadorRompeSiFalta(unittest.TestCase):
    """El enganche solo cubre lo nuevo; esto cubre lo que ya está."""

    def _carpeta(self, dias, listados):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name
        base = os.path.join(raiz, resumen.CARPETA, resumen.RESUMENES)
        for d in dias:
            os.makedirs(os.path.join(base, d))
        lineas = "".join(f"- [{d}/]({d}/) — algo.\n" for d in listados)
        with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
            f.write("# Resúmenes\n\n## Días\n\n" + lineas)
        return raiz

    def test_el_dia_sin_linea_es_falla(self):
        raiz = self._carpeta(["2026-01-01", "2026-01-02"], ["2026-01-01"])
        hallazgos = enlaces.validar_dias_con_resumen(raiz)
        self.assertEqual(1, len(hallazgos))
        self.assertIn("2026-01-02", hallazgos[0].mensaje)
        self.assertEqual("FALLA", hallazgos[0].severidad)

    def test_el_dia_de_mas_es_aviso(self):
        """Se nombra un día cuya carpeta ya no está: se avisa, no se falla."""
        raiz = self._carpeta(["2026-01-01"], ["2026-01-01", "2026-01-09"])
        hallazgos = enlaces.validar_dias_con_resumen(raiz)
        self.assertEqual(1, len(hallazgos))
        self.assertEqual("AVISO", hallazgos[0].severidad)

    def test_todo_al_dia_no_reporta_nada(self):
        raiz = self._carpeta(["2026-01-01", "2026-01-02"],
                             ["2026-01-01", "2026-01-02"])
        self.assertEqual([], enlaces.validar_dias_con_resumen(raiz))

    def test_sin_indice_no_reporta_nada(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], enlaces.validar_dias_con_resumen(tmp.name))

    def test_el_repositorio_de_verdad_esta_al_dia(self):
        """Los diez días de esta casa, incluidos el 16 y el 17 que faltaban."""
        self.assertEqual([], [str(h) for h in
                              enlaces.validar_dias_con_resumen(RAIZ)])


if __name__ == "__main__":
    unittest.main()
