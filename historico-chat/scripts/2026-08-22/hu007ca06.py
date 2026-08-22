# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")

H = "documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/"
p = H + "HU-007-regla-de-las-reglas.md"
s = L.leer(p)
ca06 = """### CA-06 — Lo que se pidió dos veces no se pierde entre sesiones

```gherkin
Dado que el usuario pidió un mismo criterio en dos sesiones distintas y en el momento nadie lo notó
Cuando se va a publicar la versión que cierra ese tramo
Entonces el procedimiento obliga a releer el tramo y a escribir ese criterio como candidata a regla, con las veces que se pidió
Y la candidata sale con una de cuatro salidas: cubierta, regla nueva, afinar una existente, o no es regla del estándar
Y ninguna candidata se convierte en regla desde ese documento: eso lo decide el usuario
```

**Por qué no lo cubría ninguno de los cinco anteriores, ni `01·C10`.** `C10` atrapa el patrón **en el momento** en que el pedido llega, y lo que se pierde es justamente lo que en el momento no se notó: dos pedidos parecidos, con otras palabras, separados por diez sesiones. `CA-01` a `CA-03` revisan la regla cuando ya alguien decidió escribirla; este se para antes, cuando todavía nadie la propuso.

**Cómo validarlo:**

1. Tomar el barrido que se hizo a mano el 2026-08-13 ([prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md](../../../../prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md)) y comprobar que el molde del estándar habría producido lo mismo: 27 fichas, cada una con una de las cuatro salidas. Resultado esperado: ninguna de las 27 se queda sin salida posible.
2. Comprobar que el disparo existe en el flujo: la regla nombra el momento de publicar la versión, que `20·M10` ya obliga a atravesar. Resultado esperado: el barrido no depende de que alguien se acuerde de pedirlo.
- **Aprobado cuando:** el molde está en `plantillas/`, la regla del capítulo `20` lo exige antes de publicar, y las cuatro salidas están escritas y son excluyentes.

"""
a = "### Criterios de aceptación transversales"
assert a in s
s = s.replace(a, ca06 + a, 1)
L.escribir(p, s)
print("ok")
