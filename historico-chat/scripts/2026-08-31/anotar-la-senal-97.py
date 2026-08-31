# -*- coding: utf-8 -*-
"""Agrega S-097, de la fase `A-EP-011-HU-001`."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
R = os.path.join(RAIZ, "documentacion", "senales.md")

NUEVA = u"""
## S-097 · La batería de la plataforma no la corre nadie, y una subida de versión la puso en rojo  ·  aprendizaje · activa
- **What:** al abrir la primera fase de la plataforma en once días, dos de sus 187 pruebas estaban en rojo. **No por esa fase:** su proyecto de mentiras declaraba la versión del estándar escrita a mano, y esa misma mañana el estándar había subido de `37.0.0` a `37.1.0`. Las dos pruebas daban por supuesto que el proyecto estaba al día, y dejó de ser cierto.
- **Why:** `validar.py internas` corre las pruebas de `validadores/tests/` y **ninguna de las 187 de `plataforma/`**. Así que el rojo estuvo puesto desde la mañana y se supo por la tarde, y solo porque hubo que tocar la plataforma. El estándar tiene una historia entera sobre esto —que las pruebas que existen se corran— y la plataforma quedó fuera de su alcance sin que nadie lo notara.
- **Also:** el defecto de las dos pruebas es el mismo patrón de siempre: **un número escrito a mano al lado de otro que se mueve**. La cura fue la de siempre: leerlo de donde vive. Ahora el proyecto de mentiras declara la versión que el estándar publica, y la prueba no se cae la próxima vez que suba.
- **And:** lo que lo destapó fue correr la batería entera **antes** de dar la fase por buena, no después. Si esta fase solo hubiera corrido sus propias pruebas —que era lo que `02·F5` permite— el rojo seguiría puesto.
- **Where:** `plataforma/nucleo/proyectos/tests.py`, `version_al_dia()` · la fase `A-EP-011-HU-001`.
- **Learned:** cuando un repositorio guarda dos productos con dos baterías, la que no corre el comando de todos los días **se pudre sin avisar**. Y una prueba que escribe a mano un número que otro programa mueve tiene fecha de caducidad desde que se escribe.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar y plataforma; aplica a toda suite que no cuelgue de la corrida diaria.
- **Rel:** S-091 (la frase que describe lo que hace un programa se deriva), S-096 (lo nuevo no pasó por donde la regla vigila).
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "S-097" in t:
    print("ya estaba: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + NUEVA)
    print("senal S-097 agregada")
