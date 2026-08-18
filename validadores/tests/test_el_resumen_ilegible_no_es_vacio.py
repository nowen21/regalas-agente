# -*- coding: utf-8 -*-
"""EP-005 · HU-008 · Un resumen escrito fuera del molde no es un resumen vacío.

El molde ([`plantillas/sesion.md`](../../plantillas/sesion.md)) pide `### H-1 ·`
y el programa busca exactamente eso. Tres resúmenes se escribieron como
`### 1 ·` — **29 hallazgos entre los tres** — y para el programa no existía
ninguno.

**Queda mudo por partida doble.** El resumen se cuenta como vacío; y como la
comprobación del cierre necesita encontrar un hallazgo antes de mirar, esa
tampoco corre nunca. Encima el aviso de «sigue vacío» se marca a sí mismo como
ya dado: se ve **una vez** y después calla.

**Y el aviso equivocado es peor que ninguno.** Quien lee «este resumen sigue
vacío» sobre un archivo con quince hallazgos delante concluye que el enganche
se equivocó, y sigue. Los dos casos piden cosas distintas: uno, escribir; el
otro, renumerar lo que ya está escrito.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import resumen   # noqa: E402

CIERRE = u"""
## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
"""


class Resumen(unittest.TestCase):

    def escribir(self, texto):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        ruta = os.path.join(tmp.name, "sesion-1.md")
        with io.open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)
        return ruta


class VacioEIlegibleNoSonLoMismo(Resumen):

    def test_el_que_no_tiene_nada_sigue_diciendo_vacio(self):
        self.assertEqual(["vacio"], resumen.falta(
            self.escribir(u"# Sesión\n\nTodavía nada.\n")))

    def test_el_escrito_sin_la_h_dice_molde_y_no_vacio(self):
        ruta = self.escribir(u"# Sesión\n\n### 1 · Uno\n\ntexto\n\n### 2 · Dos\n\ntexto\n")
        self.assertEqual(["molde"], resumen.falta(ruta))

    def test_dice_cuantos_hay_escritos(self):
        """Para poder decir «renumerar los que ya están», no «escribir»."""
        ruta = self.escribir(u"# Sesión\n\n### 1 · Uno\n\n### 2 · Dos\n\n### 3 · Tres\n")
        self.assertEqual([u"Uno", u"Dos", u"Tres"],
                         resumen.hallazgos_fuera_del_molde(ruta))

    def test_el_que_ya_tiene_los_suyos_no_se_reporta(self):
        """Un resumen correcto puede tener secciones numeradas y no pasa nada.

        La comprobación solo mira cuando **no hay ni un** `H-`: si los hay, el
        molde se está siguiendo y un `### 2 ·` suelto es otra sección.
        """
        ruta = self.escribir(u"# Sesión\n\n### H-1 · Uno\n\n### 2 · Una tabla\n" + CIERRE)
        self.assertEqual([], resumen.hallazgos_fuera_del_molde(ruta))
        self.assertNotIn("molde", resumen.falta(ruta))

    def test_el_aviso_no_se_repite(self):
        ruta = self.escribir(u"# Sesión\n\n### 1 · Uno\n")
        self.assertEqual(["molde"], resumen.falta(ruta))
        resumen.marcar_avisado(ruta, "molde")
        self.assertEqual([], resumen.falta(ruta))

    def test_la_marca_del_molde_no_es_la_del_vacio(self):
        """Marcar uno no puede apagar el otro: son dos avisos distintos."""
        ruta = self.escribir(u"# Sesión\n\nTodavía nada.\n")
        resumen.marcar_avisado(ruta, "molde")
        self.assertEqual(["vacio"], resumen.falta(ruta),
                         "marcar el molde apagó el aviso de vacío")


class LoQueEsteDefectoTapaba(Resumen):
    """La comprobación del cierre no llegaba a correr, y eso no se veía."""

    def test_sin_hallazgos_legibles_el_cierre_nunca_se_mira(self):
        ruta = self.escribir(u"# Sesión\n\n### 1 · Uno\n\n"
                             u"## ¿Se puede cerrar la sesión?\n\n"
                             u"| Para cerrar | Estado |\n|---|---|\n| Algo | ☐ |\n")
        self.assertEqual(["molde"], resumen.falta(ruta),
                         "debería avisar del molde, no del cierre")

    def test_con_la_h_puesta_el_cierre_si_se_mira(self):
        """El mismo archivo, con `H-`: ahora sí llega a mirar el cierre."""
        ruta = self.escribir(u"# Sesión\n\n### H-1 · Uno\n\n"
                             u"## ¿Se puede cerrar la sesión?\n\n"
                             u"| Para cerrar | Estado |\n|---|---|\n| Algo | ☐ |\n")
        self.assertEqual(["cierre"], resumen.falta(ruta))


class ElHistoricoSigueElMolde(unittest.TestCase):
    """Sobre los resúmenes de verdad. Se cae cuando alguien escriba el próximo
    a mano sin la `H-`, que es cuando hace falta que se caiga."""

    def test_ningun_resumen_del_repositorio_queda_ilegible(self):
        raiz = os.path.dirname(VALIDADORES)
        carpeta = os.path.join(raiz, "historico-chat", "resumenes")
        malos = []
        for dirp, _dn, fn in os.walk(carpeta):
            for n in fn:
                if not n.endswith(".md") or n == "README.md":
                    continue
                ruta = os.path.join(dirp, n)
                fuera = resumen.hallazgos_fuera_del_molde(ruta)
                if fuera:
                    malos.append((os.path.relpath(ruta, raiz), len(fuera)))
        self.assertEqual([], malos)


if __name__ == "__main__":
    unittest.main()
