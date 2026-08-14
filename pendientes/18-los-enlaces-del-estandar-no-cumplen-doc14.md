# Pendiente · Los enlaces del estándar no cumplen su propia regla

**Estado:** abierto · anotado 2026-08-14.

## El problema

`13·DOC14` pide que el texto de un enlace sea la ruta completa desde la raíz y el destino la ruta relativa. Al escribir el validador de ese formato aparecieron **354 enlaces** del propio estándar que no lo cumplen.

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
