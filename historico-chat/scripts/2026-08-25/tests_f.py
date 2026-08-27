

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
