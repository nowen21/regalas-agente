# -*- coding: utf-8 -*-
"""Los nueve casos del plan de pruebas de la fase E.

El que más daño evita es `CP-009`: comparar la carpeta del proyecto archivo por
archivo antes y después de traer. Traer es la operación que **más archivos
ajenos lee**, y por eso es donde más caro sale equivocarse.

El que más se aprende es `CP-008`: traer este mismo repositorio, que es el caso
más grande que existe hoy. Si el módulo no puede con él, no puede con nada.

**Ninguna carpeta real del usuario se usa como conejillo**, salvo el
repositorio del estándar en `CP-008`, y ahí lo que se comprueba es justamente
que traer no lo toque.
"""
import io
import os
import shutil
import tempfile
import time

from django.test import TestCase, override_settings

from nucleo.auditoria.models import Registro
from nucleo.proyectos import core as proyectos
from . import core, moldes
from .models import Traido


def _escribir(ruta, texto):
    carpeta = os.path.dirname(ruta)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="") as archivo:
        archivo.write(texto)


def _retrato(carpeta):
    """Qué archivos hay, con su contenido y su fecha. Para comparar después."""
    huella = {}
    for raiz, _, archivos in os.walk(carpeta):
        for nombre in archivos:
            completa = os.path.join(raiz, nombre)
            relativa = os.path.relpath(completa, carpeta)
            with io.open(completa, "rb") as abierto:
                huella[relativa] = (abierto.read(), os.path.getmtime(completa))
    return huella


class BaseImportacion(TestCase):
    """Cada prueba corre sobre su propia carpeta de datos y su propio proyecto."""

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-datos-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos)
        self.contexto.enable()
        self.ajenas = []

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.datos, ignore_errors=True)
        for carpeta in self.ajenas:
            shutil.rmtree(carpeta, ignore_errors=True)

    def proyecto_con(self, documentos, extras=None):
        """Un proyecto de mentira con la documentación que se le diga.

        `documentos` es {ruta dentro de documentacion/: texto}.
        `extras` es {ruta dentro del proyecto: texto}, para lo que no es del ciclo.
        """
        carpeta = tempfile.mkdtemp(prefix="prueba-proyecto-")
        self.ajenas.append(carpeta)
        _escribir(os.path.join(carpeta, "codigo.py"), "# el codigo\n")
        _escribir(os.path.join(carpeta, "CLAUDE.md"),
                  "**Versión del estándar adoptada:** `34.1.0`\n")
        for relativa, texto in documentos.items():
            _escribir(os.path.join(carpeta, "documentacion",
                                   relativa.replace("/", os.sep)), texto)
        for relativa, texto in (extras or {}).items():
            _escribir(os.path.join(carpeta, relativa.replace("/", os.sep)), texto)
        proyecto, _ = proyectos.conectar("El de la prueba", carpeta)
        return proyecto, carpeta


class ReconocerTests(BaseImportacion):
    """CP-001 · lo que sigue un molde entra con su tipo."""

    LOS_SIETE = {
        "epicas/EP-001/epica.md": "# La épica\n",
        "epicas/EP-001/HU-001-lo-que-sea.md": "# La historia\n",
        "epicas/EP-001/A-fase/plan_trabajo.md": "# El plan\n",
        "epicas/EP-001/A-fase/plan_pruebas.md": "# Las pruebas\n",
        "epicas/EP-001/A-fase/resultado_pruebas.md": "# El resultado\n",
        "epicas/EP-001/A-fase/funcionalidad_implementada.md": "# El cierre\n",
        "epicas/EP-001/A-fase/estado-fase.md": "# El estado\n",
    }

    def test_cada_documento_entra_con_su_tipo(self):
        proyecto, _ = self.proyecto_con(self.LOS_SIETE)

        hallazgo, nuevos, ya = core.traer(proyecto)

        self.assertEqual(nuevos, 7)
        self.assertEqual(ya, 0)
        tipos = sorted(t.tipo for t in Traido.objects.all())
        self.assertEqual(tipos, [
            "estado de fase", "funcionalidad implementada",
            "historia de usuario", "plan de pruebas", "plan de trabajo",
            "resultado de pruebas", "épica"])

    def test_cada_documento_dice_de_que_archivo_salio(self):
        proyecto, _ = self.proyecto_con(self.LOS_SIETE)
        core.traer(proyecto)

        uno = Traido.objects.get(tipo="épica")
        self.assertEqual(uno.origen, "documentacion/epicas/EP-001/epica.md")

    def test_los_tres_moldes_que_faltaban_se_reconocen(self):
        """Salieron de contar sobre el repositorio real, y no eran casos raros."""
        proyecto, _ = self.proyecto_con({
            "senales.md": "# Señales\n",
            "epicas/EP-001/A-fase/resultado_pruebas_2.md": "# Segundo ciclo\n",
            "versiones/2026-08-14-15.0.0.md": "# La versión\n",
        })

        core.traer(proyecto)

        tipos = sorted(t.tipo for t in Traido.objects.all())
        self.assertEqual(tipos, ["registro de versión", "resultado de pruebas",
                                 "señales"])

    def test_un_proyecto_sin_documentacion_lo_dice(self):
        proyecto, _ = self.proyecto_con({})

        hallazgo = core.mirar(proyecto)

        self.assertFalse(hallazgo.hay_documentacion)
        self.assertEqual(hallazgo.cuantos, 0)


class NoSeTransformaTests(BaseImportacion):
    """CP-002 · lo traído dice lo mismo que el original."""

    def test_el_texto_es_identico_caracter_por_caracter(self):
        original = ("# Un documento\n\n"
                    "Con acentos: ñáéíóú, comillas «así», y una tabla:\n\n"
                    "| Uno | Dos |\n|---|---|\n| a | b |\n")
        proyecto, carpeta = self.proyecto_con({"epicas/EP-001/epica.md": original})

        core.traer(proyecto)

        traido = Traido.objects.get()
        completa = os.path.join(self.datos,
                                traido.guardado_en.replace("/", os.sep))
        with io.open(completa, encoding="utf-8", newline="") as abierto:
            self.assertEqual(abierto.read(), original)

    def test_los_saltos_de_linea_no_se_cambian(self):
        """Un salto de línea cambiado también es una transformación."""
        original = "# Con saltos de Windows\r\n\r\nSegunda línea\r\n"
        proyecto, _ = self.proyecto_con({"epicas/EP-001/epica.md": original})

        core.traer(proyecto)

        traido = Traido.objects.get()
        completa = os.path.join(self.datos,
                                traido.guardado_en.replace("/", os.sep))
        with io.open(completa, "rb") as abierto:
            self.assertEqual(abierto.read().decode("utf-8"), original)


class SinReconocerTests(BaseImportacion):
    """CP-003 y CP-004 · lo que no entra, y decirlo cuando todo entró."""

    def test_lo_que_no_sigue_un_molde_no_entra_y_se_cuenta(self):
        proyecto, _ = self.proyecto_con({
            "epicas/EP-001/epica.md": "# La épica\n",
            "epicas/EP-001/HU-001-algo.md": "# La historia\n",
            "apuntes.md": "# Apuntes sueltos\n",
            "borrador-viejo.md": "# Un borrador\n",
            "epicas/notas-de-la-reunion.md": "# Notas\n",
        })

        hallazgo, nuevos, _ = core.traer(proyecto)

        self.assertEqual(nuevos, 2)
        self.assertEqual(Traido.objects.count(), 2)
        self.assertEqual(len(hallazgo.sin_reconocer), 3)
        self.assertIn("documentacion/apuntes.md", hallazgo.sin_reconocer)

    def test_lo_no_reconocido_trae_su_ruta(self):
        proyecto, _ = self.proyecto_con({"raro.md": "# Raro\n"})

        hallazgo = core.mirar(proyecto)

        self.assertEqual(hallazgo.sin_reconocer, ["documentacion/raro.md"])

    def test_si_todo_se_reconocio_se_dice(self):
        proyecto, _ = self.proyecto_con({"epicas/EP-001/epica.md": "# Épica\n"})

        hallazgo = core.mirar(proyecto)

        self.assertTrue(hallazgo.todo_reconocido)

    def test_la_pantalla_lo_dice_con_palabras(self):
        proyecto, _ = self.proyecto_con({"epicas/EP-001/epica.md": "# Épica\n"})

        cuerpo = self.client.get(
            "/proyecto/%s/traer/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("Nada quedó afuera", cuerpo)

    def test_las_carpetas_que_no_se_miran_se_nombran(self):
        """`RN-4`: saltarse carpetas sin decirlo es perder en silencio."""
        proyecto, _ = self.proyecto_con(
            {"epicas/EP-001/epica.md": "# Épica\n"},
            extras={"base/00-nucleo.md": "# Reglas\n",
                    "pendientes/1-algo.md": "# Pendiente\n"})

        hallazgo = core.mirar(proyecto)
        nombres = [c for c, _ in hallazgo.carpetas_que_no_se_miraron]

        self.assertIn("base", nombres)
        self.assertIn("pendientes", nombres)
        cuerpo = self.client.get(
            "/proyecto/%s/traer/" % proyecto.identificador).content.decode("utf-8")
        self.assertIn("no se miraron", cuerpo)


class NoDuplicarTests(BaseImportacion):
    """CP-005 · traer dos veces no duplica, y un documento editado se actualiza."""

    def test_traer_dos_veces_no_sube_la_cuenta(self):
        proyecto, _ = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Épica\n",
            "epicas/EP-001/HU-001-algo.md": "# Historia\n",
        })
        core.traer(proyecto)
        antes = Traido.objects.count()

        _, nuevos, ya_estaban = core.traer(proyecto)

        self.assertEqual(Traido.objects.count(), antes)
        self.assertEqual(nuevos, 0)
        self.assertEqual(ya_estaban, 2)

    def test_un_documento_editado_entra_con_su_version_nueva(self):
        """Distingue «no duplicar» de «no actualizar»."""
        proyecto, carpeta = self.proyecto_con(
            {"epicas/EP-001/epica.md": "# Como era\n"})
        core.traer(proyecto)

        _escribir(os.path.join(carpeta, "documentacion", "epicas", "EP-001",
                               "epica.md"), "# Como quedó\n")
        core.traer(proyecto)

        self.assertEqual(Traido.objects.count(), 1)
        traido = Traido.objects.get()
        completa = os.path.join(self.datos,
                                traido.guardado_en.replace("/", os.sep))
        with io.open(completa, encoding="utf-8") as abierto:
            self.assertEqual(abierto.read(), "# Como quedó\n")


class ConfirmacionTests(BaseImportacion):
    """CP-006 · se muestra qué se va a traer antes de traerlo."""

    def test_sin_confirmar_no_entra_nada(self):
        proyecto, _ = self.proyecto_con({"epicas/EP-001/epica.md": "# Épica\n"})
        antes = Registro.objects.count()

        respuesta = self.client.post("/proyecto/%s/traer/" % proyecto.identificador)

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Traido.objects.count(), 0)
        self.assertEqual(Registro.objects.count(), antes)

    def test_se_muestra_el_recuento_por_tipo_y_no_la_lista_entera(self):
        documentos = {"epicas/EP-%03d/epica.md" % n: "# Épica %d\n" % n
                      for n in range(20)}
        proyecto, _ = self.proyecto_con(documentos)

        cuerpo = self.client.get(
            "/proyecto/%s/traer/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("Tipo de documento", cuerpo)
        self.assertIn("épica", cuerpo)
        # El recuento sale; las veinte rutas, no.
        self.assertNotIn("EP-017", cuerpo)

    def test_la_confirmacion_dice_que_no_va_a_pasar(self):
        proyecto, _ = self.proyecto_con({"epicas/EP-001/epica.md": "# Épica\n"})

        cuerpo = self.client.get(
            "/proyecto/%s/traer/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("se copia, no se mueve", cuerpo)
        self.assertIn("no queda nada de esta pasada", cuerpo)

    def test_al_confirmar_si_entra_y_queda_registrado(self):
        proyecto, _ = self.proyecto_con({"epicas/EP-001/epica.md": "# Épica\n"})
        antes = Registro.objects.count()

        self.client.post("/proyecto/%s/traer/" % proyecto.identificador,
                         {"confirmado": "si"})

        self.assertEqual(Traido.objects.count(), 1)
        self.assertEqual(Registro.objects.count(), antes + 1)
        registro = Registro.objects.get(
            que_se_hizo="traer la documentación de un proyecto")
        self.assertIn("1 documento", registro.que_cambio)


class FallaAMitadTests(BaseImportacion):
    """CP-007 · una falla a mitad no deja media importación."""

    def test_si_falla_a_mitad_no_queda_nada_de_esa_pasada(self):
        proyecto, carpeta = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Uno\n",
            "epicas/EP-002/epica.md": "# Dos\n",
            "epicas/EP-003/epica.md": "# Tres\n",
        })

        original = core._escribir
        escrituras = []

        def falla_en_la_segunda(nombre, texto):
            escrituras.append(nombre)
            if len(escrituras) == 2:
                raise IOError("el disco dijo que no")
            return original(nombre, texto)

        core._escribir = falla_en_la_segunda
        try:
            with self.assertRaises(core.NoSePudoTraer):
                core.traer(proyecto)
        finally:
            core._escribir = original

        self.assertEqual(Traido.objects.count(), 0)
        traido = os.path.join(self.datos, "proyectos", proyecto.identificador,
                              "traido")
        quedaron = []
        for raiz, _, archivos in os.walk(traido):
            quedaron.extend(archivos)
        self.assertEqual(quedaron, [], "quedó media importación")

    def test_el_origen_queda_intacto_despues_de_fallar(self):
        proyecto, carpeta = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Uno\n",
            "epicas/EP-002/epica.md": "# Dos\n",
        })
        antes = _retrato(carpeta)

        original = core._escribir
        core._escribir = lambda n, t: (_ for _ in ()).throw(IOError("no"))
        try:
            with self.assertRaises(core.NoSePudoTraer):
                core.traer(proyecto)
        finally:
            core._escribir = original

        self.assertEqual(antes, _retrato(carpeta))


class NoTocarElOrigenTests(BaseImportacion):
    """CP-009 · que NO pase: que se toque el proyecto de origen."""

    def test_la_carpeta_del_proyecto_queda_intacta(self):
        proyecto, carpeta = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Épica\n",
            "epicas/EP-001/HU-001-algo.md": "# Historia\n",
            "apuntes.md": "# Lo que no se reconoce\n",
        })
        antes = _retrato(carpeta)

        core.traer(proyecto)

        despues = _retrato(carpeta)
        self.assertEqual(sorted(antes), sorted(despues),
                         "cambió la lista de archivos del proyecto")
        for nombre, contenido in antes.items():
            self.assertEqual(contenido, despues[nombre],
                             "cambió el archivo %s del proyecto" % nombre)

    def test_lo_traido_queda_dentro_de_los_datos_de_la_plataforma(self):
        proyecto, carpeta = self.proyecto_con(
            {"epicas/EP-001/epica.md": "# Épica\n"})

        core.traer(proyecto)

        adentro = os.path.join(self.datos, "proyectos", proyecto.identificador,
                               "traido", "documentacion", "epicas", "EP-001",
                               "epica.md")
        self.assertTrue(os.path.isfile(adentro))
        self.assertFalse(os.path.exists(os.path.join(carpeta, "traido")))


class IndiceTests(BaseImportacion):
    """El índice de lo traído se rehace desde los archivos copiados."""

    def test_el_indice_se_rehace_desde_el_texto(self):
        proyecto, _ = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Épica\n",
            "epicas/EP-001/HU-001-algo.md": "# Historia\n",
        })
        core.traer(proyecto)
        Traido.objects.all().delete()

        cuantos = core.reconstruir_indice()

        self.assertEqual(cuantos, 2)
        self.assertEqual(Traido.objects.count(), 2)


class CasoRealTests(TestCase):
    """CP-008 · se trae este mismo repositorio, que es el caso más grande.

    **No es un conejillo:** lo que se comprueba acá es justamente que traer no
    lo toque. La comparación de sus archivos es parte de la prueba.
    """

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-caso-real-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos)
        self.contexto.enable()

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.datos, ignore_errors=True)

    def test_se_trae_el_repositorio_del_estandar(self):
        from django.conf import settings
        repositorio = str(settings.CARPETA_VALIDADORES.parent)
        proyecto, _ = proyectos.conectar("Cimiento", repositorio)

        cuantos_antes = _cuantos_md(os.path.join(repositorio, "documentacion"))

        arranca = time.time()
        hallazgo, nuevos, _ = core.traer(proyecto)
        tardo = time.time() - arranca

        self.assertGreater(nuevos, 900, "entraron menos de los esperados")
        self.assertEqual(nuevos, hallazgo.cuantos)
        self.assertEqual(_cuantos_md(os.path.join(repositorio, "documentacion")),
                         cuantos_antes,
                         "cambió la cantidad de archivos del repositorio")

        print("\n   CP-008: %d documentos reconocidos, %d sin reconocer, "
              "en %.2f s" % (nuevos, len(hallazgo.sin_reconocer), tardo))
        print("   CP-008: por tipo -> %s" % ", ".join(
            "%s: %d" % (t, c) for t, c in hallazgo.por_tipo))
        if hallazgo.sin_reconocer:
            print("   CP-008: sin reconocer -> %s"
                  % ", ".join(hallazgo.sin_reconocer))


def _cuantos_md(carpeta):
    return sum(1 for r, _, a in os.walk(carpeta)
               for n in a if n.endswith(".md"))
