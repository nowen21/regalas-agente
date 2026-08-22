# Funcionalidad implementada — Fase A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.11.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Se puede comprobar, con una orden, si una fase tocó los archivos que su plan declaró.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| Los archivos declarados se leen del plan | código | [`validadores/plan_vs_hecho.py`](../../../../../validadores/plan_vs_hecho.py) | ✅ | `declarados`, sobre la §2.1 del molde |
| Se comparan contra el commit de origen | código | el mismo | ✅ | `--desde`; sin él, lo dice y no inventa |
| El archivo de más se avisa | código | el mismo | ✅ | y encontró tres del trabajo de hoy |
| Los documentos de la fase no cuentan | código | el mismo | ✅ | `CP-004` |
| El criterio sin caso se avisa | código | `comparar_casos` | ✅ | `CP-003` |
| Nunca detiene | código | el mismo | ✅ | `CP-005` |
| `02·F8` pasa a validador escrito | doc | [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) | ✅ | con lo que sigue siendo criterio, escrito |
| El `CA-03` queda como criterio humano | doc | el mismo | ✅ | con su motivo |
| El contrato | doc | [`docs/plan_vs_hecho.md`](../../../../../validadores/docs/plan_vs_hecho.md) | ✅ | qué compara y qué no |
| Los casos | prueba | [`test_el_plan_contra_lo_hecho.py`](../../../../../validadores/tests/test_el_plan_contra_lo_hecho.py) | ✅ | once |

## 2. Lo que cambia para un proyecto que hereda

**Gana una orden.** Al cerrar una fase, `validar.py plan --fase … --desde …` dice si se tocó algo que el plan no decía. No corre sola en la corrida completa porque necesita el commit de origen, que solo sabe quien abrió la fase.

## 3. Lo que queda abierto

**Trece avisos de criterios sin caso** en fases viejas, cuyos planes de prueba nombran los criterios de otra forma. Son de sus propias fases y no se tocaron: arreglarlos de paso sería repetir el defecto que este mismo validador acaba de encontrar.

**Y el que encontró sobre el trabajo de hoy:** la fase del conteo por regla amplió su plan sin escribirlo. Queda anotado en su [resultado](../../HU-009-conteo-por-regla/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/resultado_pruebas.md) y en el de esta.
