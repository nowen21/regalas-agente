# Resultado de Pruebas · Fase `A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple` |
| **HU** | [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `b2151fc` más los cambios de la fase, versión 48.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `test_nada_fuera_del_plan.py` (4 pruebas) | La plantilla pide la aprobación con quién, cuándo y versión, y rutas exactas en la 2.1; la carpeta, el comodín y la descripción fallan una por fila; la aprobación sin quién o sin fecha falla; el plan aprobado con 47.0.0 no se revisa | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-03 | Alta | `test_nada_fuera_del_plan.py` (6 pruebas) en un repositorio de git temporal | Lo declarado pasa; lo no declarado falla y se nombra; los documentos de la fase y el resumen pasan; sin tocar una fase o con plan anterior no compara; el `pre-commit` corre `validar.py plan --preparados` | Aprobado | EV-02 | Ninguno |
| CP-003 | CA-04 | Alta | `test_nada_fuera_del_plan.py` (4 pruebas) | Las diez reglas traen su línea; `autorizado.py` dice qué regla autoriza el análisis, el guion y la memoria; lo que autoriza una `P1` del proyecto pasa; el ejemplo dentro de un bloque de código no cuenta | Aprobado | EV-03 | Ninguno |
| CP-004 | RNF-06 | Media | `validar.py flujo` | Ninguna tarea sin su criterio; queda el aviso de que la especificación son los criterios de la HU | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:**

- `autorizado.py` leyó primero el ejemplo de la línea, que está dentro de un bloque de código de `20·M5`, como si fuera una regla. Se corrigió dentro de la T-05 para que salte los bloques de código.
- Las rutas de la línea iban separadas por un punto medio, y eso sube las marcas de `00·ID8`. Se separan por coma, dentro de la T-04.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `validar.py marcas --preparados` | Ninguna nueva |
| 2 | Que las reglas sigan coherentes y el mapa de tareas al día | `validar.py estandar` y `validar.py tareas` | Sin fallas |
| 3 | Que los programas que cambió la fase sigan andando | Las 88 pruebas de `flujo.py`, `plan_vs_hecho.py` e `instalar.py` | Pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-03 | CP-002 | Aprobado | Sí |
| CA-04 | CP-003 | Aprobado | Sí |
| RNF-06 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-03.

**Justificación:** los CA-01, CA-03 y CA-04 y el RNF-06 tienen sus casos ejecutados y aprobados. Las pruebas de la fase pasan: 14 de `test_nada_fuera_del_plan.py`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Plantilla y validador | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `validadores/flujo.py`, `validadores/plan_vs_hecho.py` |
| EV-02 | Prueba, validador y enganche | `validadores/tests/test_nada_fuera_del_plan.py`, `validadores/validar.py`, `validadores/instalar.py` |
| EV-03 | Reglas y programa | `20·M5`, `plantillas/reglas-proyecto.md`, las diez reglas de la línea, `validadores/autorizado.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 4 | 0 | Primera ejecución |
