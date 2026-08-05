# Pendiente · Versión del estándar

**Estado:** abierto · anotado 2026-08-04.

Declarar una **versión del estándar** y que cada proyecto fije la que sigue. Hoy `base/` cambia y no queda rastro de qué versión siguió un proyecto que cerró fases hace meses.

## El problema

Cambias una regla en `base/09-git.md`. A partir de ese momento:

- Los proyectos vivos empiezan a seguir la regla nueva **sin aviso** — a mitad de un módulo, con fases ya cerradas bajo la anterior.
- Nadie sabe si las fases viejas siguen siendo válidas o quedaron incumplidas retroactivamente.
- Una auditoría de un proyecto cerrado no tiene contra qué contrastarlo: `git log` de este repo tiene la historia, pero el proyecto no apunta a ningún punto de ella.

## Qué cubriría

- **Versión declarada** — un `VERSION` en la raíz del estándar, con semántica clara sobre qué es cambio mayor (una regla nueva que obliga) vs menor (redacción, ejemplos).
- **Fijación por proyecto** — el `CLAUDE.md` del proyecto registra la versión adoptada y la fecha.
- **CHANGELOG del estándar** — qué cambió y, sobre todo, **si obliga a migrar** o solo aplica de aquí en adelante.
- **Regla de retroactividad** — por defecto, un cambio de norma **no invalida** fases ya cerradas; las cerradas quedan selladas con su versión. Lo contrario sería reabrir trabajo terminado cada vez que se afina una redacción.
- **Aviso de desfase** — al abrir una fase, si la versión del proyecto está por detrás, decirlo (no migrar solo).

## Por qué importa

Sin esto, "el proyecto cumple el estándar" es una frase sin fecha — no se puede verificar ni defender ante nadie. Con esto, cumplir pasa a ser un hecho comprobable: *versión X, sellada tal día*.

## Relación con otros pendientes

Un validador del [01 · validadores y hooks](01-validadores-y-hooks.md) puede comprobar el desfase automáticamente al abrir fase — por eso conviene que el 01 ya esté hecho.
