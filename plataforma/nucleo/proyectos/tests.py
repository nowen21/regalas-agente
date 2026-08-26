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


class DesconectarTests(BaseProyectos):
    """CP-001 y CP-002 · desconectar saca y no borra, y la marca vive en el texto."""

    def _con_documentacion(self, nombre="Con papeles"):
        """Un proyecto conectado que ya tiene algo escrito en su carpeta."""
        from nucleo.almacen import core as almacen
        from nucleo.auditoria import core as auditoria
        proyecto, _ = core.conectar(nombre, self.proyecto_de_mentira())
        documento = "proyectos/%s/analisis.md" % proyecto.identificador
        auditoria.con_constancia(
            lambda c: almacen.guardar(documento, "# El análisis" + chr(10), c),
            que_se_hizo="guardar un documento", sobre_que=documento,
            quien="el agente")
        return proyecto, documento

    def test_desconectar_lo_saca_de_la_lista(self):
        proyecto, _ = self._con_documentacion()

        core.desconectar(proyecto)

        vuelto = Proyecto.objects.get(identificador=proyecto.identificador)
        self.assertFalse(vuelto.esta_conectado)
        self.assertTrue(vuelto.desconectado)
        self.assertEqual(Proyecto.objects.filter(desconectado="").count(), 0)

    def test_su_documentacion_sigue_con_lo_que_tenia(self):
        """Que la carpeta exista no basta: una carpeta vacía también existe."""
        from nucleo.almacen import core as almacen
        proyecto, documento = self._con_documentacion()
        antes = almacen.leer(documento)

        core.desconectar(proyecto)

        self.assertEqual(almacen.leer(documento), antes)
        self.assertEqual(antes, "# El análisis" + chr(10))

    def test_rehacer_el_indice_no_lo_resucita(self):
        """CP-002. Si la marca viviera solo en la base, volvería solo."""
        proyecto, _ = self._con_documentacion()
        core.desconectar(proyecto)
        Proyecto.objects.all().delete()

        core.reconstruir_indice()

        vuelto = Proyecto.objects.get(identificador=proyecto.identificador)
        self.assertFalse(vuelto.esta_conectado)

    def test_la_marca_esta_en_la_ficha_y_no_solo_en_el_indice(self):
        proyecto, _ = self._con_documentacion()
        core.desconectar(proyecto)

        ficha = os.path.join(self.datos, "proyectos", proyecto.identificador,
                             "proyecto.md")
        with io.open(ficha, encoding="utf-8") as abierto:
            texto = abierto.read()
        self.assertIn("Fecha de desconexión", texto)
        self.assertNotIn("sigue conectado", texto)

    def test_desconectar_queda_en_la_auditoria(self):
        proyecto, _ = self._con_documentacion()
        antes = Registro.objects.count()

        core.desconectar(proyecto, quien="el agente", sesion="5f06ce4e")

        self.assertEqual(Registro.objects.count(), antes + 1)
        # Se busca por lo que se hizo, no con `last()`: la marca de tiempo del
        # registro tiene precisión de segundos, y en una prueba las tres
        # acciones caen en el mismo segundo. El orden entre ellas queda
        # indeterminado, y eso quedó anotado como deuda de la fase.
        registro = Registro.objects.get(que_se_hizo="desconectar un proyecto")
        self.assertEqual(registro.sesion, "5f06ce4e")
        self.assertEqual(registro.proyecto, proyecto.identificador)


class RenombrarTests(BaseProyectos):
    """CP-003 · renombrar cambia el nombre y no mueve la carpeta."""

    def test_el_nombre_cambia_y_la_carpeta_es_la_misma(self):
        proyecto, _ = core.conectar("Nombre Viejo", self.proyecto_de_mentira())
        carpeta = os.path.join(self.datos, "proyectos", proyecto.identificador)
        antes = _retrato(carpeta)

        renombrado = core.renombrar(proyecto, "Nombre Nuevo")

        self.assertEqual(renombrado.nombre, "Nombre Nuevo")
        self.assertEqual(renombrado.identificador, proyecto.identificador)
        self.assertTrue(os.path.isdir(carpeta))
        self.assertEqual(sorted(antes), sorted(_retrato(carpeta)))

    def test_el_nombre_nuevo_queda_en_la_ficha(self):
        proyecto, _ = core.conectar("Nombre Viejo", self.proyecto_de_mentira())
        core.renombrar(proyecto, "Nombre Nuevo")

        Proyecto.objects.all().delete()
        core.reconstruir_indice()

        self.assertEqual(Proyecto.objects.first().nombre, "Nombre Nuevo")

    def test_no_se_puede_dejar_sin_nombre(self):
        proyecto, _ = core.conectar("Tiene Nombre", self.proyecto_de_mentira())

        with self.assertRaises(core.NombreVacio):
            core.renombrar(proyecto, "   ")

        self.assertEqual(
            Proyecto.objects.get(pk=proyecto.pk).nombre, "Tiene Nombre")


class CorregirVersionTests(BaseProyectos):
    """CP-004 · corregir la versión la vuelve a comprobar."""

    def test_la_version_corregida_se_relee_del_proyecto(self):
        carpeta = self.proyecto_de_mentira(version="")
        proyecto, _ = core.conectar("Sin versión", carpeta)
        self.assertEqual(proyecto.version_reglas, "")

        _escribir(os.path.join(carpeta, "CLAUDE.md"),
                  "**Versión del estándar adoptada:** `34.1.0`" + chr(10))
        corregido = core.corregir_version(proyecto)

        self.assertEqual(corregido.version_reglas, "34.1.0")

    def test_una_version_que_no_existe_no_se_guarda(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Con versión", carpeta)

        _escribir(os.path.join(carpeta, "CLAUDE.md"),
                  "**Versión del estándar adoptada:** `999.0.0`" + chr(10))
        with self.assertRaises(core.VersionQueNoExiste):
            core.corregir_version(proyecto)

        self.assertEqual(
            Proyecto.objects.get(pk=proyecto.pk).version_reglas, "34.1.0")

    def test_corregir_no_escribe_dentro_del_proyecto(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Solo lectura", carpeta)
        antes = _retrato(carpeta)

        core.corregir_version(proyecto)

        self.assertEqual(antes, _retrato(carpeta))


class ConfirmacionTests(BaseProyectos):
    """CP-005 · los cambios preguntan antes, y quedan registrados."""

    def test_desconectar_pregunta_antes_y_no_cambia_nada(self):
        proyecto, _ = core.conectar("Preguntón", self.proyecto_de_mentira())
        antes = Registro.objects.count()

        respuesta = self.client.post(
            "/proyecto/%s/desconectar/" % proyecto.identificador)
        cuerpo = respuesta.content.decode("utf-8")

        self.assertIn("Qué va a pasar", cuerpo)
        self.assertIn("Qué NO va a pasar", cuerpo)
        self.assertIn("documentación se queda", cuerpo)
        self.assertTrue(Proyecto.objects.get(pk=proyecto.pk).esta_conectado)
        self.assertEqual(Registro.objects.count(), antes)

    def test_al_confirmar_si_cambia_y_queda_registrado(self):
        proyecto, _ = core.conectar("Confirmado", self.proyecto_de_mentira())
        antes = Registro.objects.count()

        self.client.post("/proyecto/%s/desconectar/" % proyecto.identificador,
                         {"confirmado": "si"})

        self.assertFalse(Proyecto.objects.get(pk=proyecto.pk).esta_conectado)
        self.assertEqual(Registro.objects.count(), antes + 1)

    def test_renombrar_pregunta_antes(self):
        proyecto, _ = core.conectar("Antes", self.proyecto_de_mentira())

        respuesta = self.client.post(
            "/proyecto/%s/renombrar/" % proyecto.identificador)

        self.assertIn("no se mueve", respuesta.content.decode("utf-8"))
        self.assertEqual(Proyecto.objects.get(pk=proyecto.pk).nombre, "Antes")

    def test_corregir_version_pregunta_antes(self):
        proyecto, _ = core.conectar("Versión", self.proyecto_de_mentira())

        respuesta = self.client.post(
            "/proyecto/%s/corregir-version/" % proyecto.identificador)

        self.assertIn("solo se lee", respuesta.content.decode("utf-8"))


class DesconectadosSeVenTests(BaseProyectos):
    """CP-006 · los desconectados se ven, y se ve que su documentación sigue."""

    def test_la_lista_los_muestra_aparte(self):
        core.conectar("El que sigue", self.proyecto_de_mentira())
        fuera, _ = core.conectar("El que salió", self.proyecto_de_mentira())
        core.desconectar(fuera)

        cuerpo = self.client.get("/").content.decode("utf-8")

        self.assertIn("El que sigue", cuerpo)
        self.assertIn("El que salió", cuerpo)
        self.assertIn("Desconectados", cuerpo)
        self.assertIn("documentación sigue guardada", cuerpo)

    def test_su_pantalla_dice_que_su_documentacion_sigue(self):
        fuera, _ = core.conectar("El que salió", self.proyecto_de_mentira())
        core.desconectar(fuera)

        cuerpo = self.client.get(
            "/proyecto/%s/" % fuera.identificador).content.decode("utf-8")

        self.assertIn("está desconectado", cuerpo)
        self.assertIn("sigue guardada", cuerpo)


class ReconectarTests(BaseProyectos):
    """CP-007 · reconectar la ruta de un desconectado lo reactiva."""

    def test_vuelve_el_mismo_proyecto_con_su_documentacion(self):
        from nucleo.almacen import core as almacen
        from nucleo.auditoria import core as auditoria
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El de siempre", carpeta)
        documento = "proyectos/%s/analisis.md" % proyecto.identificador
        auditoria.con_constancia(
            lambda c: almacen.guardar(documento, "# Lo suyo" + chr(10), c),
            que_se_hizo="guardar", sobre_que=documento, quien="el agente")
        core.desconectar(proyecto)

        vuelto, _ = core.conectar("Como se llame ahora", carpeta)

        self.assertEqual(vuelto.identificador, proyecto.identificador)
        self.assertTrue(vuelto.esta_conectado)
        self.assertEqual(almacen.leer(documento), "# Lo suyo" + chr(10))
        self.assertEqual(Proyecto.objects.count(), 1)

    def test_no_quedan_dos_proyectos_apuntando_a_la_misma_ruta(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Uno solo", carpeta)
        core.desconectar(proyecto)

        core.conectar("Otro nombre", carpeta)

        self.assertEqual(
            Proyecto.objects.filter(
                ruta_normalizada=core.ruta_normalizada(carpeta)).count(), 1)

    def test_la_ruta_de_un_desconectado_queda_libre(self):
        """Si siguiera tomada, desconectar no serviría para corregir el error."""
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Mal conectado", carpeta)
        core.desconectar(proyecto)

        vuelto, _ = core.conectar("Bien conectado", carpeta)

        self.assertTrue(vuelto.esta_conectado)

    def test_la_pantalla_avisa_antes_de_reactivar(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El de antes", carpeta)
        core.desconectar(proyecto)

        respuesta = self.client.post("/conectar/",
                                     {"nombre": "Otro", "ruta": carpeta})
        cuerpo = respuesta.content.decode("utf-8")

        self.assertIn("ya estuvo conectado", cuerpo)
        self.assertIn("empezar de cero", cuerpo)
        self.assertFalse(Proyecto.objects.get(pk=proyecto.pk).esta_conectado)

    def test_al_confirmar_si_reactiva(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El de antes", carpeta)
        core.desconectar(proyecto)

        self.client.post("/conectar/", {"nombre": "Otro", "ruta": carpeta,
                                        "confirmado": "si"})

        self.assertTrue(Proyecto.objects.get(pk=proyecto.pk).esta_conectado)


class DesconectarNoTocaElProyectoTests(BaseProyectos):
    """CP-008 · que NO pase: que desconectar toque la carpeta del proyecto.

    Es peor que al conectar: acá el usuario cree que está quitando algo, y si
    la plataforma se pasa de lista podría quitarlo del lado equivocado.
    """

    def test_la_carpeta_del_proyecto_queda_intacta(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Intacto", carpeta)
        antes = _retrato(carpeta)

        core.desconectar(proyecto)

        despues = _retrato(carpeta)
        self.assertEqual(sorted(antes), sorted(despues),
                         "cambió la lista de archivos del proyecto")
        for nombre, contenido in antes.items():
            self.assertEqual(contenido, despues[nombre],
                             "cambió el archivo %s del proyecto" % nombre)

    def test_renombrar_tampoco_lo_toca(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Intacto", carpeta)
        antes = _retrato(carpeta)

        core.renombrar(proyecto, "Otro nombre")

        self.assertEqual(antes, _retrato(carpeta))


class RutaPerdidaTests(BaseProyectos):
    """CP-001 y CP-002 · la ruta que se pierde se avisa, y no pierde nada."""

    def _con_la_ruta_perdida(self, nombre="El que se movió"):
        """Un proyecto conectado cuya carpeta de código ya no está."""
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar(nombre, carpeta)
        shutil.rmtree(carpeta, ignore_errors=True)
        return proyecto, carpeta

    def test_el_aviso_dice_que_ruta_se_busco(self):
        """`RN-2`. Decir solo «no existe» obliga al usuario a adivinar."""
        proyecto, carpeta = self._con_la_ruta_perdida()

        avisos = core.avisos_de(proyecto.ruta_codigo, proyecto.version_reglas)

        self.assertEqual(len(avisos), 1)
        self.assertIn(carpeta, avisos[0],
                      "el aviso no nombra la ruta que se buscó")

    def test_la_lista_lo_marca(self):
        proyecto, _ = self._con_la_ruta_perdida()

        cuerpo = self.client.get("/").content.decode("utf-8")

        self.assertIn("El que se movió", cuerpo)
        self.assertIn("Esa carpeta ya no está", cuerpo)

    def test_su_pantalla_nombra_la_ruta_que_se_busco(self):
        proyecto, carpeta = self._con_la_ruta_perdida()

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("ya no está donde estaba", cuerpo)
        self.assertIn(carpeta, cuerpo)

    def test_su_documentacion_sigue_a_la_vista(self):
        """CP-002. Perder la ruta no pierde nada: la documentación vive acá."""
        from nucleo.almacen import core as almacen
        from nucleo.auditoria import core as auditoria
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("Con papeles", carpeta)
        documento = "proyectos/%s/analisis.md" % proyecto.identificador
        auditoria.con_constancia(
            lambda c: almacen.guardar(documento, "# Lo suyo" + chr(10), c),
            que_se_hizo="guardar", sobre_que=documento, quien="el agente")

        shutil.rmtree(carpeta, ignore_errors=True)

        self.assertFalse(Proyecto.objects.get(pk=proyecto.pk).ruta_viva)
        self.assertEqual(almacen.leer(documento), "# Lo suyo" + chr(10))


class CorregirRutaTests(BaseProyectos):
    """CP-003, CP-004 y CP-005 · corregir la ruta, y lo que rechaza."""

    def test_corregir_la_ruta_quita_el_aviso(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", carpeta)
        shutil.rmtree(carpeta, ignore_errors=True)
        nueva = self.proyecto_de_mentira()

        corregido = core.corregir_ruta(proyecto, nueva)

        self.assertEqual(corregido.ruta_codigo, nueva)
        self.assertTrue(corregido.ruta_viva)
        self.assertEqual(
            core.avisos_de(corregido.ruta_codigo, corregido.version_reglas), [])

    def test_la_ruta_nueva_queda_en_la_ficha(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", carpeta)
        nueva = self.proyecto_de_mentira()
        core.corregir_ruta(proyecto, nueva)

        Proyecto.objects.all().delete()
        core.reconstruir_indice()

        self.assertEqual(Proyecto.objects.first().ruta_codigo, nueva)

    def test_el_registro_dice_de_donde_a_donde(self):
        """«Se corrigió la ruta» sin las dos rutas no sirve para rastrear."""
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", carpeta)
        nueva = self.proyecto_de_mentira()

        core.corregir_ruta(proyecto, nueva, quien="el agente", sesion="5f06ce4e")

        registro = Registro.objects.get(
            que_se_hizo="corregir la ruta de un proyecto")
        self.assertIn(carpeta, registro.que_cambio)
        self.assertIn(nueva, registro.que_cambio)
        self.assertEqual(registro.sesion, "5f06ce4e")

    def test_una_ruta_que_no_existe_se_rechaza_y_conserva_la_que_tenia(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", carpeta)
        inventada = os.path.join(self.datos, "no-existe-esta")

        with self.assertRaises(core.RutaQueNoExiste) as fallo:
            core.corregir_ruta(proyecto, inventada)

        self.assertIn(inventada, str(fallo.exception))
        self.assertEqual(
            Proyecto.objects.get(pk=proyecto.pk).ruta_codigo, carpeta)

    def test_una_ruta_de_otro_proyecto_se_rechaza(self):
        primera = self.proyecto_de_mentira()
        segunda = self.proyecto_de_mentira()
        uno, _ = core.conectar("El Primero", primera)
        dos, _ = core.conectar("El Segundo", segunda)

        with self.assertRaises(core.RutaYaRegistrada) as fallo:
            core.corregir_ruta(dos, primera)

        self.assertIn("El Primero", str(fallo.exception))
        self.assertEqual(Proyecto.objects.get(pk=dos.pk).ruta_codigo, segunda)

    def test_apuntar_a_su_propia_ruta_no_se_rechaza(self):
        """El proyecto no puede chocar consigo mismo."""
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El mismo", carpeta)

        corregido = core.corregir_ruta(proyecto, carpeta)

        self.assertEqual(corregido.ruta_codigo, carpeta)

    def test_corregir_la_ruta_relee_la_version_de_reglas(self):
        """CP-005. La carpeta cambió: lo que declara puede ser otra cosa.

        **La versión nueva tiene que quedar en la ficha, no solo en el
        índice.** Un sabotaje que quitaba la versión de la reescritura de la
        ficha pasó en verde con la primera forma de esta prueba: el objeto que
        devolvía la función traía la versión correcta y la ficha se quedaba con
        la vieja. Al rehacer el índice volvía la vieja, y nadie se enteraba.
        """
        vieja = self.proyecto_de_mentira(version="34.1.0")
        proyecto, _ = core.conectar("El que se movió", vieja)
        self.assertEqual(proyecto.version_reglas, "34.1.0")
        nueva = self.proyecto_de_mentira(con_claude=False)

        corregido = core.corregir_ruta(proyecto, nueva)

        self.assertEqual(corregido.version_reglas, "")

        # Lo que decide: que también haya quedado en el texto.
        Proyecto.objects.all().delete()
        core.reconstruir_indice()
        self.assertEqual(
            Proyecto.objects.first().version_reglas, "",
            "la versión nueva no quedó en la ficha: al rehacer el índice "
            "volvió la vieja")

    def test_una_carpeta_nueva_con_version_inventada_se_rechaza(self):
        vieja = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", vieja)
        nueva = self.proyecto_de_mentira(version="999.0.0")

        with self.assertRaises(core.VersionQueNoExiste):
            core.corregir_ruta(proyecto, nueva)

        self.assertEqual(Proyecto.objects.get(pk=proyecto.pk).ruta_codigo, vieja)

    def test_corregir_la_ruta_pregunta_antes(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", carpeta)

        respuesta = self.client.post(
            "/proyecto/%s/corregir-ruta/" % proyecto.identificador)
        cuerpo = respuesta.content.decode("utf-8")

        self.assertIn("Ninguna de las dos carpetas se toca", cuerpo)
        self.assertIn("No se copia ni se mueve código", cuerpo)
        self.assertEqual(
            Proyecto.objects.get(pk=proyecto.pk).ruta_codigo, carpeta)

    def test_el_rechazo_se_ve_en_la_pantalla(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", carpeta)

        respuesta = self.client.post(
            "/proyecto/%s/corregir-ruta/" % proyecto.identificador,
            {"confirmado": "si", "ruta": os.path.join(self.datos, "no-existe")})

        self.assertIn("No existe la carpeta",
                      respuesta.content.decode("utf-8"))


class RendimientoTests(BaseProyectos):
    """CP-006 · cincuenta proyectos listan bajo un segundo (`RNF-02`)."""

    def test_cincuenta_proyectos_listan_bajo_un_segundo(self):
        import time
        for numero in range(50):
            core.conectar("Proyecto %02d" % numero, self.proyecto_de_mentira())
        self.assertEqual(Proyecto.objects.count(), 50)

        arranca = time.time()
        respuesta = self.client.get("/")
        tardo = time.time() - arranca

        self.assertEqual(respuesta.status_code, 200)
        self.assertLess(tardo, 1.0,
                        "listar cincuenta proyectos tardó %.3f s" % tardo)
        # El número se escribe aunque cumpla: sin él no se puede comparar
        # cuando haya doscientos proyectos.
        print("\n   CP-006: listar 50 proyectos tardó %.3f s" % tardo)


class CorregirNoTocaLasCarpetasTests(BaseProyectos):
    """CP-007 · que NO pase: que corregir toque alguna de las dos carpetas.

    Se miran **las dos**, no solo la nueva: el descuido posible es «mover» el
    proyecto de verdad, y eso tocaría la vieja.
    """

    def test_ninguna_de_las_dos_carpetas_cambia(self):
        vieja = self.proyecto_de_mentira()
        nueva = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se mueve", vieja)
        retrato_vieja = _retrato(vieja)
        retrato_nueva = _retrato(nueva)

        core.corregir_ruta(proyecto, nueva)

        self.assertEqual(retrato_vieja, _retrato(vieja),
                         "cambió la carpeta vieja: se está moviendo código")
        self.assertEqual(retrato_nueva, _retrato(nueva),
                         "cambió la carpeta nueva")

    def test_tampoco_se_tocan_cuando_se_rechaza(self):
        vieja = self.proyecto_de_mentira()
        nueva = self.proyecto_de_mentira(version="999.0.0")
        proyecto, _ = core.conectar("El que se mueve", vieja)
        retrato_vieja = _retrato(vieja)
        retrato_nueva = _retrato(nueva)

        with self.assertRaises(core.VersionQueNoExiste):
            core.corregir_ruta(proyecto, nueva)

        self.assertEqual(retrato_vieja, _retrato(vieja))
        self.assertEqual(retrato_nueva, _retrato(nueva))


class BaseEstado(BaseProyectos):
    """Un proyecto con documentación traída, para calcularle el estado."""

    def _con_documentacion(self, ciclo=None, etapas=(), extras=None):
        """Arma un proyecto, le escribe documentación y la trae.

        `ciclo` son documentos dentro de `documentacion/`; `etapas` son nombres
        de etapas que tendrán su documento en `cvds/`.
        """
        from nucleo.importacion import core as importacion
        carpeta = self.proyecto_de_mentira()
        for relativa, texto in (ciclo or {}).items():
            _escribir(os.path.join(carpeta, "documentacion",
                                   relativa.replace("/", os.sep)), texto)
        for etapa in etapas:
            _escribir(os.path.join(carpeta, "cvds", etapa, "README.md"),
                      "# La etapa de %s" % etapa + chr(10))
        for relativa, texto in (extras or {}).items():
            _escribir(os.path.join(carpeta, relativa.replace("/", os.sep)), texto)
        proyecto, _ = core.conectar("El de la prueba", carpeta)
        importacion.traer(proyecto)
        return proyecto, carpeta


class EtapasQueEntranTests(BaseEstado):
    """CP-001 · las etapas del ciclo entran al traer.

    Este caso existe porque una fase cerrada tenía un defecto: la fase E
    declaraba que recorría la documentación del ciclo y no recorría las etapas
    del ciclo, que viven en otra carpeta. Y se saltaba **en silencio**.
    """

    def test_las_siete_etapas_entran_reconocidas(self):
        from nucleo.importacion.models import Traido
        from nucleo.importacion import moldes
        proyecto, _ = self._con_documentacion(etapas=moldes.ETAPAS)

        etapas = Traido.objects.filter(proyecto=proyecto.identificador,
                                       tipo="etapa del ciclo de vida")

        self.assertEqual(etapas.count(), 7)

    def test_los_documentos_de_las_etapas_tambien_entran(self):
        from nucleo.importacion.models import Traido
        proyecto, _ = self._con_documentacion(extras={
            "cvds/diseno/modelo-de-datos.md": "# El modelo" + chr(10),
            "cvds/planificacion/acta-de-constitucion.md": "# El acta" + chr(10),
        })

        tipos = sorted(Traido.objects.filter(
            proyecto=proyecto.identificador).values_list("tipo", flat=True))

        self.assertIn("modelo de datos", tipos)
        self.assertIn("acta de constitución", tipos)

    def test_el_readme_de_una_etapa_no_es_un_indice_cualquiera(self):
        """El nombre solo no alcanza: hay que mirar dónde está."""
        from nucleo.importacion import moldes
        self.assertEqual(
            moldes.tipo_de("README.md", "cvds/planificacion/README.md"),
            "etapa del ciclo de vida")
        self.assertEqual(
            moldes.tipo_de("README.md", "documentacion/epicas/README.md"),
            "índice")


class EtapasEnElEstadoTests(BaseEstado):
    """CP-002 · el estado dice qué etapas tienen documento."""

    def test_dice_cuales_tienen_y_cuales_no(self):
        proyecto, _ = self._con_documentacion(
            etapas=("planificacion", "analisis-requisitos", "diseno",
                    "implementacion"))

        estado = proyecto.detalle_del_estado

        self.assertEqual(len(estado.etapas_con_documento), 4)
        self.assertEqual(len(estado.etapas_sin_documento), 3)
        self.assertIn("pruebas", estado.etapas_sin_documento)

    def test_lo_que_falta_tambien_se_ve_en_la_pantalla(self):
        proyecto, _ = self._con_documentacion(etapas=("planificacion",))

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("Etapas todavía sin documento", cuerpo)
        self.assertIn("mantenimiento", cuerpo)


class FasesEnElEstadoTests(BaseEstado):
    """CP-003 y CP-004 · las fases, y lo que no se deja leer."""

    ABIERTA = ("# Estado" + chr(10) * 2 +
               "**Estación actual:** 6 · ejecución continua" + chr(10))
    CERRADA = ("# Estado" + chr(10) * 2 +
               "**Estación actual:** 9 · commit único" + chr(10))
    DICE_CERRADA = ("# Estado" + chr(10) * 2 +
                    "**Estación actual:** cerrada" + chr(10))
    ILEGIBLE = ("# Estado" + chr(10) * 2 +
                "**Estación actual:** ya casi, falta poco" + chr(10))

    def test_cuenta_las_fases_y_cuales_siguen_abiertas(self):
        proyecto, _ = self._con_documentacion(ciclo={
            "epicas/EP-001/A/estado-fase.md": self.ABIERTA,
            "epicas/EP-001/B/estado-fase.md": self.CERRADA,
            "epicas/EP-001/C/estado-fase.md": self.DICE_CERRADA,
        })

        estado = proyecto.detalle_del_estado

        self.assertEqual(estado.fases, 3)
        self.assertEqual(estado.fases_abiertas, 1)
        self.assertEqual(estado.fases_ilegibles, [])

    def test_una_estacion_que_no_se_deja_leer_se_dice(self):
        """`04·R4`. Cinco de los 125 estados reales caen acá."""
        proyecto, _ = self._con_documentacion(ciclo={
            "epicas/EP-001/A/estado-fase.md": self.ABIERTA,
            "epicas/EP-001/B/estado-fase.md": self.ILEGIBLE,
        })

        estado = proyecto.detalle_del_estado

        self.assertEqual(estado.fases, 2)
        self.assertEqual(estado.fases_abiertas, 1)
        self.assertEqual(len(estado.fases_ilegibles), 1)
        self.assertIn("EP-001/B", estado.fases_ilegibles[0])

    def test_la_ilegible_no_se_cuenta_ni_como_abierta_ni_como_cerrada(self):
        proyecto, _ = self._con_documentacion(ciclo={
            "epicas/EP-001/A/estado-fase.md": self.ILEGIBLE,
        })

        estado = proyecto.detalle_del_estado

        self.assertEqual(estado.fases, 1)
        self.assertEqual(estado.fases_abiertas, 0)
        self.assertEqual(len(estado.fases_ilegibles), 1)

    def test_la_pantalla_dice_cuales_no_se_pudieron_leer(self):
        proyecto, _ = self._con_documentacion(ciclo={
            "epicas/EP-001/A/estado-fase.md": self.ILEGIBLE,
        })

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("no dice en qué estación va", cuerpo)
        self.assertIn("EP-001/A", cuerpo)


class AprobadoTests(BaseEstado):
    """CP-005 · lo aprobado se distingue, y se dice con palabras."""

    APROBADO = ("# Un plan" + chr(10) * 2 +
                "**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.**"
                + chr(10))
    SIN_APROBAR = "# Otro plan" + chr(10) * 2 + "Pendiente de aprobación." + chr(10)

    def test_cuenta_los_aprobados_y_los_que_no(self):
        proyecto, _ = self._con_documentacion(ciclo={
            "epicas/EP-001/A/plan_trabajo.md": self.APROBADO,
            "epicas/EP-001/A/plan_pruebas.md": self.APROBADO,
            "epicas/EP-001/B/plan_trabajo.md": self.SIN_APROBAR,
        })

        estado = proyecto.detalle_del_estado

        self.assertEqual(estado.aprobados, 2)
        self.assertEqual(estado.documentos, 3)

    def test_dice_desde_cuando(self):
        proyecto, _ = self._con_documentacion(ciclo={
            "epicas/EP-001/A/plan_trabajo.md": self.APROBADO,
        })

        self.assertEqual(proyecto.detalle_del_estado.ultima_aprobacion,
                         "2026-08-25")

    def test_la_pantalla_lo_dice_con_palabras_y_no_solo_con_color(self):
        proyecto, _ = self._con_documentacion(ciclo={
            "epicas/EP-001/A/plan_trabajo.md": self.APROBADO,
            "epicas/EP-001/B/plan_trabajo.md": self.SIN_APROBAR,
        })

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("están aprobados", cuerpo)
        self.assertIn("2026-08-25", cuerpo)


class SinEmpezarTests(BaseProyectos):
    """CP-006 · un proyecto sin nada dice qué haría falta."""

    def test_el_estado_dice_sin_empezar(self):
        proyecto, _ = core.conectar("Recién conectado",
                                    self.proyecto_de_mentira())

        self.assertEqual(proyecto.estado, "sin empezar")
        self.assertTrue(proyecto.detalle_del_estado.esta_sin_empezar)

    def test_dice_que_haria_falta_para_arrancar(self):
        proyecto, _ = core.conectar("Recién conectado",
                                    self.proyecto_de_mentira())

        falta = proyecto.detalle_del_estado.que_haria_falta

        self.assertIn("traer", falta)
        self.assertIn("planificación", falta)

    def test_si_la_ruta_se_perdio_lo_que_falta_es_otra_cosa(self):
        carpeta = self.proyecto_de_mentira()
        proyecto, _ = core.conectar("El que se movió", carpeta)
        shutil.rmtree(carpeta, ignore_errors=True)

        falta = Proyecto.objects.get(pk=proyecto.pk).detalle_del_estado.que_haria_falta

        self.assertIn("corregir dónde vive su código", falta)

    def test_la_pantalla_no_queda_vacia(self):
        proyecto, _ = core.conectar("Recién conectado",
                                    self.proyecto_de_mentira())

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("Sin empezar", cuerpo)
        self.assertIn("Para empezar", cuerpo)


class SinLeerLaCarpetaTests(BaseEstado):
    """CP-007 y CP-009 · el estado sale de lo traído, no de la carpeta.

    Es la forma más dura de probarlo: se borra la carpeta del proyecto entera y
    el estado tiene que salir **idéntico**. Si cambia, se estaba leyendo, y
    entonces la plataforma no serviría para un proyecto entregado o archivado.
    """

    def _retrato_del_estado(self, proyecto):
        e = Proyecto.objects.get(pk=proyecto.pk).detalle_del_estado
        return (e.documentos, e.fases, e.fases_abiertas, e.aprobados,
                tuple(e.etapas_con_documento), tuple(e.etapas_sin_documento),
                tuple(e.fases_ilegibles), e.ultima_aprobacion)

    def test_el_estado_sale_identico_con_la_carpeta_borrada(self):
        proyecto, carpeta = self._con_documentacion(
            ciclo={"epicas/EP-001/A/estado-fase.md":
                   "**Estación actual:** 6 · ejecución" + chr(10),
                   "epicas/EP-001/A/plan_trabajo.md":
                   "**Aprobado por alguien, el 2026-08-25.**" + chr(10)},
            etapas=("planificacion", "diseno"))
        antes = self._retrato_del_estado(proyecto)

        shutil.rmtree(carpeta, ignore_errors=True)

        self.assertEqual(antes, self._retrato_del_estado(proyecto),
                         "el estado cambió al borrar la carpeta: se estaba "
                         "leyendo el proyecto en vez de lo traído")

    def test_con_la_ruta_perdida_el_estado_se_ve_igual_en_la_pantalla(self):
        proyecto, carpeta = self._con_documentacion(etapas=("planificacion",))
        shutil.rmtree(carpeta, ignore_errors=True)

        cuerpo = self.client.get(
            "/proyecto/%s/" % proyecto.identificador).content.decode("utf-8")

        self.assertIn("Etapas del ciclo con documento", cuerpo)
        self.assertIn("ya no está donde estaba", cuerpo)


class RendimientoDelEstadoTests(BaseProyectos):
    """CP-008 · cincuenta proyectos con estado listan bajo un segundo."""

    def test_cincuenta_proyectos_con_estado_listan_bajo_un_segundo(self):
        import time
        from nucleo.importacion import core as importacion
        for numero in range(50):
            carpeta = self.proyecto_de_mentira()
            _escribir(os.path.join(carpeta, "documentacion", "epicas",
                                   "EP-001", "A", "estado-fase.md"),
                      "**Estación actual:** 6 · ejecución" + chr(10))
            _escribir(os.path.join(carpeta, "cvds", "planificacion",
                                   "README.md"), "# Planificación" + chr(10))
            proyecto, _ = core.conectar("Proyecto %02d" % numero, carpeta)
            importacion.traer(proyecto)
        self.assertEqual(Proyecto.objects.count(), 50)

        arranca = time.time()
        respuesta = self.client.get("/")
        tardo = time.time() - arranca

        self.assertEqual(respuesta.status_code, 200)
        self.assertLess(tardo, 1.0,
                        "listar cincuenta proyectos con estado tardó %.3f s"
                        % tardo)
        print("\n   CP-008 de la fase G: listar 50 proyectos con estado "
              "calculado tardó %.3f s" % tardo)
