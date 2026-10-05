# Pendiente: nadie ve cuántos tokens se gastan ni puede ajustar las reglas sin tocar código

| | |
|---|---|
| **De dónde sale** | [H-1 · Nadie ve cuántos tokens se gastan ni puede ajustar las reglas sin tocar código](../../sesion-2.md), en el resumen de la sesión del 2026-10-04, versión 2 según el [análisis 1](analisis-1.md) |

## El problema

Cimiento no tiene administración ni muestra el gasto de tokens. Falta correr sobre MariaDB `cimiento`, con pantallas propias y entrada con usuario; registrar los proyectos; fijar por proyecto el nivel de cada regla (frena, avisa o apagada) y que el freno lo lea de la base; guardar el gasto por proyecto, sesión, enganche, archivo leído y los demás niveles; verlo en vivo, y avisar cuando un enganche o un archivo pasa de su límite.

Los datos del gasto ya existen: Claude Code anota cada llamada en los `.jsonl` de `~/.claude/projects/<proyecto>/` y puede mandarla por telemetría. En la sesión `b931dba0`, medida el 2026-10-04, hubo 1012 llamadas y unos 450 000 tokens releídos por llamada.

## Por qué importa

Sin medir no se sabe qué automatizar primero, y Claude Code borra los `.jsonl` a los 30 días. Sin niveles por proyecto, cada ajuste de una regla es un cambio de código que afecta a todos, y una regla fija puede bloquear a Cimiento para corregirse, como pasó el 2026-10-04.
