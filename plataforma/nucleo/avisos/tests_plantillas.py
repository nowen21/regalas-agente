# -*- coding: utf-8 -*-
"""Que ninguna pantalla imprima lo que era un comentario.

**Lo vio el usuario en la pantalla, no una prueba.** Un comentario de plantilla
escrito con llave-almohadilla ocupaba dos líneas, y **esa forma solo admite
una**: Django se tragó la primera y escupió el resto como texto visible, en
todas las pantallas a la vez.

Ninguna de las quince pruebas de pantalla lo vio, porque todas preguntan si una
frase **está** y ninguna preguntaba si sobra algo. Esta pregunta lo contrario.
"""
import re

from django.test import Client, TestCase

from nucleo.proyectos.models import Proyecto
from nucleo.acceso import para_probar

# Lo que nunca puede llegar al navegador. **Solo las marcas de comentario**: las
# de etiqueta y variable —`{%`, `{{`— aparecen legítimamente dentro del
# JavaScript y del CSS de la página, y buscarlas ahí da falsos rojos. Un rojo
# falso enseña a ignorar la prueba (`S-108`).
SOBRAS = ("{#", "#}")


class NingunaPantallaImprimeSusComentarios(TestCase):

    def setUp(self):
        self.cliente = Client()
        # Todo exige haber entrado: la prueba entra como quien manda.
        para_probar.como_usuario(self.cliente)
        Proyecto.objects.create(
            identificador="de-prueba", nombre="De prueba",
            ruta_codigo="/no-existe", ruta_normalizada="/no-existe",
            conectado="conectado")

    def _revisar(self, ruta):
        cuerpo = self.cliente.get(ruta).content.decode("utf-8")
        # Lo que va dentro de un bloque de código sí puede traer llaves: se mira
        # el resto de la página.
        fuera = re.sub(r"<code>.*?</code>|<pre>.*?</pre>", " ", cuerpo,
                       flags=re.S)
        for sobra in SOBRAS:
            self.assertNotIn(
                sobra, fuera,
                "%s imprime %r: era una etiqueta de plantilla y salió a la "
                "pantalla" % (ruta, sobra))

    def test_la_ficha_con_datos_tampoco_imprime_etiquetas(self):
        """**La primera versión de esta prueba no lo habría visto.**

        El proyecto que usaba estaba vacío, así que media pantalla —la que
        muestra las cifras y su lectura— no se dibujaba. Un comentario mal
        escrito ahí adentro pasaba entero. Se prueba con datos y sin ellos.
        """
        import os as sistema
        import tempfile as temporal
        raiz = temporal.mkdtemp(prefix="prueba-ficha-")
        try:
            carpeta = sistema.path.join(raiz, "cvds", "planificacion")
            sistema.makedirs(carpeta)
            with open(sistema.path.join(carpeta, "README.md"), "w",
                      encoding="utf-8") as abierto:
                abierto.write("# Planificacion\n")
            from nucleo.importacion.models import Traido
            Traido.objects.create(proyecto="con-datos",
                                  origen="cvds/planificacion/README.md",
                                  tipo="etapa del ciclo de vida",
                                  guardado_en="x.md")
            Proyecto.objects.create(
                identificador="con-datos", nombre="Con datos",
                ruta_codigo=raiz, ruta_normalizada=raiz.lower(),
                conectado="conectado")
            self._revisar("/proyecto/con-datos/")
        finally:
            import shutil as borrar
            borrar.rmtree(raiz, ignore_errors=True)

    def test_las_siete_pantallas_no_imprimen_etiquetas(self):
        for ruta in ("/", "/tablero/",
                     "/proyecto/de-prueba/",
                     "/proyecto/de-prueba/fases/",
                     "/proyecto/de-prueba/funcionalidades/",
                     "/proyecto/de-prueba/aprobaciones/",
                     "/proyecto/de-prueba/memoria/"):
            self._revisar(ruta)

    def test_un_comentario_de_varias_lineas_va_con_comment(self):
        """La regla que hay que recordar, escrita como prueba.

        `{# ... #}` en varias líneas deja escapar todo menos la primera. La
        forma que sí aguanta varias líneas es `{% comment %}`.
        """
        from django.template import Context, Template
        con_llave = Template(u"{# una\ndos #}visible")
        con_bloque = Template(u"{% comment %}una\ndos{% endcomment %}visible")
        self.assertIn("dos", con_llave.render(Context({})))
        self.assertEqual("visible", con_bloque.render(Context({})).strip())
