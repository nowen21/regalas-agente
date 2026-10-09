# Funcionalidad implementada · Fase `A-EP-029-HU-004-sin-copia-local` (módulo Proyectos de Cimiento: `core/proyectos/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-004-sin-copia-local` |
| **Módulo** | Proyectos de Cimiento: `core/proyectos/`, con su ayuda y el instalador |
| **Especificación del módulo** | Los CA de la [HU-004](../HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-004 (CA-01, CA-02) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cimiento ya no escribe `.agente/configuracion.md` al guardar un proyecto, la configuración común o una suspensión: se quitaron `core/proyectos/copia.py` y sus cuatro llamadas. La ayuda dice que cada proyecto consulta su configuración en Cimiento. Volver a instalar Cimiento en un proyecto borra la copia que quedó.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Vista y ayuda | `core/proyectos/views.py`, `core/ayuda/textos.py`, `core/ayuda/templates/ayuda/secciones/` | Hecho | CP-001 |
| CA-02 | Instalador | `Instalador.quitar_copia_de_configuracion` en `core/herramientas/instalar.py` | Hecho | CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No hay nada que usar: la configuración se ve y se cambia en «Proyectos» → «Editar» y en «Configuración común». La copia vieja se va al volver a instalar el proyecto.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La copia vieja la borra el instalador | Volver a instalar ya es obligatorio con esta épica; se descartó una orden aparte | Ninguna |

## 6. Deuda técnica y pendientes generados

Se paga: la copia que nadie leía.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Las secciones «Configuración» y «Registrar» del manual.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Volver a instalar cada proyecto.
