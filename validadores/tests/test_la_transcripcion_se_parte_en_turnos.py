# -*- coding: utf-8 -*-
"""`EP-011 · HU-001` — quien escribe el formato es quien sabe leerlo.

`historico.py` escribe la transcripción: el mensaje del usuario citado con `>`,
y la respuesta del agente con su sello de máquina. **Leerla vive en el mismo
archivo a propósito.** La plataforma indexa las conversaciones con esta función,
y copiar allá las expresiones dejaría dos verdades que se separan el día que una
marca cambie — y la copia vieja leería mal en silencio.

Es el mismo argumento que ya sostiene `nucleo/seguridad/claves.py`, que tampoco
reconoce las claves: se las pide al estándar.
"""
import io
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import historico     # noqa: E402


def transcripcion(*turnos):
    """Una transcripción como la escribe el enganche."""
    partes = ["<!-- sesion: abc -->\n\n# 2026-01-02 — Sesión\n\n## Conversación\n"]
    for i, (quien, dicho) in enumerate(turnos, 1):
        if quien == "usuario":
            cita = "\n".join("> %s" % l for l in dicho.split("\n"))
            partes.append("\n### %d · Usuario — 2026-01-02 10:0%d:00\n%s\n"
                          % (i, i, cita))
        else:
            partes.append("\n**Agente** — 2026-01-02 10:0%d:30\n"
                          "<!-- agente: %d -->\n\n%s\n" % (i, i, dicho))
    return "".join(partes)


class LosTurnosSalenEnOrden(unittest.TestCase):

    def test_el_turno_del_usuario_se_reconoce(self):
        turnos = historico.turnos(transcripcion(("usuario", "hola")))
        self.assertEqual([("usuario", "2026-01-02 10:01:00", "hola")], turnos)

    def test_el_turno_del_agente_se_reconoce(self):
        turnos = historico.turnos(transcripcion(("agente", "qué tal")))
        self.assertEqual("agente", turnos[0][0])
        self.assertEqual("qué tal", turnos[0][2])

    def test_van_en_el_orden_de_la_conversacion(self):
        turnos = historico.turnos(transcripcion(
            ("usuario", "uno"), ("agente", "dos"), ("usuario", "tres")))
        self.assertEqual(["usuario", "agente", "usuario"],
                         [t[0] for t in turnos])

    def test_la_cita_del_usuario_se_desarma(self):
        """Se escribe con `>` delante; lo que el usuario dijo no lleva eso."""
        turnos = historico.turnos(transcripcion(("usuario", "primera\nsegunda")))
        self.assertEqual("primera\nsegunda", turnos[0][2])

    def test_el_sello_de_maquina_no_es_parte_de_lo_dicho(self):
        turnos = historico.turnos(transcripcion(("agente", "respuesta")))
        self.assertNotIn("<!-- agente:", turnos[0][2])

    def test_la_hora_es_la_que_el_enganche_anoto(self):
        turnos = historico.turnos(transcripcion(("agente", "x")))
        self.assertEqual("2026-01-02 10:01:30", turnos[0][1])


class LoQueNoEncajaNoSeInventa(unittest.TestCase):

    def test_un_texto_sin_marcas_no_da_turnos(self):
        """Lista vacía es un dato: esa sesión no tenía conversación escrita."""
        self.assertEqual([], historico.turnos("# Un documento cualquiera\n"))

    def test_un_texto_vacio_no_revienta(self):
        self.assertEqual([], historico.turnos(""))

    def test_none_no_revienta(self):
        self.assertEqual([], historico.turnos(None))

    def test_el_encabezado_de_la_sesion_no_es_un_turno(self):
        turnos = historico.turnos(transcripcion(("usuario", "hola")))
        self.assertEqual(1, len(turnos))


class SobreElHistoricoDeVerdad(unittest.TestCase):
    """Contra los archivos que el enganche escribió, no contra los inventados."""

    def _una_transcripcion(self):
        carpeta = os.path.join(os.path.dirname(VALIDADORES), "historico-chat")
        for nombre in sorted(os.listdir(carpeta), reverse=True):
            if nombre.endswith(".md") and nombre[:4].isdigit():
                return os.path.join(carpeta, nombre)
        return ""

    def test_una_sesion_real_se_parte_en_turnos(self):
        ruta = self._una_transcripcion()
        if not ruta:
            self.skipTest("no hay transcripciones en este repositorio")
        with io.open(ruta, encoding="utf-8", errors="replace") as f:
            turnos = historico.turnos(f.read())
        self.assertGreater(len(turnos), 0)
        self.assertTrue(all(t[0] in ("usuario", "agente") for t in turnos))
        self.assertTrue(all(t[2] for t in turnos))


if __name__ == "__main__":
    unittest.main(verbosity=2)
