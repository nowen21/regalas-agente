# Pendiente · Los enlaces del estándar no cumplen su propia regla

**Estado:** abierto · anotado 2026-08-14.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-005 — Comprobar los enlaces y las citas a reglas](../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md) — es la deuda de su RN-03, que es DOC14 palabra por palabra |

## El problema

[`13·DOC14`](../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) pide que el texto de un enlace sea la ruta completa desde la raíz y el destino la ruta relativa. Al escribir el validador de ese formato aparecieron **354 enlaces** del propio estándar que no lo cumplen.

No son falsos positivos. Son enlaces cuyo texto dice el nombre del archivo pero no dónde vive: `[00-nucleo-blindado.md]` en vez de `[base/00-nucleo-blindado.md]`.

| Dónde | Cuántos |
|---|---|
| `prompts/` | 106 |
| `base/` | 45 |
| `historico-chat/` | 43 |
| `documentacion/` | 42 |
| `validadores/` | 40 |
| `notas/` | 30 |
| El resto | 48 |

## Qué falta

**1. Decidir el alcance.** Las transcripciones de `historico-chat/` se copian literales del chat, así que ahí el formato no aplica. Los de `prompts/` son palabras del usuario. Quedan unos 200 reales.

**2. Corregirlos.** Es mecánico: el validador ya dice, enlace por enlace, qué texto debería tener.

**3. Decidir si el validador entra en la corrida de todos los días.** Hoy se corre aparte, porque 354 avisos sepultan cualquier otra cosa.

## El límite

El validador solo mira el enlace cuyo texto ya tiene forma de ruta. El de texto descriptivo no se toca: la propia regla lo permite.

## De acá nació [`02·F21`](../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md)

Este pendiente se estaba usando como permiso. El 2026-08-14, con los 354 ya contados, los documentos escritos ese mismo día sumaron 122 incumplimientos nuevos de la misma familia: la deuda dejaba de ser deuda y pasaba a ser costumbre.

De ahí salió la regla: **desde que un incumplimiento queda registrado, lo que se escriba de ahí en adelante nace cumpliendo.** El usuario lo dijo así: *"yo antes escribía sin ortografía, pero a partir de que aprendí ya escribo con ortografía, no importa el contexto"*.

Para este pendiente eso significa dos cosas:

- **La cuenta ya no crece.** Los 354 son los de antes del 2026-08-14; si aparecen más, no es deuda vieja, es un incumplimiento nuevo de `F21`.
- **Limpiarlos sigue siendo trabajo aparte**, y es lo que este pendiente guarda.
