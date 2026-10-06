# Plan de Pruebas · Fase A-EP-025-HU-026, franja y pestañas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU026-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-026](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md), CA-01 a CA-03 |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Integración | Sumas, vistas y plantillas | El agente | `manage.py test` | Sí |
| Sistema | Las cinco pestañas en el navegador | El agente | `runserver` local | No |

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`core.consumo.tests_tablero`, y `core.consumo` entera porque `tablero.py` lo usan otras pruebas del módulo.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-026 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-026 | CA-01 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-026 | CA-02 | CP-003 | Funcional | Crítica | Sí | ☑ |
| HU-026 | CA-02 | CP-004 | Funcional | Alta | Sí | ☑ |
| HU-026 | CA-02 | CP-005 | Funcional | Alta | Sí | ☑ |
| HU-026 | CA-02 | CP-007 | Funcional | Alta | No | ☑ |
| HU-026 | CA-03 | CP-006 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 criterios cubiertos = 100 %. RNF-01 lo cubre CP-003 (cada pestaña, su ruta) y RNF-02 CP-005 (no se carga nada nuevo).

## 6. Casos de prueba

### CP-001 · La franja trae el total, las llamadas, el % de caché y el contexto máximo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `/gasto/franja/` con la cuenta de consulta | 200, con el total del período |
| 2 | Leer las llamadas, el % de caché y el contexto máximo | Los de los datos de prueba |
| 3 | Pedirla sin cuenta | Manda a entrar |

### CP-002 · La variación compara con el tramo anterior cortado a la misma hora

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner una llamada ayer antes de la hora actual y otra ayer después | Datos listos |
| 2 | Pedir la franja de «Hoy» | El tramo anterior cuenta solo la de antes de la hora |
| 3 | Sin gasto en el tramo anterior | La variación no se muestra como número |

### CP-003 · Cada pestaña tiene su ruta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `/gasto/pestana/resumen/`, `donde`, `contexto`, `ahorro` y `actividad` | 200 cada una, con su contenido |
| 2 | Pedir `/gasto/pestana/otra/` | 404 |

### CP-004 · «Dónde se gasta» agrupa con porcentaje

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir la pestaña con `agrupar=proyecto` | Una fila por proyecto, con su % del total |
| 2 | Pedirla con `agrupar=modelo` y con un valor que no existe | Por modelo; el que no existe cae en proyecto |

### CP-005 · Sin repetidos y sin intervalos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `/gasto/` | No trae `every `, ni `grafica-proyectos`, ni la tabla por tipo de token |
| 2 | Leer las bibliotecas que carga | Las mismas de `base.html` |

### CP-006 · Contexto muestra promedio, máximo y límite

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir la pestaña Contexto | Cada enganche y archivo con veces, promedio y máximo por vez |
| 2 | Con un proyecto filtrado | El límite es el de ese proyecto |
| 3 | Buscar una marca de fila pasada de límite | No hay |

### CP-007 · Las cinco pestañas en el navegador

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `http://127.0.0.1:8015/gasto/` y elegir cada pestaña | Cada una carga lo suyo; Resumen dibuja sus dos gráficas |
| 2 | Oprimir ↻ | La franja y la pestaña abierta se vuelven a pedir y cambia la hora |

## 9. Gestión de defectos

Van a `resultado_pruebas.md` §4; si obligan a tocar un archivo que el plan no declara, se detiene la fase.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre los 7 diseñados.
