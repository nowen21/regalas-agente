# Plan de Pruebas · Fase A-EP-025-HU-027, aviso y eventos   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU027-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-027](../HU-027-la-pantalla-se-entera-en-el-momento.md), CA-01 y CA-02 |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

`manage.py test core.consumo`, que es el módulo que la fase cambia.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-027 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-027 | CA-01 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-027 | CA-01 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-027 | CA-02 | CP-004 | Seguridad | Crítica | Sí | ☑ |

**Cobertura:** 2 de 2 = 100 %.

## 6. Casos de prueba

### CP-001 · El aviso llega a quien espera, sin reloj

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Esperar un aviso en un hilo y avisar desde otro | El que espera despierta con el número nuevo |
| 2 | Pedir el primer evento del generador después de un aviso | Trae `event: gasto` |
| 3 | Buscar `sleep(`, `every ` y `setInterval` en `avisos.py`, `vigilante.py` y `tablero.html` | No aparecen |

### CP-002 · El vigilante avisa solo cuando guardó algo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir un `.jsonl` y llamar `avisar` | Se avisa a Cimiento una vez |
| 2 | Llamar `avisar` sin nada nuevo | No se avisa |
| 3 | Avisar a un puerto cerrado | No falla y vuelve en menos de 2 segundos |

### CP-003 · La pantalla escucha los eventos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `/gasto/` | Trae `EventSource` con `/gasto/eventos/` y dispara `actualizar` |
| 2 | Pedir `/gasto/eventos/` con cuenta | 200 con `text/event-stream` |
| 3 | Pedirlo sin cuenta | Manda a entrar |

### CP-004 · El aviso solo desde la misma máquina

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `POST /gasto/aviso/` desde `127.0.0.1`, sin cuenta | 204 y el número de avisos sube |
| 2 | Lo mismo desde otra dirección | 403 y el número no cambia |
| 3 | `GET /gasto/aviso/` | 405 |

## 9. Gestión de defectos

Van a `resultado_pruebas.md` §4.

## 12. Métricas e informe

4 casos.
