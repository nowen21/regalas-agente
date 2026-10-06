# Funcionalidad implementada · Fase A-EP-025-HU-025-lineas-a-la-base-sin-relojes (módulo Cimiento, consumo)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-025-lineas-a-la-base-sin-relojes` |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) ([CA-01](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-01--la-línea-queda-en-la-base-sin-claves-y-una-sola-vez), [CA-02](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-02--el-vigilante-guarda-en-el-momento-del-aviso), [CA-03](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-03--un-proyecto-nuevo-entra-con-su-primer-aviso), [CA-04](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-04--el-readme-dice-cómo-llega-el-gasto)) |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.2.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Cada línea que Claude Code escribe en un `.jsonl` de un proyecto activo queda en la base de Cimiento, con las claves tapadas, en el mismo aviso de Windows que la trae. El vigilante ya no espera 2 segundos ni relee los proyectos cada 60: guarda con cada aviso y relee la lista cuando llega una carpeta que no conoce. Lo que ya estaba en los `.jsonl`, 102 478 líneas, se trajo con `leer_consumo --desde-cero`.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01: cada línea en la base, tapada, una sola vez | modelo, servicio | `core/consumo/models.py` (`LineaDeSesion`), `core/consumo/guardar.py` (`guardar_lineas`) | ✅ | CP-001, CP-002, CP-003 |
| RN-02: conteos de las mismas líneas, misma transacción | servicio | `core/consumo/guardar.py` (`leer_archivo`), `core/consumo/lector.py` (`crudas`) | ✅ | CP-001 |
| RN-03: guarda con cada aviso | servicio | `core/consumo/vigilante.py` (`avisar`) | ✅ | CP-004 |
| RN-04: carpeta desconocida relee la lista | servicio | `core/consumo/vigilante.py` (`proyecto_de`) | ✅ | CP-005 |
| RN-05: ningún intervalo | servicio | `core/consumo/vigilante.py` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Modelo y migración | ✅ hecha | `core/consumo/models.py`, `core/consumo/migrations/0005_lineas_de_sesion.py` | CP-006 |
| T-02 | Líneas crudas con su posición | ✅ hecha | `core/consumo/lector.py` | CP-001 |
| T-03 | Guardar las líneas tapadas | ✅ hecha | `core/consumo/guardar.py` | CP-001 |
| T-04 | `leer_consumo --desde-cero` | ✅ hecha | `core/consumo/management/commands/leer_consumo.py` | CP-002, CP-006 |
| T-05 | `tests_lineas.py` | ✅ hecha | `core/consumo/tests_lineas.py` | EV-01 |
| T-06 | `avisar` en el acto y relectura por carpeta | ✅ hecha | `core/consumo/vigilante.py` | CP-004, CP-005 |
| T-07 | Espera sin reloj | ✅ hecha | `core/consumo/vigilante.py` (`correr`) | CP-004 |
| T-08 | Ajustar `tests_vigilante.py` | ✅ hecha | `core/consumo/tests_vigilante.py` | EV-02 |
| T-09 | README | ✅ hecha | `proyectos/cimiento/README.md` | CP-007 |
| T-10 | CHANGELOG y VERSION | ✅ hecha | `CHANGELOG.md`, `VERSION` | 55.2.0 |

**Correspondencia con el plan:** 10 tareas en el plan, 10 acá.

**Tareas que no se hicieron:** ninguna. `vigilar_consumo.py` estaba declarado para T-07 y no hizo falta tocarlo: ya llama `correr()` sin argumentos.

**Archivos tocados que el plan no declaraba**, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** 6 h contra 6,4 h.

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

| Qué | Resultado |
|---|---|
| Suites ejecutadas | `core.consumo.tests_lineas`, `tests_vigilante` y `tests`: 27 de 27 en verde |
| Verificaciones manuales | Migración de ida y vuelta, y lectura desde cero sobre la base real |
| Defectos abiertos aceptados | DEF-01, el tapado no conoce las claves de Anthropic: es de EP-005·HU-002 y queda en el pendiente 129 |

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

`vigilar_consumo` guarda solo. `leer_consumo --desde-cero` trae de nuevo todo lo que hay, sin duplicar.

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Línea única por archivo y huella | Por posición se perdería una versión cuando Claude Code reescribe el archivo | S-314 |
| `avisar` guarda en el hilo de `watchdog`, con candado | Una cola necesita revisarse cada cierto tiempo, y eso es un reloj | S-314 |
| `correr` espera un evento sin tiempo | En Windows, Ctrl+C no corta esa espera; se detiene con `--parar`, como lo hace la instalación | S-314 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino (fase futura / ticket / `pendientes/`) |
|---|---|---|
| El tapado no conoce las claves de Anthropic | No previsto | [Pendiente 129](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/pendiente.md) |

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

- [x] Fila de la HU-025 en la épica.

## 8. Despliegue, si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

| Paso | Qué |
|---|---|
| Migración | `manage.py migrate` (aplica `consumo.0005`); ya corrida en esta máquina |
| Datos | `manage.py leer_consumo --desde-cero` una vez; ya corrida en esta máquina |
| Después | Reiniciar el vigilante: `manage.py vigilar_consumo --parar` y volver a arrancarlo, o cerrar y abrir la sesión de Windows |
| Reversión | `manage.py migrate consumo 0004` y revertir el commit |
