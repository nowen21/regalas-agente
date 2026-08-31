# -*- coding: utf-8 -*-
"""Agrega S-100, de la fase `B-EP-011-HU-002`."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVA = u"""
## S-100 · La mejora propuesta y aprobada no funcionaba, y medirla costó veinte minutos  ·  aprendizaje · activa
- **What:** el reporte de correcciones repetidas salía encabezado por «debe quedar», «puede cerrar» y «debe tener», que no son correcciones sino la forma en que el usuario redacta cualquier exigencia. El agente propuso ordenar por sesiones distintas en vez de por veces, el usuario lo aprobó, y **al medirlo no cambiaba nada**: «debe quedar» seguía de primero, con catorce sesiones.
- **Why:** una propuesta que suena razonable se aprueba rápido, y construirla cuesta una fase entera. Medirla contra los datos de verdad costó veinte minutos y evitó entregar algo que no servía **con la aprobación del usuario encima**, que es la peor forma de entregar algo inservible: queda como si lo hubiera pedido él.
- **Also:** la segunda idea también se midió y también se descartó. Pesar cada frase por lo raras que son sus palabras se va al otro extremo: arriba quedan términos técnicos que solo aparecen juntos. **Dos de tres ideas no servían**, y eso solo se sabe probando.
- **And:** lo que sí sirvió fue **descartar las frases hechas con las palabras más comunes del propio corpus**, calculadas y no escritas a mano. «Español colombiano» pasó del puesto 21 al cuarto, y arriba apareció «estoy preguntando» en ocho sesiones distintas: el usuario aclarando que pregunta, no que ordena.
- **Where:** `plataforma/nucleo/medicion/repeticion.py`, `vocabulario_de_la_casa` · la fase `B-EP-011-HU-002`.
- **Learned:** cuando el agente propone una mejora y el usuario la aprueba, **medirla contra los datos antes de construirla**. Si no funciona, se dice y se propone la que sí: entregar lo aprobado sabiendo que no sirve es peor que haber propuesto mal.
- **When/Who:** 2026-08-31 · el usuario aprobó la primera; el agente midió y propuso la que funciona.
- **Scope:** estándar; aplica a toda mejora que el agente proponga sobre algo ya construido.
- **Rel:** S-092 (medir la lista de pendientes antes de estimarla), S-099 (el reporte medía la herramienta).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-100" in t:
    print("ya estaba: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVA)
    print("senal S-100 agregada")
