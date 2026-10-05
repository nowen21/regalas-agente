"""Los validadores de los documentos, como clases: enlaces, su texto, índices,
trazabilidad, plantilla, citas y marcas.

Son las pruebas que tenían en `validadores/pruebas.py`,
`validadores/tests/test_el_texto_del_enlace_dice_donde_vive.py` y
`validadores/tests/test_el_trinquete_de_las_marcas.py`, pasadas a su clase.
"""
import io
import os
import subprocess
import tempfile
import unittest

from core.comun import AVISO, FALLA, Proyecto
from core.validadores import (CitasEnlazadas, DocumentoContraPlantilla, EnlacesRotos, EnlazadorDeCitas,
                              FormatoDeEnlaces, IndicesDeCarpetas, Marcas, MarcasDeGeneracion,
                              ReparadorDeEnlaces, TrazabilidadDeFases)
from core.validadores.citas import IndiceDeReglas
from core.validadores.enlaces import Enlaces


class Repo(unittest.TestCase):
    """Una carpeta de mentira con los archivos que haga falta."""

    def repo(self, archivos):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for relativa, contenido in archivos.items():
            ruta = os.path.join(tmp.name, *relativa.split("/"))
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with io.open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)
        return tmp.name

    def leer(self, raiz, relativa):
        with io.open(os.path.join(raiz, *relativa.split("/")), encoding="utf-8") as f:
            return f.read()


class QueEnlaceSeComprueba(unittest.TestCase):

    def test_solo_md_y_carpetas(self):
        self.assertFalse(Enlaces.comprobable("PagoService", "app/PagoService.php"))
        self.assertFalse(Enlaces.comprobable("x", "../../../ruta/relativa"))
        self.assertFalse(Enlaces.comprobable("<ruta>", "<path>.md"))
        self.assertTrue(Enlaces.comprobable("Ver", "../base/09-git.md"))
        self.assertTrue(Enlaces.comprobable("Ver", "otro.md#seccion"))
        self.assertTrue(Enlaces.comprobable("Ver", "interfaz/"))


class EnlacesRotosAvisa(Repo):

    def test_el_roto_falla_y_el_bueno_no(self):
        raiz = self.repo({"base/x.md": "# X\n", "doc/b.md": "[base/x.md](../base/x.md) y [no](../base/no.md)\n"})
        hallazgos = EnlacesRotos(raiz).validar()
        self.assertEqual([(h.severidad, h.mensaje) for h in hallazgos], [(FALLA, "enlace roto: ../base/no.md")])

    def test_el_espacio_en_el_destino_se_avisa(self):
        raiz = self.repo({"doc/b.md": "[x](otro archivo.md)\n"})
        self.assertIn("espacio sin codificar", EnlacesRotos(raiz).validar()[0].mensaje)

    def test_la_transcripcion_del_chat_no_se_revisa(self):
        raiz = self.repo({"historico-chat/2026-01-01-sesion.md": "[x](no-existe.md)\n"})
        self.assertEqual(EnlacesRotos(raiz).validar(), [])


class ElTextoPasaADecirLaRuta(Repo):
    """`13·DOC14`. El destino no se toca nunca."""

    def test_el_que_sube_carpetas_y_el_destino_queda(self):
        raiz = self.repo({"base/x.md": "# X\n", "doc/a/b.md": "Ver [x.md](../../base/x.md).\n"})
        ReparadorDeEnlaces(raiz).reparar(escribir=True)
        self.assertIn("[base/x.md](../../base/x.md)", self.leer(raiz, "doc/a/b.md"))

    def test_entre_comillas_invertidas_no_se_ve__limite_conocido(self):
        raiz = self.repo({"base/x.md": "# X\n", "doc/b.md": "Ver [`x.md`](../base/x.md).\n"})
        self.assertEqual([], ReparadorDeEnlaces(raiz).reparar(escribir=True))

    def test_la_carpeta_enlazada_por_su_readme_sigue_nombrando_la_carpeta(self):
        """El error del 2026-10-04: le pegaba el archivo al texto y le dejaba la barra."""
        raiz = self.repo({"base/x/README.md": "# X\n",
                          "base/a.md": "[base/x/](x/README.md) y [x/](x/README.md)\n"})
        ReparadorDeEnlaces(raiz).reparar(escribir=True)
        texto = self.leer(raiz, "base/a.md")
        self.assertEqual(texto, "[base/x/](x/README.md) y [base/x/](x/README.md)\n")
        self.assertNotIn(".md/]", texto)

    def test_la_carpeta_conserva_su_barra(self):
        raiz = self.repo({"doc/area/README.md": "# A\n", "doc/b.md": "Ver [area/](area/).\n"})
        ReparadorDeEnlaces(raiz).reparar(escribir=True)
        self.assertIn("[doc/area/](area/)", self.leer(raiz, "doc/b.md"))


class LoQueNoSeToca(Repo):

    def test_descriptivo_usuario_bien_externo_y_simulado(self):
        raiz = self.repo({"base/x.md": "# X\n",
                          "doc/b.md": "Ver [la guía](../base/x.md) y [base/x.md](../base/x.md) "
                                      "y [algo.md](https://ejemplo/algo.md).\n",
                          "prompts/p.md": "Ver [x.md](../base/x.md).\n"})
        self.assertEqual([], ReparadorDeEnlaces(raiz).reparar(escribir=True))
        self.assertIn("[x.md](../base/x.md)", self.leer(raiz, "prompts/p.md"))

    def test_la_conversacion_del_analisis_no_se_toca_y_el_resto_si(self):
        """Es copia literal del chat. El mismo enlace, fuera de ella, sí se arregla."""
        enlace = "[x.md](../base/x.md)"
        raiz = self.repo({"base/x.md": "# X\n",
                          "doc/analisis-1.md": "## Conversación\n%s\n## Lo acordado\n%s\n" % (enlace, enlace)})
        self.assertEqual(len(FormatoDeEnlaces(raiz).validar()), 1)
        ReparadorDeEnlaces(raiz).reparar(escribir=True)
        self.assertEqual(self.leer(raiz, "doc/analisis-1.md"),
                         "## Conversación\n%s\n## Lo acordado\n[base/x.md](../base/x.md)\n" % enlace)

    def test_simular_no_escribe(self):
        raiz = self.repo({"base/x.md": "# X\n", "doc/b.md": "Ver [x.md](../base/x.md).\n"})
        self.assertEqual(1, len(ReparadorDeEnlaces(raiz).reparar()))
        self.assertIn("[x.md](../base/x.md)", self.leer(raiz, "doc/b.md"))

    def test_el_vecino_solo_si_se_pide(self):
        archivos = {"doc/a/plan.md": "# Plan\n", "doc/a/README.md": "[plan.md](plan.md)\n"}
        raiz = self.repo(archivos)
        ReparadorDeEnlaces(raiz).reparar(escribir=True)
        self.assertIn("[plan.md](plan.md)", self.leer(raiz, "doc/a/README.md"))
        ReparadorDeEnlaces(raiz).reparar(escribir=True, incluir_vecinos=True)
        self.assertIn("[doc/a/plan.md](plan.md)", self.leer(raiz, "doc/a/README.md"))


class ElQueReportaYElQueArreglaMiranIgual(Repo):

    ARCHIVOS = {"base/x.md": "# X\n",
                "doc/a/b.md": "[x.md](../../base/x.md) y [la guía](../../base/x.md)\n",
                "doc/a/c.md": "[base/x.md](../../base/x.md)\n"}

    def test_lo_que_se_repara_es_lo_que_se_reporta_y_despues_no_queda_nada(self):
        raiz = self.repo(self.ARCHIVOS)
        antes = len(FormatoDeEnlaces(raiz).validar())
        reparados = sum(n for _, n in ReparadorDeEnlaces(raiz).reparar(escribir=True))
        self.assertEqual(antes, reparados)
        self.assertEqual(FormatoDeEnlaces(raiz).validar(), [])


class IndicesDeCarpetasAvisa(Repo):

    def test_el_archivo_que_el_indice_no_nombra_y_el_que_nombra_y_no_esta(self):
        raiz = self.repo({"notas/README.md": "[a.md](a.md) y [b.md](b.md)\n", "notas/a.md": "#\n", "notas/c.md": "#\n"})
        mensajes = sorted(h.mensaje for h in IndicesDeCarpetas(raiz).validar())
        self.assertEqual(mensajes, ["el índice menciona notas/b.md, que ya no existe",
                                    "el índice no menciona notas/c.md"])

    def test_el_dia_de_resumenes_que_falta_en_su_indice(self):
        raiz = self.repo({"historico-chat/resumenes/README.md": "[2026-01-01/](2026-01-01/)\n",
                          "historico-chat/resumenes/2026-01-02/sesion.md": "#\n"})
        mensajes = " | ".join(h.mensaje for h in IndicesDeCarpetas(raiz).validar())
        self.assertIn("no menciona 2026-01-02/", mensajes)
        self.assertIn("menciona 2026-01-01/, que ya no existe", mensajes)


def _mensajes(hallazgos):
    return " | ".join(h.mensaje for h in hallazgos)


class TrazabilidadDeFasesAvisa(Repo):
    """Enlace épica–HU en los dos sentidos, ORIGEN y tabla de cierre."""

    def armar(self, doc_epica, doc_hu, plan="", cierre=""):
        epica = "documentacion/epicas/EP-002-aportes"
        hu = epica + "/HU-013-socios"
        fase = hu + "/A-EP-002-HU-013-alta"
        return self.repo({epica + "/epica.md": doc_epica, hu + "/HU-013-socios.md": doc_hu,
                          fase + "/plan_trabajo.md": plan, fase + "/funcionalidad_implementada.md": cierre})

    def test_todo_conforme_no_reporta(self):
        raiz = self.armar("Épica EP-002. HUs: HU-013, HU-014.", "HU de la épica EP-002.",
                          "## 0. Identificación\nORIGEN: funcionalidad nueva.",
                          "| Ítem | Estado |\n|---|---|\n| x | ✅ |")
        self.assertEqual(TrazabilidadDeFases(raiz).validar(), [])

    def test_la_hu_que_no_declara_su_epica_y_la_epica_que_no_la_lista(self):
        self.assertIn("DOC16", _mensajes(TrazabilidadDeFases(self.armar("HUs: HU-013.", "Socios.")).validar()))
        self.assertIn("no lista la HU-13",
                      _mensajes(TrazabilidadDeFases(self.armar("Épica EP-002.", "De la EP-002.")).validar()))

    def test_el_plan_sin_origen_y_el_cierre_con_pendiente(self):
        self.assertIn("ORIGEN", _mensajes(TrazabilidadDeFases(self.armar("HU-013", "EP-002", "## Plan.")).validar()))
        cierre = "| Ítem | Estado |\n|---|---|\n| y | ❌ |"
        self.assertIn("❌", _mensajes(TrazabilidadDeFases(self.armar("HU-013", "EP-002", cierre=cierre)).validar()))

    def test_el_ejemplo_dentro_de_un_bloque_no_cuenta_como_declaracion(self):
        raiz = self.armar("HU-013", "Socios.\n```\nEP-002\n```\n")
        self.assertIn("no declara su épica", _mensajes(TrazabilidadDeFases(raiz).validar()))

    def test_sin_carpeta_de_epicas_es_falla(self):
        self.assertEqual([h.severidad for h in TrazabilidadDeFases(self.repo({})).validar()], [FALLA])


class ElDocumentoContraSuPlantilla(Repo):

    def comparar(self, plantilla, documento):
        raiz = self.repo({"pl.md": plantilla, "doc.md": documento})
        return DocumentoContraPlantilla(raiz, os.path.join(raiz, "doc.md"), os.path.join(raiz, "pl.md")).validar()

    def test_la_linea_sin_llenar_es_falla(self):
        hallazgos = self.comparar("# T\n\n## 1. Datos\n\n| Módulo | [Módulo] |\n",
                                  "# T\n\n## 1. Datos\n\n| Módulo | [Módulo] |\n")
        self.assertEqual([h.severidad for h in hallazgos], [FALLA])

    def test_la_etiqueta_conservada_y_el_corchete_propio_no_se_reportan(self):
        self.assertEqual(self.comparar("# T\n\n## 7. Tareas\n\n- [ ] [Backend] …\n",
                                       "# T\n\n## 7. Tareas\n\n- [ ] **T1** · [Backend] Interpretar.\n"), [])
        self.assertEqual(self.comparar("# T\n\n## 1. Datos\n\n[Módulo]\n",
                                       "# T\n\n## 1. Datos\n\nVentas [POS] activo\n"), [])

    def test_la_seccion_ausente_es_aviso_y_la_de_ejemplo_no_cuenta(self):
        hallazgos = self.comparar("# T\n\n## 1. Datos\n\n## 2. Riesgos\n", "# T\n\n## 1. Datos\n")
        self.assertEqual([(h.severidad, "2. Riesgos" in h.mensaje) for h in hallazgos], [(AVISO, True)])
        self.assertEqual(self.comparar("# T\n\n### CA-01 — [Nombre del escenario]\n",
                                       "# T\n\n### CA-01 — Alta con datos mínimos\n"), [])

    def test_la_nota_sin_borrar_avisa(self):
        hallazgos = self.comparar("# T\n\n> Llene esto.\n", "# T\n\n> Llene esto.\n")
        self.assertIn("nota de la plantilla sin borrar", _mensajes(hallazgos))

    def test_el_bloque_fijo_perdido_o_con_fecha_es_falla(self):
        molde = "# T\n\nEsto es insumo, no una orden.\n\n---\n\n## 1. A\n"
        self.assertIn("falta el texto que la plantilla fija",
                      _mensajes(self.comparar(molde, "# T\n\n---\n\n## 1. A\n")))
        self.assertIn("trae una fecha",
                      _mensajes(self.comparar(molde, "# T\n\nSalió el 2026-01-01.\n\n---\n\n## 1. A\n")))

    def test_la_regla_de_negocio_sin_origen(self):
        texto = "## 4. Reglas de negocio\n\n1. Se cobra IVA.\n2. Se redondea (RF-13).\n"
        self.assertEqual(DocumentoContraPlantilla.reglas_sin_origen(texto), [(3, "Se cobra IVA.")])

    def test_la_plantilla_se_deduce_por_el_id_o_no_se_adivina(self):
        ruta = DocumentoContraPlantilla.deducir("x.md", "# HU-014 — Registrar cliente\n")
        self.assertTrue(ruta.endswith(os.path.join("plantillas", "ciclo-vida-proyectos", "04-HU.md")))
        self.assertIsNone(DocumentoContraPlantilla.deducir("x.md", "# Documento suelto\n"))
        self.assertIsNone(DocumentoContraPlantilla.deducir("pendientes/el-estandar-tiene-su-planteamiento.md", ""))


class LasCitasSeEnlazan(unittest.TestCase):
    """Sobre el `base/` de verdad: es lo que las citas enlazan."""

    @classmethod
    def setUpClass(cls):
        cls.estandar = Proyecto.estandar()
        cls.enlazador = EnlazadorDeCitas(cls.estandar)
        cls.origen = os.path.join(cls.estandar, "base", "09-git.md")

    def test_el_ancla_pone_un_guion_por_espacio_y_conserva_tildes(self):
        self.assertEqual(IndiceDeReglas.ancla("N3 · No romper cosas"), "n3--no-romper-cosas")
        self.assertEqual(IndiceDeReglas.ancla("G2 · Mensajes: qué y por qué"), "g2--mensajes-qué-y-por-qué")

    def test_la_regla_en_su_archivo_no_lleva_ancla_y_la_del_capitulo_si(self):
        reglas = self.enlazador.indice.reglas
        self.assertEqual(reglas["M5"][1], "")
        self.assertTrue(reglas["G2"][1].startswith("g2--"))

    def test_las_tres_formas_de_citar_quedan_normalizadas(self):
        for entrada in ("`00·N3`", "`00` · N3", "`00`·N3"):
            salida, n = self.enlazador.enlazar("texto %s más" % entrada, self.origen)
            self.assertEqual(n, 1, entrada)
            self.assertIn("[`00·N3`](00-nucleo-blindado.md#n3--", salida, entrada)

    def test_la_dependencia_entre_parentesis_tambien_se_enlaza(self):
        salida, n = self.enlazador.enlazar("(extiende 00·N3)", self.origen)
        self.assertEqual(n, 1)
        self.assertTrue(salida.startswith("(extiende [`00·N3`]("), salida)

    def test_lo_que_no_se_enlaza(self):
        cercado = "```\nver `00·N3`\n```\n"
        self.assertEqual(self.enlazador.enlazar(cercado, self.origen), (cercado, 0))
        self.assertEqual(self.enlazador.enlazar("ver `ZZ99`", self.origen), ("ver `ZZ99`", 0))
        self.assertEqual(self.enlazador.enlazar("como dice `G2`", self.enlazador.indice.archivo_de("G2"))[1], 0)

    def test_enlazar_dos_veces_no_cambia_nada(self):
        una, _ = self.enlazador.enlazar("ver `00·N3`", self.origen)
        self.assertEqual(self.enlazador.enlazar(una, self.origen), (una, 0))

    def test_no_queda_ninguna_cita_suelta_en_base(self):
        self.assertEqual(CitasEnlazadas(self.estandar).validar(), [])


DURO = " "
RAYA = "—"


class LasMarcasSeMiden(unittest.TestCase):

    def test_la_raya_del_titulo_y_la_de_la_tabla_no_son_inciso(self):
        self.assertEqual(Marcas.de_linea("# EP-000 %s Título" % RAYA), [])
        self.assertEqual(Marcas.de_linea("| Fase 1 %s MVP |" % RAYA), [])
        self.assertEqual([c for c, _ in Marcas.de_linea("Un texto %s con inciso." % RAYA)], ["raya"])

    def test_la_cita_y_el_capitulo_no_son_punto_medio(self):
        self.assertEqual(Marcas.de_linea("ver 00·N3 y el 21 · Automatización"), [])
        self.assertEqual([c for c, _ in Marcas.de_linea("Una frase · otra frase")], ["punto-medio"])

    def test_el_campo_por_llenar_no_es_vineta_de_prosa(self):
        self.assertEqual(Marcas.de_linea("- **Objetivo:** «qué se logra»"), [])
        self.assertEqual([c for c, _ in Marcas.de_linea("- **Objetivo:** se logra esto")], ["vineta"])

    def test_dentro_de_codigo_no_cuenta_y_limpiar_no_lo_toca(self):
        texto = "a%sb `c%sd`\n```\ne%sf\n```\n" % (DURO, DURO, DURO)
        self.assertEqual([n for n, _, _ in Marcas.de_texto(texto)], [1])
        self.assertEqual(Marcas.limpiar(texto), ("a b `c%sd`\n```\ne%sf\n```\n" % (DURO, DURO), 1))

    def test_medir_dice_que_va_en_su_lugar(self):
        self.assertEqual(Marcas.medir("x%sy" % DURO)[0][3], "un espacio normal")
        self.assertEqual(Marcas.medir("x %s y" % RAYA)[0][3], "coma, dos puntos o paréntesis")

    def test_lo_heredado_avisa_una_vez_por_clase_y_linea_y_dice_su_alcance(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for rel, texto in (("base/a.md", "x %s y %s z\n" % (RAYA, RAYA)), ("notas/b.md", "x %s y\n" % RAYA)):
            os.makedirs(os.path.dirname(os.path.join(tmp.name, rel)), exist_ok=True)
            with io.open(os.path.join(tmp.name, rel), "w", encoding="utf-8") as f:
                f.write(texto)
        validador = MarcasDeGeneracion(tmp.name)
        self.assertEqual(len(validador.validar()), 1)
        self.assertIn("(1 archivos)", validador.alcance()[0])
        self.assertEqual(validador.contar()[0], {"raya": 3})


class ElTrinqueteDeLasMarcas(unittest.TestCase):
    """La deuda no crece: las invisibles en todas partes, todas las marcas en lo
    heredado, y silencio cuando no hay marca nueva. Cada prueba arma un repositorio."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.raiz = tmp.name
        for orden in (("init", "-q"), ("config", "user.email", "p@e"), ("config", "user.name", "P")):
            self.git(*orden)

    def git(self, *argumentos):
        subprocess.run(("git", "-C", self.raiz) + argumentos, capture_output=True, check=True)

    def preparar(self, rel, texto, commitear=False):
        ruta = os.path.join(self.raiz, *rel.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        self.git("add", rel)
        if commitear:
            self.git("commit", "-q", "-m", "base", "--no-verify")

    def niveles(self):
        return [h.severidad for h in MarcasDeGeneracion(self.raiz, solo_preparados=True).validar()]

    def test_la_invisible_nueva_bloquea_en_cualquier_carpeta(self):
        self.preparar("notas/algo.md", "espacio%sduro." % DURO)
        self.assertIn(FALLA, self.niveles())

    def test_crecer_en_lo_heredado_bloquea_y_afuera_avisa(self):
        self.preparar("base/a.md", "liso.\n", commitear=True)
        self.preparar("notas/b.md", "liso.\n", commitear=True)
        self.preparar("base/a.md", "un %s inciso.\n" % RAYA)
        self.preparar("notas/b.md", "un %s inciso.\n" % RAYA)
        self.assertEqual(sorted(self.niveles()), [AVISO, FALLA])

    def test_lo_que_ya_estaba_lo_cercado_y_el_historico_no_bloquean(self):
        viejo = "con espacio%sduro.\n" % DURO
        self.preparar("base/a.md", viejo, commitear=True)
        self.preparar("base/a.md", viejo + "```\nasi%sno\n```\n" % DURO)
        self.preparar("historico-chat/x.md", "dijo %s así%s.\n" % (RAYA, DURO))
        self.assertEqual(self.niveles(), [])

    def test_renombrar_no_cuenta_las_marcas_viejas_pero_si_las_nuevas(self):
        self.preparar("plantillas/algo.md", "un %s viejo.\n" % RAYA, commitear=True)
        os.makedirs(os.path.join(self.raiz, "plantillas", "ciclo"))
        self.git("mv", "plantillas/algo.md", "plantillas/ciclo/algo.md")
        self.assertEqual(self.niveles(), [])
        self.preparar("plantillas/ciclo/algo.md", "un %s viejo %s y nueva.\n" % (RAYA, RAYA))
        self.assertEqual(self.niveles(), [FALLA])


if __name__ == "__main__":
    unittest.main()
