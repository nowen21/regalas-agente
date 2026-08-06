# Pendiente · Validadores de código de proyecto

**Estado:** abierto · anotado 2026-08-04 · núcleo cerrado 2026-08-05.

Extender la capa de **verificación mecánica** del estándar a lo que vive **dentro del código de un proyecto**: los validadores que no se pueden construir "en seco" sobre el estándar porque necesitan inspeccionar código/config o correr una herramienta instalada (linter, pruebas, audit).

> **Casi cerrado** — hooks activos y ~50 reglas con validador (137 pruebas verdes): documentación/estructura, código del proyecto, herramientas del stack y documentación de flujo. Se registra en [hecho/validadores-y-hooks.md](hecho/validadores-y-hooks.md). Quedan **~9**: 4 fuzzy o pesadas y 5 que necesitan que el proyecto declare su convención/dominio (ver abajo).

## El principio que lo ordena

Una regla vive en **un solo lugar**: el `.md`. El validador **no la reescribe**, solo la hace cumplir. Si la regla se duplica en código, tarde o temprano el `.md` dice una cosa y el `.py` otra.

Criterio para decidir qué se automatiza:

> Si dos personas pueden discutir si se cumplió → se queda en `.md` (lo interpreta el agente).
> Si un script puede decir sí/no sin opinar → validador.

## Qué falta cubrir

Todo lo de aquí necesita un **proyecto real** más allá de su documentación —inspeccionar el código/config o correr una herramienta instalada— por eso no se pudo construir "en seco" sobre el estándar. Se va sumando apuntando a agro-system o rni.

**Fuzzy o pesadas** (necesitan diseño extra, riesgo de falsos positivos):

- **`F2` · puertas del flujo** — que no haya código de una fase sin su spec y su plan. Requiere **cruzar el código de la fase con su spec**, no solo su carpeta de documentación. Es el más pesado.
- **`F4.4`** — cada intervención del plan referencia un CA (mapear intervención→CA dentro del plan).
- **`DOC7`** — cruce bidireccional A↔B en el historial cruzado de fases complementarias (narrativa).
- **`DOC14`-formato** — link de dos partes con texto = ruta absoluta. Forzarlo marca todo link de texto descriptivo → alto FP.

**Necesitan que el proyecto declare su convención/dominio en `.agente/`:**

- **`EST1`** (ubicación de módulos) y **resto de `EST2`** (nombres) — contra la convención declarada.
- **resto de `D1`** (columnas de auditoría, `UNIQUE`, índices) — qué tablas son de dominio, no framework.
- **`IM2`/`IM5`** (estados y permiso de anulación) — qué entidades son inmutables.

> Precondición para este grupo: definir **cómo** el proyecto declara su convención/entidades en `.agente/` (un formato mínimo, machine-readable). Sin eso no hay contra qué comparar. El inventario regla por regla está en [validadores/reglas-validables.md](../validadores/reglas-validables.md).

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
