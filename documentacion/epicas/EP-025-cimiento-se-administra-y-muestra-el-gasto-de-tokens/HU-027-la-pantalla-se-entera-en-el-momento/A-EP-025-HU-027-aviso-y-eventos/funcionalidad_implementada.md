# Funcionalidad implementada · Fase `A-EP-025-HU-027-aviso-y-eventos` (módulo Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-027-aviso-y-eventos` |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-027](../HU-027-la-pantalla-se-entera-en-el-momento.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-027 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.5.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cuando el vigilante guarda algo nuevo, avisa a Cimiento con un `POST` local; Cimiento pasa el aviso por SSE a cada pantalla «Gasto» abierta, y la pantalla vuelve a pedir la franja y la pestaña abierta, que salen de la base. No hay ningún intervalo; con Cimiento apagado el aviso se pierde sin daño.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Gasto» se actualiza sola. El aviso es `POST /gasto/aviso/`, solo desde la misma máquina; los eventos, `GET /gasto/eventos/`, con cuenta.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| `EventSource` del navegador en vez de la extensión SSE de htmx | No suma bibliotecas y reusa el evento `actualizar` de la HU-026 | S-321 |

## 6. Deuda técnica y pendientes generados

Ver con los ojos la franja cambiando sola: queda para el usuario. Una conexión de eventos que el navegador cierra queda esperando hasta el próximo aviso, y ahí termina.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Fila de la HU-027 en la épica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Reiniciar Cimiento y el vigilante para que tomen el código nuevo.
