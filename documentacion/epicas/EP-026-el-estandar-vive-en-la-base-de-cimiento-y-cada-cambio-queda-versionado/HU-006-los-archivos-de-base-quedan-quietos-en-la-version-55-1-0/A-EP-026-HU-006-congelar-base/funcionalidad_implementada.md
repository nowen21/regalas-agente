# Funcionalidad implementada · Fase `A-EP-026-HU-006-congelar-base` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-006-congelar-base` |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`base/`, `VERSION` y `CHANGELOG.md` quedaron quietos: el freno no deja escribirlos en la carpeta del estándar y el control del commit no los deja pasar. El estándar se cambia en la pantalla o se propone con `proponer`. Un cambio de `plantillas/` sigue en git y su versión se registra en la base con `registrar_version`. El agente lee las reglas completas con `ver_estandar`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Desde `proyectos/cimiento/`: `manage.py congelar_base` (y `--deshacer`) y `manage.py registrar_version --obliga si|no --agrega si|no --motivo …`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La marca es un ajuste común y congelar alinea la versión de la base con `VERSION` | Una sola fuente; el número sigue en la base sin retroceder | S-340 |

## 6. Deuda técnica y pendientes generados

El aviso de `ver_estandar` ocupa bytes en cada mensaje: con el mismo tope caben menos reglas completas.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ya corrió en esta máquina: `manage.py congelar_base`. El estándar quedó en la 56.8.1.
