# Pendiente · Nada hace cumplir `ID9`, y el proyecto no puede ponerle el enganche

**Estado:** abierto · anotado 2026-08-17.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-012 — Hacer cumplir lo que hoy solo se recuerda](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) — «una instrucción informa, un enganche ejecuta» es la frase de esa épica |
| **Proyecto de origen** | `shopnest-mesa` — `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **De dónde sale** | El hallazgo H-4 del resumen del 2026-08-17 de ese proyecto — `historico-chat/resumenes/2026-08-17/sesion.md` |
| **Seguimiento allá** | `pendientes/22-nada-hace-cumplir-id9.md` |

## El problema

[`ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) es núcleo y no se relaja. **Nada la mide y nada la hace cumplir.** Depende por completo de que el agente se acuerde, y eso no se cumple siempre — que es literalmente lo que el estándar ya escribió sobre el histórico en [`plantillas/historico-chat.md`](../plantillas/historico-chat.md):

> *una instrucción escrita **informa**, un enganche **ejecuta**.*

El histórico tiene su enganche. `ID9` no.

## La evidencia

En `shopnest-mesa` el usuario pidió «menos es más» **siete veces** en tres días: una el 2026-08-15, cinco el 2026-08-16 y una el 2026-08-17. Cada vez se anotó el caso en el recuerdo `respuestas-cortas.md` del proyecto, con el porqué y el ejemplo de lo que falló. **Anotarlo no cambió nada:** el registro se volvió el sustituto de cumplir la regla, y a la séptima el usuario lo dijo así — *«¿de qué le sirve anotarlo tanto si no lo está cumpliendo?»*.

Siete incumplimientos de una regla de núcleo, todos documentados, ninguno prevenido.

## Por qué el proyecto no lo puede arreglar

Los enganches viven en `.claude/settings.json`, que **lo escribe `validadores/instalar.py`** y está en el `.gitignore` del proyecto. Lo que un proyecto agregue ahí lo pisa la siguiente instalación, que es idempotente y regenera esa configuración. El canal es de cimiento; por eso llega acá y no se resuelve allá.

## El límite técnico, para que no se diseñe la pieza equivocada

**Un enganche `Stop` no puede acortar una respuesta ya emitida.** Cuando corre, el texto ya salió. Lo único que puede hacer es medirlo y **devolverlo** para que se reescriba, lo que le cuesta al usuario ver la respuesta larga primero y la corta después.

Las tres salidas que se ven, sin recomendación —la decisión es de cimiento—:

1. **`Stop` que rebota lo que pase de un umbral.** Ejecuta de verdad, pero el usuario ve las dos versiones. El umbral tendría que ser laxo (una respuesta larga a veces es correcta: `ID9` prohíbe la palabra que sobra, no la línea que hace falta) y por tanto atrapa poco.
2. **`UserPromptSubmit` que inyecta la regla en cada mensaje.** No ejecuta, informa — es lo que ya falló siete veces. Solo cambiaría el sitio del recordatorio.
3. **Medir y no bloquear:** el enganche registra el largo de cada respuesta y deja la serie a la vista. No previene, pero convierte «me parece que contesta largo» en un número, y un número sí se puede revisar en el cierre de la sesión.

La tercera es la única que no tiene el defecto de las otras dos. También es la que menos hace.

## Qué falta

Que cimiento decida si `ID9` se hace cumplir con una pieza o se asume que no se puede, **y lo escriba en la regla**. Hoy la regla no dice ninguna de las dos cosas, y esa es la parte que sí es un defecto: una regla de núcleo sin forma de cumplirse y sin decir que no la tiene.

## Con qué se cruza

Con el [36](hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md): las dos son reglas que existen en el papel y no tienen quién las ejecute.

## Cómo se sabrá que cerró

`ID9` dice cómo se comprueba —con enganche o declarando que no lo tiene—, y `shopnest-mesa` recibe el aviso para cerrar su 22.
