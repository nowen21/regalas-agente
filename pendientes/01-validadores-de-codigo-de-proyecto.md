# Pendiente · Validadores de código de proyecto

**Estado:** abierto · anotado 2026-08-04 · núcleo cerrado 2026-08-05.

| | |
|---|---|
| **Historia de usuario** | No es un ítem, es un tema. Cada uno de los nueve validadores que faltan nombra su historia en la tabla de «Qué falta»; ninguno se construye desde acá. |

Extender la capa de **verificación mecánica** del estándar a lo que vive **dentro del código de un proyecto**: los validadores que no se pueden construir "en seco" sobre el estándar porque necesitan inspeccionar código/config o correr una herramienta instalada (linter, pruebas, audit).

> **Casi cerrado** — hooks activos y ~50 reglas con validador (137 pruebas verdes): documentación/estructura, código del proyecto, herramientas del stack y documentación de flujo. Se registra en [pendientes/hecho/validadores-y-hooks.md](hecho/validadores-y-hooks.md). Quedan **~9**: 4 fuzzy o pesadas y 5 que necesitan que el proyecto declare su convención/dominio (ver abajo).

## El principio que lo ordena

Una regla vive en **un solo lugar**: el `.md`. El validador **no la reescribe**, solo la hace cumplir. Si la regla se duplica en código, tarde o temprano el `.md` dice una cosa y el `.py` otra.

Criterio para decidir qué se automatiza:

> Si dos personas pueden discutir si se cumplió → se queda en `.md` (lo interpreta el agente).
> Si un script puede decir sí/no sin opinar → validador.

## Qué falta cubrir

Todo lo de aquí necesita un **proyecto real** más allá de su documentación —inspeccionar el código/config o correr una herramienta instalada— por eso no se pudo construir "en seco" sobre el estándar. Se va sumando apuntando a agro-system o rni.

**Cada uno nombra su historia.** Ninguno se construye desde este archivo: se baja a la historia de la columna y se construye como fase suya ([`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)). Este archivo reserva el lugar del tema en la fila; no es el plan de ninguno.

**Fuzzy o pesadas** (necesitan diseño extra, riesgo de falsos positivos):

| Qué falta | Historia donde vive |
|---|---|
| **`F2` · puertas del flujo** — que no haya código de una fase sin su spec y su plan. Requiere **cruzar el código de la fase con su spec**, no solo su carpeta de documentación. Es el más pesado | [EP-004 · HU-013 — Comparar el plan con lo hecho](../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md) |
| **`F4.4`** — cada intervención del plan referencia un CA (mapear intervención→CA dentro del plan) | [EP-004 · HU-013 — Comparar el plan con lo hecho](../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md) |
| **`DOC7`** — cruce bidireccional A↔B en el historial cruzado de fases complementarias (narrativa) | [EP-004 · HU-005 — Enlaces y citas](../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md), su `RN-05` |
| **`DOC14`-formato** — link de dos partes con texto = ruta absoluta. Forzarlo marca todo link de texto descriptivo → alto FP | [EP-004 · HU-005 — Enlaces y citas](../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md), su `RN-03`. Su deuda de texto es el [18](18-los-enlaces-del-estandar-no-cumplen-doc14.md) |

**Necesitan que el proyecto declare su convención/dominio en `.agente/`:**

| Qué falta | Historia donde vive |
|---|---|
| **`EST1`** (ubicación de módulos) y **resto de `EST2`** (nombres) — contra la convención declarada | [EP-004 · HU-006 — Nomenclatura y estructura](../documentacion/epicas/EP-004-comprobacion-automatica/HU-006-nomenclatura-y-estructura/HU-006-nomenclatura-y-estructura.md) |
| **resto de `D1`** (columnas de auditoría, `UNIQUE`, índices) — qué tablas son de dominio, no framework | [EP-004 · HU-010 — Convención declarada por el proyecto](../documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/HU-010-convencion-declarada-por-el-proyecto.md) |
| **`IM2`/`IM5`** (estados y permiso de anulación) — qué entidades son inmutables | [EP-004 · HU-010 — Convención declarada por el proyecto](../documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/HU-010-convencion-declarada-por-el-proyecto.md) |
| **La precondición del grupo:** cómo el proyecto declara su convención y sus entidades en `.agente/`, en un formato mínimo que un programa pueda leer | [EP-004 · HU-010 — Convención declarada por el proyecto](../documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/HU-010-convencion-declarada-por-el-proyecto.md) |

> Sin esa precondición no hay contra qué comparar, y por eso los tres de arriba esperan. El inventario regla por regla está en [validadores/reglas-validables.md](../validadores/reglas-validables.md).

## Forma (ya establecida)

```
base/*.md            ← la norma (fuente de verdad, versionada)
validadores/*.py     ← comprueban lo comprobable
.githooks + .claude  ← disparan los validadores en el momento correcto
```

Cada validador: entrada explícita, salida sí/no + lista de incumplimientos con `archivo:linea`. Sin efectos secundarios: reportan, no arreglan. Lo que se sume debe seguir esta forma.

## Por qué importa

Es la brecha entre **"el estándar dice"** y **"el estándar se cumple"**. Todo lo demás del backlog agrega cobertura; esto agrega **garantía** sobre la cobertura que ya existe.

## Relación con otros pendientes

- Los validadores son el consumidor natural del [03 · ciclo de vida de pendientes](hecho/ciclo-de-vida-de-pendientes.md) (ya hecho): comprobar que todo `§Fuera-de-scope` tenga su señal registrada es uno de los validadores fuzzy que quedan (cruzar spec↔señales, como `F2`).
- Alimentan las [06 · métricas del proceso](hecho/metricas-del-proceso.md) (ya hecho): contar los hallazgos de validador por regla es "las puertas que fallan" — es la extensión anotada en `metricas/README.md`.
