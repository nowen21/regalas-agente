"""Las pruebas del grupo «freno»: el freno, lo hecho contra el plan, los acuerdos,
lo autorizado, el origen de cada punto, el análisis en curso, el resumen de la
sesión, el aviso de vuelta, los análisis aprobados, el plan de cada fase, las
reglas que pide el mensaje, el andamio y el cierre de un pendiente.

Son las pruebas de `validadores/pruebas.py` y `validadores/tests/*.py` que
cubrían estos módulos, pasadas a sus clases. Las que corrían un enganche de
`adaptadores/` como proceso aparte prueban acá la decisión del módulo, que es lo
que el enganche entrega; lo que el enganche agrega por su cuenta queda en su suite.
"""
import contextlib
import datetime
import io
import os
import re
import shutil
import sqlite3
import subprocess
import tempfile
import unittest
from unittest import mock

from ..comun import AVISO, FALLA, Archivos, Proyecto
from ..herramientas.andamio import MARCADOR_RAIZ, PLANTILLA_HU, Andamio
from ..herramientas.andamio import CARPETA as CARPETA_EPICAS
from ..herramientas.andamio import DOCUMENTOS as DOCUMENTOS_DE_FASE
from ..herramientas.andamio import main as andamio_main
from ..herramientas.cerrar import CerradorDePendientes
from ..herramientas.instalar import HOOKS_CLAUDE, PLANTILLA_PRE_COMMIT, Instalador
from ..herramientas.mapa_tareas import MapaDeTareas
from ..herramientas.recuperar import TOPE as TOPE_REGLAS
from ..herramientas.recuperar import RecuperadorDeReglas
from ..validadores.analisis import AnalisisAprobados
from ..validadores.enlaces import Enlaces, EnlacesRotos
from ..validadores.fases import EstructuraDeFases
from ..validadores.flujo import PlanDeLaFase
from ..validadores.marcas import Marcas
from ..validadores.pendientes import NumeracionDePendientes, Pendientes
from ..validadores.version import VersionDelEstandar
from .acuerdos import ENCABEZADO as ENCABEZADO_ACUERDOS
from .acuerdos import Acuerdos
from .analisis_en_curso import ESTADO, PLANTILLA, AnalisisEnCurso
from .autorizado import HERRAMIENTAS, Autorizaciones
from .aviso_resuelto import AVISO as ARCHIVO_AVISO
from .aviso_resuelto import PRUEBA, AvisoResuelto
from .freno import Freno
from .historico import Historico
from .niveles import BaseSinRespuesta, NivelesDelProyecto
from .origen import LectorDeAnalisis, OrigenDeCadaPunto
from .plan_vs_hecho import DE_LA_FASE, PlanContraLoHecho, PlanDeTrabajo
from .resumen import CARPETA as HISTORICO
from .resumen import MARCA_VACIO, MODELO, RESUMENES, Resumen

RAIZ = Proyecto.estandar()


class NivelesFijos:
    """`EP-025·HU-005` · El lector de niveles sustituido: las pruebas del freno no
    dependen de MariaDB. Sin niveles, todo frena, como antes de la HU-005."""

    def __init__(self, niveles=None, apagada=False):
        self.niveles, self.apagada = dict(niveles or {}), apagada

    def todos(self):
        if self.apagada:
            raise BaseSinRespuesta("MariaDB no responde en 127.0.0.1:3399: hay que prenderla")
        return dict(self.niveles)


_SIN_BASE_DE_VERDAD = mock.patch("core.enganches.freno.NivelesDelProyecto",
                                 lambda raiz: NivelesFijos())


def setUpModule():
    _SIN_BASE_DE_VERDAD.start()


def tearDownModule():
    _SIN_BASE_DE_VERDAD.stop()


def escribir(ruta, texto="x\n"):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    return ruta


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def git(repo, *args):
    subprocess.run(["git", "-C", repo, *args], check=True, capture_output=True)


def repo_con_autor(repo):
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "prueba@ejemplo.invalid")
    git(repo, "config", "user.name", "Prueba")


class Temporal(unittest.TestCase):
    """Un proyecto de mentira en una carpeta temporal."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.raiz = os.path.realpath(tmp.name)

    def ruta(self, relativa):
        return os.path.join(self.raiz, *relativa.split("/"))

    def escribir(self, relativa, texto="x\n"):
        return escribir(self.ruta(relativa), texto)

    def leer(self, relativa):
        return leer(self.ruta(relativa))


# ══ el freno (`EP-023 · HU-007 · fase B`) ═════════════════════════════════

HU_FRENO = "documentacion/epicas/EP-009-algo/HU-001-una-cosa"
FASE_FRENO = HU_FRENO + "/B-EP-009-HU-001-la-fase"
PENDIENTE_FRENO = "documentacion/epicas/EP-009-algo/pendientes/110-algo"


def plan_del_freno(aprobado=True):
    aprobacion = ("**Aprobación** (`02·F4`): Ana Pérez, el 2026-10-03, con la versión 51.0.0.\n\n"
                  if aprobado else "**Aprobación** (`02·F4`): pendiente.\n\n")
    return ("# Plan\n\n%s### 2.1 Archivos que se crean o modifican\n\n> Rutas exactas.\n\n"
            "| Archivo (ruta real verificada) | Tipo | Capa | Nota |\n|---|---|---|---|\n"
            "| `src/a.py` | Modificar | Programa | |\n\n### 2.2 Otra\n" % aprobacion)


class ProyectoConGit(Temporal):

    def setUp(self):
        super().setUp()
        git(self.raiz, "init", "-q")
        self.freno = Freno(self.raiz)

    def con_fase(self, aprobado=True):
        self.escribir(FASE_FRENO + "/plan_trabajo.md", plan_del_freno(aprobado))

    def escritura(self, relativa):
        return self.freno.revisar("Write", {"file_path": self.ruta(relativa)})[0]

    def orden(self, orden, **extra):
        return self.freno.revisar("Bash", dict(command=orden, **extra), cwd=self.raiz)[0]

    def prender_de_una(self, fila):
        self.escribir(PENDIENTE_FRENO + "/analisis-2.md",
                      "# Análisis 2\n\n## Lo que se tiene que hacer\n\n"
                      "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
                      + fila + "\n\n## Otra\n")
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE_FRENO)


class LaHerramientaDeEscritura(ProyectoConGit):
    """CP-001: la herramienta de escritura, contra la fase en curso y lo autorizado."""

    def test_sin_aprobar_el_plan_solo_los_documentos_de_la_fase(self):
        self.con_fase(aprobado=False)
        self.assertEqual("deja", self.escritura(FASE_FRENO + "/plan_pruebas.md"))
        self.assertEqual("detiene", self.escritura("src/a.py"))

    def test_con_el_plan_aprobado_lo_que_declara(self):
        self.con_fase()
        self.assertEqual("deja", self.escritura("src/a.py"))
        self.assertEqual("detiene", self.escritura("src/b.py"))

    def test_sin_fase_en_curso_solo_lo_autorizado(self):
        self.assertEqual("deja", self.escritura("historico-chat/resumenes/2026-10-03/tema.md"))
        self.assertEqual("deja", self.escritura(HU_FRENO + "/HU-001-una-cosa.md"))
        self.assertEqual("detiene", self.escritura("src/a.py"))

    def test_lo_que_el_analisis_prendido_manda_hacer_de_una(self):
        self.prender_de_una("| 1 | Corregir `src/c.py` | 1 | Este análisis, de una y sin fase |")
        self.assertEqual("deja", self.escritura("src/c.py"))
        self.assertEqual("detiene", self.escritura("src/d.py"))

    def test_la_ruta_de_una_tambien_se_lee_en_paso_a(self):
        self.prender_de_una("| 1 | Corregir la plantilla | 1 | Este análisis, de una y sin fase: `src/e.py` |")
        self.assertEqual("deja", self.escritura("src/e.py"))
        self.assertEqual("detiene", self.escritura("src/d.py"))

    def test_fuera_del_proyecto_tambien_con_rutas_que_enganan(self):
        self.assertEqual("detiene", self.escritura("../fuera.txt"))
        self.assertEqual("detiene", self.escritura("src/../../fuera.txt"))

    def test_la_carpeta_hermana_con_el_mismo_comienzo_es_afuera(self):
        """`EP-005·HU-023·CA-09`: `.../proyecto` es prefijo de `.../proyecto-otro` y no lo contiene."""
        decision, motivo, _ = self.freno.revisar("Edit", {"file_path": os.path.join(self.raiz + "-otro", "a.py")})
        self.assertEqual("detiene", decision)
        self.assertIn("fuera del proyecto", motivo)

    def test_escribir_fuera_del_proyecto_se_detiene(self):
        decision, motivo, _ = self.freno.revisar("Write", {"file_path": os.path.join(tempfile.gettempdir(), "guion.py")})
        self.assertEqual("detiene", decision)
        self.assertIn("fuera del proyecto", motivo)

    def test_el_instalador_lo_pone_sobre_toda_accion(self):
        antes = [h for h in HOOKS_CLAUDE if h[2] == "hook_antes.py"]
        self.assertEqual([("PreToolUse", None, "--modo accion")], [(h[0], h[1], h[4]) for h in antes])


class ElAnalisisAprobadoApruebaSusPlanes(ProyectoConGit):
    """`EP-023 · HU-008 · CP-002`: la aprobación que cita un análisis vale si el
    análisis está aprobado y nombra la HU del plan."""

    ANALISIS = "documentacion/epicas/EP-009-algo/pendientes/120-algo/analisis-1.md"

    def analisis(self, aprobado=True, hu="`EP-009` HU-001"):
        self.escribir(self.ANALISIS, "# Análisis 1\n\n%s## Lo que se tiene que hacer\n\n"
                      "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
                      "| 1 | Hacer la cosa | 1 | %s |\n\n## Otra\n"
                      % ("> **Aprobado** por el usuario el 2026-10-04, en el turno 3.\n\n" if aprobado else "", hu))

    def plan_citando_el_analisis(self):
        enlace = os.path.relpath(self.ruta(self.ANALISIS), self.ruta(FASE_FRENO)).replace("\\", "/")
        texto = plan_del_freno().replace("Ana Pérez", "[análisis 1 del pendiente 120](%s)" % enlace)
        self.escribir(FASE_FRENO + "/plan_trabajo.md", texto)
        return self.ruta(FASE_FRENO + "/plan_trabajo.md"), texto

    def test_el_analisis_aprobado_que_nombra_la_hu_aprueba_el_plan(self):
        self.analisis()
        ruta, texto = self.plan_citando_el_analisis()
        self.assertTrue(PlanDeTrabajo.aprobado(ruta, texto))
        self.assertEqual("deja", self.escritura("src/a.py"))
        self.assertEqual("detiene", self.escritura("src/b.py"))

    def test_el_analisis_sin_aprobar_no_aprueba(self):
        self.analisis(aprobado=False)
        ruta, texto = self.plan_citando_el_analisis()
        self.assertFalse(PlanDeTrabajo.aprobado(ruta, texto))
        self.assertEqual("detiene", self.escritura("src/a.py"))

    def test_el_analisis_que_no_nombra_la_hu_no_aprueba(self):
        self.analisis(hu="`EP-009` HU-002")
        ruta, texto = self.plan_citando_el_analisis()
        self.assertFalse(PlanDeTrabajo.aprobado(ruta, texto))

    def test_la_aprobacion_de_una_persona_sigue_valiendo(self):
        self.con_fase()
        ruta = self.ruta(FASE_FRENO + "/plan_trabajo.md")
        self.assertTrue(PlanDeTrabajo.aprobado(ruta, self.leer(FASE_FRENO + "/plan_trabajo.md")))


class LaConsola(ProyectoConGit):
    """CP-002."""

    def setUp(self):
        super().setUp()
        self.con_fase()

    def test_lo_que_escribe_fuera_del_plan_se_detiene(self):
        self.assertEqual("detiene", self.orden("echo hola > notas.txt"))
        self.assertEqual("detiene", self.orden("rm src/b.py"))
        self.assertEqual("detiene", self.orden("cp src/a.py src/b.py"))

    def test_lo_que_nunca_se_deja(self):
        self.assertEqual("detiene", self.orden("python -m unittest", run_in_background=True))
        self.assertEqual("detiene", self.orden("pip install requests"))
        self.assertEqual("detiene", self.orden("git config --global user.name x"))
        self.assertEqual("detiene", self.orden("python servidor.py &"))

    def test_lo_que_solo_lee_pasa(self):
        self.assertEqual("deja", self.orden("git status"))
        self.assertEqual("deja", self.orden("python -m unittest 2>&1 | tail -3"))
        self.assertEqual("deja", self.orden("echo x > src/a.py"))


class LoQueSePublica(ProyectoConGit):
    """CP-003."""

    def test_se_pregunta(self):
        self.assertEqual("pregunta", self.freno.revisar("mcp__docs__update", {})[0])
        self.assertEqual("deja", self.freno.revisar("Read", {})[0])


class DespuesDeActuar(ProyectoConGit):
    """CP-004: después de una orden, lo que cambió en git."""

    def test_ve_lo_que_un_programa_escribio_por_dentro(self):
        self.con_fase()
        self.escribir("viejo.txt")                 # ya estaba cambiado antes de la orden
        self.freno.tomar_foto()
        self.escribir("src/a.py")                  # declarado
        self.escribir("src/b.py")                  # no declarado
        self.assertEqual(["src/b.py"], [r for r, _ in self.freno.despues()])


class ElNivelDeLaRegla(ProyectoConGit):
    """`EP-025·HU-005 · CP-001 y CP-002`: el freno aplica el nivel de la regla."""

    def con(self, niveles):
        self.freno = Freno(self.raiz, niveles=NivelesFijos(niveles))

    def test_sin_fila_frena(self):
        self.con({})
        decision, motivo, _ = self.freno.revisar("Write", {"file_path": self.ruta("src/a.py")})
        self.assertEqual("detiene", decision)
        self.assertIn("02·F8", motivo)

    def test_avisa_deja_pasar_con_el_motivo(self):
        self.con({"02·F8": "avisa"})
        decision, motivo, ruta = self.freno.revisar("Write", {"file_path": self.ruta("src/a.py")})
        self.assertEqual(("avisa", "src/a.py"), (decision, ruta))
        self.assertIn("02·F8", motivo)
        self.assertIn("La regla está en «avisa»", Freno.aviso_de_nivel(motivo, ruta))

    def test_apagada_deja_pasar_sin_decir_nada(self):
        self.con({"02·F8": "apagada"})
        self.assertEqual(("deja", "", ""), self.freno.revisar("Write", {"file_path": self.ruta("src/a.py")}))

    def test_el_nivel_de_otra_regla_no_cambia_nada(self):
        self.con({"04·S9": "apagada"})
        self.assertEqual("detiene", self.escritura("src/a.py"))

    def test_fuera_del_proyecto_con_su_regla_en_avisa(self):
        self.con({"04·S9": "avisa"})
        decision, motivo, _ = self.freno.revisar("Write", {"file_path": os.path.join(tempfile.gettempdir(), "g.py")})
        self.assertEqual("avisa", decision)
        self.assertIn("04·S9", motivo)

    def test_por_consola_tambien(self):
        self.con({"02·F8": "avisa"})
        self.assertEqual("avisa", self.orden("echo hola > notas.txt"))

    def test_despues_de_una_orden(self):
        self.con_fase()
        self.freno.tomar_foto()
        self.escribir("src/b.py")
        self.con({"02·F8": "avisa"})
        self.assertEqual(([], ["src/b.py"]), tuple([r for r, _ in lista] for lista in self.freno.despues_por_nivel()))
        self.con({"02·F8": "apagada"})
        self.assertEqual(([], []), self.freno.despues_por_nivel())
        self.con({})
        self.assertEqual(["src/b.py"], [r for r, _ in self.freno.despues()])

    def test_el_nucleo_siempre_frena(self):
        self.con({"00·N1": "apagada"})
        self.assertEqual("pregunta", self.freno.revisar("mcp__docs__update", {})[0])
        self.assertEqual("frena", Freno.nivel_para("00·N1", {"00·N1": "apagada"}))
        self.assertEqual(("detiene", "algo (00·N1)", "x"),
                         self.freno.con_nivel(("detiene", "algo (00·N1)", "x"), True))

    def test_la_regla_sale_del_motivo(self):
        self.assertEqual("02·F8", Freno.regla_de("el plan no lo declara (02·F8)"))
        self.assertEqual("04·S10", Freno.regla_de("deja un proceso corriendo (04·S10)"))
        self.assertIsNone(Freno.regla_de("sin regla"))


class SinBaseNoSeModifica(ProyectoConGit):
    """`EP-025·HU-005 · CP-003`: sin base, lo que modifica se detiene y leer pasa."""

    def setUp(self):
        super().setUp()
        self.con_fase()
        self.freno = Freno(self.raiz, niveles=NivelesFijos(apagada=True))

    def test_escribir_lo_declarado_se_detiene(self):
        decision, motivo, _ = self.freno.revisar("Write", {"file_path": self.ruta("src/a.py")})
        self.assertEqual("sin_base", decision)
        self.assertIn("hay que prenderla", motivo)
        self.assertIn("leer sigue permitido", Freno.aviso_sin_base(motivo))

    def test_una_orden_que_escribe_se_detiene(self):
        self.assertEqual("sin_base", self.orden("echo x > src/a.py"))

    def test_leer_pasa(self):
        self.assertEqual("deja", self.orden("git status"))
        self.assertEqual("deja", self.freno.revisar("Read", {"file_path": self.ruta("src/a.py")})[0])

    def test_despues_de_una_orden_avisa_una_vez(self):
        self.freno.tomar_foto()
        self.escribir("src/b.py")
        self.escribir("src/c.py")
        frenan, avisan = self.freno.despues_por_nivel()
        self.assertEqual(([""], []), ([r for r, _ in frenan], avisan))
        self.assertIn("hay que prenderla", frenan[0][1])

    def test_el_lector_real_con_un_puerto_sin_servidor(self):
        ajustes = {"NAME": "cimiento", "USER": "root", "PASSWORD": "", "HOST": "127.0.0.1", "PORT": "3399"}
        with self.assertRaises(BaseSinRespuesta) as error:
            NivelesDelProyecto(self.raiz, ajustes=ajustes).todos()
        self.assertIn("127.0.0.1:3399", str(error.exception))


class ElHallazgoQuedaAnotado(ProyectoConGit):
    """CP-005: el hallazgo queda anotado en el resumen de la sesión."""

    def setUp(self):
        super().setUp()
        self.escribir("historico-chat/2026-10-03-tema.md", "# Sesión\n\n<!-- sesion: abc -->\n")
        self.escribir("historico-chat/resumenes/2026-10-03/tema.md",
                      "# Resumen\n\n## Hallazgos\n\n---\n\n## ¿Se puede cerrar la sesión?\n\nNo.\n")

    def test_el_resumen_suma_el_hallazgo_una_sola_vez(self):
        for _ in range(2):
            self.freno.anotar_hallazgo("abc", "una escritura", "src/b.py", "no está en el plan")
        texto = self.leer("historico-chat/resumenes/2026-10-03/tema.md")
        self.assertEqual(1, texto.count("El freno detuvo"))
        self.assertIn("vuelve al análisis", texto)
        self.assertLess(texto.index("### H-1 "), texto.index("## ¿Se puede cerrar"))

    def test_al_detener_dice_que_se_vuelve_al_analisis(self):
        """El enganche entrega lo que el freno decide: se prueba la decisión y su aviso."""
        decision, porque, ruta = self.freno.revisar("Write", {"file_path": self.ruta("src/b.py")}, self.raiz)
        self.assertEqual("detiene", decision)
        anotado = self.freno.anotar_hallazgo("abc", "una escritura", ruta, porque)
        texto = Freno.aviso(porque, ruta, bool(anotado), self.freno.analisis_prendido())
        self.assertIn("vuelve al análisis", texto)
        self.assertIn("Quedó anotado", texto)

    def prender(self, aprobado=False):
        marca = "> **Aprobado** por el usuario el 2026-10-03.\n\n" if aprobado else ""
        self.escribir(PENDIENTE_FRENO + "/analisis-2.md", "# Análisis 2\n\n" + marca)
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE_FRENO)

    def test_cp_c001_con_un_analisis_prendido_no_se_anota(self):
        self.prender()
        self.assertEqual("", self.freno.anotar_hallazgo("abc", "una escritura", "src/b.py", "no está"))
        self.assertNotIn("El freno detuvo", self.leer("historico-chat/resumenes/2026-10-03/tema.md"))
        self.assertIn("reportarlo en la conversación", Freno.aviso("no está", "src/b.py", False, True))

    def test_cp_c001_con_el_analisis_ya_aprobado_si_se_anota(self):
        self.prender(aprobado=True)
        self.assertTrue(self.freno.anotar_hallazgo("abc", "una escritura", "src/b.py", "no está"))

    def test_cp_c001_la_regla_lo_dice(self):
        regla = os.path.join(RAIZ, "base", "13-documentacion", "reglas",
                             "DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md")
        self.assertIn("análisis prendido", leer(regla))


class ElMayorQueEntreComillas(ProyectoConGit):
    """CP-002 de la fase C."""

    def test_entre_comillas_no_es_escritura(self):
        self.con_fase()
        self.assertEqual("deja", self.orden('grep -n "> acá termina" analisis.md'))
        self.assertEqual("deja", self.orden("grep -n '> acá termina' analisis.md"))
        self.assertEqual("deja", self.orden('Select-String -Pattern "^## |^> acá" -Path a.md'))

    def test_la_redireccion_real_sigue_detenida(self):
        self.con_fase()
        self.assertEqual("detiene", self.orden('grep "x" a.md > notas.txt'))
        self.assertEqual("detiene", self.orden('echo "a > b" > "otra nota.txt"'))


class LosDestinosDeUnaOrden(unittest.TestCase):
    """Análisis 14, 15 y 16 del pendiente 103: `sed`, los heredocs y las comparaciones."""

    def test_lo_que_va_tras_e_es_la_orden(self):
        self.assertEqual(["a.md"], Freno.destinos("sed -i -e 's/x/y/' -e 's/actual:/z/' a.md"))
        self.assertEqual(["a.md", "b.md"], Freno.destinos("sed -i --expression='s/x/y/' a.md b.md"))

    def test_sin_e_la_primera_palabra_es_la_orden(self):
        self.assertEqual(["a.md"], Freno.destinos("sed -i 's/x/y/' a.md"))

    def test_sin_i_no_escribe(self):
        self.assertEqual([], Freno.destinos("sed -n '1,5p' a.md"))

    def test_el_texto_del_heredoc_no_cuenta(self):
        self.assertEqual([], Freno.destinos("python - <<'EOF'\nif a > b: print(1)\nx >> y\nEOF"))

    def test_la_redireccion_de_la_linea_que_lo_abre_si(self):
        self.assertEqual(["nota.txt"], Freno.destinos("cat > nota.txt <<EOF\nhola > mundo\nEOF"))

    def test_mayor_o_igual_y_flecha_no_escriben(self):
        self.assertEqual([], Freno.destinos("python - <<EOF\nif n >= 11: pass\nEOF"))
        self.assertEqual([], Freno.destinos("awk '$1 => 2' a.txt"))

    def test_la_redireccion_sigue_viendose(self):
        self.assertEqual(["notas.txt"], Freno.destinos("echo x > notas.txt"))
        self.assertEqual(["notas.txt"], Freno.destinos("echo x >> notas.txt"))

    def test_el_dispositivo_nulo_dentro_de_una_sustitucion_no_es_un_archivo(self):
        self.assertEqual([], Freno.destinos('x=$(python a.py 2>&1 >/dev/null)'))

    @unittest.skipUnless(os.name == "nt", "solo en Windows")
    def test_la_ruta_con_barra_y_letra_es_la_unidad(self):
        """En Windows, `/c/...` es `C:\\...` (corregido con «Corrija», 2026-10-04)."""
        self.assertEqual(os.path.realpath("C:/Windows/x"), Proyecto.ruta_real("/c/Windows/x", "D:/"))


class CorrijaArreglaLasHerramientas(ProyectoConGit):
    """Análisis 16 del pendiente 103, acuerdo 2."""

    def test_con_corrija_se_corrigen_las_herramientas_y_nada_mas(self):
        curso = AnalisisEnCurso(self.raiz)
        self.assertEqual("detiene", self.escritura("validadores/freno.py"))
        curso.marcar_corrija(7)
        self.assertEqual("deja", self.escritura("validadores/freno.py"))
        self.assertEqual("deja", self.escritura("adaptadores/claude-code/hook_antes.py"))
        self.assertEqual("detiene", self.escritura("base/02-flujo-de-trabajo/reglas/F8.md"))
        curso.borrar_corrija()
        self.assertEqual("detiene", self.escritura("validadores/freno.py"))


class ElFrenoDejaLosArchivosConPunto(unittest.TestCase):
    """`rutas_de_una` le quitaba a cada ruta todos los `.` y `/` del comienzo, y
    `.gitignore` quedaba como `gitignore` (sesión del 2026-10-04, «Corrija»)."""

    def rutas(self, celda):
        with tempfile.TemporaryDirectory() as tmp:
            ruta = escribir(os.path.join(tmp, "analisis-1.md"),
                            "## Lo que se tiene que hacer\n\n| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
                            "| 1 | algo | 1 | %s |\n" % celda)
            return Freno.rutas_de_una(ruta)

    def test_el_punto_del_nombre_se_conserva(self):
        rutas = self.rutas("Este análisis, de una y sin fase: `.gitignore`, `proyectos/x/.env`")
        self.assertEqual(rutas, {".gitignore", "proyectos/x/.env"})

    def test_el_punto_barra_del_comienzo_se_quita(self):
        self.assertEqual(self.rutas("de una: `./validadores/comun.py`"), {"validadores/comun.py"})


class ElFrenoNoFrenaElRegistroDeGit(unittest.TestCase):
    """Análisis 1 del pendiente 116, fila 15: el renombrado se leía mal y `git add`
    se revisaba como si escribiera contenido."""

    def test_la_ruta_vieja_no_aparece_como_archivo(self):
        with tempfile.TemporaryDirectory() as repo:
            repo_con_autor(repo)
            escribir(os.path.join(repo, "plataforma", "a.py"), "x = 1\n" * 20)
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "inicio")
            os.makedirs(os.path.join(repo, "nueva"))
            os.replace(os.path.join(repo, "plataforma", "a.py"), os.path.join(repo, "nueva", "a.py"))
            git(repo, "add", "-A")
            self.assertEqual(sorted(Freno(repo).cambiados()), ["nueva/a.py"])

    def test_las_ordenes_que_solo_registran(self):
        for orden in ("git add -A", "git commit -m 'x; y'", 'git -C "C:/a b" commit -F m.txt',
                      "cd /c/repo && git add . && git commit -m x && git push",
                      "git commit -F - <<'EOF'\nmensaje; con punto y coma\nEOF"):
            self.assertTrue(Freno.solo_registra(orden), orden)

    def test_las_que_escriben_si_se_revisan(self):
        for orden in ("git add -A && rm -rf x", "git checkout -- a.py", "python guion.py", "", "git rm x"):
            self.assertFalse(Freno.solo_registra(orden), orden)

    def test_despues_de_registrar_no_hay_hallazgos(self):
        self.assertEqual(Freno(tempfile.gettempdir()).despues("git commit -m x"), [])


class LoQueEscribenLasHerramientas(Temporal):
    """Análisis 1 del pendiente 110: lo que un proyecto reporta se corrige para todos."""

    def test_lo_que_escriben_el_instalador_y_el_andamio_esta_autorizado(self):
        autorizadas = [HERRAMIENTAS]
        self.assertTrue(Autorizaciones.quien_autoriza("documentacion/versiones/2026-10-04-53.2.0.md", autorizadas))
        self.assertTrue(Autorizaciones.quien_autoriza("documentacion/epicas/EP-001-x/HU-001-y/README.md", autorizadas))
        self.assertIsNone(Autorizaciones.quien_autoriza("src/app.py", autorizadas))

    def test_la_carpeta_de_un_archivo_declarado_se_puede_crear(self):
        permitido = {"fases": [("documentacion/epicas/EP-1/HU-1/A", True, {"templates/registration/login.html"})],
                     "reglas": [], "de_una": set(), "corrija": False}
        freno = Freno(self.raiz)
        self.assertIsNone(freno.motivo(os.path.join(self.raiz, "templates", "registration"), permitido))
        self.assertIsNotNone(freno.motivo(os.path.join(self.raiz, "templates", "otra"), permitido))

    def test_instalar_en_el_entorno_del_proyecto_se_deja(self):
        """Pendiente 115; acuerdo 8: el entorno `venv/` está dentro del proyecto."""
        freno = Freno(self.raiz)
        app = os.path.join(self.raiz, "proyectos", "app")
        self.assertIsNone(freno.nunca("venv/Scripts/python.exe -m pip install paquete==1.0", False, app))
        self.assertIsNone(freno.nunca(".venv/bin/pip install paquete", False, self.raiz))

    def test_lo_que_nunca_se_deja_no_lee_el_texto_de_un_heredoc(self):
        self.assertIsNone(Freno(self.raiz).nunca("python - <<'EOF'\nprint('pip install x')\nEOF", False, self.raiz))

    def test_instalar_fuera_del_proyecto_sigue_detenido(self):
        freno = Freno(self.raiz)
        for orden in ("pip install paquete", "python -m pip install paquete",
                      "C:/Python311/python.exe -m pip install paquete",
                      "venv/Scripts/pip install a && npm install -g b"):
            self.assertIsNotNone(freno.nunca(orden, False, self.raiz), orden)


# ══ lo hecho contra el plan (`EP-004·HU-013`, `EP-023·HU-007`) ═══════════════

FASE_PLAN = "documentacion/epicas/EP-009-algo/HU-001-una-cosa/A-EP-009-HU-001-la-fase"


def plan_aprobado(version="48.0.0", aprobacion=None, filas=("`src/a.py`",)):
    aprobacion = aprobacion or "Ana Pérez, el 2026-10-02, con la versión " + version
    tabla = "\n".join("| %s | Modificar | Programa | |" % f for f in filas)
    return ("# Plan\n\n**Aprobación** (`02·F4`): %s.\n\n### 2.1 Archivos que se crean o modifican\n\n"
            "> Es la lista exacta.\n\n| Archivo (ruta real verificada) | Tipo | Capa | Nota |\n|---|---|---|---|\n%s\n\n"
            "### 2.2 Otra\n" % (aprobacion, tabla))


class ElPlanDiceQueTocaYQuienLoAprobo(unittest.TestCase):
    """`EP-023·HU-007·fase A` · CP-001."""

    def test_la_plantilla_pide_la_aprobacion_y_rutas_exactas(self):
        texto = leer(os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos", "07-plan-trabajo.md"))
        self.assertIn("| **Aprobación** (", texto)
        self.assertIn("con la versión «X.Y.Z»", texto)
        self.assertIn("rutas exactas entre comillas invertidas", texto)

    def test_la_fila_que_no_es_ruta_exacta_falla(self):
        filas = ("`src/`", "`src/*.py`", "Los validadores", "`src/a.py`", "`src/b.py`, `VERSION`")
        motivos = PlanDeTrabajo.revisar_aprobado(plan_aprobado(filas=filas))
        self.assertEqual(3, len(motivos))
        self.assertTrue(all("§2.1" in m for _, m in motivos))

    def test_la_aprobacion_sin_quien_o_sin_fecha_falla(self):
        for aprobacion in ("el 2026-10-02, con la versión 48.0.0", "Ana Pérez, con la versión 48.0.0"):
            motivos = PlanDeTrabajo.revisar_aprobado(plan_aprobado(aprobacion=aprobacion))
            self.assertEqual(1, len(motivos), aprobacion)
            self.assertIn("quién", motivos[0][1])

    def test_el_plan_aprobado_antes_no_se_revisa(self):
        self.assertEqual([], PlanDeTrabajo.revisar_aprobado(plan_aprobado(version="47.0.0", filas=("`src/`", "Todo"))))


class ElCommitSeComparaConElPlan(Temporal):
    """`EP-023·HU-007·fase A` · CP-002 y la última parte de CP-003."""

    def setUp(self):
        super().setUp()
        git(self.raiz, "init", "-q")
        self.escribir(FASE_PLAN + "/plan_trabajo.md", plan_aprobado())

    def preparar(self, *relativas):
        for r in relativas:
            if not os.path.exists(self.ruta(r)):
                self.escribir(r)
        git(self.raiz, "add", *relativas)

    def fallas(self):
        return [h.archivo for h in PlanContraLoHecho(self.raiz).comparar_preparados() if h.severidad == FALLA]

    def test_lo_declarado_pasa(self):
        self.preparar(FASE_PLAN + "/plan_trabajo.md", "src/a.py")
        self.assertEqual([], self.fallas())

    def test_lo_no_declarado_ni_autorizado_falla(self):
        self.preparar(FASE_PLAN + "/plan_trabajo.md", "src/a.py", "src/otro.py")
        self.assertEqual(["src/otro.py"], self.fallas())

    def test_los_documentos_de_la_fase_y_el_resumen_pasan(self):
        self.preparar(FASE_PLAN + "/plan_trabajo.md", FASE_PLAN + "/resultado_pruebas.md",
                      "historico-chat/resumenes/2026-10-02/sesion.md")
        self.assertEqual([], self.fallas())

    def test_sin_tocar_una_fase_no_compara(self):
        self.preparar("src/otro.py")
        self.assertEqual([], self.fallas())

    def test_con_el_plan_aprobado_antes_no_compara(self):
        self.escribir(FASE_PLAN + "/plan_trabajo.md", plan_aprobado(version="47.0.0"))
        self.preparar(FASE_PLAN + "/plan_trabajo.md", "src/otro.py")
        self.assertEqual([], self.fallas())

    def test_lo_que_autoriza_una_regla_del_proyecto_pasa(self):
        self.escribir(".agente/reglas-proyecto.md",
                      "# Reglas\n\n### P1 · Las notas\n\n- **Regla:** se escriben.\n- **Autoriza escribir:** `notas/*.md`\n")
        self.preparar(FASE_PLAN + "/plan_trabajo.md", "notas/hoy.md")
        self.assertEqual([], self.fallas())
        self.assertEqual("P1", Autorizaciones.quien_autoriza("notas/hoy.md", Autorizaciones().del_proyecto(self.raiz)))

    def analisis_de_una(self, marca=""):
        pendiente = "documentacion/epicas/EP-009-algo/pendientes/7-algo"
        self.escribir(pendiente + "/analisis-2.md",
                      "# Análisis 2\n\n%s## Lo que se tiene que hacer\n\n"
                      "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
                      "| 1 | Corregir | 1 | Este análisis, de una y sin fase: `src/otro.py` |\n\n## Otra\n" % marca)
        return pendiente

    def test_lo_que_el_analisis_prendido_manda_hacer_de_una_pasa(self):
        pendiente = self.analisis_de_una()
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % pendiente)
        self.preparar(FASE_PLAN + "/plan_trabajo.md", "src/otro.py", "src/tercero.py")
        self.assertEqual(["src/tercero.py"], self.fallas())

    def test_lo_que_un_analisis_aprobado_manda_hacer_entra_con_el(self):
        """Análisis 16 del pendiente 103, acuerdo 1."""
        pendiente = self.analisis_de_una("> **Aprobado** por el usuario el 2026-10-03.\n\n")
        self.preparar(FASE_PLAN + "/plan_trabajo.md", "src/otro.py", "src/tercero.py")
        self.assertEqual(["src/otro.py", "src/tercero.py"], sorted(self.fallas()))
        self.preparar(FASE_PLAN + "/plan_trabajo.md", "src/otro.py", "src/tercero.py", pendiente + "/analisis-2.md")
        self.assertEqual(["src/tercero.py"], self.fallas())

    def test_el_hash_anotado_solo_no_toca_la_fase(self):
        """Análisis 16 del pendiente 103, acuerdo 2."""
        git(self.raiz, "config", "user.email", "prueba@ejemplo.invalid")
        git(self.raiz, "config", "user.name", "Prueba")
        self.preparar(FASE_PLAN + "/plan_trabajo.md")
        git(self.raiz, "commit", "-q", "-m", "plan")
        self.preparar(FASE_PLAN + "/estado-fase.md", "src/tercero.py")
        self.assertEqual([], self.fallas())

    def test_avisa_la_prueba_que_lee_lo_que_cambia_y_no_se_declara(self):
        """Análisis 16 del pendiente 103, acuerdo 2."""
        self.escribir("src/a.py", "x = 1\n")
        self.escribir("tests/test_a.py", "import a\n")
        self.escribir("tests/test_otro.py", "import b\n")
        avisos = PlanContraLoHecho(self.raiz).pruebas_sin_declarar(self.ruta(FASE_PLAN))
        self.assertEqual(1, len(avisos))
        self.assertIn("tests/test_a.py", avisos[0].mensaje)
        self.assertNotIn("test_otro", avisos[0].mensaje)

    def test_el_pre_commit_lo_corre(self):
        self.assertIn("validar.py\" plan --raiz \"$(pwd)\" --preparados", PLANTILLA_PRE_COMMIT)


class ElRangoSeRevisaContraElPlan(Temporal):
    """`EP-023·HU-007·CA-02` · La integración continua revisa lo que trae un rango."""

    PLAN = ("# Plan\n\n**Aprobación** (`02·F4`): Ing. Prueba, el 2026-10-03, con la versión 53.1.0.\n\n"
            "### 2.1 Archivos que se crean o modifican\n\n"
            "| Archivo (ruta real verificada) | Tipo | Capa | Nota |\n|---|---|---|---|\n"
            "| `src/declarado.py` | Nuevo | Código | Lo que hace la fase |\n\n### 2.2 Otra\n")

    def test_lo_que_el_plan_no_declara_falla_y_lo_declarado_pasa(self):
        fase = "documentacion/epicas/EP-001-algo/HU-001-una-cosa/A-EP-001-HU-001-una-cosa"
        repo_con_autor(self.raiz)
        self.escribir("LEEME.md")
        git(self.raiz, "add", "-A")
        git(self.raiz, "commit", "-q", "-m", "inicio")
        self.escribir(fase + "/plan_trabajo.md", self.PLAN)
        self.escribir("src/declarado.py", "x = 1\n")
        git(self.raiz, "add", "-A")
        git(self.raiz, "commit", "-q", "-m", "la fase")
        self.assertEqual([], PlanContraLoHecho(self.raiz).comparar_rango("HEAD~1..HEAD"))
        self.escribir("src/otro.py", "y = 2\n")
        self.escribir(fase + "/estado-fase.md", "estado\n")
        git(self.raiz, "add", "-A")
        git(self.raiz, "commit", "-q", "-m", "algo más")
        fallas = PlanContraLoHecho(self.raiz).comparar_rango("HEAD~2..HEAD")
        self.assertEqual(["src/otro.py"], [h.archivo for h in fallas])


PLAN_CON_CASOS = """# Plan de Trabajo

## 2. Análisis previo

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/enlaces.py` | Modificar | lo declarado |
| `base/09-git.md` | Modificar | también |

## 3. Tareas

Cubre `CA-01` y `CA-02`.
"""

PRUEBAS_CON_CASOS = """# Plan de Pruebas

### CP-001 — algo de `CA-01`

texto

### CP-002 — algo de `CA-02`

texto
"""


class PlanContraLoHechoEnUnaFase(Temporal):
    """`EP-004 · HU-013` · Avisa, nunca detiene: un archivo de más puede ser un
    descubrimiento que se aprobó. El caso que decide es que los documentos de la
    propia fase no cuentan como archivo de más."""

    def setUp(self):
        super().setUp()
        self.fase = self.ruta("documentacion/epicas/EP-001-x/HU-001-y/A-EP-001-HU-001-la-fase")
        escribir(os.path.join(self.fase, "plan_trabajo.md"), PLAN_CON_CASOS)
        escribir(os.path.join(self.fase, "plan_pruebas.md"), PRUEBAS_CON_CASOS)
        self.plan = PlanContraLoHecho(self.raiz)

    def poner(self, nombre, texto):
        escribir(os.path.join(self.fase, nombre), texto)

    def test_cp001_lee_los_archivos_que_el_plan_declara(self):
        dec = PlanDeTrabajo.declarados(PLAN_CON_CASOS)
        self.assertIn("validadores/enlaces.py", dec)
        self.assertIn("base/09-git.md", dec)
        self.assertEqual(2, len(dec), "se coló algo que no era una ruta")

    def test_cp001b_el_declarado_no_se_avisa_y_el_de_mas_si(self):
        dec = PlanDeTrabajo.declarados(PLAN_CON_CASOS)
        self.assertTrue(PlanDeTrabajo.cuadra("validadores/enlaces.py", dec))
        self.assertFalse(PlanDeTrabajo.cuadra("validadores/secretos.py", dec))

    def test_cp002_sin_seccion_no_inventa_nada(self):
        self.poner("plan_trabajo.md", "# Plan\n\nSin la sección 2.1.\n")
        h = self.plan.comparar_archivos(self.fase, self.raiz, desde="HEAD")
        self.assertEqual(1, len(h))
        self.assertEqual(AVISO, h[0].severidad)
        self.assertIn("no declara ningún archivo", h[0].mensaje)

    def test_cp002b_sin_plan_no_hay_contra_que_comparar(self):
        os.remove(os.path.join(self.fase, "plan_trabajo.md"))
        self.assertIn("no hay contra qué comparar", self.plan.comparar_archivos(self.fase, self.raiz, desde="HEAD")[0].mensaje)

    def test_cp002c_sin_commit_de_origen_lo_dice(self):
        self.assertIn("desde qué commit", self.plan.comparar_archivos(self.fase, self.raiz, desde=None)[0].mensaje)

    def test_cp002d_lo_tocado_de_mas_se_avisa(self):
        """La vieja no comparaba contra un commit de verdad: acá se toca un archivo de más."""
        repo_con_autor(self.raiz)
        git(self.raiz, "add", "-A")
        git(self.raiz, "commit", "-q", "-m", "inicio")
        self.escribir("validadores/enlaces.py")
        self.escribir("validadores/secretos.py")
        self.poner("resultado_pruebas.md", "x\n")
        git(self.raiz, "add", "-A")
        avisos = self.plan.comparar_archivos(self.fase, self.raiz, desde="HEAD")
        self.assertEqual(["validadores/secretos.py"], [h.archivo for h in avisos])

    def test_cp003_el_criterio_sin_caso_se_avisa(self):
        self.poner("plan_pruebas.md", "# Plan de Pruebas\n\n### CP-001 — de `CA-01`\n")
        h = self.plan.comparar_casos(self.fase)
        self.assertEqual(1, len(h))
        self.assertIn("CA-02", h[0].mensaje)

    def test_cp003b_con_todos_los_criterios_cubiertos_se_calla(self):
        self.assertEqual([], self.plan.comparar_casos(self.fase))

    def test_cp003c_un_plan_de_pruebas_sin_ningun_caso_se_avisa(self):
        self.poner("plan_pruebas.md", "# Plan de Pruebas\n\nCubre `CA-01` y `CA-02`.\n")
        self.assertTrue(any("ningún caso" in x.mensaje for x in self.plan.comparar_casos(self.fase)))

    def test_cp004_los_documentos_de_la_propia_fase_no_cuentan(self):
        """Escribir el resultado **es** ejecutar la fase. La vieja comprobaba que
        cada nombre estuviera en la lista consigo misma; acá se mira la lista."""
        self.assertIn("resultado_pruebas.md", DE_LA_FASE)
        self.assertIn("estado-fase.md", DE_LA_FASE)
        self.assertFalse(PlanDeTrabajo.cuadra("documentacion/epicas/x/resultado_pruebas.md",
                                              PlanDeTrabajo.declarados(PLAN_CON_CASOS)),
                         "el filtro no es por ruta: es por nombre de documento")

    def test_cp005_nunca_detiene(self):
        self.poner("plan_trabajo.md", "# Plan\n\nSin sección.\n")
        h = self.plan.comparar_archivos(self.fase, self.raiz, desde="HEAD")
        self.assertEqual([], [x for x in h if x.severidad == FALLA])

    def test_cp006_encuentra_las_fases_por_su_plan(self):
        self.assertEqual([os.path.normcase(self.fase)], [os.path.normcase(f) for f in self.plan.fases_de()])


# ══ lo autorizado (`EP-023·HU-007·CP-003`) ════════════════════════════════

class LoAutorizanLasReglas(unittest.TestCase):
    """Con reglas de ejemplo: si entra o sale una regla real, la prueba no cambia
    (análisis 11 del pendiente 103, acuerdo 4)."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.estandar = os.path.join(tmp.name, "estandar")
        self.proyecto = os.path.join(tmp.name, "proyecto")
        os.makedirs(self.proyecto)
        self.regla("DOC90-escribe-notas.md", "## DOC90 · Escribe notas", "`notas/*.md`")
        self.regla("DOC91-escribe-actas.md", "## DOC91 · Escribe actas  ·  `[DEROGADA en 9.0.0 → ver 13·DOC90]`", "`actas/**`")
        self.regla("DOC92-escribe-senales.md", "## DOC92 · Escribe señales — *opt-in*", "`senales/*.md`")
        self.regla("DOC93-con-ejemplo.md", "## DOC93 · Muestra un ejemplo", None,
                   "```\n**Autoriza escribir:** `ejemplo/**`\n```\n")

    def regla(self, nombre, titulo, rutas, cuerpo=""):
        linea = "**Aplica a:** escribir-documento\n\n" + ("**Autoriza escribir:** %s\n" % rutas if rutas else "")
        escribir(os.path.join(self.estandar, "base", "13-documentacion", "reglas", nombre),
                 "%s\n\nTexto.\n\n%s\n%s" % (titulo, linea, cuerpo))

    def reglas(self):
        return [r for r, _ in Autorizaciones().de_la_base(self.estandar, self.proyecto)]

    def test_la_regla_vigente_autoriza(self):
        reglas = Autorizaciones().de_la_base(self.estandar, self.proyecto)
        self.assertEqual("13·DOC90", Autorizaciones.quien_autoriza("notas/hoy.md", reglas))
        self.assertIsNone(Autorizaciones.quien_autoriza("src/a.py", reglas))

    def test_la_regla_derogada_no_autoriza(self):
        self.assertNotIn("13·DOC91", self.reglas())

    def test_la_opt_in_apagada_no_autoriza_y_la_encendida_si(self):
        self.assertIn("13·DOC92", self.reglas())
        escribir(os.path.join(self.proyecto, "CLAUDE.md"), "- Patrón opt-in `13` (documentación): no\n")
        self.assertNotIn("13·DOC92", self.reglas())

    def test_el_ejemplo_dentro_de_un_bloque_de_codigo_no_cuenta(self):
        self.assertNotIn("13·DOC93", self.reglas())

    def test_una_regla_nueva_entra_sin_tocar_el_programa(self):
        antes = len(self.reglas())
        self.regla("DOC94-escribe-bitacoras.md", "## DOC94 · Escribe bitácoras", "`bitacoras/*.md`")
        self.assertEqual(antes + 1, len(self.reglas()))


# ══ los acuerdos (`EP-023 · HU-002 · fase B`) ═════════════════════════════

EPICA_A = "documentacion/epicas/EP-009-algo"
PENDIENTE_A = EPICA_A + "/pendientes/110-algo-falla"
HU_A = EPICA_A + "/HU-001-una-cosa"
FASE_A = HU_A + "/A-EP-009-HU-001-la-fase"
APROBADO_A = "> **Aprobado** por el usuario el 2026-10-03, en el turno 2.\n\n"


def analisis_con_acuerdos(numero, aprobado=True, acuerdos=("Tema uno: lo primero (turno 1).",
                                                           "Tema dos: lo segundo (turno 1).")):
    puntos = "\n".join("%d. %s" % (i, a) for i, a in enumerate(acuerdos, 1))
    filas = "\n".join("| %d | Hacer %d | %d | HU-001 |" % (i, i, i) for i in range(1, len(acuerdos) + 1))
    return ("# Análisis %d\n\n%s### 1 · Usuario, 2026-10-03 08:00:00\n\n> algo\n\n"
            "## Lo acordado\n\n%s\n\n## Lo que se tiene que hacer\n\n"
            "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n%s\n\n"
            "## Lo que aporta al análisis principal\n" % (numero, APROBADO_A if aprobado else "", puntos, filas))


def plan_con_decisiones(version="50.0.0", sale="Análisis 1, acuerdo 1", con_columna=True):
    aprobacion = "**Aprobación** (`02·F4`): Ana Pérez, el 2026-10-03, con la versión %s.\n\n" % version
    if con_columna:
        tabla = ("| Decisión | Alternativa descartada | Justificación | Sale de |\n|---|---|---|---|\n"
                 "| Hacer algo | Otra cosa | Porque sí | %s |\n" % sale)
    else:
        tabla = "| Decisión | Alternativa descartada | Justificación |\n|---|---|---|\n| Hacer algo | Otra cosa | Porque sí |\n"
    return ("# Plan\n\n%s| CA de HU-001 | Estado |\n|---|---|\n| CA-01 · Uno | ☐ |\n\n"
            "### 2.6 Decisiones técnicas\n\n%s\n### 2.7 Dudas\n\nNinguna.\n\n## 3. Tareas\n" % (aprobacion, tabla))


class ConAcuerdos(Temporal):

    def setUp(self):
        super().setUp()
        self.escribir(PENDIENTE_A + "/analisis-1.md", analisis_con_acuerdos(1))
        self.escribir(HU_A + "/HU-001-una-cosa.md",
                      "# HU-001\n\n## 4. Criterios\n\n### CA-01 · Uno\n\n**Sale de:** análisis 1, punto 1.\n\n"
                      "### CA-02 · Dos\n\n**Sale de:** análisis 1, punto 2.\n\n## 5. Otra\n")
        os.makedirs(self.ruta(FASE_A))
        self.acuerdos = Acuerdos(self.raiz)

    def claves(self):
        return [c for c, _ in self.acuerdos.de_la_fase(self.ruta(FASE_A))]


class LosAcuerdosDeLaFase(ConAcuerdos):
    """CP-001."""

    def test_la_fase_recien_creada_recibe_los_de_todos_sus_ca(self):
        self.assertEqual(["Análisis 1 del pendiente 110, acuerdo 1", "Análisis 1 del pendiente 110, acuerdo 2"],
                         self.claves())

    def test_con_plan_recibe_solo_los_de_sus_ca(self):
        self.escribir(FASE_A + "/plan_trabajo.md", plan_con_decisiones())
        self.assertEqual(["Análisis 1 del pendiente 110, acuerdo 1"], self.claves())

    def test_con_el_commit_anotado_ya_no_esta_en_curso(self):
        self.assertEqual(1, len(self.acuerdos.fases_en_curso()))
        self.escribir(FASE_A + "/estado-fase.md", "| 12 | Commit | 👤 autorizado | ✅ `abc1234` |\n")
        self.assertEqual([], self.acuerdos.fases_en_curso())

    def test_la_fase_vieja_cerrada_no_esta_en_curso(self):
        self.escribir(FASE_A + "/plan_trabajo.md", "# Plan\n\nAprobado por el usuario.\n")
        self.escribir(FASE_A + "/funcionalidad_implementada.md", "# Cierre\n")
        self.assertEqual([], self.acuerdos.fases_en_curso())

    def test_la_fase_nueva_con_cierre_y_sin_commit_sigue_en_curso(self):
        self.escribir(FASE_A + "/plan_trabajo.md", plan_con_decisiones())
        self.escribir(FASE_A + "/funcionalidad_implementada.md", "# Cierre\n")
        self.assertEqual(1, len(self.acuerdos.fases_en_curso()))


class LosAcuerdosDelAnalisisPrendido(ConAcuerdos):
    """CP-002."""

    def prender(self):
        self.escribir(PENDIENTE_A + "/analisis-2.md", analisis_con_acuerdos(2, acuerdos=("Tema tres: lo tercero (turno 1).",)))
        self.escribir(PENDIENTE_A + "/analisis-3.md", analisis_con_acuerdos(3, aprobado=False))
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-3.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE_A)

    def test_llegan_los_de_los_analisis_aprobados_del_pendiente(self):
        self.prender()
        self.assertEqual(["Análisis 1 del pendiente 110, acuerdo 1", "Análisis 1 del pendiente 110, acuerdo 2",
                          "Análisis 2 del pendiente 110, acuerdo 1"],
                         [c for c, _ in self.acuerdos.del_analisis_prendido()])

    def test_los_que_no_caben_llegan_nombrados(self):
        self.prender()
        texto = self.acuerdos.texto(tope=len(ENCABEZADO_ACUERDOS) + 400)
        self.assertIn("[NO CUPIERON", texto)
        self.assertIn("Análisis 2 del pendiente 110, acuerdo 1: Tema tres", texto)

    def test_sin_proyecto_no_hay_nada_que_dar(self):
        """El enganche nunca detiene: sobre una carpeta que no existe, el texto es vacío."""
        self.assertEqual("", Acuerdos(os.path.join(self.raiz, "no-existe")).texto())

    def test_el_instalador_registra_el_enganche(self):
        self.assertIn("hook_acuerdos.py", [h[2] for h in HOOKS_CLAUDE])


class LaDecisionDelPlanDiceDeDondeSale(ConAcuerdos):
    """CP-003."""

    def fallas(self, texto):
        self.escribir(FASE_A + "/plan_trabajo.md", texto)
        datos = {1: LectorDeAnalisis.leer(self.ruta(PENDIENTE_A + "/analisis-1.md"))}
        return [m for _, m in OrigenDeCadaPunto(self.raiz).revisar_plan(self.ruta(FASE_A + "/plan_trabajo.md"), datos)]

    def test_la_plantilla_tiene_la_columna(self):
        texto = leer(os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos", "07-plan-trabajo.md"))
        self.assertIn("| Decisión | Alternativa descartada | Justificación | Sale de |", texto)

    def test_sin_acuerdo_ni_marca_falla(self):
        self.assertEqual(1, len(self.fallas(plan_con_decisiones(sale="Me pareció bien"))))

    def test_un_acuerdo_que_no_existe_falla(self):
        self.assertIn("que no existe", self.fallas(plan_con_decisiones(sale="Análisis 1, acuerdo 9"))[0])

    def test_cita_valida_o_propuesta_pasan(self):
        self.assertEqual([], self.fallas(plan_con_decisiones()))
        self.assertEqual([], self.fallas(plan_con_decisiones(sale="Propuesta del agente")))

    def test_sin_la_columna_falla(self):
        self.assertIn("«Sale de»", self.fallas(plan_con_decisiones(con_columna=False))[0])

    def test_el_plan_aprobado_antes_no_se_revisa(self):
        self.assertEqual([], self.fallas(plan_con_decisiones(version="49.0.0", sale="Me pareció bien")))
        self.assertEqual([], self.fallas(plan_con_decisiones(version="49.0.0", con_columna=False)))


# ══ el origen de cada punto (`EP-023 · HU-002 · fase A`) ══════════════════

RESUMEN_O = "# Sesión\n\n### H-1. Algo falla\n\n| Campo | Valor |\n|---|---|\n| Qué pasó | x |\n"
PENDIENTE_O = ("# Pendiente: algo falla\n\n| | |\n|---|---|\n"
               "| **De dónde sale** | [H-1 de la sesión](../../../../resumen.md) |\n")
ANALISIS_O = """# Análisis 1: algo falla

> **Aprobado** por el usuario el 2026-10-02, en el turno 3.

## Conversación

### 1 · Usuario, 2026-10-02 10:00:00
> uno

### 2 · Usuario, 2026-10-02 10:01:00
> dos

> acá termina la conversación

## Lo acordado

1. Algo: se hace algo (turno {turno}).

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Hacer algo | {acordado} | EP-009, HU-001 |
"""
HU_O = """# HU-001 · Algo

## 4. Criterios de aceptación

### CA-01 · Algo pasa

{sale_de}

```gherkin
Dado algo
```
"""


class Origen(Temporal):

    def setUp(self):
        super().setUp()
        self.epica = self.ruta("documentacion/epicas/EP-009-algo")
        self.pendiente = os.path.join(self.epica, "7-algo-falla")
        self.armar()

    def armar(self, turno=1, acordado="1", sale_de="**Sale de:** análisis 1, punto 1.", pendiente=PENDIENTE_O):
        escribir(self.ruta("resumen.md"), RESUMEN_O)
        escribir(os.path.join(self.pendiente, "pendiente.md"), pendiente)
        escribir(os.path.join(self.pendiente, "analisis-1.md"), ANALISIS_O.format(turno=turno, acordado=acordado))
        escribir(os.path.join(self.epica, "HU-001-algo", "HU-001-algo.md"), HU_O.format(sale_de=sale_de))

    def fallas(self):
        return [m for _, m in OrigenDeCadaPunto(self.raiz).revisar()]

    def test_paso1_todo_con_su_origen_pasa(self):
        self.assertEqual(self.fallas(), [])

    def test_paso2_criterio_sin_sale_de(self):
        self.armar(sale_de="")
        self.assertEqual(self.fallas(), ["el CA-01 no tiene «Sale de»"])

    def test_paso3_criterio_cita_un_punto_que_no_existe(self):
        self.armar(sale_de="**Sale de:** análisis 1, punto 9.")
        self.assertEqual(self.fallas(), ["el CA-01 cita el punto 9 del análisis 1, que no existe"])

    def test_paso4_punto_acordado_cita_un_turno_que_no_existe(self):
        self.armar(turno=8)
        self.assertEqual(self.fallas(), ["el punto 1 de «Lo acordado» cita el turno 8, que no está en la conversación"])

    def test_paso5_punto_cita_un_acordado_que_no_existe(self):
        self.armar(acordado="4")
        self.assertEqual(self.fallas(),
                         ["el punto 1 de «Lo que se tiene que hacer» cita el punto 4 de «Lo acordado», que no existe"])

    def test_paso5b_la_fila_cita_el_acuerdo_de_otro_analisis_del_pendiente(self):
        dos = os.path.join(self.pendiente, "analisis-2.md")
        escribir(dos, ANALISIS_O.format(turno=1, acordado="Análisis 1, acuerdo 1"))
        self.assertEqual(self.fallas(), [])
        escribir(dos, ANALISIS_O.format(turno=1, acordado="Análisis 1, acuerdo 3"))
        self.assertEqual(self.fallas(), ["el punto 1 de «Lo que se tiene que hacer» cita el acuerdo 3 "
                                         "del análisis 1, que no existe"])

    def test_paso5c_la_fila_cita_una_regla_del_estandar(self):
        dos = os.path.join(self.pendiente, "analisis-2.md")
        escribir(dos, ANALISIS_O.format(turno=1, acordado="`13·DOC26`"))
        self.assertEqual(self.fallas(), [])
        escribir(dos, ANALISIS_O.format(turno=1, acordado="`13·DOC99`"))
        self.assertEqual(self.fallas(), ["el punto 1 de «Lo que se tiene que hacer» cita la regla "
                                         "13·DOC99, que no existe"])

    def test_paso6_pendiente_sin_origen_o_con_hallazgo_que_no_existe(self):
        self.armar(pendiente="# Pendiente: algo falla\n")
        self.assertEqual(self.fallas(), ["el pendiente no tiene «De dónde sale»"])
        self.armar(pendiente=PENDIENTE_O.replace("H-1 ", "H-5 "))
        self.assertEqual(self.fallas(), ["cita H-5, que no está en ../../../../resumen.md"])

    def test_paso7_epica_sin_analisis_no_se_revisa(self):
        otra = self.ruta("documentacion/epicas/EP-001-vieja")
        escribir(os.path.join(otra, "HU-001-vieja", "HU-001-vieja.md"), HU_O.format(sale_de=""))
        self.assertEqual(self.fallas(), [])

    def test_el_mensaje_cita_la_regla(self):
        self.armar(sale_de="")
        self.assertIn("02·F27", OrigenDeCadaPunto(self.raiz).validar()[0].mensaje)


# ══ el análisis en curso (`EP-023 · HU-001 · fase B`) ═════════════════════

def turno(k, usuario, agente="Respuesta."):
    return (f"### {k} · Usuario — 2026-10-02 10:0{k % 10}:00\n> {usuario}\n\n"
            f"**Agente** — 2026-10-02 10:0{k % 10}:30\n\n{agente}\n\n")


FILA_C = "| 1 | Hacer algo | 1 | EP-009, HU-001 |\n"
APORTA_C = ("## Lo que aporta al análisis principal\n\n**Resultado:** Ratifica.\n\n"
            "**Lo que suma al análisis principal:** La clase tiene suma.\n")
ANALISIS_C = ("# Análisis 1: algo\n\n## Conversación\n\n### 1 · Usuario, 2026-10-02 10:00:00\n> Algo\n\n"
              "> acá termina la conversación\n\n## Lo acordado\n\n1. Algo: se hace (turno 1).\n\n"
              "## Lo que se tiene que hacer\n\n| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n"
              "|---|---|---|---|\n" + FILA_C + "\n" + APORTA_C)
PRINCIPAL_C = ("# Análisis principal\n\n## Qué es\n\nCimiento es algo.\n\n"
               "## Lista de análisis\n\n| Fecha | Resultado | Análisis |\n|---|---|---|\n")


class ConTranscripcion(Temporal):

    def setUp(self):
        super().setUp()
        os.makedirs(self.ruta("historico-chat"))
        self.trans = escribir(self.ruta("historico-chat/2026-10-02-sesion.md"), "# Sesión\n\n")
        self.p7 = self.ruta("documentacion/7-algo-que-falla")
        escribir(os.path.join(self.p7, "pendiente.md"), "# Pendiente: algo que falla\n")
        self.curso = AnalisisEnCurso(self.raiz)

    def agregar(self, texto):
        with io.open(self.trans, "a", encoding="utf-8") as f:
            f.write(texto)

    def estado(self, analisis, desde=1):
        self.curso.guardar_estado({"analisis": analisis, "transcripcion": self.trans,
                                   "desde": desde, "pausa": None, "pausas": []})

    def llenar(self, ruta, turno_acordado):
        """Lo mínimo para que el análisis salido de la plantilla pase la revisión de origen."""
        self.curso.pasar()
        texto = leer(ruta).replace("1. «tema»: «lo que se decidió» (turno «N»).",
                                   "1. Algo: se hace (turno %d)." % turno_acordado)
        texto = re.sub(r"^\| 1 \| Pasar el pendiente.*\n", "", texto, flags=re.M)
        escribir(ruta, texto.replace("| «número» |", "| 1 |"))


class LaHerramientaLeeElEstado(ConTranscripcion):

    def test_los_puntos_suspensivos_pasan_a_tres_puntos(self):
        self.assertEqual(AnalisisEnCurso.limpiar("### 1 · Usuario — hora\n> Analicemos: …\n"),
                         "### 1 · Usuario, hora\n> Analicemos: ...\n")

    def test_cp001_escribe_en_el_analisis_del_estado(self):
        a1, a2 = os.path.join(self.p7, "analisis-1.md"), os.path.join(self.p7, "analisis-2.md")
        modelo = "# Análisis\n\n## Conversación\n\n> La escribe el enganche.\n\n> acá termina la conversación\n"
        escribir(a1, modelo)
        escribir(a2, modelo)
        self.agregar(turno(1, "hola") + turno(2, "sigue") + turno(3, "fin"))
        self.estado(a2, desde=2)
        self.curso.pasar()
        self.assertIn("### 2 · Usuario", leer(a2))
        self.assertNotIn("### 1 · Usuario", leer(a2))
        self.assertEqual(leer(a1), modelo)
        self.assertNotIn("analisis-1.md", leer(os.path.join(os.path.dirname(__file__), "analisis_en_curso.py")))

    def test_cp002_lo_agregado_a_mano_no_se_toca(self):
        a1 = escribir(os.path.join(self.p7, "analisis-1.md"),
                      "# Análisis\n\n## Conversación\n\n> Nota.\n\n> acá termina la conversación\n\n"
                      "## Lo acordado\n\nNota del usuario.\n")
        self.estado(a1)
        self.agregar(turno(1, "uno"))
        self.curso.pasar()
        self.agregar(turno(2, "dos"))
        self.curso.pasar()
        texto = leer(a1)
        self.assertIn("### 2 · Usuario", texto)
        self.assertTrue(texto.endswith("## Lo acordado\n\nNota del usuario.\n"))

    def test_cp003_sin_marcas_ni_etiquetas(self):
        a1 = escribir(os.path.join(self.p7, "analisis-1.md"),
                      "# Análisis\n\n## Conversación\n\n> Nota.\n\n> acá termina la conversación\n")
        self.agregar("### 1 · Usuario — 2026-10-02 10:00:00\n"
                     "> <ide_opened_file>The user opened x.md</ide_opened_file>\n"
                     "> <pasted_content id=\"1\">\n> texto pegado\n> </pasted_content id=\"1\">\n\n"
                     "**Agente** — 2026-10-02 10:00:30\n\nListo.\n\n")
        self.estado(a1)
        self.curso.pasar()
        texto = leer(a1)
        self.assertIn("### 1 · Usuario, 2026", texto)
        self.assertIn("**Agente**, 2026", texto)
        self.assertNotIn("pasted_content", texto)
        self.assertNotIn("ide_opened_file", texto)
        self.assertIn("texto pegado", texto)
        self.assertEqual(0, sum(len(Marcas.de_linea(l)) for l in texto.splitlines()))


class PrenderPausarApagar(ConTranscripcion):

    def test_cp004(self):
        self.agregar(turno(1, "hola") + turno(2, "Analicemos: el pendiente 7"))
        self.assertEqual(AnalisisEnCurso.pendiente_pedido("Analicemos: el pendiente 7"), 7)
        prendido, _ = self.curso.prender(7, self.trans, 2)
        self.assertTrue(prendido)
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.assertTrue(os.path.isfile(a1))
        self.assertEqual(self.curso.leer_estado()["desde"], 2)

        self.agregar(turno(3, "tres") + turno(4, "Pare") + turno(5, "otra cosa"))
        self.assertTrue(self.curso.pausar(4))
        self.agregar(turno(6, "Analicemos: el pendiente 7"))
        self.curso.prender(7, self.trans, 6)
        self.curso.pasar()
        texto = leer(a1)
        self.assertIn("Turnos 4 a 5 en pausa", texto)
        self.assertNotIn("### 5 · Usuario", texto)
        self.assertIn("### 6 · Usuario", texto)

        self.agregar("### 7 · Usuario — 2026-10-02 10:07:00\n> Apruebo el análisis\n\n")
        self.llenar(a1, 6)
        self.assertTrue(self.curso.aprobar(7, "2026-10-02"))
        self.assertIn("> **Aprobado** por el usuario el 2026-10-02, en el turno 7", leer(a1))
        self.curso.pasar()
        self.assertIsNotNone(self.curso.leer_estado())
        self.agregar("**Agente** — 2026-10-02 10:07:30\n\nAprobado.\n\n")
        self.curso.pasar()
        self.assertIsNone(self.curso.leer_estado())
        self.agregar(turno(8, "otra cosa"))
        self.curso.pasar()
        self.assertNotIn("### 8 · Usuario", leer(a1))
        self.assertIsNone(AnalisisEnCurso.pendiente_pedido("Analicemos por qué falla esto"))

    def test_h6_se_apaga_aunque_la_respuesta_llegue_tarde(self):
        """H-6: al cerrar el turno que aprobó, la respuesta aún no está escrita."""
        self.agregar(turno(1, "Analicemos: el pendiente 7"))
        self.curso.prender(7, self.trans, 1)
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.agregar("### 2 · Usuario — 2026-10-02 10:02:00\n> Apruebo el análisis\n\n")
        self.llenar(a1, 1)
        self.assertTrue(self.curso.aprobar(2, "2026-10-02"))
        self.curso.pasar()
        self.assertIsNotNone(self.curso.leer_estado())
        self.agregar("**Agente** — 2026-10-02 10:02:30\n\nAprobado.\n\n" + turno(3, "Escriba"))
        self.curso.pasar()
        self.assertIsNone(self.curso.leer_estado())
        texto = leer(a1)
        self.assertIn("Aprobado.", texto)
        self.assertNotIn("### 3 · Usuario", texto)

    def test_h9_la_respuesta_pasa_apenas_se_escribe(self):
        """H-9: la respuesta la pasa el histórico después de escribirla, no un enganche paralelo."""
        self.assertFalse([h for h in HOOKS_CLAUDE if h[0] == "Stop" and h[2] == "hook_analisis.py"])
        self.agregar(turno(1, "Analicemos: el pendiente 7").split("**Agente**")[0])
        self.curso.prender(7, self.trans, 1)
        self.agregar("**Agente** — 2026-10-02 10:01:30\n\nLa respuesta.\n\n")
        self.curso.pasar()
        self.assertIn("La respuesta.", leer(os.path.join(self.p7, "analisis-1.md")))

    def test_el_enlace_a_lo_que_se_movio_pasa_como_texto(self):
        self.agregar(turno(1, "Analicemos: el pendiente 7", "Quedó en [el archivo](otro/movido.md)."))
        self.curso.prender(7, self.trans, 1)
        self.curso.pasar()
        texto = leer(os.path.join(self.p7, "analisis-1.md"))
        self.assertIn("el archivo (`otro/movido.md`, ya no está ahí)", texto)
        self.assertNotIn("](", texto.split("## Conversación")[1].split("acá termina")[0])

    def test_h6_lo_que_entro_despues_de_aprobar_sale(self):
        self.agregar(turno(1, "Analicemos: el pendiente 7"))
        self.curso.prender(7, self.trans, 1)
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.agregar(turno(2, "Apruebo el análisis"))
        estado = self.curso.leer_estado()
        self.agregar(turno(3, "Escriba"))
        self.curso.pasar()
        self.assertIn("### 3 · Usuario", leer(a1))
        self.llenar(a1, 1)
        self.assertTrue(self.curso.aprobar(2, "2026-10-02"))
        self.curso.guardar_estado(estado)
        self.curso.pasar()
        texto = leer(a1)
        self.assertIn("### 2 · Usuario", texto)
        self.assertNotIn("### 3 · Usuario", texto)
        self.assertIsNone(self.curso.leer_estado())


class UnSoloAnalisisAbierto(ConTranscripcion):
    """La regla cambió el 2026-10-04: un análisis aprobado con HU por construir ya
    no bloquea. Lo que bloquea es otro análisis sin aprobar en la misma sesión."""

    def test_cp005(self):
        hu = escribir(self.ruta("documentacion/epicas/EP-009-x/HU-002-y/HU-002-y.md"), "| **Estado** | Lista |\n")
        escribir(os.path.join(self.p7, "analisis-1.md"),
                 "# Análisis 1\n\n> **Aprobado** por el usuario el 2026-10-01, en el turno 3.\n\n"
                 "## Lo que se tiene que hacer\n\n| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
                 "| 1 | Algo | 1 | EP-009, HU-002 |\n")
        escribir(self.ruta("documentacion/8-otra-cosa/pendiente.md"), "# Pendiente: otra cosa\n")
        self.agregar(turno(1, "Analicemos: el pendiente 8"))
        # El 7 está aprobado y su HU no ha terminado: no bloquea.
        prendido, _ = self.curso.prender(8, self.trans, 1)
        self.assertTrue(prendido)
        # El 8 quedó prendido sin aprobar: en la misma sesión no se prende otro.
        prendido, nota = self.curso.prender(7, self.trans, 2)
        self.assertFalse(prendido)
        self.assertIn("sin aprobar", nota)
        self.assertFalse(os.path.isfile(os.path.join(self.p7, "analisis-2.md")))
        os.remove(self.ruta(ESTADO.replace(os.sep, "/")))
        escribir(hu, "| **Estado** | Terminada el 2026-10-02 |\n")
        prendido, _ = self.curso.prender(7, self.trans, 1)
        self.assertTrue(prendido)


class ElAvisoDeCadaTurno(ConTranscripcion):
    """CP-006 y CP-010: lo que el enganche le entrega al agente sale de `aviso()` y
    de `por_que_no_se_aprueba()`; acá se prueban esas dos piezas."""

    def test_cp006(self):
        self.assertIn("Ningún análisis está prendido", self.curso.aviso())
        a1 = escribir(os.path.join(self.p7, "analisis-1.md"),
                      "# Análisis\n\n## Conversación\n\n> Nota.\n\n> acá termina la conversación\n")
        self.estado(a1)
        self.assertIn("analisis-1.md", self.curso.aviso())
        self.curso.pausar(3)
        self.assertIn("en pausa desde el turno 3", self.curso.aviso("una nota"))
        self.assertTrue(self.curso.aviso("una nota").endswith(" Una nota."))

    def test_cp010_dice_por_que_no_se_aprobo(self):
        a1 = escribir(os.path.join(self.p7, "analisis-1.md"), ANALISIS_C.replace(FILA_C, ""))
        self.estado(a1)
        self.assertIn("falta al menos una fila", self.curso.por_que_no_se_aprueba()[0])
        self.assertFalse(self.curso.aprobar(1, "2026-10-02"))
        self.assertNotIn("**Aprobado**", leer(a1))


class AprobarRevisaYPasaAlPrincipal(ConTranscripcion):
    """Fase D: aprobar revisa, marca la versión y pasa lo que suma."""

    def preparar(self, texto, carpeta=None):
        ruta = escribir(os.path.join(carpeta or self.p7, "analisis-1.md"), texto)
        self.estado(ruta)
        return ruta

    def test_cp006_la_marca_dice_la_version(self):
        a1 = self.preparar(ANALISIS_C)
        self.assertTrue(self.curso.aprobar(7, "2026-10-02"))
        self.assertIn(", con la versión %s." % AnalisisEnCurso.version(), leer(a1))
        self.assertTrue(AnalisisEnCurso.aprobado(a1))
        self.assertEqual(AnalisisEnCurso.turno_aprobado(a1), 7)

    def test_cp009_lo_que_suma_pasa_tal_cual_al_principal(self):
        principal = escribir(self.ruta("analisis/proyecto-analisis-principal.md"), PRINCIPAL_C)
        a1 = self.preparar(ANALISIS_C)
        self.assertTrue(self.curso.aprobar(7, "2026-10-02"))
        texto = leer(principal)
        self.assertIn("Cimiento es algo. La clase tiene suma.\n\n## Lista de análisis", texto)
        self.assertTrue(texto.endswith(
            "| 2026-10-02 | Ratifica | [Análisis 1 del pendiente 7](../documentacion/7-algo-que-falla/analisis-1.md) |\n"))
        self.assertEqual(AnalisisAprobados(self.raiz).copias(), [])
        self.assertEqual(AnalisisAprobados(self.raiz).fuera_de_la_lista(), [])
        self.assertTrue(os.path.isfile(a1))

    def test_cp009_el_modulo_con_principal_propio_lo_usa(self):
        del_proyecto = escribir(self.ruta("analisis/proyecto-analisis-principal.md"), PRINCIPAL_C)
        del_modulo = escribir(self.ruta("ventas/analisis/ventas-analisis-principal.md"), PRINCIPAL_C)
        self.preparar(ANALISIS_C, self.ruta("ventas/documentacion/8-otra-cosa"))
        self.assertTrue(self.curso.aprobar(7, "2026-10-02"))
        self.assertIn("La clase tiene suma.", leer(del_modulo))
        self.assertNotIn("La clase tiene suma.", leer(del_proyecto))

    def test_cp010_sin_filas_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS_C.replace(FILA_C, ""))
        self.assertEqual(self.curso.por_que_no_se_aprueba(), ["falta al menos una fila en «Lo que se tiene que hacer»"])
        self.assertFalse(self.curso.aprobar(7, "2026-10-02"))
        self.assertFalse(AnalisisEnCurso.aprobado(a1))

    def test_cp011_sin_lo_que_aporta_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS_C.replace(APORTA_C, ""))
        self.assertFalse(self.curso.aprobar(7, "2026-10-02"))
        self.assertFalse(AnalisisEnCurso.aprobado(a1))
        self.assertIn("Lo que aporta al análisis principal", self.curso.por_que_no_se_aprueba()[0])

    def test_cp011_sin_lo_que_suma_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS_C.replace("**Lo que suma al análisis principal:** La clase tiene suma.\n", ""))
        self.assertFalse(self.curso.aprobar(7, "2026-10-02"))
        self.assertFalse(AnalisisEnCurso.aprobado(a1))

    def test_con_una_falla_de_origen_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS_C.replace(FILA_C, "| 1 | Hacer algo | 2 | EP-009, HU-001 |\n"))
        self.assertIn("cita el punto 2 de «Lo acordado», que no existe", self.curso.por_que_no_se_aprueba()[0])
        self.assertFalse(self.curso.aprobar(7, "2026-10-02"))
        self.assertFalse(AnalisisEnCurso.aprobado(a1))

    def test_la_fila_puede_citar_el_acuerdo_de_otro_analisis(self):
        escribir(os.path.join(self.p7, "analisis-1.md"), "# Análisis 1\n\n## Lo acordado\n\n5. Otro: algo (turno 1).\n")
        escribir(os.path.join(self.p7, "pendiente.md"),
                 "# Pendiente: algo que falla\n\n| | |\n|---|---|\n| **De dónde sale** | H-1 |\n")
        a2 = escribir(os.path.join(self.p7, "analisis-2.md"), ANALISIS_C.replace(
            "# Análisis 1: algo\n", "# Análisis 2: algo\n\n## Hallazgo\n\n### H-1 · Algo\n").replace(
            FILA_C, FILA_C + "| 2 | Pasar el pendiente | Análisis 1, acuerdo 5 | Este análisis, de una |\n"))
        self.estado(a2)
        self.assertEqual(self.curso.por_que_no_se_aprueba(), [])
        escribir(a2, leer(a2).replace("acuerdo 5", "acuerdo 6"))
        self.assertIn("cita el acuerdo 6 del análisis 1, que no existe", self.curso.por_que_no_se_aprueba()[0])

    def test_la_plantilla_trae_lo_que_pide_aprobar(self):
        self.assertEqual(AnalisisEnCurso.faltantes(leer(os.path.join(RAIZ, PLANTILLA))), [])


CONVERSACION_M = ("## Conversación\n\n### 1 · Usuario, 2026-10-03 10:00:00\n> Algo\n\n"
                  "> acá termina la conversación\n\n## Lo acordado\n\n1. Algo: se hace (turno 1).\n\n")
RESTO_M = ("## Lo que se tiene que hacer\n\n| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n"
           "|---|---|---|---|\n| 1 | Hacer algo | 1 | EP-009, HU-001 |\n\n"
           "## Lo que aporta al análisis principal\n\n**Resultado:** Ratifica.\n\n"
           "**Lo que suma al análisis principal:** Algo.\n")


class ElAnalisisMejoraSuPendiente(Temporal):
    """`EP-023 · HU-003 · CA-09` · Cada análisis deja el pendiente en su versión siguiente."""

    def setUp(self):
        super().setUp()
        self.carpeta = self.ruta("documentacion/7-algo")
        self.trans = self.escribir("historico-chat/sesion.md", "# Sesión\n")
        self.curso = AnalisisEnCurso(self.raiz)

    @staticmethod
    def analisis(numero, hallazgo="### H-7 · Algo falla\n"):
        return "# Análisis %d: algo\n\n## Hallazgo\n\n%s\n%s%s" % (numero, hallazgo, CONVERSACION_M, RESTO_M)

    def pendiente(self, de_donde_sale):
        escribir(os.path.join(self.carpeta, "pendiente.md"),
                 "# Pendiente: algo\n\n| | |\n|---|---|\n| **De dónde sale** | %s |\n" % de_donde_sale)

    def prender(self, numero, texto):
        ruta = escribir(os.path.join(self.carpeta, "analisis-%d.md" % numero), texto)
        self.curso.guardar_estado({"analisis": ruta, "transcripcion": self.trans,
                                   "desde": 1, "pausa": None, "pausas": []})
        return ruta

    def test_cp001_sin_el_hallazgo_en_el_pendiente_no_se_aprueba(self):
        self.pendiente("H-3")
        ruta = self.prender(2, self.analisis(2))
        faltan = self.curso.por_que_no_se_aprueba()
        self.assertEqual(len(faltan), 1)
        self.assertIn("falta el H-7 en «De dónde sale» del pendiente", faltan[0])
        self.assertFalse(self.curso.aprobar(1, "2026-10-03"))
        self.assertFalse(AnalisisEnCurso.aprobado(ruta))

    def test_cp001_con_el_hallazgo_en_el_pendiente_se_aprueba(self):
        self.pendiente("H-3 y [H-7](x.md)")
        ruta = self.prender(2, self.analisis(2))
        self.assertEqual(self.curso.por_que_no_se_aprueba(), [])
        self.assertTrue(self.curso.aprobar(1, "2026-10-03"))
        self.assertTrue(AnalisisEnCurso.aprobado(ruta))

    def test_cp001_sin_numero_de_hallazgo_no_se_aprueba(self):
        self.pendiente("H-7")
        self.prender(2, self.analisis(2, hallazgo="Algo falla, sin número.\n"))
        self.assertIn("falta el número del hallazgo", self.curso.por_que_no_se_aprueba()[0])

    def test_cp001_un_numero_parecido_no_cuenta(self):
        self.pendiente("H-70")
        self.prender(2, self.analisis(2))
        self.assertIn("falta el H-7", self.curso.por_que_no_se_aprueba()[0])

    def test_cp002_el_analisis_1_no_se_revisa(self):
        self.pendiente("H-3")
        ruta = self.prender(1, self.analisis(1))
        self.assertEqual(self.curso.por_que_no_se_aprueba(), [])
        self.assertTrue(self.curso.aprobar(1, "2026-10-03"))
        self.assertTrue(AnalisisEnCurso.aprobado(ruta))

    def test_cp003_la_plantilla_pide_el_pendiente_en_su_version_siguiente(self):
        propuesta = AnalisisEnCurso.seccion(leer(os.path.join(RAIZ, PLANTILLA)), "Propuesta final")
        self.assertIn("### Pendiente V«N+1»", propuesta)
        self.assertIn("Antes de aprobar, se pasan a los originales", propuesta)


class ElPlanDelAnalisisLeeBienSusHU(Temporal):
    """La columna «Pasó a» de una fila hecha «de una y sin fase» nombra archivos, y
    sus rutas traían HU de otras épicas: el análisis no se cerraba nunca."""

    def hu(self, epica, hu, estado):
        nombre = "HU-%03d-algo" % hu
        self.escribir("documentacion/epicas/EP-%03d-algo/%s/%s.md" % (epica, nombre, nombre), "| **Estado** | %s |\n" % estado)

    def plan(self, celda):
        analisis = self.escribir("analisis-1.md", "## Lo que se tiene que hacer\n\n"
                                                  "| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
                                                  "| 1 | algo | 1 | %s |\n" % celda)
        return AnalisisEnCurso(self.raiz).plan_pendiente(analisis)

    def test_lo_hecho_de_una_no_espera_ninguna_hu(self):
        celda = ("Este análisis, de una y sin fase: `documentacion/epicas/EP-023-x/HU-007-y/a.md`, "
                 "`documentacion/epicas/EP-004-z/HU-012-w/b.md`, hecho el 2026-10-04")
        self.assertEqual(self.plan(celda), [])

    def test_cada_hu_va_con_su_propia_epica(self):
        self.hu(23, 7, "Terminada")
        self.hu(4, 12, "En curso")
        self.assertEqual(self.plan("EP-023, HU-007; EP-004, HU-012"), ["EP-004 HU-012"])

    def test_la_hu_enlazada_cuenta_una_vez(self):
        self.hu(23, 1, "En curso")
        self.assertEqual(self.plan("EP-023, [HU-001](../../HU-001-algo/HU-001-algo.md)"), ["EP-023 HU-001"])

    def test_terminada_la_hu_el_plan_se_cumple(self):
        self.hu(23, 1, "Terminada")
        self.assertEqual(self.plan("EP-023, HU 1"), [])


# ══ los análisis aprobados (`EP-023 · HU-001 · CA-06`, fase D, `HU-006`) ══════

SECCIONES = {
    "Cimiento": "### Cimiento: las reglas que aplican y las que chocan\n\nAlgo.\n",
    "El proyecto": "### El proyecto: lo que existe, lo que funciona y lo que falta\n\nAlgo.\n",
    "Lo aprendido": "### Lo aprendido: señales, lecciones y análisis anteriores\n\nAlgo.\n",
    "El entorno": "### El entorno: normas, herramientas y proyectos que heredan\n\nAlgo.\n",
}


def documento(aprobado=True, sin=None):
    marca = "> **Aprobado** por el usuario el 2026-10-01, en el turno 9.\n\n" if aprobado else ""
    partes = "".join(t for k, t in SECCIONES.items() if k != sin)
    return f"# Análisis 1: algo\n\n{marca}## Lo que aportó cada parte\n\n{partes}"


RECOMENDACIONES_D = "## Recomendaciones\n\n| Recomendación | Cómo |\n|---|---|\n| R-1 | Se listaron los casos |\n\n"
DONDE_D = ("### Dónde más puede pasar\n\n| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |\n"
           "|---|---|---|---|\n| Otro canal | Otra herramienta | Se escapa | Punto 1 |\n\n")
HU_D = ("## Propuesta final: hallazgo y pendiente\n\n"
        "| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos |\n"
        "|---|---|---|---|---|---|---|\n"
        "| 1 | 1 | Base | Algo | Ninguna | Las demás se apoyan en ella | 1 |\n"
        "| 2 | 2 | Encima | Algo | 1 | Usa la base | 2 |\n\n")
APORTA_D = ("## Lo que aporta al análisis principal\n\n**Resultado:** Ratifica.\n\n"
            "**Lo que suma al análisis principal:** La clase tiene suma.\n")
PRINCIPAL_D = ("# Análisis principal\n\n## Qué es\n\nCimiento es algo. La clase tiene suma.\n\n"
               "## Lista de análisis\n\n| Fecha | Resultado | Análisis |\n|---|---|---|\n"
               "| 2026-10-02 | Ratifica | [Análisis 1 del pendiente 7](../documentacion/7-algo/analisis-1.md) |\n")


def nuevo(version="44.0.0", recomendaciones=RECOMENDACIONES_D, donde=DONDE_D, hu=HU_D, aporta=APORTA_D):
    marca = "> **Aprobado** por el usuario el 2026-10-02, en el turno 9, con la versión %s.\n\n" % version
    return (f"# Análisis 1: algo\n\n{marca}{recomendaciones}## Hallazgo\n\nAlgo.\n\n"
            f"## Lo que aportó cada parte\n\n{''.join(SECCIONES.values())}{donde}{hu}{aporta}")


class UnAnalisisAprobadoTraeSusCuatroPartes(Temporal):

    def poner(self, texto, nombre="analisis-1.md"):
        self.escribir("documentacion/pendiente/" + nombre, texto)
        return AnalisisAprobados(self.raiz)

    def test_el_aprobado_completo_pasa(self):
        self.assertEqual(self.poner(documento()).revisar(), [])

    def test_al_aprobado_sin_lo_aprendido_se_le_nombra(self):
        fallas = self.poner(documento(sin="Lo aprendido")).revisar()
        self.assertEqual(len(fallas), 1)
        self.assertIn("«Lo aprendido»", fallas[0])

    def test_al_aprobado_sin_el_entorno_se_le_nombra(self):
        fallas = self.poner(documento(sin="El entorno")).revisar()
        self.assertEqual(len(fallas), 1)
        self.assertIn("«El entorno»", fallas[0])

    def test_el_abierto_incompleto_todavia_no_se_juzga(self):
        self.assertEqual(self.poner(documento(aprobado=False, sin="Cimiento")).revisar(), [])

    def test_solo_mira_los_analisis_numerados(self):
        self.assertEqual(self.poner(documento(sin="Cimiento"), nombre="base-cierre.md").revisar(), [])

    def test_la_falla_llega_a_validar(self):
        self.assertEqual(len(self.poner(documento(sin="El proyecto")).validar()), 1)


class LoQueExigeLa44(Temporal):

    def fallas(self, texto):
        self.escribir("documentacion/7-algo/analisis-1.md", texto)
        return AnalisisAprobados(self.raiz).revisar()

    def test_cp001_el_completo_pasa(self):
        self.assertEqual(self.fallas(nuevo()), [])

    def test_cp001_sin_donde_mas_falla(self):
        fallas = self.fallas(nuevo(donde=""))
        self.assertEqual(len(fallas), 1)
        self.assertIn("«Dónde más puede pasar»", fallas[0])

    def test_cp001_un_caso_sin_lo_que_lo_cubre_se_nombra(self):
        fallas = self.fallas(nuevo(donde=DONDE_D.replace("| Punto 1 |", "|  |")))
        self.assertEqual(len(fallas), 1)
        self.assertIn("«Otro canal»", fallas[0])

    def test_cp002_una_hu_antes_de_la_que_depende(self):
        fallas = self.fallas(nuevo(hu=HU_D.replace("| 1 | 1 | Base |", "| 3 | 1 | Base |")))
        self.assertEqual(len(fallas), 1)
        self.assertIn("la HU 2 va antes de la HU 1", fallas[0])

    def test_cp002_un_puesto_sin_razon(self):
        fallas = self.fallas(nuevo(hu=HU_D.replace("| Usa la base |", "|  |")))
        self.assertEqual(len(fallas), 1)
        self.assertIn("la HU 2 no dice por qué", fallas[0])

    def test_cp003_sin_recomendaciones_consultadas(self):
        fallas = self.fallas(nuevo(recomendaciones=""))
        self.assertEqual(len(fallas), 1)
        self.assertIn("recomendaciones", fallas[0])

    def test_cp003_recomendacion_sin_origen_y_repetida(self):
        self.escribir("plantillas/recomendaciones-del-analisis.md",
                      "| # | Qué se hace | Por qué | Sale de |\n|---|---|---|---|\n"
                      "| R-1 | Listar los casos | Para no dejar huecos | Análisis 8, lección 1 |\n"
                      "| R-2 | Listar los casos. | Otra razón | Análisis 2, lección 1 |\n"
                      "| R-3 | Medir la respuesta | Para no alargar | |\n")
        fallas = AnalisisAprobados(self.raiz).revisar()
        self.assertEqual(len(fallas), 2)
        self.assertTrue(any("la R-2 dice lo mismo que la R-1" in f for f in fallas))
        self.assertTrue(any("la R-3 no dice de qué análisis sale" in f for f in fallas))

    def test_cp003_las_de_cimiento_pasan(self):
        self.assertEqual(AnalisisAprobados(RAIZ).recomendaciones(), [])

    def test_cp004_el_que_no_esta_en_la_lista_avisa(self):
        self.escribir("analisis/proyecto-analisis-principal.md",
                      PRINCIPAL_D.replace("](../documentacion/7-algo/analisis-1.md)", "](otro.md)"))
        self.escribir("documentacion/7-algo/analisis-1.md", documento())
        avisos = AnalisisAprobados(self.raiz).fuera_de_la_lista()
        self.assertEqual(len(avisos), 1)
        self.assertIn("«Lista de análisis»", avisos[0][1])

    def test_cp004_el_que_esta_en_la_lista_no_avisa(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL_D)
        self.escribir("documentacion/7-algo/analisis-1.md", documento())
        self.assertEqual(AnalisisAprobados(self.raiz).fuera_de_la_lista(), [])

    def test_cp006_aprobado_antes_no_se_le_exige(self):
        self.assertEqual(self.fallas(nuevo(version="43.0.0", recomendaciones="", donde="", hu="")), [])

    def test_cp006_sin_version_en_la_marca_no_se_le_exige(self):
        self.assertEqual(self.fallas(documento()), [])

    def test_cp006_aprobado_con_la_44_sin_las_secciones_falla(self):
        self.assertEqual(len(self.fallas(nuevo(recomendaciones="", donde=""))), 2)

    def test_cp009_la_copia_cambiada_falla(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL_D.replace("tiene suma", "tiene resta"))
        fallas = self.fallas(nuevo())
        self.assertEqual(len(fallas), 1)
        self.assertIn("no está tal cual", fallas[0])

    def test_cp009_la_copia_igual_pasa(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL_D)
        self.assertEqual(self.fallas(nuevo()), [])

    def con_lecciones(self, version, senal="S-001", recomendacion="complementa R-1"):
        # La base de señales es la única fuente (análisis 10 del pendiente 103, acuerdo 7).
        base = self.ruta("senales.db")
        con = sqlite3.connect(base)
        con.execute("CREATE TABLE IF NOT EXISTS senales (id TEXT UNIQUE, tipo TEXT)")
        con.execute("INSERT OR IGNORE INTO senales VALUES ('S-001', 'leccion'), ('S-002', 'decision')")
        con.commit()
        con.close()
        os.environ["MEMORIA_DB"] = base
        self.addCleanup(os.environ.pop, "MEMORIA_DB", None)
        self.escribir("plantillas/recomendaciones-del-analisis.md",
                      "| # | Qué se hace | Por qué | Sale de |\n|---|---|---|---|\n"
                      "| R-1 | Listar los casos | Para no dejar huecos | Análisis 8, lección 1 |\n")
        tabla = ("## Lecciones aprendidas\n\n| # | Lección | Tipo | Señal | Recomendación |\n|---|---|---|---|---|\n"
                 "| 1 | Algo | Funcionó | %s | %s |\n\n" % (senal, recomendacion))
        return self.fallas(nuevo(version=version).replace("## Lo que aporta", tabla + "## Lo que aporta"))

    def test_hu006_cp001_la_leccion_que_enlaza_su_senal_pasa(self):
        self.assertEqual([], self.con_lecciones("46.0.0"))

    def test_hu006_cp001_la_leccion_sin_senal_de_tipo_leccion_falla(self):
        for senal in ("Por escribir", "S-002", "S-009"):
            fallas = self.con_lecciones("46.0.0", senal=senal)
            self.assertEqual(1, len(fallas), senal)
            self.assertIn("no enlaza una señal de tipo `leccion`", fallas[0])

    def test_hu006_cp002_la_recomendacion_vacia_o_que_no_existe_falla(self):
        self.assertIn("no dice qué recomendación", self.con_lecciones("46.0.0", recomendacion="")[0])
        self.assertIn("la R-9, que no existe", self.con_lecciones("46.0.0", recomendacion="nueva R-9")[0])
        self.assertEqual([], self.con_lecciones("46.0.0", recomendacion="no aplica"))

    def test_hu006_cp003_lo_aprobado_antes_no_se_reabre(self):
        self.assertEqual([], self.con_lecciones("45.0.0", senal="Por escribir", recomendacion=""))

    def test_los_prompts_no_son_analisis(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL_D)
        self.escribir("prompts/analisis/un-pedido.md", "# Lo que pidió el usuario\n")
        self.escribir("documentacion/7-algo/analisis-1.md", documento())
        self.assertEqual(AnalisisAprobados(self.raiz).fuera_de_la_lista(), [])


# ══ el plan de cada fase (`02·F14`, `F17`, `F0`, `F22`) ════════════════════

class Flujo(unittest.TestCase):
    """`02·F14`/`F17`: el plan de trabajo. Núcleo puro."""

    def _plan_completo(self):
        return "\n".join(f"## {k}. Sección" for k in range(0, 14))

    def test_plan_completo_no_reporta(self):
        self.assertEqual(PlanDeLaFase.revisar_plan(self._plan_completo()), ([], []))

    def test_secciones_faltantes_se_listan(self):
        faltan, _ = PlanDeLaFase.revisar_plan("## 0. Id\n## 1. Alcance\n## 13. Cierre")
        self.assertIn(5, faltan)
        self.assertNotIn(0, faltan)
        self.assertNotIn(13, faltan)

    def test_marca_de_incertidumbre_se_reporta(self):
        _, inc = PlanDeLaFase.revisar_plan(self._plan_completo() + "\n- ruta: app/Foo.php (o similar)")
        self.assertEqual(len(inc), 1)

    def test_tbd_se_reporta(self):
        _, inc = PlanDeLaFase.revisar_plan("## 0.\ntabla: TBD")
        self.assertTrue(any("TBD" in frag for _, frag in inc))


class FlujoF0(Temporal):
    """`02·F0`: los padres de cada fase, contra un árbol temporal."""

    def _fase(self, con_doc_hu, con_doc_epica):
        os.makedirs(self.ruta("documentacion/epicas/EP-001-x/HU-001-y/A-EP-001-HU-001-z"))
        if con_doc_hu:
            self.escribir("documentacion/epicas/EP-001-x/HU-001-y/HU-001-y.md", "")
        if con_doc_epica:
            self.escribir("documentacion/epicas/EP-001-x/epica.md", "")
        return PlanDeLaFase(self.raiz).validar()

    def test_padres_presentes_no_reportan_f0(self):
        self.assertFalse(any("F0" in h.mensaje for h in self._fase(True, True)))

    def test_hu_sin_documento_reporta_f0(self):
        self.assertTrue(any("F0" in h.mensaje and "HU" in h.mensaje for h in self._fase(False, True)))

    def test_epica_sin_documento_reporta_f0_una_vez(self):
        self.assertEqual(1, sum(1 for h in self._fase(True, False) if "F0" in h.mensaje and "épica" in h.mensaje))


class LaDerogacionSeCobraDondeHayFases(Temporal):
    """`02·F22` · CP-003: con una derogación sin adoptar, la falla sale por el
    recorrido del plan donde hay fases, y solo ahí."""

    def test_cp_003_sin_fases_no_se_cobra(self):
        escribir(self.ruta("CLAUDE.md"), "# Proyecto de prueba\n\nVersión del estándar adoptada: 3.0.0\n")
        fase = self.ruta("documentacion/epicas/EP-001-x/HU-001-y/A-EP-001-HU-001-z")
        os.makedirs(fase)
        self.assertTrue(VersionDelEstandar(self.raiz).derogaciones(), "sin derogaciones el caso no comprobaría nada")
        con_fase = [h for h in PlanDeLaFase(self.raiz).validar() if "F22" in str(h)]
        self.assertEqual(len(con_fase), 1, "con fase, la falla tiene que salir por el recorrido del plan")
        shutil.rmtree(fase)
        self.assertEqual([h for h in PlanDeLaFase(self.raiz).validar() if "F22" in str(h)], [])


# ══ un hallazgo detiene la fase (`EP-023 · HU-004 · fase A · CP-002`) ═══════

class UnHallazgoDetieneLaFase(Temporal):
    """Mientras el análisis que abrió el hallazgo siga sin aprobar, la fase que sale
    del pendiente no dice «Cumple» ni su HU «Terminada»."""

    EPICA = "documentacion/epicas/EP-009-algo"
    MARCA = "> **Aprobado** por el usuario el 2026-10-02, en el turno 3.\n\n"

    def setUp(self):
        super().setUp()
        hu, pendiente = self.EPICA + "/HU-001-una-cosa", self.EPICA + "/pendientes/110-algo-falla"
        self.pendiente = pendiente
        self.escribir(pendiente + "/pendiente.md", "# Pendiente: algo\n")
        self.escribir(pendiente + "/analisis-1.md", "# Análisis 1\n\n" + self.MARCA)
        self.escribir(hu + "/A-EP-009-HU-001-la-fase/plan_trabajo.md",
                      "# Plan\n\n**ORIGEN**: sale del [análisis 1](../../pendientes/110-algo-falla/analisis-1.md).\n")
        self.escribir(hu + "/A-EP-009-HU-001-la-fase/estado-fase.md",
                      "# Estado\n\n| Campo | Valor |\n|---|---|\n| **Concepto** | Cumple |\n")
        self.escribir(hu + "/HU-001-una-cosa.md", "# HU-001\n\n| Campo | Valor |\n|---|---|\n| **Estado** | Terminada |\n")

    def detenidas(self):
        return [h.mensaje for h in EstructuraDeFases(self.raiz).detenidas_por_un_hallazgo() if h.severidad == FALLA]

    def test_sin_hallazgo_cierra(self):
        self.assertEqual([], self.detenidas())

    def test_con_el_analisis_del_hallazgo_abierto_no_cierran(self):
        self.escribir(self.pendiente + "/analisis-2.md", "# Análisis 2: lo que falló\n")
        fallas = self.detenidas()
        self.assertEqual(2, len(fallas))
        self.assertTrue(any("la fase dice «Cumple»" in f and "analisis-2.md" in f for f in fallas))
        self.assertTrue(any("la HU dice «Terminada»" in f for f in fallas))

    def test_aprobado_el_analisis_del_hallazgo_vuelve_a_cerrar(self):
        self.escribir(self.pendiente + "/analisis-2.md", "# Análisis 2\n\n" + self.MARCA)
        self.assertEqual([], self.detenidas())


# ══ el resumen de la sesión (`13·DOC22`, `EP-005·HU-008`) ══════════════════

class ResumenDeLaSesion(Temporal):
    """Crea, avisa y muestra lo abierto."""

    def setUp(self):
        super().setUp()
        os.makedirs(self.ruta("historico-chat/resumenes/2026-08-14"))
        self.escribir("plantillas/sesion.md", "# Modelo\n\n## Hallazgos de esta sesión\n\n"
                                              "### H-1 · «título»\n- **Estado:** «resuelto acá / abierto»\n")

    def resumen(self, nombre, cuerpo):
        return self.escribir("historico-chat/resumenes/2026-08-14/" + nombre, cuerpo)

    def test_crea_el_archivo_con_el_modelo_y_sin_hallazgos(self):
        ruta = Resumen.crear(self.raiz, "2026-08-14-maracuya.md", self.raiz)
        self.assertTrue(os.path.isfile(ruta))
        self.assertEqual(Resumen.hallazgos(ruta), [])

    def test_no_pisa_el_resumen_que_ya_existe(self):
        ruta = self.resumen("maracuya.md", "### H-1 · algo\n- **Estado:** abierto\n")
        Resumen.crear(self.raiz, "2026-08-14-maracuya.md", self.raiz)
        self.assertIn("H-1 · algo", leer(ruta))

    def test_dos_sesiones_del_mismo_dia_son_dos_archivos(self):
        a = Resumen.crear(self.raiz, "2026-08-14-maracuya.md", self.raiz)
        b = Resumen.crear(self.raiz, "2026-08-14-pepito.md", self.raiz)
        self.assertNotEqual(a, b)
        self.assertTrue(os.path.isfile(a) and os.path.isfile(b))

    def test_renombrar_mueve_tambien_el_resumen(self):
        ruta = self.escribir("historico-chat/2026-08-14-sesion.md", "<!-- sesion: x -->\n\n# 2026-08-14 — Sesión\n")
        self.resumen("sesion.md", "# lo que quedó\n")
        Historico.renombrar(ruta, "maracuya", "prueba")
        self.assertTrue(os.path.isfile(self.ruta("historico-chat/resumenes/2026-08-14/maracuya.md")))
        self.assertFalse(os.path.isfile(self.ruta("historico-chat/resumenes/2026-08-14/sesion.md")))

    def test_renombrar_sin_resumen_no_falla(self):
        ruta = self.escribir("historico-chat/2026-08-14-sesion.md", "<!-- sesion: x -->\n\n# 2026-08-14 — Sesión\n")
        Historico.renombrar(ruta, "pepito", "prueba")
        self.assertTrue(os.path.isfile(self.ruta("historico-chat/2026-08-14-pepito.md")))

    def test_avisa_que_no_hay_ningun_hallazgo(self):
        self.assertEqual(Resumen.falta(self.resumen("maracuya.md", "# lo que quedó\n")), ["vacio"])

    def test_avisa_que_falta_decir_si_se_puede_cerrar(self):
        ruta = self.resumen("maracuya.md", "### H-1 · algo\n- **Estado:** abierto\n\n"
                                           "## ¿Se puede cerrar la sesión?\n\n| x | ☐ |\n")
        self.assertEqual(Resumen.falta(ruta), ["cierre"])

    def test_calla_cuando_no_falta_nada(self):
        ruta = self.resumen("maracuya.md", "### H-1 · algo\n- **Estado:** resuelto acá\n\n"
                                           "## ¿Se puede cerrar la sesión?\n\n| x | ☑ |\n")
        self.assertEqual(Resumen.falta(ruta), [])

    def test_el_aviso_no_se_repite(self):
        ruta = self.resumen("maracuya.md", "# lo que quedó\n")
        self.assertEqual(Resumen.falta(ruta), ["vacio"])
        Resumen.marcar_avisado(ruta, "vacio")
        self.assertEqual(Resumen.falta(ruta), [])

    def test_la_marca_del_aviso_vive_en_el_propio_resumen(self):
        ruta = self.resumen("maracuya.md", "# lo que quedó\n")
        Resumen.marcar_avisado(ruta, "vacio")
        self.assertIn(MARCA_VACIO, leer(ruta))

    def test_muestra_el_hallazgo_del_proposito_si_sigue_abierto(self):
        self.resumen("maracuya.md", "### H-4 · el hueco\n- **Estado:** abierto\n- **Con qué se retoma:** la pregunta viva\n")
        p = Resumen.proposito(self.raiz, self.resumen("pepito.md", "**Viene de:** 2026-08-14 · maracuya · H-4\n"))
        self.assertIsNotNone(p)
        self.assertEqual(p[1], "H-4")
        self.assertEqual(p[3], "la pregunta viva")

    def test_no_muestra_lo_abierto_de_otro_tema(self):
        self.resumen("otro-tema.md", "### H-9 · nada que ver\n- **Estado:** abierto\n")
        self.resumen("maracuya.md", "### H-4 · el hueco\n- **Estado:** resuelto acá\n")
        self.assertIsNone(Resumen.proposito(self.raiz, self.resumen("pepito.md", "**Viene de:** 2026-08-14 · maracuya · H-4\n")))

    def test_sin_proposito_declarado_no_muestra_nada(self):
        self.assertIsNone(Resumen.proposito(self.raiz, self.resumen("pepito.md", "**Viene de:** «AAAA-MM-DD · tema · H-N»\n")))

    def test_un_proyecto_sin_carpeta_de_resumenes_no_se_ve_afectado(self):
        with tempfile.TemporaryDirectory() as otra:
            self.assertEqual(Resumen.crear(otra, "2026-08-14-maracuya.md", otra), "")
            self.assertEqual(os.listdir(otra), [])


class ElResumenPorElCaminoReal(Temporal):
    """Los mismos criterios con la transcripción escrita por el histórico, como en
    una sesión de verdad: al abrir la transcripción no existe, y el resumen nace en
    el primer mensaje. La carpeta la deja el instalador."""

    def setUp(self):
        super().setUp()
        Instalador().instalar_historico(self.raiz, True)
        self.historico = Historico(self.raiz)

    def abrir(self, sesion, mensaje="hola"):
        transcripcion = self.historico.anotar_usuario(sesion, mensaje)
        return Resumen.crear(self.raiz, transcripcion, RAIZ)

    def test_el_instalador_deja_la_carpeta_de_resumenes(self):
        self.assertTrue(os.path.isfile(self.ruta("historico-chat/resumenes/README.md")))

    def test_al_abrir_todavia_no_hay_transcripcion_y_no_falla(self):
        self.assertEqual("", self.historico.archivo("s1"))

    def test_el_resumen_aparece_solo_en_una_sesion_nueva(self):
        ruta = self.abrir("s1")
        self.assertTrue(os.path.isfile(ruta), "el resumen no nació")
        self.assertEqual(Resumen.hallazgos(ruta), [])
        self.assertIn("¿Se puede cerrar la sesión?", leer(ruta))

    def test_el_indice_del_dia_queda_con_su_linea(self):
        ruta = self.abrir("s1")
        self.assertIn(os.path.basename(ruta), leer(os.path.join(os.path.dirname(ruta), "README.md")))

    def test_dos_sesiones_el_mismo_dia_dan_dos_archivos(self):
        a, b = self.abrir("s1"), self.abrir("s2", "otra cosa")
        self.assertNotEqual(a, b)
        self.assertTrue(os.path.isfile(a) and os.path.isfile(b))

    def test_el_encabezado_no_enlaza_fuera_del_proyecto(self):
        ruta = self.abrir("s1")
        texto = leer(ruta)
        self.assertNotIn("plantillas/sesion.md", texto)
        for destino in ("../../" + os.path.basename(self.historico.archivo("s1")), "../../README.md"):
            self.assertTrue(os.path.isfile(os.path.join(os.path.dirname(ruta), destino)), f"enlace roto: {destino}")

    def test_el_resumen_recien_nacido_avisa_que_sigue_vacio(self):
        self.assertEqual(["vacio"], Resumen.falta(self.abrir("s1")))

    def test_muestra_lo_abierto_del_proposito_y_nada_mas(self):
        ruta = self.abrir("s1")
        dia = os.path.dirname(ruta)
        escribir(os.path.join(dia, "maracuya.md"), "### H-4 · el hueco\n- **Estado:** abierto\n"
                                                   "- **Con qué se retoma:** la pregunta viva\n")
        escribir(os.path.join(dia, "pepito.md"), "### H-9 · nada que ver\n- **Estado:** abierto\n")
        escribir(ruta, leer(ruta).replace("| Viene de | «...» |", f"| Viene de | {os.path.basename(dia)} · maracuya · H-4 |"))
        origen, hid, _titulo, retoma = Resumen.proposito(self.raiz, ruta)
        self.assertEqual(("H-4", "la pregunta viva"), (hid, retoma))
        self.assertTrue(origen.endswith("maracuya.md"))

    def test_correrlo_dos_veces_no_pisa_lo_escrito(self):
        ruta = self.abrir("s1")
        with io.open(ruta, "a", encoding="utf-8") as f:
            f.write("\n### H-1 · algo escrito a mano\n- **Estado:** abierto\n")
        self.abrir("s1", "otra vez")
        self.assertIn("algo escrito a mano", leer(ruta))
        indice = leer(os.path.join(os.path.dirname(ruta), "README.md"))
        self.assertEqual(indice.count(f"({os.path.basename(ruta)})"), 1)

    def test_un_proyecto_sin_instalar_no_se_ve_afectado(self):
        with tempfile.TemporaryDirectory() as otra:
            self.assertEqual("", Historico(otra).anotar_usuario("s1", "hola"))
            self.assertEqual("", Resumen.crear(otra, "2026-08-14-x.md", RAIZ))
            self.assertEqual(os.listdir(otra), [])


class LaCarpetaDelDiaNaceEnElIndice(Temporal):
    """Pendiente 32: un resumen que no está en el índice es un resumen que nadie abre."""

    def proyecto(self, con_indice=True):
        os.makedirs(self.ruta("historico-chat/resumenes"))
        if con_indice:
            self.escribir("historico-chat/resumenes/README.md",
                          "# Resúmenes\n\n## Días\n\n- [2026-01-01/](2026-01-01/) — algo.\n")
        self.escribir("historico-chat/2026-03-04-un-tema.md", "# sesión\n")

    def crear(self):
        return Resumen.crear(self.raiz, "2026-03-04-un-tema.md", RAIZ)

    def indice(self):
        return self.leer("historico-chat/resumenes/README.md")

    def test_el_dia_nuevo_queda_anotado(self):
        self.proyecto()
        self.assertTrue(self.crear(), "no se creó el resumen")
        self.assertIn("(2026-03-04/)", self.indice())

    def test_no_pisa_los_dias_que_ya_estaban(self):
        self.proyecto()
        self.crear()
        self.assertIn("(2026-01-01/)", self.indice())

    def test_no_duplica_la_linea_al_correr_dos_veces(self):
        self.proyecto()
        self.crear()
        self.crear()
        self.assertEqual(1, self.indice().count("(2026-03-04/)"))

    def test_sin_indice_no_se_cae(self):
        self.proyecto(con_indice=False)
        self.assertTrue(self.crear(), "se cayó por no haber índice")

    def test_el_indice_del_dia_sigue_escribiendose(self):
        self.proyecto()
        ruta = self.crear()
        self.assertIn(os.path.basename(ruta), leer(os.path.join(os.path.dirname(ruta), "README.md")))

    def test_la_linea_del_dia_dice_donde_vive(self):
        """`EP-004 · HU-008 · CA-04`: el mismo cálculo que usa `DOC14` la da por buena."""
        indice = self.escribir("historico-chat/resumenes/README.md", "# Resúmenes\n\n## Días\n\n")
        self.escribir("historico-chat/README.md", "# Histórico\n")
        Resumen.indexar_dias(self.raiz, "2026-01-01")
        texto = leer(indice)
        self.assertIn("- [historico-chat/resumenes/2026-01-01/](2026-01-01/) — sin escribir todavía.", texto)
        os.makedirs(self.ruta("historico-chat/resumenes/2026-01-01"))
        enlaces = Enlaces(Proyecto(self.raiz))
        from ..comun import Markdown
        for _n, t, d in Markdown.enlaces(texto):
            self.assertIsNone(enlaces.texto_esperado(indice, t, d))


CIERRE_R = "\n## ¿Se puede cerrar la sesión?\n\n| Para cerrar | Estado |\n|---|---|\n| Todo hallazgo resuelto tiene su decisión escrita | ☑ |\n"


class VacioEIlegibleNoSonLoMismo(Temporal):
    """`EP-005 · HU-008` · Un resumen escrito como `### 1 ·` no es un resumen vacío:
    uno pide escribir y el otro renumerar lo que ya está."""

    def poner(self, texto):
        return self.escribir("sesion-1.md", texto)

    def test_el_que_no_tiene_nada_sigue_diciendo_vacio(self):
        self.assertEqual(["vacio"], Resumen.falta(self.poner("# Sesión\n\nTodavía nada.\n")))

    def test_el_escrito_sin_la_h_dice_molde_y_no_vacio(self):
        self.assertEqual(["molde"], Resumen.falta(self.poner("# Sesión\n\n### 1 · Uno\n\ntexto\n\n### 2 · Dos\n\ntexto\n")))

    def test_dice_cuantos_hay_escritos(self):
        ruta = self.poner("# Sesión\n\n### 1 · Uno\n\n### 2 · Dos\n\n### 3 · Tres\n")
        self.assertEqual(["Uno", "Dos", "Tres"], Resumen.hallazgos_fuera_del_molde(ruta))

    def test_el_que_ya_tiene_los_suyos_no_se_reporta(self):
        ruta = self.poner("# Sesión\n\n### H-1 · Uno\n\n### 2 · Una tabla\n" + CIERRE_R)
        self.assertEqual([], Resumen.hallazgos_fuera_del_molde(ruta))
        self.assertNotIn("molde", Resumen.falta(ruta))

    def test_el_aviso_no_se_repite(self):
        ruta = self.poner("# Sesión\n\n### 1 · Uno\n")
        self.assertEqual(["molde"], Resumen.falta(ruta))
        Resumen.marcar_avisado(ruta, "molde")
        self.assertEqual([], Resumen.falta(ruta))

    def test_la_marca_del_molde_no_es_la_del_vacio(self):
        ruta = self.poner("# Sesión\n\nTodavía nada.\n")
        Resumen.marcar_avisado(ruta, "molde")
        self.assertEqual(["vacio"], Resumen.falta(ruta), "marcar el molde apagó el aviso de vacío")

    def test_sin_hallazgos_legibles_el_cierre_nunca_se_mira(self):
        ruta = self.poner("# Sesión\n\n### 1 · Uno\n\n## ¿Se puede cerrar la sesión?\n\n"
                          "| Para cerrar | Estado |\n|---|---|\n| Algo | ☐ |\n")
        self.assertEqual(["molde"], Resumen.falta(ruta), "debería avisar del molde, no del cierre")

    def test_con_la_h_puesta_el_cierre_si_se_mira(self):
        ruta = self.poner("# Sesión\n\n### H-1 · Uno\n\n## ¿Se puede cerrar la sesión?\n\n"
                          "| Para cerrar | Estado |\n|---|---|\n| Algo | ☐ |\n")
        self.assertEqual(["cierre"], Resumen.falta(ruta))

    def test_ningun_resumen_del_repositorio_queda_ilegible(self):
        """Se cae cuando alguien escriba el próximo a mano sin la `H-`. Lo que vive
        en `pendientes/` del día es un pendiente o un análisis, no un resumen: la
        vieja lo contaba y fallaba con la conversación del análisis 1 del 116."""
        malos = []
        for dirp, dn, fn in os.walk(os.path.join(RAIZ, HISTORICO, RESUMENES)):
            dn[:] = [d for d in dn if d != "pendientes"]
            for nombre in fn:
                if nombre.endswith(".md") and nombre != "README.md":
                    fuera = Resumen.hallazgos_fuera_del_molde(os.path.join(dirp, nombre))
                    if fuera:
                        malos.append((os.path.relpath(os.path.join(dirp, nombre), RAIZ), len(fuera)))
        self.assertEqual([], malos)


HALLAZGO_TABLA = """### H-1 · el hueco

| Campo | Valor |
|---|---|
| Qué pasó | el usuario preguntó por qué el agente olvida las reglas |
| Estado | abierto |
| Con qué se retoma | ¿cuál es el tope? |
"""
HALLAZGO_VINETA = "### H-2 · el viejo\n\n- **Estado:** resuelto acá\n- **Con qué se retoma:** —\n"


class ElResumenLeeLasDosFormas(Temporal):
    """`EP-004·HU-012·CA-06`: la fila de tabla del molde y la viñeta de los viejos."""

    def test_lee_el_estado_en_la_tabla(self):
        ruta = self.escribir("nuevo.md", HALLAZGO_TABLA)
        self.assertEqual([("H-1", "el hueco", "abierto")], Resumen.hallazgos(ruta))
        self.assertEqual("¿cuál es el tope?", Resumen.retoma(ruta, "H-1"))

    def test_sigue_leyendo_la_forma_vieja(self):
        ruta = self.escribir("viejo.md", HALLAZGO_VINETA)
        self.assertEqual([("H-2", "el viejo", "resuelto acá")], Resumen.hallazgos(ruta))
        self.assertEqual("—", Resumen.retoma(ruta, "H-2"))

    def test_viene_de_se_lee_en_la_tabla_y_en_la_forma_vieja(self):
        nuevo_ = self.escribir("a.md", "| Campo | Valor |\n|---|---|\n| Viene de | 2026-09-28 · sesion · H-1 |\n")
        viejo = self.escribir("b.md", "**Viene de:** 2026-09-28 · sesion · H-1\n")
        vacio = self.escribir("c.md", "| Campo | Valor |\n|---|---|\n| Viene de | «...» |\n")
        self.assertEqual("2026-09-28 · sesion · H-1", Resumen.viene_de(nuevo_))
        self.assertEqual("2026-09-28 · sesion · H-1", Resumen.viene_de(viejo))
        self.assertEqual("", Resumen.viene_de(vacio))


EPICA_P = "documentacion/epicas/EP-009-algo"
HU_P = EPICA_P + "/HU-001-una-cosa"
PENDIENTE_P = ("# Pendiente: algo falla\n\n| | |\n|---|---|\n| **De dónde sale** | {origen} |\n\n"
               "## El problema\n\nAlgo.\n\n## Por qué importa\n\nAlgo.\n")
ANALISIS_P = ("# Análisis 1: algo\n\n> **Aprobado** por el usuario el 2026-10-02, en el turno 3.\n\n"
              "## Lo que se tiene que hacer\n\n"
              "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
              "| 1 | Hacer algo | 1 | [HU-001](../../HU-001-una-cosa/HU-001-una-cosa.md) |\n")
HU_MD = "# HU-001 · Una cosa\n\n| Campo | Valor |\n|---|---|\n| **Estado** | {estado} |\n"


class ElHallazgoCalculaSuEstado(Temporal):
    """`EP-023 · HU-003 · CP-005`. El estado del pendiente se calcula como lo hacía
    el módulo viejo: con el estándar como proyecto."""

    def setUp(self):
        super().setUp()
        self.escribir(HU_P + "/HU-001-una-cosa.md", HU_MD.format(estado="Lista"))
        self.escribir(EPICA_P + "/pendientes/110-algo-falla/pendiente.md", PENDIENTE_P.format(origen="algo"))
        self.escribir(EPICA_P + "/pendientes/110-algo-falla/analisis-1.md", ANALISIS_P)

    def resumen(self, fila):
        return self.escribir("historico-chat/resumenes/2026-10-02/sesion.md",
                             "# Sesión\n\n### H-1 · Algo falla\n\n| Campo | Valor |\n|---|---|\n"
                             "| Qué pasó | Algo. |\n| Por qué importa | Algo. |\n" + fila)

    def test_sin_pendiente(self):
        self.assertEqual([("H-1", "Algo falla", "abierto, sin pendiente")], Resumen.hallazgos(self.resumen("")))

    def test_anotado_y_se_retoma_por_el_ultimo_analisis(self):
        ruta = self.resumen("| Pendiente | [110](../../../%s/pendientes/110-algo-falla/pendiente.md) |\n" % EPICA_P)
        self.assertEqual("abierto, anotado", Resumen.hallazgos(ruta)[0][2])
        self.assertTrue(Resumen.retoma(ruta, "H-1").endswith("analisis-1.md"))
        self.assertEqual([("H-1", "Algo falla")], Resumen.sin_resolver(ruta))

    def test_resuelto_cuando_su_plan_se_cumplio(self):
        self.escribir(HU_P + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"))
        ruta = self.resumen("| Pendiente | [110](../../../%s/pendientes/110-algo-falla) |\n" % EPICA_P)
        self.assertEqual("resuelto", Resumen.hallazgos(ruta)[0][2])
        self.assertEqual([], Resumen.sin_resolver(ruta))

    def test_corregido_con_corrija_queda_resuelto(self):
        """`02·F8`, excepción: corregido con «Corrija» sin abrir análisis (2026-10-04)."""
        ruta = self.resumen("| Corregido con «Corrija» | El 2026-10-04: se corrigió el freno. |\n")
        self.assertEqual("resuelto", Resumen.hallazgos(ruta)[0][2])

    def test_el_resumen_viejo_se_lee_como_siempre(self):
        self.assertEqual("resuelto acá", Resumen.hallazgos(self.resumen("| Estado | resuelto acá |\n"))[0][2])


# ══ el aviso de vuelta (`EP-023 · HU-003 · fase C`) ═══════════════════════

class ElProyectoReportaYSeEntera(unittest.TestCase):
    """CP-002 y CP-003, sobre un estándar y un proyecto enlazados entre sí."""

    REPORTADO = EPICA_P + "/pendientes/110-algo-falla"
    RESUMEN_DIA = "historico-chat/resumenes/2026-10-02"
    SEGUIMIENTO = RESUMEN_DIA + "/pendientes/5-espera"
    SESION = ("# Sesión\n\n### H-1 · Algo del estándar falla\n\n| Campo | Valor |\n|---|---|\n"
              "| Qué pasó | Algo. |\n| Pendiente | [5](pendientes/5-espera/pendiente.md) |\n")

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.estandar = os.path.join(tmp.name, "estandar")
        self.proyecto = os.path.join(tmp.name, "proyecto")
        self.poner(self.estandar, HU_P + "/HU-001-una-cosa.md", HU_MD.format(estado="Lista"))
        self.poner(self.estandar, self.REPORTADO + "/pendiente.md", PENDIENTE_P.format(
            origen="[H-1 del proyecto](../../../../../../proyecto/%s/sesion.md)" % self.RESUMEN_DIA))
        self.poner(self.estandar, self.REPORTADO + "/analisis-1.md", ANALISIS_P)
        self.poner(self.proyecto, self.RESUMEN_DIA + "/sesion.md", self.SESION)
        self.poner(self.proyecto, self.SEGUIMIENTO + "/pendiente.md", PENDIENTE_P.format(
            origen="[110](../../../../../../estandar/%s/pendiente.md)" % self.REPORTADO))
        self.seguimiento = os.path.join(self.proyecto, *self.SEGUIMIENTO.split("/"))
        self.aviso = os.path.join(self.seguimiento, ARCHIVO_AVISO)

    @staticmethod
    def poner(raiz, relativa, texto):
        return escribir(os.path.join(raiz, *relativa.split("/")), texto)

    def cumplir(self, prueba=True):
        self.poner(self.estandar, HU_P + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"))
        if prueba is not None:
            # `02·F29`: Cimiento probó la corrección en una copia del proyecto.
            AvisoResuelto.anotar_prueba(os.path.join(self.estandar, *self.REPORTADO.split("/")), "2026-10-04",
                                        "una copia del proyecto", [("el caso", "reproducirlo", prueba)])

    def avisar(self):
        return AvisoResuelto(self.estandar).avisar("2026-10-04", "53.0.0")

    def test_cp002_1_con_el_plan_sin_cumplir_no_escribe(self):
        self.assertEqual(([], []), self.avisar())
        self.assertFalse(os.path.exists(self.aviso))

    def test_cp002_2_con_el_plan_cumplido_y_la_prueba_escribe_el_aviso(self):
        self.cumplir()
        escritos, sin_entregar = self.avisar()
        self.assertEqual([self.aviso], escritos)
        self.assertEqual([], sin_entregar)
        texto = leer(self.aviso)
        self.assertIn("**Comprobado:** 2026-10-04", texto)
        self.assertIn("| el caso | reproducirlo | Pasa |", texto)
        self.assertIn(self.REPORTADO, texto)

    def test_cp002_3_otra_vez_no_lo_duplica(self):
        self.cumplir()
        self.avisar()
        with io.open(self.aviso, "a", encoding="utf-8") as f:
            f.write("lo que escribió el proyecto\n")
        self.assertEqual(([], []), self.avisar())
        self.assertIn("lo que escribió el proyecto", leer(self.aviso))

    def test_cp002_4_con_el_enlace_roto_no_escribe_y_dice_cual(self):
        self.cumplir()
        self.poner(self.proyecto, self.RESUMEN_DIA + "/sesion.md", self.SESION.replace("5-espera", "6-no-existe"))
        escritos, sin_entregar = self.avisar()
        self.assertEqual([], escritos)
        self.assertEqual(1, len(sin_entregar))
        self.assertIn("H-1", sin_entregar[0][1])
        self.assertFalse(os.path.exists(self.aviso))

    def test_cp003_1_sin_prueba_en_el_proyecto_no_hay_aviso(self):
        self.cumplir(prueba=None)
        escritos, sin_entregar = self.avisar()
        self.assertEqual([], escritos)
        self.assertIn(PRUEBA, sin_entregar[0][1])
        self.assertEqual("abierto", Pendientes(self.proyecto).estado(self.seguimiento))

    def test_cp003_2_con_la_prueba_fallida_no_hay_aviso(self):
        self.cumplir(prueba=False)
        self.assertEqual([], self.avisar()[0])
        self.assertFalse(os.path.exists(self.aviso))

    def test_cp003_3_con_la_prueba_aprobada_el_seguimiento_cierra_al_llegar_el_aviso(self):
        self.cumplir()
        self.avisar()
        self.assertEqual("cerrado", Pendientes(self.proyecto).estado(self.seguimiento))
        self.assertTrue(AvisoResuelto.comprobado(self.seguimiento))

    def test_el_aviso_sigue_el_enlace_directo_al_seguimiento(self):
        """Análisis 1 del pendiente 110, acuerdo 5: el reporte enlaza su seguimiento."""
        seguimiento = os.path.dirname(self.poner(self.proyecto, "otro/pendientes/5-espera/pendiente.md", "# P\n"))
        reporte = self.poner(self.estandar, "pendientes/111-algo/pendiente.md",
                             "| | |\n|---|---|\n| **De dónde sale** | [su seguimiento](%s) |\n"
                             % os.path.join(seguimiento, "pendiente.md").replace("\\", "/"))
        self.assertEqual((seguimiento, ""), AvisoResuelto(self.estandar).seguimiento_de(os.path.dirname(reporte)))
        self.assertTrue(AvisoResuelto(self.estandar).reportado(os.path.dirname(reporte)))


# ══ las reglas que pide el mensaje (`EP-005·HU-023`) ════════════════════════

class LasReglasQuePideLaSolicitud(unittest.TestCase):
    """Elige por tareas: cada regla dice a qué tareas aplica, y las tareas del
    mensaje salen solo de la palabra clave de `01·C28` (`RN-07`)."""

    @classmethod
    def setUpClass(cls):
        cls.r = RecuperadorDeReglas(RAIZ)

    def elegir(self, mensaje, **extra):
        return self.r.elegir(mensaje, **extra)

    def test_un_saludo_trae_solo_las_de_todo_mensaje(self):
        elegidas, _descartadas, siempre = self.elegir("hola")
        self.assertEqual(elegidas, [])
        for id in ("C28", "ID8", "ID9", "ID11"):
            self.assertIn(id, siempre)

    def test_una_pregunta_con_palabras_genericas_no_trae_ninguna_tarea(self):
        for mensaje in ("ya detecta el nuevo cambio?", "eso funciona?", "qué quedó de ese trabajo"):
            self.assertEqual(self.elegir(mensaje)[0], [], f"«{mensaje}» trajo reglas de más")

    def test_lo_que_agrega_el_editor_no_cuenta_como_pedido(self):
        mensaje = ("<ide_opened_file>The user opened the file c:\\x\\HU-023\\"
                   "plan_trabajo.md in the IDE.</ide_opened_file>qué sigue?")
        elegidas, descartadas, _s = self.elegir(mensaje)
        self.assertEqual([], elegidas)
        self.assertEqual([], descartadas)

    def test_la_de_todo_mensaje_no_se_repite_entre_las_que_no_cupieron(self):
        _e, descartadas, siempre = self.elegir("Escriba el readme con la caja de reglas de redacción")
        self.assertFalse(set(descartadas) & set(siempre))

    def test_suba_a_git_trae_la_regla_del_control_de_versiones(self):
        self.assertIn("N2", [i for i, _ in self.elegir("suba a git")[0]])

    def test_un_pedido_de_redaccion_trae_las_reglas_de_redaccion(self):
        mensaje = "Escriba el readme con la caja de reglas de redacción"
        self.assertIn("ID8", [i for i, _ in self.elegir(mensaje)[0]])
        texto = self.r.como_texto(mensaje)
        for id in ("ID8", "ID9", "ID11", "ID12"):
            self.assertIn("00·" + id, texto, f"faltó {id}")

    def test_un_pendiente_trae_la_cadena_y_la_palabra_del_pedido(self):
        elegidas, descartadas, siempre = self.elegir("Registre el pendiente del H2")
        self.assertIn("F23", [i for i, _ in elegidas] + descartadas)
        self.assertIn("C28", siempre)

    def test_todo_lo_que_inyecta_cabe_en_el_tope(self):
        for mensaje in ("suba a git", "hola", "Registre el pendiente del H2",
                        "Escriba el readme con la caja de reglas de redacción", "Verifique las pruebas del validador"):
            peso = len(self.r.como_texto(mensaje).encode("utf-8"))
            self.assertLessEqual(peso, TOPE_REGLAS, f"«{mensaje}» pesa {peso} bytes")

    def con_opt_in(self, apagados=("21",)):
        raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, raiz, True)
        lineas = ["# Configuración", "", "## 5.1 Ajustes", ""]
        for capitulo in ("15", "16", "17", "18", "19", "21", "22"):
            lineas.append("- **Patrón opt-in `%s` (lo que sea):** %s" % (capitulo, "no" if capitulo in apagados else "sí"))
        escribir(os.path.join(raiz, "CLAUDE.md"), "\n".join(lineas))
        return raiz

    def test_no_ofrece_una_regla_de_un_capitulo_opt_in_apagado(self):
        """El 2026-09-16 «prueba» trajo `21·AU6` a un proyecto con el `21` en `no`."""
        idx = self.r.indice()
        elegidas, descartadas, siempre = self.elegir("Escriba el documento", proyecto=self.con_opt_in(("21",)))
        todas = [i for i, _ in elegidas] + descartadas
        self.assertFalse([i for i in todas if idx[i].capitulo == "21"])
        self.assertIn("ID8", todas + siempre, "se llevó también las que sí rigen")

    def test_si_el_opt_in_esta_encendido_la_regla_si_llega(self):
        idx = self.r.indice()
        elegidas, descartadas, _s = self.elegir("Escriba el documento", proyecto=self.con_opt_in(("15",)))
        self.assertTrue(any(idx[i].capitulo == "21" for i in [i for i, _ in elegidas] + descartadas),
                        "apagó un capítulo que el proyecto encendió")

    def test_la_cita_explicita_manda_sobre_el_opt_in_apagado(self):
        motivos = dict(self.elegir("qué dice 21·AU6?", proyecto=self.con_opt_in(("21",)))[0])
        self.assertIn("AU6", motivos)
        self.assertIn("apagado", motivos["AU6"])

    def test_sin_claude_md_no_apaga_nada(self):
        with tempfile.TemporaryDirectory() as vacio:
            self.assertEqual(RecuperadorDeReglas.opt_in_apagados(vacio), frozenset())
        self.assertEqual(RecuperadorDeReglas.opt_in_apagados(None), frozenset())

    def test_la_regla_citada_en_el_mensaje_llega_entera(self):
        texto = self.r.como_texto("qué dice 02·F24?")
        self.assertIn("F24", texto)
        self.assertIn("no lo toca", texto)

    def test_un_pedido_de_commit_trae_la_blindada_del_nucleo(self):
        self.assertIn("N2", [i for i, _ in self.elegir("Suba el commit")[0]])

    def test_borrar_en_produccion_trae_las_tres_que_lo_gobiernan(self):
        texto = "".join(leer(r) for r in MapaDeTareas(RAIZ).archivos_de("tocar-datos"))
        for id in ("N4", "N5", "N7"):
            self.assertIn("## " + id + " ·", texto, f"faltó {id} en la tarea de datos")

    def test_el_nucleo_va_primero(self):
        ids = [i for i, _ in self.elegir("Suba el commit")[0]]
        self.assertTrue(ids[0].startswith("N"), f"abrió con {ids[0]}")

    def test_lo_que_no_cabe_de_la_tarea_sale_nombrado(self):
        elegidas, descartadas, _s = self.elegir("Suba el commit")
        idx = self.r.indice()
        de_la_tarea = {r.id for r in MapaDeTareas(RAIZ).reglas_por_tarea()["tocar-git"]}
        vistas = {i for i, _ in elegidas} | set(descartadas)
        self.assertTrue(de_la_tarea <= vistas, f"se calló: {sorted(de_la_tarea - vistas)}")
        self.assertTrue(all(not idx[i].derogada for i in vistas))

    def test_ninguna_derogada_se_inyecta(self):
        idx = self.r.indice()
        for mensaje in ("escriba el plan de trabajo de la fase", "corra las pruebas y documente",
                        "haga commit de la migración"):
            for id, _ in self.elegir(mensaje)[0]:
                self.assertFalse(idx[id].derogada, f"«{mensaje}» inyectó la derogada {id}")

    def test_cada_regla_llega_con_su_motivo(self):
        for id, motivo in self.elegir("Suba el commit")[0]:
            self.assertTrue(motivo.strip(), f"{id} llegó sin motivo")

    def test_respeta_el_presupuesto_y_dice_que_dejo_afuera(self):
        mensaje = "Suba el commit. Verifique las pruebas"
        _e, descartadas, _s = self.elegir(mensaje, tope=6000)
        texto = self.r.como_texto(mensaje, tope=6000)
        self.assertLessEqual(len(texto.encode("utf-8")), 6000)
        self.assertTrue(descartadas, "recortó sin decir qué dejó afuera")
        for id in descartadas:
            self.assertIn(id, texto, f"{id} no cupo y no quedó nombrada")

    def test_lo_que_trae_cabe_en_el_presupuesto_de_un_turno(self):
        for mensaje in ("Suba el commit", "Suba el commit. Verifique las pruebas", "escriba el README del módulo"):
            kb = len(self.r.como_texto(mensaje).encode("utf-8")) / 1024
            self.assertLess(kb, 11, f"«{mensaje}» se pasó del tope: {kb:.1f} KB")

    def test_solo_la_palabra_clave_elige_la_tarea(self):
        for mensaje in ("es sencillo debe entender las reglas no lo que le parezca",
                        "como así que entendió que yo quería cambiar el estándar?", "termine la fase D"):
            self.assertEqual({}, self.r.tareas_del_mensaje(mensaje), f"«{mensaje}» eligió una tarea sin palabra clave")
        self.assertEqual({"tocar-git"}, set(self.r.tareas_del_mensaje("Suba")))
        self.assertEqual({"escribir-documento"}, set(self.r.tareas_del_mensaje("Escriba el plan del estándar")))
        self.assertEqual({"trabajar-cadena"}, set(self.r.tareas_del_mensaje("Apruebo los dos planes. Hágalo")))

    def test_la_palabra_clave_cuenta_solo_al_abrir_una_frase(self):
        self.assertEqual({}, self.r.tareas_del_mensaje("dijo que suba todo"))
        self.assertIn("tocar-git", self.r.tareas_del_mensaje("Listo. Suba todo"))

    def test_lo_que_no_cupo_dice_en_que_archivo_esta_completo(self):
        self.assertIn("reglas-por-tarea/correr-comando.md",
                      self.r.como_texto("Suba el commit. Verifique las pruebas", tope=6000))


class SinLaPalabraNoSeActua(unittest.TestCase):
    """`EP-005 · HU-023 · CA-09`: sin la palabra de `01·C28` el agente no actúa."""

    @classmethod
    def setUpClass(cls):
        cls.r = RecuperadorDeReglas(RAIZ)

    def test_sin_palabra_llega_el_aviso_con_la_lista(self):
        texto = self.r.como_texto("pero por qué no funciona")
        self.assertIn("NO ABRE CON UNA PALABRA DE `01·C28`", texto)
        for palabra in ("Pregunta", "Hágalo", "aplique", "Suba", "Pare"):
            self.assertIn("«%s»" % palabra, texto)
        self.assertNotIn("Read", texto)

    def test_con_palabra_llegan_las_reglas_y_no_el_aviso(self):
        texto = self.r.como_texto("Suba")
        self.assertNotIn("NO ABRE CON UNA PALABRA", texto)
        self.assertIn("N2", texto)

    def test_la_palabra_cuenta_con_tilde_o_sin_ella_y_al_abrir_una_frase(self):
        self.assertTrue(self.r.trae_palabra_clave("hagalo"))
        self.assertTrue(self.r.trae_palabra_clave("Listo. Continúe con eso"))
        self.assertFalse(self.r.trae_palabra_clave("ya lo quité, suba"))

    def test_lo_que_agrega_el_editor_no_cuenta_como_palabra(self):
        self.assertFalse(self.r.trae_palabra_clave("<ide_opened_file>Revise esto</ide_opened_file>ya"))

    def test_ningun_bloque_pide_leer_con_la_herramienta(self):
        self.assertNotIn("leerlas con Read", self.r.como_texto("Hágalo"))


# ══ el andamio (`09·12`, `EP-007 · HU-003`, `EP-004 · HU-005`) ══════════════

EPICA_REAL = "EP-005-automatismos-que-no-dependen-de-la-memoria"


def arbol_con_epica():
    """Una épica real del estándar y un índice de pendientes, en una carpeta temporal."""
    tmp = tempfile.mkdtemp()
    shutil.copytree(os.path.join(RAIZ, "documentacion", "epicas", EPICA_REAL),
                    os.path.join(tmp, "documentacion", "epicas", EPICA_REAL))
    escribir(os.path.join(tmp, "pendientes", "01-algo.md"), "# Pendiente · algo\n")
    escribir(os.path.join(tmp, "pendientes", "README.md"),
             "# Pendientes\n\n## Abiertos\n\n| # | P | Pendiente | Qué resuelve |\n|---|---|---|---|\n"
             "| 01 | **P2** | [algo](01-algo.md) | x |\n")
    return tmp


def fallas_de_enlaces(raiz, nombre):
    return [str(h) for h in EnlacesRotos(raiz).validar() if h.severidad == FALLA and nombre in str(h)]


class ElConsecutivoSeCalculaLeyendo(Temporal):

    def hu(self, *fases):
        hu = self.ruta("documentacion/epicas/EP-001-cuerpo/HU-003-nucleo")
        os.makedirs(hu)
        for f in fases:
            os.makedirs(os.path.join(hu, f))
        return Andamio(self.raiz).crear("EP-001-cuerpo", "HU-003-nucleo", "algo")[0]

    def test_la_primera_fase_es_A(self):
        self.assertIn("A-EP-001-HU-003-algo", self.hu())

    def test_con_A_la_siguiente_es_B(self):
        self.assertIn("B-EP-001-HU-003-algo", self.hu("A-EP-001-HU-003-lo-primero"))

    def test_con_un_hueco_no_lo_rellena(self):
        """Si existen `A` y `C` porque la `B` se renombró, contar daría `C` y pisaría una fase viva."""
        self.assertIn("B-EP-001-HU-003-algo", self.hu("A-EP-001-HU-003-una", "C-EP-001-HU-003-otra"))

    def test_despues_de_la_Z_sigue_AA(self):
        self.assertEqual("AA", Andamio.letras(27))
        self.assertEqual("Z", Andamio.letras(26))

    def test_el_numero_de_la_historia_se_lee_de_lo_que_hay(self):
        for hu in ("HU-001-a", "HU-003-c"):
            os.makedirs(self.ruta("documentacion/epicas/EP-009-x/" + hu))
        self.assertEqual("HU-004", Andamio.siguiente_hu(self.ruta("documentacion/epicas/EP-009-x")))


class ElAndamioNoEscribeContenido(Temporal):
    """**La mitad que decide si esto sirve o hace daño**: un documento que cumple
    sin decir nada es peor que no tenerlo."""

    def setUp(self):
        super().setUp()
        os.makedirs(self.ruta("documentacion/epicas/EP-001-cuerpo/HU-003-nucleo"))

    def crear(self):
        destino, _ = Andamio(self.raiz).crear("EP-001-cuerpo", "HU-003-nucleo", "algo", escribir=True)
        return {a: leer(os.path.join(destino, a)) for a, _ in DOCUMENTOS_DE_FASE
                if os.path.isfile(os.path.join(destino, a))}, destino

    def test_los_marcadores_de_contenido_quedan_intactos(self):
        textos, _ = self.crear()
        self.assertTrue(any("«" in t for t in textos.values()), "el andamio no puede dejar los documentos sin marcadores")

    def test_crea_los_cinco_documentos(self):
        self.assertEqual(5, len(self.crear()[0]))

    def test_sin_aplicar_no_crea_nada(self):
        destino, _ = Andamio(self.raiz).crear("EP-001-cuerpo", "HU-003-nucleo", "algo")
        self.assertFalse(os.path.isdir(destino))

    def test_sin_el_enlace_crudo_ni_el_marcador(self):
        """`EP-004 · HU-005 · CA-05`: las plantillas enlazan el estándar, también desde un proyecto."""
        textos, destino = self.crear()
        for nombre, texto in textos.items():
            with self.subTest(archivo=nombre):
                self.assertNotIn("](../../base/", texto)
                self.assertNotIn(MARCADOR_RAIZ, texto)
        hacia = os.path.relpath(RAIZ, destino).replace("\\", "/")
        for nombre in ("resultado_pruebas.md", "estado-fase.md"):
            self.assertIn("](%s/base/" % hacia, textos[nombre], nombre)

    def test_una_HU_que_no_existe_se_dice(self):
        with self.assertRaises(ValueError):
            Andamio(self.raiz).crear("EP-001-cuerpo", "HU-999-no-existe", "algo")

    def test_una_epica_fuera_del_molde_se_dice(self):
        os.makedirs(self.ruta("documentacion/epicas/epica-rara/HU-003-x"))
        with self.assertRaises(ValueError):
            Andamio(self.raiz).crear("epica-rara", "HU-003-x", "algo")


class ElEnlaceQueNoLlegaALaRaiz(unittest.TestCase):

    def test_cp_003_un_enlace_que_no_llega_a_la_raiz_no_se_toca(self):
        origen = os.path.join(RAIZ, "plantillas", "planes", "x.md")
        destino = os.path.join(RAIZ, "documentacion", "epicas", "EP", "HU", "A-EP-001-HU-001-p")
        texto = "ver [otra](../otra/cosa.md) y [raiz](../../base/x.md) y [fuera](../../../x.md)"
        salida = Andamio.reenlazar(texto, origen, destino)
        self.assertIn("](../otra/cosa.md)", salida)
        self.assertIn("](../../../../../base/x.md)", salida)
        self.assertIn("](../../../x.md)", salida)       # más allá de la raíz: no se sabe adónde iba


class LaHistoriaYElPendienteNacenConSuEsqueleto(unittest.TestCase):
    """`EP-007 · HU-003 · CA-04` y `EP-023 · HU-003 · CA-01 y CA-08`."""

    def setUp(self):
        self.tmp = arbol_con_epica()
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))
        self.epica_dir = os.path.join(self.tmp, "documentacion", "epicas", EPICA_REAL)
        self.andamio = Andamio(self.tmp)

    def test_cp_001_la_historia_nace_con_sus_indices(self):
        destino, _ = self.andamio.crear_hu(EPICA_REAL, "prueba-del-andamio", escribir=True)
        nombre = os.path.basename(destino)
        self.assertTrue(nombre.startswith("HU-0"))
        self.assertTrue(os.path.isfile(os.path.join(destino, nombre + ".md")))
        self.assertTrue(os.path.isfile(os.path.join(destino, "README.md")))
        epica = leer(os.path.join(self.epica_dir, "epica.md"))
        fila = [l for l in epica.splitlines() if l.startswith("| [%s](%s/%s.md)" % (nombre[:6], nombre, nombre))]
        self.assertEqual(1, len(fila))
        cabecera = [l for l in epica.splitlines() if l.startswith("| ID | Título")][0]
        self.assertEqual(cabecera.count("|"), fila[0].count("|"))
        self.assertIn("| [documentacion/epicas/%s/%s/](%s/) |" % (EPICA_REAL, nombre, nombre),
                      leer(os.path.join(self.epica_dir, "README.md")))

    def test_cp_004_no_escribe_contenido(self):
        destino, _ = self.andamio.crear_hu(EPICA_REAL, "prueba", escribir=True)
        nombre = os.path.basename(destino)
        plantilla = leer(os.path.join(RAIZ, PLANTILLA_HU))
        creada = leer(os.path.join(destino, nombre + ".md"))
        estructurales = 1 + plantilla.count(MARCADOR_RAIZ)   # «Épica padre» y la ruta
        self.assertEqual(plantilla.count("«") - estructurales, creada.count("«"))
        self.assertNotIn("HU-000", creada)

    def test_cp_005_los_validadores_no_reclaman_nada(self):
        destino, _ = self.andamio.crear_hu(EPICA_REAL, "prueba", escribir=True)
        self.assertEqual([], fallas_de_enlaces(self.tmp, os.path.basename(destino)))

    def test_cp_003_con_su_hu_nace_en_pendientes_de_la_hu(self):
        hu = "%s/HU-008-enganche-del-resumen" % EPICA_REAL
        antes = leer(os.path.join(self.tmp, "pendientes", "README.md"))
        numero = Pendientes(self.tmp).proximo_libre()
        destino, tocados = self.andamio.crear_pendiente("prueba", hu, escribir=True)
        self.assertEqual(os.path.join(self.tmp, "documentacion", "epicas", EPICA_REAL, "HU-008-enganche-del-resumen",
                                      "pendientes", "%03d-prueba" % numero, "pendiente.md"), destino)
        texto = leer(destino)
        self.assertIn("**De dónde sale**", texto)
        self.assertNotIn("Historia de usuario", texto)
        self.assertEqual([destino], tocados)
        self.assertEqual(antes, leer(os.path.join(self.tmp, "pendientes", "README.md")))
        self.assertEqual(numero + 1, Pendientes(self.tmp).proximo_libre())

    def test_sin_aplicar_no_escribe(self):
        destino, _ = self.andamio.crear_pendiente("prueba", "%s/HU-008-enganche-del-resumen" % EPICA_REAL)
        self.assertFalse(os.path.exists(destino))

    def test_sin_dueno_nace_en_el_resumen_del_dia(self):
        numero = Pendientes(self.tmp).proximo_libre()
        destino, _ = self.andamio.crear_pendiente("prueba-sin-historia", "", escribir=True, hoy=datetime.date(2026, 10, 2))
        self.assertEqual(os.path.join(self.tmp, "historico-chat", "resumenes", "2026-10-02", "pendientes",
                                      "%03d-prueba-sin-historia" % numero, "pendiente.md"), destino)

    def test_una_historia_que_no_existe_sigue_fallando(self):
        with self.assertRaises(ValueError) as e:
            self.andamio.crear_pendiente("prueba", "%s/HU-999-no-existe" % EPICA_REAL, escribir=True)
        self.assertIn("no existe la historia", str(e.exception))

    def test_el_pendiente_nuevo_pasa_la_validacion(self):
        self.andamio.crear_pendiente("prueba-sin-historia", "", escribir=True)
        fallas = [h for h in NumeracionDePendientes(self.tmp).validar()
                  if h.severidad == FALLA and "prueba-sin-historia" in str(h)]
        self.assertEqual([], fallas)

    def correr(self, *argumentos):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            codigo = andamio_main(list(argumentos) + ["--raiz", self.tmp])
        return codigo, salida.getvalue()

    def test_sin_hu_por_la_linea_de_ordenes(self):
        codigo, salida = self.correr("pendiente", "prueba-sin-historia")
        self.assertEqual(0, codigo)
        self.assertIn("simulado", salida)

    def test_el_modo_de_fase_sigue_igual(self):
        codigo, salida = self.correr(EPICA_REAL, "HU-008-enganche-del-resumen", "prueba")
        self.assertEqual(0, codigo)
        self.assertIn("simulado", salida)
        self.assertIn("plan_trabajo.md", salida)


class LasHerramientasSirvenDesdeUnProyecto(Temporal):
    """Pendientes 110 y 114: el andamio arma con las plantillas del estándar."""

    def rotos(self, archivo):
        texto = leer(archivo)
        enlaces = [e for e in re.findall(r"\]\(([^)]+)\)", texto) if not e.startswith("http") and "«" not in e]
        return [e for e in enlaces if not os.path.exists(os.path.join(os.path.dirname(archivo), e.split("#")[0]))]

    def test_el_andamio_crea_la_historia_con_las_plantillas_del_estandar(self):
        self.escribir("documentacion/epicas/EP-001-algo/epica.md", "# EP-001 · Algo\n\n## 9. Historias\n\n| a |\n|---|\n")
        destino, _ = Andamio(self.raiz).crear_hu("EP-001-algo", "una-cosa", escribir=True)
        hu = os.path.join(destino, os.path.basename(destino) + ".md")
        self.assertTrue(os.path.isfile(hu))
        self.assertEqual([], self.rotos(hu))

    def test_el_pendiente_puede_vivir_en_una_epica(self):
        self.escribir("documentacion/epicas/EP-001-algo/epica.md", "# EP-001 · Algo\n")
        destino, _ = Andamio(self.raiz).crear_pendiente("algo-falla", "EP-001-algo", escribir=True)
        self.assertIn(os.path.join("EP-001-algo", "pendientes"), destino)
        self.assertEqual([], self.rotos(destino))

    def test_el_indice_escrito_como_lista_recibe_la_historia(self):
        self.escribir("documentacion/epicas/EP-001-algo/epica.md", "# EP-001 · Algo\n\n## 9. Historias\n\n| a |\n|---|\n")
        readme = self.escribir("documentacion/epicas/EP-001-algo/README.md", "# EP-001\n\n- [epica.md](epica.md) — la épica.\n")
        Andamio(self.raiz).crear_hu("EP-001-algo", "una-cosa", escribir=True)
        self.assertIn("- [", leer(readme).splitlines()[-1])


# ══ cerrar un pendiente (pendientes 36, 54, 61 y 71) ═══════════════════════

class CerrarArrastraLasCitas(unittest.TestCase):
    """`cerrar` no busca texto: resuelve cada enlace contra el disco y compara rutas
    absolutas. Se fijan las dos direcciones y las tres trampas que costaron una
    corrida cada una."""

    def repo(self, archivos):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for rel, texto in archivos.items():
            escribir(os.path.join(tmp.name, *rel.split("/")), texto)
        return tmp.name

    def leer(self, raiz, rel):
        return leer(os.path.join(raiz, *rel.split("/")))

    def cerrar(self, raiz, numero="07", como="algo-resuelto", escribir_=True):
        return CerradorDePendientes(raiz).cerrar(numero, como, escribir=escribir_)

    def test_la_cita_desde_lejos_se_reapunta(self):
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n",
                          "documentacion/epicas/EP-1/HU-1/A-1/plan.md":
                              "Ver [el 07](../../../../../pendientes/07-algo.md).\n"})
        self.cerrar(raiz)
        self.assertIn("../../../../../pendientes/hecho/algo-resuelto.md",
                      self.leer(raiz, "documentacion/epicas/EP-1/HU-1/A-1/plan.md"))
        self.assertEqual([], EnlacesRotos(raiz).validar())

    def test_la_cita_desde_la_misma_carpeta_tambien(self):
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n", "pendientes/README.md": "- [07](07-algo.md)\n"})
        self.cerrar(raiz)
        self.assertIn("hecho/algo-resuelto.md", self.leer(raiz, "pendientes/README.md"))

    def test_el_ancla_se_conserva(self):
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n\n## El problema\n",
                          "notas/n.md": "Ver [el 07](../pendientes/07-algo.md#el-problema).\n"})
        self.cerrar(raiz)
        self.assertIn("algo-resuelto.md#el-problema", self.leer(raiz, "notas/n.md"))

    def test_el_enlace_con_espacios_tambien_se_arrastra(self):
        raiz = self.repo({"pendientes/07-un algo.md": "# Algo\n",
                          "notas/n.md": "Ver [el 07](../pendientes/07-un%20algo.md).\n"})
        self.cerrar(raiz)
        self.assertIn("hecho/algo-resuelto.md", self.leer(raiz, "notas/n.md"))

    def test_lo_que_el_archivo_citaba_se_recalcula(self):
        raiz = self.repo({"base/x.md": "# X\n", "pendientes/07-algo.md": "Ver [x](../base/x.md).\n"})
        self.cerrar(raiz)
        self.assertIn("../../base/x.md", self.leer(raiz, "pendientes/hecho/algo-resuelto.md"))
        self.assertEqual([], EnlacesRotos(raiz).validar())

    def test_el_archivo_que_se_cita_a_si_mismo_no_se_enreda(self):
        raiz = self.repo({"pendientes/07-algo.md": "Yo soy [el 07](07-algo.md).\n"})
        self.cerrar(raiz)
        self.assertIn("(algo-resuelto.md)", self.leer(raiz, "pendientes/hecho/algo-resuelto.md"))

    def test_no_toca_lo_externo_ni_los_anclajes_sueltos(self):
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n",
                          "notas/n.md": "[fuera](https://ejemplo.org/07-algo.md) y [acá](#07-algo).\n"})
        self.cerrar(raiz)
        texto = self.leer(raiz, "notas/n.md")
        self.assertIn("https://ejemplo.org/07-algo.md", texto)
        self.assertIn("(#07-algo)", texto)

    def test_no_confunde_a_otro_pendiente_con_numero_parecido(self):
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n", "pendientes/70-otro.md": "# Otro\n",
                          "notas/n.md": "[70](../pendientes/70-otro.md)\n"})
        self.cerrar(raiz)
        self.assertIn("../pendientes/70-otro.md", self.leer(raiz, "notas/n.md"))

    def test_simular_no_escribe_nada(self):
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n", "notas/n.md": "[07](../pendientes/07-algo.md)\n"})
        _o, _d, tocados = self.cerrar(raiz, escribir_=False)
        self.assertTrue(tocados, "no dijo qué haría")
        self.assertTrue(os.path.isfile(os.path.join(raiz, "pendientes", "07-algo.md")), "movió el archivo sin --aplicar")
        self.assertIn("07-algo.md", self.leer(raiz, "notas/n.md"))

    def test_no_pisa_un_nombre_que_ya_existe(self):
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n", "pendientes/hecho/algo-resuelto.md": "# Ya estaba\n"})
        with self.assertRaises(SystemExit):
            self.cerrar(raiz)
        self.assertIn("Ya estaba", self.leer(raiz, "pendientes/hecho/algo-resuelto.md"))

    def test_avisa_si_el_numero_no_existe(self):
        with self.assertRaises(SystemExit):
            self.cerrar(self.repo({"pendientes/07-algo.md": "# Algo\n"}), "99", "lo-que-sea")

    def test_avisa_si_el_numero_esta_repetido(self):
        with self.assertRaises(SystemExit):
            self.cerrar(self.repo({"pendientes/07-uno.md": "# Uno\n", "pendientes/07-otro.md": "# Otro\n"}),
                        "07", "lo-que-sea")

    def test_el_destino_con_espacio_sale_codificado(self):
        """Pendiente 71: el enlace de salida hacia una ruta con espacio conserva `%20`."""
        raiz = self.repo({"pendientes/07-algo.md": "# Algo\n\nVer [x](../con%20espacio/x.md).\n",
                          "con espacio/x.md": "# x\n"})
        self.cerrar(raiz)
        texto = self.leer(raiz, "pendientes/hecho/algo-resuelto.md")
        self.assertIn("../../con%20espacio/x.md", texto)
        self.assertNotIn("con espacio/x.md)", texto)
        self.assertEqual([], EnlacesRotos(raiz).validar())

    def test_la_fila_del_indice_queda_en_forma_de_hecho(self):
        """`EP-005 · HU-003 · fase C · CP-005`."""
        raiz = self.repo({"pendientes/99-p.md": "# Pendiente · p\n",
                          "pendientes/README.md": "# Pendientes\n\n| # | P | Pendiente | Qué resuelve |\n|---|---|---|---|\n"
                                                  "| 99 | **P2** | [t](99-p.md) | q |\n"})
        self.cerrar(raiz, 99, "p")
        self.assertIn("| ~~99~~ | — | **hecho** → [t](hecho/p.md) | q |", self.leer(raiz, "pendientes/README.md"))
        self.assertTrue(os.path.isfile(os.path.join(raiz, "pendientes", "hecho", "p.md")))


FICHA = """# Pendiente · Algo que se rompió

| | |
|---|---|
| **Proyecto de origen** | **%s** · `%s` |
| **A quién avisar al cerrar** | %s |

## El problema

Algo.
"""


class ElAvisoLlegaAQuienLoReporto(unittest.TestCase):
    """Pendiente 36 y `61`: escribe **un archivo de pendiente y nada más**, no
    duplica, no inventa una carpeta, y dice a quién no le llegó."""

    def proyectos(self, cuantos=3, con_backlog=True):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        salida = []
        for i in range(1, cuantos + 1):
            ruta = os.path.join(tmp.name, "proy%d" % i)
            os.makedirs(os.path.join(ruta, "pendientes") if con_backlog else ruta)
            salida.append(("Proyecto %d" % i, ruta))
        return salida

    def avisar(self, texto, proyectos, escribir_=True, raiz="/raiz"):
        return CerradorDePendientes(raiz).avisar(texto, "/raiz/pendientes/hecho/algo.md", "9.9.9",
                                                 proyectos, "2026-01-02", escribir_)

    def test_llega_al_de_origen_y_a_nadie_mas(self):
        proyectos = self.proyectos()
        escritos = self.avisar(FICHA % ("Proyecto 2", proyectos[1][1], "al de origen"), proyectos)[0]
        self.assertEqual(1, len(escritos))
        self.assertEqual("Proyecto 2", escritos[0][0])
        self.assertTrue(os.path.isfile(escritos[0][1]))
        for nombre, ruta in (proyectos[0], proyectos[2]):
            self.assertEqual([], os.listdir(os.path.join(ruta, "pendientes")), f"{nombre} recibió un aviso que no era suyo")

    def test_si_dice_todos_llega_a_todos(self):
        proyectos = self.proyectos()
        texto = FICHA % ("Proyecto 2", proyectos[1][1], "a **todos** los proyectos instalados")
        self.assertEqual(3, len(self.avisar(texto, proyectos)[0]))

    def test_no_duplica_si_se_cierra_dos_veces(self):
        proyectos = self.proyectos()
        texto = FICHA % ("Proyecto 1", proyectos[0][1], "al de origen")
        self.avisar(texto, proyectos)
        self.assertEqual([], self.avisar(texto, proyectos)[0], "el segundo cierre escribió otro aviso")
        self.assertEqual(1, len(os.listdir(os.path.join(proyectos[0][1], "pendientes"))))

    def test_el_aviso_dice_que_version_lo_trae(self):
        proyectos = self.proyectos()
        _n, archivo = self.avisar(FICHA % ("Proyecto 1", proyectos[0][1], "al de origen"), proyectos)[0][0]
        contenido = leer(archivo)
        self.assertIn("9.9.9", contenido)
        self.assertIn("Algo que se rompió", contenido)
        self.assertIn("comprob", contenido.lower(), "no dice que hay que comprobarlo antes de cerrar")

    def test_no_escribe_nada_fuera_de_la_carpeta_de_pendientes(self):
        proyectos = self.proyectos()
        antes = set(os.listdir(proyectos[0][1]))
        self.avisar(FICHA % ("Proyecto 1", proyectos[0][1], "al de origen"), proyectos)
        self.assertEqual(antes, set(os.listdir(proyectos[0][1])), "creó algo fuera de `pendientes/`")

    def test_sin_proyecto_de_origen_no_avisa_a_nadie(self):
        self.assertEqual([], self.avisar("# Pendiente\n\nSin ficha.\n", self.proyectos())[0])

    def test_el_estandar_no_se_avisa_a_si_mismo(self):
        """El registro escribe la unidad en minúscula y el comando en mayúscula:
        comparando el texto tal cual, el estándar se mandaba un aviso a sí mismo."""
        proyectos = self.proyectos()
        raiz = proyectos[0][1]
        texto = FICHA % ("Proyecto 1", raiz, "a **todos** los proyectos")
        for escrita in (raiz, raiz.upper(), os.path.join(raiz, os.pardir, os.path.basename(raiz))):
            with self.subTest(ruta=escrita):
                if os.path.normcase(escrita) != os.path.normcase(raiz) and os.path.normcase("A") != os.path.normcase("a"):
                    continue            # sistema que distingue mayúsculas
                self.assertEqual([], CerradorDePendientes(raiz).avisar(
                    texto, "/x/hecho/algo.md", "9.9.9", [(proyectos[0][0], escrita)], "2026-01-02", True)[0])
        self.assertEqual([], os.listdir(os.path.join(raiz, "pendientes")))

    def test_el_nombre_del_aviso_no_lleva_dos_veces_la_extension(self):
        proyectos = self.proyectos()
        _n, archivo = self.avisar(FICHA % ("Proyecto 1", proyectos[0][1], "al de origen"), proyectos)[0][0]
        self.assertTrue(archivo.endswith(".md"))
        self.assertFalse(archivo.endswith(".md.md"), archivo)

    def test_simular_no_escribe(self):
        proyectos = self.proyectos()
        escritos = self.avisar(FICHA % ("Proyecto 1", proyectos[0][1], "al de origen"), proyectos, escribir_=False)[0]
        self.assertEqual(1, len(escritos), "no dijo a quién avisaría")
        self.assertEqual([], os.listdir(os.path.join(proyectos[0][1], "pendientes")), "escribió sin --aplicar")

    def test_sin_carpeta_no_se_escribe_y_se_dice_a_quien_no_llego(self):
        escritos, sin_entregar = self.avisar(FICHA % ("Proyecto 1", "C:/x", "todos"), self.proyectos(1, False))
        self.assertEqual([], escritos)
        self.assertEqual(1, len(sin_entregar))
        self.assertEqual("Proyecto 1", sin_entregar[0][0])
        self.assertIn("pendientes", sin_entregar[0][1])

    def test_con_carpeta_no_hay_nada_que_reportar(self):
        escritos, sin_entregar = self.avisar(FICHA % ("Proyecto 1", "C:/x", "todos"), self.proyectos(1))
        self.assertEqual((1, []), (len(escritos), sin_entregar))

    def test_el_proyecto_que_ya_no_existe_tambien_se_dice(self):
        _e, sin_entregar = self.avisar(FICHA % ("Proyecto 1", "C:/x", "todos"), [("Fantasma", "/no/existe/por/aca")])
        self.assertEqual(1, len(sin_entregar))
        self.assertIn("no existe", sin_entregar[0][1])

    def test_los_dos_lados_salen_en_la_misma_vuelta(self):
        con, sin = self.proyectos(1), self.proyectos(1, False)
        escritos, sin_entregar = self.avisar(FICHA % ("Proyecto 1", "C:/x", "todos"), con + [("Proyecto 2", sin[0][1])])
        self.assertEqual((1, 1), (len(escritos), len(sin_entregar)))


if __name__ == "__main__":
    unittest.main()
