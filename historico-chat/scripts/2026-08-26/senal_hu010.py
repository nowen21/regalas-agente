# -*- coding: utf-8 -*-
"""S-048 y la corrección de H-34."""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")

# 1. La cita dentro de una celda de tabla no renderiza. Se vuelve texto.
MAL = ("un documento aparte la repetiría.  > **Acá se citó primero la "
       "[EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/"
       "HU-010-cuando-no-aplica-la-especificacion/"
       "HU-010-cuando-no-aplica-la-especificacion.md) como si estuviera "
       "abierta esperando escribir esa regla, y se corrigió el 2026-08-26.**")
BIEN = ("un documento aparte la repetiría. **Corregido el 2026-08-26:** acá se "
        "citó primero la [EP-001 · HU-010](../../../"
        "EP-001-cuerpo-de-reglas-heredable/"
        "HU-010-cuando-no-aplica-la-especificacion/"
        "HU-010-cuando-no-aplica-la-especificacion.md) como si estuviera "
        "abierta esperando escribir esa regla.")

for ruta in [
    "documentacion/epicas/EP-004-comprobacion-automatica/"
    "HU-019-inventario-que-no-se-mantiene-a-mano/"
    "A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/plan_trabajo.md",
    "documentacion/epicas/EP-004-comprobacion-automatica/"
    "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano/"
    "A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/plan_trabajo.md",
]:
    t = io.open(ruta, encoding="utf-8").read()
    assert t.count(MAL) == 1, "no coincide en %s" % ruta[-20:]
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        t.replace(MAL, BIEN, 1))
print("Dos celdas de tabla, limpias")

# 2. La señal.
SENAL = """
## S-048 · Se citó cuatro veces una historia como «abierta» sin leer su estado, y estaba cerrada  ·  error-resuelto · activa
- **What:** cuatro fases seguidas declararon no llevar especificación aparte, y las cuatro lo justificaron diciendo que la [EP-001 · HU-010](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) **estaba abierta esperando escribir esa regla**. Sobre esa base se levantó un hallazgo entero, `H-34`, que decía «cuatro ya no es un caso suelto: es la regla que falta». **Era falso.** Esa historia dice `Estado: Done`, cerró el 2026-08-18 con su commit, y su pendiente está en `pendientes/hecho/`.
- **Why:** peor todavía, cerró **diciendo justamente lo contrario**: «nada nuevo, y ese es el resultado». La regla ya existía dos reglas más abajo en el mismo capítulo — [`02·F19`](../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), *«la redacción del CA es la especificación funcional»*—, y en su momento se intentó agregar otra que decía lo mismo y **chocaba con `02·F0`**. Se citó como pendiente algo que ya se había resuelto, y se propuso rehacer un trabajo que además se había descartado con razón.
- **Also:** el error se cometió una vez y se **copió** tres. Cada fase nueva tomó la redacción de la anterior sin volver a la fuente, y **la repetición hizo la afirmación más creíble**, no menos: para la cuarta, «es la regla que falta» se leía como un hecho establecido por acumulación. Lo que se leyó de la historia fue su **narrativa**, que describe el problema en presente porque se escribió antes de resolverlo. Nadie miró el campo `Estado`, que está en la primera tabla.
- **Where:** los cinco documentos corregidos, cada uno diciendo qué afirmaba y por qué era falso · el hallazgo `H-34` del resumen, reescrito.
- **Learned:** **el estado de un documento se lee en su campo de estado, no en su narrativa.** Una historia sin resolver y una resuelta se leen igual en el cuerpo: las dos describen el problema en presente. Y hay una comprobación barata que habría bastado: si la historia dice que falta una regla, **buscar la regla**. Estaba a un `grep` del capítulo que la historia misma nombraba.
- **When/Who:** 2026-08-26 · agente, al ir a construir lo que creía pendiente.
- **Scope:** estándar; aplica a toda cita de un documento como pendiente o abierto.
- **Rel:** S-026 (marcar como siguiente una fase que no lo era) — el mismo error de leer el cuerpo y no el estado.
"""

t = io.open("documentacion/senales.md", encoding="utf-8").read()
io.open("documentacion/senales.md", "w", encoding="utf-8",
        newline="\n").write(t + SENAL)
print("S-048 escrita")

# 3. H-34, reescrito entero.
ruta = "historico-chat/resumenes/2026-08-22/sesion-6.md"
t = io.open(ruta, encoding="utf-8").read()

VIEJO_H34 = """### H-34 · Cuatro fases seguidas declararon no llevar especificación, y la regla sigue sin escribirse

- **Qué pasó:** cada una de las cuatro fases de esta sesión declaró que no lleva especificación aparte, porque su historia ya trae alcance, reglas, criterios con pasos y requisitos no funcionales. Las cuatro lo dijeron por escrito, con su porqué.
- **Por qué importa:** la [EP-001 · HU-010](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) existe desde antes y dice exactamente esto: **«una regla que se incumple dos veces seguidas con buenos motivos se vuelve costumbre incumplirla, y la próxima vez nadie va a saber si el caso era legítimo o si se saltó el paso»**. Van cuatro.
- **Qué lo soluciona:** nada todavía. Declararlo cada vez evita el incumplimiento silencioso, pero no escribe la regla.
- **Qué se decidió:** dejarlo dicho en las cuatro fases como evidencia de esa historia, en vez de callarlo.
- **Estado:** abierto.
- **Responde a:** —
- **Dispara:** construir la `EP-001 · HU-010`, que ya está escrita y sin fase.
- **Orden de resolución:** cuando el usuario lo decida. Ya hay cuatro casos reales de los que sacar la regla, que es más de lo que había cuando se escribió la historia.
- **Dónde queda:** el §0 del plan de trabajo de las cuatro fases, y su `estado-fase.md`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** —
- **Con qué se retoma:** bajar la `HU-010` a fase, con los cuatro casos como insumo."""

NUEVO_H34 = """### H-34 · Se citó cuatro veces una historia como «abierta» sin leer su estado, y estaba cerrada

> **Este hallazgo decía otra cosa hasta el 2026-08-26**, y lo que decía era falso. Se deja reescrito, no borrado: el error importa más que la conclusión que traía.

- **Qué pasó:** cuatro fases seguidas declararon no llevar especificación aparte, y las cuatro lo justificaron diciendo que la [EP-001 · HU-010](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) **estaba abierta esperando escribir esa regla**. Sobre eso se levantó este hallazgo, que concluía «cuatro ya no es un caso suelto: es la regla que falta». **Esa historia dice `Estado: Done`**, cerró el 2026-08-18, y su pendiente está en `hecho/`.
- **Por qué importa:** cerró **diciendo lo contrario**: «nada nuevo, y ese es el resultado». La regla ya existía dos reglas más abajo en el mismo capítulo, [`02·F19`](../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md): *«la redacción del CA es la especificación funcional»*. Y en su momento se intentó agregar otra que decía lo mismo y **chocaba con `02·F0`**. Se iba a rehacer un trabajo ya hecho **y descartado con razón**.
- **Qué lo soluciona:** se corrigieron los cinco documentos, cada uno diciendo qué afirmaba y por qué era falso.
- **Qué se decidió:** citar `02·F19`, que es la regla de verdad. Y no borrar lo que se dijo mal: queda tachado y explicado, porque el error enseña más que la conclusión.
- **Cómo se cometió, que es lo que vale:** se leyó la **narrativa** de la historia, que describe el problema en presente porque se escribió antes de resolverlo. **Nadie miró el campo `Estado`, que está en su primera tabla.** Y el error se cometió una vez y se **copió tres**: cada fase tomó la redacción de la anterior sin volver a la fuente, y la repetición lo hizo parecer más establecido, no menos.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** los cinco documentos corregidos y la señal `S-048`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —"""

assert t.count(VIEJO_H34) == 1, "H-34 no coincide"
t = t.replace(VIEJO_H34, NUEVO_H34, 1)

viejo_cierre = ("Quedan dos abiertos y **ninguno tiene pendiente creado**: "
                "`H-28` —el tope de ruta en Windows— y `H-34` —cuatro fases "
                "declarando la misma excepción que sigue sin ser regla—. En "
                "los dos falta lo mismo: una decisión del usuario que es la "
                "que dice qué pendiente escribir.")
nuevo_cierre = ("**`H-34` también cerró, y cerró corrigiéndose**: la regla que "
                "decía faltar existía desde antes. Queda **uno** abierto y sin "
                "pendiente creado: `H-28`, el tope de ruta en Windows. Falta "
                "una decisión del usuario, que es la que dice qué pendiente "
                "escribir.")
assert t.count(viejo_cierre) == 1, "cierre no coincide"
t = t.replace(viejo_cierre, nuevo_cierre, 1)
t = t.replace("☐ · faltan los de `H-28` y `H-34` |",
              "☐ · falta el de `H-28` |", 1)

io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)
print("H-34 reescrito y el cierre al día")
