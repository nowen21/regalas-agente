# -*- coding: utf-8 -*-
"""Agrega S-102, de la fase `A-EP-012-HU-002`."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVA = u"""
## S-102 · Un convertidor se comprueba contando lo que quedó a la vista, no mirando un ejemplo  ·  patrón · activa
- **What:** el convertidor que produce el entregable pasaba todas sus pruebas con documentos inventados. Sobre los 762 documentos reales dejó **205 marcas del texto de origen a la vista**: 174 asteriscos porque el separador de una celda partía una negrita que lo contenía, y 31 barras porque una cita con una tabla adentro salía cruda. Un tercer defecto salió por el mismo camino: el código con asteriscos se volvía negrita, que es justo lo contrario de para qué se escribe.
- **Why:** los ejemplos de una prueba se eligen, y uno elige los casos que entiende. El texto real trae las combinaciones que a nadie se le ocurren: una negrita que contiene el separador de listas, una cita que trae una tabla, un trozo de código que muestra marcado para que no actúe. **Ninguno de los tres se ve leyendo el código.**
- **Also:** lo que los encontró fue contar, no mirar. Buscar cuántas marcas quedaron fuera de los bloques de código da un número que se puede seguir arreglo tras arreglo: 205, después 31, después 15. Mirar el archivo y decir «se ve bien» no distingue esos tres estados.
- **And:** las 15 que quedaron son de un solo caso —énfasis dentro de énfasis— y se dejaron declaradas. Quince en ocho millones de caracteres es dos milésimas de por mil; resolverlo bien pide un analizador de verdad, y eso se decide con el número delante, no con la impresión.
- **Where:** `plataforma/nucleo/expediente/marcado.py` · la fase `A-EP-012-HU-002`.
- **Learned:** cuando algo transforma texto, la prueba que vale es **contar sobre el texto real cuánto quedó mal**, y seguir ese número. Un ejemplo bien elegido dice que funciona; el conteo dice cuánto.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar y plataforma; aplica a toda pieza que transforme documentos.
- **Rel:** S-099 (el reporte medía la herramienta), S-101 (la marca de un hueco es una convención).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-102" in t:
    print("ya estaba: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVA)
    print("senal S-102 agregada")
