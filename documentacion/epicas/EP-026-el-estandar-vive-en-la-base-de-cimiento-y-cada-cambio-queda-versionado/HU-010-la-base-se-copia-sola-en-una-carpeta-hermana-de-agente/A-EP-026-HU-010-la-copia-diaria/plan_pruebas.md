# Plan de Pruebas · Fase A-EP-026-HU-010, la copia diaria   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU010-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-010](../HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.historia`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-010 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-010 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-010 | CA-03 | CP-003 | Seguridad | Crítica | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La copia del día, una sola vez

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Copiar la base de pruebas a una carpeta temporal | Queda `cimiento-AAAA-MM-DD.sql` con las tablas |
| 2 | Pedir la copia de hoy otra vez | No se hace otra |

### CP-002 · Se guardan las últimas 7

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dejar 8 copias viejas y copiar la de hoy | Quedan las 7 más nuevas, con la de hoy |

### CP-003 · Sin claves y se restaura

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en la copia filas de las sesiones del navegador | No hay |
| 2 | Probar la copia en una base aparte | Se carga, cuenta sus tablas y la base aparte desaparece |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
