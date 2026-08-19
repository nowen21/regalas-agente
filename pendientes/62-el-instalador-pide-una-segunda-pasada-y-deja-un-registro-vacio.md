# Pendiente · El instalador pide una segunda pasada y deja un registro vacío

**Estado:** abierto · anotado 2026-08-18 · sale de correr la instalación en `shopnest-mesa` para subir del `23.5.0` al `23.10.0`.

| | |
|---|---|
| **Historia de usuario** | EP-007 · la instalación idempotente que «no pregunta» y «comprueba el resultado al terminar» |
| **Proyecto de origen** | `shopnest-mesa` — reportado, no corregido acá (`02·F24`) |

## El problema

**El instalador escribe el registro de versión y, en la misma pasada, dice que falta.**

Primera corrida:

```
· sellar CLAUDE.md contra la plantilla (a5ceeb693286 → 7499949ecd72)
· el proyecto ya estaba en el registro central
· registrar documentacion\versiones\2026-08-18-23.10.0.md      ← lo escribe

  INSTALACIÓN INCOMPLETA · shopnest-mesa · 13 de 14 · falta: versiones
  - **versiones** — lo instalado dice `23.10.0` y el último registro
    dice `23.5.0`: falta registrar la actualización                ← y dice que falta
```

El archivo `2026-08-18-23.10.0.md` **quedó escrito en esa misma corrida**, con su tabla de componentes y la huella de `CLAUDE.md` antes y después. El checklist que corre al final no lo ve: sigue leyendo el estado de antes.

Segunda corrida, la que el propio mensaje recomienda:

```
· CLAUDE.md ya estaba sellado al día
· registrar documentacion\versiones\2026-08-18-23.10.0-2.md    ← un registro más

  Instalación del agente completa · shopnest-mesa · 14 de 14
```

## Qué deja

**Dos registros para una sola actualización**, y el segundo no registra nada:

| Archivo | Hora | Componentes actualizados |
|---|---|---|
| `2026-08-18-23.10.0.md` | 20:30:29 | `claude-md` · `a5ceeb693286 → 7499949ecd72` |
| `2026-08-18-23.10.0-2.md` | 20:30:36 | **«Ninguno cambió de huella: solo se refrescó la instalación»** |

Siete segundos de diferencia, la misma versión, y el segundo existe **solo para que el checklist se dé por satisfecho**.

## Por qué importa

1. **Contradice lo que el propio `CLAUDE.md` promete de la instalación:** *«Es idempotente: lo que ya está al día no se toca, no se duplica y no se pisa»*. Acá se duplica, y la duplicación la provoca el mensaje que pide correr otra vez.
2. **`documentacion/versiones/` se versiona en el repositorio** y es lo que se mira para saber bajo qué versión cerró cada fase. Un registro vacío entre los buenos obliga a abrir los dos para saber cuál cuenta.
3. **El instalador «no pregunta»**, pero acá sí pide algo: pide que lo vuelvan a correr. Y lo que pide no es una decisión del usuario — es trabajo que ya hizo.

## Qué se debe decidir

Dos salidas, y la primera parece la obvia:

| Salida | Qué implica |
|---|---|
| **Que el checklist final lea el estado después de aplicar** | Una corrida basta. El registro que acaba de escribirse cuenta como escrito, que es lo que es |
| Que el registro se escriba **antes** de la comprobación | Mismo efecto, distinto sitio en el código |

**Y en cualquiera de las dos, un detalle aparte:** si una corrida no cambió ninguna huella y la versión ya está registrada, **no debería escribir un registro nuevo**. Hoy escribe uno que dice «ninguno cambió de huella», y ese archivo no le sirve a nadie.

## Cómo se comprueba que quedó

En un proyecto con la versión atrasada, **una sola corrida** de `instalar.py --aplicar` deja:

- `Instalación del agente completa · N de N` al terminar, sin pedir una segunda pasada;
- **un** archivo en `documentacion/versiones/`, no dos;
- y una segunda corrida seguida **no escribe ningún registro nuevo**.

## Lo que este proyecto hizo mientras tanto

Los dos registros **se dejaron como están**. Los escribe el instalador y el estándar dice que no se editan a mano; borrar el segundo sería tapar el síntoma en el único sitio donde queda constancia de que pasó.
