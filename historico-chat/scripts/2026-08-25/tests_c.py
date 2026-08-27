

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
        """CP-005. La carpeta cambió: lo que declara puede ser otra cosa."""
        vieja = self.proyecto_de_mentira(version="34.1.0")
        proyecto, _ = core.conectar("El que se movió", vieja)
        self.assertEqual(proyecto.version_reglas, "34.1.0")
        nueva = self.proyecto_de_mentira(con_claude=False)

        corregido = core.corregir_ruta(proyecto, nueva)

        self.assertEqual(corregido.version_reglas, "")

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
