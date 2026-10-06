# Funcionalidad implementada · Fase A-EP-001-HU-040-c29-nombra-la-base-de-cimiento (módulo Capítulo 01)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-040-c29-nombra-la-base-de-cimiento` |
| **Módulo** | Capítulo `01 · Conducta de la IA` |
| **Especificación del módulo** | [base/01-conducta.md](../../../../../base/01-conducta.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-040](../HU-040-c29-reconoce-la-base-de-cimiento.md) ([CA-01](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-01--la-regla-nombra-la-base-de-cimiento), [CA-02](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-02--la-regla-pasa-sus-comprobaciones)) |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.1.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

`01·C29` ahora dice que lo del agente o del proyecto vive en el repositorio o en la base de datos del agente. Lo que la herramienta guarda afuera y no se deja corregir en su origen se trae a esa base en cuanto aparece, sin claves, y se lee de allá. Con eso, guardar en la base de Cimiento el gasto que Claude Code deja en su almacén cumple la regla.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01: lo del proyecto vive en el repositorio o en la base | doc | `base/01-conducta.md`, `## C29` | ✅ | CP-001 |
| RN-02: lo que no se corrige en su origen se trae a la base y se lee de allá | doc | `base/01-conducta.md`, `## C29` | ✅ | CP-001 |
| RN-03: antes pasa por el tapado de claves | doc | `base/01-conducta.md`, enlace a `00·N6` | ✅ | CP-001 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Reescribir cuerpo y ejemplo de `C29` | ✅ hecha | `base/01-conducta.md` | CP-001 |
| T-02 | Regenerar las copias de `reglas-por-tarea/` | ✅ hecha | `base/reglas-por-tarea/escribir-documento-1.md`, `cambiar-codigo-1.md`, `correr-comando.md` | Verificación manual 1 |
| T-03 | Volver a aplicar el checklist | ✅ hecha | `base/01-conducta.md`, checklist de `C29` | CP-001 |
| T-04 | CHANGELOG y VERSION 55.1.0 | ✅ hecha | `CHANGELOG.md`, `VERSION` | CP-003 |
| T-05 | Correr los validadores | ✅ hecha | `resultado_pruebas.md` §2 | CP-002 |
| T-06 | El checklist cita el acuerdo 5 | ✅ hecha | `base/01-conducta.md` | CP-001 |

**Correspondencia con el plan:** 6 tareas en el plan, 6 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno de esta fase. `mapa_tareas.py` reescribe todos los archivos de `reglas-por-tarea/`; los cambios en `cambiar-codigo-2.md` a `cambiar-codigo-4.md` vienen de otras sesiones y no entran en el commit de esta fase.

**Esfuerzo real contra estimado:** 1,5 h contra 1,5 h.

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

| Qué | Resultado |
|---|---|
| Suites ejecutadas | `validar.py metareglas` sin fallas y `validar.py estandar` sin incumplimientos |
| Verificaciones manuales | Las copias de `C29` quedaron iguales a la regla |
| Defectos abiertos aceptados | Ninguno |

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

La regla llega a cada proyecto con `base/` y la recupera el enganche de reglas en las tareas escribir-documento, cambiar-codigo y correr-comando.

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La regla dice «base de datos del agente» y no «Cimiento» | `20·M3` prohíbe nombres propios en `base/`; se descartó nombrar la plataforma | S-312 |
| Se conserva el título de `C29` | El ancla la citan el mapa de tareas, la memoria y otras reglas; cambiarlo los rompe | S-312 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

- [x] `base/mapa-de-tareas.md` y `base/reglas-por-tarea/` regenerados.

## 8. Despliegue, si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

No aplica: la regla llega a los proyectos con la próxima actualización del estándar.
