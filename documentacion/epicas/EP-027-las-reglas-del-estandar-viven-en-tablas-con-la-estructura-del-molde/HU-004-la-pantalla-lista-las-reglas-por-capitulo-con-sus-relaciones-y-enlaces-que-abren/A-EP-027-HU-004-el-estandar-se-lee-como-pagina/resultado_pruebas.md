# Resultado de Pruebas · Fase `A-EP-027-HU-004-el-estandar-se-lee-como-pagina`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-027-HU-004-el-estandar-se-lee-como-pagina` |
| **HU** | [HU-004](../HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django, con el estándar importado de `base/`; versión 57.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LaListaVaPorCapitulo` (3 pruebas) | Los capítulos llevan su nombre; F1 sale con código y título, sin ruta; C1 lleva a su sección del capítulo; buscar deja solo lo que dice la palabra | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElDocumentoSeLeeComoPagina` (2 pruebas) | F1 trae las tarjetas «Incorrecto» y «Correcto», la tabla de Tabler y ninguna marca del texto; «Cambiar el texto» solo lo ve quien administra | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `ElTextoNoEntraComoHtml` (2 pruebas) | `<script>` sale escapado; el ancla es la de GitHub | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-03 | Alta | `LosEnlacesAbrenYLasRelacionesSeVen` (3 pruebas) | El enlace de F0 a F2 abre F2 en Cimiento; las relaciones salen en tres grupos sin repetirse; un archivo fuera de la base queda como texto | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.estandar.tests_vista_estandar --noinput` | Ran 10 tests in 14.435s, OK |
| 2 | Los 153 documentos de la base | Pasarlos todos a HTML y buscar marcas sueltas y anclas repetidas | Las marcas que quedan están dentro de código, como muestras; 0 anclas repetidas |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002, CP-003 | Aprobado | Sí |
| CA-03 | CP-004 | Aprobado | Sí |
| RNF-02 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen sus casos aprobados, y `core.estandar` y `core.ayuda` pasan completas (59 pruebas).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar core.ayuda`: 59 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 4 | 0 | Primera ejecución |
