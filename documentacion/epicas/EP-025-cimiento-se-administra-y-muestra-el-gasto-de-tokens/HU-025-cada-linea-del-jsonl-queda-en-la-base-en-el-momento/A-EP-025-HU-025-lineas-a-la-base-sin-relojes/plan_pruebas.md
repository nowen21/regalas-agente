# Plan de Pruebas · Fase A-EP-025-HU-025, las líneas del `.jsonl` a la base sin relojes   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU025-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitarias | Guardado de líneas, tapado, vigilante | El agente | Local, base de pruebas | Sí |
| Integración | `watchdog` de verdad avisa y la línea llega | El agente | Local | Sí |
| Sistema | Migración de ida y vuelta, lectura desde cero sobre los `.jsonl` reales | El agente | Local, base `cimiento` | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Criterios de aceptación de la HU |
| Seguridad | ☑ | Ninguna clave en la base |
| Rendimiento | ☑ | Lectura desde cero archivo por archivo |
| Recuperación | ☑ | La migración se deshace |

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`manage.py test core.consumo.tests_lineas core.consumo.tests_vigilante core.consumo.tests`, que son la suite nueva, la del vigilante y la del guardado que la fase cambia.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-025 | [CA-01](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-01--la-línea-queda-en-la-base-sin-claves-y-una-sola-vez) | [CP-001](#cp-001--cada-línea-queda-en-la-base-con-la-clave-tapada), [CP-002](#cp-002--leer-otra-vez-no-duplica), [CP-003](#cp-003--un-archivo-reescrito-conserva-las-dos-versiones) | Funcional | Crítica | Sí | ☐ |
| HU-025 | [CA-02](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-02--el-vigilante-guarda-en-el-momento-del-aviso) | [CP-004](#cp-004--el-aviso-guarda-en-el-acto-y-no-hay-relojes) | Funcional | Crítica | Sí | ☐ |
| HU-025 | [CA-03](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-03--un-proyecto-nuevo-entra-con-su-primer-aviso) | [CP-005](#cp-005--un-proyecto-nuevo-entra-con-su-primer-aviso) | Funcional | Alta | Sí | ☐ |
| HU-025 | [CA-04](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-04--el-readme-dice-cómo-llega-el-gasto) | [CP-007](#cp-007--el-readme-dice-cómo-llega-el-gasto) | Documental | Media | No | ☐ |
| HU-025 | RNF-01 | [CP-001](#cp-001--cada-línea-queda-en-la-base-con-la-clave-tapada) | Seguridad | Crítica | Sí | ☐ |
| HU-025 | RNF-02 | [CP-006](#cp-006--la-migración-va-y-vuelve-y-la-lectura-desde-cero-termina) | Rendimiento | Alta | No | ☐ |

**Cobertura:** 6 de 6 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Cada línea queda en la base con la clave tapada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-025 / CA-01, RNF-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Un proyecto activo y un `.jsonl` de muestra con dos llamadas y una línea que trae una clave armada en tiempo de ejecución |
| **Datos de entrada** | `muestra()` de `core/consumo/tests.py` más la línea con la clave |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el archivo con `GuardadoDeConsumo.leer_archivo` | Devuelve lo nuevo |
| 2 | Contar las filas de `LineaDeSesion` | Una por línea completa del archivo |
| 3 | Buscar la clave en el texto guardado | No aparece; aparece la marca del `Enmascarador` |
| 4 | Contar las llamadas | Las mismas dos que antes de esta fase |

### CP-002 · Leer otra vez no duplica

| Campo | Valor |
|---|---|
| **HU / CA** | HU-025 / CA-01 |
| **Tipo** | Funcional, idempotencia |
| **Prioridad** | Crítica |
| **Precondiciones** | CP-001 hecho |
| **Datos de entrada** | El mismo archivo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner en cero el avance del archivo y volver a guardarlo | Termina sin error |
| 2 | Contar líneas y llamadas | Las mismas cantidades que en CP-001 |
| 3 | Correr `leer_consumo --desde-cero` | Las mismas cantidades |

### CP-003 · Un archivo reescrito conserva las dos versiones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-025 / CA-01 |
| **Tipo** | Funcional, caso borde |
| **Prioridad** | Alta |
| **Precondiciones** | CP-001 hecho |
| **Datos de entrada** | El archivo reescrito con una línea distinta y más corto |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reescribir el archivo con otra línea, más corto | El tamaño baja |
| 2 | Guardarlo | Lee desde el comienzo |
| 3 | Contar líneas | Las de antes más la nueva |

### CP-004 · El aviso guarda en el acto y no hay relojes

| Campo | Valor |
|---|---|
| **HU / CA** | HU-025 / CA-02 |
| **Tipo** | Funcional e integración |
| **Prioridad** | Crítica |
| **Precondiciones** | Un proyecto activo |
| **Datos de entrada** | `muestra()` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el archivo y llamar `avisar` una vez | Las llamadas ya están en la base al volver |
| 2 | Arrancar el vigilante de verdad en un hilo y escribir el archivo | Las llamadas llegan sin que nada las pida |
| 3 | Parar el vigilante con su evento | El hilo termina |
| 4 | Buscar `sleep`, `CADA` y `LISTA_CADA` en `vigilante.py` | No aparecen |

### CP-005 · Un proyecto nuevo entra con su primer aviso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-025 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Vigilante con la lista leída |
| **Datos de entrada** | Un proyecto registrado después de leer la lista |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Registrar el proyecto y escribir su `.jsonl` | El vigilante no lo tiene en la lista |
| 2 | Llamar `avisar` con ese archivo | Relee la lista y guarda las llamadas |
| 3 | Llamar `avisar` con un archivo de una carpeta que no es de ningún proyecto | No guarda nada y no falla |

### CP-006 · La migración va y vuelve, y la lectura desde cero termina

| Campo | Valor |
|---|---|
| **HU / CA** | HU-025 / RNF-02, contraria de `02·F30` |
| **Tipo** | Sistema |
| **Prioridad** | Alta |
| **Precondiciones** | Base `cimiento` local |
| **Datos de entrada** | Los `.jsonl` reales de los proyectos registrados |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `python manage.py migrate consumo` | Aplica `0005` |
| 2 | `python manage.py migrate consumo 0004` | La tabla sale |
| 3 | `python manage.py migrate consumo` | La tabla vuelve |
| 4 | `python manage.py leer_consumo --desde-cero` | Termina y cuenta líneas guardadas |

### CP-007 · El README dice cómo llega el gasto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-025 / CA-04 |
| **Tipo** | Documental |
| **Prioridad** | Media |
| **Precondiciones** | T-09 hecha |
| **Datos de entrada** | `proyectos/cimiento/README.md` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `/v1/logs` | No aparece |
| 2 | Leer el párrafo del gasto | Nombra al vigilante y la base |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4 con el paso que falló; si obliga a tocar un archivo que el plan no declara, es hallazgo y se detiene la fase.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre los 7 diseñados, en `resultado_pruebas.md`.
