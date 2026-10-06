# Funcionalidad implementada · Fase C-EP-005-HU-002-claves-de-anthropic-y-con-prefijo (módulo Cimiento, tapado de claves)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-002-claves-de-anthropic-y-con-prefijo` |
| **Módulo** | Cimiento, `core/validadores/secretos.py` y `core/enganches/enmascarar.py` |
| **Especificación del módulo** | [HU-002](../HU-002-enmascarar-claves.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-002](../HU-002-enmascarar-claves.md) ([CA-03](../HU-002-enmascarar-claves.md#ca-03--las-claves-de-anthropic-y-las-variables-con-prefijo-también-se-tapan)) |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.3.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

El tapado y el validador de secretos reconocen las claves de Anthropic (`sk-ant-...`) y toda variable que termine en `_API_KEY`, `_TOKEN`, `_SECRET` o `_PASSWORD`, tenga lo que tenga delante. Lo que lee del entorno y los moldes siguen sin tocarse.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Forma de Anthropic | servicio | `core/validadores/secretos.py` (`SEGUROS`) | ✅ | CP-001, CP-004 |
| Variable con prefijo, con comillas | servicio | `core/validadores/secretos.py` (`ASIGNA`, `CON_PREFIJO`) | ✅ | CP-002, CP-004 |
| Variable con prefijo, sin comillas | servicio | `core/enganches/enmascarar.py` (`_ASIGNA_SIN_COMILLAS`) | ✅ | CP-002 |
| Lo del entorno y los moldes no se tocan | servicio | Los mismos | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Forma de Anthropic | ✅ hecha | `core/validadores/secretos.py` | CP-001 |
| T-02 | Prefijo en `ASIGNA` | ✅ hecha | `core/validadores/secretos.py` | CP-002 |
| T-03 | Prefijo en `_ASIGNA_SIN_COMILLAS` | ✅ hecha | `core/enganches/enmascarar.py` | CP-002 |
| T-04 | Pruebas | ✅ hecha | `core/enganches/tests_claves_con_prefijo.py` | EV-01 |
| T-05 | Suites | ✅ hecha | 569 en verde | EV-02 |
| T-06 | `validar.py secretos` | ✅ hecha | Sin fallas nuevas | EV-03 |
| T-07 | CHANGELOG y VERSION | ✅ hecha | 55.3.0 | — |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** 2 h contra 2,2 h.

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

| Qué | Resultado |
|---|---|
| Suites ejecutadas | 569 en verde, 4 saltadas que ya existían |
| Verificaciones manuales | Ninguna |
| Defectos abiertos aceptados | Ninguno |

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Nada que hacer: el histórico, el guardado del gasto y el control de commits usan el tapado y la lista de secretos.

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El prefijo solo se admite unido con `_` | Sin `_` se taparía texto común | S-317 |
| Las pruebas comparan sin repetir la clave al fallar | Así entró una clave falsa al registro de la sesión | S-315 |

## 6. Deuda técnica y pendientes generados

Ninguna. Las 9 fallas de `validar.py secretos` son de antes de esta fase: claves falsas en pruebas ya versionadas.

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

- [x] Fila de la fase en la HU-002.

## 8. Despliegue, si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

No aplica: llega con la actualización del estándar. El vigilante usa el tapado nuevo cuando se reinicie.
