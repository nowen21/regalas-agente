# Plan de Pruebas · Fase B-EP-027-HU-005, la historia   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU005-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-005](../HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles.md), CA-02 |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.historia`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | CA-02 | CP-001 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias de esta fase cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La historia con nombres legibles

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear un documento del estándar y abrir «Historia» | La tabla dice «Documento del estándar» y la fila, el título del documento |
| 2 | Quitar el documento y abrir «Historia» | Su fila se sigue nombrando por su título |
| 3 | Contar las consultas al abrir una página con varios cambios del mismo documento | No crecen con el número de filas |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 1, en `resultado_pruebas.md`.
