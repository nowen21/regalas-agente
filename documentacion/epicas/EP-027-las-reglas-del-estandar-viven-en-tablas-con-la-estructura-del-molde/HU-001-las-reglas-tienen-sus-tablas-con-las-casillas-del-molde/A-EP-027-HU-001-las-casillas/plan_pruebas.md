# Plan de Pruebas · Fase A-EP-027-HU-001, las casillas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU001-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-001](../HU-001-las-reglas-tienen-sus-tablas-con-las-casillas-del-molde.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-001 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Las tablas tienen las casillas del molde

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear un capítulo, una regla con todas sus casillas, dos tareas y una dependencia | Se guardan y se leen igual |
| 2 | Dar a la marca, a la dependencia y a «validable» un valor fuera de los suyos | La validación lo rechaza |
| 3 | Repetir un código | La validación del modelo lo rechaza: MariaDB no tiene índices únicos con condición, y el código se repite entre el estándar y un proyecto |

### CP-002 · Una regla se lee en casillas y se vuelve a armar igual

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer y armar cada regla del estándar | Las 270 dan el mismo texto, con el orden del molde |
| 2 | Leer una regla con excepción, ejemplo, quién la hace cumplir y sello | Cada parte en su casilla, y de ellas salen incorrecto y correcto, condición, límite y autoriza, y el resultado del sello |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
