# -*- coding: utf-8 -*-
"""`00·ID8` · `00·ID9` · `00·ID10` — medir el turno al cerrarlo.

**Las tres reglas hablan de cómo escribe el agente y ninguna tenía quien la
hiciera cumplir.** La evidencia está contada en el [pendiente 58](../../pendientes/hecho/nada-hace-cumplir-id9.md):
en otro proyecto el usuario pidió «menos es más» **siete veces en tres días**, y
cada vez se anotó el caso sin que cambiara nada.

**Mide y no detiene, y eso es lo que la historia acepta.** Cuando el enganche
corre, el texto ya salió: no hay nada que bloquear. Lo único que queda es
dejarlo a la vista (`RN-05` de `EP-005·HU-012`).

**Se calla cuando todo está bien**, y esa es la mitad que estas pruebas cuidan.
Un aviso que sale en cada turno deja de leerse a la tercera, y entonces tampoco
se lee el que sí importaba.
"""
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

ADAPTADOR = os.path.join(os.path.dirname(VALIDADORES),
                         "adaptadores", "claude-code")
sys.path.insert(0, ADAPTADOR)

import brevedad      # noqa: E402
import instalar      # noqa: E402
import redaccion     # noqa: E402

ENGANCHE = os.path.join(ADAPTADOR, "hook_redaccion.py")


class ElTratoDirectoSeCuenta(unittest.TestCase):
    """`00·ID10` descarta el trato directo sin discusión, así que se cuenta."""

    def test_usted_se_cuenta(self):
        self.assertEqual(1, len(redaccion.tratos(u"Usted abre la terminal.")))

    def test_tu_se_cuenta(self):
        self.assertEqual(1, len(redaccion.tratos(u"Después tú lo ejecutas.")))

    def test_la_tercera_persona_no_se_cuenta(self):
        self.assertEqual([], redaccion.tratos(
            u"El agente abre la terminal y ejecuta el programa."))

    def test_el_infinitivo_no_se_cuenta(self):
        self.assertEqual([], redaccion.tratos(
            u"Abrir la terminal y ejecutar el programa."))

    def test_lo_citado_no_se_cuenta(self):
        """**Citar es reportar, no redactar.** La regla lo dice de frente."""
        self.assertEqual([], redaccion.tratos(
            u"El texto dice «usted» y eso es una cita."))

    def test_lo_que_va_en_codigo_no_se_cuenta(self):
        self.assertEqual([], redaccion.tratos(
            u"```\nprint('usted')\n```"))

    def test_se_dice_en_que_linea_aparece(self):
        tratos = redaccion.tratos(u"primera línea\nUsted abre la terminal.")
        self.assertEqual(2, tratos[0][0])

    def test_una_palabra_que_contiene_tu_no_cuenta(self):
        """`estudio` lleva las letras y no es un trato."""
        self.assertEqual([], redaccion.tratos(u"El estudio y el atún."))


class LaMedidaDeUnTurno(unittest.TestCase):

    def test_los_caracteres_son_los_del_texto(self):
        self.assertEqual(5, redaccion.medir(u"  12345  ")["caracteres"])

    def test_las_marcas_de_id8_se_cuentan(self):
        m = redaccion.medir(u"El agente abre la terminal — y la cierra.")
        self.assertEqual(1, m["marcas"])

    def test_las_marcas_dentro_del_codigo_no_se_cuentan(self):
        m = redaccion.medir(u"```\nuna raya — dentro del código\n```")
        self.assertEqual(0, m["marcas"])

    def test_el_texto_limpio_no_deja_nada(self):
        m = redaccion.medir(u"El agente abre la terminal y ejecuta el programa.")
        self.assertEqual(0, m["marcas"])
        self.assertEqual([], m["tratos"])


class LaLineaDeCierre(unittest.TestCase):
    """La salida del enganche: lo único que el usuario llega a ver."""

    def test_el_texto_limpio_no_dice_nada(self):
        self.assertEqual(u"", redaccion.linea_de_cierre(
            u"El agente abre la terminal y ejecuta el programa."))

    def test_el_trato_directo_se_reporta_con_la_palabra(self):
        linea = redaccion.linea_de_cierre(u"Usted abre la terminal.")
        self.assertIn(u"00·ID10", linea)
        self.assertIn(u"usted", linea)

    def test_la_marca_se_reporta_nombrando_id8(self):
        linea = redaccion.linea_de_cierre(
            u"El agente abre la terminal — y la cierra.")
        self.assertIn(u"00·ID8", linea)

    def test_el_largo_se_compara_contra_el_umbral_de_brevedad(self):
        """`S-091` — un umbral escrito aparte se separa del otro sin avisar."""
        linea = redaccion.linea_de_cierre(u"a" * (brevedad.HOLGADO + 1))
        self.assertIn(u"00·ID9", linea)
        self.assertIn(str(brevedad.HOLGADO), linea)

    def test_lo_que_cabe_en_el_umbral_no_se_reporta(self):
        self.assertEqual(u"", redaccion.linea_de_cierre(u"a" * 100))

    def test_la_mediana_de_la_sesion_se_dice_cuando_se_conoce(self):
        linea = redaccion.linea_de_cierre(u"a" * (brevedad.HOLGADO + 1), 900)
        self.assertIn(u"900", linea)

    def test_las_tres_caben_en_una_linea(self):
        linea = redaccion.linea_de_cierre(
            u"Usted abre la terminal — y la cierra. " + u"a" * brevedad.HOLGADO)
        self.assertIn(u"00·ID8", linea)
        self.assertIn(u"00·ID9", linea)
        self.assertIn(u"00·ID10", linea)


class ElEngancheDeCierre(unittest.TestCase):
    """De punta a punta: lo que el enganche recibe y lo que deja."""

    def _correr(self, datos):
        p = subprocess.Popen([sys.executable, ENGANCHE],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        salida, error = p.communicate(
            json.dumps(datos, ensure_ascii=False).encode("utf-8"))
        return (p.returncode, salida.decode("utf-8", "replace"),
                error.decode("utf-8", "replace"))

    def _transcript(self, respuesta):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        ruta = os.path.join(tmp.name, "transcript.jsonl")
        entradas = [
            {"type": "user", "message": {"role": "user", "content": "hola"}},
            {"type": "assistant", "message": {"role": "assistant", "content": [
                {"type": "text", "text": respuesta}]}}]
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            for e in entradas:
                f.write(json.dumps(e, ensure_ascii=False) + u"\n")
        return ruta

    def test_lo_sucio_se_deja_a_la_vista(self):
        ruta = self._transcript(u"Usted abre la terminal.")
        codigo, salida, _e = self._correr(
            {"transcript_path": ruta, "session_id": "x"})
        self.assertEqual(0, codigo)
        self.assertIn(u"ID10", salida)

    def test_lo_limpio_no_dice_nada(self):
        ruta = self._transcript(u"El agente abre la terminal.")
        _c, salida, _e = self._correr(
            {"transcript_path": ruta, "session_id": "x"})
        self.assertEqual(u"", salida.strip())

    def test_sin_transcripcion_termina_bien_y_calla(self):
        codigo, salida, _e = self._correr(
            {"transcript_path": "", "session_id": "x"})
        self.assertEqual(0, codigo)
        self.assertEqual(u"", salida.strip())

    def test_una_entrada_ilegible_no_rompe_el_turno(self):
        """**Medir no puede costarle el turno a nadie.**"""
        p = subprocess.Popen([sys.executable, ENGANCHE],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.communicate(b"esto no es json")
        self.assertEqual(0, p.returncode)


class ElCanalEsElInstalador(unittest.TestCase):
    """`RN-04` — el proyecto no puede agregar enganches por su cuenta."""

    def test_el_enganche_esta_declarado_en_el_instalador(self):
        declarados = [h[2] for h in instalar.HOOKS_CLAUDE]
        self.assertIn("hook_redaccion.py", declarados)

    def test_se_conecta_al_cerrar_el_turno(self):
        evento = [h[0] for h in instalar.HOOKS_CLAUDE
                  if h[2] == "hook_redaccion.py"]
        self.assertEqual(["Stop"], evento)

    def test_el_archivo_del_enganche_existe(self):
        self.assertTrue(os.path.isfile(ENGANCHE))

    def test_no_es_punto_de_entrada(self):
        with io.open(os.path.join(VALIDADORES, "redaccion.py"),
                     encoding="utf-8") as f:
            self.assertIn(u"no_es_punto_de_entrada", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
