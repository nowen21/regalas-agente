# Plan de Pruebas · Fase B-EP-001-HU-041, los totales del sello se leen   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP001-HU041-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-041](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Se corre `python validadores/validar.py metareglas`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-041 | CA-03 | CP-001 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El validador lee los totales

| Campo | Valor |
|---|---|
| **HU / CA** | HU-041 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | T-01 hecha |
| **Datos de entrada** | `M10`, `C19` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en `M10` y en `C19` la línea de totales del sello | Tiene el formato del checklist |
| 2 | Correr `python validadores/validar.py metareglas` | Sin fallas, y ningún aviso nombra `M10` ni `C19` |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 1, en `resultado_pruebas.md`.
