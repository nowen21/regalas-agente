# Resultado de Pruebas · Fase `B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar` |
| **HU** | [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-03 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `2dad127` más los cambios de la fase, versión 51.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-02 | Alta | `test_el_freno.py` (6 pruebas) y `test_nada_fuera_del_plan.py` (5 de lo autorizado) | Sin aprobar el plan pasan solo los documentos de la fase; aprobado, lo que declara; sin fase en curso, lo autorizado, incluida la HU; lo que el análisis prendido manda hacer de una pasa; afuera, también con `..`, se detiene; solo la regla vigente autoriza; el instalador pone el freno sobre toda acción | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_el_freno.py` (3 pruebas) | Redirigir, copiar o borrar fuera del plan se detiene; el segundo plano, instalar paquetes, la configuración global y el proceso que queda corriendo se detienen; lo que solo lee pasa | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `test_el_freno.py` (1 prueba) | La herramienta que publica se pregunta; la de lectura pasa | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Alta | `test_el_freno.py` (1 prueba) en un repositorio de git temporal | Después de la orden, avisa el archivo no declarado; no cuenta el que ya estaba cambiado ni el declarado | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-02 | Alta | `test_el_freno.py` (2 pruebas) | El resumen suma el hallazgo una sola vez, antes del cierre; el enganche detiene y dice que se vuelve al análisis | Aprobado | EV-02 | Ninguno |
| CP-006 | RNF-06 | Media | `validar.py flujo` | Ninguna tarea sin su criterio | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 6 casos en el plan, 6 acá.

**Qué salió distinto de lo esperado:**

- El H-14: una prueba de la fase `A` contaba exactamente diez reglas. El análisis 11 la cambió por reglas de ejemplo y el plan pasó a su versión 2.
- El H-15: fallan tres pruebas de la EP-005 que describen el freno viejo. No afectan esta fase; su pendiente es el [109](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `validar.py marcas --preparados` | Ninguna nueva |
| 2 | Coherencia del estándar, mapa de tareas y origen | `validar.py estandar`, `tareas` y `origen` | Sin fallas |
| 3 | Que los programas que cambió la fase sigan andando | Las 114 pruebas del instalador, el análisis y los acuerdos | Pasan |

## 4. Defectos encontrados

Ninguno en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-02, capas 1 y 2 | CP-001 a CP-005 | Aprobado | Sí |
| RNF-06 | CP-006 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 6 de 6 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-03.

**Justificación:** el CA-02, en sus capas 1 y 2, y el RNF-06 tienen sus casos ejecutados y aprobados. Las pruebas de la fase pasan: 13 de `test_el_freno.py` y 16 de `test_nada_fuera_del_plan.py`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa, enganches e instalador | `validadores/freno.py`, `validadores/autorizado.py`, `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py`, `validadores/instalar.py` |
| EV-02 | Pruebas, reglas y plantilla | `validadores/tests/test_el_freno.py`, `validadores/tests/test_nada_fuera_del_plan.py`, `13·DOC15`, `13·DOC16`, `02·F23`, `plantillas/analisis.md` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-03 | 6 | 0 | Primera ejecución |
