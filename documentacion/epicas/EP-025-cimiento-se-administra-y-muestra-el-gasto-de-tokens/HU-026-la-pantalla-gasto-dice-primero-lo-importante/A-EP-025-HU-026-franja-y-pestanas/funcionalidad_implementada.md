# Funcionalidad implementada · Fase `A-EP-025-HU-026-franja-y-pestanas` (módulo Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-026-franja-y-pestanas` |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-026](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-026 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La pantalla «Gasto» muestra arriba la franja con el total del período y su variación frente al tramo anterior cortado a la misma hora, las llamadas, el % de caché releída y el contexto máximo. Debajo, cinco pestañas que se piden solo al abrirlas: Resumen, Dónde se gasta, Contexto, Ahorro y Actividad. Salen la gráfica «Por proyecto», la tabla por tipo de token y el refresco cada 10 segundos: se actualiza con el botón ↻ hasta la HU-027.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 9 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `tests_segunda_tanda.py` y `tests_tercera_tanda.py`, que pedían `/gasto/datos/`; el usuario aprobó ampliar el plan el 2026-10-06 y quedaron en su tabla 2.1.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Gasto» en el menú de la izquierda. Las pestañas se recuerdan en la dirección con `?pestana=`, y «Dónde se gasta» con `&agrupar=`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La hora se muestra fija, «Actualizado a las HH:MM:SS» | Contar segundos en la pantalla sería un reloj, y el acuerdo 4 los descarta | Plan §2.6 |

## 6. Deuda técnica y pendientes generados

El dibujo de las gráficas y el botón ↻ no se vieron en un navegador; los ve el usuario al abrir la pantalla. La falta de matriz de dependencias completa dejó dos pruebas fuera del plan: lección S-320.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Fila de la HU-026 en la épica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega con la actualización de Cimiento; basta recargar la pantalla.
