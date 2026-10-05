"""Los validadores del grupo «proceso»: pendientes, acciones, amarre, brevedad,
redacción, expediente, reaperturas, sesiones, sitio, inmutable, índices y conteo.

Son las pruebas de `validadores/pruebas.py` y `validadores/tests/*.py` que
cubrían estos módulos, pasadas a sus clases. Las que solo leían un documento
del estándar o un enganche, sin llamar al módulo, se quedan donde estaban.
"""
import io
import os
import shutil
import subprocess
import tempfile
import time
import unittest

from core.comun import AVISO, FALLA, Hallazgo, Proyecto
from core.validadores.acciones import ANEXO, ESCALA, InventarioDeAcciones
from core.validadores.amarre import MAPA as MAPA_AMARRE
from core.validadores.amarre import MapaDelAmarre
from core.validadores.brevedad import HOLGADO, Brevedad, Respuestas
from core.validadores.conteo import ConteoPorRegla
from core.validadores.expediente import Expediente
from core.validadores.indices import CompletadorDeIndices, IndicesPorAfinar
from core.validadores.inmutable import HistoricoInmutable
from core.validadores.pendientes import NumeracionDePendientes, Pendientes
from core.validadores.reaperturas import Reaperturas
from core.validadores.redaccion import Redaccion
from core.validadores.sesiones import CARPETA as TOCADO
from core.validadores.sesiones import VIGENCIA, Sesiones, SesionesMezcladas
from core.validadores.sitio import MapaDelSitio

RAIZ = Proyecto.estandar()


class Carpeta(unittest.TestCase):
    """Un proyecto de mentira en una carpeta temporal."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.raiz = tmp.name

    def escribir(self, relativa, texto="x\n", raiz=None):
        ruta = os.path.join(raiz or self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def leer(self, relativa):
        with io.open(os.path.join(self.raiz, *relativa.split("/")), encoding="utf-8") as f:
            return f.read()


def git(raiz, *orden):
    subprocess.run(["git", "-C", raiz, *orden], capture_output=True)


def repo_vacio(raiz):
    git(raiz, "init", "-q")
    git(raiz, "config", "user.name", "prueba")
    git(raiz, "config", "user.email", "prueba@local")


# ── pendientes ────────────────────────────────────────────────────────────

class NumeracionDeLosPendientes(Carpeta):
    """`EP-004·HU-018` · El número ya tomado. Los pendientes se citan entre sí por
    número: dar uno usado rompe esas citas sin que nadie se entere."""

    def carpeta(self, abiertos=(), cerrados=(), indice=None):
        for nombre in abiertos:
            self.escribir("pendientes/" + nombre, "# pendiente de mentira\n")
        for nombre in cerrados:
            self.escribir("pendientes/hecho/" + nombre, "# cerrado de mentira\n")
        os.makedirs(os.path.join(self.raiz, "pendientes", "hecho"), exist_ok=True)
        if indice is not None:
            self.escribir("pendientes/README.md", indice)
        return self.raiz

    def de_numeracion(self, raiz):
        return [h for h in NumeracionDePendientes(raiz).validar() if h.severidad == FALLA and "número" in h.mensaje]

    def test_dice_cual_es_el_proximo_numero_libre(self):
        p = Pendientes(self.carpeta(abiertos=("01-uno.md", "02-dos.md", "03-tres.md")))
        self.assertEqual(4, p.proximo_libre())
        self.assertIn("el próximo libre es el 04", p.linea_proximo())

    def test_el_hueco_no_se_reutiliza(self):
        self.assertEqual(6, Pendientes(self.carpeta(abiertos=("01-uno.md", "05-cinco.md"))).proximo_libre())

    def test_el_numero_de_un_cerrado_sigue_tomado_aunque_pierda_el_nombre(self):
        """Al cerrarse el archivo pasa a `hecho/` sin número; lo conserva la fila tachada."""
        indice = ("# Pendientes\n\n| # | P | Pendiente |\n|---|---|---|\n| 01 | P1 | [uno](01-uno.md) |\n"
                  "| ~~02~~ | — | **hecho** [dos](hecho/sin-numero.md) |\n")
        p = Pendientes(self.carpeta(abiertos=("01-uno.md",), cerrados=("sin-numero.md",), indice=indice))
        self.assertIn(2, p.tomados(), "el número de un cerrado se dio por libre")
        self.assertEqual(3, p.proximo_libre())

    def test_la_linea_sale_sobre_el_estandar(self):
        """Antes corría `validar.py pendientes`; acá se pide a la clase sobre el estándar."""
        self.assertIn("el próximo libre es el", Pendientes(RAIZ).linea_proximo())

    def test_avisa_del_numero_repetido(self):
        fallas = self.de_numeracion(self.carpeta(abiertos=("07-uno.md", "07-otro.md")))
        self.assertEqual(1, len(fallas))
        self.assertIn("07-uno.md", fallas[0].mensaje)
        self.assertIn("07-otro.md", fallas[0].mensaje)

    def test_el_repetido_entre_abierto_y_cerrado_tambien_se_ve(self):
        self.assertEqual(1, len(self.de_numeracion(self.carpeta(abiertos=("07-uno.md",), cerrados=("07-otro.md",)))))

    def test_los_ceros_a_la_izquierda_no_hacen_dos_numeros(self):
        self.assertEqual(1, len(self.de_numeracion(self.carpeta(abiertos=("07-uno.md", "7-otro.md")))))

    def test_el_pendiente_sin_linea_en_el_indice_se_avisa(self):
        indice = "# Pendientes\n\n| # | Pendiente |\n|---|---|\n| 01 | [uno](01-uno.md) |\n"
        raiz = self.carpeta(abiertos=("01-uno.md", "02-dos.md"), indice=indice)
        avisos = [h for h in NumeracionDePendientes(raiz).validar() if "02-dos.md" in h.archivo]
        self.assertEqual(1, len(avisos))

    def test_la_linea_del_indice_sin_archivo_se_avisa(self):
        indice = ("# Pendientes\n\n| # | Pendiente |\n|---|---|\n"
                  "| 01 | [uno](01-uno.md) |\n| 02 | [dos](02-dos.md) |\n")
        raiz = self.carpeta(abiertos=("01-uno.md",), indice=indice)
        avisos = [h for h in NumeracionDePendientes(raiz).validar()
                  if "02-dos.md" in h.mensaje and "no está en la carpeta" in h.mensaje]
        self.assertEqual(1, len(avisos))

    def test_el_estandar_no_tiene_numeros_repetidos(self):
        self.assertEqual([], [h.mensaje for h in self.de_numeracion(RAIZ)])

    def test_la_carpeta_vacia_no_revienta(self):
        raiz = self.carpeta()
        self.assertEqual({}, Pendientes(raiz).numerados())
        self.assertEqual(1, Pendientes(raiz).proximo_libre())
        self.assertEqual([], [h for h in NumeracionDePendientes(raiz).validar() if h.severidad == FALLA])

    def test_sin_la_carpeta_no_es_falla(self):
        """`pendientes/` es historia: el proyecto nuevo no la tiene."""
        self.assertFalse(any(h.severidad == FALLA for h in NumeracionDePendientes(self.raiz).validar()))

    def test_el_archivo_sin_numero_se_reporta_y_no_detiene(self):
        raiz = self.carpeta(abiertos=("01-uno.md", "notas-sueltas.md"))
        hallazgos = NumeracionDePendientes(raiz).validar()
        self.assertEqual(1, len([h for h in hallazgos if "no empieza por un número" in h.mensaje]))
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])
        self.assertEqual(2, Pendientes(raiz).proximo_libre())


class ElProyectoDeOrigenSeNombra(Carpeta):
    """`02·F24` · Sin el nombre, el aviso al cerrar no tiene a dónde ir."""

    def origen(self, ficha):
        self.escribir("pendientes/07-algo.md", ficha)
        return Pendientes(self.raiz).sin_proyecto_de_origen()

    def test_la_casilla_vacia_se_reporta(self):
        self.assertEqual(1, len(self.origen("# Algo\n\n| | |\n|---|---|\n| **Proyecto de origen** |  |\n")))

    def test_el_marcador_sin_llenar_se_reporta(self):
        self.assertEqual(1, len(self.origen("# Algo\n\n| | |\n|---|---|\n"
                                            "| **Proyecto de origen** | «Nombre» · `«ruta»` |\n")))

    def test_el_nombre_puesto_no_se_reporta(self):
        self.assertEqual([], self.origen("# Algo\n\n| | |\n|---|---|\n| **Proyecto de origen** | **shopnest-mesa** |\n"))

    def test_el_que_no_declara_origen_no_se_reporta(self):
        self.assertEqual([], self.origen("# Algo\n\nSin ficha de origen.\n"))

    def test_la_casilla_vacia_falla_en_la_corrida(self):
        self.origen("# Algo\n\n| | |\n|---|---|\n| **Proyecto de origen** |  |\n")
        self.assertTrue([h for h in NumeracionDePendientes(self.raiz).validar()
                         if h.severidad == FALLA and "02·F24" in h.mensaje])


FICHA = "# Pendiente · %s\n\n**Estado:** %s\n\n| | |\n|---|---|\n%s\n\n## El problema\n\nTexto.\n"


class ElCerradoDiceSuFase(Carpeta):
    """`EP-004·HU-016` · Hacia abajo, el cerrado dice en qué fase se hizo; hacia
    arriba ya no se exige la historia: la decide el análisis."""

    def setUp(self):
        super().setUp()
        os.makedirs(os.path.join(self.raiz, "pendientes", "hecho"))
        os.makedirs(os.path.join(self.raiz, "documentacion", "epicas", "EP-001-x", "HU-001-y",
                                 "A-EP-001-HU-001-la-fase"))

    def cerrados(self):
        return Pendientes(self.raiz).cerrado_declara_su_fase()

    def test_el_abierto_sin_la_fila_ya_no_falla(self):
        self.escribir("pendientes/77-algo.md", FICHA % ("Algo", "abierto", "| **Tamaño** | chico |"))
        self.assertEqual([], [h for h in NumeracionDePendientes(self.raiz).validar() if h.severidad == FALLA])

    def test_el_que_trae_la_fila_tambien_pasa(self):
        self.escribir("pendientes/77-libreta.md", FICHA % (
            "Libreta", "abierto", "| **Historia de usuario** | La que diga su análisis |"))
        self.assertEqual([], [h for h in NumeracionDePendientes(self.raiz).validar() if h.severidad == FALLA])

    def test_el_cerrado_sin_fase_se_reporta_y_el_que_la_nombra_no(self):
        self.escribir("pendientes/hecho/sin-fase.md", FICHA % ("Sin fase", "✅ **hecho** el 2026-08-20",
                                                               "| **Tamaño** | chico |"))
        h = self.cerrados()
        self.assertEqual(1, len(h))
        self.assertEqual(AVISO, h[0].severidad, "no rompe nada hoy: informa")
        self.escribir("pendientes/hecho/con-fase.md", FICHA % (
            "Con fase", "✅ **hecho** el 2026-08-20, en la fase `A-EP-001-HU-001-la-fase`", "| **Tamaño** | chico |"))
        self.assertFalse(any("con-fase" in x.archivo for x in self.cerrados()))

    def test_la_fase_inventada_se_reporta(self):
        self.escribir("pendientes/hecho/inventada.md", FICHA % (
            "Inventada", "✅ **hecho** el 2026-08-20, en la fase `Z-EP-999-HU-999-no-existe`", "| **Tamaño** | chico |"))
        self.assertTrue(any("no existe" in x.mensaje for x in self.cerrados()))

    def test_el_cerrado_por_decision_no_se_reporta(self):
        self.escribir("pendientes/hecho/por-decision.md", FICHA % (
            "Por decisión", "✅ **hecho** el 2026-08-20 · cerrado por decisión del usuario: no hubo que construir nada",
            "| **Tamaño** | chico |"))
        self.assertEqual([], self.cerrados())

    def test_lo_cerrado_antes_del_corte_queda_de_su_lado(self):
        self.escribir("pendientes/hecho/viejo.md", FICHA % ("Viejo", "cerrado el 2026-08-06", "| **Tamaño** | chico |"))
        self.assertEqual([], self.cerrados())

    def test_sin_fecha_declarada_tampoco_se_exige(self):
        self.escribir("pendientes/hecho/sin-fecha.md", "# Hecho · Algo viejo\n\nTexto sin ficha ni fecha.\n")
        self.assertEqual([], self.cerrados())


EPICA = "documentacion/epicas/EP-009-algo"
HU = EPICA + "/HU-001-una-cosa"
PENDIENTE = ("# Pendiente: algo falla\n\n| | |\n|---|---|\n| **De dónde sale** | {origen} |\n\n"
             "## El problema\n\nAlgo.\n\n## Por qué importa\n\nAlgo.\n")
ANALISIS = ("# Análisis 1: algo\n\n{marca}## Lo que se tiene que hacer\n\n"
            "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
            "| 1 | Hacer algo | 1 | {paso} |\n")
MARCA = "> **Aprobado** por el usuario el 2026-10-02, en el turno 3.\n\n"
HU_MD = "# HU-001 · Una cosa\n\n| Campo | Valor |\n|---|---|\n| **Estado** | {estado} |\n"


class LaFormaNueva(Carpeta):
    """`EP-023·HU-003` · El pendiente carpeta: sus tres partes, su estado calculado y su índice."""

    def setUp(self):
        super().setUp()
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Lista"))
        self.carpeta = os.path.join(self.raiz, *(EPICA + "/pendientes/110-algo-falla").split("/"))

    def pendiente(self, origen="algo", marca=MARCA, paso="[HU-001](../../HU-001-una-cosa/HU-001-una-cosa.md)"):
        self.escribir(EPICA + "/pendientes/110-algo-falla/pendiente.md", PENDIENTE.format(origen=origen))
        if marca is not None:
            self.escribir(EPICA + "/pendientes/110-algo-falla/analisis-1.md", ANALISIS.format(marca=marca, paso=paso))

    def terminar(self, estado="Terminada"):
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado=estado))

    def estado(self, carpeta=None):
        return Pendientes(self.raiz).estado(carpeta or self.carpeta)

    def fallas(self):
        return [h for h in NumeracionDePendientes(self.raiz).validar() if h.severidad == FALLA]

    def test_el_pendiente_con_sus_tres_partes_pasa(self):
        self.pendiente()
        self.assertEqual([], self.fallas())

    def test_al_que_le_falta_una_parte_se_le_nombra(self):
        self.escribir(EPICA + "/pendientes/110-algo-falla/pendiente.md", "# Pendiente: algo\n\n## El problema\n\nAlgo.\n")
        fallas = [h.mensaje for h in self.fallas()]
        self.assertEqual(1, len(fallas))
        self.assertIn("«De dónde sale»", fallas[0])
        self.assertIn("«Por qué importa»", fallas[0])

    def test_sin_analisis_aprobado_esta_abierto(self):
        self.pendiente(marca="")
        self.assertEqual("abierto", self.estado())

    def test_con_su_hu_sin_terminar_esta_abierto(self):
        self.pendiente()
        self.assertEqual("abierto", self.estado())

    def test_con_su_hu_terminada_esta_cerrado_y_su_archivo_no_cambia(self):
        self.pendiente()
        self.terminar("Terminada el 2026-10-02")
        antes = self.leer(EPICA + "/pendientes/110-algo-falla/pendiente.md")
        self.assertEqual("cerrado", self.estado())
        self.assertEqual(antes, self.leer(EPICA + "/pendientes/110-algo-falla/pendiente.md"))

    def test_la_hu_nombrada_sin_enlace_tambien_cuenta(self):
        self.pendiente(paso="EP-009, HU-001, fase A")
        self.terminar()
        self.assertEqual("cerrado", self.estado())

    def test_la_hu_escrita_con_espacio_tambien_cuenta(self):
        self.pendiente(paso="EP-009, HU 1")
        self.terminar()
        self.assertEqual("cerrado", self.estado())

    def test_la_fila_de_la_epica_espera_a_que_la_epica_termine(self):
        self.pendiente(paso="EP-009, la épica")
        self.assertEqual("abierto", self.estado())
        self.escribir(EPICA + "/epica.md", HU_MD.format(estado="Terminada el 2026-10-03"))
        self.assertEqual("cerrado", self.estado())

    def test_lo_hecho_en_el_mismo_analisis_no_espera_nada(self):
        self.pendiente(paso="Este análisis, de una y sin fase")
        self.assertEqual("cerrado", self.estado())

    def test_el_seguimiento_toma_el_estado_de_su_padre_y_espera_la_comprobacion(self):
        self.pendiente()
        dia = "historico-chat/resumenes/2026-10-02/pendientes/111-espera"
        self.escribir(dia + "/pendiente.md", PENDIENTE.format(
            origen="[el del estándar](../../../../../%s/pendientes/110-algo-falla/pendiente.md)" % EPICA))
        hijo = os.path.join(self.raiz, *dia.split("/"))
        self.assertEqual("abierto", self.estado(hijo))
        self.terminar()
        self.assertEqual("abierto", self.estado(hijo))      # falta comprobar (HU-003, CA-11)
        self.escribir(dia + "/aviso-resuelto.md", "**Comprobado:** 2026-10-03\n")
        self.assertEqual("cerrado", self.estado(hijo))

    def test_el_seguimiento_en_otro_proyecto_cierra_con_el_aviso(self):
        """Lo de `test_el_proyecto_reporta_y_se_entera`, sin el aviso que escribe
        `aviso_resuelto.py` (de otro grupo): el archivo se pone a mano."""
        estandar, proyecto = os.path.join(self.raiz, "estandar"), os.path.join(self.raiz, "proyecto")
        reportado = EPICA + "/pendientes/110-algo-falla"
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Lista"), raiz=estandar)
        self.escribir(reportado + "/pendiente.md", PENDIENTE.format(origen="algo"), raiz=estandar)
        self.escribir(reportado + "/analisis-1.md", ANALISIS.format(
            marca=MARCA, paso="[HU-001](../../HU-001-una-cosa/HU-001-una-cosa.md)"), raiz=estandar)
        seguimiento = "historico-chat/resumenes/2026-10-02/pendientes/5-espera"
        self.escribir(seguimiento + "/pendiente.md", PENDIENTE.format(
            origen="[110](../../../../../../estandar/%s/pendiente.md)" % reportado), raiz=proyecto)
        hijo = os.path.join(proyecto, *seguimiento.split("/"))
        self.assertEqual("abierto", Pendientes(proyecto).estado(hijo))
        self.escribir(HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"), raiz=estandar)
        self.assertEqual("abierto", Pendientes(proyecto).estado(hijo))
        self.escribir(seguimiento + "/aviso-resuelto.md", "**Comprobado:** 2026-10-04\n", raiz=proyecto)
        self.assertEqual("cerrado", Pendientes(proyecto).estado(hijo))

    def test_el_pendiente_reunido_toma_el_estado_del_que_lo_reune(self):
        self.escribir("p/110-a/pendiente.md", "# P\n")
        reunido = os.path.dirname(self.escribir(
            "p/111-b/pendiente.md", "# P\n\nSe resuelve en el [análisis 1 del 110](../110-a/analisis-1.md).\n"))
        self.assertTrue(Pendientes(self.raiz).resuelto_en(reunido).endswith("110-a"))

    def test_el_proximo_numero_cuenta_todas_las_carpetas(self):
        self.pendiente()
        self.escribir("historico-chat/resumenes/2026-10-02/pendientes/115-suelto/pendiente.md",
                      PENDIENTE.format(origen="algo"))
        self.escribir("pendientes/90-viejo.md", "# Pendiente · viejo\n")
        self.assertEqual(116, Pendientes(self.raiz).proximo_libre())

    def test_el_mismo_numero_en_dos_carpetas_falla(self):
        self.pendiente()
        self.escribir("historico-chat/resumenes/2026-10-02/pendientes/110-otro/pendiente.md",
                      PENDIENTE.format(origen="algo"))
        self.assertTrue(any("el número 110" in h.mensaje for h in self.fallas()))

    def test_el_que_paso_a_la_forma_nueva_no_choca_con_su_archivo_viejo(self):
        self.pendiente()
        self.escribir("pendientes/110-algo-falla.md", "# Pendiente · algo falla\n")
        self.assertEqual([], [h for h in self.fallas() if "110" in h.mensaje])

    def test_el_indice_lista_todos_con_donde_viven_y_su_estado(self):
        self.pendiente()
        self.escribir("pendientes/90-viejo.md", "# Pendiente · viejo\n\n**Estado:** abierto.\n")
        ruta = Pendientes(self.raiz).escribir_indice()
        self.assertEqual(os.path.join(Proyecto(self.raiz).raiz, "documentacion", "pendientes.md"), ruta)
        texto = self.leer("documentacion/pendientes.md")
        self.assertIn("| 90 | [viejo](../pendientes/90-viejo.md) | `pendientes/`, forma anterior | abierto |", texto)
        self.assertIn("| 110 | [algo falla](epicas/EP-009-algo/pendientes/110-algo-falla/pendiente.md) "
                      "| `documentacion/epicas/EP-009-algo/pendientes/110-algo-falla` | abierto |", texto)


# ── acciones ──────────────────────────────────────────────────────────────

class InventarioDeAccionesSinHuecos(Carpeta):
    """`EP-001·HU-012` · Cada clase con su nivel y su ejemplo, y ninguna herramienta sin clase."""

    def copia(self, cambio=None):
        with io.open(os.path.join(RAIZ, ANEXO), encoding="utf-8") as f:
            texto = f.read()
        self.escribir(ANEXO.replace(os.sep, "/"), cambio(texto) if cambio else texto)
        return InventarioDeAcciones(self.raiz)

    def test_ninguna_herramienta_queda_sin_clase(self):
        self.assertEqual([], InventarioDeAcciones(RAIZ).validar())

    def test_si_falta_una_clase_se_reporta(self):
        """Sin este, «cero huérfanas» podría significar que no se busca nada."""
        hallazgos = self.copia(lambda t: t.replace("**Tocar datos reales**", "**Otra cosa**")).validar()
        self.assertTrue(hallazgos)
        self.assertIn("datos", hallazgos[0].mensaje)

    def test_las_doce_clases_se_leen(self):
        self.assertEqual(12, len(InventarioDeAcciones(RAIZ).clases()))

    def test_ninguna_fila_sin_ejemplo_y_todos_los_niveles_de_la_escala(self):
        for nombre, nivel, ejemplo in InventarioDeAcciones(RAIZ).clases():
            self.assertTrue(ejemplo, nombre)
            self.assertTrue(any(x in nivel for x in ESCALA), nombre)

    def test_un_nivel_inventado_se_reporta(self):
        v = self.copia(lambda t: t.replace(
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | 🟢 |",
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | medio |"))
        self.assertTrue([h for h in v.validar() if "no es de la escala" in h.mensaje])

    def test_dos_niveles_en_la_misma_fila_se_reportan(self):
        v = self.copia(lambda t: t.replace(
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | 🟢 |",
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | 🟢 o 🔴 |"))
        self.assertTrue([h for h in v.validar() if "niveles en la misma fila" in h.mensaje])

    def test_una_fila_sin_ejemplo_se_reporta(self):
        v = self.copia(lambda t: t.replace("| 🟢 | Nada: no cambia estado | — |", "| 🟢 |  | — |"))
        self.assertTrue([h for h in v.validar() if "no tiene ejemplo" in h.mensaje])

    def test_sin_anexo_se_reporta_y_no_revienta(self):
        hallazgos = InventarioDeAcciones(self.raiz).validar()
        self.assertEqual([FALLA], [h.severidad for h in hallazgos])
        self.assertEqual("", InventarioDeAcciones(self.raiz).linea_resumen())

    def test_el_resumen_cuenta_los_tres_niveles(self):
        linea = InventarioDeAcciones(RAIZ).linea_resumen()
        for marca in ESCALA:
            self.assertIn(marca, linea)


# ── amarre ────────────────────────────────────────────────────────────────

class ElMapaDelAmarreNoEnvejece(Carpeta):
    """`EP-005·HU-011·CA-03` · Una pieza nueva sin clasificar se nota, y
    clasificarla la calla: uno que reporta siempre se apaga."""

    def setUp(self):
        super().setUp()
        os.makedirs(os.path.join(self.raiz, "anatomia"))
        shutil.copy(os.path.join(RAIZ, MAPA_AMARRE), os.path.join(self.raiz, MAPA_AMARRE))
        destino = os.path.join(self.raiz, "validadores")
        os.makedirs(destino)
        for n in os.listdir(os.path.join(RAIZ, "validadores")):
            if n.endswith(".py"):
                shutil.copy(os.path.join(RAIZ, "validadores", n), os.path.join(destino, n))

    def pieza(self, nombre, contenido):
        self.escribir("validadores/" + nombre, contenido)

    def agregar_al_mapa(self, texto):
        with io.open(os.path.join(self.raiz, MAPA_AMARRE), "a", encoding="utf-8") as f:
            f.write(texto)

    def fallas(self, pieza="zzz_prueba.py"):
        """Las fallas de la pieza de la prueba. Las viejas contaban todas, y
        dependían de que el mapa real estuviera al día: con el mapa atrasado
        fallaban por piezas ajenas a la prueba."""
        return [h for h in MapaDelAmarre(self.raiz).validar() if h.severidad == FALLA and pieza in h.mensaje]

    def test_en_el_estandar_ninguna_pieza_queda_sin_columna(self):
        self.assertEqual([], [h for h in MapaDelAmarre(RAIZ).validar() if h.severidad == FALLA])

    def test_el_recuento_del_programa_coincide_con_el_del_mapa(self):
        """Riesgo `R-01`: que el programa y el mapa midan distinto y nadie lo note."""
        p = MapaDelAmarre(RAIZ).piezas()
        with io.open(os.path.join(RAIZ, MAPA_AMARRE), encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("%d amarrados de %d" % (sum(1 for n in p.values() if n > 0), len(p)), texto)
        for n in [n for n, c in p.items() if c == 0]:
            self.assertIn("`%s`" % n, texto, n)

    def test_una_pieza_nueva_sin_clasificar_se_reporta(self):
        self.assertEqual([], self.fallas())
        self.pieza("zzz_prueba.py", "# usa CLAUDE.md\n")
        self.assertEqual(1, len(self.fallas()))

    def test_clasificarla_la_calla(self):
        self.pieza("zzz_prueba.py", "# usa CLAUDE.md\n")
        self.agregar_al_mapa("\n\n| Pieza | Libre o amarrada | Por qué |\n|---|---|---|\n"
                             "| `zzz_prueba.py` | 🟡 adaptador | Nombra la herramienta |\n")
        self.assertEqual([], self.fallas())

    def test_nombrarla_en_una_frase_no_la_clasifica(self):
        self.pieza("zzz_prueba.py", "# usa CLAUDE.md\n")
        self.agregar_al_mapa("\n\n`zzz_prueba.py` sigue sin clasificar: no es de esta fase.\n")
        self.assertTrue(self.fallas())

    def test_la_linea_que_solo_lista_nombres_la_clasifica(self):
        self.pieza("zzz_libre.py", "# solo lee archivos\n")
        self.agregar_al_mapa("\n\n`otra.py` · `zzz_libre.py`\n")
        self.assertFalse([h for h in MapaDelAmarre(self.raiz).validar() if "zzz_libre.py" in h.mensaje])

    def test_una_pieza_que_el_mapa_nombra_y_ya_no_existe_se_reporta(self):
        os.remove(os.path.join(self.raiz, "validadores", "citas.py"))
        avisos = [h for h in MapaDelAmarre(self.raiz).validar() if h.severidad == AVISO]
        self.assertTrue([h for h in avisos if "citas.py" in h.mensaje])

    def test_la_que_no_toca_la_herramienta_tambien_tiene_que_estar(self):
        self.pieza("zzz_libre.py", "# solo lee archivos\n")
        self.assertTrue([h for h in MapaDelAmarre(self.raiz).validar() if "zzz_libre.py" in h.mensaje])

    def test_sin_mapa_se_reporta_y_no_revienta(self):
        os.remove(os.path.join(self.raiz, MAPA_AMARRE))
        self.assertEqual([FALLA], [h.severidad for h in MapaDelAmarre(self.raiz).validar()])

    def test_el_propio_medidor_no_se_reporta_a_si_mismo(self):
        self.assertNotIn("amarre.py", MapaDelAmarre(RAIZ).piezas())

    def test_el_recuento_incluye_las_dos_carpetas_y_los_enganches_cuentan(self):
        piezas = MapaDelAmarre(RAIZ).piezas()
        self.assertIn("enlaces.py", piezas)
        for guion in ("hook_md.py", "hook_sesion.py"):
            self.assertGreater(piezas.get(guion, 0), 0, "%s no nombra la herramienta?" % guion)

    def test_el_resumen_dice_los_tres_numeros(self):
        linea = MapaDelAmarre(RAIZ).linea_resumen()
        for palabra in ("Piezas", "amarradas", "libres"):
            self.assertIn(palabra, linea)


# ── sitio ─────────────────────────────────────────────────────────────────

class ElMapaDelSitioNoEnvejece(Carpeta):
    """`EP-005·HU-011` · Por los dos lados, y callado cuando está al día."""

    def setUp(self):
        super().setUp()
        os.makedirs(os.path.join(self.raiz, "anatomia"))

    def carpeta(self, nombre):
        os.makedirs(os.path.join(self.raiz, nombre), exist_ok=True)

    def mapa(self, texto):
        self.escribir("anatomia/mapa-del-sitio.md", texto)

    def hallazgos(self):
        return MapaDelSitio(self.raiz).validar()

    def test_la_carpeta_nueva_que_el_mapa_no_nombra_es_falla(self):
        self.carpeta("validadores")
        self.mapa("# Mapa\n\nanatomia/ es esto.\n")
        self.assertTrue(any("validadores/" in h.mensaje for h in self.hallazgos() if h.severidad == FALLA))

    def test_falta_el_mapa_entero(self):
        self.carpeta("base")
        h = self.hallazgos()
        self.assertEqual(FALLA, h[0].severidad)
        self.assertIn("falta el mapa del sitio", h[0].mensaje)

    def test_la_que_el_mapa_nombra_y_ya_no_existe_es_aviso(self):
        self.carpeta("base")
        self.mapa("# Mapa\n\n- `base/` la norma\n- `diplomado-ia/` apuntes\n- anatomia/ este archivo\n")
        h = self.hallazgos()
        self.assertEqual([], [x for x in h if x.severidad == FALLA])
        self.assertTrue(any("diplomado-ia/" in x.mensaje for x in h if x.severidad == AVISO))

    def test_nombrada_la_carpeta_se_calla(self):
        self.carpeta("base")
        self.carpeta("validadores")
        self.mapa("# Mapa\n\nbase/ la norma · validadores/ los programas ·\nanatomia/ este archivo\n")
        self.assertEqual([], self.hallazgos())

    def test_lo_local_y_lo_generado_no_es_del_mapa(self):
        for nombre in (".venv", "__pycache__", "terceros", "node_modules"):
            self.carpeta(nombre)
        self.mapa("# Mapa\n\nanatomia/ este archivo\n")
        self.assertEqual([], self.hallazgos())

    def test_el_recuento_se_puede_mirar_sin_abrir_el_mapa(self):
        self.carpeta("base")
        self.carpeta("plantillas")
        self.mapa("# Mapa\n\nbase/ la norma · anatomia/ este archivo\n")
        linea = MapaDelSitio(self.raiz).linea_resumen()
        self.assertIn("Carpetas de primer nivel: 3", linea)
        self.assertIn("sin nombrar: 1", linea)

    def test_el_nombre_parecido_no_cuenta_por_la_carpeta(self):
        self.carpeta("plantillas")
        self.mapa("# Mapa\n\nmis-plantillas/ otra cosa · anatomia/ este archivo\n")
        self.assertTrue(any("`plantillas/`" in h.mensaje for h in self.hallazgos() if h.severidad == FALLA))


# ── brevedad y redacción ──────────────────────────────────────────────────

def transcripcion(*respuestas):
    """Una transcripción como la escribe `hook_historico.py`."""
    partes = ["<!-- sesion: abc -->\n\n# 2026-01-02 — Sesión\n\n## Conversación\n"]
    for i, texto in enumerate(respuestas, 1):
        partes.append("\n### %d · Usuario — 2026-01-02 10:0%d:00\n> algo\n" % (i, i))
        partes.append("\n**Agente** — 2026-01-02 10:0%d:30\n<!-- agente: %d -->\n\n%s\n" % (i, i, texto))
    return "".join(partes)


class LaBrevedadSeMide(Carpeta):
    """`00·ID9` · Se cuenta lo que se lee, y nunca detiene."""

    def archivo(self, contenido):
        return self.escribir("historico-chat/2026-01-02-sesion.md", contenido)

    def test_cuenta_una_y_varias_respuestas(self):
        self.assertEqual(1, len(Respuestas.de(self.archivo(transcripcion("hola")))))
        self.assertEqual(3, len(Respuestas.de(self.archivo(transcripcion("una", "dos", "tres")))))

    def test_el_largo_es_el_del_texto_sin_los_comentarios_de_maquina(self):
        self.assertEqual(5, Respuestas.de(self.archivo(transcripcion("12345")))[0][1])

    def test_el_mensaje_del_usuario_no_cuenta(self):
        self.assertEqual(3, sum(n for _f, n in Respuestas.de(self.archivo(transcripcion("abc")))))

    def test_una_respuesta_vacia_no_entra(self):
        self.assertEqual(1, len(Respuestas.de(self.archivo(transcripcion("", "algo")))))

    def test_la_tabla_y_el_codigo_cuentan(self):
        self.assertGreater(Respuestas.de(self.archivo(transcripcion("| a | b |\n|---|---|\n| 1 | 2 |")))[0][1], 10)

    def test_la_mediana_y_la_maxima(self):
        self.assertEqual(100, Respuestas.resumen(self.archivo(transcripcion("a" * 10, "b" * 100, "c" * 1000)))["mediana"])
        self.assertEqual(15, Respuestas.resumen(self.archivo(transcripcion("a" * 10, "b" * 20)))["mediana"])
        self.assertEqual(900, Respuestas.resumen(self.archivo(transcripcion("a" * 10, "b" * 900)))["maxima"])

    def test_sin_respuestas_no_revienta(self):
        self.assertEqual({"cuantas": 0, "mediana": 0, "maxima": 0, "total": 0},
                         Respuestas.resumen(self.archivo("# 2026-01-02 — Sesión\n\nsin nada\n")))

    def test_la_sesion_larga_avisa_y_nunca_falla(self):
        self.archivo(transcripcion(*["x" * 9000] * 10))
        self.assertEqual([AVISO], [h.severidad for h in Brevedad(self.raiz).validar()])

    def test_la_sesion_corta_calla(self):
        self.archivo(transcripcion(*["corto"] * 10))
        self.assertEqual([], Brevedad(self.raiz).validar())

    def test_una_sesion_de_pocos_turnos_no_avisa(self):
        self.archivo(transcripcion(*["x" * 9000] * 4))
        self.assertEqual([], Brevedad(self.raiz).validar())

    def test_se_mira_la_mediana_no_la_maxima(self):
        self.archivo(transcripcion(*(["corto"] * 9 + ["x" * 90000])))
        self.assertEqual([], Brevedad(self.raiz).validar())

    def test_sin_historico_no_dice_nada(self):
        self.assertEqual([], Brevedad(self.raiz).transcripciones())
        self.assertEqual([], Brevedad(self.raiz).validar())
        self.assertEqual("", Brevedad(self.raiz).como_texto())

    def test_lo_que_no_es_transcripcion_se_ignora(self):
        self.archivo(transcripcion("algo"))
        self.escribir("historico-chat/README.md", "# Cómo se usa\n")
        self.assertEqual(1, len(Brevedad(self.raiz).transcripciones()))

    def test_el_texto_sale_con_una_linea_por_sesion(self):
        self.archivo(transcripcion("algo"))
        self.assertIn("2026-01-02-sesion", Brevedad(self.raiz).como_texto())


class LoQueSeAcabaDeEscribirSeMide(unittest.TestCase):
    """`00·ID8`, `00·ID9`, `00·ID10` sobre un turno. Se calla cuando todo está bien."""

    def test_el_trato_directo_se_cuenta(self):
        self.assertEqual(1, len(Redaccion.tratos("Usted abre la terminal.")))
        self.assertEqual(1, len(Redaccion.tratos("Después tú lo ejecutas.")))

    def test_la_tercera_persona_y_el_infinitivo_no_se_cuentan(self):
        self.assertEqual([], Redaccion.tratos("El agente abre la terminal y ejecuta el programa."))
        self.assertEqual([], Redaccion.tratos("Abrir la terminal y ejecutar el programa."))

    def test_lo_citado_y_lo_que_va_en_codigo_no_se_cuentan(self):
        self.assertEqual([], Redaccion.tratos("El texto dice «usted» y eso es una cita."))
        self.assertEqual([], Redaccion.tratos("```\nprint('usted')\n```"))

    def test_se_dice_en_que_linea_aparece(self):
        self.assertEqual(2, Redaccion.tratos("primera línea\nUsted abre la terminal.")[0][0])

    def test_una_palabra_que_contiene_tu_no_cuenta(self):
        self.assertEqual([], Redaccion.tratos("El estudio y el atún."))

    def test_la_medida_de_un_turno(self):
        self.assertEqual(5, Redaccion.medir("  12345  ")["caracteres"])
        self.assertEqual(1, Redaccion.medir("El agente abre la terminal — y la cierra.")["marcas"])
        self.assertEqual(0, Redaccion.medir("```\nuna raya — dentro del código\n```")["marcas"])
        limpio = Redaccion.medir("El agente abre la terminal y ejecuta el programa.")
        self.assertEqual((0, []), (limpio["marcas"], limpio["tratos"]))

    def test_la_linea_de_cierre(self):
        self.assertEqual("", Redaccion.linea_de_cierre("El agente abre la terminal y ejecuta el programa."))
        self.assertEqual("", Redaccion.linea_de_cierre("a" * 100))
        linea = Redaccion.linea_de_cierre("Usted abre la terminal.")
        self.assertIn("00·ID10", linea)
        self.assertIn("usted", linea)
        self.assertIn("00·ID8", Redaccion.linea_de_cierre("El agente abre la terminal — y la cierra."))

    def test_el_largo_se_compara_contra_el_umbral_de_brevedad(self):
        linea = Redaccion.linea_de_cierre("a" * (HOLGADO + 1), 900)
        self.assertIn("00·ID9", linea)
        self.assertIn(str(HOLGADO), linea)
        self.assertIn("900", linea)

    def test_las_tres_caben_en_una_linea(self):
        linea = Redaccion.linea_de_cierre("Usted abre la terminal — y la cierra. " + "a" * HOLGADO)
        for regla in ("00·ID8", "00·ID9", "00·ID10"):
            self.assertIn(regla, linea)


# ── expediente ────────────────────────────────────────────────────────────

class ElExpedienteSeMide(Carpeta):
    """Encuentra el entregable por su nombre, distingue sus tres estados y nunca detiene."""

    def texto(self):
        return "\n".join(Expediente(self.raiz).reporte()[0])

    def test_encuentra_por_nombre_viva_donde_viva(self):
        self.escribir("prompts/miproyecto-planteamiento.md", "El problema.\n")
        self.escribir("docs/22-plan-de-mantenimiento.md", "Las rutinas.\n")
        self.assertIn("prompts/miproyecto-planteamiento.md", self.texto())
        self.assertIn("docs/22-plan-de-mantenimiento.md", self.texto())

    def test_el_molde_en_plantillas_no_es_el_entregable(self):
        self.escribir("plantillas/ciclo/12-estudio-factibilidad.md", "Molde con «…».\n")
        self.assertIn("| 12 | Estudio de factibilidad | (no hay) | **Falta** |", self.texto())

    def test_un_nombre_parecido_no_cuenta(self):
        self.escribir("docs/replanteamiento.md", "Otra cosa.\n")
        self.assertIn("| 01 | Planteamiento | (no hay) | **Falta** |", self.texto())

    def test_los_tres_estados(self):
        self.escribir("a/planteamiento.md", "Todo escrito.\n")
        self.escribir("a/inventario-funcionalidades.md", "Falta esto: «…» y esto: «…»\n")
        self.escribir("a/documentacion-de-api.md", "No aplica porque el sistema no expone API.\n")
        texto = self.texto()
        self.assertIn("| Completo |", texto)
        self.assertIn("En llenado (2 espacios)", texto)
        self.assertIn("Declara no aplicar", texto)

    def test_declarar_no_aplica_con_espacios_es_en_llenado(self):
        self.assertEqual(("en llenado", 1), Expediente.estado("No aplica porque «…»\n"))

    def test_lo_que_falta_es_aviso_nunca_falla(self):
        hallazgos = Expediente(self.raiz).validar()
        self.assertTrue(hallazgos)
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])

    def test_cuenta_la_cadena_de_ejecucion(self):
        self.escribir("documentacion/epicas/EP-001-x/epica.md", "La épica.\n")
        self.escribir("documentacion/epicas/EP-001-x/HU-001-y/HU-001-y.md", "La historia.\n")
        self.escribir("documentacion/epicas/EP-001-x/HU-001-y/A-EP-001-HU-001-z/plan_trabajo.md", "El plan.\n")
        self.assertIn("1 épica(s), 1 HU, 1 fase(s) con plan", self.texto())


# ── reaperturas ───────────────────────────────────────────────────────────

def tabla(estaciones):
    filas = "\n".join("| %d | Etapa | puerta | %s |" % (n, "☑" if v else "☐") for n, v in sorted(estaciones.items()))
    return "# Estado de fase\n\n| # | Etapa | Puerta | Estado |\n|---|---|---|---|\n%s\n" % filas


class LaFaseReabiertaSeDistingue(Carpeta):
    """Se deriva de la historia de la casilla, no de las palabras."""

    def repo(self, *versiones):
        repo_vacio(self.raiz)
        for i, estaciones in enumerate(versiones):
            self.escribir("documentacion/epicas/EP-001/HU-001/A-fase/estado-fase.md", tabla(estaciones))
            git(self.raiz, "add", "-A")
            git(self.raiz, "commit", "-qm", "v%d" % i)
        return Reaperturas(self.raiz).reaperturas()

    def test_cerrar_y_volver_atras_es_reapertura(self):
        self.assertEqual(1, len(self.repo({7: True, 8: True}, {7: False, 8: True})))

    def test_dos_vueltas_se_cuentan_dos(self):
        self.assertEqual(2, len(self.repo({7: True}, {7: False}, {7: True}, {7: False})[0][1]))

    def test_avanzar_no_es_reapertura(self):
        self.assertEqual([], self.repo({7: False, 8: False}, {7: True, 8: False}, {7: True, 8: True}))

    def test_volver_atras_antes_de_cerrar_no_cuenta(self):
        self.assertEqual([], self.repo({3: True, 7: False}, {3: False, 7: False}))

    def test_una_fase_recien_creada_no_es_reapertura(self):
        self.assertEqual([], self.repo({7: False}))

    def test_sin_epicas_no_revienta_y_el_resumen_va_igual(self):
        self.assertEqual([], Reaperturas(self.raiz).reaperturas())
        self.assertIn("Fases reabiertas: 0", Reaperturas(self.raiz).linea_resumen())


class LasReaperturasDelEstandar(unittest.TestCase):
    """Sobre el repositorio de verdad: recorrer su historia tarda, así que se recorre una vez."""

    @classmethod
    def setUpClass(cls):
        cls.validador = Reaperturas(RAIZ)
        cls.encontradas = cls.validador.reaperturas()

    def test_encuentra_las_dos_que_se_reabrieron_y_no_las_que_solo_hablan_de_reabrir(self):
        rutas = " ".join(r for r, _v in self.encontradas)
        self.assertEqual(2, len(self.encontradas))
        self.assertIn("A-EP-005-HU-008", rutas)
        self.assertIn("A-EP-007-HU-006", rutas)

    def test_nunca_es_una_falla(self):
        self.validador.reaperturas = lambda: self.encontradas
        self.assertEqual([], [h for h in self.validador.validar() if h.severidad == FALLA])


# ── sesiones ──────────────────────────────────────────────────────────────

class DosSesionesNoSePisan(Carpeta):
    """`80` · Un commit que mezcla dos sesiones avisa. La mitad es de lo que NO avisa."""

    def setUp(self):
        super().setUp()
        os.makedirs(os.path.join(self.raiz, "historico-chat"))
        self.sesiones = Sesiones(self.raiz)

    def toca(self, sesion, *relativos):
        for rel in relativos:
            self.sesiones.anotar(sesion, self.escribir(rel))

    def validar(self, *entrando):
        """Lo que entra en el commit lo dice la prueba, no git. No se hereda: una
        subclase se registraría con el mismo nombre."""
        v = SesionesMezcladas(self.raiz)
        v.preparados = lambda: list(entrando)
        return v.validar()

    def test_el_commit_que_mezcla_dos_sesiones_avisa(self):
        self.toca("aaa111", "validadores/plantillas.py")
        self.toca("bbb222", "CHANGELOG.md")
        h = self.validar("validadores/plantillas.py", "CHANGELOG.md")
        self.assertEqual([AVISO], [x.severidad for x in h])
        self.assertIn("2 sesiones", h[0].mensaje)

    def test_el_aviso_nombra_algun_archivo(self):
        self.toca("aaa111", "mio.md")
        self.toca("bbb222", "ajeno.py")
        self.assertIn("ajeno.py", self.validar("mio.md", "ajeno.py")[0].mensaje)

    def test_una_sola_sesion_no_avisa(self):
        self.toca("aaa111", "uno.md", "dos.md")
        self.assertEqual([], self.validar("uno.md", "dos.md"))

    def test_un_commit_vacio_no_avisa(self):
        self.toca("aaa111", "uno.md")
        self.toca("bbb222", "dos.md")
        self.assertEqual([], self.validar())

    def test_lo_que_toco_otra_sesion_pero_no_entra_no_avisa(self):
        self.toca("aaa111", "mio.md")
        self.toca("bbb222", "ajeno.py")
        self.assertEqual([], self.validar("mio.md"))

    def test_una_sesion_vieja_ya_no_cuenta(self):
        self.toca("vieja1", "ajeno.py")
        viejo = time.time() - VIGENCIA - 60
        os.utime(os.path.join(self.raiz, TOCADO, "vieja1.txt"), (viejo, viejo))
        self.toca("aaa111", "mio.md")
        self.assertEqual([], self.validar("mio.md", "ajeno.py"))

    def test_el_mismo_archivo_tocado_por_las_dos_no_alcanza_para_callar(self):
        self.toca("aaa111", "indice.md", "mio.md")
        self.toca("bbb222", "indice.md", "ajeno.py")
        self.assertEqual(1, len(self.validar("indice.md", "mio.md", "ajeno.py")))

    def test_no_se_anota_lo_que_es_de_otro_proyecto(self):
        otro = tempfile.TemporaryDirectory()
        self.addCleanup(otro.cleanup)
        self.sesiones.anotar("aaa111", self.escribir("cosa.md", raiz=otro.name))
        self.assertEqual({}, self.sesiones.registros())

    def test_sin_identificador_de_sesion_no_se_anota_nada(self):
        self.toca("", "uno.md")
        self.assertEqual({}, self.sesiones.registros())

    def test_el_mismo_archivo_dos_veces_se_anota_una(self):
        self.toca("aaa111", "uno.md")
        self.toca("aaa111", "uno.md")
        self.assertEqual({"aaa111": {"uno.md"}}, self.sesiones.registros())


class ElTurnoAnotaLoQueCambio(Carpeta):
    """`EP-005·HU-020` · Lo escrito por un guion queda anotado, y lo de antes no se reclama."""

    def setUp(self):
        super().setUp()
        if not shutil.which("git"):
            self.skipTest("sin git")
        repo_vacio(self.raiz)
        self.sesiones = Sesiones(self.raiz)

    def reloj(self, sesion="s1"):
        return os.path.getmtime(self.sesiones.ruta_de(sesion))

    def escribir_en(self, rel, cuando, texto="x\n"):
        ruta = self.escribir(rel, texto)
        os.utime(ruta, (cuando, cuando))
        return ruta

    def registro(self, sesion="s1"):
        return Sesiones.leer_sesion(self.sesiones.ruta_de(sesion))

    def test_lo_escrito_sin_las_herramientas_queda_anotado(self):
        self.sesiones.anotar_el_turno("s1")
        self.escribir_en("del-guion.md", self.reloj() + 10)
        self.sesiones.anotar_el_turno("s1")
        self.assertIn("del-guion.md", self.registro())

    def test_no_reclama_un_archivo_de_antes_del_turno(self):
        self.sesiones.anotar_el_turno("s1")
        self.escribir_en("viejo.md", self.reloj() - 3600)
        self.sesiones.anotar_el_turno("s1")
        self.assertNotIn("viejo.md", self.registro())

    def test_la_primera_vuelta_no_reclama_el_arbol_y_deja_el_reloj(self):
        for i in range(5):
            self.escribir("sucio-%d.md" % i)
        self.assertEqual([], self.sesiones.anotar_el_turno("s1"))
        self.assertEqual(set(), self.registro())
        self.assertTrue(os.path.isfile(self.sesiones.ruta_de("s1")))

    def test_solo_entra_lo_modificado_despues_del_reloj(self):
        self.sesiones.anotar_el_turno("s1")
        self.escribir_en("antes.md", self.reloj() - 60)
        self.escribir_en("despues.md", self.reloj() + 60)
        self.sesiones.anotar_el_turno("s1")
        self.assertIn("despues.md", self.registro())
        self.assertNotIn("antes.md", self.registro())

    def test_un_borrado_se_anota_aunque_no_tenga_fecha(self):
        self.escribir("condenado.md")
        git(self.raiz, "add", "-A")
        git(self.raiz, "commit", "-qm", "base")
        self.sesiones.anotar_el_turno("s1")
        os.remove(os.path.join(self.raiz, "condenado.md"))
        self.sesiones.anotar_el_turno("s1")
        self.assertIn("condenado.md", self.registro())

    def test_dos_sesiones_con_el_mismo_archivo_avisan(self):
        ruta = self.escribir("compartido.md")
        for sesion in ("s1", "s2"):
            self.sesiones.anotar(sesion, ruta)
        git(self.raiz, "add", "compartido.md")
        h = SesionesMezcladas(self.raiz).validar()
        self.assertEqual(1, len(h))
        self.assertIn("2 sesiones", h[0].mensaje)

    def test_el_caso_real_una_sesion_escribe_y_otra_commitea(self):
        for nombre in ("manual-a.md", "manual-b.md"):
            self.escribir(nombre)
        self.sesiones.anotar_el_turno("otra")
        for nombre in ("manual-a.md", "manual-b.md"):
            self.escribir_en(nombre, self.reloj("otra") + 10, "cambiado\n")
        self.sesiones.anotar_el_turno("otra")
        self.sesiones.anotar_el_turno("mia")
        self.escribir_en("manual-a.md", self.reloj("mia") + 10, "y otra vez\n")
        self.sesiones.anotar_el_turno("mia")
        git(self.raiz, "add", "-A")
        self.assertEqual(1, len(SesionesMezcladas(self.raiz).validar()))

    def test_no_duplica_lo_que_la_herramienta_ya_anoto(self):
        self.sesiones.anotar_el_turno("s1")
        ruta = self.escribir_en("doble.md", self.reloj() + 10)
        self.sesiones.anotar("s1", ruta)
        self.sesiones.anotar_el_turno("s1")
        with io.open(self.sesiones.ruta_de("s1"), encoding="utf-8") as f:
            self.assertEqual(1, f.read().split().count("doble.md"))

    def test_sin_sesion_no_hace_nada(self):
        self.assertEqual([], self.sesiones.anotar_el_turno(""))
        self.assertFalse(os.path.isdir(os.path.join(self.raiz, TOCADO)))

    def test_validar_sin_nada_preparado_no_avisa(self):
        self.assertEqual([], SesionesMezcladas(self.raiz).validar())


class SinRepositorio(Carpeta):

    def test_sin_git_no_revienta_y_no_anota(self):
        self.assertEqual([], Sesiones(self.raiz).cambios_del_turno(0))


# ── inmutable ─────────────────────────────────────────────────────────────

class ElHistoricoSoloCrece(Carpeta):
    """Se agrega, no se reescribe."""

    def test_agregar_al_final_es_crecer(self):
        self.assertTrue(HistoricoInmutable.solo_crecio("a\nb\n", "a\nb\nc\n"))
        self.assertTrue(HistoricoInmutable.solo_crecio("a\nb\n", "a\nb\n"))

    def test_editar_el_pasado_no_es_crecer(self):
        self.assertFalse(HistoricoInmutable.solo_crecio("a\nb\n", "a\nX\nc\n"))

    def test_los_finales_de_linea_de_windows_no_confunden(self):
        self.assertTrue(HistoricoInmutable.solo_crecio("a\nb\n", "a\r\nb\r\nc\r\n"))

    def test_la_transcripcion_reescrita_avisa_y_la_que_crece_no(self):
        """Nueva: las viejas solo probaban la comparación, nunca el recorrido por git."""
        repo_vacio(self.raiz)
        self.escribir("historico-chat/2026-01-02-sesion.md", "a\nb\n")
        self.escribir("historico-chat/2026-01-03-otra.md", "a\nb\n")
        git(self.raiz, "add", "-A")
        git(self.raiz, "commit", "-qm", "base")
        self.escribir("historico-chat/2026-01-02-sesion.md", "a\nX\n")
        self.escribir("historico-chat/2026-01-03-otra.md", "a\nb\nc\n")
        h = HistoricoInmutable(self.raiz).validar()
        self.assertEqual([AVISO], [x.severidad for x in h])
        self.assertIn("2026-01-02-sesion.md", h[0].archivo)


# ── índices ───────────────────────────────────────────────────────────────

INDICE = "# Notas\n\n- [notas/vieja.md](vieja.md) — la que ya estaba, con su descripción cuidada.\n"


class ElIndiceSeCompletaSolo(Carpeta):
    """`13·DOC17` · La línea que falta se escribe; la que ya estaba no se toca."""

    def carpeta(self, *archivos):
        self.escribir("notas/README.md", INDICE)
        for nombre, contenido in archivos:
            self.escribir("notas/" + nombre, contenido)
        return CompletadorDeIndices(self.raiz)

    def completar(self, escribir=True):
        CompletadorDeIndices(self.raiz).completar(carpetas=["notas"], escribir=escribir)
        return self.leer("notas/README.md")

    def test_ve_el_archivo_sin_su_linea(self):
        c = self.carpeta(("vieja.md", "# Vieja\n"), ("nueva.md", "# La nueva\n"))
        self.assertEqual(["nueva.md"], c.faltantes(os.path.join(self.raiz, "notas")))

    def test_sin_aplicar_no_toca_el_archivo(self):
        self.carpeta(("vieja.md", "# Vieja\n"), ("nueva.md", "# La nueva\n"))
        self.assertNotIn("nueva.md", self.completar(escribir=False))

    def test_con_aplicar_escribe_la_linea_con_el_titulo_y_la_ruta(self):
        self.carpeta(("vieja.md", "# Vieja\n"), ("nueva.md", "# La nueva\n"),
                     ("x.md", "# Cómo se guarda la historia de un valor\n"))
        texto = self.completar()
        self.assertIn("La nueva", texto)
        self.assertIn("[notas/nueva.md](nueva.md)", texto)
        self.assertIn("Cómo se guarda la historia", texto)

    def test_la_descripcion_cuidada_sobrevive(self):
        self.carpeta(("vieja.md", "# Vieja\n"), ("nueva.md", "# La nueva\n"))
        self.assertIn("con su descripción cuidada", self.completar())

    def test_correrlo_dos_veces_no_duplica(self):
        self.carpeta(("vieja.md", "# Vieja\n"), ("nueva.md", "# La nueva\n"))
        self.completar()
        self.assertEqual(1, self.completar().count("nueva.md]"))

    def test_no_borra_la_linea_de_un_archivo_que_ya_no_esta(self):
        self.carpeta()
        self.assertIn("vieja.md", self.completar())

    def test_avisa_de_la_linea_sin_afinar(self):
        self.carpeta(("vieja.md", "# Vieja\n"), ("nueva.md", "# La nueva\n"))
        self.completar()
        self.assertEqual(1, len(IndicesPorAfinar(self.raiz, carpetas=["notas"]).validar()))

    def test_el_estandar_no_tiene_ninguna_sin_afinar(self):
        self.assertEqual([], IndicesPorAfinar(RAIZ).validar())

    def test_sin_indice_no_revienta(self):
        self.assertEqual([], CompletadorDeIndices(self.raiz).completar(carpetas=["notas"]))
        self.assertEqual([], IndicesPorAfinar(self.raiz, carpetas=["notas"]).validar())


# ── conteo ────────────────────────────────────────────────────────────────

class ElConteoPorRegla(Carpeta):
    """`EP-004·HU-009` · El registro guarda la regla y cuántas veces; nunca lo revisado."""

    def setUp(self):
        super().setUp()
        self.escribir("VERSION", "31.10.0\n")
        self.conteo = ConteoPorRegla(self.raiz)

    def test_el_registro_no_contiene_el_texto_del_hallazgo(self):
        secreto = "AKIA1234567890ABCDEF"
        self.conteo.anotar([Hallazgo(FALLA, "config.py", 9, "posible secreto en el código (%s) · 04·S4" % secreto)],
                           cuando="2026-08-22 10:00:00")
        guardado = self.leer("metricas/conteo-por-regla.jsonl")
        self.assertNotIn(secreto, guardado)
        self.assertNotIn("config.py", guardado, "tampoco la ruta revisada")
        self.assertIn("04·S4", guardado)
        self.assertIn("31.10.0", guardado, "sin la versión no se puede comparar")

    def test_una_linea_por_corrida(self):
        for i in range(3):
            self.conteo.anotar([Hallazgo(AVISO, "a.md", 0, "de `20·M5`")], cuando="2026-08-22 1%d:00:00" % i)
        self.assertEqual(3, len(self.leer("metricas/conteo-por-regla.jsonl").strip().splitlines()))
        self.assertEqual(3, len(self.conteo.corridas()))

    def test_el_total_se_cuenta_aunque_lleguen_de_un_generador(self):
        """Nueva: el viejo contaba el total después de recorrer los hallazgos, y
        con un generador anotaba 0."""
        fila = self.conteo.anotar(Hallazgo(AVISO, "a.md", 0, "de `20·M5`") for _ in range(2))
        self.assertEqual(2, fila["total"])

    def test_dos_corridas_con_un_arreglo_en_medio_muestran_la_baja(self):
        self.conteo.anotar([Hallazgo(FALLA, "a.md", 0, "de `20·M5`"), Hallazgo(FALLA, "b.md", 0, "de `20·M5`"),
                            Hallazgo(FALLA, "c.md", 0, "de `09·G2`")], cuando="2026-08-22 10:00:00")
        self.conteo.anotar([Hallazgo(FALLA, "c.md", 0, "de `09·G2`")], cuando="2026-08-22 11:00:00")
        cambios = {r: (a, b) for r, a, b in self.conteo.comparar()}
        self.assertEqual((2, 0), cambios["20·M5"])
        self.assertNotIn("09·G2", cambios, "lo que no cambió no se reporta")
        self.assertIn("baja", "\n".join(self.conteo.lineas([Hallazgo(FALLA, "c.md", 0, "de `09·G2`")])))

    def test_con_una_sola_corrida_no_hay_con_que_comparar(self):
        self.conteo.anotar([Hallazgo(FALLA, "a.md", 0, "de `20·M5`")], cuando="2026-08-22 10:00:00")
        self.assertEqual([], self.conteo.comparar())

    def test_una_linea_rota_no_se_lleva_el_registro(self):
        self.conteo.anotar([Hallazgo(AVISO, "a.md", 0, "de `20·M5`")], cuando="2026-08-22 10:00:00")
        with io.open(self.conteo.registro, "a", encoding="utf-8", newline="\n") as f:
            f.write("esto no es json\n")
        self.assertEqual(1, len(self.conteo.corridas()))

    def test_lo_que_se_imprime_ordena_por_cuantos(self):
        texto = "\n".join(self.conteo.lineas([Hallazgo(FALLA, "a.md", 0, "de `20·M5`"),
                                              Hallazgo(FALLA, "b.md", 0, "de `20·M5`"),
                                              Hallazgo(FALLA, "c.md", 0, "de `09·G2`")]))
        self.assertIn("3 en total", texto)
        self.assertLess(texto.index("20·M5"), texto.index("09·G2"), "la regla con más hallazgos va primero")

    def test_sin_hallazgos_lo_dice(self):
        self.assertEqual(["Ningún hallazgo que contar."], self.conteo.lineas([]))
