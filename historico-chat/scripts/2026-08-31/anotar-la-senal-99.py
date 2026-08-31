# -*- coding: utf-8 -*-
"""Agrega S-099, de la fase `A-EP-011-HU-002`."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVA = u"""
## S-099 · El primer reporte medía lo que pega la herramienta, no lo que escribió la persona  ·  patrón · activa
- **What:** el reporte de qué correcciones se repiten salió, en su primera corrida sobre datos reales, con **las catorce primeras filas hechas de ruido**: «this may», «current task», «the user», «ide_opened_file the», cada una 139 veces en 41 sesiones. Son los bloques que el editor le pega al mensaje del usuario para decir qué archivo tiene abierto y qué líneas seleccionó.
- **Why:** esos bloques **están dentro del mensaje del usuario** en la transcripción, porque así llegan. Un programa que cuenta «lo que dijo el usuario» los cuenta como dichos, y entonces mide la herramienta en vez de la persona. Un reporte cuyas primeras filas no las escribió nadie es peor que no tenerlo: da la sensación de estar mirando.
- **Also:** **con datos inventados se habría visto perfecto.** Una conversación de mentiras no trae bloques del editor, así que las pruebas del módulo pasaban todas. Lo que lo destapó fue correrlo sobre las 67 sesiones reales, que es lo que el plan pedía como último paso.
- **And:** el arreglo es de una línea de idea y varias de lista: lo que viene entre las etiquetas de la herramienta se saca antes de contar. La lista de etiquetas está escrita y se lee, porque el día que la herramienta agregue una nueva, esta cuenta vuelve a ensuciarse en silencio.
- **Where:** `plataforma/nucleo/medicion/repeticion.py`, `sin_lo_de_la_maquina` · la fase `A-EP-011-HU-002`.
- **Learned:** un reporte sobre lo que dijo una persona se corre **sobre datos reales antes de darlo por bueno**. Los inventados no traen lo que la herramienta agrega, y eso es justamente lo que ensucia la cuenta.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar y plataforma; aplica a toda medición sobre texto conversado.
- **Rel:** S-087 (un caso mal armado se lee igual que un programa roto), S-097 (la batería que nadie corría).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-099" in t:
    print("ya estaba: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVA)
    print("senal S-099 agregada")
