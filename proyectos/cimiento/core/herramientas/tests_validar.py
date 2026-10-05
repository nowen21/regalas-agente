"""`validar.py`, el punto de entrada único, como clase de Cimiento.

Son las pruebas de `validadores/tests/` y de `validadores/pruebas.py` que miran
`validar.py` (`test_la_corrida_completa_en_una_linea.py`,
`test_ninguno_termina_en_silencio.py`, `test_el_validador_dice_sobre_que_corrio.py`,
`test_el_validador_no_revisa_lo_ajeno.py`, `test_el_conteo_por_regla.py`,
`test_la_sesion_tiene_traza.py`, `LasPruebasQueExistenSeCorren` y
`FormatoDelHallazgo`), pasadas a `core.herramientas.validar`. Lo que antes corría
`validar.py` como orden del sistema ahora llama a `main([...])` en el mismo
proceso; solo la puerta de `validadores/` se corre como orden, porque es lo que
llaman los `.githooks`.

La corrida completa se prueba sobre un proyecto temporal: sobre el estándar
tarda minutos, y lo que se fija acá es su forma, no los hallazgos del día.
"""
import contextlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

from core.comun import Proyecto
from core.herramientas import validar
from core.herramientas.validar import FUERA_DE_LA_CORRIDA, Consola, main, raiz_del_proyecto

ESTANDAR = Proyecto.estandar()
PUERTA = os.path.join(ESTANDAR, "validadores", "validar.py")


def correr(*args, cwd=None):
    """`(salida, errores, código)` de `main(args)`, parado en `cwd` si se da."""
    salida, errores = io.StringIO(), io.StringIO()
    antes = os.getcwd()
    try:
        if cwd:
            os.chdir(cwd)
        with contextlib.redirect_stdout(salida), contextlib.redirect_stderr(errores):
            codigo = main(list(args))
    finally:
        os.chdir(antes)
    return salida.getvalue(), errores.getvalue(), codigo


def por_la_puerta(*args, cwd=None):
    return subprocess.run([sys.executable, PUERTA] + list(args), cwd=cwd or ESTANDAR, capture_output=True,
                          text=True, encoding="utf-8", errors="replace", timeout=600,
                          env=dict(os.environ, PYTHONIOENCODING="utf-8"))


class ConCarpeta(unittest.TestCase):
    """Un proyecto temporal con los archivos que se le pidan."""

    def carpeta(self, archivos=None, git=False):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for ruta, cuerpo in (archivos or {}).items():
            destino = os.path.join(tmp.name, *ruta.split("/"))
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "wb") as f:
                f.write(cuerpo if isinstance(cuerpo, bytes) else cuerpo.encode("utf-8"))
        if git:
            subprocess.run(["git", "init", "-q", tmp.name], check=True, capture_output=True)
        return tmp.name


class LaCorridaCompleta(ConCarpeta):
    """`EP-004·HU-008` · Una línea dice cómo está el proyecto. El caso que decide
    es `CP-004`: un subcomando nuevo entra solo."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        subprocess.run(["git", "init", "-q", cls.tmp.name], check=True, capture_output=True)
        cls.salida, cls.errores, cls.codigo = correr("todo", "--raiz", cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_cp001_cada_subcomando_sigue_corriendo_por_separado(self):
        """La corrida no cambia lo que hacía cada uno: los llama, no los rehace."""
        salida, _, codigo = correr("estandar")
        self.assertEqual(0, codigo)
        self.assertIn("Coherencia del estándar", salida)

    def test_cp002_una_linea_corre_todo_lo_que_aplica(self):
        self.assertIn("Corrida completa", self.salida)
        self.assertRegex(self.salida, r"\d+ comprobación\(es\) corridas")
        for esperado in ("Coherencia del estándar", "El estándar contra sus meta-reglas"):
            self.assertIn(esperado, self.salida, "no corrió una comprobación que aplica")

    def test_cp003_lo_que_queda_fuera_dice_por_que(self):
        """Sin el motivo escrito, «no corrió» se lee como «no hacía falta»."""
        for lento in ("linter", "suite", "audit", "internas"):
            self.assertIn("(fuera: %s" % lento, self.salida)
        self.assertIn("tarda", self.salida)

    def test_cp004_un_subcomando_nuevo_entra_solo(self):
        """El caso que decide: la lista sale del propio analizador."""
        consola = Consola()
        consola.armar()
        corridas = {n for n in consola.nombres if n not in FUERA_DE_LA_CORRIDA}
        self.assertGreater(len(corridas), 25, "la corrida mira muy pocos: ¿se coló una lista a mano?")
        self.assertNotIn("todo", corridas)
        # Fuera del estándar corren todas las que no están en la lista de fuera.
        self.assertEqual(len(corridas), int(re.search(r"(\d+) comprobación\(es\) corridas", self.salida).group(1)))

    def test_cp005_la_corrida_termina_con_un_resumen_unico(self):
        ultimas = "\n".join(self.salida.strip().splitlines()[-3:])
        self.assertTrue("con fallas" in ultimas or "Sin fallas" in ultimas,
                        "el resumen final no está al final: %r" % ultimas)

    def test_cp006_el_codigo_de_salida_refleja_la_peor(self):
        """Cero si ninguna falló; uno si alguna falló. Sin eso, no sirve en CI."""
        con_fallas = "con fallas: " in self.salida
        self.assertEqual(1 if con_fallas else 0, self.codigo)

    def test_cp007_el_subcomando_esta_en_la_ayuda(self):
        salida, _, codigo = correr("--help")
        self.assertEqual(0, codigo)
        self.assertIn("todo", salida)

    def test_el_conteo_por_regla_va_al_final_y_sin_el_texto(self):
        """`EP-004·HU-009` · Se imprime antes del resumen y se anota sin el texto
        del hallazgo: en un mensaje puede viajar una clave."""
        self.assertTrue("Hallazgos por regla" in self.salida or "Ningún hallazgo que contar." in self.salida)
        registro = os.path.join(self.tmp.name, "metricas", "conteo-por-regla.jsonl")
        with open(registro, encoding="utf-8") as f:
            filas = [json.loads(l) for l in f if l.strip()]
        self.assertEqual(1, len(filas), "una línea por corrida")
        self.assertEqual({"conteo", "cuando", "total", "version"}, set(filas[0]))
        self.assertNotIn("pipeline", json.dumps(filas[0], ensure_ascii=False))

    def test_internas_queda_fuera_porque_tarda(self):
        """`02·F5`: juntarlas daría trece minutos en cada corrida de rutina."""
        self.assertIn("internas", FUERA_DE_LA_CORRIDA)
        self.assertIn("tarda", FUERA_DE_LA_CORRIDA["internas"])


class EnElEstandarNoSeMideLaInstalacion(ConCarpeta):

    def test_checklist_versiones_y_version_quedan_fuera_con_su_motivo(self):
        raiz = self.carpeta({"base/uno.md": "# Uno\n", "VERSION": "1.0.0\n"}, git=True)
        salida, _, _ = correr("todo", "--raiz", raiz)
        for nombre in ("checklist", "versiones", "version"):
            self.assertIn("(fuera: %s —" % nombre, salida)
        self.assertIn("acá estamos **en** el estándar", salida)


class LaRaizPorDefectoEsDondeEstaElUsuario(ConCarpeta):
    """`61` · El que revisa un proyecto no revisa el estándar creyendo que es él."""

    def test_el_ayudante_devuelve_donde_se_esta_parado(self):
        self.assertEqual(os.getcwd(), raiz_del_proyecto())

    def test_desde_una_carpeta_ajena_no_revisa_el_estandar(self):
        """**El caso reportado.** Antes salían las claves falsas de `validadores/tests/`."""
        salida, _, _ = correr("secretos", cwd=self.carpeta())
        self.assertNotIn("validadores/tests/", salida)

    def test_dice_que_no_hay_repositorio_en_vez_de_revisar_otro(self):
        _, errores, codigo = correr("versionado", cwd=self.carpeta())
        self.assertEqual(1, codigo)
        self.assertIn("no hay repositorios git", errores)

    @unittest.skipUnless(os.name == "nt", "la letra de unidad es cosa de Windows")
    def test_la_carpeta_se_nombra_como_se_pidio(self):
        """`realpath` cambia `c:` por `C:`; el reporte la escribe como llegó."""
        raiz = self.carpeta()
        pedida = raiz[0].lower() + raiz[1:]
        salida, _, _ = correr("ci", "--raiz", pedida)
        self.assertIn("[AVISO] %s —" % os.path.abspath(pedida).replace("\\", "/"), salida)


class FormatoDelHallazgo(ConCarpeta):
    """`EP-004·HU-003` · El aviso no detiene, la falla sí, y lo ilegible se dice."""

    def test_la_corrida_respeta_los_dos_codigos(self):
        self.assertEqual(0, correr("flujo", "--raiz", ESTANDAR)[2], "una corrida de solo avisos no dio 0")
        self.assertEqual(1, correr("commit", "--archivo", self._mensaje("arreglos.\n"))[2])

    def test_el_archivo_que_no_se_puede_leer_se_dice_como_aviso(self):
        """Ni volcado ni silencio: la corrida sigue y el archivo queda dicho."""
        raiz = self.carpeta({"base/raro.md": b"# T\xed\xf3tulo mal codificado\n"})
        salida, _, codigo = correr("marcas", "--raiz", raiz)
        self.assertEqual(0, codigo)
        self.assertRegex(salida, r"\[AVISO\] .*raro\.md — no es UTF-8")

    def test_la_ruta_relativa_se_lee_desde_donde_se_esta_parado(self):
        """Como el `.git/COMMIT_EDITMSG` del enganche: es del proyecto, no del estándar."""
        raiz = self.carpeta({"msg.txt": "arreglos.\n"})
        salida, _, _ = correr("commit", "--archivo", "msg.txt", cwd=raiz)
        self.assertIn("== Mensaje de msg.txt ==", salida)
        self.assertIn("[FALLA] %s:1 —" % os.path.join(raiz, "msg.txt").replace("\\", "/"), salida)

    def _mensaje(self, texto):
        return os.path.join(self.carpeta({"m.txt": texto}), "m.txt")

    def test_un_mensaje_bueno_pasa(self):
        ruta = self._mensaje("feat(x): el validador dice qué miró\n\nPorque un cero sin alcance engaña.\n")
        self.assertEqual(0, correr("commit", "--archivo", ruta)[2])


class ElValidadorDiceSobreQueCorrio(ConCarpeta):
    """`EP-004·HU-024` · Un cero dice sobre qué corrió, o no dice nada."""

    def _alcance(self, archivos):
        salida, _, _ = correr("marcas", "--raiz", self.carpeta(archivos))
        return [l for l in salida.splitlines() if l.startswith("Alcance: ") or l.startswith("Y ")]

    def test_dice_cuantos_archivos_miro(self):
        donde, _ = self._alcance({"base/uno.md": "# Uno\n", "plantillas/dos.md": "# Dos\n"})
        self.assertIn("2 archivos", donde)

    def test_no_cuenta_los_que_estan_fuera_de_su_alcance(self):
        donde, _ = self._alcance({"base/uno.md": "# Uno\n\nTexto limpio.\n",
                                  "documentacion/tres.md": "# Tres\n\nUna frase — con raya — acá.\n"})
        self.assertIn("1 archivos", donde)
        self.assertNotIn("documentacion", donde)

    def test_el_arbol_sin_nada_que_mirar_lo_dice(self):
        donde, _ = self._alcance({"notas/algo.md": "# Algo\n"})
        self.assertIn("no se miró ningún archivo", donde)

    def test_dice_que_partes_no_cuenta(self):
        _, sin_contar = self._alcance({"base/uno.md": "# Uno\n"})
        self.assertIn("leer", sin_contar)


class LaSesionTieneTraza(ConCarpeta):
    """`EP-005 · HU-016` · Qué ejecutó la sesión, paso a paso, sin copiar resultados."""

    BASE = "2026-08-20T10:00:%02d.000Z"

    def _transcripcion(self):
        lineas = []
        for id_, nombre, entrada, inicio, fin, error in (
                ("t1", "Read", {"file_path": "a.md"}, 0, 2, False),
                ("t2", "Bash", {"command": "python x.py"}, 10, 15, True),
                ("t3", "WebFetch", {"url": "https://e.test"}, 20, 21, False)):
            lineas.append({"type": "assistant", "timestamp": self.BASE % inicio, "message": {"content": [
                {"type": "tool_use", "id": id_, "name": nombre, "input": entrada}]}})
            lineas.append({"type": "user", "timestamp": self.BASE % fin, "message": {"content": [
                {"type": "tool_result", "tool_use_id": id_, "is_error": error, "content": "CENTINELA-" + id_}]}})
        raiz = self.carpeta({"abc.jsonl": "\n".join(json.dumps(l) for l in lineas) + "\n"})
        return os.path.join(raiz, "abc.jsonl")

    def test_tres_pasos_uno_con_error(self):
        salida, _, codigo = correr("traza", self._transcripcion())
        self.assertEqual(0, codigo)
        datos = [l for l in salida.splitlines() if l.startswith("| ") and l.split("|")[1].strip().isdigit()]
        self.assertEqual(3, len(datos))
        self.assertIn("Read", datos[0])
        self.assertIn("2 s", datos[0])
        self.assertIn("error", datos[1])
        self.assertNotIn("CENTINELA", salida)

    def test_sin_pasos_lo_dice_y_sale_con_uno(self):
        salida, _, codigo = correr("traza", os.path.join(self.carpeta(), "no-existe.jsonl"))
        self.assertEqual(1, codigo)
        self.assertIn("sin pasos que trazar", salida)


class LaPuertaDeLosEnganches(unittest.TestCase):
    """`validadores/validar.py` sigue existiendo: los `.githooks` de cada
    proyecto instalado lo llaman por esa ruta."""

    def test_el_enganche_del_commit_corre_por_la_puerta(self):
        r = por_la_puerta("versionado", "--raiz", ESTANDAR, "--preparados")
        self.assertIn(r.returncode, (0, 1), r.stderr)
        self.assertIn("== Qué está versionado (lo que entra en el commit) · . ==", r.stdout)

    def test_sin_subcomando_dice_como_se_usa_y_sale_con_dos(self):
        """No termina en silencio: «no comprobé nada» no se confunde con «hay fallas»."""
        r = por_la_puerta()
        self.assertEqual(2, r.returncode)
        self.assertIn("usage", r.stderr.lower())

    def test_la_puerta_sigue_dando_lo_que_las_pruebas_viejas_importan(self):
        spec = importlib.util.spec_from_file_location("puerta_validar", PUERTA)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        self.assertIs(FUERA_DE_LA_CORRIDA, modulo.FUERA_DE_LA_CORRIDA)
        self.assertIs(raiz_del_proyecto, modulo.raiz_del_proyecto)

    def test_la_puerta_no_importa_nada_de_validadores(self):
        with open(validar.__file__, encoding="utf-8") as f:
            fuente = f.read()
        self.assertNotRegex(fuente, r"(?m)^\s*(import|from)\s+(comun|validadores)\b")


class LosQueSeCorrenAparte(unittest.TestCase):

    def test_internas_reclamo_existe(self):
        salida, _, codigo = correr("internas", "--reclamo")
        self.assertIn(codigo, (0, 1))
        self.assertIn("pruebas del estándar", salida.lower())

    def test_metareglas_comprueba_algo(self):
        salida, _, _ = correr("metareglas")
        self.assertIn("meta-reglas", salida.lower())
        self.assertTrue(salida.strip())
