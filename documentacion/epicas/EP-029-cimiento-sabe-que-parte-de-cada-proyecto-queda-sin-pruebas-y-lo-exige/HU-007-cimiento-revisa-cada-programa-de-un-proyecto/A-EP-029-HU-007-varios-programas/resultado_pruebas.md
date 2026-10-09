# Resultado de Pruebas · Fase `A-EP-029-HU-007-varios-programas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-007-varios-programas` |
| **HU** | [HU-007](../HU-007-cimiento-revisa-cada-programa-de-un-proyecto.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django sobre MariaDB, con la herramienta simulada; versión 59.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 3 | 3 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `EncuentraTodosLosProgramas` | Angular en `proyectos/front` y Python en `proyectos/back`; lo de adentro de Django es de Django | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `RevisaYPonLaParteEnCadaUno` | Dos revisiones con la misma fecha, coverage.py y ng test; la parte en cada programa | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `LaFilaYElDetalle` | La fila dice 30,0% y «Angular y Python»; el detalle muestra los dos programas | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** en el ciclo 1, CP-003 esperaba «30.0%» y la página escribe «30,0%», con la coma decimal de Colombia; la prueba se corrigió. La regresión de ese ciclo dio 5 errores en `core.proyectos` («Duplicate entry 'admin-logentry'»), que no volvieron al repetirla: coincidieron con pruebas de otra sesión sobre la misma base de pruebas.

## 4. Defectos encontrados

Ninguno de la fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | Las pruebas de la HU-002 con revisiones sin programa | Aprobado | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen su caso aprobado y la regresión de `core.proyectos core.pruebas` pasa entera.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.proyectos core.pruebas`: Ran 118 tests, OK; `core.inicio core.ayuda core.herramientas.tests_instalacion` pasaron en la corrida de 373 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 2 | 1 | La coma decimal en la prueba |
| 2 | 2026-10-08 | 3 | 0 | |
