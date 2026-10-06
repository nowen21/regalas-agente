# Resultado de Pruebas · Fase `A-EP-025-HU-026-franja-y-pestanas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-026-franja-y-pestanas` |
| **HU** | [HU-026](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento local con MariaDB, sobre `ae82d18` con los cambios de la fase sin guardar; versión 55.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | `LaFranja.test_total_llamadas_cache_y_maximo` y `test_sin_cuenta_manda_a_entrar` | Total 6.515, 2 llamadas, 77 % de caché, contexto máximo 6.200; sin cuenta manda a entrar | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | `LaFranja.test_compara_con_el_tramo_anterior_a_la_misma_hora`, con llamadas ayer antes y después de las 12:00 | El tramo anterior contó solo la de antes (100); la variación sin tramo anterior no es número y dice «Sin gasto en el tramo anterior» | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Crítica | `LasPestanas.test_cada_pestana_tiene_su_ruta_y_la_que_no_existe_da_404` | Las cinco dieron 200 y `/gasto/pestana/otra/` dio 404 | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Alta | `LasPestanas.test_donde_agrupa_con_porcentaje` | «uno» 6.500 con 100 %, «dos» 15 con 0 %; `agrupar=modelo` agrupa por modelo y `agrupar=nada` cae en proyecto | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-02 | Alta | `LasPestanas.test_sin_repetidos` y `SeActualizaConElBoton.test_sin_intervalos_y_con_los_filtros` | Sin `grafica-proyectos`, sin tabla por tipo de token y sin `every `; la franja escucha `actualizar from:body` | Aprobado | EV-01 | Ninguno |
| CP-007 | CA-02 | Alta | Las siete vistas armadas con `RequestFactory` sobre la base real, en «7 días», «30 días» con un proyecto y «Hoy» | Las 21 respondieron 200, la más lenta en 0,47 s; las gráficas de ApexCharts no se vieron en un navegador: queda para el usuario | Aprobado | EV-01 | Ninguno |
| CP-006 | CA-03 | Alta | `LasPestanas.test_contexto_trae_promedio_maximo_y_limite_sin_marcar` | «Revisando las reglas...» con 3 veces, promedio y máximo 100; el límite es el del proyecto; ninguna fila marcada | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá.

**Qué salió distinto de lo esperado:** CP-007 se hizo armando las vistas en el servidor y no en un navegador: las dos gráficas del Resumen y el botón ↻ quedan por ver con los ojos.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.consumo` | Ran 64 tests in 9.810s, OK |

## 4. Defectos encontrados

Ninguno. Para cerrar se agregaron al plan, con aprobación del usuario, `tests_segunda_tanda.py` y `tests_tercera_tanda.py`, que pedían `/gasto/datos/`.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003, CP-004, CP-005, CP-007 | Aprobado | Sí |
| CA-03 | CP-006 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 7 de 7 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** Los tres criterios tienen sus casos aprobados y `core.consumo` pasa 64 de 64; lo único sin ver es el dibujo de las gráficas en un navegador.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/consumo/tests_tablero.py`, `tests_segunda_tanda.py`, `tests_tercera_tanda.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 7 | 0 | Primera ejecución |
