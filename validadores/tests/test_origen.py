# -*- coding: utf-8 -*-
"""`EP-023 · HU-002 · fase A` · Cada punto dice de qué punto del anterior sale.

El caso CP-002 del plan de pruebas de la fase, sobre una épica de prueba en una
carpeta temporal.
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import origen   # noqa: E402

RESUMEN = "# Sesión\n\n### H-1. Algo falla\n\n| Campo | Valor |\n|---|---|\n| Qué pasó | x |\n"

PENDIENTE = ("# Pendiente: algo falla\n\n| | |\n|---|---|\n"
             "| **De dónde sale** | [H-1 de la sesión](../../../../resumen.md) |\n")

ANALISIS = """# Análisis 1: algo falla

> **Aprobado** por el usuario el 2026-10-02, en el turno 3.

## Conversación

### 1 · Usuario, 2026-10-02 10:00:00
> uno

### 2 · Usuario, 2026-10-02 10:01:00
> dos

> acá termina la conversación

## Conclusiones

| # | Tema | Conclusión | Sale de |
|---|---|---|---|
| 1 | Algo | Se hace algo | Turno {turno} |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de la conclusión | Pasó a |
|---|---|---|---|
| 1 | Hacer algo | {conclusion} | EP-009, HU-001 |
"""

HU = """# HU-001 · Algo

## 4. Criterios de aceptación

### CA-01 · Algo pasa

{sale_de}

```gherkin
Dado algo
```
"""


class Origen(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        self.epica = os.path.join(self.raiz, "documentacion", "epicas", "EP-009-algo")
        self.pendiente = os.path.join(self.epica, "7-algo-falla")
        self.armar()

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, ruta, texto):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)

    def armar(self, turno=1, conclusion="1", sale_de="**Sale de:** análisis 1, punto 1.",
               pendiente=PENDIENTE):
        self.escribir(os.path.join(self.raiz, "resumen.md"), RESUMEN)
        self.escribir(os.path.join(self.pendiente, "pendiente.md"), pendiente)
        self.escribir(os.path.join(self.pendiente, "analisis-1.md"),
                      ANALISIS.format(turno=turno, conclusion=conclusion))
        self.escribir(os.path.join(self.epica, "HU-001-algo", "HU-001-algo.md"),
                      HU.format(sale_de=sale_de))

    def fallas(self):
        return [m for _, m in origen.revisar(self.raiz)]

    def test_paso1_todo_con_su_origen_pasa(self):
        self.assertEqual(self.fallas(), [])

    def test_paso2_criterio_sin_sale_de(self):
        self.armar(sale_de="")
        self.assertEqual(self.fallas(), ["el CA-01 no tiene «Sale de»"])

    def test_paso3_criterio_cita_un_punto_que_no_existe(self):
        self.armar(sale_de="**Sale de:** análisis 1, punto 9.")
        self.assertEqual(self.fallas(), ["el CA-01 cita el punto 9 del análisis 1, que no existe"])

    def test_paso4_conclusion_cita_un_turno_que_no_existe(self):
        self.armar(turno=8)
        self.assertEqual(self.fallas(), ["la conclusión 1 cita el turno 8, que no está en la conversación"])

    def test_paso5_punto_cita_una_conclusion_que_no_existe(self):
        self.armar(conclusion="4")
        self.assertEqual(self.fallas(),
                         ["el punto 1 de «Lo que se tiene que hacer» cita la conclusión 4, que no existe"])

    def test_paso6_pendiente_sin_origen_o_con_hallazgo_que_no_existe(self):
        self.armar(pendiente="# Pendiente: algo falla\n")
        self.assertEqual(self.fallas(), ["el pendiente no tiene «De dónde sale»"])
        self.armar(pendiente=PENDIENTE.replace("H-1 ", "H-5 "))
        self.assertEqual(self.fallas(), ["cita H-5, que no está en ../../../../resumen.md"])

    def test_paso7_epica_sin_analisis_no_se_revisa(self):
        otra = os.path.join(self.raiz, "documentacion", "epicas", "EP-001-vieja")
        self.escribir(os.path.join(otra, "HU-001-vieja", "HU-001-vieja.md"), HU.format(sale_de=""))
        self.assertEqual(self.fallas(), [])

    def test_el_mensaje_cita_la_regla(self):
        self.armar(sale_de="")
        self.assertIn("02·F27", origen.validar(self.raiz)[0].mensaje)


if __name__ == "__main__":
    unittest.main()
