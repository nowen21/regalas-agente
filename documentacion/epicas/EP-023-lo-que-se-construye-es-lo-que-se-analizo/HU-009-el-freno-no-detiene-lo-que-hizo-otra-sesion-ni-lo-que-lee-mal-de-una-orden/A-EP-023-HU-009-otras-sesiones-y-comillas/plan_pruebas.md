# Plan de Pruebas · Fase A-EP-023-HU-009, otras sesiones y comillas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU009-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-009](../HU-009-el-freno-no-detiene-lo-que-hizo-otra-sesion-ni-lo-que-lee-mal-de-una-orden.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 4 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.enganches.tests_freno_otras_sesiones core.enganches.tests_freno core.enganches.tests_freno_salida`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-009 | CA-02 | CP-003, CP-004 | Funcional | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Otra sesión activa escribió el archivo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Otra transcripción reciente nombra `.gitignore`, y `.gitignore` cambia | El freno no lo cuenta |

### CP-002 · Nadie más lo nombra, o la otra sesión es vieja

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ninguna otra transcripción nombra el archivo | El freno lo cuenta |
| 2 | La que lo nombra se escribió hace más de 10 minutos | El freno lo cuenta |
| 3 | Solo la propia transcripción lo nombra | El freno lo cuenta |

### CP-003 · La tabla dentro de un `sed`

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `sed -i 's/^| a | b |$/| c |/' x.md` | Los archivos que escribe son solo `x.md` |

### CP-004 · Los separadores de fuera se siguen respetando

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `rm a.txt; touch b.txt && echo "x;y" \| tee c.txt` | Escribe `a.txt`, `b.txt` y `c.txt`, y nada con `y` |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
