"""El validador de fases y las piezas que comparte con los enganches.

Las de estructura son las de `validadores/pruebas.py` (clase `Fases`), pasadas a
su clase; las demás cubren lo que antes solo se probaba a través de la corrida.
"""
import io
import os
import tempfile
import unittest

from core.comun import AVISO, FALLA
from core.validadores import EstacionDelCommit, EstructuraDeFases, Moldes, Veredictos
from core.validadores.epicas import DOCUMENTOS, Epicas

HU = "documentacion/epicas/EP-001-x/HU-003-y"
CUMPLE = "| **Concepto** | Cumple |\n| **CA cumplidos** | 2 de 2 |\n"


class Arbol(unittest.TestCase):
    """Un proyecto de mentira con el árbol de épicas que haga falta."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.raiz = tmp.name

    def escribir(self, relativa, texto=""):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)
        return ruta

    def fase(self, nombre, hu=HU, **documentos):
        """Una fase con sus cinco documentos; los dados llevan ese texto."""
        self.escribir(hu.rsplit("/", 1)[0] + "/epica.md")
        self.escribir("%s/%s.md" % (hu, hu.rsplit("/", 1)[1]))
        for d in DOCUMENTOS:
            self.escribir("%s/%s/%s" % (hu, nombre, d), documentos.get(d.split(".")[0].replace("-", "_"), ""))
        return os.path.join(self.raiz, *hu.split("/"), nombre)

    def hallazgos(self):
        return EstructuraDeFases(self.raiz).validar()

    def severidades(self):
        return [h.severidad for h in self.hallazgos()]

    def mensajes(self):
        return " | ".join(h.mensaje for h in self.hallazgos())


class LaEstructuraSeRevisa(Arbol):
    """`02·F12` · jerarquía y nombres."""

    def test_la_conforme_no_reporta_y_el_ancho_del_numero_no_importa(self):
        self.fase("A-EP-002-HU-013-x", hu="documentacion/epicas/EP-2-a/HU-13-b")
        self.assertEqual(self.hallazgos(), [])

    def test_la_que_complementa_es_valida(self):
        for nombre in ("A-EP-001-HU-003-uno", "B-EP-001-HU-003-dos", "C-B-EP-001-HU-003-ajuste"):
            self.fase(nombre)
        self.assertEqual(self.hallazgos(), [])

    def test_el_nombre_fuera_de_f12_6_y_la_hu_equivocada_fallan(self):
        self.fase("fase-gz-tipo")
        self.assertEqual(self.severidades(), [FALLA])
        self.assertIn("F12.6", self.mensajes())

    def test_la_fase_guardada_bajo_otra_hu(self):
        self.fase("A-EP-001-HU-009-z")
        self.assertEqual(self.severidades(), [FALLA])
        self.assertIn("F12.3", self.mensajes())

    def test_el_consecutivo_repetido_falla_y_el_hueco_avisa(self):
        self.fase("A-EP-001-HU-003-uno")
        self.fase("A-EP-001-HU-003-otra")
        self.fase("C-EP-001-HU-003-tres")
        self.assertIn("F12.7", self.mensajes())
        self.assertIn("F12.5", self.mensajes())

    def test_dentro_de_una_epica_solo_van_hu_y_los_pendientes_se_saltan(self):
        self.escribir("documentacion/epicas/EP-001-x/epica.md")
        os.makedirs(os.path.join(self.raiz, "documentacion", "epicas", "EP-001-x", "notas-sueltas"))
        os.makedirs(os.path.join(self.raiz, "documentacion", "epicas", "EP-001-x", "pendientes"))
        self.assertEqual(self.severidades(), [FALLA])
        self.assertIn("F12.11", self.mensajes())

    def test_la_hu_sin_fases_solo_avisa_y_sin_epicas_falla(self):
        self.assertEqual(self.severidades(), [FALLA])
        self.escribir("documentacion/epicas/EP-001-x/epica.md")
        self.escribir(HU + "/HU-003-y.md")
        self.assertEqual(self.severidades(), [AVISO])

    def test_el_documento_que_falta_avisa(self):
        ruta = self.fase("A-EP-001-HU-003-uno")
        os.remove(os.path.join(ruta, "plan_pruebas.md"))
        self.assertIn("faltan documentos de la fase (F12.13): plan_pruebas.md", self.mensajes())


class LosDosVeredictosDicenLoMismo(Arbol):
    """`HU-014` · el resultado y el estado no se contradicen."""

    def test_el_concepto_distinto_el_conteo_distinto_y_la_exigencia_en_no(self):
        resultado = ("| **Concepto** | No cumple |\n| **CA cumplidos** | 1 de 2 |\n\n"
                     "## 5. Exigencias\n| Exigencia | Detalle | Cumple |\n|---|---|---|\n| Rapidez | x | No |\n\n## 6. Fin\n")
        self.fase("A-EP-001-HU-003-uno", resultado_pruebas=resultado, estado_fase=CUMPLE)
        mensajes = self.mensajes()
        self.assertIn("los dos veredictos de la fase no coinciden", mensajes)
        self.assertIn("«Rapidez» en No", mensajes)
        self.assertIn("dice 1 de 2 y `estado-fase` dice 2 de 2", mensajes)

    def test_las_formas_del_veredicto_se_leen_y_el_criterio_suelto_no(self):
        for texto, dice in (("**Concepto:** Cumple.", "Cumple"), ("**Concepto: No cumple.**", "No cumple"),
                            ("## 6. Veredicto\n\nCumple\n", "Cumple"),
                            ("## 4. Veredicto por criterio\n\nCumple\n", None)):
            ruta = self.fase("A-EP-001-HU-003-uno", resultado_pruebas=texto)
            self.assertEqual(Veredictos.de_la_fase(ruta), dice, texto)


class LaCuentaDiceTerminadasYCumplidas(Arbol):

    def test_la_fase_con_documentos_vacios_cuenta_terminada_sin_plantillas(self):
        self.fase("A-EP-001-HU-003-uno", resultado_pruebas="**Concepto:** Cumple")
        validador = EstructuraDeFases(self.raiz)
        self.assertEqual((validador.inventario(), validador.por_veredicto()), ((1, 1, 0), (1, 0, 0)))

    def test_el_documento_que_sigue_siendo_el_molde_no_cuenta(self):
        self.escribir("plantillas/ciclo-vida-proyectos/07-plan-trabajo.md", "«uno» «dos» «tres» «cuatro»")
        self.fase("A-EP-001-HU-003-uno", plan_trabajo="«uno» «dos» «tres»")
        validador = EstructuraDeFases(self.raiz)
        self.assertEqual(validador.inventario(), (1, 0, 1))
        self.assertIn("sigue siendo la plantilla: conserva 3", self.mensajes())

    def test_el_rojo_reemplazado_sale_de_la_cuenta_y_el_mal_declarado_avisa(self):
        self.fase("A-EP-001-HU-003-uno", resultado_pruebas="**Concepto:** No cumple")
        self.fase("B-EP-001-HU-003-dos", resultado_pruebas="**Concepto:** Cumple",
                  funcionalidad_implementada="| **Reemplaza el veredicto de** | `A-EP-001-HU-003-uno` |")
        self.assertEqual(EstructuraDeFases(self.raiz).por_veredicto(), (1, 0, 0))
        self.fase("C-EP-001-HU-003-tres", funcionalidad_implementada="| **Reemplaza el veredicto de** | Z-otra |")
        self.assertIn("esa fase no está en esta historia", self.mensajes())

    def test_la_linea_del_inventario_dice_que_es_cada_numero(self):
        self.assertEqual(EstructuraDeFases(self.raiz).linea_inventario(), "")
        self.fase("A-EP-001-HU-003-uno", resultado_pruebas="**Concepto:** Cumple")
        self.assertIn("1 terminadas, de las cuales 1 cumplen", EstructuraDeFases(self.raiz).linea_inventario())


class LosAvisosDelMismoArbol(Arbol):

    def test_el_cierre_nuevo_sin_sello_avisa_y_el_viejo_no(self):
        self.fase("A-EP-001-HU-003-uno", funcionalidad_implementada="| **Fecha de cierre** | 2026-09-01 |")
        self.fase("B-EP-001-HU-003-dos", funcionalidad_implementada="| **Fecha de cierre** | 2026-01-01 |")
        self.assertEqual(self.mensajes().count("no dice bajo qué versión"), 1)

    def test_la_cuenta_escrita_a_mano(self):
        self.escribir("pendientes/inventario.md", "| **Total de HU** | 78 |\n")
        self.fase("A-EP-001-HU-003-uno")
        self.assertIn("guarda la cuenta a mano en el campo **Total de HU**", self.mensajes())

    def test_el_estado_fuera_del_vocabulario_del_glosario(self):
        self.escribir("documentacion/epicas/EP-001-x/epica.md")
        self.escribir(HU + "/HU-003-y.md", "| **Estado** | Finalizada |\n")
        self.assertIn("declara el estado «Finalizada», que el glosario no define", self.mensajes())

    def test_la_fase_detenida_por_el_analisis_de_un_hallazgo(self):
        self.escribir("pendientes/9-algo/pendiente.md")
        self.escribir("pendientes/9-algo/analisis-1.md", "> **Aprobado** el 2026-01-01\n")
        self.escribir("pendientes/9-algo/analisis-2.md", "sin aprobar\n")
        enlace = "[análisis](../../../../../pendientes/9-algo/analisis-1.md)"
        self.fase("A-EP-001-HU-003-uno", plan_trabajo=enlace, estado_fase=CUMPLE)
        self.assertIn("la fase dice «Cumple» y el análisis del hallazgo, `pendientes/9-algo/analisis-2.md`",
                      self.mensajes())

    def test_la_estacion_del_commit_se_cuenta_por_grupo(self):
        fila = "| Estación | Qué | Dónde |\n|---|---|---|\n| 12 | commit | git | |\n"
        self.fase("A-EP-001-HU-003-uno", estado_fase=fila, funcionalidad_implementada="cerrada")
        self.fase("B-EP-001-HU-003-dos", estado_fase=fila)
        self.fase("C-EP-001-HU-003-tres", estado_fase="sin tabla")
        mensajes = self.mensajes()
        self.assertIn("1 fase(s) con su cierre escrito", mensajes)
        self.assertIn("**esto sí es trabajo**: B-EP-001-HU-003-dos", mensajes)
        self.assertIn("1 fase(s) **sin la fila de la estación 12**", mensajes)


class LaEstacionDelCommitSeMarca(Arbol):

    FILA = "| 12 | commit | git | |\n"

    def test_marca_una_vez_y_no_pisa(self):
        marcado = EstacionDelCommit.marcar(self.FILA, "abc1234")
        self.assertIn("✅ `abc1234`", marcado)
        self.assertIsNone(EstacionDelCommit.marcar(marcado, "fff9999"))
        self.assertIsNone(EstacionDelCommit.marcar("sin la fila", "abc1234"))

    def test_reconoce_la_fase_por_su_nombre(self):
        self.assertEqual(EstacionDelCommit.fases_que_toca([HU + "/A-EP-001-HU-003-uno/plan_trabajo.md",
                                                           HU + "/A-EP-001-HU-003-uno/estado-fase.md", "otro.md"]),
                         [HU + "/A-EP-001-HU-003-uno"])

    def test_marca_solo_la_fase_cerrada_en_git_y_escrita(self):
        ruta = self.fase("A-EP-001-HU-003-uno", estado_fase=self.FILA, funcionalidad_implementada="cerrada")
        archivos = [HU + "/A-EP-001-HU-003-uno/estado-fase.md"]
        self.assertEqual(EstacionDelCommit.marcar_las_fases(self.raiz, archivos, "abc1234", lambda _: False), [])
        tocadas = EstacionDelCommit.marcar_las_fases(self.raiz, archivos, "abc1234", lambda _: True)
        self.assertEqual(tocadas, [HU + "/A-EP-001-HU-003-uno"])
        with io.open(os.path.join(ruta, "estado-fase.md"), encoding="utf-8") as f:
            self.assertIn("`abc1234`", f.read())


class ElArbolSeLeeUnaVez(unittest.TestCase):

    def test_los_nombres(self):
        self.assertEqual(Epicas.epica("EP-002-a"), 2)
        self.assertIsNone(Epicas.historia("notas"))
        self.assertEqual(Epicas.fase("C-B-EP-001-HU-003-x")["complementa"], "B")
        self.assertEqual([Epicas.orden_letras(c) for c in ("A", "Z", "AA")], [1, 26, 27])

    def test_sin_plantillas_los_moldes_no_afirman(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(Moldes(tmp))
            self.assertIsNone(Moldes(tmp).sigue_siendo_el_molde(os.path.join(tmp, "plan_trabajo.md")))


if __name__ == "__main__":
    unittest.main()
