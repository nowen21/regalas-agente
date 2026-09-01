# -*- coding: utf-8 -*-
"""Agrega S-101, de la fase `A-EP-012-HU-001`."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVA = u"""
## S-101 · La marca de un hueco es una convención, no una forma tipográfica  ·  patrón · activa
- **What:** al contar qué documentos del expediente estaban a medio llenar, la primera versión conto como hueco cualquier texto entre comillas angulares. Sobre los 1 002 documentos traídos de este repositorio dio **559 «a medio llenar»**. Contando solo la marca que el estándar fija para eso, quedan **31**.
- **Why:** en esta casa se cita con esas mismas comillas todo el tiempo, y por eso el conteo daba por incompleto cualquier documento bien escrito. Un reporte que marca 559 de 762 no lo mira nadie: se lee como que el proyecto entero está a medio hacer, y ahí se pierde la información de los 31 que sí lo están.
- **Also:** el otro defecto de la misma fase es de la misma familia. **Ordenar «por el ciclo» se cae dentro del grupo, no entre grupos:** los cinco documentos de una fase salían por nombre de archivo, con el cierre antes que el plan. Entre grupos el orden estaba bien y se veía bien; el error vivía un nivel más adentro.
- **And:** los dos los cazó una prueba o la corrida sobre datos reales, no la lectura del código. Con documentos de mentiras el conteo de huecos se ve perfecto: una conversación inventada no trae citas, igual que no trae lo que pega el editor (`S-099`).
- **Where:** `plataforma/nucleo/expediente/core.py`, `MARCA_DEL_HUECO` · `orden.posicion_en_grupo` · la fase `A-EP-012-HU-001`.
- **Learned:** cuando algo se cuenta buscando una forma \u2014unas comillas, una raya, una etiqueta\u2014 hay que preguntarse **qué más tiene esa forma** en el texto real. Y un orden se comprueba en el nivel más profundo que tenga, porque el de arriba casi siempre sale bien.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar y plataforma; aplica a toda medición que reconozca algo por su forma.
- **Rel:** S-099 (el reporte medía la herramienta), S-095 (nombrar un enganche no es serlo).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-101" in t:
    print("ya estaba: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVA)
    print("senal S-101 agregada")
