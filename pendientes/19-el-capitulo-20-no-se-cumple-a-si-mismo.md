# Pendiente · El capítulo de meta-reglas no se cumple a sí mismo

**Estado:** abierto, con una de sus tres deudas cerrada · anotado 2026-08-14 · nace del hallazgo H-6 de [2026-08-14](../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

## El problema

El validador de meta-reglas midió por primera vez el propio cuerpo de reglas. De **188 reglas**:

| Qué | Cuántas |
|---|---|
| Sin bloque de checklist | 129 |
| Publicadas con el checklist en "no cumple" | 7 |
| Sin clasificar en `reglas-validables.md` | 33 |

Las siete en "no cumple" son `F4`, `F5`, `F12`, `M2`, `M4`, `M7` y `M8`. `M14` dice que sin CUMPLE una regla no se publica, y están publicadas.

Las 33 sin clasificar incluyen los capítulos `18` y `19` completos, que ese archivo no menciona.

## Qué falta

**1. Decidir qué se hace con las siete.** Tres caminos: corregirlas, derogarlas, o aceptar que el checklist no aplica hacia atrás y dejarlo escrito.

**2. Clasificar las 33.** ✅ **Hecho el 2026-08-16** (v23.1.1), en la fase [`A-EP-001-HU-009`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/). Bajaron a cero.

**Y cambió el diagnóstico:** quince de las 33 **ya estaban clasificadas**. El registro decía `C1–C17`, un rango, y el programa busca cada identificador literal. Las que faltaban de verdad eran 18 — los capítulos `18` y `19` completos, más `G9`, `M15`, `F4` y `F12`.

**3. Las 121 sin bloque** (eran 129 cuando se anotó). Aplicarles el checklist es trabajo largo y con criterio. Conviene por capítulo, no de a una.

## El límite

El validador dice cuáles faltan, no si la regla está bien escrita. Eso lo decide quien la lee.
