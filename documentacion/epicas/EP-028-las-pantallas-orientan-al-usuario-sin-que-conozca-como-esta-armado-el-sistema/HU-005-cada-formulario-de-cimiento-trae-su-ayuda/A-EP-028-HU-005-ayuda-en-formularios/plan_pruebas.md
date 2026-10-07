# Plan de Pruebas · Fase A-EP-028-HU-005, ayuda en formularios   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU005-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-005](../HU-005-cada-formulario-de-cimiento-trae-su-ayuda.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.ayuda core.estandar core.historia core.proyectos core.niveles core.consumo core.cuentas core.inicio`: la ayuda y las suites de las pantallas que cambian.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-005 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Cada campo tiene su «?»

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar cada plantilla de formulario | Cada campo visible tiene su `ayuda_campo` |
| 2 | Revisar las claves usadas | Todas tienen texto |

### CP-002 · Cada pantalla con formulario dice para qué sirve

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar cada plantilla de formulario | Trae `ayuda_pantalla`, con su texto de «¿Para qué sirve?» |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
