# -*- coding: utf-8 -*-
"""Cierra H-31 y escribe H-32, H-33 y H-34."""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")
ruta = "historico-chat/resumenes/2026-08-22/sesion-6.md"
t = io.open(ruta, encoding="utf-8").read()

CIERRE_31 = [
 ("- **Qué lo soluciona:** nada todavía, **y a propósito**. El plan de la fase "
  "no declara ese archivo, y `02·F8` prohíbe editar lo que el plan no declara. "
  "Además, cambiar `plantillas/` suma entrada en el `CHANGELOG` y sube "
  "`VERSION` (`20·M10`).",
  "- **Qué lo soluciona:** se resolvió acá, por la cadena: `HU-020` y su fase "
  "`A`. La plantilla remite al comando en vez de pedir la cuenta, y el "
  "estándar subió a `34.2.0`. **Y apareció una segunda mitad que nadie había "
  "declarado:** la comprobación que impedía que la copia volviera miraba "
  "`pendientes/48-inventario-hu.md` escrito fijo, así que en un proyecto no "
  "veía nada. La guardia protegía al estándar y a nadie más."),
 ("- **Qué se decidió:** reportarlo en vez de tocarlo de paso. Es exactamente "
  "lo que la regla pide cuando aparece un archivo nuevo a mitad de una fase: "
  "pausar y decir, no editar por iniciativa.",
  "- **Qué se decidió:** reportarlo en vez de tocarlo de paso, y bajarlo por "
  "la cadena. La segunda mitad no se descubrió leyendo: salió de preguntarse, "
  "al abrir la historia, **si un proyecto podía siquiera correr el comando**. "
  "La pregunta era sobre otra cosa."),
 ("- **Estado:** abierto.\n- **Responde a:** —\n- **Dispara:** por decidir con "
  "el usuario.\n- **Orden de resolución:** después de esta fase, que es la que "
  "muestra cómo queda un inventario que no se mantiene a mano.\n- **Dónde "
  "queda:** el cierre de la fase §6, y el `estado-fase.md` §3.",
  "- **Estado:** resuelto acá.\n- **Responde a:** "
  "[EP-004](../../../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) "
  "· HU-020.\n- **Dispara:** —\n- **Orden de resolución:** —\n- **Dónde "
  "queda:** [plantillas/inventario-hu.md](../../../plantillas/inventario-hu.md) "
  "reescrita, `CARPETAS_DEL_INVENTARIO` en "
  "[validadores/fases.py](../../../validadores/fases.py), y la señal `S-045`."),
 ("- **Cerrado en:** —\n- **Con qué se retoma:** decidir si la plantilla se "
  "pone al día, sabiendo que es cambio de `plantillas/` y sube la versión del "
  "estándar.",
  "- **Cerrado en:** 2026-08-22 · sesion-6\n- **Con qué se retoma:** —"),
]

for viejo, nuevo in CIERRE_31:
    assert t.count(viejo) == 1, "H-31: no coincide -> %s" % viejo[:45]
    t = t.replace(viejo, nuevo, 1)

NUEVOS = """### H-32 · El mismo defecto tiene dos formas, y una sola expresión no caza las dos

- **Qué pasó:** la comprobación busca el rótulo de la cuenta **con un número al lado**, porque en un inventario de verdad el defecto es un número escrito. Un sabotaje devolvió el campo a la **plantilla** y la suite quedó en verde: ahí el mismo defecto viene como `«N»`, el hueco por llenar. Sin número, no había coincidencia.
- **Por qué importa:** era invisible **justo en el archivo donde más caro sale**. La plantilla es la que se copia, así que un defecto ahí se multiplica por cada proyecto que la use.
- **Qué lo soluciona:** se resolvió acá, con una prueba que en la plantilla busca **el rótulo como campo, valga lo que valga**.
- **Qué se decidió:** **no** aflojar la expresión. Que el inventario de verdad exija un número es correcto: su narrativa tiene cifras y marcarlas volvería el aviso ruido. Son dos comprobaciones con dos formas, no una mal escrita.
- **Estado:** resuelto acá.
- **Responde a:** [EP-004](../../../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) · HU-020.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `test_la_plantilla_no_trae_campos_de_cuenta` y la señal `S-046`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-33 · «No dupliques lo derivable» no aplica a un hecho histórico

- **Qué pasó:** al cerrar la fase anterior se escribió, en «Versión del estándar al cerrar», **«la que declara `VERSION`»** en vez del número. Al subir `VERSION` a `34.2.0` una hora después, ese cierre pasó a afirmar que cerró bajo una versión **que no existía cuando cerró**.
- **Por qué importa:** es el error **inverso** al que se acababa de arreglar, cometido por aplicar bien la regla en el sitio equivocado. La cuenta de historias es derivable y el puntero la mejora; **la versión al cerrar es una foto**, y el puntero la falsifica el día que la fuente cambia.
- **Qué lo soluciona:** nada todavía. **No se corrigió porque el plan de la fase no declara ese archivo** (`02·F8`).
- **Qué se decidió:** reportarlo y dejarlo a decisión del usuario. Es una línea, y aun así la regla es la regla.
- **Estado:** abierto.
- **Responde a:** —
- **Dispara:** por decidir con el usuario: una línea en el cierre de la fase `A-EP-004-HU-019`.
- **Orden de resolución:** cuanto antes — mientras no se corrija, el repositorio afirma algo falso.
- **Dónde queda:** el cierre de la `HU-020` §6, y la señal `S-047`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** —
- **Con qué se retoma:** autorizar que se toque ese archivo, que es lo único que falta.

---

### H-34 · Cuatro fases seguidas declararon no llevar especificación, y la regla sigue sin escribirse

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
- **Con qué se retoma:** bajar la `HU-010` a fase, con los cuatro casos como insumo.

---

"""

ancla = "## ¿Se puede cerrar la sesión?"
assert t.count(ancla) == 1
t = t.replace(ancla, NUEVOS + ancla, 1)

viejo_cierre = ("`H-27` **cerró**: el inventario dejó de mantenerse a mano, por "
                "la cadena completa hasta la fase `A` de la `HU-019`. Quedan "
                "dos abiertos y **ninguno tiene pendiente creado**: `H-28` —el "
                "tope de ruta para quien clone en Windows— y `H-31` —la "
                "plantilla del inventario, que sigue enseñando lo que el "
                "estándar acaba de quitarse—. En los dos falta lo mismo: una "
                "decisión del usuario que es la que dice qué pendiente "
                "escribir.")
nuevo_cierre = ("**`H-27` y `H-31` cerraron**, los dos por la cadena completa: "
                "el inventario dejó de mantenerse a mano, adentro y en lo que "
                "el estándar reparte. Quedan tres abiertos y **ninguno tiene "
                "pendiente creado**: `H-28` —el tope de ruta en Windows—, "
                "`H-33` —una línea que afirma algo falso y que no se tocó "
                "porque el plan no la declaraba— y `H-34` —cuatro fases "
                "declarando la misma excepción que sigue sin ser regla—. En "
                "los tres falta lo mismo: una decisión del usuario que es la "
                "que dice qué pendiente escribir.")
assert t.count(viejo_cierre) == 1, "cierre no coincide"
t = t.replace(viejo_cierre, nuevo_cierre, 1)
t = t.replace("☐ · faltan los de `H-28` y `H-31` |",
              "☐ · faltan los de `H-28`, `H-33` y `H-34` |", 1)

io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)
print("H-32, H-33 y H-34 escritos. H-31 cerrado.")
