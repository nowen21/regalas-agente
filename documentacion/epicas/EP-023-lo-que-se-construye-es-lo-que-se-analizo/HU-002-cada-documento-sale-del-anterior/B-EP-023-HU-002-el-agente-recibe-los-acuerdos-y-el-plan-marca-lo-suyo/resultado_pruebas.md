# Resultado de Pruebas · Fase `B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo` |
| **HU** | [HU-002](../HU-002-cada-documento-sale-del-anterior.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-03 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `6034476` más los cambios de la fase, versión 50.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-04 | Alta | `test_los_acuerdos_llegan.py` (5 pruebas) | La fase recién creada recibe los acuerdos de todos los CA de su HU; con plan, solo los de sus CA; con el commit anotado o vieja y cerrada, deja de estar en curso; la nueva con cierre y sin commit sigue en curso | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-04 | Alta | `test_los_acuerdos_llegan.py` (4 pruebas) y el enganche sobre el repositorio | Llegan los acuerdos de los análisis aprobados del pendiente; con un tope pequeño, los que no caben llegan nombrados con su tema y su número; con una entrada dañada el enganche sale con 0; el instalador lo registra | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-05 | Alta | `test_los_acuerdos_llegan.py` (6 pruebas) | La plantilla tiene la columna; la decisión sin acuerdo ni marca, la que cita un acuerdo que no existe y la tabla sin la columna fallan; la cita válida y la propuesta pasan; el plan aprobado con 49.0.0 no se revisa | Aprobado | EV-02 | Ninguno |
| CP-004 | RNF-06 | Media | `validar.py flujo` | Ninguna tarea sin su criterio; queda el aviso de que la especificación son los criterios de la HU | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** el mapa del sitio no lista los enganches uno por uno; la carpeta `adaptadores/claude-code/` ya los cubre, así que solo se sumó `acuerdos.py`.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `validar.py marcas --preparados` | Ninguna nueva |
| 2 | Coherencia del estándar y origen de cada punto | `validar.py estandar` y `validar.py origen` | Sin fallas |
| 3 | Que los programas que cambió la fase sigan andando | Las 93 pruebas de `origen.py` y del instalador | Pasan |
| 4 | Lo que entrega el enganche sobre este repositorio | Correrlo con la fase en curso | Entrega los acuerdos 3 y 4 del análisis 10 |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-04 | CP-001, CP-002 | Aprobado | Sí |
| CA-05 | CP-003 | Aprobado | Sí |
| RNF-06 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-03.

**Justificación:** los CA-04 y CA-05 y el RNF-06 tienen sus casos ejecutados y aprobados. Las pruebas de la fase pasan: 15 de `test_los_acuerdos_llegan.py`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa, enganche e instalador | `validadores/acuerdos.py`, `adaptadores/claude-code/hook_acuerdos.py`, `validadores/instalar.py` |
| EV-02 | Plantilla, validador y pruebas | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `validadores/origen.py`, `validadores/tests/test_los_acuerdos_llegan.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-03 | 4 | 0 | Primera ejecución |
