"""`EP-028·HU-007`, fase B: las pestañas del gasto funcionan con AdminLTE y traen su ayuda.

Que el clic cambie de pestaña en el navegador lo prueba `historico-chat/scripts/2026-10-08/ver_pestanas.mjs`;
aquí se prueba lo que lo hace posible en el HTML."""
import re

from django.urls import reverse

from core.ayuda.textos import CAMPOS
from core.consumo.tablero import GastoDelPeriodo
from core.consumo.tests_tablero import ConGasto

AYUDA = re.compile(r'class="ayuda-icono[^"]*"')


class LasPestanasFuncionan(ConGasto):
    """CP-001."""

    def setUp(self):
        super().setUp()
        self.entrar()

    def test_la_pestana_pulsada_cancela_la_que_estaba_cargando(self):
        html = self.client.get(reverse("consumo:tablero")).content.decode()
        barra = html.split('id="pestanas"', 1)[1].split("</ul>", 1)[0]
        enlaces = re.findall(r'<a class="nav-link[^>]*>', barra)
        self.assertEqual(len(enlaces), len(GastoDelPeriodo.PESTANAS))
        for enlace in enlaces:
            self.assertIn('hx-target="#pestana"', enlace)
            self.assertIn('hx-sync="#pestana:replace"', enlace)
            self.assertIn('hx-indicator="#pestana-cargando"', enlace)
        self.assertIn('id="pestana-cargando"', html)
        self.assertRegex(html, r'id="pestana"[^>]*hx-sync="this:replace"')

    def test_lo_que_se_refresca_no_tapa_la_pestana_escogida(self):
        for nombre in GastoDelPeriodo.PESTANAS:
            html = self.client.get(reverse("consumo:pestana", args=[nombre])).content.decode()
            self.assertIn('hx-sync="#pestana:drop"', html, nombre)

    def test_lo_que_carga_en_pestana_desde_adentro_no_la_reemplaza(self):
        """Lo que reportó el usuario: los botones de «Dónde se gasta» heredaban `outerHTML` y borraban #pestana."""
        for nombre in GastoDelPeriodo.PESTANAS:
            html = self.client.get(reverse("consumo:pestana", args=[nombre])).content.decode()
            for etiqueta in re.findall(r'<[a-z]+[^>]*hx-target="#pestana"[^>]*>', html):
                self.assertIn('hx-swap="innerHTML"', etiqueta, nombre)

    def test_la_pestana_pedida_sale_marcada_y_es_la_que_carga(self):
        for nombre in GastoDelPeriodo.PESTANAS:
            html = self.client.get(reverse("consumo:tablero"), {"pestana": nombre}).content.decode()
            activa = re.search(r'<a class="nav-link active"[^>]*hx-get="([^"]+)"', html)
            self.assertIn("/pestana/%s/" % nombre, activa.group(1))
            self.assertRegex(html, r'id="pestana"\s+hx-get="[^"]*/pestana/%s/' % nombre)


class LasPestanasTienenSuAyuda(ConGasto):
    """CP-002."""

    def setUp(self):
        super().setUp()
        self.entrar()

    def test_cada_pestana_y_la_franja_traen_su_ayuda(self):
        rutas = [reverse("consumo:pestana", args=[n]) for n in GastoDelPeriodo.PESTANAS]
        rutas.append(reverse("consumo:franja"))
        for ruta in rutas:
            html = self.client.get(ruta).content.decode()
            self.assertGreaterEqual(len(AYUDA.findall(html)), 4, ruta)
            self.assertNotIn("ayuda-icono-falta", html, ruta)

    def test_las_claves_del_gasto_tienen_texto(self):
        from pathlib import Path
        carpeta = Path(__file__).parent / "templates" / "consumo"
        usadas = set()
        for plantilla in carpeta.glob("*.html"):
            usadas |= set(re.findall(r'ayuda_campo "([^"]+)"', plantilla.read_text(encoding="utf-8")))
        self.assertTrue(usadas)
        self.assertEqual(sorted(c for c in usadas if c not in CAMPOS), [])

    def test_la_ayuda_se_activa_en_lo_que_llega_por_htmx(self):
        from django.contrib.staticfiles import finders
        with open(finders.find("ayuda/ayuda.js"), encoding="utf-8") as archivo:
            guion = archivo.read()
        self.assertIn("htmx:load", guion)
        self.assertIn("htmx:beforeSwap", guion)
