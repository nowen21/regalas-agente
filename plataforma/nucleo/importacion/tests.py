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


class ReporteTests(BaseImportacion):
    """CP-001, CP-003 y CP-004 · qué dice el reporte guardado."""

    CON_MOLDE = {
        "epicas/EP-001/epica.md": "# La épica" + chr(10),
        "epicas/EP-001/HU-001-algo.md": "# La historia" + chr(10),
    }
    SIN_MOLDE = {
        "apuntes.md": "# Apuntes" + chr(10),
        "borrador.md": "# Borrador" + chr(10),
        "epicas/notas.md": "# Notas" + chr(10),
    }

    def _texto_del_ultimo_reporte(self, proyecto):
        reportes = core.reportes_de(proyecto)
        self.assertTrue(reportes, "no se escribió ningún reporte")
        return core.leer_reporte(reportes[0][1])

    def test_el_reporte_lista_lo_no_reconocido_con_su_ruta(self):
        documentos = dict(self.CON_MOLDE)
        documentos.update(self.SIN_MOLDE)
        proyecto, _ = self.proyecto_con(documentos)

        core.traer(proyecto)
        texto = self._texto_del_ultimo_reporte(proyecto)

        self.assertIn("3", texto)
        for nombre in ("apuntes.md", "borrador.md", "notas.md"):
            self.assertIn(nombre, texto,
                          "el reporte no nombra %s" % nombre)

    def test_el_reporte_dice_cuantos_entraron_y_cuantos_no(self):
        documentos = dict(self.CON_MOLDE)
        documentos.update(self.SIN_MOLDE)
        proyecto, _ = self.proyecto_con(documentos)

        core.traer(proyecto)
        texto = self._texto_del_ultimo_reporte(proyecto)

        self.assertIn("Documentos que entraron", texto)
        self.assertIn("Que NO entraron", texto)

    def test_cuando_no_quedo_nada_afuera_el_reporte_lo_dice(self):
        """CP-003. El reporte se escribe **siempre**, también si salió limpio."""
        proyecto, _ = self.proyecto_con(self.CON_MOLDE)

        core.traer(proyecto)
        texto = self._texto_del_ultimo_reporte(proyecto)

        self.assertIn("Nada quedó afuera", texto)

    def test_el_reporte_existe_aunque_no_haya_nada_que_reportar(self):
        """Su ausencia no distinguiría entre «salió limpio» y «no se corrió»."""
        proyecto, _ = self.proyecto_con(self.CON_MOLDE)

        core.traer(proyecto)

        self.assertEqual(len(core.reportes_de(proyecto)), 1)

    def test_el_reporte_dice_que_carpetas_no_se_miraron(self):
        """CP-004. Es la otra mitad de lo que no entró."""
        proyecto, _ = self.proyecto_con(
            self.CON_MOLDE,
            extras={"base/00-nucleo.md": "# Reglas" + chr(10),
                    "pendientes/1-algo.md": "# Pendiente" + chr(10)})

        core.traer(proyecto)
        texto = self._texto_del_ultimo_reporte(proyecto)

        self.assertIn("base/", texto)
        self.assertIn("pendientes/", texto)
        self.assertIn("no es documentación del ciclo", texto,
                      "el reporte nombra las carpetas pero no dice por qué")

    def test_el_reporte_se_lee_sin_la_plataforma(self):
        proyecto, _ = self.proyecto_con(self.CON_MOLDE)
        core.traer(proyecto)

        _, ruta = core.reportes_de(proyecto)[0]
        completa = os.path.join(self.datos, ruta.replace("/", os.sep))
        with io.open(completa, encoding="utf-8") as abierto:
            texto = abierto.read()

        self.assertTrue(texto.startswith("# Qué no entró al traer"))


class ReporteQuedaGuardadoTests(BaseImportacion):
    """CP-002 · el reporte se puede volver a mirar sin traer otra vez.

    Es lo único que esta fase construye de cero, y la razón por la que existe:
    antes, el registro de auditoría decía cuántos documentos habían quedado
    afuera, **no cuáles**. Para saberlo había que traer el proyecto entero.
    """

    def test_el_reporte_sale_con_la_carpeta_del_proyecto_borrada(self):
        proyecto, carpeta = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Épica" + chr(10),
            "apuntes.md": "# Lo que no entra" + chr(10),
        })
        core.traer(proyecto)

        shutil.rmtree(carpeta, ignore_errors=True)

        reportes = core.reportes_de(proyecto)
        self.assertEqual(len(reportes), 1)
        texto = core.leer_reporte(reportes[0][1])
        self.assertIn("apuntes.md", texto,
                      "el reporte no sobrevivió a borrar el proyecto")

    def test_no_hace_falta_traer_otra_vez_para_mirarlo(self):
        proyecto, _ = self.proyecto_con({"apuntes.md": "# Nada" + chr(10)})
        core.traer(proyecto)
        cuantos_registros = Registro.objects.count()

        texto = core.leer_reporte(core.reportes_de(proyecto)[0][1])

        self.assertIn("apuntes.md", texto)
        # Mirar el reporte no es una acción que cambie nada: no registra.
        self.assertEqual(Registro.objects.count(), cuantos_registros)


class ReporteEnLaAuditoriaTests(BaseImportacion):
    """CP-005 · el registro dice dónde está el reporte, y no repite la lista."""

    def test_el_registro_trae_la_ruta_del_reporte(self):
        proyecto, _ = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Épica" + chr(10),
            "apuntes.md": "# Lo que no entra" + chr(10),
        })

        core.traer(proyecto)

        registro = Registro.objects.get(
            que_se_hizo="traer la documentación de un proyecto")
        self.assertIn("reportes/", registro.que_cambio)
        self.assertIn("lo-que-no-entro", registro.que_cambio)

    def test_el_registro_no_repite_la_lista(self):
        """Dos copias de lo mismo se separan. El registro enlaza, no copia."""
        proyecto, _ = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Épica" + chr(10),
            "apuntes.md": "# Uno" + chr(10),
            "borrador.md": "# Otro" + chr(10),
        })

        core.traer(proyecto)

        registro = Registro.objects.get(
            que_se_hizo="traer la documentación de un proyecto")
        self.assertNotIn("apuntes.md", registro.que_cambio)
        self.assertNotIn("borrador.md", registro.que_cambio)
        # Pero sí dice cuántos, que es lo que la auditoría necesita saber.
        self.assertIn("2 sin reconocer", registro.que_cambio)

    def test_del_registro_se_llega_al_reporte(self):
        proyecto, _ = self.proyecto_con({"apuntes.md": "# Uno" + chr(10)})
        core.traer(proyecto)

        registro = Registro.objects.get(
            que_se_hizo="traer la documentación de un proyecto")
        ruta = registro.que_cambio.split("El detalle, en ")[-1].strip()

        self.assertIn("apuntes.md", core.leer_reporte(ruta))


class DosReportesTests(BaseImportacion):
    """CP-006 · dos traídas dejan dos reportes, y se ve qué cambió."""

    def test_el_segundo_reporte_no_pisa_al_primero(self):
        import time
        carpeta_documentos = {
            "epicas/EP-001/epica.md": "# Épica" + chr(10),
            "uno.md": "# Uno" + chr(10),
            "dos.md": "# Dos" + chr(10),
            "tres.md": "# Tres" + chr(10),
        }
        proyecto, carpeta = self.proyecto_con(carpeta_documentos)
        core.traer(proyecto)

        # Se «corrige» uno: pasa a llamarse como un molde conocido.
        os.remove(os.path.join(carpeta, "documentacion", "uno.md"))
        _escribir(os.path.join(carpeta, "documentacion", "senales.md"),
                  "# Señales" + chr(10))
        time.sleep(1.1)          # para que el nombre del reporte sea otro
        core.traer(proyecto)

        reportes = core.reportes_de(proyecto)
        self.assertEqual(len(reportes), 2, "el segundo reporte pisó al primero")

        nuevo = core.leer_reporte(reportes[0][1])
        viejo = core.leer_reporte(reportes[1][1])
        self.assertIn("uno.md", viejo)
        self.assertNotIn("uno.md", nuevo)

    def test_estan_del_mas_nuevo_al_mas_viejo(self):
        import time
        proyecto, _ = self.proyecto_con({"apuntes.md": "# Uno" + chr(10)})
        core.traer(proyecto)
        time.sleep(1.1)
        core.traer(proyecto)

        reportes = core.reportes_de(proyecto)

        self.assertEqual(len(reportes), 2)
        self.assertGreater(reportes[0][0], reportes[1][0])


class PantallaDeReportesTests(BaseImportacion):
    """CP-007 · los reportes se ven desde la pantalla del proyecto."""

    def test_sin_traidas_la_pantalla_lo_dice(self):
        proyecto, _ = self.proyecto_con({"epicas/EP-001/epica.md": "# Épica\n"})

        cuerpo = self.client.get(
            "/proyecto/%s/reportes/" % proyecto.identificador
        ).content.decode("utf-8")

        self.assertIn("todavía no se ha traído", cuerpo)

    def test_con_traidas_se_ven_con_su_fecha(self):
        proyecto, _ = self.proyecto_con({"apuntes.md": "# Uno" + chr(10)})
        core.traer(proyecto)

        cuerpo = self.client.get(
            "/proyecto/%s/reportes/" % proyecto.identificador
        ).content.decode("utf-8")

        self.assertIn("Ver el reporte", cuerpo)
        self.assertIn(core.reportes_de(proyecto)[0][0], cuerpo)

    def test_se_abre_un_reporte_y_trae_su_texto(self):
        proyecto, _ = self.proyecto_con({"apuntes.md": "# Uno" + chr(10)})
        core.traer(proyecto)
        cuando = core.reportes_de(proyecto)[0][0]

        cuerpo = self.client.get(
            "/proyecto/%s/reportes/%s/" % (proyecto.identificador, cuando)
        ).content.decode("utf-8")

        self.assertIn("apuntes.md", cuerpo)

    def test_un_reporte_que_no_existe_da_404(self):
        proyecto, _ = self.proyecto_con({"apuntes.md": "# Uno" + chr(10)})

        respuesta = self.client.get(
            "/proyecto/%s/reportes/2020-01-01-000000/"
            % proyecto.identificador)

        self.assertEqual(respuesta.status_code, 404)

    def test_desde_el_proyecto_se_llega_a_los_reportes(self):
        proyecto, _ = self.proyecto_con({"apuntes.md": "# Uno" + chr(10)})

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("Ver qué no entró en cada traída", cuerpo)


class ElReporteNoTocaNadaTests(BaseImportacion):
    """CP-008 · que NO pase: que lo no reconocido entre o se toque.

    Escribir el reporte no puede volverse una excusa para tocar lo que se
    reporta.
    """

    def test_lo_no_reconocido_no_entra_y_su_carpeta_no_cambia(self):
        proyecto, carpeta = self.proyecto_con({
            "epicas/EP-001/epica.md": "# Épica" + chr(10),
            "apuntes.md": "# Lo que no entra" + chr(10),
        })
        antes = _retrato(carpeta)

        core.traer(proyecto)

        self.assertEqual(Traido.objects.filter(
            proyecto=proyecto.identificador).count(), 1)
        despues = _retrato(carpeta)
        self.assertEqual(sorted(antes), sorted(despues))
        for nombre, contenido in antes.items():
            self.assertEqual(contenido, despues[nombre],
                             "cambió %s del proyecto" % nombre)

    def test_el_reporte_queda_en_los_datos_y_no_en_el_proyecto(self):
        proyecto, carpeta = self.proyecto_con({"apuntes.md": "# Uno" + chr(10)})

        core.traer(proyecto)

        adentro = os.path.join(self.datos, "proyectos",
                               proyecto.identificador, "reportes")
        self.assertTrue(os.path.isdir(adentro))
        self.assertFalse(os.path.exists(os.path.join(carpeta, "reportes")))
