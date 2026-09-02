# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de las fases `S`, `T` y `U` — `F-011` a `F-013`.

**El caso que decide el CP-001 es el que NO deja abrir:** una fase sin historia.
Abrirla igual dejaría trabajo colgando de nada, que es justo lo que `02·F0` vino
a evitar.

**El que más protege es el CP-002:** que abrir dos veces la misma fase no pise lo
escrito. Es el único daño irreparable de este módulo.

**Y el que más enseña es el CP-004:** que la tabla mande sobre la frase. Un
`estado-fase.md` dice dos veces en qué estación va, y cuando no coinciden, la que
sabe es la tabla.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.proyectos.models import Proyecto
from . import apertura, estaciones, puertas

TABLA = u"""# Estado de fase — `X-EP-001-HU-001-de-mentiras`

| Campo | Valor |
|---|---|
| **Última actualización** | 2026-08-20 |

**Estación actual:** %(dice)s · Lo que sea.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador | contexto entendido | ☑ |
| 2 | Proponente | alcance aprobado | ☑ |
| 3 | Escritor de épica | épica aprobada | ☑ |
| 4 | Escritor de historia | HUs aprobadas | ☑ |
| 5 | Escritor de especificación | especificación aprobada | ☑ |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador | plan + pruebas aprobados | %(siete)s |
| 8 | Implementador | pruebas verdes | %(ocho)s |
| 9 | Verificador | trazabilidad | ☐ |
| 10 | Crítico | sin hallazgos | ☐ |
| 11 | Cierre documental | docs al día | ☐ |
| 12 | Commit | autorizado | ☐ |
| 13 | Publicación | autorizado | N/A |

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | %(concepto)s |
"""


def tabla(dice="7", siete=u"☐", ocho=u"☐", concepto=u"**Sin veredicto**"):
    return TABLA % {"dice": dice, "siete": siete, "ocho": ocho,
                    "concepto": concepto}


class Base(TestCase):

    def setUp(self):
        self.proyecto = tempfile.mkdtemp(prefix="prueba-operacion-proy-")
        self.plantillas = tempfile.mkdtemp(prefix="prueba-operacion-moldes-")
        self.datos = tempfile.mkdtemp(prefix="prueba-operacion-datos-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos,
                                          CARPETA_PLANTILLAS=self.plantillas)
        self.contexto.enable()
        Proyecto.objects.create(identificador="de-prueba", nombre="De prueba",
                                ruta_codigo=self.proyecto,
                                ruta_normalizada=self.proyecto.lower(),
                                conectado="conectado")
        self.moldes()

    def tearDown(self):
        self.contexto.disable()
        for carpeta in (self.proyecto, self.plantillas, self.datos):
            shutil.rmtree(carpeta, ignore_errors=True)

    def moldes(self):
        """Los cinco moldes que una fase necesita, con algo adentro."""
        carpeta = os.path.join(self.plantillas, "ciclo-vida-proyectos")
        os.makedirs(carpeta, exist_ok=True)
        for archivo in ("07-plan-trabajo.md", "08-plan-pruebas.md",
                        "09-resultado-pruebas.md", "10-estado-fase.md",
                        "11-funcionalidad-implementada.md"):
            with io.open(os.path.join(carpeta, archivo), "w",
                         encoding="utf-8", newline="") as abierto:
                abierto.write(u"# Molde de %s\n\nResponsable: «…»\n" % archivo)

    def historia(self, epica="EP-001-la-primera", hu="HU-001-la-primera"):
        """La carpeta de una historia, para que la fase tenga de dónde colgar."""
        carpeta = os.path.join(self.proyecto, "documentacion", "epicas",
                               epica, hu)
        os.makedirs(carpeta, exist_ok=True)
        return carpeta

    def fase_escrita(self, texto, nombre="X-EP-001-HU-001-de-mentiras"):
        """Una fase con su `estado-fase.md` ya escrito."""
        carpeta = os.path.join(self.historia(), nombre)
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, "estado-fase.md")
        with io.open(ruta, "w", encoding="utf-8", newline="") as abierto:
            abierto.write(texto)
        return ruta


class CP001SinHistoriaNoSeAbre(Base):
    """`CA-2` de `F-011`: una fase sin historia no se puede abrir."""

    def test_sin_la_historia_no_se_abre(self):
        with self.assertRaises(apertura.NoSePuedeAbrir) as fallo:
            apertura.abrir_fase("de-prueba", "S", "EP-001", "HU-001", "lo que sea")
        self.assertIn("HU-001", str(fallo.exception))
        self.assertIn("nadie pidió", str(fallo.exception))

    def test_con_la_historia_si_se_abre(self):
        self.historia()
        abierta = apertura.abrir_fase("de-prueba", "S", "EP-001", "HU-001",
                                      "lo que sea")
        self.assertTrue(os.path.isdir(abierta["carpeta"]))

    def test_el_proyecto_que_no_esta_conectado_se_dice(self):
        with self.assertRaises(apertura.NoSePuedeAbrir) as fallo:
            apertura.abrir_fase("ninguno", "S", "EP-001", "HU-001", "lo que sea")
        self.assertIn("no está conectado", str(fallo.exception))

    def test_la_epica_mal_escrita_se_rechaza_antes_de_tocar_el_disco(self):
        with self.assertRaises(apertura.NoSePuedeAbrir):
            apertura.nombre_de_fase("S", "EP-1", "HU-001", "lo que sea")


class CP002AbrirNoPisa(Base):
    """El daño irreparable: abrir dos veces sobre trabajo ya escrito."""

    def test_abrir_dos_veces_no_toca_lo_escrito(self):
        self.historia()
        abierta = apertura.abrir_fase("de-prueba", "S", "EP-001", "HU-001",
                                      "lo que sea")
        propio = os.path.join(abierta["carpeta"], "plan_trabajo.md")
        with io.open(propio, "w", encoding="utf-8", newline="") as abierto:
            abierto.write(u"# Lo que ya estaba escrito\n")

        with self.assertRaises(apertura.NoSePuedeAbrir) as fallo:
            apertura.abrir_fase("de-prueba", "S", "EP-001", "HU-001",
                                "lo que sea")
        self.assertIn("ya existe", str(fallo.exception))
        with io.open(propio, encoding="utf-8") as abierto:
            self.assertEqual(u"# Lo que ya estaba escrito\n", abierto.read())

    def test_quedan_los_cinco_documentos_con_el_molde(self):
        self.historia()
        abierta = apertura.abrir_fase("de-prueba", "S", "EP-001", "HU-001",
                                      "lo que sea")
        self.assertEqual(5, len(abierta["documentos"]))
        for archivo, _tipo in apertura.LOS_CINCO:
            ruta = os.path.join(abierta["carpeta"], archivo)
            self.assertTrue(os.path.exists(ruta), archivo)
            with io.open(ruta, encoding="utf-8") as abierto:
                dentro = abierto.read()
            self.assertIn(u"Molde de", dentro)
            self.assertIn(abierta["nombre"], dentro)

    def test_abrir_queda_registrado_en_la_auditoria(self):
        from nucleo.auditoria.models import Registro
        self.historia()
        antes = Registro.objects.count()
        apertura.abrir_fase("de-prueba", "S", "EP-001", "HU-001", "lo que sea")
        self.assertEqual(antes + 1, Registro.objects.count())


class CP003ElNombreSaleDelIdentificador(Base):
    """`CA-3` de `F-011`: el nombre no se escribe a mano."""

    def test_el_nombre_junta_letra_epica_historia_y_titulo(self):
        self.assertEqual(
            "D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto",
            apertura.nombre_de_fase("D", "EP-009", "HU-001",
                                    "La constancia va antes que el efecto"))

    def test_las_tildes_y_la_ene_se_bajan(self):
        self.assertEqual(
            "S-EP-001-HU-001-el-ano-que-vino-con-nada",
            apertura.nombre_de_fase("S", "EP-001", "HU-001",
                                    "El año que vino con NADA"))

    def test_un_titulo_que_no_deja_letras_se_rechaza(self):
        with self.assertRaises(apertura.NoSePuedeAbrir) as fallo:
            apertura.nombre_de_fase("S", "EP-001", "HU-001", "···")
        self.assertIn("de qué trata", str(fallo.exception))

    def test_donde_iria_no_crea_nada(self):
        self.historia()
        carpeta, nombre = apertura.donde_iria("de-prueba", "S", "EP-001",
                                              "HU-001", "lo que sea")
        self.assertIn(nombre, carpeta)
        self.assertFalse(os.path.isdir(carpeta))


class CP004LaTablaMandaSobreLaFrase(Base):
    """`CA-1` y `RN-5` de `F-012`: el estado lo fija lo escrito."""

    def test_la_estacion_actual_es_la_primera_sin_marcar(self):
        leida = estaciones.de_un_texto(tabla(dice="7"))
        self.assertEqual(7, leida["actual"])
        self.assertEqual("Planificador", leida["nombre"])
        self.assertTrue(leida["coincide"])

    def test_cuando_la_frase_y_la_tabla_no_coinciden_manda_la_tabla(self):
        leida = estaciones.de_un_texto(tabla(dice="11"))
        self.assertEqual(7, leida["actual"])
        self.assertEqual(11, leida["declarada"])
        self.assertFalse(leida["coincide"])
        self.assertIn("Manda la tabla", estaciones.dicho(dict(leida, fase="X")))

    def test_una_fase_con_todo_marcado_esta_terminada(self):
        texto = tabla(dice="13").replace(u"| ☐ |", u"| ☑ |")
        leida = estaciones.de_un_texto(texto)
        self.assertEqual(estaciones.TERMINADA, leida["actual"])

    def test_la_estacion_que_no_aplica_no_detiene_la_fase(self):
        texto = tabla(dice="13").replace(u"| ☐ |", u"| ☑ |")
        leida = estaciones.de_un_texto(texto)
        trece = [una for una in leida["estaciones"] if una["numero"] == 13][0]
        self.assertEqual("no aplica", trece["estado"])


class CP005SeVeQueFaltaYDesdeCuando(Base):
    """`CA-2` y `CA-3` de `F-012`."""

    def test_se_dice_que_puerta_falta_no_solo_que_falta(self):
        leida = estaciones.de_un_texto(tabla())
        self.assertEqual("plan + pruebas aprobados", leida["puerta"])
        self.assertIn("plan + pruebas",
                      estaciones.dicho(dict(leida, fase="X")))

    def test_una_fase_detenida_dice_desde_cuando(self):
        leida = estaciones.de_un_texto(tabla())
        self.assertEqual("2026-08-20", leida["actualizada"])
        self.assertEqual(12, estaciones.detenida_desde(leida, "2026-09-01"))

    def test_la_que_no_dice_cuando_se_distingue_de_la_de_cero_dias(self):
        sin_fecha = tabla().replace(
            u"| **Última actualización** | 2026-08-20 |",
            u"| **Última actualización** | |")
        leida = estaciones.de_un_texto(sin_fecha)
        self.assertEqual(-1, estaciones.detenida_desde(leida, "2026-09-01"))

    def test_se_leen_todas_las_fases_del_proyecto(self):
        self.fase_escrita(tabla(), "X-EP-001-HU-001-una")
        self.fase_escrita(tabla(dice="8", siete=u"☑"), "Y-EP-001-HU-001-otra")
        todas = estaciones.de_un_proyecto(self.proyecto)
        self.assertEqual(2, len(todas))
        # La menos avanzada va primero: es la que lleva más tiempo quieta.
        self.assertEqual("X-EP-001-HU-001-una", todas[0]["fase"])

    def test_un_proyecto_sin_fases_devuelve_lista_vacia_sin_reventar(self):
        self.assertEqual([], estaciones.de_un_proyecto(self.proyecto))


class CP006LaPuertaDiceCualFalta(Base):
    """`CA-1` a `CA-3` de `F-013`."""

    def test_sin_plan_aprobado_no_pasa_a_ejecucion(self):
        leida = estaciones.de_un_texto(tabla())
        pasa, motivo = puertas.se_puede_pasar(leida, tabla(), 8)
        self.assertFalse(pasa)
        self.assertIn("estación 7", motivo)
        self.assertIn("nadie pidió", motivo)

    def test_con_el_plan_aprobado_si_pasa(self):
        texto = tabla(siete=u"☑")
        leida = estaciones.de_un_texto(texto)
        pasa, motivo = puertas.se_puede_pasar(leida, texto, 8)
        self.assertTrue(pasa)
        self.assertIn("plan y pruebas aprobados", motivo)

    def test_sin_veredicto_no_se_cierra(self):
        texto = tabla()
        leida = estaciones.de_un_texto(texto)
        pasa, motivo = puertas.se_puede_pasar(leida, texto, 12)
        self.assertFalse(pasa)
        self.assertIn("veredicto", motivo)

    def test_con_veredicto_que_no_cumple_tampoco_se_cierra(self):
        texto = tabla(concepto=u"**No cumple**")
        leida = estaciones.de_un_texto(texto)
        pasa, motivo = puertas.se_puede_pasar(leida, texto, 12)
        self.assertFalse(pasa)
        self.assertIn("No cumple", motivo)

    def test_con_veredicto_que_cumple_se_cierra(self):
        texto = tabla(concepto=u"**Cumple**")
        leida = estaciones.de_un_texto(texto)
        pasa, _motivo = puertas.se_puede_pasar(leida, texto, 12)
        self.assertTrue(pasa)

    def test_una_estacion_sin_puerta_comprobable_lo_dice(self):
        texto = tabla()
        leida = estaciones.de_un_texto(texto)
        pasa, motivo = puertas.se_puede_pasar(leida, texto, 5)
        self.assertTrue(pasa)
        self.assertIn("no opina", motivo)

    def test_las_tres_puertas_se_revisan_de_un_golpe(self):
        texto = tabla()
        leida = estaciones.de_un_texto(texto)
        revisadas = puertas.revisar(leida, texto)
        self.assertEqual([8, 12, 13], [una["estacion"] for una in revisadas])
        self.assertTrue(all(una["motivo"] for una in revisadas))


class CP007ElLectorSeAdaptaALoQueHay(Base):
    """Lo que salió al correrlo contra las 209 fases reales del repositorio.

    Tres cosas que leyendo el código parecían resueltas y no lo estaban.
    """

    def test_la_marca_vieja_tambien_cuenta_como_cumplida(self):
        """76 fases cierran con `✅`, no con `☑`. Ninguna se reescribe."""
        texto = tabla(dice="13").replace(u"| ☐ |", u"| ✅ |")
        leida = estaciones.de_un_texto(texto)
        self.assertEqual(estaciones.TERMINADA, leida["actual"])

    def test_una_estacion_con_prosa_no_es_una_estacion_pendiente(self):
        texto = tabla().replace(
            u"| 7 | Planificador | plan + pruebas aprobados | ☐ |",
            u"| 7 | Planificador | plan + pruebas aprobados | "
            u"No se hizo como estación aparte |")
        leida = estaciones.de_un_texto(texto)
        self.assertEqual(7, leida["actual"])
        self.assertEqual("sin marcar", leida["como_quedo"])
        self.assertIn("No se marcó", estaciones.dicho(dict(leida, fase="X")))

    def test_una_tabla_de_otro_modelo_no_se_compara_con_la_frase(self):
        """107 de 209 fases traen tablas de once estaciones o menos."""
        once = u"""# Estado

**Estación actual:** 12 · Commit.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro | identificador | ☑ |
| 2 | Disparo | autorización | ☑ |
| 3 | Diseño del plan | los dos planes | ☑ |
| 4 | Pausa y presentación | falta presentarlo | ☐ |
"""
        leida = estaciones.de_un_texto(once)
        self.assertEqual(4, leida["modelo"])
        self.assertFalse(leida["comparable"])
        # No se acusa de contradicción a una tabla que habla de otra cosa.
        self.assertTrue(leida["coincide"])
        self.assertIn("no se compara", estaciones.dicho(dict(leida, fase="X")))

    def test_el_resumen_separa_las_tres_cosas(self):
        self.fase_escrita(tabla(), "X-EP-001-HU-001-una")
        cuenta = estaciones.resumen(estaciones.de_un_proyecto(self.proyecto))
        for clave in ("cuantas", "terminadas", "sin_coincidir",
                      "con_estaciones_sin_marcar", "de_otro_modelo"):
            self.assertIn(clave, cuenta)
