# Pendiente · Validadores de código de proyecto

**Estado:** abierto · anotado 2026-08-04 · núcleo cerrado 2026-08-05.

Extender la capa de **verificación mecánica** del estándar a lo que vive **dentro del código de un proyecto**: los validadores que no se pueden construir "en seco" sobre el estándar porque necesitan inspeccionar código/config o correr una herramienta instalada (linter, pruebas, audit).

> **La base ya está hecha** — hooks activos y ~22 reglas con validador que corren sobre la documentación y la estructura (62 pruebas verdes). Se registra en [hecho/validadores-y-hooks.md](hecho/validadores-y-hooks.md). Este pendiente es **lo que queda**: la mitad más pesada, con riesgo de falsos positivos, que se va sumando apuntando a un proyecto real (agro-system o rni).

## El principio que lo ordena

Una regla vive en **un solo lugar**: el `.md`. El validador **no la reescribe**, solo la hace cumplir. Si la regla se duplica en código, tarde o temprano el `.md` dice una cosa y el `.py` otra.

Criterio para decidir qué se automatiza:

> Si dos personas pueden discutir si se cumplió → se queda en `.md` (lo interpreta el agente).
> Si un script puede decir sí/no sin opinar → validador.

## Qué falta cubrir

Todo lo de aquí necesita un **proyecto real** más allá de su documentación —inspeccionar el código/config o correr una herramienta instalada— por eso no se pudo construir "en seco" sobre el estándar. Se va sumando apuntando a agro-system o rni.

- **Puertas del flujo** (`02·F2`) — que no haya código de una fase sin su spec acordada y su plan de trabajo. Requiere leer el código de la fase, no solo su carpeta de documentación.
- **Precondiciones de cierre** (`cerrar-fase`) — pruebas ejecutadas, checklist de trazabilidad marcado.
- **Trazabilidad hasta el commit** — el tramo documentación→commit (la parte épica↔HU/ORIGEN/tabla ya la hace `trazabilidad.py`).
- **Los ~38 validadores de código/config/herramienta** — linter (`Q6`), pruebas (`T5`), audit de dependencias (`DEP3`), esquema/migraciones (`D1`–`D3`), heurísticas de seguridad y rendimiento (`S3`, `R1`, `R2`)… El inventario regla por regla, con su estado, está en [validadores/reglas-validables.md](../validadores/reglas-validables.md).

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

- Los validadores son el consumidor natural del [03 · ciclo de vida de pendientes](03-ciclo-de-vida-de-pendientes.md) (avisar de deuda abierta al abrir fase).
- Alimentan las [06 · métricas del proceso](06-metricas-del-proceso.md): cada fallo de validador es un dato.
