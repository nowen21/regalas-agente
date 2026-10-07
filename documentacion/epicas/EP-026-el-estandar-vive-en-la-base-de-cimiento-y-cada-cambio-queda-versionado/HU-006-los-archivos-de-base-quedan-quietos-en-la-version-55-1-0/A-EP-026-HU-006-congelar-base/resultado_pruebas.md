# Resultado de Pruebas · Fase `A-EP-026-HU-006-congelar-base`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-006-congelar-base` |
| **HU** | [HU-006](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local con la base de pruebas de Django sobre MariaDB, y la base real para congelar; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-06 | `ElFreno`: con la marca detiene `base/`, `VERSION` y `CHANGELOG.md` y deja `plantillas/`; sin la marca o en otra carpeta no detiene por esto | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Crítica | 2026-10-06 | `ElCommit`: `base/` y `VERSION` fallan; `plantillas/` falla sin versión nueva y pasa con ella; el código no pide nada | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | 2026-10-06 | `CongelarYDescongelar`: deja la marca, la versión de la base no queda por debajo de `VERSION` y `--deshacer` la quita | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | 2026-10-06 | `DondeLeerLasReglas`: el texto de la base y la instrucción del arranque dicen `ver_estandar`; los del disco no | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** la regresión dio una falla en la prueba «mismas reglas» de la HU-004: el aviso de `ver_estandar` ocupa bytes y con el tope de siempre caben otras reglas. La prueba compara ahora sin tope y sin el aviso. El freno detuvo dos veces la regresión en segundo plano (H-9, H-10)

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.estandar --noinput` | Ran 18 tests in 66.171s, OK |

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

**Justificación:** los cuatro criterios tienen su caso aprobado: 5 pruebas nuevas, 18 de `core.estandar` y 911 en la regresión; el congelamiento real dejó el estándar en la 56.8.1.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar`: 18 OK; regresión `core.estandar core.enganches.tests_freno core.enganches.tests_freno_salida core.enganches.tests_sesion core.herramientas.tests_respondo core.validadores`: 911, con la falla de «mismas reglas» corregida; `congelar_base` real: 56.8.1 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | Primera ejecución |
