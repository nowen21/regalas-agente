# Funcionalidad implementada — Fase A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.10.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Al terminar la corrida completa se sabe por cuál regla se incumple más, y dos corridas se pueden comparar.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| Cada hallazgo dice a qué regla pertenece | código | [`validadores/comun.py`](../../../../../validadores/comun.py) | ✅ | `Hallazgo.regla`, deducida del mensaje que ya se escribe |
| La corrida deja el conteo | código | [`validadores/conteo.py`](../../../../../validadores/conteo.py) y `validar.py todo` | ✅ | el recuento se imprime y se anota |
| El registro guarda solo el identificador y el número | código | el mismo | ✅ | `CP-002`: ni la clave, ni la ruta, ni el mensaje |
| Vive fuera del control de versiones | doc | `.gitignore` | ✅ | `metricas/conteo-por-regla.jsonl`, con el motivo escrito |
| Dos corridas se comparan | código | `conteo.comparar` | ✅ | `CP-003` |
| El contrato dice qué se guarda y qué no | doc | [`validadores/docs/conteo.md`](../../../../../validadores/docs/conteo.md) | ✅ | con las dos tablas |
| Los casos | prueba | [`test_el_conteo_por_regla.py`](../../../../../validadores/tests/test_el_conteo_por_regla.py) | ✅ | once |

## 2. Lo que cambia para un proyecto que hereda

**Corre solo con la corrida completa**, y no pide nada. Un proyecto que use `validar.py todo` empieza a acumular su propio recuento, en su carpeta y fuera de su control de versiones.

## 3. Lo que queda abierto

**El primer dato ya pide una conversación:** `00·ID8` produce dos de cada tres hallazgos del repositorio, porque se mide sobre todo el árbol mientras la regla exige limpieza en lo que se **entrega**. O la medición se acota a lo entregable, o la regla dice que aplica a todo. Está anotado en el resultado de esta fase; decidirlo no es de acá.
