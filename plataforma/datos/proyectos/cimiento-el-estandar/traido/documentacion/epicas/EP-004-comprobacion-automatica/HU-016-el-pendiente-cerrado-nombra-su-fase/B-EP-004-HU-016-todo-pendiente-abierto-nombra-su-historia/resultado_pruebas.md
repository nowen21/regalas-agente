# Resultado de Pruebas — Fase B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia` |
| **HU** | [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el abierto sin la fila se reporta | y **detiene**: un pendiente sin historia no se puede ejecutar | ✅ Aprobado |
| CP-002 · la historia inventada se reporta | queda cubierto por el mismo camino que la fase inventada | ✅ Aprobado |
| CP-003 · el tema declarado pasa, la fila vacía no | no toda idea tiene historia todavía, y decirlo es una respuesta | ✅ Aprobado |
| CP-004 · los enrutados siguen en verde | los tres pendientes abiertos de hoy pasan sin tocar nada | ✅ Aprobado |
| CP-005 · la fila fuera de la ficha no cuenta | la fila vive en la ficha de cabecera, no en cualquier tabla | ✅ Aprobado |
| CP-006 · los casos borde del archivo | el índice de la carpeta no es un pendiente | ✅ Aprobado |

## 3. Por qué esta falla y la otra avisa

**Un abierto sin historia es un impedimento**: [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) manda construirlo como fase de una historia, y sin ella no hay dónde. **Un cerrado sin fase ya no rompe nada**: cortó su rastro, que es grave para leer el pasado y no impide nada hoy.

Es la misma regla que quedó escrita en el pendiente 59: **detiene lo que impide trabajar, avisa lo que solo informa mal.**

## 4. Veredicto

**Cumple.** Seis casos de seis. Los tres pendientes abiertos del repositorio pasan hoy sin cambios: el enrutamiento del 2026-08-17 dejó a cada uno con su historia, y esto es lo que impide que el próximo nazca sin ella.
