# Pendiente · El estándar no tiene planteamiento

**Estado:** cerrado el 2026-08-22, versión 30.6.1 · anotado 2026-08-16.

| | |
|---|---|
| **Historia de usuario** | [EP-003 · HU-002 — Modelos del encargo](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) — el planteamiento es uno de los modelos del encargo; lo que falta es llenarlo para esta casa |
| **De dónde sale** | El hallazgo H-13 del [resumen de la sesión 7](../../historico-chat/resumenes/2026-08-16/sesion-7.md) |
| **Lo destapó** | El punto de la cadena que nació al cerrar el [30](la-revision-ve-la-cadena.md) (v23.0.0) |

## El problema

La revisión de instalación, corrida contra esta casa el 2026-08-16:

```
cadena -> FALTA | no hay ningún planteamiento en `prompts/`
```

`prompts/` tiene cuarenta archivos y **ninguno es un planteamiento**. `02·F0` arranca ahí, y el trabajo del estándar también es desarrollo.

## Cómo leerlo sin sacar la conclusión equivocada

La misma corrida dice «6 de 14», y ese número **no significa lo mismo que en un proyecto**: el estándar no se instala a sí mismo, así que ocho de esos puntos —el `CLAUDE.md` heredado, los archivos de `.agente/`, los enganches— no le aplican.

El de la cadena **sí** le aplica, y es el único de los ocho que reprueba con razón.

## Por qué no se resolvió al destaparlo

Escribir el planteamiento de este repositorio es **decidir qué es este proyecto**: qué problema resuelve, para quién, qué queda fuera. Eso no es una tarea de código que el agente cierre por su cuenta — es exactamente el documento que `02·F0` pone primero porque nadie más lo puede escribir.

## Qué falta

Escribirlo en `prompts/<slug>-planteamiento.md`, desde [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../plantillas/ciclo-vida-proyectos/01-planteamiento.md). Sale de una conversación, no de leer el repositorio.

**Ojo con el atajo:** reconstruirlo leyendo lo que el estándar ya hace produciría un planteamiento que describe la solución en vez del problema, y eso es peor que no tenerlo — apagaría el aviso sin arreglar nada.

## Con qué se cruza

Con el punto 8 del [33](../33-defectos-que-destaparon-los-resumenes-viejos.md), donde ya está preguntado si las fases de EP-001 son plan o retrodocumentación. Las dos preguntas son la misma: **este repositorio se documentó hacia atrás, y nunca escribió por qué existe.**

## Cómo cerró

El usuario decidió que las tres preguntas (qué problema, para quién, qué queda fuera, qué es éxito) se contestaran «con lo que ya se tiene del proyecto». Se escribió [../prompts/cimiento-planteamiento.md](../../prompts/cimiento-planteamiento.md) desde el README, los pedidos en `prompts/` y la dirección del usuario del 2026-08-21 (citada con sus palabras), evitando el atajo que este pendiente advertía: describe el problema (sesiones que reinventan, olvidan y arriesgan) y el criterio de éxito medible, no la solución. Y como `02·F26` lo exige a todos desde la 29.0.0, nació también el [inventario de funcionalidades de Cimiento](../../prompts/cimiento-inventario-funcionalidades.md), en revisión del usuario: 22 ítems existentes, 4 por construir, 3 por confirmar. La revisión de instalación de esta casa pasa a ver la cadena.

## Cómo se sabrá que cerró

La revisión dice «14 de 14» en esta casa, y el planteamiento se puede leer sin haber visto el código.
