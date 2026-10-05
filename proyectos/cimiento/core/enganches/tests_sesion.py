"""Las pruebas del grupo «sesión»: el histórico, el enmascarado, los enganches
que acompañan cada mensaje, la traza, el respaldo, el corredor y los temas.

Son las de `validadores/pruebas.py` (`Historico`, `TranscripcionDeLaSesion`,
`RepartoDeLasReglas`, `ElGuionSeQuedaEnElRepositorio`,
`LasPruebasQueExistenSeCorren`, `TestPresupuesto` y las dos de renombrar de
`ResumenDeLaSesion`) y las de `validadores/tests/` que cubren estos módulos,
pasadas a sus clases. Las que corrían el enganche del adaptador como proceso
aparte llaman acá a la clase que decide: el adaptador se prueba con el suyo.

Todo corre sobre carpetas temporales; nunca sobre un `historico-chat/` real.
"""
import datetime
import hashlib
import inspect
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

from core.comun import AVISO, FALLA, Proyecto
from core.enganches.cargador import GATE, Cargador
from core.enganches.checkpoint import Checkpoint
from core.enganches.enmascarar import MARCA, Enmascarador
from core.enganches.externo import ContenidoExterno
from core.enganches.historico import INDICE, LIMITE, MARCA_NOMBRE, RESUMENES, Historico, Transcript
from core.enganches.presupuesto import TRAMO, Presupuesto
from core.enganches.rutas_fuera import DESTINO, RutasFuera
from core.enganches.veredicto import CopiaDelVeredicto
from core.herramientas.corredor import PLATAFORMA, SELLO, PruebasDelEstandar
from core.herramientas.respaldo import Respaldo
from core.herramientas.temas import IndiceTematico
from core.validadores.traza import Traza

ESTANDAR = Proyecto.estandar()
GUION_RESPALDO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                              "herramientas", "respaldo.py")


def escribir(ruta, texto="x", fecha=None):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    if fecha is not None:
        os.utime(ruta, (fecha, fecha))
    return ruta


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def huella(ruta):
    with open(ruta, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


class Temporal(unittest.TestCase):

    def temporal(self):
        tmp = tempfile.mkdtemp(prefix="cimiento-sesion-")
        self.addCleanup(shutil.rmtree, tmp, True)
        return tmp


# ── El histórico ─────────────────────────────────────────────────────────

class ElHistoricoSeEscribeSolo(Temporal):
    """El enganche que escribe la transcripción de la sesión (`pruebas.Historico`)."""

    def _carpeta(self, contenido=None):
        tmp = self.temporal()
        os.makedirs(os.path.join(tmp, "historico-chat"))
        if contenido is not None:
            escribir(os.path.join(tmp, "historico-chat", "2026-01-01-x.md"), contenido)
        return tmp

    def test_el_primer_mensaje_crea_el_archivo(self):
        ruta = Historico(self._carpeta()).anotar_usuario("s1", "hola")
        self.assertTrue(ruta, "un saludo también abre el histórico")
        texto = leer(ruta)
        self.assertIn("<!-- sesion: s1 -->", texto)
        self.assertIn("### 1 · Usuario — ", texto)
        self.assertIn("> hola", texto)

    def test_sin_carpeta_no_inventa_nada(self):
        tmp = self.temporal()
        self.assertEqual(Historico(tmp).anotar_usuario("s1", "hola"), "")
        self.assertEqual(os.listdir(tmp), [], "escribió en un proyecto que no tiene la carpeta")

    def test_el_mensaje_vacio_no_se_anota(self):
        self.assertEqual(Historico(self._carpeta()).anotar_usuario("s1", "   "), "")

    def test_sigue_la_numeracion_y_respeta_abierto(self):
        raiz = self._carpeta("<!-- sesion: s2 -->\n\n# t\n\n## Conversación\n\n"
                             "### 7 · Usuario — 2026-01-01 00:00:00\n> vieja\n\n"
                             "## Abierto\n- nada.\n")
        texto = leer(Historico(raiz).anotar_usuario("s2", "nueva"))
        self.assertIn("### 8 · Usuario — ", texto)
        self.assertLess(texto.index("### 8"), texto.index("## Abierto"),
                        "el mensaje nuevo quedó por debajo de `## Abierto`")

    def test_no_duplica_la_respuesta_si_el_enganche_repite(self):
        raiz = self._carpeta("<!-- sesion: s3 -->\n\n# t\n\n## Conversación\n")
        transcripcion = escribir(os.path.join(raiz, "t.jsonl"), "\n".join([
            json.dumps({"type": "user", "message": {"content": "pregunta"}}),
            json.dumps({"type": "assistant", "uuid": "u1",
                        "message": {"content": [{"type": "text", "text": "respuesta"}]}})]))
        historico = Historico(raiz)
        self.assertTrue(historico.anotar_agente("s3", transcripcion))
        self.assertEqual(historico.anotar_agente("s3", transcripcion), "")

    def test_la_respuesta_sin_mensaje_previo_no_tiene_donde_escribirse(self):
        raiz = self._carpeta()
        transcripcion = escribir(os.path.join(raiz, "t.jsonl"), json.dumps(
            {"type": "assistant", "uuid": "u1", "message": {"content": [{"type": "text", "text": "r"}]}}))
        self.assertEqual(Historico(raiz).anotar_agente("nadie", transcripcion), "")

    def test_la_sesion_queda_en_el_indice_aunque_el_readme_llegue_despues(self):
        # La línea del índice es lo único por lo que la próxima sesión
        # encuentra a esta: si al crear el archivo no había README, quedaba invisible.
        raiz = self._carpeta()
        historico = Historico(raiz)
        ruta = historico.anotar_usuario("s4", "primero")
        escribir(os.path.join(raiz, "historico-chat", "README.md"), "# Histórico\n\n## Índice\n\n")
        historico.anotar_usuario("s4", "segundo")
        indice = leer(os.path.join(raiz, "historico-chat", "README.md"))
        self.assertIn("(%s)" % os.path.basename(ruta), indice)
        self.assertEqual(indice.count(os.path.basename(ruta)), 2,
                         "la línea se duplicó: el índice no es idempotente")

    def test_el_indice_alimenta_el_arranque_de_la_proxima_sesion(self):
        raiz = self._carpeta()
        escribir(os.path.join(raiz, "historico-chat", "README.md"),
                 "# Histórico\n\n## Índice\n\n"
                 "- [2026-01-01-x.md](2026-01-01-x.md) — de qué se trató.\n"
                 "- [README.md](README.md) — no es una sesión.\n")
        historico = Historico(raiz)
        self.assertEqual(historico.sesiones(), [("2026-01-01-x.md", "de qué se trató.")])
        texto = historico.contexto()
        self.assertIn("historico-chat/2026-01-01-x.md — de qué se trató.", texto)
        self.assertNotIn("README.md", texto)

    def test_sin_sesiones_no_se_inyecta_nada(self):
        self.assertEqual(Historico(self._carpeta()).contexto(), "")

    def test_se_recortan_las_sesiones_viejas_y_se_dice(self):
        raiz = self._carpeta()
        filas = "".join("- [s%d.md](s%d.md) — tema %d.\n" % (n, n, n) for n in range(10))
        escribir(os.path.join(raiz, "historico-chat", "README.md"), "# Histórico\n\n## Índice\n\n" + filas)
        texto = Historico(raiz).contexto(limite=3)
        self.assertIn("últimas 3 de 10", texto)
        self.assertIn("s9.md", texto)
        self.assertNotIn("s6.md", texto, "se listó una fuera del recorte")

    def test_con_tope_cabe_y_dice_donde_esta_el_resto(self):
        """`EP-005·HU-009·CA-04`: el arranque tiene 10.000 caracteres para todo."""
        raiz = self._carpeta()
        lineas = ["- [2026-09-%02d-s.md](2026-09-%02d-s.md) — %s" % (i, i, "tema " * 20) for i in range(1, 41)]
        escribir(os.path.join(raiz, "historico-chat", "README.md"), "# Histórico\n\n" + "\n".join(lineas) + "\n")
        historico = Historico(raiz)
        texto = historico.contexto(tope=1000)
        self.assertLessEqual(len(texto), 1000)
        self.assertIn("historico-chat/README.md", texto)
        self.assertEqual(historico.contexto(), historico.contexto(LIMITE), "sin tope cambió lo de siempre")

    def test_junta_el_texto_partido_por_herramientas_y_descarta_lo_ajeno(self):
        filas = [
            {"type": "user", "message": {"content": "pregunta real"}},
            {"type": "assistant", "uuid": "a1", "message": {"content": [
                {"type": "thinking", "thinking": "razonamiento"},
                {"type": "text", "text": "Primero."},
                {"type": "tool_use", "name": "Bash"}]}},
            {"type": "user", "message": {"content": [{"type": "tool_result", "content": "salida cruda"}]}},
            {"type": "assistant", "uuid": "a2", "message": {"content": [{"type": "text", "text": "Después."}]}},
            {"type": "assistant", "uuid": "a3", "isSidechain": True,
             "message": {"content": [{"type": "text", "text": "subagente"}]}},
        ]
        ruta = escribir(os.path.join(self.temporal(), "t.jsonl"), "\n".join(json.dumps(x) for x in filas))
        self.assertEqual(Transcript.ultima_respuesta(ruta), ("Primero.\n\nDespués.", "a2"))

    def test_sin_transcript_no_hay_respuesta(self):
        self.assertEqual(Transcript.ultima_respuesta(""), ("", ""))
        self.assertEqual(Transcript.ultima_respuesta(os.path.join(self.temporal(), "no.jsonl")), ("", ""))

    def test_archivo_de_sesion_no_crea_nada(self):
        raiz = self._carpeta("<!-- sesion: abc -->\n")
        historico = Historico(raiz)
        self.assertTrue(historico.archivo_de_sesion("abc").endswith("2026-01-01-x.md"))
        self.assertEqual(historico.archivo_de_sesion("otra"), "")
        self.assertEqual(len(os.listdir(os.path.join(raiz, "historico-chat"))), 1)


class LaHoraYLaPrivacidad(Temporal):
    """La sesión se escribe sola, con la hora del reloj (`EP-005·HU-001`)."""

    def _carpeta(self):
        tmp = self.temporal()
        os.makedirs(os.path.join(tmp, "historico-chat"))
        return tmp

    def _texto(self, raiz):
        carpeta = os.path.join(raiz, "historico-chat")
        archivos = [n for n in os.listdir(carpeta) if n.endswith(".md")]
        self.assertTrue(archivos, "no nació el archivo de la sesión")
        return leer(os.path.join(carpeta, archivos[0]))

    def test_la_hora_viene_del_reloj_y_no_del_texto_del_mensaje(self):
        """CA-02. Si el programa copiara la hora que dice el texto, bastaría
        escribir «10:00» para falsear el histórico."""
        raiz = self._carpeta()
        Historico(raiz).anotar_usuario("s1", "eran las 03:33 de la madrugada")
        texto = self._texto(raiz)
        self.assertIn("03:33", texto, "no se guardó el mensaje")
        self.assertIn(datetime.date.today().isoformat(), texto, "la fecha no es la del reloj")

    def test_privacidad_la_clave_asignada_no_queda_en_claro(self):
        """**Corregida al pasarla.** La vieja decía que «nada enmascara» y
        afirmaba que `mi clave es abc123def` quedaba en claro: pasaba, pero
        porque esa frase no tiene forma de asignación, no porque nada tapara.
        Desde `EP-005·HU-002` sí se tapa; se prueban las dos mitades."""
        raiz = self._carpeta()
        historico = Historico(raiz)
        historico.anotar_usuario("s1", "mi clave es " + "abc" + "123def")
        historico.anotar_usuario("s1", "clave=" + "abc" + "123def")
        texto = self._texto(raiz)
        self.assertEqual(1, texto.count("abc123def"), "la clave asignada quedó en claro")
        self.assertIn("mi clave es abc123def", texto, "se tapó una frase sin asignación")
        self.assertIn("clave=" + MARCA, texto)


class LosTurnosSeLeen(unittest.TestCase):
    """`EP-011·HU-001` · Quien escribe el formato es quien sabe leerlo."""

    @staticmethod
    def transcripcion(*turnos):
        partes = ["<!-- sesion: abc -->\n\n# 2026-01-02 — Sesión\n\n## Conversación\n"]
        for i, (quien, dicho) in enumerate(turnos, 1):
            if quien == "usuario":
                cita = "\n".join("> %s" % l for l in dicho.split("\n"))
                partes.append("\n### %d · Usuario — 2026-01-02 10:0%d:00\n%s\n" % (i, i, cita))
            else:
                partes.append("\n**Agente** — 2026-01-02 10:0%d:30\n<!-- agente: %d -->\n\n%s\n" % (i, i, dicho))
        return "".join(partes)

    def test_el_turno_del_usuario_se_reconoce(self):
        self.assertEqual([("usuario", "2026-01-02 10:01:00", "hola")],
                         Historico.turnos(self.transcripcion(("usuario", "hola"))))

    def test_el_turno_del_agente_se_reconoce(self):
        turnos = Historico.turnos(self.transcripcion(("agente", "qué tal")))
        self.assertEqual(("agente", "qué tal"), (turnos[0][0], turnos[0][2]))

    def test_van_en_el_orden_de_la_conversacion(self):
        turnos = Historico.turnos(self.transcripcion(("usuario", "uno"), ("agente", "dos"), ("usuario", "tres")))
        self.assertEqual(["usuario", "agente", "usuario"], [t[0] for t in turnos])

    def test_la_cita_del_usuario_se_desarma(self):
        self.assertEqual("primera\nsegunda",
                         Historico.turnos(self.transcripcion(("usuario", "primera\nsegunda")))[0][2])

    def test_el_sello_de_maquina_no_es_parte_de_lo_dicho(self):
        self.assertNotIn("<!-- agente:", Historico.turnos(self.transcripcion(("agente", "respuesta")))[0][2])

    def test_la_hora_es_la_que_el_enganche_anoto(self):
        self.assertEqual("2026-01-02 10:01:30", Historico.turnos(self.transcripcion(("agente", "x")))[0][1])

    def test_lo_que_no_encaja_no_se_inventa(self):
        self.assertEqual([], Historico.turnos("# Un documento cualquiera\n"))
        self.assertEqual([], Historico.turnos(""))
        self.assertEqual([], Historico.turnos(None))
        self.assertEqual(1, len(Historico.turnos(self.transcripcion(("usuario", "hola")))))

    def test_una_sesion_real_se_parte_en_turnos(self):
        """Contra lo que el enganche escribió, no contra lo inventado. Solo lee."""
        carpeta = os.path.join(ESTANDAR or "", "historico-chat")
        nombres = sorted((n for n in os.listdir(carpeta) if n.endswith(".md") and n[:4].isdigit()),
                         reverse=True) if os.path.isdir(carpeta) else []
        if not nombres:
            self.skipTest("no hay transcripciones en este repositorio")
        with io.open(os.path.join(carpeta, nombres[0]), encoding="utf-8", errors="replace") as f:
            turnos = Historico.turnos(f.read())
        self.assertGreater(len(turnos), 0)
        self.assertTrue(all(t[0] in ("usuario", "agente") and t[2] for t in turnos))


class RenombrarLaSesion(Temporal):
    """`historico.py --renombrar` mueve la transcripción, la titula, corrige el
    índice y arrastra el resumen con su enlace de vuelta (`B-EP-005-HU-008`)."""

    FECHA = "2026-01-02"
    VIEJO = "2026-01-02-sesion.md"
    TEMA = "el-tema-real"
    NUEVO = "2026-01-02-el-tema-real.md"
    AJENA = "2026-01-01-otra.md"

    def setUp(self):
        self.carpeta = os.path.join(self.temporal(), "historico-chat")
        self.dia = os.path.join(self.carpeta, RESUMENES, self.FECHA)
        os.makedirs(self.dia)
        escribir(os.path.join(self.carpeta, self.VIEJO), "# %s — Sesión\n\nLo que se conversó.\n" % self.FECHA)
        escribir(os.path.join(self.carpeta, INDICE),
                 "# Histórico\n\n- [%s](%s) — sesión del %s.\n" % (self.VIEJO, self.VIEJO, self.FECHA))

    def _resumen(self, con_ajena=False):
        texto = ("# %s · lo que quedó\n\nHallazgos de la sesión transcrita en "
                 "[historico-chat/%s](../../%s).\n" % (self.FECHA, self.VIEJO, self.VIEJO))
        if con_ajena:
            texto += "\nViene de [historico-chat/%s](../../%s).\n" % (self.AJENA, self.AJENA)
        return escribir(os.path.join(self.dia, self.VIEJO[len(self.FECHA) + 1:]), texto)

    def test_el_resumen_arrastrado_apunta_al_nombre_nuevo_y_abre(self):
        viejo_resumen = self._resumen()
        Historico.renombrar(os.path.join(self.carpeta, self.VIEJO), self.TEMA)
        nuevo_resumen = os.path.join(self.dia, "%s.md" % self.TEMA)
        self.assertTrue(os.path.isfile(nuevo_resumen), "el resumen no se arrastró")
        self.assertFalse(os.path.exists(viejo_resumen), "quedó el resumen con el nombre viejo")
        texto = leer(nuevo_resumen)
        self.assertIn("[historico-chat/%s](../../%s)" % (self.NUEVO, self.NUEVO), texto)
        self.assertNotIn(self.VIEJO, texto, "quedó una mención al nombre viejo de la sesión")
        self.assertTrue(os.path.isfile(os.path.normpath(os.path.join(self.dia, "../..", self.NUEVO))),
                        "el enlace apunta a algo que no está")

    def test_el_enlace_a_otra_sesion_no_se_toca(self):
        self._resumen(con_ajena=True)
        Historico.renombrar(os.path.join(self.carpeta, self.VIEJO), self.TEMA)
        texto = leer(os.path.join(self.dia, "%s.md" % self.TEMA))
        self.assertIn("[historico-chat/%s](../../%s)" % (self.NUEVO, self.NUEVO), texto)
        self.assertIn("[historico-chat/%s](../../%s)" % (self.AJENA, self.AJENA), texto,
                      "se le cambió el enlace a una sesión que no era")

    def test_sin_resumen_no_revienta_y_el_indice_queda_al_dia(self):
        shutil.rmtree(os.path.join(self.carpeta, RESUMENES))
        ruta = Historico.renombrar(os.path.join(self.carpeta, self.VIEJO), self.TEMA, "prueba")
        self.assertTrue(os.path.isfile(ruta), "no se renombró la transcripción")
        self.assertIn("[%s](%s) — prueba." % (self.NUEVO, self.NUEVO), leer(os.path.join(self.carpeta, INDICE)))
        self.assertIn("# %s — El tema real" % self.FECHA, leer(ruta))

    def test_el_tema_vacio_y_el_archivo_que_no_esta_se_rechazan(self):
        with self.assertRaises(ValueError):
            Historico.renombrar(os.path.join(self.carpeta, self.VIEJO), "--")
        with self.assertRaises(FileNotFoundError):
            Historico.renombrar(os.path.join(self.carpeta, "no-esta.md"), "x")

    def test_el_enlace_al_resumen_dice_donde_vive(self):
        """`EP-004·HU-008·CA-04`: el texto del enlace cumple `13·DOC14`."""
        escribir(os.path.join(self.carpeta, "resumenes", "2026-01-01", "tema.md"), "# x\n")
        self.assertEqual(" · [historico-chat/resumenes/2026-01-01/tema.md](resumenes/2026-01-01/tema.md)",
                         Historico._enlace_al_resumen(self.carpeta, "2026-01-01-tema.md"))


class RenombrarConElModeloDelResumen(Temporal):
    """Las dos de renombrar de `pruebas.ResumenDeLaSesion` (CP-003)."""

    def _sesion(self):
        raiz = self.temporal()
        os.makedirs(os.path.join(raiz, "historico-chat", "resumenes", "2026-08-14"))
        return escribir(os.path.join(raiz, "historico-chat", "2026-08-14-sesion.md"),
                        "<!-- sesion: x -->\n\n# 2026-08-14 — Sesión\n")

    def test_renombrar_mueve_tambien_el_resumen(self):
        ruta = self._sesion()
        dia = os.path.join(os.path.dirname(ruta), "resumenes", "2026-08-14")
        escribir(os.path.join(dia, "sesion.md"), "# lo que quedó\n")
        Historico.renombrar(ruta, "maracuya", "prueba")
        self.assertTrue(os.path.isfile(os.path.join(dia, "maracuya.md")))
        self.assertFalse(os.path.isfile(os.path.join(dia, "sesion.md")))

    def test_renombrar_sin_resumen_no_falla(self):
        ruta = self._sesion()
        Historico.renombrar(ruta, "pepito", "prueba")
        self.assertTrue(os.path.isfile(os.path.join(os.path.dirname(ruta), "2026-08-14-pepito.md")))


class ElNombreSePideUnaVez(Temporal):
    """`aviso_de_nombre` no tenía ninguna prueba en la batería vieja."""

    def _sesion(self, nombre="2026-01-02-sesion.md", con_respuesta=True):
        carpeta = os.path.join(self.temporal(), "historico-chat")
        texto = "<!-- sesion: s -->\n\n# 2026-01-02 — Sesión\n"
        if con_respuesta:
            texto += "\n**Agente** — 2026-01-02 10:00:00\n\nhola\n"
        return escribir(os.path.join(carpeta, nombre), texto)

    def test_se_pide_una_sola_vez_y_deja_la_marca(self):
        ruta = self._sesion()
        aviso = Historico.aviso_de_nombre(ruta)
        self.assertIn("TODAVÍA NO TIENE NOMBRE", aviso)
        self.assertIn("--renombrar", aviso)
        self.assertIn(os.path.abspath(inspect.getfile(Historico)).replace(os.sep, "/"), aviso,
                      "la orden no apunta al módulo que renombra")
        self.assertEqual(MARCA_NOMBRE, leer(ruta).split("\n")[1])
        self.assertEqual("", Historico.aviso_de_nombre(ruta), "se pidió dos veces")

    def test_calla_sin_respuesta_con_tema_o_sin_ruta(self):
        self.assertEqual("", Historico.aviso_de_nombre(self._sesion(con_respuesta=False)))
        self.assertEqual("", Historico.aviso_de_nombre(self._sesion("2026-01-02-con-tema.md")))
        self.assertEqual("", Historico.aviso_de_nombre(""))

    def test_la_orden_del_aviso_corre(self):
        """La orden que se le da al agente tiene que funcionar tal cual."""
        ruta = self._sesion()
        r = subprocess.run([sys.executable, inspect.getfile(Historico), "--renombrar", ruta, "--tema", "ya va"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertTrue(os.path.isfile(os.path.join(os.path.dirname(ruta), "2026-01-02-ya-va.md")))


# ── El enmascarado ────────────────────────────────────────────────────────

class SeTapaLaClave(Temporal):
    """`EP-005·HU-002` y el pendiente 84: la clave se tapa antes de escribirse."""

    def tapa(self, texto):
        salida, cuantas = Enmascarador.enmascarar(texto)
        return cuantas, salida

    def test_las_formas_que_delatan_un_proveedor(self):
        for clave in ("AKIA1234567890ABCDEF", "ghp_abcdefghijklmnopqrstuvwxyz012345",
                      "xoxb-1234567890-abcdefghij", "sk_live_abcdefghijklmnop1234"):
            with self.subTest(clave=clave[:12]):
                n, t = self.tapa("pegá esto: %s y listo" % clave)
                self.assertEqual(1, n)
                self.assertNotIn(clave, t)
                self.assertIn(MARCA, t)

    def test_la_variable_con_pinta_de_clave_y_se_tapa_solo_el_valor(self):
        n, t = self.tapa('password: "S3creto-de-verdad"')
        self.assertEqual(1, n)
        self.assertNotIn("S3creto", t)
        self.assertIn("password", t)

    def test_varias_lineas(self):
        n, t = self.tapa("uno\nAKIA1234567890ABCDEF\ntres")
        self.assertEqual(1, n)
        self.assertIn("uno", t)
        self.assertIn("tres", t)

    def test_la_asignacion_sin_comillas(self):
        n, t = self.tapa("API_KEY=supersecreto123456")
        self.assertEqual(1, n)
        self.assertIn(Enmascarador.MARCA, t)
        self.assertIn("API_KEY", t, "se tapa el valor, no la variable")
        self.assertNotIn("MiClave123456", self.tapa("password: MiClave123456")[1])
        self.assertEqual(1, self.tapa("la contraseña: Patito2026")[0])
        self.assertEqual(1, self.tapa("secret=abcdefghijklmnop")[0])

    def test_la_asignacion_con_comillas_sigue_tapandose(self):
        n, t = self.tapa('API_KEY="supersecreto123456"')
        self.assertEqual(1, n)
        self.assertNotIn("supersecreto123456", t)

    def test_hay_clave_avisa_sin_reescribir(self):
        self.assertTrue(Enmascarador.hay_clave("AKIA1234567890ABCDEF"))
        self.assertFalse(Enmascarador.hay_clave("nada que tapar"))

    # La mitad del trabajo: lo que NO hay que tapar.

    def test_el_molde_no_se_tapa(self):
        for molde in ("tu-clave-aqui", "changeme", "your_api_key", "<TU-CLAVE>"):
            with self.subTest(molde=molde):
                n, t = self.tapa('password: "%s"' % molde)
                self.assertEqual(0, n)
                self.assertIn(molde, t)
        self.assertEqual(0, self.tapa("password: changeme")[0])

    def test_leer_del_entorno_no_se_tapa(self):
        for linea in ('password: os.environ["X"]', 'api_key = env("CLAVE")', "secret: process.env.TOKEN",
                      "API_KEY=os.environ['MI_CLAVE_LARGA']"):
            with self.subTest(linea=linea):
                self.assertEqual(0, self.tapa(linea)[0])

    def test_el_codigo_pegado_y_lo_corto_no_se_tapan(self):
        n, t = self.tapa("clave = h.regla or algo")
        self.assertEqual(0, n)
        self.assertIn("h.regla", t)
        self.assertEqual(0, self.tapa("token: xyz")[0])

    def test_el_texto_sin_claves_no_se_toca(self):
        for original in ("esto es un mensaje normal\ncon dos líneas\n",
                         "La clave del asunto es que el proceso sirva antes de automatizarlo."):
            self.assertEqual((0, original), self.tapa(original))
        self.assertEqual(("", 0), Enmascarador.enmascarar(""))

    def test_no_reescribe_de_mas(self):
        _, t = self.tapa("uno\n\ndos\nAKIA1234567890ABCDEF\n")
        self.assertEqual(4, len(t.splitlines()))
        self.assertTrue(t.endswith("\n"))
        _, t = self.tapa("primera línea\nAPI_KEY=supersecreto123456\ntercera línea\n")
        self.assertEqual(3, len(t.splitlines()))
        self.assertTrue(t.startswith("primera línea\n") and t.endswith("tercera línea\n"))

    # De punta a punta, por el camino real.

    def _anotado(self, mensaje):
        raiz = self.temporal()
        os.makedirs(os.path.join(raiz, "historico-chat"))
        return leer(Historico(raiz).anotar_usuario("s-1", mensaje))

    def test_el_mensaje_del_usuario_llega_tapado_y_entero(self):
        escrito = self._anotado("la clave es AKIA1234567890ABCDEF, guardala")
        self.assertNotIn("AKIA1234567890ABCDEF", escrito)
        self.assertIn(MARCA, escrito)
        self.assertIn("guardala", escrito)

    def test_se_tapa_antes_de_escribir_no_despues(self):
        """Lo que se fija es dónde vive la llamada: dentro de `anotar_usuario`,
        antes del `_anotar`. Si alguien la mueve después, la de arriba se cae."""
        fuente = inspect.getsource(Historico.anotar_usuario)
        self.assertIn("Enmascarador.enmascarar(mensaje)", fuente)
        self.assertLess(fuente.index("Enmascarador.enmascarar"), fuente.index("_anotar("))


# ── Los enganches que deciden ─────────────────────────────────────────────

class LoDeAfueraLlegaMarcado(Temporal):
    """`EP-005·HU-015`. Las del enganche, contra la clase que decide."""

    INTERNAS = ("Write", "Edit", "Bash", "Glob", "Grep")

    def test_la_pagina_trae_herramienta_origen_y_regla_en_tres_lineas(self):
        texto = ContenidoExterno.sobre("WebFetch", {"url": "https://ejemplo.test/pagina"}, self.temporal())
        for parte in ("WebFetch", "https://ejemplo.test/pagina", "dato", "C27"):
            self.assertIn(parte, texto)
        self.assertLessEqual(len(texto.splitlines()), 3)

    def test_mcp_nombra_servidor_y_herramienta(self):
        self.assertTrue(ContenidoExterno.es_externa("mcp__gmail__leer_correo", {"id": "123"}))
        texto = ContenidoExterno.sobre("mcp__gmail__leer_correo", {"id": "123"})
        self.assertIn("gmail", texto)
        self.assertIn("leer_correo", texto)

    def test_el_archivo_de_fuera_nombra_su_ruta(self):
        raiz = self.temporal()
        afuera = os.path.join(tempfile.gettempdir(), "cimiento-afuera", "doc.pdf")
        self.assertTrue(ContenidoExterno.es_externa("Read", {"file_path": afuera}, raiz))
        self.assertIn(afuera, ContenidoExterno.sobre("Read", {"file_path": afuera}, raiz))

    def test_lo_de_adentro_calla(self):
        raiz = self.temporal()
        self.assertFalse(ContenidoExterno.es_externa("Read", {"file_path": os.path.join(raiz, "README.md")}, raiz))
        for nombre in self.INTERNAS:
            self.assertFalse(ContenidoExterno.es_externa(nombre, {"x": 1}, raiz), nombre)

    def test_sin_argumentos_no_inventa_origen(self):
        self.assertTrue(ContenidoExterno.es_externa("WebFetch"))
        self.assertNotIn("origen", ContenidoExterno.sobre("WebFetch"))
        self.assertIn("WebFetch", ContenidoExterno.sobre("WebFetch", "cadena"))

    def test_decide_por_nombre_y_ruta(self):
        raiz = os.path.abspath("proyecto")
        self.assertTrue(ContenidoExterno.es_externa("WebSearch"))
        self.assertTrue(ContenidoExterno.es_externa("mcp__drive__bajar"))
        self.assertFalse(ContenidoExterno.es_externa("Read", {"file_path": os.path.join(raiz, "a.md")}, raiz))
        self.assertTrue(ContenidoExterno.es_externa("Read", {"file_path": os.path.abspath("otro/a.md")}, raiz))
        self.assertFalse(ContenidoExterno.es_externa("Read", {}, raiz))
        self.assertFalse(ContenidoExterno.es_externa("Bash", {"command": "curl x"}, raiz))

    def test_el_origen_de_cada_clase(self):
        self.assertEqual("https://a.b", ContenidoExterno.origen("WebFetch", {"url": "https://a.b"}))
        self.assertIn("drive", ContenidoExterno.origen("mcp__drive__bajar"))
        self.assertIn("bajar", ContenidoExterno.origen("mcp__drive__bajar"))
        self.assertEqual("", ContenidoExterno.origen("WebFetch", None))


class ElConsumoSeVe(unittest.TestCase):
    """`TestPresupuesto` y `EP-005·HU-014`: sumar y avisar por tramo, sin detener nada."""

    def test_suma_y_total(self):
        r = Presupuesto.resumen([{"entrada": 100, "salida": 20, "cache": 5}, {"entrada": 50, "salida": 30}])
        self.assertEqual((2, 150, 50, 5, 200), (r["turnos"], r["entrada"], r["salida"], r["cache"], r["total"]))

    def test_umbral(self):
        r = Presupuesto.resumen([{"entrada": 900, "salida": 200}])
        self.assertTrue(Presupuesto.excedido(r, 1000))
        self.assertFalse(Presupuesto.excedido(r, 2000))
        self.assertFalse(Presupuesto.excedido(r, 0))
        self.assertIn("AVISO", Presupuesto.como_texto(r, 1000))
        self.assertNotIn("AVISO", Presupuesto.como_texto(r))

    def test_el_reporte_de_cierre_no_cambia(self):
        r = Presupuesto.resumen([{"entrada": 100, "salida": 20, "cache": 5}, {"entrada": 50, "salida": 30}])
        self.assertIn("Consumo de la sesión: 2 turno(s) · 150 fichas de entrada · 50 de salida · "
                      "5 leídas de caché", Presupuesto.como_texto(r))

    def test_al_cruzar_un_tramo_se_avisa_una_vez(self):
        turnos = [{"entrada": 500_000}, {"entrada": 450_000}, {"entrada": 100_000}]
        cruzo, numero, totales = Presupuesto.cruzo_tramo(turnos)
        self.assertTrue(cruzo)
        aviso = Presupuesto.aviso_de_tramo(totales, numero)
        self.assertIn("TRAMO 1", aviso)
        self.assertIn("1,050,000", aviso)
        self.assertFalse(Presupuesto.cruzo_tramo(turnos + [{"entrada": 10_000}])[0], "avisó dentro del mismo tramo")
        cruzo, numero, _ = Presupuesto.cruzo_tramo(turnos + [{"entrada": 10_000}, {"entrada": 990_000}])
        self.assertEqual((True, 2), (cruzo, numero))

    def test_exactamente_el_tramo_y_el_umbral_apagado(self):
        self.assertFalse(Presupuesto.cruzo_tramo([{"entrada": 999_998}, {"entrada": 1}])[0])
        self.assertEqual((True, 1), Presupuesto.cruzo_tramo([{"entrada": 999_999}, {"entrada": 1}])[:2])
        self.assertFalse(Presupuesto.cruzo_tramo([{"entrada": 5_000_000}], 0)[0])
        self.assertFalse(Presupuesto.cruzo_tramo([])[0])

    def test_la_cache_no_cuenta_y_el_tramo_es_un_millon(self):
        self.assertFalse(Presupuesto.cruzo_tramo([{"entrada": 10, "cache": 5_000_000}])[0])
        self.assertEqual(1_000_000, TRAMO)


class ElGuionSeQuedaEnElRepositorio(Temporal):
    """`EP-005·HU-018`. Lo que se vigila no es que avise: es que NO avise de más."""

    def _casa(self, nombre="agente"):
        padre = self.temporal()
        casa = os.path.join(padre, nombre)
        os.makedirs(os.path.join(casa, "validadores"))
        os.makedirs(os.path.join(casa, "historico-chat", "scripts"))
        return padre, casa

    def test_escribir_fuera_avisa_y_dice_donde_iba(self):
        padre, casa = self._casa()
        texto = RutasFuera.aviso(os.path.join(padre, "suelto.py"), casa)
        self.assertIn("suelto.py", texto)
        self.assertIn(DESTINO, texto)

    def test_no_avisa_por_las_rutas_del_proyecto(self):
        _, casa = self._casa()
        for ruta in (os.path.join(casa, "validadores", "x.py"),
                     os.path.join(casa, "historico-chat", "scripts", "y.py"),
                     os.path.join(casa, "README.md"), casa,
                     os.path.join(casa, "validadores", "..", "README.md"),
                     casa + "/validadores/x.py", casa + "\\validadores\\x.py"):
            self.assertEqual(RutasFuera.aviso(ruta, casa), "", ruta)

    def test_no_avisa_por_una_ruta_relativa_dentro_del_proyecto(self):
        """La relativa es la única que distingue resolver de no resolver."""
        _, casa = self._casa()
        antes = os.getcwd()
        os.chdir(casa)
        self.addCleanup(os.chdir, antes)
        for ruta in ("README.md", os.path.join("validadores", "x.py"), "."):
            self.assertEqual(RutasFuera.aviso(ruta, casa), "", ruta)

    def test_la_carpeta_hermana_con_el_mismo_prefijo_si_avisa(self):
        padre, casa = self._casa("agente")
        self.assertTrue(RutasFuera.aviso(os.path.join(padre, "agente-viejo", "x.py"), casa))

    def test_una_ruta_que_empieza_dentro_y_termina_fuera_avisa(self):
        _, casa = self._casa()
        self.assertTrue(RutasFuera.aviso(os.path.join(casa, "validadores", "..", "..", "afuera.py"), casa))

    def test_no_revienta_con_entradas_malas(self):
        _, casa = self._casa()
        for ruta in ("", None, "   "):
            self.assertEqual(RutasFuera.aviso(ruta, casa), "", repr(ruta))
        self.assertEqual(RutasFuera.aviso("x.py", ""), "")

    def test_si_la_ruta_no_se_deja_resolver_se_calla(self):
        """Se fuerza el fallo: una prueba que no toca la rama que dice probar
        es peor que no tenerla."""
        _, casa = self._casa()
        original = os.path.realpath

        def revienta(_ruta):
            raise OSError("de mentira, para tocar la rama")

        os.path.realpath = revienta
        self.addCleanup(setattr, os.path, "realpath", original)
        self.assertEqual(RutasFuera.aviso(os.path.join(casa, "..", "x.py"), casa), "")


class ElCheckpointSeReclama(Temporal):
    """`EP-005·HU-013`. Las fechas se fuerzan con `os.utime` (`08·T3`)."""

    def setUp(self):
        self.tmp = self.temporal()
        self.fase = os.path.join(self.tmp, "documentacion", "epicas", "EP-001-prueba", "HU-001-prueba",
                                 "A-EP-001-HU-001-prueba")
        os.makedirs(self.fase)

    def test_sin_checkpoint_se_avisa_y_se_nombra_la_fase(self):
        ruta = escribir(os.path.join(self.fase, "resultado_pruebas.md"))
        hallazgo = Checkpoint.rezago(ruta)
        self.assertEqual(("falta", self.fase, "resultado_pruebas.md"), hallazgo)
        texto = Checkpoint.como_texto(hallazgo, self.tmp)
        self.assertIn("SIN CHECKPOINT", texto)
        self.assertIn("documentacion/epicas/EP-001-prueba/HU-001-prueba/A-EP-001-HU-001-prueba", texto)

    def test_atrasado_se_avisa_con_el_documento(self):
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=1000)
        ruta = escribir(os.path.join(self.fase, "funcionalidad_implementada.md"), fecha=2000)
        texto = Checkpoint.como_texto(Checkpoint.rezago(ruta), self.tmp)
        self.assertIn("QUEDÓ ATRÁS", texto)
        self.assertIn("funcionalidad_implementada.md", texto)
        self.assertIn("A-EP-001-HU-001-prueba", texto)

    def test_al_dia_calla(self):
        ruta = escribir(os.path.join(self.fase, "funcionalidad_implementada.md"), fecha=2000)
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=3000)
        self.assertIsNone(Checkpoint.rezago(ruta))

    def test_lo_que_no_es_puerta_calla(self):
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=1000)
        for nombre in ("estado-fase.md", "plan_pruebas.md", "README.md"):
            self.assertIsNone(Checkpoint.rezago(escribir(os.path.join(self.fase, nombre), fecha=5000)), nombre)
        self.assertIsNone(Checkpoint.rezago(escribir(os.path.join(self.tmp, "notas", "suelta.md"), fecha=5000)))
        self.assertIsNone(Checkpoint.rezago(os.path.join(self.fase, "plan_trabajo.md")), "no existe y habló")

    def test_el_checkpoint_no_se_toca(self):
        estado = escribir(os.path.join(self.fase, "estado-fase.md"), "## 1. En qué estación va\n", fecha=1000)
        ruta = escribir(os.path.join(self.fase, "resultado_pruebas.md"), fecha=2000)
        antes = huella(estado)
        Checkpoint.como_texto(Checkpoint.rezago(ruta), self.tmp)
        self.assertEqual(antes, huella(estado))

    def test_solo_mira_fechas(self):
        """RNF-01: un documento ilegible avisa igual, porque no se lee."""
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=1000)
        ruta = os.path.join(self.fase, "resultado_pruebas.md")
        with open(ruta, "wb") as f:
            f.write(os.urandom(64))
        os.utime(ruta, (2000, 2000))
        self.assertEqual("atrasado", Checkpoint.rezago(ruta)[0])

    def test_reconoce_la_fase_por_su_nombre(self):
        self.assertEqual(self.fase, Checkpoint.fase_de(os.path.join(self.fase, "plan_trabajo.md")))
        self.assertEqual("", Checkpoint.fase_de(os.path.join(self.tmp, "plan_trabajo.md")))


class ElVeredictoSeCopiaSolo(Temporal):
    """`EP-005·HU-003·CA-04`, fase C."""

    FASE = "A-EP-001-HU-001-p"
    HOY = datetime.date.today().isoformat()

    @staticmethod
    def resultado(concepto, conteo="2 de 2"):
        return ("# Resultado\n\n## 6. Veredicto de la fase\n\n| Campo | Valor |\n|---|---|\n"
                "| **Concepto** | **%s** |\n| **CA cumplidos** | %s |\n" % (concepto, conteo))

    def setUp(self):
        tmp = self.temporal()
        self.hu_dir = os.path.join(tmp, "documentacion", "epicas", "EP-001-p", "HU-001-p")
        self.fase = os.path.join(self.hu_dir, self.FASE)
        self.hu_md = os.path.join(self.hu_dir, "HU-001-p.md")
        self.readme_fase = escribir(os.path.join(self.fase, "README.md"),
                                    "# %s\n\n**Estado:** estación 4, esperando aprobación.\n" % self.FASE)
        self.readme_hu = escribir(
            os.path.join(self.hu_dir, "README.md"),
            "# HU-001-p\n\n| Qué | De qué se trata |\n|---|---|\n"
            "| [documentacion/epicas/EP-001-p/HU-001-p/%s/](%s/) | La fase A: la prueba. Plan escrito, "
            "esperando aprobación |\n" % (self.FASE, self.FASE))
        self.estado = escribir(os.path.join(self.fase, "estado-fase.md"), "## 1. En qué estación va\n")

    def hu_seis(self):
        f = self.FASE
        escribir(self.hu_md, "# HU-001 — La prueba\n\n## 8. Fases que la implementan\n\n"
                 "| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
                 "|---|---|---|---|---|---|\n"
                 "| [%s](%s/README.md) | CA-01 | [p](%s/plan_trabajo.md) | [q](%s/plan_pruebas.md) | cuando se "
                 "ejecute | Estación 4: plan escrito |\n\n## 9. Otra\n" % (f, f, f, f))

    def fila(self):
        return [l for l in leer(self.hu_md).splitlines() if l.startswith("| [%s]" % self.FASE)][0]

    def propagar(self, texto, nombre="resultado_pruebas.md"):
        return CopiaDelVeredicto.propagar(escribir(os.path.join(self.fase, nombre), texto), self.HOY)

    def test_cumple_llega_a_los_tres_sitios_con_seis_columnas(self):
        self.hu_seis()
        tocados, avisos = self.propagar(self.resultado("Cumple"))
        self.assertEqual([], avisos)
        self.assertEqual(3, len(tocados))
        esperado = "Cerrada el %s: Cumple, 2 de 2 CA" % self.HOY
        self.assertTrue(self.fila().endswith("| %s |" % esperado), self.fila())
        self.assertIn("| CA-01 | [p](", self.fila())
        self.assertIn("**Estado:** %s. Falta el commit" % esperado, leer(self.readme_fase))
        self.assertIn("| La fase A: la prueba. %s |" % esperado, leer(self.readme_hu))

    def test_no_cumple_llega_igual_con_tres_columnas(self):
        f = self.FASE
        escribir(self.hu_md, "# HU-001 — La prueba\n\n## 8. Fases que la implementan\n\n"
                 "| Fase | Qué CA cubre | Estado |\n|---|---|---|\n"
                 "| [%s](%s/README.md) | CA-01 | Estación 4: plan escrito |\n\n## 9. Otra\n" % (f, f))
        _tocados, avisos = self.propagar(self.resultado("No cumple", "1 de 2"))
        self.assertEqual([], avisos)
        self.assertEqual("| [%s](%s/README.md) | CA-01 | Ejecutada el %s: No cumple, 1 de 2 CA |"
                         % (f, f, self.HOY), self.fila())

    def test_sin_concepto_no_se_toca_nada(self):
        self.hu_seis()
        antes = (huella(self.hu_md), huella(self.readme_fase), huella(self.readme_hu))
        self.assertEqual(([], []), self.propagar(self.resultado("Todavía no se ejecutó")))
        self.assertEqual(antes, (huella(self.hu_md), huella(self.readme_fase), huella(self.readme_hu)))

    def test_el_estado_fase_no_cambia(self):
        self.hu_seis()
        antes = huella(self.estado)
        self.propagar(self.resultado("Cumple"))
        self.assertEqual(antes, huella(self.estado))

    def test_lo_que_no_le_toca_y_lo_que_no_encuentra(self):
        self.hu_seis()
        self.assertEqual(([], []), self.propagar("x", "plan_trabajo.md"))
        escribir(self.hu_md, "# HU-001 — La prueba\n\n## 8. Fases\n\n| Fase | CA | Estado |\n|---|---|---|\n")
        _tocados, avisos = self.propagar(self.resultado("Cumple"))
        self.assertTrue(any("no tiene fila" in a for a in avisos), avisos)

    def test_sin_escribir_dice_que_tocaria_y_no_toca(self):
        self.hu_seis()
        antes = huella(self.hu_md)
        ruta = escribir(os.path.join(self.fase, "resultado_pruebas.md"), self.resultado("Cumple"))
        tocados, _ = CopiaDelVeredicto.propagar(ruta, self.HOY, escribir=False)
        self.assertIn(self.hu_md, tocados)
        self.assertEqual(antes, huella(self.hu_md))


class ElArranqueDiceComoLleganLasReglas(Temporal):
    """`RepartoDeLasReglas` y el gate del arranque (pendiente 33, punto 5)."""

    def _base(self, *nombres):
        raiz = self.temporal()
        for nombre in nombres:
            escribir(os.path.join(raiz, "base", nombre), "# Título de %s\n\nCuerpo de %s.\n" % (nombre, nombre))
        return raiz

    def test_dice_como_llegan_las_reglas(self):
        texto = Cargador.contexto(self._base("00-nucleo.md", "05-tema/base.md"))
        self.assertIn("LLEGAN CON CADA MENSAJE", texto)
        self.assertIn("base/mapa-de-tareas.md", texto)
        self.assertIn("`01·C28`", texto)

    def test_no_manda_el_texto_de_ninguna_regla(self):
        nombres = ("00-nucleo.md", "01-conducta.md", "05-tema/base.md")
        texto = Cargador.contexto(self._base(*nombres))
        for nombre in nombres:
            self.assertNotIn("Cuerpo de %s" % nombre, texto, nombre)

    def test_sin_base_o_con_base_vacia_no_entrega_nada(self):
        raiz = self.temporal()
        self.assertEqual(Cargador.contexto(raiz), "")
        self.assertEqual(os.listdir(raiz), [])
        os.makedirs(os.path.join(raiz, "base"))
        self.assertEqual(Cargador.contexto(raiz), "")

    def test_sin_pasar_el_gate_entrega_solo_esa_regla(self):
        texto = Cargador.contexto(self._base("00-nucleo.md", GATE), gate_ok=False)
        self.assertIn("ARRANQUE DETENIDO", texto)
        self.assertIn("Cuerpo de %s" % GATE, texto)
        self.assertNotIn("LLEGAN CON CADA MENSAJE", texto)

    def test_lo_de_este_repositorio_es_corto(self):
        """Deja espacio en el canal para la memoria y el histórico."""
        texto = Cargador.contexto(ESTANDAR) if ESTANDAR else ""
        if not texto:
            self.skipTest("sin base/ en la raíz de la corrida")
        self.assertLess(len(texto), 1000)
        for ruta in ("base/mapa-de-tareas.md", "base/01-conducta/palabras-clave.md", "base/00-nucleo-blindado.md"):
            self.assertTrue(os.path.isfile(os.path.join(ESTANDAR, ruta)), ruta)

    def test_el_gate_es_un_archivo_que_existe_y_es_f13(self):
        """Un renombre lo dejó apuntando a una ruta que no existía, y la puerta
        desapareció en silencio: sin coincidencia, `_solo_gate` da vacío."""
        ruta = os.path.join(ESTANDAR, "base", *GATE.split("/"))
        self.assertTrue(os.path.isfile(ruta), "GATE apunta a %s, que no existe" % GATE)
        self.assertIn("F13", leer(ruta)[:400], "el archivo del gate no es la regla F13")

    def test_la_puerta_de_verdad_devuelve_algo(self):
        """Por el camino real, no comprobando la constante."""
        base = os.path.join(ESTANDAR, "base")
        texto = Cargador._solo_gate(base, list(Cargador.reglas(base)))
        self.assertTrue(texto, "la puerta no devolvió nada: desapareció")
        self.assertIn("ARRANQUE DETENIDO", texto)


# ── La traza ──────────────────────────────────────────────────────────────

class LaSesionTieneTraza(Temporal):
    """`EP-005·HU-016`. Las marcas de tiempo son fijas (`08·T3`).

    Las viejas pasaban por `validar.py traza`; acá `correr` hace lo mismo que
    ese subcomando con las piezas de `Traza`.
    """

    BASE = "2026-08-20T10:00:%02d.000Z"

    def setUp(self):
        self.tmp = self.temporal()

    def _uso(self, id_, nombre, entrada, segundo):
        return {"type": "assistant", "timestamp": self.BASE % segundo,
                "message": {"content": [{"type": "tool_use", "id": id_, "name": nombre, "input": entrada}]}}

    def _respuesta(self, id_, segundo, error=False):
        return {"type": "user", "timestamp": self.BASE % segundo,
                "message": {"content": [{"type": "tool_result", "tool_use_id": id_, "is_error": error,
                                         "content": "CENTINELA-" + id_}]}}

    def _escribir(self, lineas, nombre="abc.jsonl"):
        return escribir(os.path.join(self.tmp, nombre), "".join(
            (l if isinstance(l, str) else json.dumps(l)) + "\n" for l in lineas))

    def transcripcion(self):
        """Tres pasos con respuestas a 2, 5 y 1 segundos; el segundo con error."""
        return self._escribir([
            self._uso("t1", "Read", {"file_path": "a.md"}, 0), self._respuesta("t1", 2),
            self._uso("t2", "Bash", {"command": "python x.py"}, 10), self._respuesta("t2", 15, error=True),
            self._uso("t3", "WebFetch", {"url": "https://e.test"}, 20), self._respuesta("t3", 21)])

    @staticmethod
    def correr(ruta, raiz=None):
        """`(código, texto)` como `validar.py traza [--escribir --raiz]`."""
        lista = Traza.pasos(ruta)
        if not lista:
            return 1, ""
        texto = Traza.como_texto(lista, Traza.cierre(lista))
        if raiz is None:
            return 0, texto
        return (0 if Traza.escribir(raiz, Traza.sesion_de(ruta), texto) else 1), texto

    def test_la_linea_de_tiempo(self):
        codigo, salida = self.correr(self.transcripcion())
        self.assertEqual(0, codigo)
        datos = [l for l in salida.splitlines() if l.startswith("| ") and l.split("|")[1].strip().isdigit()]
        self.assertEqual(3, len(datos))
        for parte in ("Read", "2 s", "a.md", "ok", "10:00:00"):
            self.assertIn(parte, datos[0])
        for parte in ("Bash", "5 s", "python x.py", "error"):
            self.assertIn(parte, datos[1])
        self.assertIn("WebFetch", datos[2])
        self.assertIn("1 s", datos[2])
        self.assertNotIn("CENTINELA", salida, "se copió el contenido de un resultado")

    def test_el_cierre(self):
        _, salida = self.correr(self.transcripcion())
        for parte in ("3 pasos", "1 error", "Bash 1", "Read 1", "WebFetch 1", "Bash (5 s)", "21 s"):
            self.assertIn(parte, salida)

    def test_escribe_junto_al_historico_e_indexa_una_vez(self):
        escribir(os.path.join(self.tmp, "historico-chat", "2026-08-20-sesion.md"),
                 "<!-- sesion: abc -->\n\n# 2026-08-20 — Sesión\n")
        ruta = self.transcripcion()
        self.assertEqual(0, self.correr(ruta, self.tmp)[0])
        destino = os.path.join(self.tmp, "historico-chat", "trazas", "2026-08-20-sesion.md")
        texto = leer(destino)
        self.assertIn("| 1 |", texto)
        self.assertIn("3 pasos", texto)
        indice = os.path.join(self.tmp, "historico-chat", "trazas", "README.md")
        self.assertIn("historico-chat/trazas/2026-08-20-sesion.md", leer(indice))
        self.correr(ruta, self.tmp)
        self.assertEqual(1, leer(indice).count("(2026-08-20-sesion.md)"))

    def test_sin_historico_no_inventa(self):
        ruta = self.transcripcion()
        trazas = os.path.join(self.tmp, "historico-chat", "trazas")
        self.assertEqual(1, self.correr(ruta, self.tmp)[0])
        self.assertFalse(os.path.isdir(trazas))
        os.makedirs(os.path.join(self.tmp, "historico-chat"))
        self.assertEqual(1, self.correr(ruta, self.tmp)[0])
        self.assertFalse(os.path.isdir(trazas))

    def test_lo_raro_no_revienta(self):
        ruta = self._escribir([self._uso("t1", "Read", {"file_path": "a.md"}, 0), "esto no es JSON",
                               self._respuesta("t1", 2), self._uso("t2", "Bash", {"command": "x"}, 5)])
        codigo, salida = self.correr(ruta)
        self.assertEqual(0, codigo)
        self.assertIn("2 pasos", salida)
        self.assertIn("sin respuesta", salida)
        self.assertEqual(1, self.correr(self._escribir([], "vacia.jsonl"))[0])
        self.assertEqual(1, self.correr(os.path.join(self.tmp, "no-existe.jsonl"))[0])

    def test_las_respuestas_desordenadas_se_emparejan_por_id(self):
        lista = Traza.pasos(self._escribir([
            self._uso("t1", "Read", {"file_path": "a.md"}, 0), self._uso("t2", "Grep", {"pattern": "x"}, 1),
            self._respuesta("t2", 3), self._respuesta("t1", 6)]))
        self.assertEqual(["6 s", "2 s"], [p["duracion"] for p in lista])


# ── Las herramientas ──────────────────────────────────────────────────────

class ElRespaldoAntesDeLoIrreversible(Temporal):
    """`09·15`. Si no hay red, no se salta; y el límite se dice cada vez."""

    def proyecto(self, comando=None):
        raiz = self.temporal()
        filas = "| Acción | Comando |\n|---|---|\n| Correr las pruebas | `pytest` |\n"
        filas += "| **Respaldo de datos** | `%s` |\n" % (comando or "«…»")
        escribir(os.path.join(raiz, ".agente", "stack.md"), "# Stack\n\n" + filas)
        return raiz

    def correr(self, *args):
        return subprocess.run([sys.executable, GUION_RESPALDO] + list(args), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=60)

    def test_el_marcador_sin_llenar_no_cuenta_como_comando(self):
        self.assertEqual("", Respaldo(self.proyecto()).comando_de_respaldo())

    def test_sin_declaracion_no_da_el_visto_bueno_ni_inventa(self):
        respaldo = Respaldo(self.proyecto())
        ok, mensaje = respaldo.respaldar("2026-01-02", escribir=True)
        self.assertFalse(ok)
        self.assertIn("no se corre la operación", mensaje)
        self.assertIn("no declara", respaldo.respaldar("2026-01-02")[1])

    def test_el_programa_sale_con_error_sin_declaracion(self):
        r = self.correr("--raiz", self.proyecto(), "--aplicar", "--", "echo", "peligro")
        self.assertEqual(1, r.returncode)
        self.assertNotIn("peligro\n", r.stdout.replace("echo peligro", ""))

    def test_lee_el_comando_y_sin_aplicar_no_corre_nada(self):
        respaldo = Respaldo(self.proyecto("echo respaldando"))
        self.assertEqual("echo respaldando", respaldo.comando_de_respaldo())
        ok, mensaje = respaldo.respaldar("2026-01-02", escribir=False)
        self.assertTrue(ok)
        self.assertIn("se correría", mensaje)

    def test_si_el_respaldo_falla_no_se_corre_la_operacion(self):
        ok, mensaje = Respaldo(self.proyecto("exit 1")).respaldar("2026-01-02", escribir=True)
        self.assertFalse(ok)
        self.assertIn("no se corre la operación", mensaje)

    def test_con_respaldo_bueno_la_operacion_corre(self):
        r = self.correr("--raiz", self.proyecto("echo respaldando"), "--aplicar", "--", "echo", "listo")
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("listo", r.stdout)
        self.assertLess(r.stdout.index("operación:"), r.stdout.rindex("listo"),
                        "la salida de la operación salió antes que su aviso")

    def test_la_salida_advierte_lo_que_no_cubre(self):
        for comando in ("echo respaldando", None):
            self.assertIn("no los ve nadie", self.correr("--raiz", self.proyecto(comando), "--", "echo", "x").stdout)

    def test_sin_operacion_no_hace_nada_y_dice_como_se_usa(self):
        r = self.correr()
        self.assertEqual(2, r.returncode)
        self.assertIn("Uso:", r.stdout)

    def test_la_plantilla_declara_respaldar_y_restaurar(self):
        texto = leer(os.path.join(ESTANDAR, "plantillas", "stack.md"))
        self.assertIn("Respaldo de datos", texto)
        self.assertIn("Restaurar un respaldo", texto)


class LasPruebasQueExistenSeCorren(Temporal):
    """`EP-005·HU-021`. Lo que más se vigila es que cero pruebas NO pase por verde.

    No se pasan las que miran a `validar.py` o al instalador, ni la que corre la
    batería real de Cimiento: dentro de esta misma batería se correría a sí misma.
    """

    UNA_QUE_PASA = ("import unittest\nclass C(unittest.TestCase):\n"
                    "    def test_a(self): self.assertTrue(True)\n    def test_b(self): self.assertTrue(True)\n")
    UNA_QUE_FALLA = "import unittest\nclass D(unittest.TestCase):\n    def test_c(self): self.assertEqual(1, 2)\n"

    def _proyecto(self, con=(), plataforma=False):
        raiz = self.temporal()
        os.makedirs(os.path.join(raiz, "validadores", "tests"))
        for nombre, cuerpo in con:
            escribir(os.path.join(raiz, "validadores", "tests", nombre), cuerpo)
        if plataforma:
            escribir(os.path.join(raiz, PLATAFORMA, "manage.py"), "# un punto de entrada de mentiras\n")
        return raiz

    def validar(self, raiz, solo=None):
        return PruebasDelEstandar(raiz, solo=solo).validar()

    def fallas(self, hallazgos):
        return [h for h in hallazgos if h.severidad == FALLA]

    def test_la_carpeta_vacia_es_roja(self):
        fallas = self.fallas(self.validar(self._proyecto()))
        self.assertTrue(fallas, "una carpeta vacía pasó por verde")
        self.assertIn("0 pruebas", fallas[0].mensaje)

    def test_la_carpeta_que_no_existe_es_roja(self):
        fallas = self.fallas(self.validar(self.temporal()))
        self.assertTrue(fallas)
        self.assertIn("no existe", fallas[0].mensaje)

    def test_archivos_sin_ninguna_prueba_dentro_es_rojo(self):
        self.assertTrue(self.fallas(self.validar(self._proyecto([("test_vacio.py", "x = 1\n")]))))

    def test_unittest_discover_solo_daria_cero_y_por_eso_hace_falta(self):
        """No prueba el corredor: prueba que el corredor hace falta."""
        raiz = self._proyecto()
        escribir(os.path.join(raiz, "validadores", "tests", "__init__.py"), "")
        salida = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests"],
                                cwd=os.path.join(raiz, "validadores"), capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=120)
        self.assertEqual(salida.returncode, 0, "la razón por la que existe el corredor cambió")

    def test_corre_y_dice_cuantas(self):
        hallazgos = self.validar(self._proyecto([("test_uno.py", self.UNA_QUE_PASA)]))
        self.assertEqual([], self.fallas(hallazgos))
        self.assertTrue(any("2 prueba(s)" in h.mensaje for h in hallazgos if h.severidad == AVISO))

    def test_una_falla_nombra_su_archivo_y_su_caso(self):
        fallas = self.fallas(self.validar(self._proyecto([("test_uno.py", self.UNA_QUE_PASA),
                                                          ("test_dos.py", self.UNA_QUE_FALLA)])))
        self.assertEqual(1, len(fallas))
        self.assertIn("test_dos.py", fallas[0].archivo)
        self.assertIn("test_c", fallas[0].mensaje)

    def test_un_archivo_que_no_carga_se_reporta_y_no_tumba_el_resto(self):
        hallazgos = self.validar(self._proyecto([("test_uno.py", self.UNA_QUE_PASA),
                                                 ("test_roto.py", "import no_existe_este_modulo\n")]))
        self.assertTrue(any("no se pudo cargar" in h.mensaje for h in self.fallas(hallazgos)))
        self.assertTrue(any("2 prueba(s)" in h.mensaje for h in hallazgos))

    def test_se_puede_pedir_un_solo_archivo(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA), ("test_dos.py", self.UNA_QUE_FALLA)])
        hallazgos = self.validar(raiz, solo=["test_uno"])
        self.assertEqual([], self.fallas(hallazgos), "corrió el que no se le pidió")
        self.assertTrue(any("2 prueba(s) en 1 archivo(s)" in h.mensaje for h in hallazgos))

    def test_un_nombre_que_no_existe_es_rojo(self):
        fallas = self.fallas(self.validar(self._proyecto([("test_uno.py", self.UNA_QUE_PASA)]), ["test_no_esta"]))
        self.assertTrue(any("no está en la carpeta" in h.mensaje for h in fallas))

    def test_sin_sello_reclama(self):
        avisos = PruebasDelEstandar(self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])).reclamo()
        self.assertIn("nunca corrieron", avisos[0].mensaje)

    def test_la_corrida_entera_y_limpia_deja_el_sello_en_cero(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        pruebas = PruebasDelEstandar(raiz)
        pruebas.validar()
        self.assertTrue(os.path.isfile(os.path.join(raiz, SELLO)))
        self.assertEqual([], pruebas.reclamo())

    def test_una_corrida_con_fallas_sella_diciendo_cuantas(self):
        pruebas = PruebasDelEstandar(self._proyecto([("test_dos.py", self.UNA_QUE_FALLA)]))
        pruebas.validar()
        mensaje = pruebas.reclamo()[0].mensaje
        self.assertIn("1 falla(s)", mensaje)
        self.assertIn("dejó", mensaje)
        self.assertNotIn("nunca corrieron", mensaje)

    def test_un_sello_viejo_sin_conteo_se_lee_como_limpio(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        escribir(os.path.join(raiz, SELLO), "2026-08-28 10:00:00\n")
        self.assertEqual([], PruebasDelEstandar(raiz).reclamo())

    def test_un_subconjunto_no_sella(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA), ("test_tres.py", self.UNA_QUE_PASA)])
        self.validar(raiz, ["test_uno"])
        self.assertFalse(os.path.isfile(os.path.join(raiz, SELLO)))

    def test_el_reclamo_calla_cuando_el_sello_es_posterior_al_commit(self):
        if not shutil.which("git"):
            self.skipTest("sin git")
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        for orden in (["init", "-q"], ["config", "user.name", "p"], ["config", "user.email", "p@l"],
                      ["add", "-A"], ["commit", "-qm", "base"]):
            subprocess.run(["git"] + orden, cwd=raiz, capture_output=True)
        pruebas = PruebasDelEstandar(raiz)
        pruebas.sellar()
        self.assertEqual([], pruebas.reclamo())

    def test_el_reclamo_no_revienta_sin_repositorio(self):
        pruebas = PruebasDelEstandar(self._proyecto([("test_uno.py", self.UNA_QUE_PASA)]))
        pruebas.sellar()
        self.assertEqual([], pruebas.reclamo())

    def test_el_sello_no_va_en_el_cajon_de_las_sesiones(self):
        """La primera versión lo puso en `historico-chat/.tocado/`, donde cada
        `.txt` es el registro de una sesión. Antes se miraba con
        `sesiones.registros()`, que es de otro grupo: acá se mira la carpeta."""
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        self.validar(raiz)
        self.assertTrue(os.path.isfile(os.path.join(raiz, SELLO)))
        self.assertFalse(os.path.isdir(os.path.join(raiz, "historico-chat", ".tocado")))

    # La otra batería (`EP-005·HU-021`, fase B).

    def test_sin_plataforma_se_avisa_y_no_es_falla(self):
        hallazgos, cuantas = PruebasDelEstandar(self._proyecto()).correr_la_plataforma()
        self.assertEqual(0, cuantas)
        self.assertEqual([AVISO], [h.severidad for h in hallazgos])
        self.assertIn("No es lo mismo que estar en verde", hallazgos[0].mensaje)

    def test_la_plataforma_que_no_corre_nada_es_roja(self):
        hallazgos, cuantas = PruebasDelEstandar(self._proyecto(plataforma=True)).correr_la_plataforma()
        self.assertEqual(0, cuantas)
        self.assertEqual([FALLA], [h.severidad for h in hallazgos])
        self.assertIn("cero no es verde", hallazgos[0].mensaje)

    def _resumen(self, hallazgos):
        lineas = [h.mensaje for h in hallazgos if h.severidad == AVISO and "prueba(s) en" in h.mensaje]
        self.assertEqual(1, len(lineas))
        return lineas[0]

    def test_las_dos_baterias_se_cuentan_aparte(self):
        UNA = "import unittest\nclass Una(unittest.TestCase):\n    def test_pasa(self): self.assertTrue(True)\n"
        raiz = self._proyecto([("test_una.py", UNA)])
        resumen = self._resumen(self.validar(raiz))
        self.assertIn("1 prueba(s) en 1 archivo(s)", resumen)
        self.assertIn("0 prueba(s) de la plataforma", resumen)
        self.assertNotIn("de la plataforma", self._resumen(self.validar(raiz, ["test_una.py"])),
                         "un subconjunto arrastró la otra batería")


class ElHistoricoSeBuscaPorTema(Temporal):
    """`EP-005·HU-001`. El caso que decide: generar dos veces da lo mismo."""

    def setUp(self):
        self.tmp = self.temporal()

    def resumen(self, dia, nombre, texto):
        escribir(os.path.join(self.tmp, "historico-chat", "resumenes", dia, nombre), texto)

    def indice(self):
        return IndiceTematico(self.tmp)

    def test_recoge_los_hallazgos_de_todos_los_resumenes(self):
        self.resumen("2026-01-02", "uno.md", "# 2026-01-02 · lo que quedó\n\n### H-1 · La primera cosa\n\n"
                                             "texto\n\n### H-2 · La segunda cosa\n\ntexto\n")
        self.resumen("2026-01-03", "dos.md", "# 2026-01-03 · lo que quedó\n\n### H-1 · Otra cosa\n")
        salida = self.indice().generar()
        for parte in ("La primera cosa", "La segunda cosa", "Otra cosa", "**3 hallazgos** en **2 resúmenes**"):
            self.assertIn(parte, salida)

    def test_cada_hallazgo_enlaza_a_su_resumen(self):
        self.resumen("2026-01-02", "el-tema.md", "# 2026-01-02 · lo que quedó\n\n### H-1 · La cosa\n")
        self.assertIn("(2026-01-02/el-tema.md)", self.indice().generar())

    def test_el_resumen_sin_hallazgos_no_ensucia(self):
        self.resumen("2026-01-02", "vacio.md", "# 2026-01-02 · lo que quedó\n\nNada.\n")
        self.assertNotIn("vacio.md", self.indice().generar())
        self.assertIn("sin ningún hallazgo: 1", self.indice().linea_resumen())

    def test_el_readme_de_la_carpeta_no_es_un_resumen(self):
        self.resumen("2026-01-02", "README.md", "# Índice\n\n### H-1 · Esto no es un hallazgo\n")
        self.assertNotIn("Esto no es un hallazgo", self.indice().generar())

    def test_generar_dos_veces_da_lo_mismo(self):
        self.resumen("2026-01-02", "uno.md", "# 2026-01-02 · lo que quedó\n\n### H-1 · La cosa\n")
        self.assertEqual(self.indice().generar(), self.indice().generar())

    def test_avisa_cuando_queda_atras_y_nunca_detiene(self):
        self.resumen("2026-01-02", "uno.md", "# 2026-01-02 · lo que quedó\n\n### H-1 · La cosa\n")
        hallazgos = self.indice().validar()
        self.assertEqual([AVISO], [h.severidad for h in hallazgos])
        self.indice().escribir()
        self.assertEqual([], self.indice().validar())
        self.resumen("2026-01-03", "dos.md", "# 2026-01-03 · lo que quedó\n\n### H-1 · Nueva\n")
        self.assertTrue(any("quedó atrás" in h.mensaje for h in self.indice().validar()))

    def test_sin_resumenes_no_revienta(self):
        self.assertIn("Todavía no hay resúmenes", self.indice().generar())
        self.assertEqual("", self.indice().linea_resumen())


if __name__ == "__main__":
    unittest.main()
