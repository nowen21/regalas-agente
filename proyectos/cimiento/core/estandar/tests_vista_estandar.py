# -*- coding: utf-8 -*-
"""`EP-027·HU-004` · Pruebas de la fase A: el estándar se lee como página (CP-001 a CP-004)."""
from django.test import SimpleTestCase

from .models import Documento
from .presentar import Estandar, Pagina, ancla
from .tests_pantalla import ConEstandar

F0 = "base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md"
F1 = "base/02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md"


class LaListaVaPorCapitulo(ConEstandar):
    """CP-001."""

    def test_capitulos_con_nombre_y_reglas_sin_ruta(self):
        html = self.client.get("/estandar/").content.decode()
        self.assertIn("02 · Flujo de trabajo", html)
        self.assertIn("Carga el contexto antes de actuar", html)
        self.assertIn(">F1<", html)
        self.assertNotIn("reglas/F1-", html)
        self.assertNotIn(".md<", html)

    def test_la_regla_de_un_capitulo_de_un_archivo_lleva_a_su_seccion(self):
        html = self.client.get("/estandar/").content.decode()
        conducta = self.doc("base/01-conducta.md")
        self.assertIn('href="/estandar/documento/%d/#c1--avisa-antes-de-tocar"' % conducta.pk, html)
        self.assertIn("Avisa antes de tocar", html)

    def test_buscar_deja_solo_lo_que_dice_la_palabra(self):
        html = self.client.get("/estandar/", {"q": "cadena completa"}).content.decode()
        self.assertIn("Recorre la cadena completa", html)
        self.assertNotIn("Avisa antes de tocar", html)


class ElDocumentoSeLeeComoPagina(ConEstandar):
    """CP-002."""

    def test_ejemplo_en_tarjetas_tabla_de_tabler_y_sin_marcas(self):
        html = self.client.get("/estandar/documento/%d/" % self.doc(F1).pk).content.decode()
        pagina = html[html.index("pagina-estandar"):html.index('id="cambiar"')]
        self.assertIn("Incorrecto", pagina)
        self.assertIn("Correcto", pagina)
        self.assertIn("border-danger", pagina)
        self.assertIn("border-success", pagina)
        self.assertIn('<table class="table table-vcenter card-table">', pagina)
        for marca in ("|---|", "```", "**", "\n## ", "\n### "):
            self.assertNotIn(marca, pagina)
        self.assertNotIn("<pre", pagina)

    def test_cambiar_el_texto_solo_lo_ve_quien_administra(self):
        url = "/estandar/documento/%d/" % self.doc(F1).pk
        self.assertIn("Cambiar el texto", self.client.get(url).content.decode())
        self.client.force_login(self.mira)
        html = self.client.get(url).content.decode()
        self.assertNotIn("Cambiar el texto", html)
        self.assertIn("Carga el contexto antes de actuar", html)


class ElTextoNoEntraComoHtml(SimpleTestCase):
    """CP-003."""

    def test_se_escapa(self):
        html = Pagina(Estandar([]), "base/x.md").armar("<script>alert(1)</script> y **negrita**")
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertIn("<strong>negrita</strong>", html)

    def test_el_ancla_es_la_de_github(self):
        self.assertEqual("n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada",
                         ancla("N1 · Ningún cambio de estado sin aprobación explícita (BLINDADA)"))


class LosEnlacesAbrenYLasRelacionesSeVen(ConEstandar):
    """CP-004."""

    def test_el_enlace_abre_la_otra_regla_en_cimiento(self):
        html = self.client.get("/estandar/documento/%d/" % self.doc(F0).pk).content.decode()
        f2 = Documento.objects.get(ruta__startswith="base/02-flujo-de-trabajo/reglas/F2-")
        self.assertIn('href="/estandar/documento/%d/"' % f2.pk, html)

    def test_dependencias_las_que_nombra_y_las_que_la_nombran_por_separado(self):
        estandar = Estandar(Documento.objects.all())
        relaciones = estandar.relaciones(estandar.por_ruta[F0])
        dependencias = {r["codigo"] for r in relaciones["dependencias"]}
        self.assertIn("F2", dependencias)
        self.assertEqual({"Depende de"}, {r["tipo"] for r in relaciones["dependencias"]})
        self.assertFalse(dependencias & {r["codigo"] for r in relaciones["nombra"]})
        self.assertIn("02 · Flujo de trabajo", {r["nombre"] for r in relaciones["la_nombran"]})
        html = self.client.get("/estandar/documento/%d/" % self.doc(F0).pk).content.decode()
        for titulo in ("De qué depende", "Reglas que nombra", "La nombran"):
            self.assertIn(titulo, html)

    def test_un_archivo_que_no_esta_en_la_base_queda_como_texto(self):
        html = Pagina(Estandar([]), "base/x.md").armar("Ver [la épica](../documentacion/epica.md).")
        self.assertIn('<span class="text-secondary">la épica</span>', html)
        self.assertNotIn("href", html)
