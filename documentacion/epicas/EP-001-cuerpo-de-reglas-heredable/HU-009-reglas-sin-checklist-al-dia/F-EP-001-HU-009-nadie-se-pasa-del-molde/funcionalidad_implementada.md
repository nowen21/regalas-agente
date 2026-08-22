# Funcionalidad implementada — Fase F-EP-001-HU-009-nadie-se-pasa-del-molde

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive. El plan está en [plan_trabajo.md](plan_trabajo.md); lo que se probó, en [resultado_pruebas.md](resultado_pruebas.md).

> **Cerrada el 2026-08-22, con el estándar en la versión 30.9.1.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Ninguna regla del estándar está publicada reprobando su propio checklist.** Ni por lo que exige ni por su largo. Era la deuda que la HU-009 nombra desde que nació.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| Las 27 reglas en NO CUMPLE pasan a CUMPLE | doc | `base/`, capítulos 01, 02, 04, 08, 10, 18, 19, 20 | ✅ | v30.8.0 · `metareglas` de 27 fallas a 0 |
| Ninguna regla pasa de 320 caracteres | doc | `base/`, capítulos 00, 01, 02, 03, 13, 20 | ✅ | v30.8.1 a v30.9.1 · sin avisos de largo |
| El texto que no cabe se conserva entero | doc | tres anexos de capítulo | ✅ | [nomenclatura-de-fases.md](../../../../../base/02-flujo-de-trabajo/nomenclatura-de-fases.md), [tabla-de-trazabilidad.md](../../../../../base/13-documentacion/tabla-de-trazabilidad.md), [desempate.md](../../../../../base/20-meta-reglas/desempate.md) |
| Los porqués recortados no se pierden | doc | `notas/` | ✅ | [porques-recortados-al-molde.md](../../../../../notas/porques-recortados-al-molde.md), 34 filas |
| Las 26 candidatas a partirse quedan resueltas | doc | `base/` | ✅ | 23 partidas desde el 2026-08-18, `EST2` y `PR3` resueltas sin partirse, `I3` decidida por el usuario |
| Cada cambio versionado y registrado | doc | `CHANGELOG.md`, `VERSION` | ✅ | seis entradas, de la 30.8.0 a la 30.9.1 |
| Lo aprendido queda como señal | doc | `documentacion/senales.md` | ✅ | S-020 |
| La cadena queda cerrada hacia arriba | doc | esta carpeta | parcial | la fase se escribió **después** de ejecutar; ver §3 |

## 2. Lo que cambió para un proyecto que hereda

**Nada que hacer.** Ninguna exigencia cambió: las mismas reglas piden lo mismo, dicho más corto. Un proyecto al día sube la versión declarada y sigue.

**Lo que sí cambia es cómo se cita.** Los sub-identificadores `F12.1` a `F12.13` dejaron de ser identificadores de regla y pasaron a ser puntos del anexo de nomenclatura: quien los citaba escribe ahora `02·F12` y el punto. Es la única consecuencia visible, y quedó anotada en la entrada de la 30.8.0.

## 3. Lo que queda abierto, dicho sin adornos

**La fase se escribió después de ejecutar.** [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) pide bajar el pendiente a fase antes de construir, y acá el trabajo salió de una orden directa del usuario, capítulo por capítulo, sin carpeta de fase. Lo publicado está probado y aprobado, pero el orden fue el inverso, y esta carpeta lo dice en vez de disimularlo.

**Qué se hizo con eso:** se levantó la fase con su plan, sus pruebas y este cierre, declarando como línea base lo ya publicado, que es el mismo patrón de la señal [S-018](../../../../../documentacion/senales.md). Lo que no se puede arreglar hacia atrás es el orden.

## 4. Lo que esta fase deja para la siguiente

- **Las 21 fases de retrodocumentación** de los capítulos `02` a `22` (HU-015 a HU-035), que dirán de dónde baja cada regla.
- **El pendiente 33 y el 59**, que esperan datos que solo tiene el usuario.
