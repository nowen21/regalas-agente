# Funcionalidad implementada · Fase `A-EP-029-HU-006-sin-interfaz` (módulo Estándar: el repositorio)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-006-sin-interfaz` |
| **Módulo** | Estándar: `interfaz/`, `.claude/settings.json` y `anatomia/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-el-visor-viejo-interfaz-sale-del-estandar.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-01) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 59.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Salió `interfaz/`, el visor viejo que reemplazó Cimiento: sus 50 archivos de git y lo que tenía suelto, su Python incluido. Salió su permiso de `.claude/settings.json`, y `anatomia/` ya no la describe. Las fases cerradas, `CHANGELOG.md`, `cvds/` y `documentacion/senales.md` la siguen nombrando, como historia. El estándar se reconoce ahora como un solo programa: Cimiento.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Estándar | `interfaz/` (borrada), `.claude/settings.json`, `anatomia/` | Hecho | CP-001 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 2 tareas del plan quedaron hechas.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. Los 6 enlaces rotos (H-8) los agregó al plan el análisis 5 del pendiente 141 antes de tocarlos.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Nada que usar: lo que mostraba el visor viejo lo muestra Cimiento.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las fases cerradas no se tocan | Son historia (`20·M11`) | Ninguna |

## 6. Deuda técnica y pendientes generados

Se paga: un visor sin uso dentro del estándar.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

`anatomia/componentes-del-agente.md` y `anatomia/mapa-del-sitio.md`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno.
