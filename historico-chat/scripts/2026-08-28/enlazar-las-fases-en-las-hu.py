# -*- coding: utf-8 -*-
"""Pone la fila de la fase en la §7 de cada historia, y le cambia el estado.

Sin esta fila la fase existe en el disco y la historia no la nombra: es el
mismo defecto que `H-52` ---la carpeta se crea al trabajar y la tabla vive en
otro archivo que se edita en otro rato--- y ya cobro dos veces esta semana.

**Solo toca las historias cuya fase ya esta escrita.** Si la carpeta no existe,
no se escribe la fila: una fila que apunta a nada es peor que ninguna.
"""
import io
import os
import re
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICA = os.path.join(RAIZ, "documentacion", "epicas",
                     "EP-001-cuerpo-de-reglas-heredable")
DE_CAPITULO = re.compile(r"^HU-(\d+)-el-capitulo-(\d+)-")

VIEJA = ("| (ninguna todav\u00eda) | | La primera fase ser\u00e1 la "
         "retrodocumentaci\u00f3n del cap\u00edtulo |")

puestas, sin_fase, ya_estaban = 0, 0, 0
for h in sorted(os.listdir(EPICA)):
    m = DE_CAPITULO.match(h)
    if not m:
        continue
    numero_hu, cap = m.group(1), m.group(2)
    fase = "A-EP-001-HU-%s-retrodocumentar-el-capitulo-%s" % (numero_hu, cap)
    if not os.path.isdir(os.path.join(EPICA, h, fase)):
        print("SIN FASE  %s" % h)
        sin_fase += 1
        continue

    ruta = os.path.join(EPICA, h, h + ".md")
    with io.open(ruta, encoding="utf-8") as f:
        t = f.read()

    if fase in t:
        ya_estaban += 1
        continue
    if VIEJA not in t:
        print("NO CALZA  %s  (la fila de §7 no es la esperada)" % h)
        sin_fase += 1
        continue

    nueva = ("| [%s](%s/) | CA-01, CA-02 | **Terminada** \u00b7 "
             "[Cumple](%s/resultado_pruebas.md) |" % (fase, fase, fase))
    t = t.replace(VIEJA, nueva, 1)
    t = t.replace("| **Estado** | Pendiente |", "| **Estado** | Terminada |", 1)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    puestas += 1

print("")
print("Filas puestas: %d \u00b7 ya estaban: %d \u00b7 sin fase o sin calzar: %d"
      % (puestas, ya_estaban, sin_fase))
