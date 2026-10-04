# -*- coding: utf-8 -*-
"""`EP-023 · HU-007 · fase B` · El freno antes y después de actuar.

CP-001: la herramienta de escritura, contra la fase en curso y lo autorizado.
CP-002: la consola.
CP-003: lo que se publica.
CP-004: después de una orden, lo que cambió en git.
CP-005: el hallazgo queda anotado en el resumen de la sesión.
"""
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
sys.path.insert(0, VALIDADORES)

import freno                # noqa: E402
import instalar             # noqa: E402

HU = "documentacion/epicas/EP-009-algo/HU-001-una-cosa"
FASE = HU + "/B-EP-009-HU-001-la-fase"
PENDIENTE = "documentacion/epicas/EP-009-algo/pendientes/110-algo"


def plan(aprobado=True):
    aprobacion = ("**Aprobación** (`02·F4`): Ana Pérez, el 2026-10-03, con la versión 51.0.0.\n\n"
                  if aprobado else "**Aprobación** (`02·F4`): pendiente.\n\n")
    return ("# Plan\n\n%s### 2.1 Archivos que se crean o modifican\n\n> Rutas exactas.\n\n"
            "| Archivo (ruta real verificada) | Tipo | Capa | Nota |\n|---|---|---|---|\n"
            "| `src/a.py` | Modificar | Programa | |\n\n### 2.2 Otra\n" % aprobacion)


class Proyecto(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = os.path.realpath(self.tmp.name)
        subprocess.run(["git", "init", "-q", self.raiz], check=True)

    def tearDown(self):
        self.tmp.cleanup()

    def ruta(self, relativa):
        return os.path.join(self.raiz, *relativa.split("/"))

    def escribir(self, relativa, texto="x\n"):
        os.makedirs(os.path.dirname(self.ruta(relativa)), exist_ok=True)
        with io.open(self.ruta(relativa), "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def con_fase(self, aprobado=True):
        self.escribir(FASE + "/plan_trabajo.md", plan(aprobado))

    def escritura(self, relativa):
        return freno.revisar(self.raiz, "Write", {"file_path": self.ruta(relativa)})[0]

    def orden(self, orden, **extra):
        entrada = dict(command=orden, **extra)
        return freno.revisar(self.raiz, "Bash", entrada, cwd=self.raiz)[0]


class LaHerramientaDeEscritura(Proyecto):
    """CP-001."""

    def test_sin_aprobar_el_plan_solo_los_documentos_de_la_fase(self):
        self.con_fase(aprobado=False)
        self.assertEqual("deja", self.escritura(FASE + "/plan_pruebas.md"))
        self.assertEqual("detiene", self.escritura("src/a.py"))

    def test_con_el_plan_aprobado_lo_que_declara(self):
        self.con_fase()
        self.assertEqual("deja", self.escritura("src/a.py"))
        self.assertEqual("detiene", self.escritura("src/b.py"))

    def test_sin_fase_en_curso_solo_lo_autorizado(self):
        self.assertEqual("deja", self.escritura("historico-chat/resumenes/2026-10-03/tema.md"))
        self.assertEqual("deja", self.escritura(HU + "/HU-001-una-cosa.md"))
        self.assertEqual("detiene", self.escritura("src/a.py"))

    def test_lo_que_el_analisis_prendido_manda_hacer_de_una(self):
        self.escribir(PENDIENTE + "/analisis-2.md",
                      "# Análisis 2\n\n## Lo que se tiene que hacer\n\n"
                      "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
                      "| 1 | Corregir `src/c.py` | 1 | Este análisis, de una y sin fase |\n\n## Otra\n")
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE)
        self.assertEqual("deja", self.escritura("src/c.py"))
        self.assertEqual("detiene", self.escritura("src/d.py"))

    def test_la_ruta_de_una_tambien_se_lee_en_paso_a(self):
        self.escribir(PENDIENTE + "/analisis-2.md",
                      "# Análisis 2\n\n## Lo que se tiene que hacer\n\n"
                      "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
                      "| 1 | Corregir la plantilla | 1 | Este análisis, de una y sin fase: `src/e.py` |\n\n## Otra\n")
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE)
        self.assertEqual("deja", self.escritura("src/e.py"))
        self.assertEqual("detiene", self.escritura("src/d.py"))

    def test_fuera_del_proyecto_tambien_con_rutas_que_enganan(self):
        self.assertEqual("detiene", self.escritura("../fuera.txt"))
        self.assertEqual("detiene", self.escritura("src/../../fuera.txt"))

    def test_el_instalador_lo_pone_sobre_toda_accion(self):
        antes = [h for h in instalar.HOOKS_CLAUDE if h[2] == "hook_antes.py"]
        self.assertEqual([("PreToolUse", None)], [h[:2] for h in antes])


class LaConsola(Proyecto):
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


class LoQueSePublica(Proyecto):
    """CP-003."""

    def test_se_pregunta(self):
        self.assertEqual("pregunta", freno.revisar(self.raiz, "mcp__docs__update", {})[0])
        self.assertEqual("deja", freno.revisar(self.raiz, "Read", {})[0])


class DespuesDeActuar(Proyecto):
    """CP-004."""

    def test_ve_lo_que_un_programa_escribio_por_dentro(self):
        self.con_fase()
        self.escribir("viejo.txt")                 # ya estaba cambiado antes de la orden
        freno.tomar_foto(self.raiz)
        self.escribir("src/a.py")                  # declarado
        self.escribir("src/b.py")                  # no declarado
        self.assertEqual(["src/b.py"], [r for r, _ in freno.despues(self.raiz)])


class ElHallazgoQuedaAnotado(Proyecto):
    """CP-005."""

    def setUp(self):
        super().setUp()
        self.escribir("historico-chat/2026-10-03-tema.md", "# Sesión\n\n<!-- sesion: abc -->\n")
        self.escribir("historico-chat/resumenes/2026-10-03/tema.md",
                      "# Resumen\n\n## Hallazgos\n\n---\n\n## ¿Se puede cerrar la sesión?\n\nNo.\n")

    def test_el_resumen_suma_el_hallazgo_una_sola_vez(self):
        for _ in range(2):
            freno.anotar_hallazgo(self.raiz, "abc", "una escritura", "src/b.py", "no está en el plan")
        texto = io.open(self.ruta("historico-chat/resumenes/2026-10-03/tema.md"), encoding="utf-8").read()
        self.assertEqual(1, texto.count("El freno detuvo"))
        self.assertIn("vuelve al análisis", texto)
        self.assertLess(texto.index("### H-1 "), texto.index("## ¿Se puede cerrar"))

    def test_el_enganche_detiene_y_dice_que_se_vuelve_al_analisis(self):
        enganche = os.path.join(RAIZ, "adaptadores", "claude-code", "hook_antes.py")
        datos = {"tool_name": "Write", "tool_input": {"file_path": self.ruta("src/b.py")},
                 "session_id": "abc", "cwd": self.raiz}
        r = subprocess.run([sys.executable, enganche, "--modo", "accion", "--raiz", self.raiz],
                           input=json.dumps(datos).encode("utf-8"), capture_output=True)
        salida = json.loads(r.stdout.decode("utf-8"))["hookSpecificOutput"]
        self.assertEqual("deny", salida["permissionDecision"])
        self.assertIn("vuelve al análisis", salida["permissionDecisionReason"])

    def prender(self, aprobado=False):
        marca = "> **Aprobado** por el usuario el 2026-10-03.\n\n" if aprobado else ""
        self.escribir(PENDIENTE + "/analisis-2.md", "# Análisis 2\n\n" + marca)
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE)

    def test_cp_c001_con_un_analisis_prendido_no_se_anota(self):
        self.prender()
        self.assertEqual("", freno.anotar_hallazgo(self.raiz, "abc", "una escritura", "src/b.py", "no está"))
        texto = io.open(self.ruta("historico-chat/resumenes/2026-10-03/tema.md"), encoding="utf-8").read()
        self.assertNotIn("El freno detuvo", texto)
        self.assertIn("reportarlo en la conversación", freno.aviso("no está", "src/b.py", False, True))

    def test_cp_c001_con_el_analisis_ya_aprobado_si_se_anota(self):
        self.prender(aprobado=True)
        self.assertTrue(freno.anotar_hallazgo(self.raiz, "abc", "una escritura", "src/b.py", "no está"))

    def test_cp_c001_la_regla_lo_dice(self):
        regla = os.path.join(RAIZ, "base", "13-documentacion", "reglas",
                             "DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md")
        self.assertIn("análisis prendido", io.open(regla, encoding="utf-8").read())


class ElMayorQueEntreComillas(Proyecto):
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


class LaOrdenDeSedNoEsUnArchivo(unittest.TestCase):
    """Análisis 14 del pendiente 103, acuerdo 10."""

    def test_lo_que_va_tras_e_es_la_orden(self):
        self.assertEqual(["a.md"], freno.destinos("sed -i -e 's/x/y/' -e 's/actual:/z/' a.md"))
        self.assertEqual(["a.md", "b.md"], freno.destinos("sed -i --expression='s/x/y/' a.md b.md"))

    def test_sin_e_la_primera_palabra_es_la_orden(self):
        self.assertEqual(["a.md"], freno.destinos("sed -i 's/x/y/' a.md"))

    def test_sin_i_no_escribe(self):
        self.assertEqual([], freno.destinos("sed -n '1,5p' a.md"))


class CorrijaArreglaLasHerramientas(Proyecto):
    """Análisis 16 del pendiente 103, acuerdo 2."""

    def test_con_corrija_se_corrigen_las_herramientas_y_nada_mas(self):
        self.assertEqual("detiene", self.escritura("validadores/freno.py"))
        freno.curso.marcar_corrija(self.raiz, 7)
        self.assertEqual("deja", self.escritura("validadores/freno.py"))
        self.assertEqual("deja", self.escritura("adaptadores/claude-code/hook_antes.py"))
        self.assertEqual("detiene", self.escritura("base/02-flujo-de-trabajo/reglas/F8.md"))
        freno.curso.borrar_corrija(self.raiz)
        self.assertEqual("detiene", self.escritura("validadores/freno.py"))


class ElHeredocNoEsEscritura(unittest.TestCase):
    """Análisis 16 del pendiente 103, acuerdo 2."""

    def test_el_texto_del_heredoc_no_cuenta(self):
        self.assertEqual([], freno.destinos("python - <<'EOF'\nif a > b: print(1)\nx >> y\nEOF"))

    def test_la_redireccion_de_la_linea_que_lo_abre_si(self):
        self.assertEqual(["nota.txt"], freno.destinos("cat > nota.txt <<EOF\nhola > mundo\nEOF"))


class LaComparacionNoEsEscritura(unittest.TestCase):
    """Análisis 15 del pendiente 103, acuerdo 1."""

    def test_mayor_o_igual_y_flecha_no_escriben(self):
        self.assertEqual([], freno.destinos("python - <<EOF\nif n >= 11: pass\nEOF"))
        self.assertEqual([], freno.destinos("awk '$1 => 2' a.txt"))

    def test_la_redireccion_sigue_viendose(self):
        self.assertEqual(["notas.txt"], freno.destinos("echo x > notas.txt"))
        self.assertEqual(["notas.txt"], freno.destinos("echo x >> notas.txt"))


if __name__ == "__main__":
    unittest.main()
