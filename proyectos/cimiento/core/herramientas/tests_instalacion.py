"""El grupo «instalación», como clases: el instalador, el checklist, la versión y
los registros de versión, el guardián de la versión, las herramientas del
ecosistema, los recuerdos y la revisión de arranque.

Son las pruebas de `validadores/pruebas.py` (`Version`, `Herramientas`,
`Instalador`, `Recuerdos`, `Checklist`, `Versiones`, `DerogacionSinBorrar`,
`NumeroDeVersion`, `RutasLargas`, `MostrarAntesDeHacer`, `EstructuraDeCarpetas`,
`GenerarLosAutomatismos`, `NoPisarLoEscrito`, `IndiceDeLosRecuerdos`,
`ElRecuerdoTraeSusTresPartes`, `ElAlmacenLocalQuedaVacio` y las que miran la
lista de enganches) y de `validadores/tests/` que cubren estos módulos, pasadas
a sus clases. Lo que antes corría `instalar.py` como orden del sistema ahora
llama a `main()` en el mismo proceso.
"""
import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from core.comun import AVISO, FALLA, Proyecto
from core.enganches.recuerdos import Recuerdos
from core.enganches.sesion import ArranqueDeSesion
from core.herramientas import instalar as modulo_instalar
from core.herramientas.instalar import (CARPETAS_BASE, CI_GITHUB, CI_GITLAB, CONFIG_AGENTE, HOOKS,
                                        HOOKS_CLAUDE, IGNORADOS, MARCA, PLANTILLA_PRE_COMMIT,
                                        PLANTILLA_PRE_PUSH, Instalador, Plantillas, main)
from core.validadores.checklist import Checklist
from core.validadores.guardian_version import VersionDelCambio
from core.validadores.herramientas import HerramientaDelEcosistema
from core.validadores.secretos import SecretosEnElCodigo
from core.validadores.version import VersionDelEstandar
from core.validadores.versiones import (COMPONENTES, POR_ID, SIN_SELLO, VIEJO, CARPETA,
                                        DocumentosHeredados, RegistroDeVersiones, Sello)

ESTANDAR = Proyecto.estandar()
ADAPTADOR = os.path.join(ESTANDAR, "adaptadores", "claude-code")
MARCADOR_CRUDO = "«RUTA-ESTANDAR»"


def leer(ruta):
    try:
        with io.open(ruta, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def callado(funcion, *args, **kwargs):
    """Corre sin ensuciar la salida de la suite."""
    with contextlib.redirect_stdout(io.StringIO()):
        return funcion(*args, **kwargs)


def claude_md_completo(proyecto="demo"):
    """La plantilla central ya rellenada, como la deja el instalador."""
    instalador = Instalador()
    return instalador.rellenar(leer(POR_ID["claude-md"].ruta_plantilla()), instalador.rellenos(proyecto))


def carpeta(caso):
    tmp = tempfile.TemporaryDirectory()
    caso.addCleanup(tmp.cleanup)
    return tmp.name


@contextlib.contextmanager
def estandar_temporal():
    """Copia desechable del estándar: las plantillas y `VERSION` se editan en la
    copia, y el registro de proyectos que escribe el instalador cae ahí."""
    copia = tempfile.mkdtemp(prefix="cimiento-estandar-")
    shutil.copytree(os.path.join(ESTANDAR, "plantillas"), os.path.join(copia, "plantillas"))
    shutil.copy2(os.path.join(ESTANDAR, "VERSION"), os.path.join(copia, "VERSION"))
    try:
        yield copia
    finally:
        shutil.rmtree(copia, ignore_errors=True)


class Corrida:
    def __init__(self, codigo, salida):
        self.returncode, self.stdout, self.stderr = codigo, salida, ""


# ── version ──────────────────────────────────────────────────────────────

class Version(unittest.TestCase):
    """Pendiente 04 · desfase de versión. Núcleo puro."""

    def test_extrae_la_version_adoptada(self):
        txt = "- **Versión del estándar adoptada:** `1.2.0` · sellada `2026-08-06`"
        self.assertEqual(VersionDelEstandar.extraer_adoptada(txt), "1.2.0")

    def test_placeholder_sin_llenar_no_matchea(self):
        self.assertIsNone(VersionDelEstandar.extraer_adoptada("adoptada: `«X.Y.Z»`"))

    def test_al_dia_no_avisa(self):
        self.assertIsNone(VersionDelEstandar.comparar("1.0.0", "1.0.0"))
        self.assertIsNone(VersionDelEstandar.comparar("1.1.0", "1.0.0"))

    def test_por_detras_avisa(self):
        m = VersionDelEstandar.comparar("1.0.0", "1.2.0")
        self.assertIsNotNone(m)
        self.assertIn("1.2.0", m)

    def test_sin_declarar_avisa(self):
        self.assertIsNotNone(VersionDelEstandar.comparar(None, "1.0.0"))

    def test_estandar_sin_version_no_opina(self):
        self.assertIsNone(VersionDelEstandar.comparar(None, None))


class _VersionFija(VersionDelEstandar):
    """Un estándar de mentira: qué versiones publica y cuál es la vigente."""
    nombre = ""
    publicadas = {"1.0.0", "2.0.0", "3.0.0"}
    vigente_fija = "3.0.0"

    def versiones_publicadas(self):
        return self.publicadas

    def version_estandar(self):
        return self.vigente_fija


class LaVersionAdoptadaSeComprueba(unittest.TestCase):
    """Pendiente 82 · la versión declarada se comprueba contra algo. La mitad de
    los casos son de lo que NO debe fallar."""

    def setUp(self):
        self.tmp = carpeta(self)
        self.clase = type("V", (_VersionFija,), {"nombre": ""})

    def proyecto(self, adoptada, adopciones=()):
        escribir(os.path.join(self.tmp, "CLAUDE.md"),
                 "# Proyecto\n\n- **Versión del estándar adoptada:** `%s` · sellada `2026-08-20`.\n" % adoptada)
        for v in adopciones:
            escribir(os.path.join(self.tmp, "documentacion", "versiones", "2026-08-20-%s.md" % v),
                     "# Actualización a %s\n" % v)
        return self.clase(self.tmp).validar()

    def fallas(self, hallazgos):
        return [h for h in hallazgos if h.severidad == FALLA]

    def test_una_version_que_no_existe_falla(self):
        h = self.fallas(self.proyecto("99.9.9"))
        self.assertEqual(1, len(h))
        self.assertIn("no existe en el registro", h[0].mensaje)

    def test_la_version_inventada_ya_no_apaga_el_aviso(self):
        self.assertTrue(self.fallas(self.proyecto("99.9.9")))

    def test_declarada_y_ultimo_registro_que_difieren_falla(self):
        h = self.fallas(self.proyecto("1.0.0", adopciones=["1.0.0", "2.0.0"]))
        self.assertEqual(1, len(h))
        self.assertIn("1.0.0", h[0].mensaje)
        self.assertIn("2.0.0", h[0].mensaje)

    def test_un_proyecto_al_dia_no_falla(self):
        self.assertEqual([], self.fallas(self.proyecto("3.0.0")))

    def test_un_proyecto_atrasado_avisa_y_no_falla(self):
        hallazgos = self.proyecto("2.0.0")
        self.assertEqual([], self.fallas(hallazgos))
        self.assertEqual([AVISO], [h.severidad for h in hallazgos])

    def test_declarada_y_registro_que_coinciden_no_falla(self):
        self.assertEqual([], self.fallas(self.proyecto("2.0.0", adopciones=["1.0.0", "2.0.0"])))

    def test_sin_registro_de_cambios_no_se_afirma_nada(self):
        self.clase.publicadas = set()
        self.assertEqual([], self.fallas(self.proyecto("99.9.9")))

    def test_un_proyecto_que_no_declara_version_avisa_como_antes(self):
        escribir(os.path.join(self.tmp, "CLAUDE.md"), "# Proyecto sin versión declarada\n")
        hallazgos = self.clase(self.tmp).validar()
        self.assertEqual([], self.fallas(hallazgos))
        self.assertEqual(1, len(hallazgos))

    def test_el_ultimo_registro_es_el_mayor_y_no_el_ultimo_alfabetico(self):
        self.clase.publicadas = {"9.0.0", "10.0.0"}
        self.clase.vigente_fija = "10.0.0"
        h = self.fallas(self.proyecto("9.0.0", adopciones=["9.0.0", "10.0.0"]))
        self.assertEqual(1, len(h))
        self.assertIn("10.0.0", h[0].mensaje)


REGISTRO_DE_CAMBIOS = """# Cambios del estándar

## 3.0.0 — 2026-08-20

**MAYOR** ⚠ obliga a migrar.

**Los planes ahora declaran su origen.** Antes no se sabía de dónde salía cada fase.

## 2.1.0 — 2026-08-19

**MENOR** (algo aditivo).

**Se puede saber qué reglas nadie revisó.** Una orden las ordena por antigüedad.

## 2.0.0 — 2026-08-18

**MAYOR** ⚠ obliga a migrar.

**El registro se escribe para quien no siguió el cambio.** Antes abría con jerga.
"""


class ElTramoDelRegistro(unittest.TestCase):
    """Pendiente 83 · qué versiones separan a las dos, y cómo se cuenta."""

    def setUp(self):
        self.tmp = carpeta(self)
        escribir(os.path.join(self.tmp, "CHANGELOG.md"), REGISTRO_DE_CAMBIOS)
        self.version = VersionDelEstandar(self.tmp, estandar=self.tmp)

    def test_el_tramo_son_las_de_en_medio_y_la_de_llegada(self):
        self.assertEqual(["2.1.0", "3.0.0"], sorted(v for v, _, _ in self.version.tramo("2.0.0", "3.0.0")))

    def test_la_version_adoptada_no_entra_en_su_propio_tramo(self):
        self.assertNotIn("2.0.0", [v for v, _, _ in self.version.tramo("2.0.0", "3.0.0")])

    def test_un_proyecto_al_dia_tiene_tramo_vacio(self):
        self.assertEqual([], self.version.tramo("3.0.0", "3.0.0"))

    def test_cada_entrada_trae_su_tipo_y_su_titulo(self):
        entradas = {v: (tipo, titulo) for v, tipo, titulo in self.version.tramo("2.0.0", "3.0.0")}
        self.assertEqual("MAYOR", entradas["3.0.0"][0])
        self.assertIn("declaran su origen", entradas["3.0.0"][1])

    def test_sin_registro_no_se_inventa_un_tramo(self):
        self.assertEqual([], self.version.tramo("1.0.0", "3.0.0", carpeta(self)))

    def test_lo_que_obliga_a_migrar_va_primero(self):
        linea = VersionDelEstandar.resumen_del_tramo(self.version.tramo("2.0.0", "3.0.0"))
        self.assertIn("obliga a migrar", linea)
        self.assertLess(linea.index("obliga a migrar"), linea.index("Lo último"))

    def test_sin_tramo_no_hay_nada_que_resumir(self):
        self.assertEqual("", VersionDelEstandar.resumen_del_tramo(self.version.tramo("2.1.0", "2.1.0")))


class ElAvisoLlegaAlAbrir(unittest.TestCase):
    """Pendiente 83 · el arranque de sesión pregunta por la versión."""

    def setUp(self):
        self.tmp = carpeta(self)
        os.makedirs(os.path.join(self.tmp, "proyectos"))
        escribir(os.path.join(self.tmp, "CLAUDE.md"),
                 "# Proyecto\n\n- **Versión del estándar adoptada:** `2.0.0` · sellada `2026-08-20`.\n")

    def test_el_arranque_pregunta_por_la_version(self):
        llamadas = []
        with mock.patch.object(VersionDelEstandar, "validar", lambda yo: llamadas.append(yo) or []):
            ArranqueDeSesion(self.tmp, estandar=ESTANDAR).revisar()
        self.assertEqual(1, len(llamadas))

    def test_lo_que_devuelve_la_version_llega_al_arranque(self):
        marca = object()
        with mock.patch.object(VersionDelEstandar, "validar", lambda yo: [marca]):
            salida = ArranqueDeSesion(self.tmp, estandar=ESTANDAR).revisar()
        self.assertIn(marca, salida)


def _f22(hallazgos):
    return [h for h in hallazgos if "F22" in str(h)]


class LaDerogacionSinAdoptarDetieneLaFase(unittest.TestCase):
    """`02·F22`, contra las derogaciones reales del estándar. El caso que pasaba
    por `flujo.py` queda en su suite: `flujo` no es de este grupo."""

    def setUp(self):
        self.proyecto = os.path.join(carpeta(self), "proyecto")
        os.makedirs(self.proyecto)
        self.declarar("3.0.0")

    def declarar(self, adoptada):
        texto = "# Proyecto de prueba\n"
        if adoptada:
            texto += f"\nVersión del estándar adoptada: {adoptada}\n"
        escribir(os.path.join(self.proyecto, "CLAUDE.md"), texto)

    def test_cp_001_el_proyecto_atrasado_falla_y_nombra_cada_regla(self):
        version = VersionDelEstandar(self.proyecto)
        derogadas = version.derogaciones()
        self.assertTrue(derogadas, "sin derogaciones el caso no comprobaría nada")
        hallazgos = _f22(version.validar_fase())
        self.assertEqual(len(hallazgos), 1)
        texto = str(hallazgos[0])
        self.assertIn(derogadas[0][1], texto)
        self.assertIn(derogadas[0][0], texto)
        self.assertIn(derogadas[0][2].split(" y ")[0], texto)
        self.declarar(version.version_estandar())
        self.assertEqual(_f22(version.validar_fase()), [])

    def test_cp_002_lo_ya_adoptado_no_se_cuenta(self):
        inventadas = [("2.0.0", "X1", "X9"), ("5.0.0", "X2", "X8"), ("7.0.0", "X3", "X7")]
        sin_adoptar = VersionDelEstandar.sin_adoptar
        self.assertEqual(len(sin_adoptar("1.0.0", "7.0.0", inventadas)), 3)
        self.assertEqual([d[1] for d in sin_adoptar("2.0.0", "7.0.0", inventadas)], ["X2", "X3"])
        self.assertEqual(sin_adoptar("7.0.0", "7.0.0", inventadas), [])
        self.assertEqual(sin_adoptar(None, "7.0.0", inventadas), [])

    def test_cp_004_los_limites_callan_en_vez_de_romper(self):
        antes = sorted(os.listdir(self.proyecto))
        os.remove(os.path.join(self.proyecto, "CLAUDE.md"))
        self.assertEqual(VersionDelEstandar(self.proyecto).validar_fase(), [])
        self.declarar(None)
        self.assertEqual(_f22(VersionDelEstandar(self.proyecto).validar_fase()), [])
        self.assertEqual(sorted(os.listdir(self.proyecto)), antes)


class DerogacionSinBorrar(unittest.TestCase):
    """EP-001 · HU-008 · derogar sin borrar ni renumerar. Los dos casos que
    miran `metareglas` quedan en su suite: no es de este grupo."""

    def _texto_de_base(self):
        partes = []
        for donde, _, archivos in os.walk(os.path.join(ESTANDAR, "base")):
            partes += [leer(os.path.join(donde, n)) for n in archivos if n.endswith(".md")]
        return "\n".join(partes)

    def derogaciones(self):
        return VersionDelEstandar(ESTANDAR).derogaciones()

    def test_cada_derogacion_conserva_su_cuerpo(self):
        derogadas = self.derogaciones()
        self.assertTrue(derogadas)
        base = self._texto_de_base()
        for _, identificador, _ in derogadas:
            self.assertIn(identificador, base)

    def test_la_marca_dice_desde_cuando_y_por_cual(self):
        base = self._texto_de_base()
        for desde, identificador, reemplazo in self.derogaciones():
            self.assertRegex(desde, r"^\d+\.\d+\.\d+$")
            self.assertTrue(reemplazo, identificador)
            for nombre in re.findall(r"[A-Z]{1,4}\d+(?:\.\d+)?", reemplazo):
                self.assertIn(nombre, base)

    def test_limites_toda_derogacion_de_hoy_tiene_reemplazo(self):
        self.assertEqual([i for _, i, r in self.derogaciones() if not r], [])


class NumeroDeVersion(unittest.TestCase):
    """EP-002 · HU-001 · el número de versión y qué significa cada parte."""

    def _entradas_del_registro(self):
        texto = leer(os.path.join(ESTANDAR, "CHANGELOG.md"))
        return [(tuple(int(p) for p in m.group(1).split(".")), m.group(0))
                for m in re.finditer(r"^## (\d+\.\d+\.\d+).*$", texto, re.M)]

    def test_el_numero_tiene_tres_partes_y_sale_de_version(self):
        crudo = leer(os.path.join(ESTANDAR, "VERSION")).strip()
        self.assertRegex(crudo, r"^\d+\.\d+\.\d+$")
        self.assertEqual(VersionDelEstandar.vigente(ESTANDAR), crudo)

    def test_la_version_del_archivo_es_la_ultima_del_registro(self):
        crudo = leer(os.path.join(ESTANDAR, "VERSION")).strip()
        self.assertEqual(self._entradas_del_registro()[0][0], tuple(int(p) for p in crudo.split(".")))

    @staticmethod
    def _reclamos(entradas):
        """Lo que está mal en `[(versión, encabezado)]` de vieja a nueva. Un número
        repetido no se renumera: se declara."""
        malos = []
        for (antes, previo), (ahora, encabezado) in zip(entradas, entradas[1:]):
            if ahora == antes:
                if "repetido" not in (previo + encabezado).lower():
                    malos.append(f"{ahora} está dos veces y no lo declara")
                continue
            if ahora < antes:
                malos.append(f"la versión bajó: {antes} → {ahora}")
                continue
            ma, me, pa = antes
            Ma, Me, Pa = ahora
            if Ma != ma and (Ma, Me, Pa) != (ma + 1, 0, 0):
                malos.append(f"salto de MAYOR mal formado: {antes} → {ahora}")
            elif Ma == ma and Me != me and (Me, Pa) != (me + 1, 0):
                malos.append(f"salto de MENOR mal formado: {antes} → {ahora}")
            elif Ma == ma and Me == me and Pa != pa + 1:
                malos.append(f"salto de PARCHE mal formado: {antes} → {ahora}")
        return malos

    def test_las_tres_partes_avanzan_y_lo_repetido_se_declara(self):
        self.assertEqual(self._reclamos(list(reversed(self._entradas_del_registro()))), [])

    def test_el_numero_repetido_que_no_se_declara_si_falla(self):
        callado_ = [((1, 0, 0), "## 1.0.0"), ((1, 1, 0), "## 1.1.0"), ((1, 1, 0), "## 1.1.0")]
        self.assertEqual(len(self._reclamos(callado_)), 1)
        dicho = callado_[:2] + [((1, 1, 0), "## 1.1.0 · número repetido")]
        self.assertEqual(self._reclamos(dicho), [])

    def test_toda_entrada_del_registro_declara_su_tipo(self):
        texto = leer(os.path.join(ESTANDAR, "CHANGELOG.md"))
        bloques = re.split(r"^## (\d+\.\d+\.\d+)", texto, flags=re.M)[1:]
        pares = list(zip(bloques[::2], bloques[1::2]))
        self.assertTrue(pares)
        sin_tipo = [v for v, cuerpo in pares[:-1] if not re.search(r"\*\*(MAYOR|MENOR|PARCHE)\.?\*\*", cuerpo)]
        self.assertEqual(sin_tipo, [])


# ── versiones ────────────────────────────────────────────────────────────

class Versiones(unittest.TestCase):
    """Nada heredado del estándar puede quedar viejo."""

    def _estandar(self, **plantillas):
        raiz = carpeta(self)
        os.makedirs(os.path.join(raiz, "plantillas"))
        for nombre, texto in plantillas.items():
            escribir(os.path.join(raiz, "plantillas", nombre), texto)
        return raiz

    def test_el_sello_se_reemplaza_en_su_sitio_y_nunca_se_duplica(self):
        texto = Sello.poner("hola\n", "aaa111", "1.0.0")
        self.assertIn("<!-- huella: aaa111 · estandar 1.0.0 -->", texto)
        de_nuevo = Sello.poner(texto, "bbb222", "2.0.0")
        self.assertEqual(de_nuevo.count("<!-- huella:"), 1)
        self.assertIn("bbb222", de_nuevo)
        self.assertNotIn("aaa111", de_nuevo)
        self.assertIn("hola", de_nuevo)

    def test_el_sello_se_lee_de_vuelta(self):
        archivo = os.path.join(carpeta(self), "x.md")
        escribir(archivo, Sello.poner("contenido\n", "abc123", "1.2.3"))
        self.assertEqual(Sello.leer(archivo), ("abc123", "1.2.3"))

    def test_sin_sello_no_se_inventa_uno(self):
        archivo = os.path.join(carpeta(self), "x.md")
        escribir(archivo, "sin sello\n")
        self.assertEqual(Sello.leer(archivo), ("", ""))

    def test_un_cambio_dentro_de_una_seccion_existente_se_detecta(self):
        estandar = self._estandar(**{"CLAUDE.md.plantilla": "# C\n\n## 6. Instalación\n\n- paso uno\n"})
        proyecto = carpeta(self)
        comp = POR_ID["claude-md"]
        escribir(os.path.join(proyecto, "CLAUDE.md"), Sello.poner(
            "# C del proyecto\n\n## 6. Instalación\n\n- paso uno\n",
            Sello.huella_central(comp, estandar), "1.0.0"))
        self.assertTrue(DocumentosHeredados(proyecto, estandar).estado_de("claude-md").al_dia)

        escribir(os.path.join(estandar, "plantillas", "CLAUDE.md.plantilla"),
                 "# C\n\n## 6. Instalación\n\n- paso uno\n- paso dos\n")
        est = DocumentosHeredados(proyecto, estandar).estado_de("claude-md")
        self.assertFalse(est.al_dia)
        self.assertEqual(est.situacion, VIEJO)
        self.assertIn("quedó viejo", est.mensaje())

    def test_un_documento_heredado_sin_sello_no_pasa_por_al_dia(self):
        estandar = self._estandar(**{"CLAUDE.md.plantilla": "# C\n"})
        proyecto = carpeta(self)
        escribir(os.path.join(proyecto, "CLAUDE.md"), "# el mío, sin sello\n")
        est = DocumentosHeredados(proyecto, estandar).estado_de("claude-md")
        self.assertEqual(est.situacion, SIN_SELLO)
        self.assertIn("no declara", est.mensaje())

    def test_el_checklist_reprueba_un_claude_md_viejo(self):
        proyecto = carpeta(self)
        escribir(os.path.join(proyecto, "CLAUDE.md"), Sello.poner("# mío\n", "000000000000", "0.0.1"))
        cumple, detalle = Checklist(proyecto, ESTANDAR)._claude_md()
        self.assertFalse(cumple)
        self.assertIn("viejo", detalle)

    def test_registrar_deja_el_archivo_con_lo_que_cambio(self):
        archivo = RegistroDeVersiones(carpeta(self)).registrar(
            "1.5.0", antes={"claude-md": "aaa"}, despues={"claude-md": "bbb"},
            pasos=["sellar CLAUDE.md"], pendientes=["**f13** — falta proyectos/"])
        texto = leer(archivo)
        for esperado in ("1.5.0", "claude-md", "aaa", "bbb", "sellar CLAUDE.md"):
            self.assertIn(esperado, texto)
        self.assertIn("pendiente", texto.lower())
        self.assertIn("1.5.0", os.path.basename(archivo))

    def test_solo_se_listan_los_componentes_que_cambiaron(self):
        archivo = RegistroDeVersiones(carpeta(self)).registrar(
            "1.5.0", antes={"claude-md": "aaa", "historico": "zzz"},
            despues={"claude-md": "bbb", "historico": "zzz"}, pasos=[])
        tabla = leer(archivo).split("## Componentes actualizados")[1].split("##")[0]
        self.assertIn("claude-md", tabla)
        self.assertNotIn("historico", tabla)

    def test_una_instalacion_desde_cero_no_declara_venir_de_si_misma(self):
        proyecto = carpeta(self)
        escribir(os.path.join(proyecto, ".agente", "stack-instalacion.md"), Sello.poner("copia\n", "abc123", "1.4.0"))
        archivo = RegistroDeVersiones(proyecto).registrar("1.4.0", {}, {"x": "a"}, [], anterior="")
        self.assertIn("(primera instalación)", leer(archivo))

    def test_una_actualizacion_declara_de_donde_viene(self):
        archivo = RegistroDeVersiones(carpeta(self)).registrar("1.5.0", {}, {"x": "b"}, [], anterior="1.4.0")
        self.assertIn("| Versión anterior | 1.4.0 |", leer(archivo))

    def test_dos_registros_el_mismo_dia_no_se_pisan(self):
        registro = RegistroDeVersiones(carpeta(self))
        uno = registro.registrar("1.5.0", {}, {"x": "a"}, [])
        dos = registro.registrar("1.5.0", {}, {"x": "b"}, [])
        self.assertNotEqual(uno, dos)
        self.assertTrue(os.path.isfile(uno) and os.path.isfile(dos))

    def test_el_indice_lista_los_registros(self):
        registro = RegistroDeVersiones(carpeta(self))
        registro.registrar("1.5.0", {}, {"x": "a"}, [])
        self.assertIn("1.5.0", leer(os.path.join(registro.carpeta, "README.md")))

    def _con_claude(self, adoptada):
        proyecto = carpeta(self)
        escribir(os.path.join(proyecto, "CLAUDE.md"), f"# C\n\n- Versión del estándar adoptada: {adoptada}\n")
        return proyecto

    def test_una_version_vieja_del_estandar_ya_no_reprueba_por_si_sola(self):
        cumple, _ = Checklist(self._con_claude("0.0.1"), ESTANDAR)._version()
        self.assertTrue(cumple)

    def test_no_declarar_la_version_si_reprueba(self):
        cumple, detalle = Checklist(self._con_claude("«X.Y.Z»"), ESTANDAR)._version()
        self.assertFalse(cumple)
        self.assertIn("no declara", detalle)

    def test_el_registro_no_vive_en_una_carpeta_ignorada(self):
        partes = CARPETA.replace("\\", "/").split("/")
        self.assertNotIn(".agente", partes)
        self.assertEqual(partes[0], "documentacion")

    def test_sin_carpeta_de_versiones_el_componente_reprueba(self):
        cumple, detalle = RegistroDeVersiones(carpeta(self)).revisar()
        self.assertFalse(cumple)
        self.assertIn("versiones", detalle)

    def test_instalado_una_version_y_registrado_otra_reprueba(self):
        proyecto = carpeta(self)
        RegistroDeVersiones(proyecto).registrar("1.0.0", {}, {"x": "a"}, [])
        escribir(os.path.join(proyecto, ".agente", "stack-instalacion.md"), Sello.poner("copia\n", "abc123", "2.0.0"))
        cumple, detalle = RegistroDeVersiones(proyecto).revisar()
        self.assertFalse(cumple)
        self.assertIn("falta registrar", detalle)

    def test_la_lista_de_componentes_heredados_no_se_desincroniza(self):
        for c in COMPONENTES:
            self.assertTrue(os.path.isfile(c.ruta_plantilla()), c.id)
            self.assertTrue(Sello.huella_central(c), c.id)


class ElOrdenMiraLaVersion(unittest.TestCase):
    """`EP-007 · HU-006 · CA-02` · el registro no gana una entrada vacía: la
    `23.10.0` va después de la `23.5.0` aunque sean del mismo día."""

    def proyecto(self, *nombres):
        raiz = carpeta(self)
        for n in nombres:
            escribir(os.path.join(raiz, *CARPETA.split(os.sep), n), "# registro\n")
        os.makedirs(os.path.join(raiz, *CARPETA.split(os.sep)), exist_ok=True)
        return RegistroDeVersiones(raiz)

    def test_el_caso_que_lo_destapo(self):
        self.assertEqual("23.10.0", self.proyecto("2026-08-18-23.5.0.md", "2026-08-18-23.10.0.md").version_registrada())

    def test_no_es_el_orden_del_nombre(self):
        self.assertEqual("23.10.0", self.proyecto("2026-08-18-23.10.0.md", "2026-08-18-23.5.0.md").version_registrada())

    def test_dos_digitos_contra_uno_en_el_medio(self):
        self.assertEqual("1.10.0", self.proyecto("2026-08-18-1.2.0.md", "2026-08-18-1.10.0.md").version_registrada())

    def test_dos_digitos_contra_uno_al_final(self):
        self.assertEqual("1.0.11", self.proyecto("2026-08-18-1.0.9.md", "2026-08-18-1.0.11.md").version_registrada())

    def test_la_fecha_sigue_mandando_sobre_la_version(self):
        self.assertEqual("23.5.0", self.proyecto("2026-08-18-23.10.0.md", "2026-08-19-23.5.0.md").version_registrada())

    def test_a_igual_fecha_y_version_manda_el_sufijo(self):
        r = self.proyecto("2026-08-18-9.0.0.md", "2026-08-18-9.0.0-2.md")
        self.assertEqual("2026-08-18-9.0.0-2.md", r.registros()[-1][0])

    def test_una_version_que_no_es_solo_numeros_no_revienta(self):
        self.assertEqual(2, len(self.proyecto("2026-08-18-23.10.0.md", "2026-08-18-23.10.0-beta.md").registros()))

    def test_el_orden_completo_de_una_historia_larga(self):
        r = self.proyecto("2026-08-10-9.2.0.md", "2026-08-18-23.5.0.md",
                          "2026-08-18-23.10.0.md", "2026-08-18-23.9.0.md")
        self.assertEqual(["9.2.0", "23.5.0", "23.9.0", "23.10.0"], [v for _, _, v in r.registros()])

    def test_sin_carpeta_de_registros_no_revienta(self):
        r = RegistroDeVersiones(carpeta(self))
        self.assertEqual([], r.registros())
        self.assertEqual("", r.version_registrada())

    def test_carpeta_vacia_no_revienta(self):
        self.assertEqual("", self.proyecto().version_registrada())

    def test_lo_que_no_es_un_registro_se_ignora(self):
        self.assertEqual(1, len(self.proyecto("2026-08-18-23.10.0.md", "README.md", "notas.txt").registros()))

    def test_el_orden_de_version_corrige_al_del_texto(self):
        """La vieja comparaba `"23.10.0" < "23.5.0"` en Python, que no prueba el
        código: acá se ordenan las dos formas y se ve cuál arregla el defecto."""
        versiones = ["23.10.0", "23.5.0"]
        self.assertEqual(["23.10.0", "23.5.0"], sorted(versiones))
        self.assertEqual(["23.5.0", "23.10.0"], sorted(versiones, key=RegistroDeVersiones.orden_de_version))

    def test_lo_que_no_es_numero_va_al_final(self):
        self.assertLess(RegistroDeVersiones.orden_de_version("1.0.0"), RegistroDeVersiones.orden_de_version("1.0.0rc"))


class LaFotoSeTomaAlFinal(unittest.TestCase):
    """Pendiente 46 · el registro no dice que falta escribirse a sí mismo."""

    def _registrar(self, proyecto, pendientes):
        ruta = RegistroDeVersiones(proyecto).registrar(
            "1.0.0", {}, {"x": "huella"}, ["se aplicó algo"], pendientes=pendientes, anterior="0.9.0")
        return ruta, leer(ruta)

    def test_el_apartado_se_calcula_con_el_archivo_ya_escrito(self):
        proyecto = carpeta(self)
        visto = {}

        def faltantes():
            donde = RegistroDeVersiones(proyecto).carpeta
            visto["archivos"] = sorted(os.listdir(donde)) if os.path.isdir(donde) else []
            return []
        ruta, _ = self._registrar(proyecto, faltantes)
        self.assertIn(os.path.basename(ruta), visto["archivos"])

    def test_lo_que_de_verdad_falta_si_se_escribe(self):
        _, texto = self._registrar(carpeta(self), lambda: ["**algo** — que sí decide el usuario"])
        self.assertIn("Qué quedó pendiente", texto)
        self.assertIn("que sí decide el usuario", texto)

    def test_sin_faltantes_no_se_escribe_el_apartado(self):
        _, texto = self._registrar(carpeta(self), lambda: [])
        self.assertNotIn("Qué quedó pendiente", texto)

    def test_la_lista_ya_calculada_sigue_valiendo(self):
        _, texto = self._registrar(carpeta(self), ["**x** — algo"])
        self.assertIn("Qué quedó pendiente", texto)

    def test_el_registro_queda_bien_formado_con_las_dos_escrituras(self):
        _, texto = self._registrar(carpeta(self), lambda: ["**x** — algo"])
        for parte in ("# Actualización a 1.0.0", "## Qué se aplicó", "## Qué quedó pendiente", "No se edita a mano"):
            self.assertEqual(1, texto.count(parte), parte)
        self.assertLess(texto.index("## Qué quedó pendiente"), texto.index("No se edita a mano"))

    def test_el_indice_queda_escrito_igual(self):
        proyecto = carpeta(self)
        self._registrar(proyecto, lambda: [])
        self.assertTrue(os.path.isfile(os.path.join(RegistroDeVersiones(proyecto).carpeta, "README.md")))


# ── guardian_version ─────────────────────────────────────────────────────

class ElCambioDeReglasLlevaSuVersion(unittest.TestCase):
    """`EP-005 · HU-005` · un cambio de la norma no se guarda sin su versión."""

    def hallazgos(self, *preparados):
        return VersionDelCambio(".", preparados=list(preparados)).validar()

    def test_cp001_sin_version_ni_entrada_no_pasa(self):
        h = self.hallazgos("base/09-git.md")
        self.assertEqual(1, len(h))
        self.assertEqual(FALLA, h[0].severidad)
        self.assertIn("VERSION", h[0].mensaje)
        self.assertIn("CHANGELOG.md", h[0].mensaje)

    def test_cp001b_con_las_dos_pasa(self):
        self.assertEqual([], self.hallazgos("base/09-git.md", "VERSION", "CHANGELOG.md"))

    def test_cp002_el_cambio_mezclado_se_detecta_igual(self):
        h = self.hallazgos("validadores/enlaces.py", "documentacion/x.md", "plantillas/CLAUDE.md.plantilla")
        self.assertEqual(1, len(h))
        self.assertIn("plantillas/CLAUDE.md.plantilla", h[0].mensaje)

    def test_cp003_lo_que_no_toca_reglas_no_nota_nada(self):
        self.assertEqual([], self.hallazgos("documentacion/epicas/x.md", "pendientes/y.md",
                                            "validadores/z.py", "historico-chat/a.md"))

    def test_cp004_el_rechazo_dice_exactamente_que_falta(self):
        solo_registro = self.hallazgos("base/09-git.md", "VERSION")
        self.assertIn("CHANGELOG.md", solo_registro[0].mensaje)
        self.assertNotIn("subir `VERSION`", solo_registro[0].mensaje)
        self.assertIn("subir `VERSION`", self.hallazgos("base/09-git.md", "CHANGELOG.md")[0].mensaje)

    def test_cp005_varios_archivos_de_norma_se_cuentan(self):
        h = self.hallazgos("base/09-git.md", "base/03-datos.md", "plantillas/ADR.md")
        self.assertIn("2 archivo(s) más de la norma", h[0].mensaje)

    def test_cp006_un_commit_vacio_no_revienta(self):
        self.assertEqual([], self.hallazgos())


# ── herramientas ─────────────────────────────────────────────────────────

class Herramientas(unittest.TestCase):
    """Q6, T5, DEP3: se prueba la detección; la ejecución depende de lo instalado."""

    def test_detecta_el_ecosistema_por_manifiesto(self):
        stack = HerramientaDelEcosistema.stack_de_manifiesto
        self.assertEqual(stack("composer.json"), "php")
        self.assertEqual(stack("package.json"), "node")
        self.assertEqual(stack("pyproject.toml"), "python")
        self.assertEqual(stack("Gemfile"), "ruby")
        self.assertIsNone(stack("README.md"))

    def test_ignora_manifiestos_de_dependencias_instaladas(self):
        es = HerramientaDelEcosistema.es_instalado
        self.assertTrue(es("vendor/x/composer.json"))
        self.assertTrue(es("node_modules/y/package.json"))
        self.assertFalse(es("proyectos/app/composer.json"))


# ── recuerdos ────────────────────────────────────────────────────────────

def _monta(caso, locales=None, repo=None):
    """Un proyecto temporal con su carpeta local y su carpeta del repositorio."""
    tmp = carpeta(caso)
    proyecto = os.path.join(tmp, "proyecto")
    casa = os.path.join(tmp, "casa")
    memoria = Recuerdos(proyecto, casa)
    for donde, archivos in ((memoria.carpeta_local(), locales or {}), (memoria.carpeta_repo(), repo or {})):
        if archivos:
            os.makedirs(donde, exist_ok=True)
        for nombre, texto in archivos.items():
            escribir(os.path.join(donde, nombre), texto)
    return proyecto, casa


class RecuerdosEnElRepositorio(unittest.TestCase):
    """La memoria del agente: en el repositorio, y solo ahí (`01·C19`)."""

    def test_la_carpeta_local_es_la_que_usa_la_herramienta(self):
        proyecto, casa = _monta(self)
        local = Recuerdos(os.path.join(proyecto, "Ing. Jose"), casa).carpeta_local()
        self.assertTrue(local.startswith(os.path.join(casa, ".claude", "projects")))
        self.assertEqual(os.path.basename(local), "memory")
        self.assertTrue(os.path.basename(os.path.dirname(local)).endswith("Ing--Jose"))

    def test_mueve_el_recuerdo_al_repositorio(self):
        memoria = Recuerdos(*_monta(self, {"lo-mio.md": "el recuerdo"}))
        self.assertEqual(memoria.migrar(True), [("lo-mio.md", "lo-mio.md")])
        self.assertEqual(memoria.sueltos(), [])
        self.assertEqual(leer(os.path.join(memoria.carpeta_repo(), "lo-mio.md")), "el recuerdo")

    def test_simular_no_toca_nada(self):
        memoria = Recuerdos(*_monta(self, {"lo-mio.md": "el recuerdo"}))
        self.assertTrue(memoria.migrar(False))
        self.assertTrue(memoria.sueltos())

    def test_el_duplicado_identico_tampoco_se_borra(self):
        memoria = Recuerdos(*_monta(self, {"x.md": "igual"}, {"x.md": "igual"}))
        self.assertEqual(memoria.migrar(True), [("x.md", "x-local.md")])
        self.assertEqual(leer(os.path.join(memoria.carpeta_repo(), "x.md")), "igual")
        self.assertEqual(leer(os.path.join(memoria.carpeta_repo(), "x-local.md")), "igual")

    def test_el_almacen_enlazado_a_la_carpeta_del_repo_ya_cumple(self):
        proyecto, _ = _monta(self, repo={"x.md": "el recuerdo", "memory.md": "# Índice"})
        with mock.patch.object(Recuerdos, "carpeta_local", lambda yo: yo.carpeta_repo()):
            memoria = Recuerdos(proyecto)
            self.assertTrue(memoria.enlazada())
            self.assertEqual(memoria.sueltos(), [])
            self.assertEqual(memoria.migrar(True), [])
            self.assertEqual(memoria.revisar(), (True, ""))
            self.assertEqual(sorted(os.listdir(memoria.carpeta_repo())), ["memory.md", "x.md"])
            self.assertEqual(Instalador().instalar_recuerdos(proyecto, aplicar=True),
                             ["memoria enlazada a `historico-chat/memory/`: ya cumple, no se toca"])
            self.assertEqual(leer(os.path.join(memoria.carpeta_repo(), "memory.md")), "# Índice")

    def test_el_indice_de_la_herramienta_cuenta_como_indice(self):
        proyecto, _ = _monta(self, repo={"MEMORY.md": "el índice del proyecto"})
        self.assertTrue(Recuerdos(proyecto).indice_presente())
        Instalador().instalar_recuerdos(proyecto, aplicar=True)
        self.assertIn("el índice del proyecto", leer(os.path.join(Recuerdos(proyecto).carpeta_repo(), "MEMORY.md")))

    def test_un_nombre_ocupado_no_se_pisa(self):
        memoria = Recuerdos(*_monta(self, {"x.md": "la local"}, {"x.md": "la del repo"}))
        self.assertEqual(memoria.migrar(True), [("x.md", "x-local.md")])
        self.assertEqual(leer(os.path.join(memoria.carpeta_repo(), "x.md")), "la del repo")
        self.assertEqual(leer(os.path.join(memoria.carpeta_repo(), "x-local.md")), "la local")

    def test_el_indice_no_se_pierde_por_las_mayusculas(self):
        memoria = Recuerdos(*_monta(self, {"MEMORY.md": "el de la herramienta"}, {"memory.md": "el del proyecto"}))
        self.assertEqual(memoria.migrar(True), [("MEMORY.md", "MEMORY-local.md")])
        self.assertEqual(leer(os.path.join(memoria.carpeta_repo(), "memory.md")), "el del proyecto")

    def test_reprueba_mientras_quede_algo_en_la_carpeta_local(self):
        memoria = Recuerdos(*_monta(self, {"x.md": "lo mío"}))
        cumple, detalle = memoria.revisar()
        self.assertFalse(cumple)
        self.assertIn("x.md", detalle)
        memoria.migrar(True)
        self.assertEqual(memoria.revisar(), (True, ""))

    def test_la_memoria_se_inyecta_al_arrancar(self):
        proyecto, _ = _monta(self, repo={"memory.md": "# Índice\n\n| a | b |\n"})
        texto = Recuerdos(proyecto).contexto()
        self.assertIn("MEMORIA DEL AGENTE", texto)
        self.assertIn("| a | b |", texto)

    def test_sin_indice_no_se_inyecta_nada(self):
        proyecto, _ = _monta(self)
        self.assertEqual(Recuerdos(proyecto).contexto(), "")

    def test_el_instalador_crea_el_indice_sellado_y_no_lo_pisa(self):
        proyecto, _ = _monta(self)
        os.makedirs(proyecto, exist_ok=True)
        self.assertIn("crear historico-chat/memory/memory.md", Instalador().instalar_recuerdos(proyecto, aplicar=True))
        comp = POR_ID["recuerdos"]
        self.assertEqual(Sello.huella_sellada(proyecto, comp), Sello.huella_central(comp))
        indice = Recuerdos(proyecto).ruta_indice()
        with io.open(indice, "a", encoding="utf-8") as f:
            f.write("\n| lo mío | una línea del proyecto |\n")
        self.assertEqual(Instalador().instalar_recuerdos(proyecto, aplicar=True),
                         ["historico-chat/memory/memory.md ya estaba sellado al día"])
        self.assertIn("una línea del proyecto", leer(indice))


def memoria_larga(raiz, filas=120):
    cuerpo = ["# Memoria", "", "Explicación. " * 40, "", "| Recuerdo | De qué |", "|---|---|"]
    cuerpo += [f"| [Recuerdo {i}](r{i}.md) | {'Lo que pide el usuario. ' * 6}|" for i in range(filas)]
    escribir(os.path.join(raiz, "historico-chat", "memory", "memory.md"), "\n".join(cuerpo) + "\n")


class LoQueNoCabeSeRecortaYSeDice(unittest.TestCase):
    """`EP-005 · HU-009 · CA-04` · la memoria con tope cabe, sin filas cortadas."""

    def test_la_memoria_con_tope_cabe_sin_filas_cortadas(self):
        tmp = carpeta(self)
        memoria_larga(tmp)
        texto = Recuerdos(tmp).contexto(tope=3000)
        self.assertLessEqual(len(texto), 3000)
        self.assertIn("historico-chat/memory/memory.md", texto)
        for linea in texto.splitlines():
            if linea.startswith("| ["):
                self.assertTrue(linea.endswith("|"), linea)

    def test_sin_tope_queda_como_antes(self):
        tmp = carpeta(self)
        memoria_larga(tmp)
        self.assertIn("Explicación.", Recuerdos(tmp).contexto())


class ElAlmacenLocalQuedaVacio(unittest.TestCase):
    """`EP-006 · HU-006` · no queda una segunda copia donde nadie la revisa."""

    def test_despues_de_recoger_el_almacen_local_no_tiene_archivos(self):
        memoria = Recuerdos(*_monta(self, locales={"algo.md": "# Algo\n"}))
        memoria.migrar(aplicar=True)
        self.assertEqual([f for f in os.listdir(memoria.carpeta_local()) if f.endswith(".md")], [])

    def test_no_queda_un_puntero_en_lugar_del_texto(self):
        puntero = "# Ver el repositorio\n\nEste recuerdo vive en `historico-chat/memory/algo.md`.\n"
        memoria = Recuerdos(*_monta(self, locales={"puntero.md": puntero}))
        memoria.migrar(aplicar=True)
        self.assertEqual([f for f in os.listdir(memoria.carpeta_local()) if f.endswith(".md")], [])

    def test_con_el_almacen_ya_vacio_no_falla_ni_hace_nada(self):
        self.assertEqual(Recuerdos(*_monta(self, repo={"algo.md": "# Algo\n"})).migrar(aplicar=True), [])

    def test_se_lleva_todo_y_el_almacen_queda_vacio(self):
        memoria = Recuerdos(*_monta(self, locales={"algo.md": "# Algo\n", "config.json": "{}\n"}))
        memoria.migrar(aplicar=True)
        self.assertEqual(os.listdir(memoria.carpeta_local()), [])
        self.assertIn("config.json", os.listdir(memoria.carpeta_repo()))

    def test_no_quedan_dos_versiones_del_mismo_recuerdo(self):
        memoria = Recuerdos(*_monta(self, locales={"algo.md": "# Algo local\n"}))
        memoria.migrar(aplicar=True)
        self.assertEqual([f for f in os.listdir(memoria.carpeta_local()) if f.endswith(".md")], [])
        self.assertEqual(len([f for f in os.listdir(memoria.carpeta_repo()) if f.endswith(".md")]), 1)

    def test_el_almacen_de_esta_maquina_esta_vacio(self):
        local = Recuerdos(ESTANDAR, os.path.expanduser("~")).carpeta_local()
        quedan = [f for f in os.listdir(local) if f.endswith(".md")] if os.path.isdir(local) else []
        self.assertEqual(quedan, [])


MEMORIA = os.path.join(ESTANDAR, "historico-chat", "memory")


class IndiceDeLosRecuerdos(unittest.TestCase):
    """`EP-006 · HU-002 · CA-02` · el índice dice de qué trata cada recuerdo, en
    los dos sentidos."""

    def _archivos(self, donde):
        return {f for f in os.listdir(donde) if f.endswith(".md") and f != "memory.md"}

    def _enlazados(self, donde):
        idx = leer(os.path.join(donde, "memory.md"))
        return {e for e in re.findall(r"\]\(([^)]+\.md)\)", idx) if "/" not in e and e != "memory.md"}

    def test_todo_recuerdo_de_esta_casa_tiene_su_linea_en_el_indice(self):
        self.assertEqual(self._archivos(MEMORIA) - self._enlazados(MEMORIA), set())

    def test_toda_linea_del_indice_de_esta_casa_tiene_su_archivo(self):
        self.assertEqual(self._enlazados(MEMORIA) - self._archivos(MEMORIA), set())

    def test_privacidad_ningun_recuerdo_lleva_claves_ni_datos_personales(self):
        """La vieja corría el detector sobre el repositorio y filtraba los de la
        memoria, pero el detector salta los `.md` y la memoria solo tiene `.md`:
        pasaba siempre sin mirar nada. Acá se le pasa cada recuerdo."""
        hallazgos = []
        for nombre in sorted(os.listdir(MEMORIA)):
            if nombre.endswith(".md"):
                hallazgos += SecretosEnElCodigo.revisar_texto(leer(os.path.join(MEMORIA, nombre)), nombre)
        self.assertEqual([h for h in hallazgos if h.severidad == FALLA], [])
        self.assertTrue(SecretosEnElCodigo.revisar_texto("clave = 'AKIA" + "ABCDEFGHIJKLMNOP'\n", "x.md"),
                        "el detector no ve una clave puesta a propósito: la prueba no probaría nada")

    def test_el_indice_vacio_es_valido(self):
        tmp = carpeta(self)
        escribir(os.path.join(tmp, "memory.md"), "# Memoria del agente\n\n## Índice\n\n(todavía no hay ninguno)\n")
        self.assertEqual(self._archivos(tmp), set())
        self.assertEqual(self._enlazados(tmp), set())

    def test_por_el_indice_se_llega_al_recuerdo_sin_abrir_los_otros(self):
        idx = leer(os.path.join(MEMORIA, "memory.md"))
        filas = [l for l in idx.splitlines() if l.startswith("|") and re.search(r"\]\([^/)]+\.md\)", l)]
        self.assertGreaterEqual(len(filas), 1)
        for fila in filas:
            descripcion = [c.strip() for c in fila.strip().strip("|").split("|")][-1]
            self.assertGreater(len(descripcion), 20, fila)


class ElRecuerdoTraeSusTresPartes(unittest.TestCase):
    """`EP-006 · HU-005 · CA-02` · qué se pide, por qué y cómo se aplica."""

    def _partes(self, texto):
        return ("**Por qué" in texto, "Cómo se aplica" in texto)

    def test_todo_recuerdo_de_esta_casa_dice_por_que_y_como_se_aplica(self):
        sin_partes = []
        for f in sorted(os.listdir(MEMORIA)):
            if f.endswith(".md") and f != "memory.md":
                porque, como = self._partes(leer(os.path.join(MEMORIA, f)))
                if not (porque and como):
                    sin_partes.append((f, porque, como))
        self.assertEqual(sin_partes, [])

    def test_un_recuerdo_sin_el_porque_se_detecta(self):
        porque, como = self._partes("# Algo\n\nSe hace así.\n\n**Cómo se aplica:** así.\n")
        self.assertFalse(porque)
        self.assertTrue(como)


# ── checklist ────────────────────────────────────────────────────────────

class ChecklistDelStack(unittest.TestCase):
    """El stack de instalación: qué le falta a un proyecto."""

    def test_la_lista_y_las_comprobaciones_no_se_separan(self):
        ids = {i for i, _, _ in Checklist.componentes()}
        self.assertTrue(ids)
        self.assertEqual(ids, set(Checklist.COMPROBACIONES))

    def test_cada_comprobacion_tiene_su_metodo(self):
        for id, metodo in Checklist.COMPROBACIONES.items():
            self.assertTrue(callable(getattr(Checklist, metodo, None)), id)

    def test_cada_componente_dice_como_se_instala(self):
        for id, componente, arreglo in Checklist.componentes():
            self.assertTrue(componente.strip(), id)
            self.assertTrue(arreglo.strip(), id)

    def test_un_proyecto_vacio_no_pasa_nada(self):
        puntos = Checklist(carpeta(self)).revisar()
        self.assertEqual(len(puntos), len(Checklist.COMPROBACIONES))
        self.assertTrue(Checklist.pendientes(puntos))
        self.assertIn("INSTALACIÓN INCOMPLETA", Checklist.resumen("x", puntos))

    def test_la_marca_se_escribe_y_se_borra_sola(self):
        revision = Checklist(carpeta(self))
        puntos = revision.revisar()
        archivo = revision.escribir_marca(puntos)
        self.assertTrue(os.path.isfile(archivo))
        for p in puntos:
            p.cumple = True
        self.assertEqual(revision.escribir_marca(puntos), "")
        self.assertFalse(os.path.isfile(archivo))

    def test_detecta_que_el_stack_central_cambio(self):
        raiz = carpeta(self)
        escribir(os.path.join(raiz, ".agente", "stack-instalacion.md"), "lo que sea\n<!-- huella: 000000000000 -->\n")
        self.assertEqual(Checklist.huella_instalada(raiz), "000000000000")
        cumple, detalle = Checklist(raiz, ESTANDAR)._stack_instalacion()
        self.assertFalse(cumple)
        self.assertIn("cambió en el estándar", detalle)

    def test_un_componente_que_el_validador_no_conoce_se_dice(self):
        class Inventada(Checklist):
            @classmethod
            def componentes(cls, estandar=None):
                return [("inventado", "Algo nuevo", "correr el instalador")]
        punto = Inventada(carpeta(self)).revisar()[0]
        self.assertFalse(punto.cumple)
        self.assertIn("no sabe comprobar", punto.detalle)

    def test_el_checklist_lee_la_lista_de_ignorados_del_instalador(self):
        raiz = carpeta(self)
        escribir(os.path.join(raiz, ".gitignore"), "\n".join(IGNORADOS) + "\n")
        self.assertTrue(Checklist(raiz)._gitignore()[0])
        escribir(os.path.join(raiz, ".gitignore"), "CLAUDE.md\n.agente/\n")
        ok, msg = Checklist(raiz)._gitignore()
        self.assertFalse(ok)
        self.assertIn("historico-chat/.tocado/", msg)


class LaRevisionVeLaCadena(unittest.TestCase):
    """`A-EP-007-HU-007` · la revisión ve la cadena de `02·F0`."""

    def setUp(self):
        self.proyecto = os.path.join(carpeta(self), "proyecto")
        for sub in ("prompts", "proyectos", os.path.join("documentacion", "epicas")):
            os.makedirs(os.path.join(self.proyecto, sub))

    def _con_codigo(self):
        escribir(os.path.join(self.proyecto, "proyectos", "app.py"), "# código\n")

    def _con_planteamiento(self):
        escribir(os.path.join(self.proyecto, "prompts", "mesas-planteamiento.md"), "# Planteamiento\n")

    def _punto(self):
        return next((p for p in Checklist(self.proyecto).revisar() if p.id == "cadena"), None)

    def test_cp_001_la_cadena_vacia_se_nombra(self):
        self._con_codigo()
        punto = self._punto()
        self.assertIsNotNone(punto)
        self.assertFalse(punto.cumple)
        self.assertIn("planteamiento", punto.detalle)
        self.assertIn("instalador", punto.arreglo)
        resumen = Checklist.resumen(self.proyecto, Checklist(self.proyecto).revisar())
        self.assertNotIn("instalación completa", resumen.lower())
        self.assertIn("de 14", resumen)

    def test_cp_002_el_punto_se_apaga_al_escribir_el_planteamiento(self):
        self._con_codigo()
        self.assertFalse(self._punto().cumple)
        self._con_planteamiento()
        os.makedirs(os.path.join(self.proyecto, "documentacion", "epicas", "EP-001-una-epica"))
        self.assertTrue(self._punto().cumple)

    def test_cp_003_la_epica_solo_se_exige_si_hay_codigo(self):
        self._con_planteamiento()
        self.assertTrue(self._punto().cumple)
        self._con_codigo()
        punto = self._punto()
        self.assertFalse(punto.cumple)
        self.assertIn("épica", punto.detalle)


def _otra_unidad(ruta, mayuscula):
    unidad, resto = os.path.splitdrive(ruta)
    return (unidad.upper() if mayuscula else unidad.lower()) + resto if unidad else ruta


class MayusculaDeUnidad(unittest.TestCase):
    """Pendiente 72 · `c:/x` y `C:/x` son la misma ruta para el checklist."""

    def setUp(self):
        tmp = carpeta(self)
        self.proyecto = os.path.join(tmp, "proyecto")
        os.makedirs(os.path.join(self.proyecto, ".claude"))
        self.estandar = os.path.join(tmp, "estandar")
        os.makedirs(self.estandar)
        self.tmp = tmp

    def _escribir_enganches(self, estandar, proyecto):
        hooks = {}
        for evento, _, guion, mensaje, args in HOOKS_CLAUDE:
            h = Instalador.hook_claude(estandar.replace("\\", "/"), proyecto.replace("\\", "/"), guion, mensaje, args)
            hooks.setdefault(evento, []).append({"hooks": [h]})
        escribir(os.path.join(self.proyecto, ".claude", "settings.json"), json.dumps({"hooks": hooks}))

    @unittest.skipUnless(os.name == "nt", "solo Windows ignora la mayúscula de la unidad")
    def test_minuscula_y_mayuscula_dan_lo_mismo(self):
        self._escribir_enganches(_otra_unidad(self.estandar, True), _otra_unidad(self.proyecto, True))
        ok_may, _ = Checklist(_otra_unidad(self.proyecto, True), _otra_unidad(self.estandar, True))._enganches_claude()
        ok_min, msg = Checklist(_otra_unidad(self.proyecto, False), _otra_unidad(self.estandar, False))._enganches_claude()
        self.assertTrue(ok_may)
        self.assertTrue(ok_min, msg)

    def test_un_enganche_de_otro_estandar_si_se_reporta(self):
        self._escribir_enganches(os.path.join(self.tmp, "otro-estandar"), self.proyecto)
        ok, msg = Checklist(self.proyecto, self.estandar)._enganches_claude()
        self.assertFalse(ok)
        self.assertIn("sin poner o vencidos", msg)


# ── el instalador por partes ─────────────────────────────────────────────

def _espacio(caso, *repos):
    raiz = carpeta(caso)
    for repo in repos:
        os.makedirs(os.path.join(raiz, repo, ".git"))
    return raiz


def _texto(*lineas):
    return "\n".join(lineas) + "\n"


class InstaladorPorPartes(unittest.TestCase):

    def test_lee_el_registro_de_proyectos(self):
        proyectos = Instalador().proyectos_registrados()
        self.assertTrue(proyectos)
        self.assertNotIn("Proyecto", [n for n, _ in proyectos])
        for _, ruta in proyectos:
            self.assertNotIn("`", ruta)

    def test_el_gate_f13_exige_la_carpeta_proyectos(self):
        self.assertTrue(Instalador.cumple_f13(_espacio(self, "proyectos/rni-back")))
        suelto = _espacio(self)
        os.makedirs(os.path.join(suelto, "localhub"))
        self.assertFalse(Instalador.cumple_f13(suelto))

    def test_encuentra_los_repos_dentro_de_proyectos(self):
        raiz = _espacio(self, "proyectos/rni-back", "proyectos/rni-front")
        hallados = [os.path.relpath(r, raiz).replace("\\", "/") for r in Instalador.repositorios_git(raiz)]
        self.assertEqual(hallados, ["proyectos/rni-back", "proyectos/rni-front"])

    def test_un_solo_repo_en_la_raiz(self):
        raiz = _espacio(self, ".")
        self.assertEqual(Instalador.repositorios_git(raiz), [raiz])

    def test_sin_repos_no_devuelve_nada(self):
        raiz = _espacio(self)
        os.makedirs(os.path.join(raiz, "documentacion"))
        self.assertEqual(Instalador.repositorios_git(raiz), [])

    def test_reemplaza_un_enganche_propio_en_vez_de_duplicarlo(self):
        """La vieja armaba el JSON y probaba su propia comprensión de lista, sin
        llamar al instalador: pasaba aunque el instalador duplicara. Acá se
        instala sobre un `settings.json` con el enganche viejo y uno ajeno."""
        raiz = _espacio(self)
        escribir(os.path.join(raiz, ".claude", "settings.json"), json.dumps({"hooks": {"PostToolUse": [
            {"matcher": "Write|Edit", "hooks": [
                {"type": "command", "command": "prettier --write x"},
                {"type": "command", "command": 'python "/viejo/validadores/hook_md.py"'}]}]}}))
        pasos = Instalador().instalar_claude(raiz, ESTANDAR.replace("\\", "/"), aplicar=True)
        self.assertIn("reemplazar el enganche PostToolUse en %s" % os.path.join(".claude", "settings.json"), pasos)
        grupo = [g for g in json.loads(leer(os.path.join(raiz, ".claude", "settings.json")))["hooks"]["PostToolUse"]
                 if g.get("matcher") == "Write|Edit"][0]
        comandos = [h["command"] for h in grupo["hooks"]]
        self.assertIn("prettier --write x", comandos, "se tocó un enganche ajeno")
        self.assertEqual(1, len([c for c in comandos if "hook_md.py" in c]), "quedó duplicado")
        self.assertFalse([c for c in comandos if "/viejo/" in c], "quedó el viejo")

    def test_el_historico_se_instala_en_dos_eventos(self):
        eventos = {e: args for e, _, g, _, args in HOOKS_CLAUDE if g == "hook_historico.py"}
        self.assertEqual(eventos, {"UserPromptSubmit": "--modo usuario", "Stop": "--modo agente"})

    def test_los_argumentos_van_antes_de_la_raiz(self):
        cmd = Instalador.hook_claude("/estandar", "/proy", "hook_historico.py", "…", "--modo agente")["command"]
        self.assertIn('hook_historico.py" --modo agente --raiz "/proy"', cmd)

    def test_crea_la_carpeta_del_historico_y_no_la_pisa(self):
        raiz = _espacio(self)
        self.assertEqual(Instalador().instalar_historico(raiz, aplicar=True),
                         ["crear historico-chat/README.md", "crear historico-chat/resumenes/README.md"])
        indice = os.path.join(raiz, "historico-chat", "README.md")
        self.assertTrue(os.path.isfile(os.path.join(raiz, "historico-chat", "resumenes", "README.md")))
        comp = POR_ID["historico"]
        self.assertEqual(Sello.huella_sellada(raiz, comp), Sello.huella_central(comp))
        with io.open(indice, "a", encoding="utf-8") as f:
            f.write("\n- línea del proyecto\n")
        self.assertEqual(Instalador().instalar_historico(raiz, aplicar=True),
                         ["historico-chat/README.md ya estaba sellado al día"])
        self.assertIn("línea del proyecto", leer(indice))

    def test_al_readme_del_historico_solo_se_le_refresca_el_sello(self):
        raiz = _espacio(self)
        Instalador().instalar_historico(raiz, aplicar=True)
        indice = os.path.join(raiz, "historico-chat", "README.md")
        escribir(indice, "# El mío, reescrito entero\n")
        pasos = Instalador().instalar_historico(raiz, aplicar=True)
        self.assertTrue(any("sellar" in p for p in pasos), pasos)
        texto = leer(indice)
        self.assertIn("El mío, reescrito entero", texto)
        self.assertIn("<!-- huella:", texto)

    def test_sella_el_claude_md_sin_tocarle_el_contenido(self):
        raiz = _espacio(self)
        local = os.path.join(raiz, "CLAUDE.md")
        escribir(local, claude_md_completo() + "\nlo mío\n")
        Instalador().instalar_claude_md(raiz, aplicar=True)
        self.assertIn("lo mío", leer(local))
        comp = POR_ID["claude-md"]
        self.assertEqual(Sello.huella_sellada(raiz, comp), Sello.huella_central(comp))
        self.assertEqual(Instalador().instalar_claude_md(raiz, aplicar=True), ["CLAUDE.md ya estaba sellado al día"])
        self.assertEqual(len([l for l in leer(local).splitlines() if l.startswith("<!-- huella:")]), 1)

    def test_sin_claude_md_se_genera_lleno_desde_la_plantilla(self):
        raiz = _espacio(self)
        self.assertIn("crear CLAUDE.md", Instalador().instalar_claude_md(raiz, aplicar=True)[0])
        texto = leer(os.path.join(raiz, "CLAUDE.md"))
        self.assertIsNone(modulo_instalar._MARCADOR.search(texto), texto[:400])
        self.assertIn(VersionDelEstandar.vigente(), texto)
        self.assertIn(ESTANDAR.replace("\\", "/"), texto)

    def test_al_claude_md_solo_se_le_agrega_lo_que_la_plantilla_sumo(self):
        raiz = _espacio(self)
        local = os.path.join(raiz, "CLAUDE.md")
        recortado = claude_md_completo().split("## 4. Precedencia")[0]
        escribir(local, recortado + "\n## Sección propia\n\nmía y de nadie más\n")
        pasos = Instalador().instalar_claude_md(raiz, aplicar=True)
        self.assertTrue(any("lo que la plantilla sumó" in p for p in pasos), pasos)
        texto = leer(local)
        self.assertIn("mía y de nadie más", texto)
        self.assertIn("## 4. Precedencia", texto)
        self.assertEqual(texto.count("## 1. Ubicación del estándar"), 1)

    def test_la_estructura_base_se_crea_sola_y_no_toca_lo_que_hay(self):
        raiz = _espacio(self)
        ajeno = os.path.join(raiz, "proyectos", "app")
        os.makedirs(ajeno)
        Instalador.instalar_estructura(raiz, aplicar=True)
        for sub in CARPETAS_BASE:
            self.assertTrue(os.path.isdir(os.path.join(raiz, sub)), sub)
        self.assertTrue(os.path.isdir(ajeno))
        self.assertEqual(Instalador.instalar_estructura(raiz, aplicar=True), ["la estructura base ya estaba"])

    def test_pendientes_ya_no_esta_en_la_estructura_base(self):
        self.assertNotIn("pendientes", CARPETAS_BASE)
        raiz = _espacio(self)
        Instalador.instalar_estructura(raiz, aplicar=True)
        self.assertFalse(os.path.isdir(os.path.join(raiz, "pendientes")))

    def test_la_estructura_no_pisa_los_pendientes_que_ya_estaban(self):
        raiz = _espacio(self)
        escribir(os.path.join(raiz, "pendientes", "07-algo.md"), "# Pendiente\n")
        Instalador.instalar_estructura(raiz, aplicar=True)
        self.assertEqual(["07-algo.md"], os.listdir(os.path.join(raiz, "pendientes")))

    def test_el_gitignore_solo_se_le_agrega_lo_que_falta(self):
        raiz = _espacio(self)
        archivo = os.path.join(raiz, ".gitignore")
        escribir(archivo, "# lo mío\nnode_modules/\nCLAUDE.md\n")
        Instalador.instalar_gitignore(raiz, aplicar=True)
        lineas = leer(archivo).splitlines()
        self.assertIn("node_modules/", lineas)
        self.assertEqual(lineas.count("CLAUDE.md"), 1)
        self.assertIn(".agente/", lineas)
        self.assertIn("historico-chat/.tocado/", lineas)
        self.assertEqual(Instalador.instalar_gitignore(raiz, aplicar=True),
                         ["el .gitignore ya ignoraba la configuración local"])

    def test_el_claude_md_se_pone_al_dia_con_lo_que_la_plantilla_cambio(self):
        base = _texto("# C — X", "", "## 1. Ubicación", "", "Rutas viejas.")
        plantilla = _texto("# C — X", "", "## 1. Ubicación", "", "Rutas nuevas.")
        texto, al_dia, a_mano = Plantillas.sincronizar_secciones(base, plantilla, base)
        self.assertEqual((al_dia, a_mano), (["1. Ubicación"], []))
        self.assertIn("Rutas nuevas.", texto)
        self.assertNotIn("Rutas viejas.", texto)

    def test_lo_que_el_proyecto_escribio_encima_no_se_pisa(self):
        base = _texto("# C — X", "", "## 1. Ubicación", "", "Rutas viejas.")
        plantilla = _texto("# C — X", "", "## 1. Ubicación", "", "Rutas nuevas.")
        local = _texto("# C — X", "", "## 1. Ubicación", "", "Rutas viejas.", "", "Y una nota mía.")
        texto, al_dia, a_mano = Plantillas.sincronizar_secciones(local, plantilla, base)
        self.assertEqual((al_dia, a_mano, texto), ([], ["1. Ubicación"], local))

    def test_sin_base_no_se_reemplaza_nada(self):
        plantilla = _texto("# C — X", "", "## 1. Ubicación", "", "Rutas nuevas.")
        local = _texto("# C — X", "", "## 1. Ubicación", "", "Rutas viejas.")
        self.assertEqual(Plantillas.sincronizar_secciones(local, plantilla, ""), (local, [], []))

    def test_los_ajustes_del_punto_5_no_se_pisan_nunca(self):
        base = _texto("# C — X", "", "## 5.1 Ajustar", "", "- Idioma: es.")
        plantilla = _texto("# C — X", "", "## 5.1 Ajustar", "", "- Idioma: en.")
        self.assertEqual(Plantillas.sincronizar_secciones(base, plantilla, base), (base, [], []))
        for titulo in ("5.1 Ajustar una regla", "5.2 Agregar reglas nuevas"):
            self.assertTrue(Plantillas.es_del_proyecto(titulo))
        for titulo in ("1. Ubicación", "4. Precedencia", "6. Cómo pedir"):
            self.assertFalse(Plantillas.es_del_proyecto(titulo))

    def test_sin_diferencias_el_claude_md_no_se_toca(self):
        igual = _texto("# T", "", "## 1. Ubicación", "", "Lo mismo.")
        self.assertEqual(Plantillas.sincronizar_secciones(igual, igual, igual), (igual, [], []))

    def test_los_cuatro_archivos_de_agente_se_ponen_y_no_se_pisan(self):
        raiz = _espacio(self)
        Instalador().instalar_agente_config(raiz, aplicar=True)
        for nombre in CONFIG_AGENTE:
            self.assertTrue(os.path.isfile(os.path.join(raiz, ".agente", nombre)))
        stack = os.path.join(raiz, ".agente", "stack.md")
        escribir(stack, "# lo que declaró el proyecto\n")
        self.assertEqual(Instalador().instalar_agente_config(raiz, aplicar=True),
                         ["los 4 archivos de .agente/ ya estaban"])
        self.assertIn("lo que declaró el proyecto", leer(stack))

    def test_stack_md_nace_y_se_repara_sin_enlaces_rotos(self):
        raiz = os.path.realpath(_espacio(self))

        def rotos(archivo):
            enlaces = [e for e in re.findall(r"\]\(([^)]+)\)", leer(archivo))
                       if not e.startswith("http") and "«" not in e]
            return [e for e in enlaces
                    if not os.path.exists(os.path.join(os.path.dirname(archivo), e.split("#")[0]))]
        instalador = Instalador()
        instalador.instalar_agente_config(raiz, True)
        stack = os.path.join(raiz, ".agente", "stack.md")
        self.assertEqual([], rotos(stack))
        escribir(stack, "[ID8](../base/00-identidad-y-rol/x.md) y [mío](../LEEME.md)\n")
        escribir(os.path.join(raiz, "LEEME.md"), "x\n")
        instalador.reparar_marcadores(stack, raiz, True, "stack")
        texto = leer(stack)
        self.assertIn("](%s/base/" % ESTANDAR.replace("\\", "/"), texto)
        self.assertIn("[mío](../LEEME.md)", texto)

    def test_el_propio_estandar_no_se_trata_como_un_proyecto(self):
        self.assertTrue(Instalador().es_el_estandar(ESTANDAR))
        self.assertFalse(Instalador().es_el_estandar(_espacio(self)))


class LaListaDeEnganches(unittest.TestCase):
    """Construido y no colgado no sirve de nada (`EP-002·HU-004`): cada enganche
    está en la lista del instalador, con su momento."""

    def guiones(self):
        return [h[2] for h in HOOKS_CLAUDE]

    def test_los_que_se_cuelgan_de_la_herramienta(self):
        for guion in ("hook_rutas.py", "hook_turno.py", "hook_acuerdos.py", "hook_redaccion.py"):
            self.assertIn(guion, self.guiones())

    def test_el_freno_va_antes_de_toda_accion(self):
        suyos = [e for e in HOOKS_CLAUDE if e[2] == "hook_antes.py"]
        self.assertEqual([("PreToolUse", None, "--modo accion")], [(e[0], e[1], e[4]) for e in suyos])

    def test_la_redaccion_se_mide_al_cerrar_el_turno(self):
        self.assertEqual(["Stop"], [h[0] for h in HOOKS_CLAUDE if h[2] == "hook_redaccion.py"])

    def test_el_analisis_no_tiene_enganche_propio_al_cerrar(self):
        self.assertFalse([h for h in HOOKS_CLAUDE if h[0] == "Stop" and h[2] == "hook_analisis.py"])

    def test_el_post_commit_lo_escribe_el_instalador(self):
        self.assertIn("post-commit", [h[0] for h in HOOKS])

    def test_el_pre_commit_revisa_el_plan(self):
        self.assertIn("validar.py\" plan --raiz \"$(pwd)\" --preparados", PLANTILLA_PRE_COMMIT)

    def test_el_pre_push_reclama_y_no_corre_las_pruebas(self):
        self.assertIn("internas --reclamo", PLANTILLA_PRE_PUSH)
        self.assertNotIn("validar.py internas", PLANTILLA_PRE_PUSH.replace("internas --reclamo", ""))
        self.assertIn("ejecutable tareas; do", PLANTILLA_PRE_PUSH)

    def test_los_enganches_del_adaptador_son_los_que_la_instalacion_enchufa(self):
        hay = sorted(f for f in os.listdir(ADAPTADOR) if f.startswith("hook_") and f.endswith(".py"))
        self.assertEqual(Instalador.enganches_enchufados(), hay)

    def test_la_instalacion_apunta_al_adaptador(self):
        cmd = Instalador.hook_claude("/estandar", "/proyecto", "hook_md.py", "mensaje")["command"]
        self.assertIn("adaptadores/claude-code/hook_md.py", cmd)
        self.assertNotIn("validadores/hook_", cmd)

    def test_cada_guion_de_la_lista_existe_donde_dice(self):
        for guion in self.guiones():
            self.assertTrue(os.path.isfile(os.path.join(ADAPTADOR, guion)), guion)


class ElEngancheDePublicar(unittest.TestCase):
    """`09·08` · la batería corre antes de publicar, y no todo detiene."""

    GANCHO = os.path.join(ESTANDAR, ".githooks", "pre-push")

    def test_esta_en_la_lista_y_el_archivo_lleva_la_marca(self):
        self.assertIn("pre-push", [n for n, _p, _d in HOOKS])
        self.assertIn(MARCA, leer(self.GANCHO))

    def test_que_detiene_y_que_no(self):
        t = leer(self.GANCHO)
        self.assertIn("for SUB in estandar versionado", t)
        self.assertIn("no detiene", t)
        self.assertNotIn("for SUB in estandar metareglas", t)
        self.assertIn("--no-verify", t)
        for sub in ("linter", "suite", "audit"):
            self.assertNotIn(' "%s"' % sub, t)


class LaIntegracionContinuaRevisaElPlan(unittest.TestCase):
    """`EP-023 · HU-007 · CA-02` · la revisión del plan se agrega a la
    integración continua que el proyecto ya tiene."""

    REPO = "https://ejemplo.invalid/cimiento.git"

    def setUp(self):
        self.raiz = carpeta(self)

    def poner(self, relativa, texto):
        escribir(os.path.join(self.raiz, *relativa.split("/")), texto)

    def ver(self, relativa):
        return leer(os.path.join(self.raiz, *relativa.split("/")))

    def test_con_github_crea_su_flujo_con_el_repo_como_dato(self):
        self.poner(".github/workflows/pruebas.yml", "name: pruebas\n")
        pasos = Instalador().instalar_ci(self.raiz, True, repo=self.REPO)
        self.assertIn("crear .github/workflows/cimiento.yml: la integración continua revisa el plan", pasos)
        texto = self.ver(CI_GITHUB)
        self.assertIn("CIMIENTO_REPO: " + self.REPO, texto)
        self.assertIn("plan --raiz", texto)
        self.assertIn('--rango "$DESDE..HEAD"', texto)

    def test_el_dato_del_proyecto_no_se_pisa(self):
        self.poner(".github/workflows/pruebas.yml", "name: pruebas\n")
        self.poner(CI_GITHUB, "CIMIENTO_REPO: el-del-proyecto\n")
        Instalador().instalar_ci(self.raiz, True, repo=self.REPO)
        self.assertEqual("CIMIENTO_REPO: el-del-proyecto\n", self.ver(CI_GITHUB))

    def test_con_gitlab_crea_su_archivo_y_lo_incluye(self):
        self.poner(".gitlab-ci.yml", "pruebas:\n  script: [make test]\n")
        Instalador().instalar_ci(self.raiz, True, repo=self.REPO)
        self.assertIn("CIMIENTO_REPO: " + self.REPO, self.ver(CI_GITLAB))
        self.assertIn("include:\n  - local: .cimiento-ci.yml", self.ver(".gitlab-ci.yml"))
        Instalador().instalar_ci(self.raiz, True, repo=self.REPO)
        self.assertEqual(1, self.ver(".gitlab-ci.yml").count("include:"))

    def test_gitlab_con_include_propio_no_se_toca_y_se_avisa(self):
        self.poner(".gitlab-ci.yml", "include:\n  - local: otro.yml\n")
        pasos = Instalador().instalar_ci(self.raiz, True, repo=self.REPO)
        self.assertTrue(any(p.startswith("AVISO") for p in pasos))
        self.assertEqual("include:\n  - local: otro.yml\n", self.ver(".gitlab-ci.yml"))

    def test_sin_integracion_continua_no_se_agrega(self):
        self.assertEqual(["sin integración continua: no se agrega la revisión del plan"],
                         Instalador().instalar_ci(self.raiz, True, repo=self.REPO))
        self.assertFalse(os.path.exists(os.path.join(self.raiz, ".github")))

    def test_sin_de_donde_descargar_no_se_agrega_y_se_dice(self):
        self.poner(".github/workflows/pruebas.yml", "name: pruebas\n")
        pasos = Instalador().instalar_ci(self.raiz, True, repo="")
        self.assertTrue(pasos[0].startswith("OMITIDO"))
        self.assertFalse(os.path.exists(os.path.join(self.raiz, *CI_GITHUB.split("/"))))


class LoQueLlegaDeAfueraSeInstala(unittest.TestCase):
    """`EP-005 · HU-015 · CA-04` · el portero se instala con su filtro y se
    reclama si falta."""

    def test_cp_006_se_instala_con_su_filtro_y_se_reclama_si_falta(self):
        proyecto = os.path.join(carpeta(self), "proyecto")
        os.makedirs(proyecto)
        estandar = ESTANDAR.replace("\\", "/")
        Instalador().instalar_claude(proyecto, estandar, aplicar=True)
        archivo = os.path.join(proyecto, ".claude", "settings.json")
        datos = json.loads(leer(archivo))
        grupos = [g for g in datos["hooks"]["PostToolUse"] if any("hook_externo.py" in h["command"] for h in g["hooks"])]
        self.assertEqual(1, len(grupos))
        for marca in ("WebFetch", "WebSearch", "Read", "mcp__.*"):
            self.assertIn(marca, grupos[0]["matcher"])
        self.assertTrue(Checklist(proyecto, estandar)._enganches_claude()[0])
        datos["hooks"]["PostToolUse"].remove(grupos[0])
        escribir(archivo, json.dumps(datos))
        ok, mensaje = Checklist(proyecto, estandar)._enganches_claude()
        self.assertFalse(ok)
        self.assertIn("hook_externo.py", mensaje)


# ── el instalador entero, sobre un estándar de mentira ───────────────────

class ConEstandarTemporal(unittest.TestCase):

    def setUp(self):
        self.proyecto = os.path.join(carpeta(self), "proyecto de prueba")
        os.makedirs(self.proyecto)
        contexto = estandar_temporal()
        self.estandar = contexto.__enter__()
        self.addCleanup(contexto.__exit__, None, None, None)
        self.instalador = Instalador(self.estandar)

    def _instalar(self):
        return callado(self.instalador.instalar, "proyecto de prueba", self.proyecto, aplicar=True)


class ElReadmeHeredadoSeCompleta(ConEstandarTemporal):
    """`EP-007 · HU-005` · el README heredado gana lo que la plantilla sumó, sin
    pisar lo que escribió el proyecto."""

    @property
    def readme(self):
        return os.path.join(self.proyecto, "historico-chat", "README.md")

    def _instalar(self):
        return self.instalador.instalar_historico(self.proyecto, aplicar=True)

    def _plantilla_gana_seccion(self, titulo="## Lo que el estándar sumó"):
        with io.open(self.instalador.plantilla_historico, "a", encoding="utf-8", newline="\n") as f:
            f.write("\n\n%s\n\nEsto es nuevo y tiene que llegar.\n" % titulo)
        return titulo.lstrip("# ").strip()

    def test_cp01_la_seccion_nueva_llega_al_proyecto_ya_instalado(self):
        self._instalar()
        titulo = self._plantilla_gana_seccion()
        pasos = self._instalar()
        self.assertTrue(any("lo que la plantilla sumó" in p for p in pasos), pasos)
        self.assertIn(titulo, leer(self.readme))
        self.assertIn("Esto es nuevo y tiene que llegar", leer(self.readme))

    def test_cp02_lo_que_el_proyecto_escribio_sigue_ahi(self):
        self._instalar()
        with io.open(self.readme, "a", encoding="utf-8", newline="\n") as f:
            f.write("\n\n## Cómo trabajamos acá\n\nEsto lo escribió el proyecto.\n")
        self._plantilla_gana_seccion()
        self._instalar()
        texto = leer(self.readme)
        self.assertIn("Cómo trabajamos acá", texto)
        self.assertIn("Esto lo escribió el proyecto.", texto)

    def test_cp03_sin_novedad_no_reescribe_nada(self):
        self._instalar()
        antes = leer(self.readme)
        pasos = self._instalar()
        self.assertEqual([], [p for p in pasos if "lo que la plantilla sumó" in p])
        self.assertEqual(antes, leer(self.readme))

    def test_cp04_la_seccion_llega_con_su_texto_no_vacia(self):
        self._instalar()
        self._plantilla_gana_seccion("## Con su cuerpo")
        self._instalar()
        texto = leer(self.readme)
        self.assertGreater(len(texto[texto.find("## Con su cuerpo"):].strip().splitlines()), 1)

    def test_cp05_el_sello_queda_al_dia(self):
        self._instalar()
        self._plantilla_gana_seccion()
        self._instalar()
        self.assertIn("<!-- huella:", leer(self.readme))

    def test_cp06_si_no_existe_se_crea_entero(self):
        self.assertTrue(any("crear historico-chat/README.md" in p for p in self._instalar()))
        self.assertTrue(os.path.isfile(self.readme))


class ReparaLoYaInstalado(ConEstandarTemporal):
    """`A-EP-007-HU-006` · un proyecto ya instalado queda al día reinstalando.
    Todos instalan dos veces: el defecto aparece al **volver** a instalar."""

    def _agente_config(self):
        return [os.path.join(self.proyecto, ".agente", n) for n in CONFIG_AGENTE]

    def _config_con_ruta(self):
        ruta = self.estandar.replace("\\", "/")
        for archivo in self._agente_config():
            if ruta in leer(archivo):
                return archivo
        self.fail("ningún archivo de .agente/ quedó citando al estándar")

    def test_cp_001_una_copia_con_el_marcador_crudo_queda_limpia(self):
        self._instalar()
        sucios = [os.path.join(self.proyecto, ".agente", "stack-instalacion.md"), self._config_con_ruta()]
        for archivo in sucios:
            escribir(archivo, leer(archivo).replace(self.estandar.replace("\\", "/"), MARCADOR_CRUDO))
            self.assertIn(MARCADOR_CRUDO, leer(archivo))
        self._instalar()
        for archivo in sucios:
            self.assertNotIn(MARCADOR_CRUDO, leer(archivo))
            self.assertIn(self.estandar.replace("\\", "/"), leer(archivo))

    def test_cp_002_la_plantilla_que_cambio_baja_al_proyecto(self):
        self._instalar()
        plantilla = os.path.join(self.estandar, "plantillas", "stack-instalacion.md")
        escribir(plantilla, leer(plantilla) + "\nLínea nueva de la prueba.\n")
        self._instalar()
        texto = leer(os.path.join(self.proyecto, ".agente", "stack-instalacion.md"))
        self.assertIn("Línea nueva de la prueba.", texto)
        self.assertNotIn(MARCADOR_CRUDO, texto)

    def test_cp_003_el_hueco_que_llena_el_proyecto_sobrevive(self):
        self._instalar()
        antes = {a: leer(a) for a in self._agente_config()}
        self.assertGreater(sum(t.count("«") for t in antes.values()), 0, "no quedó ningún hueco")
        self._instalar()
        for archivo in self._agente_config():
            self.assertEqual(leer(archivo), antes[archivo])

    def test_cp_004_sube_la_version_y_queda_el_registro(self):
        self._instalar()
        registro = RegistroDeVersiones(self.proyecto, self.estandar)
        primeros = registro.registros()
        self.assertTrue(primeros)
        escribir(os.path.join(self.estandar, "VERSION"), "99.0.0\n")
        self.assertEqual(VersionDelEstandar.vigente(self.estandar), "99.0.0")
        self._instalar()
        despues = registro.registros()
        self.assertEqual(len(despues), len(primeros) + 1)
        self.assertEqual(despues[-1][2], "99.0.0")
        texto = leer(os.path.join(registro.carpeta, despues[-1][0]))
        self.assertIn("99.0.0", texto)
        self.assertIn("Ninguno cambió de huella", texto)
        cumple, detalle = registro.revisar()
        self.assertTrue(cumple, detalle)
        faltan = Checklist.pendientes(Checklist(self.proyecto, self.estandar).revisar())
        self.assertEqual([p.id for p in faltan if p.id != "cadena"], [])

    def test_cp_004_el_propio_estandar_no_se_escribe_registros(self):
        self.assertEqual(self.instalador.registrar_version(self.estandar, {}, [], aplicar=True, anterior="1.0.0"), [])
        self.assertFalse(os.path.isdir(RegistroDeVersiones(self.estandar).carpeta))

    def test_cp_005_reinstalar_sin_novedad_no_agrega_registro(self):
        self._instalar()
        antes = len(RegistroDeVersiones(self.proyecto).registros())
        self._instalar()
        self.assertEqual(len(RegistroDeVersiones(self.proyecto).registros()), antes)


class PreparaSuPropiaSalida(ConEstandarTemporal):
    """`B-EP-007-HU-001` · el instalador prepara su propia salida: llamado como
    biblioteca no revienta con la consola de Windows."""

    @staticmethod
    def _consola_pobre():
        return io.TextIOWrapper(io.BytesIO(), encoding="cp1252", errors="strict")

    def test_cp_001_instalar_no_revienta_con_una_consola_pobre(self):
        with self.assertRaises(UnicodeEncodeError):
            self._consola_pobre().write("→")
        self._instalar()
        # La flecha sale al refrescar un sello viejo: por eso se sube la versión.
        escribir(os.path.join(self.estandar, "VERSION"), "99.0.0\n")
        original = sys.stdout
        sys.stdout = self._consola_pobre()
        try:
            self.instalador.instalar("proyecto de prueba", self.proyecto, aplicar=True)
            sys.stdout.flush()
            escrito = sys.stdout.buffer.getvalue().decode("utf-8", "replace")
        finally:
            sys.stdout = original
        self.assertIn("→", escrito)


def _md_instalados(raiz):
    salida = []
    for donde, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s != ".git"]
        salida += [os.path.join(donde, n) for n in sorted(archivos) if n.lower().endswith(".md")]
    return salida


class InstalacionSinMarcadores(unittest.TestCase):
    """`A-EP-007-HU-001` · ningún archivo copiado conserva un marcador que el
    instalador sabe llenar. El registro de proyectos va a una copia desechable."""

    nombre_carpeta = "proyecto de prueba"

    def setUp(self):
        tmp = carpeta(self)
        self.proyecto = os.path.join(tmp, self.nombre_carpeta)
        os.makedirs(self.proyecto)
        self.instalador = Instalador()
        self.instalador.registro = os.path.join(tmp, "proyectos.md")
        shutil.copy2(Instalador().registro, self.instalador.registro)

    def _instalar(self):
        return callado(self.instalador.instalar, self.nombre_carpeta, self.proyecto, aplicar=True)

    def _sin_llenar(self):
        marcadores = sorted(self.instalador.rellenos(self.proyecto))
        return [(os.path.relpath(a, self.proyecto), n, m) for a in _md_instalados(self.proyecto)
                for n, linea in enumerate(leer(a).splitlines(), 1) for m in marcadores if m in linea]

    def test_cp_001_ninguna_copia_conserva_un_marcador(self):
        self._instalar()
        self.assertTrue(_md_instalados(self.proyecto))
        self.assertEqual(self._sin_llenar(), [])

    def test_cp_002_la_ruta_del_estandar_quedo_escrita(self):
        self._instalar()
        texto = leer(os.path.join(self.proyecto, ".agente", "stack-instalacion.md"))
        self.assertNotIn("«RUTA-ESTANDAR»", texto)
        self.assertIn(self.instalador.estandar.replace("\\", "/"), texto)

    def test_cp_003_reinstalar_no_cambia_lo_que_ya_estaba_bien(self):
        self._instalar()
        antes = {a: leer(a) for a in _md_instalados(self.proyecto)}
        self._instalar()
        despues = {a: leer(a) for a in _md_instalados(self.proyecto)}
        self.assertEqual(sorted(antes), sorted(despues))
        self.assertEqual([a for a in antes if antes[a] != despues[a]], [])
        self.assertEqual(self._sin_llenar(), [])


class InstalacionEnRutaConTildes(InstalacionSinMarcadores):
    """CP-004 · lo mismo, en una carpeta con espacios y eñe."""
    nombre_carpeta = "proyecto de prueba ñ"


# ── el instalador por su orden, en un repositorio de verdad ──────────────

class ProyectoConGit(unittest.TestCase):
    """Un proyecto temporal con git, instalado por `main()` como lo haría la
    orden de consola. Al estar en la carpeta temporal, no va al registro real."""

    def setUp(self):
        self.registro = leer(Instalador().registro)

    def tearDown(self):
        self.assertEqual(self.registro, leer(Instalador().registro), "una prueba escribió en el registro real")

    def _proyecto(self, nombre="proyecto"):
        if not shutil.which("git"):
            self.skipTest("sin git")
        raiz = os.path.join(carpeta(self), nombre)
        os.makedirs(raiz)
        subprocess.run(["git", "init"], cwd=raiz, capture_output=True, timeout=30)
        return raiz

    def _instalar(self, raiz, aplicar):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            codigo = main([raiz] + (["--aplicar"] if aplicar else []))
        return Corrida(codigo, salida.getvalue())

    def _archivos(self, raiz):
        encontrados = {}
        for donde, dirs, archivos in os.walk(raiz):
            dirs[:] = [d for d in dirs if d != ".git"]
            for a in archivos:
                encontrados[os.path.relpath(os.path.join(donde, a), raiz)] = leer(os.path.join(donde, a))
        return encontrados

    def _ajustes(self, raiz):
        return json.loads(leer(os.path.join(raiz, ".claude", "settings.json")))


class RutasLargas(ProyectoConGit):
    """`EP-007 · HU-009` · el instalador deja puesto `core.longpaths`."""

    def _ajuste(self, raiz, *alcance):
        return subprocess.run(["git", "config", *alcance, "--get", "core.longpaths"], cwd=raiz,
                              capture_output=True, text=True, timeout=30).stdout.strip()

    def test_instalar_deja_core_longpaths_en_true(self):
        raiz = self._proyecto()
        self.assertEqual(self._ajuste(raiz, "--local"), "")
        salida = self._instalar(raiz, aplicar=True)
        self.assertEqual(salida.returncode, 0)
        self.assertEqual(self._ajuste(raiz, "--local"), "true")
        self.assertIn("core.longpaths", salida.stdout)

    def test_correrlo_dos_veces_no_repite_el_trabajo(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        self.assertIn("ya estaba puesto", self._instalar(raiz, aplicar=True).stdout)
        self.assertEqual(self._ajuste(raiz, "--local"), "true")

    def test_un_false_puesto_a_mano_no_se_pisa(self):
        raiz = self._proyecto()
        subprocess.run(["git", "config", "core.longpaths", "false"], cwd=raiz, capture_output=True, timeout=30)
        salida = self._instalar(raiz, aplicar=True)
        self.assertEqual(self._ajuste(raiz, "--local"), "false")
        self.assertIn("OMITIDO", salida.stdout)

    def test_el_modo_que_muestra_no_pone_el_ajuste(self):
        raiz = self._proyecto()
        self.assertIn("core.longpaths", self._instalar(raiz, aplicar=False).stdout)
        self.assertEqual(self._ajuste(raiz, "--local"), "")

    def test_no_se_toca_la_configuracion_global_de_la_maquina(self):
        antes = self._ajuste(ESTANDAR, "--global")
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=False)
        self.assertEqual(self._ajuste(ESTANDAR, "--global"), antes)
        self._instalar(raiz, aplicar=True)
        self.assertEqual(self._ajuste(ESTANDAR, "--global"), antes)
        # El valor **local**: si se hubiera escrito afuera, acá no habría nada.
        self.assertEqual(self._ajuste(raiz, "--local"), "true")

    def test_esta_escrito_que_hacer_al_ver_el_error(self):
        texto = leer(os.path.join(ESTANDAR, "cvds", "despliegue", "README.md"))
        for frase in ("Filename too long", "core.longpaths", "--global", "no viaja al clonar"):
            self.assertIn(frase, texto)


class MostrarAntesDeHacer(ProyectoConGit):
    """`EP-007 · HU-002` · el modo que muestra no toca nada, y lo que muestra es
    lo que hace."""

    def test_el_modo_que_muestra_no_escribe_ni_un_archivo(self):
        raiz = self._proyecto()
        antes = self._archivos(raiz)
        salida = self._instalar(raiz, aplicar=False)
        self.assertEqual(salida.returncode, 0)
        self.assertEqual(self._archivos(raiz), antes)
        self.assertIn("SIMULACIÓN", salida.stdout)

    def test_lo_que_muestra_es_lo_que_hace(self):
        raiz = self._proyecto()
        simulado = self._instalar(raiz, aplicar=False).stdout
        antes = set(self._archivos(raiz))
        self._instalar(raiz, aplicar=True)
        nuevos = set(self._archivos(raiz)) - antes
        self.assertTrue(nuevos)
        for archivo in nuevos:
            self.assertIn(os.path.basename(archivo), simulado, archivo)

    def test_limites_un_proyecto_al_dia_no_anuncia_trabajo(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        segunda = self._instalar(raiz, aplicar=False).stdout
        self.assertNotIn("(simulado) crear", segunda)
        self.assertIn("SIMULACIÓN", segunda)

    def test_claridad_cada_linea_dice_el_verbo_y_el_archivo(self):
        raiz = self._proyecto()
        lineas = [l.strip() for l in self._instalar(raiz, aplicar=False).stdout.splitlines() if "(simulado)" in l]
        self.assertTrue(lineas)
        for l in lineas:
            resto = l.split("(simulado)", 1)[1].strip()
            self.assertGreaterEqual(len(resto.split()), 2, l)
            self.assertFalse(resto.split()[0].startswith((".", "/", "\\")), l)


class EstructuraDeCarpetas(ProyectoConGit):
    """`EP-007 · HU-003` · las carpetas quedan creadas y lo que existía no se toca."""

    def test_instalar_dos_veces_deja_el_mismo_resultado(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        primera = self._archivos(raiz)
        self._instalar(raiz, aplicar=True)
        segunda = self._archivos(raiz)
        self.assertEqual(set(primera), set(segunda))
        self.assertEqual([a for a in primera if primera[a] != segunda[a] and "versiones" not in a], [])

    def test_compatibilidad_ruta_con_espacios_y_tildes(self):
        raiz = self._proyecto("proyecto de prueba con tildes áéíóú")
        self.assertEqual(self._instalar(raiz, aplicar=True).returncode, 0)
        self.assertTrue(os.path.isfile(os.path.join(raiz, "CLAUDE.md")))

    def test_limites_el_proyecto_completo_no_cambia_en_nada(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        antes = self._archivos(raiz)
        salida = self._instalar(raiz, aplicar=False)
        self.assertEqual(self._archivos(raiz), antes)
        self.assertNotIn("(simulado) crear", salida.stdout)


class GenerarLosAutomatismos(ProyectoConGit):
    """`EP-007 · HU-004` · los automatismos quedan puestos, sin duplicarse. El
    caso que corre cada enganche queda en la suite del adaptador."""

    def test_los_enganches_quedan_registrados_con_su_momento(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        puestos = json.dumps(self._ajustes(raiz).get("hooks", {}))
        for guion in ("hook_sesion.py", "hook_historico.py", "hook_recuerdos.py",
                      "hook_md.py", "hook_checklist.py", "hook_resumen.py"):
            self.assertIn(guion, puestos)

    def test_no_se_duplican_al_instalar_dos_veces(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        una = json.dumps(self._ajustes(raiz).get("hooks", {}))
        self._instalar(raiz, aplicar=True)
        self.assertEqual(una, json.dumps(self._ajustes(raiz).get("hooks", {})))

    def test_compatibilidad_la_ruta_generada_soporta_espacios(self):
        raiz = self._proyecto("carpeta con espacios")
        self._instalar(raiz, aplicar=True)
        self.assertIn("hook_sesion.py", json.dumps(self._ajustes(raiz).get("hooks", {})))


class NoPisarLoEscrito(ProyectoConGit):
    """`EP-007 · HU-005` · lo que la persona llenó no se pierde."""

    def test_el_archivo_modificado_a_mano_conserva_su_contenido(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        propio = os.path.join(raiz, ".agente", "stack.md")
        with io.open(propio, "a", encoding="utf-8") as f:
            f.write("\n## Lo que escribió la persona\n\nEsto no se puede perder.\n")
        self._instalar(raiz, aplicar=True)
        self.assertIn("Esto no se puede perder", leer(propio))

    def test_el_claude_md_con_texto_propio_sobrevive(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        claude = os.path.join(raiz, "CLAUDE.md")
        with io.open(claude, "a", encoding="utf-8") as f:
            f.write("\n## Regla propia del proyecto\n\nNo tocar los viernes.\n")
        self._instalar(raiz, aplicar=True)
        self.assertIn("No tocar los viernes", leer(claude))

    def test_los_enganches_de_git_si_se_reemplazan(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        gancho = os.path.join(raiz, ".githooks", "commit-msg")
        with io.open(gancho, "a", encoding="utf-8") as f:
            f.write("\n# lo escribió la persona\n")
        self._instalar(raiz, aplicar=True)
        self.assertNotIn("lo escribió la persona", leer(gancho))

    def test_limites_pisar_un_archivo_modificado_se_avisa(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        limpio = self._instalar(raiz, aplicar=False).stdout
        with io.open(os.path.join(raiz, ".githooks", "commit-msg"), "a", encoding="utf-8") as f:
            f.write("\n# lo escribió la persona\n")
        self.assertNotEqual(limpio, self._instalar(raiz, aplicar=False).stdout)

    def test_el_registro_de_version_dice_que_se_actualizo(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        donde = os.path.join(raiz, "documentacion", "versiones")
        registros = [n for n in os.listdir(donde) if n != "README.md"]
        self.assertTrue(registros)
        self.assertIn(leer(os.path.join(ESTANDAR, "VERSION")).strip(), leer(os.path.join(donde, registros[0])))


# ── preparar Cimiento (EP-025·HU-001) ────────────────────────────────────

class PrepararCimiento(unittest.TestCase):
    """La instalación del estándar deja lista la aplicación de Cimiento, y lo
    que no puede hacer lo dice sin detenerse. Las órdenes no se corren: se
    anotan, para no instalar npm ni tocar MariaDB desde una prueba."""

    def setUp(self):
        self.estandar = carpeta(self)
        self.cimiento = os.path.join(self.estandar, "proyectos", "cimiento")
        escribir(os.path.join(self.cimiento, "manage.py"), "")
        self.ordenes = []

    def con_ambiente(self):
        escribir(os.path.join(self.cimiento, ".venv", "Scripts", "python.exe"), "")

    def ejecutar(self, codigo=0, salida="La base «cimiento» está lista.", error=""):
        def falso(orden, **_):
            self.ordenes.append(orden)
            corrida = Corrida(codigo, salida if codigo == 0 else "")
            corrida.stderr = error
            return corrida
        return falso

    def test_en_simulacion_lo_anuncia_y_no_corre_nada(self):
        pasos = Instalador(self.estandar).preparar_cimiento(False, ejecutar=self.ejecutar())
        self.assertEqual(len(pasos), 1)
        self.assertIn("preparar_base", pasos[0])
        self.assertEqual(self.ordenes, [])

    def test_sin_ambiente_queda_dicho_y_no_corre_nada(self):
        pasos = Instalador(self.estandar).preparar_cimiento(True, ejecutar=self.ejecutar())
        self.assertTrue(pasos[0].startswith("OMITIDO"))
        self.assertIn("README", pasos[0])
        self.assertEqual(self.ordenes, [])

    def test_con_todo_instala_npm_y_prepara_la_base(self):
        self.con_ambiente()
        with mock.patch.object(modulo_instalar.shutil, "which", return_value="npm"):
            pasos = Instalador(self.estandar).preparar_cimiento(True, ejecutar=self.ejecutar())
        self.assertEqual([o[1:] for o in self.ordenes],
                         [["ci", "--no-audit", "--no-fund"], ["manage.py", "preparar_base"]])
        self.assertIn("está lista", pasos[-1])

    def test_con_node_modules_no_vuelve_a_instalar(self):
        self.con_ambiente()
        os.makedirs(os.path.join(self.cimiento, "node_modules"))
        Instalador(self.estandar).preparar_cimiento(True, ejecutar=self.ejecutar())
        self.assertEqual([o[1:] for o in self.ordenes], [["manage.py", "preparar_base"]])

    def test_sin_mariadb_queda_dicho_con_su_mensaje(self):
        self.con_ambiente()
        os.makedirs(os.path.join(self.cimiento, "node_modules"))
        apagada = self.ejecutar(1, error="CommandError: MariaDB no responde en 127.0.0.1:3307.")
        pasos = Instalador(self.estandar).preparar_cimiento(True, ejecutar=apagada)
        self.assertEqual(pasos, ["OMITIDO: MariaDB no responde en 127.0.0.1:3307."])

    def test_un_estandar_sin_cimiento_no_tiene_este_paso(self):
        otro = carpeta(self)
        self.assertEqual(Instalador(otro).preparar_cimiento(True, ejecutar=self.ejecutar()), [])

    def test_un_proyecto_que_no_es_el_estandar_no_lo_corre(self):
        proyecto = carpeta(self)
        instalador = Instalador(self.estandar)
        with mock.patch.object(instalador, "preparar_cimiento") as preparar, \
                mock.patch.object(instalador, "asegurar_pymysql") as pymysql:
            callado(instalador.instalar, "demo", proyecto, False)
        preparar.assert_not_called()
        pymysql.assert_not_called()


class LaLecturaDelConsumoQuedaProgramada(unittest.TestCase):
    """`EP-025·HU-006 · CP-004`: la instalación programa `leer_consumo` una vez al día."""

    def setUp(self):
        self.estandar = carpeta(self)
        self.cimiento = os.path.join(self.estandar, "proyectos", "cimiento")
        escribir(os.path.join(self.cimiento, "manage.py"), "")
        escribir(os.path.join(self.cimiento, ".venv", "Scripts", "python.exe"), "")
        self.ordenes = []

    def ejecutar(self, existe=False, crea=True):
        def falso(orden, **_):
            self.ordenes.append(orden)
            codigo = 0 if ("/Query" in orden and existe) or ("/Create" in orden and crea) else 1
            corrida = Corrida(codigo, "")
            corrida.stderr = "" if codigo == 0 else "ERROR: acceso denegado"
            return corrida
        return falso

    def programar(self, aplicar=True, sistema="nt", **kwargs):
        return Instalador(self.estandar).programar_lectura(aplicar, ejecutar=self.ejecutar(**kwargs), sistema=sistema)

    def test_en_simulacion_lo_anuncia(self):
        self.assertIn("programar la lectura", self.programar(aplicar=False)[0])
        self.assertEqual(self.ordenes, [])

    def test_crea_la_tarea_con_la_orden_de_cimiento(self):
        self.assertIn("programada una vez al día", self.programar()[0])
        crear = self.ordenes[-1]
        self.assertEqual(crear[:3], ["schtasks", "/Create", "/SC"])
        self.assertIn("leer_consumo", crear[crear.index("/TR") + 1])

    def test_si_ya_estaba_no_la_crea_otra_vez(self):
        self.assertEqual(["la lectura del consumo ya estaba programada"], self.programar(existe=True))
        self.assertEqual(1, len(self.ordenes))

    def test_si_falla_queda_dicho(self):
        self.assertIn("OMITIDO: no se pudo programar", self.programar(crea=False)[0])

    def test_fuera_de_windows_dice_como_hacerlo(self):
        pasos = self.programar(sistema="posix")
        self.assertTrue(pasos[0].startswith("OMITIDO: programar a mano"))
        self.assertIn("leer_consumo", pasos[0])
        self.assertEqual(self.ordenes, [])


class ActivarLaTelemetria(unittest.TestCase):
    """`EP-025·HU-007 · CP-004`: la instalación manda la telemetría de Claude Code a Cimiento."""

    def setUp(self):
        self.estandar = carpeta(self)
        self.cimiento = os.path.join(self.estandar, "proyectos", "cimiento")
        escribir(os.path.join(self.cimiento, "manage.py"), "")
        escribir(os.path.join(self.cimiento, ".env"), "PUERTO=8015\n")
        self.configuracion = os.path.join(carpeta(self), ".claude", "settings.json")

    def activar(self, aplicar=True):
        return Instalador(self.estandar).activar_telemetria(aplicar, configuracion=self.configuracion)

    def leer(self):
        with io.open(self.configuracion, encoding="utf-8") as f:
            return json.load(f)

    def test_sin_env_quedan_las_variables_y_lo_demas_sigue(self):
        escribir(self.configuracion, json.dumps({"permissions": {"allow": ["Bash(ls)"]}}))
        self.assertIn("telemetría hacia Cimiento activada", self.activar()[0])
        datos = self.leer()
        self.assertEqual({"allow": ["Bash(ls)"]}, datos["permissions"])
        self.assertEqual("1", datos["env"]["CLAUDE_CODE_ENABLE_TELEMETRY"])
        self.assertEqual("http/json", datos["env"]["OTEL_EXPORTER_OTLP_PROTOCOL"])
        self.assertEqual("http://127.0.0.1:8015/v1/logs", datos["env"]["OTEL_EXPORTER_OTLP_LOGS_ENDPOINT"])

    def test_no_pisa_lo_que_el_usuario_ya_tenia(self):
        escribir(self.configuracion, json.dumps({"env": {"OTEL_LOGS_EXPORTER": "console"}}))
        self.activar()
        self.assertEqual("console", self.leer()["env"]["OTEL_LOGS_EXPORTER"])

    def test_otra_vez_no_cambia_nada(self):
        self.activar()
        antes = self.leer()
        self.assertEqual(["la telemetría hacia Cimiento ya estaba activa"], self.activar())
        self.assertEqual(antes, self.leer())

    def test_en_simulacion_lo_anuncia_y_no_escribe(self):
        self.assertIn("activar la telemetría", self.activar(aplicar=False)[0])
        self.assertFalse(os.path.exists(self.configuracion))

    def test_sin_puerto_declarado_usa_el_8000(self):
        os.remove(os.path.join(self.cimiento, ".env"))
        self.activar()
        self.assertEqual("http://127.0.0.1:8000/v1/logs", self.leer()["env"]["OTEL_EXPORTER_OTLP_LOGS_ENDPOINT"])

    def test_json_invalido_no_se_toca(self):
        escribir(self.configuracion, "{roto")
        self.assertTrue(self.activar()[0].startswith("OMITIDO"))
        with io.open(self.configuracion, encoding="utf-8") as f:
            self.assertEqual("{roto", f.read())


class PyMySQLParaElFreno(unittest.TestCase):
    """`EP-025·HU-005 · CP-004`: la instalación deja PyMySQL donde corren los enganches."""

    def setUp(self):
        self.ordenes = []

    def sin_pymysql(self, nombre):
        raise ImportError(nombre)

    def ejecutar(self, codigo=0, error=""):
        def falso(orden, **_):
            self.ordenes.append(orden)
            corrida = Corrida(codigo, "")
            corrida.stderr = error
            return corrida
        return falso

    def test_si_ya_esta_no_hace_nada(self):
        pasos = Instalador.asegurar_pymysql(True, ejecutar=self.ejecutar(), importar=lambda n: None)
        self.assertEqual(pasos, ["PyMySQL ya estaba en el Python que corre los enganches"])
        self.assertEqual(self.ordenes, [])

    def test_en_simulacion_lo_anuncia(self):
        pasos = Instalador.asegurar_pymysql(False, ejecutar=self.ejecutar(), importar=self.sin_pymysql)
        self.assertIn("instalar PyMySQL", pasos[0])
        self.assertEqual(self.ordenes, [])

    def test_aplicando_lo_instala_con_el_mismo_python(self):
        pasos = Instalador.asegurar_pymysql(True, ejecutar=self.ejecutar(), importar=self.sin_pymysql)
        self.assertEqual(self.ordenes[0][:4], [sys.executable, "-m", "pip", "install"])
        self.assertIn("instalado", pasos[0])

    def test_si_falla_queda_dicho(self):
        pasos = Instalador.asegurar_pymysql(True, ejecutar=self.ejecutar(1, "ERROR: sin red"),
                                            importar=self.sin_pymysql)
        self.assertEqual(pasos, ["OMITIDO: no se pudo instalar PyMySQL: ERROR: sin red"])


if __name__ == "__main__":
    unittest.main()
