# Resultado de Pruebas · Fase `A-EP-026-HU-009-vista-previa-y-opt-in`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-009-vista-previa-y-opt-in` |
| **HU** | [HU-009](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local con la base de pruebas de Django sobre MariaDB; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | 2026-10-06 | `LosOptInSonAjustes`: editar el proyecto con el 15 en «Sí» lo guarda, con historia, versión nueva y copia | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | 2026-10-06 | `LasReglasSeEligenConLaBase`: registrado manda la base; sin registro, el `CLAUDE.md` | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | 2026-10-06 | `ElClaudeMdPasaALaBase`: pasan los siete, lo no nombrado en «sí», y la segunda vez nada | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | 2026-10-06 | `LaVistaPrevia`: muestra el bloque y los opt-in sin tocar la historia, con un mensaje simulado y con el estándar real | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** la regresión dio una falla: la ayuda exige el globo «?» de cada ajuste, y los siete opt-in no lo tenían. Se agregaron en `core/ayuda/textos.py`. Al migrar la base real, el paso apagaba los capítulos que el `CLAUDE.md` no nombra, que antes regían; ahora pasan en «sí»

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.proyectos.tests_opt_in core.estandar.tests_vista_previa --noinput` | Ran 5 tests in 5.401s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios tienen su caso aprobado: 5 pruebas nuevas; la regresión de 985 con la ayuda corregida, y 70 de `core.proyectos`, `core.ayuda` y la vista previa después de la corrección del paso.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.proyectos.tests_opt_in core.estandar.tests_vista_previa`: 5 OK; regresión: 985, una corregida; la base real migrada con 84 ajustes opt-in |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | Primera ejecución |
