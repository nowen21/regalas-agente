# Pendiente · Ciclo de vida de pendientes y deuda técnica

**Estado:** abierto · anotado 2026-08-04.

Darle **cierre** a lo que el agente difiere. Hoy los pendientes de trabajo nacen dispersos y nadie los junta:

- `§Fuera-de-scope` del spec del módulo (`02` · F4.5).
- Los `gap-N` y los ítems del cierre de análisis (`02`).
- La tabla de decisiones de [plantillas/planes/trabajo.md](../plantillas/planes/trabajo.md).
- Señales de tipo `deuda-tecnica` y `pregunta-abierta` en `senales.db`.

El resultado: lo diferido se pierde salvo que alguien relea el spec completo.

## Por qué NO una carpeta de archivos

Un pendiente no es un documento, es un **estado que cambia**: nace abierto, alguien lo toma, se cierra. Un `.md` por pendiente da carpeta de zombis (cerrar = borrar a mano, se olvida), sin consulta posible ("¿qué queda abierto del módulo X?" = leer 40 archivos), duplicado respecto al spec y con conflictos de merge.

Aplica la regla del estándar: **lo que se decide y se discute → git; lo que se acumula y se consulta → DB.** El *porqué* del diferimiento es prosa y se queda en el spec; la **cuenta de qué sigue abierto** va en `senales.db`.

> Nota: este pendiente es sobre los pendientes **de un proyecto** (deuda diferida por el agente). La carpeta `pendientes/` de este repo es otra cosa: el backlog del estándar mismo, que sí es discusión y sí va en git.

## Qué cubriría

El tipo ya existe en [memoria/esquema.sql](../memoria/esquema.sql) (`deuda-tecnica`, `pregunta-abierta`). Falta el ciclo de vida:

```sql
-- estado: activa | reemplazada | revertida | cerrada
ALTER TABLE senales ADD COLUMN cerrada_en TEXT;   -- ISO date
ALTER TABLE senales ADD COLUMN cierra_ref TEXT;   -- commit / fase / HU que lo cerró
```

Y en `memoria.py`:

```
python memoria.py pendientes [--scope modulo:facturacion]
python memoria.py cerrar S-014 --ref "F3 / commit abc1234"
```

Enganches en el flujo (`02`):

- Al declarar algo en `§Fuera-de-scope`, **registrar la señal** — no basta con escribirlo en el spec.
- Al abrir una fase, **listar lo abierto del scope** antes de planificar.
- Al cerrar una fase, **cerrar lo que esa fase resolvió**, con referencia.

## Relación con otros pendientes

- Comparte migración de esquema con la [02 · vigencia y poda de la memoria](02-vigencia-y-poda-de-memoria.md) — diseñar los estados juntos, una sola vez. Por eso van seguidos.
- Los [01 · validadores](01-validadores-de-codigo-de-proyecto.md) pueden comprobar que todo `§Fuera-de-scope` tenga su señal registrada.
