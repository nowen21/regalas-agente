# Lo que dejó la sesión — las HU sin su fase

**Viene de:** —, es trabajo nuevo.

---

## Hallazgos de esta sesión

### H-1 · 52 de las 66 HU no tienen su fase completa

- **Qué pasó:** se contaron las 66 HU de `documentacion/epicas/` contra lo que exige [`02·F12.2`](../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md): **49 no tienen ninguna carpeta de fase**, 3 la tienen a medias y 14 están completas.
- **Por qué importa:** la mayoría de esas HU **ya están construidas** —memoria, versionado, validadores, enganches, todos cerrados en `pendientes/hecho/`— y sus §8 siguen diciendo «todavía no se descompuso en fases». El documento afirma algo falso sobre código que corre, y ningún CA tiene dónde estar marcado: nadie puede decir qué quedó cumplido.
- **Qué lo soluciona:**
  **EP-004 · HU nueva — Decir cuántas HU quedan sin su fase completa**
  - **Como** quien mantiene el estándar
  - **Quiero** que la corrida de fases termine diciendo cuántas HU hay, cuántas completas y cuántas incompletas
  - **Para** responder «cuánto falta» leyendo una línea, en vez de contar los avisos a mano
  - **Contexto:** `validar.py fases` **ya lista** la HU sin fase (`F12.2`) y el documento que le falta a cada fase (`F12.13`) — 54 avisos hoy. Lo que no da es el total, y por eso la cuenta de esta sesión se escribió en un script aparte que no quedó en el repositorio.

  **Se creyó al revés y se comprobó tarde.** Durante la sesión se dio por hecho que el validador no veía nada de esto, y se corrió antes de dejar la HU escrita: veía casi todo. La HU nació pidiendo lo que ya existía y hubo que recortarla el mismo día.
- **Qué se decidió:** un solo pendiente con la tabla completa, no uno por HU ni uno por épica. Columnas: HU, fase y los cinco documentos, con casilla ☐/☑ por cada uno. Y que esa forma quede como molde reusable, no como un archivo suelto de esta casa: nace [`plantillas/inventario-hu.md`](../../../plantillas/inventario-hu.md) en la **v23.2.0**.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** 1. EP-004 · HU nueva — el revisor cuenta las HU sin fase. No bloquea al pendiente 48: lo que hace es que la cuenta no se vuelva a perder.
- **Orden de resolución:** 1 de 2 · es el trabajo de la sesión.
- **Dónde queda:** pendiente [48](../../../pendientes/48-inventario-hu.md) · plantilla [`inventario-hu.md`](../../../plantillas/inventario-hu.md) (v23.2.0)
- **Nace en:** 2026-08-16 · las HU sin su fase
- **Cerrado en:** —
- **Con qué se retoma:** ¿por cuál fila se empieza, y se abre una fase por HU o una que cubra varias de la misma épica?

### H-2 · Dos sesiones tocaron el mismo backlog al mismo tiempo

- **Qué pasó:** mientras se levantaba la tabla, otra sesión creó dos carpetas de fase (`A-EP-001-HU-009`, `A-EP-004-HU-014`), completó documentos de una de ellas y tomó el número **52** de `pendientes/`. La cuenta cambió dos veces en la misma sesión: primero 51 HU sin fase, después 49.
- **Por qué importa:** es el mismo defecto del pendiente [22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) —dos sesiones versionando a la vez— pero sobre la numeración de `pendientes/`, no sobre `VERSION`. Dos sesiones pueden escribir el mismo número y ninguna se entera; acá se vio solo porque el archivo ya estaba ahí al ir a crearlo.
- **Qué lo soluciona:**
  **EP-004 · HU nueva — Nadie toma un número de pendiente que ya exista**
  - **Como** quien abre un pendiente
  - **Quiero** que el número se asigne mirando la carpeta, y que avise si otro lo tomó
  - **Para** que dos sesiones abiertas no escriban dos pendientes distintos con el mismo número
  - **Contexto:** hoy el número se elige a ojo leyendo el README, que puede estar desactualizado respecto de la carpeta. El [22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) ya tiene el problema planteado para `VERSION` y tres opciones sobre la mesa; esto es la misma pregunta un piso más abajo.
- **Qué se decidió:** sin decidir. Acá se resolvió a mano: se listó la carpeta antes de escribir y se tomó el 48, que estaba libre.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** 1. EP-004 · HU nueva — nadie toma un número de pendiente que ya exista. Va después de decidir el [22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md), que es la misma decisión sobre `VERSION`.
- **Orden de resolución:** 2 de 2 · no bloquea nada hoy, y su decisión de fondo está en el 22.
- **Dónde queda:** anotado acá; se suma al pendiente [22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) cuando se retome.
- **Nace en:** 2026-08-16 · las HU sin su fase
- **Cerrado en:** —
- **Con qué se retoma:** ¿el número de pendiente lo asigna una herramienta, o basta con listar la carpeta antes de escribir?

### H-3 · Renombrar la sesión rompió dos enlaces de fuera

- **Qué pasó:** al renombrar la sesión con `historico.py --renombrar`, el resumen pasó de `sesion-8.md` a `las-hu-sin-su-fase.md`. Los dos `README` de las HU nuevas lo citaban por el nombre viejo, y quedaron rotos. El revisor pasó de 3 fallas a 5 en la misma corrida.
- **Por qué importa:** es el punto 4 del pendiente [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) —renombrar deja rotos los enlaces de fuera— y no es teoría: pasó a los diez minutos de que el mismo comando dejara «índice al día». El [35](../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md) cerró el enlace de **adentro** del resumen; los de afuera siguen a cargo de quien se acuerde.
- **Qué lo soluciona:** ya está escrito en el punto 4 del 33, y `citas.py` tiene el modo que repara. No hace falta historia nueva: hace falta que `--renombrar` lo llame.
- **Qué se decidió:** arreglar los dos a mano y dejar el caso anotado como evidencia del 33. No se abre pendiente nuevo: sería el tercero sobre lo mismo.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** pendiente [33 · punto 4](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md)
- **Nace en:** 2026-08-16 · las HU sin su fase
- **Cerrado en:** 2026-08-16 · las HU sin su fase
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ |
| Toda historia disparada está escrita en su épica | ☑ |
| Lo que se hizo está aprobado y guardado | ☑ commits `333c3a1` y `3b51065` |

**Cerrada.** Dos commits: `333c3a1` con los 12 archivos del trabajo y `3b51065` con el renombrado y los dos enlaces que rompió. En los dos, nada de la otra sesión: los cinco borrados que ya estaban en el índice se sacaron, y de `CHANGELOG.md`, del índice de pendientes y del índice del día se tomó solo la parte propia.

**Lo que había antes:** Las dos historias quedaron escritas en EP-004 —[HU-017](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) y [HU-018](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md)—, con su línea en la épica, su lugar en la hoja de ruta como fase 9 y su fila en el inventario. Lo único que queda es la aprobación y el commit, que son del usuario.

Los dos hallazgos siguen **abiertos**, y eso está bien: lo que cierra la sesión es que quedaran anotados con su archivo, no que se resolvieran. Se retoman por el pendiente [48](../../../pendientes/48-inventario-hu.md) y por el [22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md).

<!-- aviso: falta decir si la sesión se puede cerrar -->
