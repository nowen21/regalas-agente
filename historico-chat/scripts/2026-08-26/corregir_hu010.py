# -*- coding: utf-8 -*-
"""Corrige lo que se afirmó sin leer: la EP-001 HU-010 no está abierta.

Cerró el 2026-08-18 en `febcaf3`, y cerró **diciendo que no hacía falta regla
nueva**: `02·F19` ya dice que «la redacción del CA es la especificación
funcional». Se afirmó lo contrario en cinco documentos, y cada repetición lo
hizo parecer más establecido.
"""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")

H19 = ("documentacion/epicas/EP-004-comprobacion-automatica/"
       "HU-019-inventario-que-no-se-mantiene-a-mano/"
       "A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/")
H20 = ("documentacion/epicas/EP-004-comprobacion-automatica/"
       "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano/"
       "A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/")

BUENO_PLAN = (
    "**No hay documento aparte, y la regla que lo permite ya existe.** "
    "[`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/"
    "F19-implementa-literal-el-criterio-de-aceptacion.md) dice que **la "
    "redacción del CA es la especificación funcional**. La historia trae "
    "alcance, reglas de negocio, criterios con sus pasos y requisitos no "
    "funcionales: un documento aparte la repetiría.\n"
    "\n"
    "> **Acá se citó primero la [EP-001 · HU-010]"
    "(../../../EP-001-cuerpo-de-reglas-heredable/"
    "HU-010-cuando-no-aplica-la-especificacion/"
    "HU-010-cuando-no-aplica-la-especificacion.md) como si estuviera abierta "
    "esperando escribir esa regla, y se corrigió el 2026-08-26.** Está "
    "**cerrada** desde el 2026-08-18, y cerró diciendo «nada nuevo, y ese es "
    "el resultado»: el capítulo ya la contestaba dos reglas más abajo, y "
    "agregar otra chocaba con `02·F0`. Se afirmó sin leer su estado.")

CAMBIOS = [
 # -- HU-019, plan de trabajo --
 (H19 + "plan_trabajo.md",
  "| **Especificación del módulo** | **No hay documento aparte, y se declara "
  "por qué.** La historia trae alcance, reglas de negocio, criterios con sus "
  "pasos y requisitos no funcionales: una especificación separada repetiría la "
  "historia. Es el caso que la [EP-001 · HU-010](../../../"
  "EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/"
  "HU-010-cuando-no-aplica-la-especificacion.md) está abierta para dejar "
  "escrito en el estándar, y **esta es la tercera fase que lo declara**. Se "
  "anota acá para que quede como evidencia de esa historia, no como excepción "
  "silenciosa |",
  "| **Especificación del módulo** | " + BUENO_PLAN.replace("\n", " ") + " |"),

 # -- HU-019, estado de fase --
 (H19 + "estado-fase.md",
  "**La estación 5 pasó sin documento aparte, y se dice por qué.** La historia "
  "trae alcance, reglas de negocio, criterios con sus pasos y requisitos no "
  "funcionales; una especificación separada repetiría la historia. Es el caso "
  "que la [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/"
  "HU-010-cuando-no-aplica-la-especificacion/"
  "HU-010-cuando-no-aplica-la-especificacion.md) está abierta para dejar "
  "escrito en el estándar, y **esta es la tercera fase que lo declara**. Queda "
  "anotado como evidencia de esa historia, no como excepción silenciosa.",
  "**La estación 5 pasó sin documento aparte, y la regla que lo permite ya "
  "existe.** [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/"
  "F19-implementa-literal-el-criterio-de-aceptacion.md) dice que la redacción "
  "del CA es la especificación funcional.\n"
  "\n"
  "> **Acá se citó la `EP-001 · HU-010` como si estuviera abierta esperando "
  "escribir esa regla, y se corrigió el 2026-08-26.** Está cerrada desde el "
  "2026-08-18, y cerró diciendo que no hacía falta regla nueva. Se afirmó sin "
  "leer su estado."),

 # -- HU-020, plan de trabajo --
 (H20 + "plan_trabajo.md",
  "| **Especificación del módulo** | **No hay documento aparte**, por lo mismo "
  "que la fase anterior: la historia trae alcance, reglas, criterios con pasos "
  "y requisitos no funcionales. **Es la cuarta fase que lo declara**, y sigue "
  "siendo evidencia para la [EP-001 · HU-010](../../../"
  "EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/"
  "HU-010-cuando-no-aplica-la-especificacion.md), que está abierta para "
  "escribir esa regla |",
  "| **Especificación del módulo** | " + BUENO_PLAN.replace("\n", " ") + " |"),

 # -- HU-020, estado de fase --
 (H20 + "estado-fase.md",
  "**La estación 5 pasó sin documento aparte, y es la cuarta vez.** La "
  "historia trae alcance, reglas, criterios con pasos y requisitos no "
  "funcionales; una especificación separada la repetiría. Sigue siendo el caso "
  "que la [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/"
  "HU-010-cuando-no-aplica-la-especificacion/"
  "HU-010-cuando-no-aplica-la-especificacion.md) está abierta para escribir. "
  "**Cuatro fases declarándolo ya no es un caso suelto: es la regla que "
  "falta.**",
  "**La estación 5 pasó sin documento aparte, y la regla que lo permite ya "
  "existe.** [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/"
  "F19-implementa-literal-el-criterio-de-aceptacion.md) dice que la redacción "
  "del CA es la especificación funcional.\n"
  "\n"
  "> **Acá decía que la `EP-001 · HU-010` estaba abierta y que «cuatro fases "
  "declarándolo ya no es un caso suelto: es la regla que falta». Se corrigió "
  "el 2026-08-26, y era falso.** Esa historia cerró el 2026-08-18 diciendo "
  "justamente que no hacía falta regla nueva. Cuatro documentos repitieron la "
  "afirmación, y cada repetición la hizo parecer más establecida."),

 # -- HU-020, cierre: identificación --
 (H20 + "funcionalidad_implementada.md",
  "| **Especificación del módulo** | No hay documento aparte. La historia hace "
  "de especificación, declarado en el [plan_trabajo.md](plan_trabajo.md) §0. "
  "**Cuarta fase que lo declara** |",
  "| **Especificación del módulo** | No hay documento aparte, y la regla que "
  "lo permite ya existe: `02·F19`, «la redacción del CA es la especificación "
  "funcional». Ver §6 |"),

 # -- HU-020, cierre: la deuda que decia que faltaba la regla --
 (H20 + "funcionalidad_implementada.md",
  "| **Cuatro fases seguidas declararon no llevar especificación aparte** | "
  "Acumulado | Ya no es un caso suelto: es la regla que falta. La [EP-001 · "
  "HU-010](../../../EP-001-cuerpo-de-reglas-heredable/"
  "HU-010-cuando-no-aplica-la-especificacion/"
  "HU-010-cuando-no-aplica-la-especificacion.md) lleva abierta esperando "
  "escribirla |",
  "| ~~Cuatro fases seguidas declararon no llevar especificación aparte, y la "
  "regla falta~~ **Era falso** | Acumulado, y mal | La regla **existe**: "
  "`02·F19`. La `EP-001 · HU-010` cerró el 2026-08-18 diciendo que no hacía "
  "falta ninguna nueva. Se afirmó lo contrario en cinco documentos sin leer su "
  "estado, y se corrigió el 2026-08-26. `S-048` |"),
]

for ruta, viejo, nuevo in CAMBIOS:
    t = io.open(ruta, encoding="utf-8").read()
    assert t.count(viejo) == 1, "no coincide en %s -> %s" % (ruta[-26:], viejo[:50])
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))

print("Corregidos %d documentos" % len(CAMBIOS))
