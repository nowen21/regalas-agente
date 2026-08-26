# Resultado de pruebas — Fase A-EP-003-HU-009-modelo-del-resumen-de-sesion

**Para qué sirve este documento.** Dice **qué se ejecutó y cuánto dio**. El plan de pruebas no se toca al correrlo: la línea base aprobada se queda como está y lo que pasó se escribe acá. Sin este documento, una exigencia no se puede dar por cumplida.

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-009-modelo-del-resumen-de-sesion` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-003-HU-009 v1.0 |
| **Fecha de ejecución** | 2026-08-14 |
| **Ejecutado por** | El agente, con el usuario aprobando el plan y su ampliación |

---

## 1. Línea base antes de ejecutar

| Medida | Valor de partida |
|---|---|
| Resúmenes escritos con el modelo | 2, los dos del 2026-08-14 |
| Hallazgos anotados entre los dos | 16 |
| Campos por hallazgo en el modelo | 12, más «viene de» a nivel de sesión |
| Enlaces al resumen desde el índice del histórico | 0 |
| Qué dice el modelo sobre un hallazgo heredado | Nada |

---

## 2. Casos ejecutados

| Caso | Exigencia | Con qué se probó | Veredicto | Evidencia |
|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-resumen-y-la-transcripción-responden-preguntas-distintas) | [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) | El resumen `hu-de-la-comprobacion-automatica.md` contra su transcripción de 1.400 líneas | Cumple | La tabla "cuál de los dos abrir" del índice de resúmenes |
| [CP-002](plan_pruebas.md#cp-002--un-hallazgo-abierto-se-retoma-sin-preguntarle-a-nadie) | [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) · [RNF-02](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Los 9 hallazgos abiertos de los dos resúmenes, leídos sin abrir sus transcripciones | Cumple | Cada uno con su pregunta viva |
| [CP-003](plan_pruebas.md#cp-003--un-hallazgo-que-se-arrastra-se-puede-seguir) | [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) | El `H-4` del 2026-08-14, que nació en `hu-de-la-comprobacion-automatica` y lo trabajó `h4-cerrar-…` | Cumple | Seguido en las dos direcciones, sin copias |
| [CP-004](plan_pruebas.md#cp-004--la-sección-de-cierre-dice-qué-falta) | [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) | Las secciones de cierre de los dos resúmenes del 2026-08-14 | Cumple | Las dos dicen qué falta, casilla por casilla |
| [CP-005](plan_pruebas.md#cp-005--el-resumen-se-lee-de-una-vez) | [RNF-01](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | El resumen más largo: 198 líneas y 2.426 palabras, con 9 hallazgos | Cumple | Se lee de corrido, unos 10 minutos |
| [CP-006](plan_pruebas.md#cp-006--los-dos-resúmenes-traen-los-mismos-campos) | [RNF-03](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Los dos resúmenes del 2026-08-14, campo por campo, contra `plantillas/sesion.md` | Cumple | Los 12 campos, idénticos en los dos |

**Detalle de CP-001.** El resumen responde qué quedó abierto y por dónde se sigue; la transcripción responde qué se dijo y en qué orden. Se comprobó buscando en el resumen una frase textual del usuario: no está, y no tiene por qué estar. Ninguno de los dos resúmenes copia diálogo.

**Detalle de CP-002.** Se tomaron los 9 hallazgos abiertos de los dos resúmenes y se leyeron sin abrir sus transcripciones. En los 9 se entendió qué falta y por dónde arrancar; todos nombran las historias que disparan, y esas historias existen o están declaradas como faltantes; y todos traen una pregunta concreta en «con qué se retoma», no un "seguir con el tema".

**Detalle de CP-003.** El H-4 nació el 2026-08-14 en la sesión `hu-de-la-comprobacion-automatica` y lo trabajó `h4-cerrar-h-4-…`. Desde el resumen que lo trabajó, su «viene de» nombra el original con fecha, tema y número; desde el original, su «nace en» sigue siendo la sesión donde apareció. No hay dos copias del hallazgo: lo que se decidió se escribió en un solo sitio.

**Detalle de CP-004.** Se abrió la sección de cierre de los dos resúmenes. El de esta sesión decía "todavía no" con tres casillas sin marcar, y cada una nombra el trabajo concreto que la marcaría: el pendiente de H-1, la historia que dispara, y el commit. El otro, lo mismo con cuatro.

**Detalle de CP-005.** El resumen más largo tiene 198 líneas y 2.426 palabras, con 9 hallazgos: unos 10 minutos de lectura contra las 1.400 líneas de su transcripción. Se lee de una vez.

**Detalle de CP-006.** Los dos resúmenes usan exactamente los mismos 12 campos por hallazgo, sin faltar ni sobrar ninguno. Las dos apariciones de `«…»` que encontró el paso 3 están dentro de comillas de código, citando la marca como tema del hallazgo; no son huecos sin llenar ([`13·DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)).

---

## 3. Defectos encontrados

| ID | Título | Caso | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El resumen `hu-de-la-comprobacion-automatica.md` no tiene el campo «viene de»: se escribió antes de que ese campo existiera | [CP-006](plan_pruebas.md#cp-006--los-dos-resúmenes-traen-los-mismos-campos) | Baja | Abierto y fuera de alcance: el plan declara que los resúmenes ya escritos no se rehacen |

DEF-01 no toca ninguna exigencia: el campo es de sesión, no de hallazgo, y la uniformidad que pide `RNF-03` es la de los campos del hallazgo. Queda anotado porque el próximo resumen que se escriba sí lo lleva, y la diferencia se va a ver.

---

## 4. Métricas

| Métrica | Meta | Obtenido |
|---|---|---|
| Cobertura de exigencias | 100% | 100%: 6 de 6 con caso ejecutado |
| Hallazgos abiertos retomables sin la transcripción | 100% | 100%: los 9 abiertos de los dos resúmenes |
| Campos del modelo que ningún resumen usa | 0 | 0 |
| Fallas nuevas en la corrida del estándar | 0 | 0 |
| Líneas del índice del histórico que el programa sigue reconociendo | 35 de 35 | 35 de 35 |

---

## 5. Verificación por exigencia

| Exigencia | Veredicto | De dónde sale |
|---|---|---|
| [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) · el modelo se distingue de la transcripción | **Cumple** | CP-001 |
| [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) · un hallazgo dice si está cerrado y por dónde sigue | **Cumple** | CP-002 y CP-003 |
| [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) · dice si la sesión se puede cerrar | **Cumple** | CP-004 |
| [RNF-01](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) · se lee de una vez | **Cumple** | CP-005 |
| [RNF-02](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) · se entiende sin la transcripción | **Cumple** | CP-002 |
| [RNF-03](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) · todos traen los mismos campos | **Cumple** | CP-006 |

---

## 6. Concepto final

**Cumple.** Las seis exigencias quedaron verificadas, con un defecto abierto (DEF-01) que el propio plan había declarado fuera de alcance.

Lo que falta para cerrar la fase no es prueba: es el commit.
