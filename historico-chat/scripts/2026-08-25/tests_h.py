

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
        registro = Registro.objects.last()
        self.assertEqual(registro.que_se_hizo, "desconectar un proyecto")
        self.assertEqual(registro.sesion, "5f06ce4e")


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
