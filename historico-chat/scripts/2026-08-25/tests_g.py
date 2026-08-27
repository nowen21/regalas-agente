

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
