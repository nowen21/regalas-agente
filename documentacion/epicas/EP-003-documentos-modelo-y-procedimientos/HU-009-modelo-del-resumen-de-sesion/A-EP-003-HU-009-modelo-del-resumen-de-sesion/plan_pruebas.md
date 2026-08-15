# Plan de Pruebas — Fase A-EP-003-HU-009-modelo-del-resumen-de-sesion

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ninguna exigencia quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el [resultado_pruebas.md](resultado_pruebas.md) de esta misma fase. La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-009 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-009-modelo-del-resumen-de-sesion` |
| **Fecha** | 2026-08-14 |
| **Elaborado por** | Ing. José Dúmar Jiménez Ruíz |
| **Estado** | Borrador |

> **Proporcionalidad.** Una sola fase de una HU pequeña: se llenan las secciones 3, 5, 6, 9 y 12, como manda la plantilla.

---

## 3. Estrategia de pruebas

El entregable es un modelo de documento. La prueba no es una suite: es **usar el modelo y ver si responde**. Los dos resúmenes reales del 2026-08-14 son el banco de pruebas, y la comprobación más dura es la de autonomía, que exige leer un hallazgo sin abrir la transcripción de donde salió.

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Lectura | Que el resumen responda sin la transcripción | El repositorio | No |
| Comparación | Que los dos resúmenes traigan los mismos campos | El repositorio | Parcial: `grep` lista los campos, la persona compara |
| Regresión | Que la corrida del estándar siga en verde | El repositorio | Sí |

**Tipos que aplican:** funcional (los tres CA) y usabilidad (brevedad y autonomía). No aplican seguridad, rendimiento, migración de datos ni recuperación.

**Alcance de la corrida automatizada ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):** solo `python validadores/validar.py estandar`.

---

## 5. Matriz de trazabilidad

> Ninguna exigencia puede quedar sin al menos un caso de prueba. Los `RNF-0N` llevan su fila propia.
>
> Cada `CP-00N` enlaza a su caso de §6, y cada `CA-0N` o `RNF-0N` a su exigencia en la HU.

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) | [CP-001](#cp-001--el-resumen-y-la-transcripción-responden-preguntas-distintas) | Funcional | Crítica | No | ☐ |
| HU-009 | [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) | [CP-002](#cp-002--un-hallazgo-abierto-se-retoma-sin-preguntarle-a-nadie), [CP-003](#cp-003--un-hallazgo-que-se-arrastra-se-puede-seguir) | Funcional | Crítica | No | ☐ |
| HU-009 | [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) | [CP-004](#cp-004--la-sección-de-cierre-dice-qué-falta) | Funcional | Alta | No | ☐ |
| HU-009 | [RNF-01](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | [CP-005](#cp-005--el-resumen-se-lee-de-una-vez) | Usabilidad | Media | No | ☐ |
| HU-009 | [RNF-02](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | [CP-002](#cp-002--un-hallazgo-abierto-se-retoma-sin-preguntarle-a-nadie) | Usabilidad | Alta | No | ☐ |
| HU-009 | [RNF-03](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | [CP-006](#cp-006--los-dos-resúmenes-traen-los-mismos-campos) | Funcional | Media | Parcial | ☐ |

**Cobertura:** 6 de 6 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

### CP-001 — El resumen y la transcripción responden preguntas distintas

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | El índice de la carpeta de resúmenes escrito (T-01) |
| **Datos de entrada** | El resumen `hu-de-la-comprobacion-automatica.md` y su transcripción |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el resumen qué quedó abierto | Se responde sin abrir la transcripción |
| 2 | Buscar en el resumen qué se dijo textualmente en un momento dado | No está: para eso es la transcripción |
| 3 | Revisar si el resumen copia diálogo | No copia ninguno |

**Resultado esperado final:** cada documento responde lo suyo y ninguno hace el trabajo del otro.

### CP-002 — Un hallazgo abierto se retoma sin preguntarle a nadie

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) y [RNF-02](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | T-04 y T-05 hechas |
| **Datos de entrada** | Un hallazgo abierto real, sin abrir su transcripción |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el hallazgo completo, sin abrir la transcripción | Se entiende qué falta y por dónde arrancar |
| 2 | Mirar qué historias dispara | Las nombra, y esas historias existen o están declaradas como faltantes |
| 3 | Mirar con qué pregunta se retoma | Hay una pregunta concreta, no un "seguir trabajando en el tema" |

**Resultado esperado final:** se puede empezar a trabajar sin preguntarle a quien estuvo en esa sesión.

### CP-003 — Un hallazgo que se arrastra se puede seguir

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) |
| **Tipo** | Funcional — el caso que ya pasó de verdad |
| **Prioridad** | Crítica |
| **Precondiciones** | T-04 y T-05 hechas |
| **Datos de entrada** | El H-4 del 2026-08-14, que nació en una sesión y lo trabajó otra |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Partir del resumen de la sesión que lo trabajó | Su «viene de» nombra el hallazgo original con fecha, tema y número |
| 2 | Ir al hallazgo original | Su «nace en» sigue diciendo la sesión donde apareció, no la que lo heredó |
| 3 | Buscar dónde quedó escrito lo que se hizo | Está en un solo sitio: no hay dos copias del hallazgo diciendo cosas distintas |

**Resultado esperado final:** un hallazgo que cruza tres sesiones se sigue en las dos direcciones.

### CP-004 — La sección de cierre dice qué falta

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | T-08 hecha |
| **Datos de entrada** | Los dos resúmenes del 2026-08-14 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la sección de cierre de un resumen con hallazgos abiertos | Dice que todavía no se puede cerrar, y qué falta |
| 2 | Mirar cada casilla sin marcar | Dice cuál es el trabajo concreto que la marcaría |

### CP-005 — El resumen se lee de una vez

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [RNF-01](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) |
| **Tipo** | Usabilidad |
| **Prioridad** | Media |
| **Datos de entrada** | El resumen más largo que exista |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leerlo entero de corrido, cronometrando | Se termina sin abandonar a la mitad |
| 2 | Contar cuántos hallazgos trae y cuánto ocupa cada uno | Ninguno se lleva más de lo que aporta |

> Si acá falla, lo que se corrige es el modelo, no el resumen: es la señal de que sobran campos.

### CP-006 — Los dos resúmenes traen los mismos campos

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-009 / [RNF-03](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) |
| **Tipo** | Funcional — cobertura |
| **Prioridad** | Media |
| **Datos de entrada** | Los dos resúmenes del 2026-08-14 y `plantillas/sesion.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los campos de cada hallazgo en los dos resúmenes | La misma lista en los dos |
| 2 | Compararla con la del modelo | No falta ninguno ni sobra ninguno |
| 3 | Buscar campos con la marca `«…»` sin reemplazar | Ninguno ([`13·DOC20`](../../../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md)) |

---

## 9. Gestión de defectos

| Severidad | Qué sería, acá | Atención |
|---|---|---|
| **Crítica** | Un hallazgo abierto que no se puede retomar sin abrir la transcripción | Antes de cerrar la fase |
| **Alta** | El resumen no se encuentra desde el índice del histórico | Antes de cerrar la fase |
| **Media** | Un campo del modelo que ningún resumen usa | Se decide en la fase: se quita o se justifica |
| **Baja** | Diferencia de redacción entre dos resúmenes | Backlog |

Se registran en el [resultado_pruebas.md](resultado_pruebas.md), no acá.

---

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) totales | 100% |
| Hallazgos abiertos retomables sin la transcripción | Retomables / abiertos | 100% |
| Campos del modelo que ningún resumen usa | Conteo | 0 |
| Fallas nuevas en la corrida del estándar | Después − antes | 0 |

El resultado de medirlas va en el [resultado_pruebas.md](resultado_pruebas.md).
