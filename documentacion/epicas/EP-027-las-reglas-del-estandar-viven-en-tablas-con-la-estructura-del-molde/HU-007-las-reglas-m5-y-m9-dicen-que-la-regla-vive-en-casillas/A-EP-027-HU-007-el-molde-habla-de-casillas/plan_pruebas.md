# Plan de Pruebas · Fase A-EP-027-HU-007, el molde habla de casillas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU007-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-007](../HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar.tests_molde`. La fase no cambia programas: solo texto del estándar.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · `20·M5` habla de casillas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `20·M5` del estándar en la base | Dice «casilla» y que el texto se arma desde ellas |
| 2 | Leer su checklist | Aplicado contra la versión nueva |

### CP-002 · `20·M9` manda a la casilla «validable»

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `20·M9`, el capítulo 20, su checklist y el molde | Ninguno nombra `validadores/reglas-validables.md` como el lugar donde se registra |
| 2 | Leer `20·M9` | Nombra los tres valores |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
