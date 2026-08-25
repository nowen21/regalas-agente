# -*- coding: utf-8 -*-
"""Los nueve casos del plan de pruebas de la fase B.

El que más daño evita es `CP-009`: comparar la carpeta del proyecto archivo por
archivo, antes y después de conectarlo. La plataforma administra carpetas
ajenas, y escribir donde no debe es el error que nadie perdona.

**Ninguna carpeta real del usuario se usa como conejillo.** Todos los proyectos
de estas pruebas se crean y se borran acá mismo.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.auditoria.models import Registro
from . import core
from .models import Proyecto


def _escribir(ruta, texto):
    carpeta = os.path.dirname(ruta)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as archivo:
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


class BaseProyectos(TestCase):
    """Cada prueba corre sobre su propia carpeta de datos y sus propios proyectos."""

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

    def proyecto_de_mentira(self, version="34.1.0", con_git=True,
                            con_claude=True):
        """Una carpeta que se parece a un proyecto, y que esta prueba borra."""
        carpeta = tempfile.mkdtemp(prefix="prueba-proyecto-")
        self.ajenas.append(carpeta)
        _escribir(os.path.join(carpeta, "codigo.py"), "# el codigo del proyecto\n")
        if con_claude:
            declara = ("**Versión del estándar adoptada:** `%s`\n" % version
                       if version else "Sin versión declarada todavía.\n")
            _escribir(os.path.join(carpeta, "CLAUDE.md"),
                      "# El proyecto\n\n" + declara)
        if con_git:
            os.makedirs(os.path.join(carpeta, ".git"), exist_ok=True)
            _escribir(os.path.join(carpeta, ".git", "HEAD"),
                      "ref: refs/heads/main\n")
        return carpeta


class ConectarTests(BaseProyectos):
    """CP-001 · un proyecto queda conectado."""

    def test_el_proyecto_queda_con_lo_que_lo_identifica(self):
        carpeta = self.proyecto_de_mentira()

        proyecto, avisos = core.conectar("Mi Proyecto Ñandú", carpeta)

        self.assertEqual(proyecto.nombre, "Mi Proyecto Ñandú")
        self.assertEqual(proyecto.ruta_codigo, carpeta)
        self.assertEqual(proyecto.version_reglas, "34.1.0")
        self.assertTrue(proyecto.conectado)
        self.assertEqual(proyecto.estado, "sin empezar")
        self.assertEqual(avisos, [])

    def test_el_identificador_sirve_como_nombre_de_carpeta(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Mi Proyecto Ñandú", carpeta)
        self.assertEqual(proyecto.identificador, "mi-proyecto-nandu")

    def test_su_ficha_queda_escrita_y_se_lee_sin_la_plataforma(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Uno", carpeta)

        ficha = os.path.join(self.datos, "proyectos", proyecto.identificador,
                             "proyecto.md")
        self.assertTrue(os.path.isfile(ficha))
        with io.open(ficha, encoding="utf-8") as abierto:
            texto = abierto.read()
        self.assertIn("Uno", texto)
        self.assertIn(carpeta, texto)

    def test_dos_proyectos_con_el_mismo_nombre_no_se_pisan(self):
        primera = self.proyecto_de_mentira()
        segunda = self.proyecto_de_mentira()

        uno, _ = core.conectar("Igual", primera)
        dos, _ = core.conectar("Igual", segunda)

        self.assertNotEqual(uno.identificador, dos.identificador)
        self.assertEqual(Proyecto.objects.count(), 2)

    def test_el_indice_se_rehace_desde_las_fichas(self):
        core.conectar("Uno", self.proyecto_de_mentira())
        core.conectar("Dos", self.proyecto_de_mentira())
        Proyecto.objects.all().delete()

        cuantos = core.reconstruir_indice()

        self.assertEqual(cuantos, 2)
        self.assertEqual(
            sorted(Proyecto.objects.values_list("nombre", flat=True)),
            ["Dos", "Uno"])


class RechazosTests(BaseProyectos):
    """CP-002, CP-003 y CP-004 · lo que no se registra, y por qué."""

    def test_la_ruta_que_no_existe_se_rechaza_y_dice_cual_era(self):
        inventada = os.path.join(self.datos, "no-existe-esta-carpeta")

        with self.assertRaises(core.RutaQueNoExiste) as fallo:
            core.conectar("Fantasma", inventada)

        self.assertIn(inventada, str(fallo.exception))
        self.assertEqual(Proyecto.objects.count(), 0)

    def test_la_ruta_ya_registrada_dice_que_proyecto_la_tiene(self):
        carpeta = self.proyecto_de_mentira()
        core.conectar("El Primero", carpeta)

        with self.assertRaises(core.RutaYaRegistrada) as fallo:
            core.conectar("El Segundo", carpeta)

        self.assertIn("El Primero", str(fallo.exception))
        self.assertEqual(Proyecto.objects.count(), 1)

    def test_la_misma_carpeta_escrita_distinto_es_la_misma_carpeta(self):
        carpeta = self.proyecto_de_mentira()
        core.conectar("El Primero", carpeta)
        otra_forma = carpeta.upper() if os.name == "nt" else carpeta + os.sep

        with self.assertRaises(core.RutaYaRegistrada):
            core.conectar("El Segundo", otra_forma)

    def test_una_version_que_no_existe_se_rechaza(self):
        carpeta = self.proyecto_de_mentira(version="999.0.0")

        with self.assertRaises(core.VersionQueNoExiste) as fallo:
            core.conectar("Inventado", carpeta)

        self.assertIn("999.0.0", str(fallo.exception))
        self.assertEqual(Proyecto.objects.count(), 0)

    def test_nada_se_escribe_cuando_se_rechaza(self):
        """Un rechazo que igual dejó archivos es peor que no rechazar."""
        antes = os.listdir(self.datos) if os.path.isdir(self.datos) else []

        with self.assertRaises(core.RutaQueNoExiste):
            core.conectar("Fantasma", os.path.join(self.datos, "no-existe"))

        despues = os.listdir(self.datos) if os.path.isdir(self.datos) else []
        self.assertEqual(antes, despues)
        self.assertEqual(Registro.objects.count(), 0)


class AvisosTests(BaseProyectos):
    """CP-005 y CP-008 · lo que se avisa sin impedir conectar."""

    def test_la_carpeta_sin_control_de_versiones_se_conecta_con_aviso(self):
        carpeta = self.proyecto_de_mentira(con_git=False)

        proyecto, avisos = core.conectar("Sin respaldo", carpeta)

        self.assertEqual(Proyecto.objects.count(), 1)
        self.assertTrue(proyecto.pk)
        self.assertTrue(any("respaldo" in aviso for aviso in avisos))

    def test_el_proyecto_sin_estandar_instalado_se_conecta_con_aviso(self):
        """CP-008. Vacío no es lo mismo que falso: uno entra, el otro no."""
        carpeta = self.proyecto_de_mentira(con_claude=False)

        proyecto, avisos = core.conectar("Todavía sin estándar", carpeta)

        self.assertEqual(Proyecto.objects.count(), 1)
        self.assertEqual(proyecto.version_reglas, "")
        self.assertFalse(proyecto.adopto_el_estandar)
        self.assertTrue(any("no declara" in aviso for aviso in avisos))

    def test_el_claude_sin_version_declarada_tambien_se_conecta(self):
        carpeta = self.proyecto_de_mentira(version="")

        proyecto, avisos = core.conectar("Con CLAUDE pero sin versión", carpeta)

        self.assertEqual(proyecto.version_reglas, "")
        self.assertTrue(any("no declara" in aviso for aviso in avisos))

    def test_vacio_y_falso_no_se_resuelven_igual(self):
        """Si los dos caminos se juntan, uno de los dos casos quedó mal."""
        sin_nada = self.proyecto_de_mentira(con_claude=False)
        inventada = self.proyecto_de_mentira(version="999.0.0")

        core.conectar("El que no declara", sin_nada)
        with self.assertRaises(core.VersionQueNoExiste):
            core.conectar("El que inventa", inventada)

        self.assertEqual(Proyecto.objects.count(), 1)


class AuditoriaTests(BaseProyectos):
    """CP-006 · conectar deja su registro."""

    def test_conectar_deja_exactamente_un_registro(self):
        carpeta = self.proyecto_de_mentira()
        antes = Registro.objects.count()

        proyecto, _ = core.conectar("Auditado", carpeta, quien="el agente",
                                    sesion="5f06ce4e")

        self.assertEqual(Registro.objects.count(), antes + 1)
        registro = Registro.objects.last()
        self.assertEqual(registro.que_se_hizo, "conectar un proyecto")
        self.assertEqual(registro.proyecto, proyecto.identificador)
        self.assertEqual(registro.sesion, "5f06ce4e")
        self.assertEqual(registro.quien, "el agente")

    def test_si_no_se_puede_registrar_el_proyecto_no_queda_conectado(self):
        """La constancia va antes que el efecto, también acá."""
        carpeta = self.proyecto_de_mentira()
        estorbo = os.path.join(self.datos, "auditoria")
        os.makedirs(self.datos, exist_ok=True)
        _escribir(estorbo, "no soy una carpeta")

        from nucleo.auditoria import core as auditoria
        with self.assertRaises(auditoria.RegistroNoSePudoEscribir):
            core.conectar("No debería quedar", carpeta)

        self.assertEqual(Proyecto.objects.count(), 0)
        self.assertFalse(os.path.isdir(os.path.join(self.datos, "proyectos")))


class PantallasTests(BaseProyectos):
    """CP-007 · se ve la lista y se entra a un proyecto."""

    def test_la_lista_vacia_lo_dice(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("Todavía no hay ningún proyecto conectado",
                      respuesta.content.decode("utf-8"))

    def test_la_lista_trae_los_proyectos_conectados(self):
        core.conectar("Uno", self.proyecto_de_mentira())
        core.conectar("Dos", self.proyecto_de_mentira())

        cuerpo = self.client.get("/").content.decode("utf-8")

        self.assertIn("Uno", cuerpo)
        self.assertIn("Dos", cuerpo)
        self.assertIn("sin empezar", cuerpo)

    def test_se_entra_a_un_proyecto_y_trae_lo_suyo(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El Mío", carpeta)

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("El Mío", cuerpo)
        self.assertIn(carpeta, cuerpo)
        self.assertIn("34.1.0", cuerpo)

    def test_se_conecta_desde_la_pantalla(self):
        carpeta = self.proyecto_de_mentira()

        respuesta = self.client.post("/conectar/",
                                     {"nombre": "Desde la pantalla",
                                      "ruta": carpeta})

        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("Quedó conectado", respuesta.content.decode("utf-8"))
        self.assertEqual(Proyecto.objects.count(), 1)

    def test_el_rechazo_se_ve_en_la_pantalla_y_no_se_pierde_lo_escrito(self):
        respuesta = self.client.post("/conectar/",
                                     {"nombre": "Fantasma",
                                      "ruta": "/ruta/que/no/existe"})
        cuerpo = respuesta.content.decode("utf-8")

        self.assertIn("No existe la carpeta", cuerpo)
        self.assertIn("Fantasma", cuerpo)
        self.assertEqual(Proyecto.objects.count(), 0)

    def test_el_aviso_de_no_haber_adoptado_el_estandar_se_ve(self):
        proyecto, _ = core.conectar(
            "Sin estándar", self.proyecto_de_mentira(con_claude=False))

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("no declara", cuerpo)


class NoTocarElProyectoTests(BaseProyectos):
    """CP-009 · que NO pase: que conectar toque la carpeta del proyecto.

    Es `RN-1`: registrar es una anotación de la plataforma, no una
    intervención. Se compara la carpeta entera, archivo por archivo, con su
    contenido y su fecha.
    """

    def test_la_carpeta_del_proyecto_queda_intacta(self):
        carpeta = self.proyecto_de_mentira()
        antes = _retrato(carpeta)

        core.conectar("Intacto", carpeta)

        despues = _retrato(carpeta)
        self.assertEqual(sorted(antes), sorted(despues),
                         "cambió la lista de archivos del proyecto")
        for nombre, contenido in antes.items():
            self.assertEqual(contenido, despues[nombre],
                             "cambió el archivo %s del proyecto" % nombre)

    def test_tampoco_se_toca_cuando_se_rechaza(self):
        carpeta = self.proyecto_de_mentira(version="999.0.0")
        antes = _retrato(carpeta)

        with self.assertRaises(core.VersionQueNoExiste):
            core.conectar("Rechazado", carpeta)

        self.assertEqual(antes, _retrato(carpeta))

    def test_lo_que_la_plataforma_escribe_queda_dentro_de_sus_datos(self):
        carpeta = self.proyecto_de_mentira()
        core.conectar("Uno", carpeta)

        ficha = os.path.join(self.datos, "proyectos", "uno", "proyecto.md")
        self.assertTrue(os.path.isfile(ficha))
        self.assertFalse(os.path.exists(os.path.join(carpeta, "proyecto.md")))
