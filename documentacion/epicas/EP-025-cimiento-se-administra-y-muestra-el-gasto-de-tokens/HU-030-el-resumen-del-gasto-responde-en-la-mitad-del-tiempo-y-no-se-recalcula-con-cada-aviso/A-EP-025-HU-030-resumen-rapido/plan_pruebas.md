# Plan de Pruebas · Fase A-EP-025-HU-030, el Resumen rápido   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU030-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-030](../HU-030-el-resumen-del-gasto-responde-en-la-mitad-del-tiempo-y-no-se-recalcula-con-cada-aviso.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 146](../../../../../historico-chat/resumenes/2026-10-08/pendientes/146-el-resumen-del-gasto-tarda-y-se-pide-con-cada-mensaje/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.consumo.tests_rapido core.consumo.tests_tablero core.consumo.tests_en_vivo core.consumo.tests_pestanas`: las nuevas y las que ya probaban las gráficas y el aviso.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-030 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-030 | CA-01 | CP-002 | Rendimiento | Alta | No | ☑ |
| HU-030 | CA-02 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Cada llamada cae en su día local

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Llamadas de ayer a las 23:30 hora local (100 de entrada), de hoy a las 00:30 hora local (20) y de hoy al mediodía (3) | En `por_dia_por_tipo`, ayer suma 100 y hoy 23; en `por_dia`, lo mismo en el total |
| 2 | Contar las filas que trae la base | Una por hora con gasto, no una por llamada |

### CP-002 · El Resumen tarda menos de la mitad

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir tres veces `GastoDelPeriodo().pestana("resumen")` sobre la base real | Menos de 0,6 s cada una |

### CP-003 · La pantalla junta los avisos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `/gasto/` | El evento `gasto` ya no dispara `actualizar` directo: pasa por una espera de 30 segundos |
| 2 | Revisar lo que hace con la pantalla escondida | Escucha `visibilitychange` y no refresca mientras `document.hidden` |
| 3 | Revisar el botón «Actualizar» | Dispara `actualizar` en el momento |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
