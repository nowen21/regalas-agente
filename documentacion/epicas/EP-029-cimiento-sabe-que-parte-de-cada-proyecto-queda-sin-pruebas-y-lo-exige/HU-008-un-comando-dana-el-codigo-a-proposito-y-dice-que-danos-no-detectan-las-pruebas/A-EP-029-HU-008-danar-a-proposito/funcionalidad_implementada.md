# Funcionalidad implementada · Fase `A-EP-029-HU-008-danar-a-proposito` (módulo Pruebas de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-008-danar-a-proposito` |
| **Módulo** | Pruebas de Cimiento, `proyectos/cimiento/core/pruebas/` |
| **Especificación del módulo** | Los CA de la [HU-008](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-008 () |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`manage.py danar_a_proposito --danos «json» --pruebas "«orden»" [--raiz «carpeta»] [--tiempo 600]` daña el código según una lista, corre las pruebas con cada daño y dice cuáles detectaron y cuáles no. Antes de empezar exige que las pruebas pasen sin daños; devuelve cada archivo desde su copia aunque algo falle, borra lo que el daño escribió y al final comprueba que todo quedó igual y que las pruebas vuelven a pasar.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


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

Se escribe la lista de daños en un JSON:

```json
[{"nombre": "la suma resta", "archivo": "app/suma.py", "antes": "return a + b", "despues": "return a - b"}]
```

Y desde `proyectos/cimiento/`: `python manage.py danar_a_proposito --danos danos.json --pruebas "python -m pytest" --raiz «carpeta del proyecto»`. Cada `antes` tiene que aparecer una sola vez en su archivo.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La lista de daños es un JSON | Guarda textos de varias líneas sin inventar reglas de escape; se descartó un formato propio por bloques | — |
| Se detecta por el código de salida de la orden | Vale para cualquier lenguaje; leer «OK» falló antes (`S-060`, `S-068`) | — |
| Cada daño le cambia la hora al archivo | Sin eso, Python corre el `.pyc` viejo | `S-362` |
| Si se pasa del tiempo, se mata la orden con todo lo que abrió (`taskkill /T` o el grupo de procesos) | Matar solo la consola dejaba vivas las pruebas | — |

## 6. Deuda técnica y pendientes generados

Lo que borra se decide comparando qué archivos hay antes y después de cada daño: si algo externo escribe en la carpeta mientras corre, también se borra. El comando lista todo lo que borró.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La HU-008 en la tabla de la EP-029 y en su hoja de ruta; el README de la carpeta de la HU.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega a los proyectos con Cimiento.
