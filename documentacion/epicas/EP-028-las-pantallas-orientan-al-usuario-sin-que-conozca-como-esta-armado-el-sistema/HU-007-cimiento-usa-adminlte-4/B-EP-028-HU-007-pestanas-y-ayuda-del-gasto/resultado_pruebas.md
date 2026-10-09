# Resultado de Pruebas · Fase `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto` |
| **HU** | [HU-007](../HU-007-cimiento-usa-adminlte-4.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django y Cimiento en http://127.0.0.1:8015 con Chrome sin ventana; versión 58.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-04 | Alta | `core.consumo.tests_pestanas.LasPestanasFuncionan` y `ver_pestanas.mjs` | Cada pestaña muestra su contenido y queda marcada, también si se pulsa mientras el Resumen carga, justo después de un aviso de gasto nuevo, o después de agrupar en «Dónde se gasta» | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-05 | Alta | `core.consumo.tests_pestanas.LasPestanasTienenSuAyuda` y `ver_pestanas.mjs` | La franja y las cinco pestañas traen su «?» (de 4 a 16 por pestaña), ninguna clave queda sin texto, y el «?» de una pestaña cargada por htmx abre su globo | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** las tablas de Contexto, de cinco columnas, no cabían en media pantalla y se montaban unas sobre otras; pasaron a ancho completo y todas las tablas del gasto quedaron dentro de `table-responsive`.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.consumo core.ayuda --noinput` | 93 pruebas, OK |
| 2 | Las pestañas en el navegador | `node historico-chat/scripts/2026-10-08/ver_pestanas.mjs <sessionid>` | Sin errores en la consola, también al agrupar y pasar a otra pestaña; salida en EV-02 |

## 4. Defectos encontrados

Ninguno abierto. En el ciclo 2 se corrigió el que reportó el usuario: en «Dónde se gasta», los botones de agrupar heredaban `hx-swap="outerHTML"`, reemplazaban la caja `#pestana` entera y después ninguna pestaña cargaba (`htmx:targetError, #pestana`). El defecto que originó la fase (la pestaña marcada era una y el contenido, otro) quedó corregido y su salida de antes está en `historico-chat/scripts/2026-10-08/README.md`.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-04 | CP-001 | Aprobado | Sí |
| CA-05 | CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos casos pasan en Django y en el navegador, y la carrera que rompía las pestañas ya no se da.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_pestanas.py` |
| EV-02 | Salida en el navegador | `historico-chat/scripts/2026-10-08/salida_ver_pestanas.txt` y `pestanas.png` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 2 | 0 | Primera ejecución |
| 2 | 2026-10-08 | 2 | 0 | Reabierta: El usuario reporta htmx:targetError #pestana al pulsar los botones de Dónde se gasta: heredan hx-swap outerHTML y borran #pestana |
