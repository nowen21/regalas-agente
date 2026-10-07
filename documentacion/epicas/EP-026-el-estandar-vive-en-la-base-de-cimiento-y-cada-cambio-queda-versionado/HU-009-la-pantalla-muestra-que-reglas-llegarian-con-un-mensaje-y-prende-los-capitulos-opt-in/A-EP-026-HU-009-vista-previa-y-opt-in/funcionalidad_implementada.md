# Funcionalidad implementada · Fase `A-EP-026-HU-009-vista-previa-y-opt-in` (módulo Proyectos y Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-009-vista-previa-y-opt-in` |
| **Módulo** | Proyectos y Estándar en la base, `proyectos/cimiento/core/proyectos/` y `core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-009](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-009 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Los capítulos opt-in (15, 16, 17, 18, 19, 21 y 22) se prenden o apagan en «Proyectos» → «Editar», para un proyecto, o en «Configuración», para todos; de fábrica están apagados. Las reglas de un proyecto registrado se eligen con lo que diga la base; uno sin registro sigue con su `CLAUDE.md`. Al migrar, cada proyecto pasó a la base lo que decía su `CLAUDE.md`, y lo que no nombraba quedó en «sí». En «Estándar» → «Vista previa» se ve qué reglas llegarían con un mensaje en un proyecto.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): `core/ayuda/textos.py`, que se agregó al plan antes de tocarlo

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Estándar» → «Vista previa»; los opt-in, en «Proyectos» → «Editar» y en «Configuración».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lo que el `CLAUDE.md` no nombra pasa a la base en «sí» | Así regía; en «no», al estándar mismo se le apagaban los siete | S-343 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar `manage.py migrate proyectos` (hecho en esta máquina el 2026-10-06, con 84 ajustes).
