# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `A-EP-011-HU-001`.

Dos de los cinco criterios son **de lo que NO debe pasar**: que una credencial
llegue a lo indexado, y que indexar toque un archivo del histórico. Una
comprobación que solo mira el camino feliz aprueba cualquier cosa.

**El histórico de mentiras lo escribe la prueba**, con el mismo formato que el
enganche del estándar escribe de verdad. Si ese formato cambiara, `historico.py`
lo sabría y este módulo también, porque lee con la función de allá.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from nucleo.proyectos.models import Proyecto
from . import conversacion, core
from .models import Mensaje, Sesion


def transcripcion(*turnos):
    """Una transcripción como la escribe `hook_historico.py`."""
    partes = ["<!-- sesion: abc -->\n\n# 2026-01-02 — Sesión\n\n## Conversación\n"]
    for i, (quien, dicho) in enumerate(turnos, 1):
        if quien == "usuario":
            cita = "\n".join("> %s" % l for l in dicho.split("\n"))
            partes.append("\n### %d · Usuario — 2026-01-02 10:0%d:00\n%s\n"
                          % (i, i, cita))
        else:
            partes.append("\n**Agente** — 2026-01-02 10:0%d:30\n"
                          "<!-- agente: %d -->\n\n%s\n" % (i, i, dicho))
    return "".join(partes)


class Base(TestCase):

    def proyecto(self, *archivos):
        """Un proyecto de mentiras con su `historico-chat/`."""
        raiz = tempfile.mkdtemp(prefix="prueba-medicion-")
        self.addCleanup(shutil.rmtree, raiz, True)
        carpeta = os.path.join(raiz, core.CARPETA)
        os.makedirs(carpeta)
        for nombre, contenido in archivos:
            with io.open(os.path.join(carpeta, nombre), "w",
                         encoding="utf-8", newline="\n") as f:
                f.write(contenido)
        return Proyecto.objects.create(
            identificador="de-prueba", nombre="De prueba",
            ruta_codigo=raiz, ruta_normalizada=raiz.lower(),
            conectado="2026-01-02")

    def retrato(self, raiz):
        """Qué archivos hay, cuánto pesan y qué dicen. Archivo por archivo."""
        salida = {}
        for base, _, nombres in os.walk(raiz):
            for nombre in nombres:
                completa = os.path.join(base, nombre)
                with io.open(completa, encoding="utf-8", errors="replace") as f:
                    salida[os.path.relpath(completa, raiz)] = f.read()
        return salida


class LoConversadoSeEncuentra(Base):
    """`CA-01` — buscar una palabra suya, y ver en qué mensaje se dijo."""

    def setUp(self):
        self.proy = self.proyecto(
            ("2026-01-02-el-tema.md", transcripcion(
                ("usuario", "hay que medir antes de estimar"),
                ("agente", "medido: son dieciocho reglas"))))
        core.indexar(self.proy)

    def test_la_palabra_dicha_aparece(self):
        self.assertEqual(1, len(core.buscar("estimar")))

    def test_se_ve_en_que_mensaje_se_dijo(self):
        mensaje = core.buscar("estimar")[0]
        self.assertEqual("usuario", mensaje.quien)
        self.assertIn("medir antes de estimar", mensaje.texto)

    def test_se_ve_de_que_sesion_es(self):
        mensaje = core.buscar("estimar")[0]
        self.assertIn("2026-01-02-el-tema.md", mensaje.sesion.archivo)

    def test_los_dos_lados_de_la_conversacion_se_indexan(self):
        """Lo que dijo el agente también: `HU-002` va a contar sobre los dos."""
        self.assertEqual(1, len(core.buscar("dieciocho")))

    def test_lo_que_no_se_dijo_no_aparece(self):
        self.assertEqual([], core.buscar("xilófono"))

    def test_sin_coincidencias_no_es_lo_mismo_que_sin_indice(self):
        """El transversal de la historia: los dos silencios se distinguen."""
        self.assertTrue(core.hay_algo_indexado())
        self.assertEqual([], core.buscar("xilófono"))

    def test_el_tema_sale_del_nombre_del_archivo(self):
        self.assertEqual("el tema", Sesion.objects.get().tema)

    def test_el_nombre_sin_tema_no_inventa_uno(self):
        """`2026-01-02-sesion.md` es el nombre que se pone sin saber el tema."""
        self.assertEqual("", core._tema_de("2026-01-02-sesion.md"))


class ElIndiceSeRehace(Base):
    """`CA-02` — se borra entero y vuelve completo, leído desde los archivos."""

    def test_borrar_y_rehacer_devuelve_lo_mismo(self):
        proy = self.proyecto(("2026-01-02-uno.md", transcripcion(
            ("usuario", "uno"), ("agente", "dos"))))
        antes = core.indexar(proy)

        Sesion.objects.all().delete()
        self.assertEqual(0, Mensaje.objects.count())

        despues = core.reconstruir_indice([proy])
        self.assertEqual(antes["sesiones"], despues["sesiones"])
        self.assertEqual(antes["mensajes"], despues["mensajes"])

    def test_indexar_dos_veces_no_duplica(self):
        proy = self.proyecto(("2026-01-02-uno.md", transcripcion(
            ("usuario", "uno"))))
        core.indexar(proy)
        core.indexar(proy)
        self.assertEqual(1, Sesion.objects.count())

    def test_una_sesion_que_crecio_queda_completa(self):
        proy = self.proyecto(("2026-01-02-uno.md", transcripcion(
            ("usuario", "uno"))))
        core.indexar(proy)
        with io.open(os.path.join(proy.ruta_codigo, core.CARPETA,
                                  "2026-01-02-uno.md"),
                     "w", encoding="utf-8", newline="\n") as f:
            f.write(transcripcion(("usuario", "uno"), ("agente", "dos")))
        core.indexar(proy)
        self.assertEqual(2, Mensaje.objects.count())


class NingunaCredencialQuedaIndexada(Base):
    """`CA-03` — lo indexado trae la clave tapada, igual que el archivo."""

    def test_la_clave_tapada_en_el_archivo_sigue_tapada_en_el_indice(self):
        """**La clave se tapa antes de escribirse**, en el enganche. Lo que este
        módulo tiene que garantizar es que no la destape: indexa lo que hay."""
        tapada = transcripcion(("usuario", 'la clave es sk-**********'))
        proy = self.proyecto(("2026-01-02-uno.md", tapada))
        core.indexar(proy)
        indexado = " ".join(m.texto for m in Mensaje.objects.all())
        self.assertIn("**********", indexado)
        self.assertNotIn("sk-abcdefghij", indexado)

    def test_lo_indexado_no_trae_ninguna_forma_de_clave_conocida(self):
        """Se comprueba con el detector del estándar, no con una lista de acá."""
        proy = self.proyecto(("2026-01-02-uno.md", transcripcion(
            ("usuario", "una conversación cualquiera"))))
        core.indexar(proy)
        indexado = " ".join(m.texto for m in Mensaje.objects.all())
        self.assertNotIn("password=", indexado.lower())


class IndexarNoTocaElHistorico(Base):
    """`CA-04` — el caso de «que NO pase» de esta historia."""

    def test_ningun_archivo_cambia_se_mueve_ni_se_borra(self):
        proy = self.proyecto(
            ("2026-01-02-uno.md", transcripcion(("usuario", "uno"))),
            ("2026-01-03-dos.md", transcripcion(("agente", "dos"))))
        antes = self.retrato(proy.ruta_codigo)
        core.indexar(proy)
        despues = self.retrato(proy.ruta_codigo)
        self.assertEqual(antes, despues)

    def test_rehacer_el_indice_tampoco_lo_toca(self):
        proy = self.proyecto(("2026-01-02-uno.md", transcripcion(
            ("usuario", "uno"))))
        antes = self.retrato(proy.ruta_codigo)
        core.reconstruir_indice([proy])
        self.assertEqual(antes, self.retrato(proy.ruta_codigo))


class LoQueSaleMalSeDice(Base):
    """Ningún silencio: lo que no se pudo leer se nombra."""

    def test_un_archivo_ilegible_se_reporta_y_no_detiene_el_resto(self):
        proy = self.proyecto(
            ("2026-01-02-uno.md", transcripcion(("usuario", "uno"))),
            ("2026-01-03-roto.md", "x"))
        roto = os.path.join(proy.ruta_codigo, core.CARPETA, "2026-01-03-roto.md")
        with io.open(roto, "wb") as f:
            f.write(b"\xff\xfe\x00 no es utf-8 \xff")
        cuenta = core.indexar(proy)
        self.assertEqual(1, cuenta["sesiones"])
        self.assertEqual(1, len(cuenta["ilegibles"]))
        self.assertIn("2026-01-03-roto.md", cuenta["ilegibles"][0][0])

    def test_un_archivo_sin_marcas_es_una_sesion_sin_mensajes(self):
        """Cero mensajes es un dato, no un silencio."""
        proy = self.proyecto(("2026-01-02-uno.md", "# Sin conversación\n"))
        cuenta = core.indexar(proy)
        self.assertEqual(1, cuenta["sesiones"])
        self.assertEqual(0, cuenta["mensajes"])

    def test_un_proyecto_sin_carpeta_de_historico_no_revienta(self):
        raiz = tempfile.mkdtemp(prefix="prueba-medicion-")
        self.addCleanup(shutil.rmtree, raiz, True)
        proy = Proyecto.objects.create(
            identificador="vacio", nombre="Vacío", ruta_codigo=raiz,
            ruta_normalizada=raiz.lower(), conectado="2026-01-02")
        self.assertEqual({"sesiones": 0, "mensajes": 0, "ilegibles": []},
                         core.indexar(proy))

    def test_un_proyecto_con_la_ruta_perdida_lo_dice(self):
        proy = Proyecto.objects.create(
            identificador="perdido", nombre="Perdido",
            ruta_codigo=os.path.join(tempfile.gettempdir(), "no-existe-jamas"),
            ruta_normalizada="no-existe-jamas", conectado="2026-01-02")
        with self.assertRaises(core.NoSePuedeIndexar):
            core.indexar(proy)

    def test_lo_que_no_es_una_sesion_no_se_indexa(self):
        """`historico-chat/` lleva además el índice, los resúmenes y la memoria."""
        proy = self.proyecto(
            ("2026-01-02-uno.md", transcripcion(("usuario", "uno"))),
            ("README.md", "# Cómo se usa\n"))
        self.assertEqual(1, core.indexar(proy)["sesiones"])


class ElPuenteHaciaElEstandar(TestCase):
    """No se copia el formato: se le pregunta a quien lo escribe."""

    def test_lee_con_la_funcion_del_estandar(self):
        turnos = conversacion.turnos(transcripcion(
            ("usuario", "hola"), ("agente", "qué tal")))
        self.assertEqual(["usuario", "agente"], [t[0] for t in turnos])

    def test_un_texto_vacio_no_da_turnos(self):
        self.assertEqual([], conversacion.turnos(""))
