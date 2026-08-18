# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-el-checklist-de-la-regla-y-la-carpeta-de-identidad.md](../../2026-08-07-el-checklist-de-la-regla-y-la-carpeta-de-identidad.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).
>
> **Tuvo una copia.** `2026-08-07-analisis-cumplimiento-reglas.md` repetía a mano sus primeros doce intercambios. Se borró el 2026-08-16; sigue en el historial de git.

**Viene de:** —, es trabajo nuevo.

**Propósito:** medir cuánto cumplen las reglas del estándar sus propias meta-reglas, y dejar la forma de volver a medirlo.

---

## Hallazgos de esta sesión

### H-1 · Nadie había medido si las reglas cumplen las meta-reglas

- **Qué pasó:** el usuario pidió el análisis de todas las reglas del agente contra el capítulo 20. Salió el informe de las 170 reglas, en una carpeta nueva.
- **Por qué importa:** el capítulo 20 se había escrito **describiendo** lo que la base ya hacía, así que se daba por hecho que se cumplía. Medirlo mostró cuánto no.
- **Qué lo soluciona:** un informe fechado, que es una foto y no un documento vivo.
- **Qué se decidió:** el informe vive en `analisis/`. Y una regla de trato que el usuario repitió dos veces: **el informe no se corrige, solo se le agrega el enlace a donde se corrigió.** Es un registro de lo que se encontró ese día; editarlo borra la evidencia.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** el informe en `analisis/`, y hoy el [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que cuenta lo que sigue sin cerrar.
- **Nace en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Cerrado en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Con qué se retoma:** —.

### H-2 · No había forma de saber si una regla ya fue evaluada

- **Qué pasó:** el usuario lo planteó al revés de como el agente lo estaba haciendo: *«el checklist debe estar en la regla, con el fin de que si se vuelve a correr un análisis no se vuelvan a analizar esas reglas»*. Y después precisó el reparto, porque el agente lo había entendido a medias dos veces.
- **Por qué importa:** un análisis que hay que rehacer entero cada vez no se rehace nunca. El sello dentro de la regla es lo que permite saltarse lo ya revisado.
- **Qué lo soluciona:** dos piezas separadas. **El checklist es el estándar** y vive una sola vez, hermano del capítulo, en `20-meta-reglas/checklist.md`; **el sello es la evaluación** y vive dentro de cada regla, con la versión contra la que se aplicó y la fecha.
- **Qué se decidió:** eso, y que en el sello cada meta-regla nombrada vaya enlazada — *«si quiero saber qué dice esa regla, poder ir a ella»*. Abrirla en otra pestaña no se pudo: markdown no lo permite.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/20-meta-reglas/checklist.md](../../../base/20-meta-reglas/checklist.md) y el bloque de checklist al final de cada regla.
- **Nace en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Cerrado en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Con qué se retoma:** —.

### H-3 · El agente hizo otra cosa y hubo que hacerle repetir la instrucción

- **Qué pasó:** *«no entiendo qué fue lo que hizo, porque no hizo lo que le pedí. Dígame lo que le pedí»*. Hicieron falta cuatro mensajes más —*«deje el checklist en reglas»*, *«perdón, como hermano de base»*, *«el sello va dentro de cada regla pero el checklist va como hermano de base»*— para que quedara claro.
- **Por qué importa:** el agente construyó sobre su propia interpretación en vez de preguntar. Cuando la instrucción se entiende a medias, lo barato es repetirla; lo caro es lo que se construyó encima.
- **Qué lo soluciona:** que el agente diga qué entendió **antes** de construir.
- **Qué se decidió:** el agente reformuló el pedido con las palabras del usuario y rehízo el trabajo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** en ninguna parte. Ocho días después el mismo problema, visto desde el otro lado, deja el [pendiente 24](../../../pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md).
- **Nace en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Cerrado en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Con qué se retoma:** —.

### H-4 · No existía la regla que dice cómo nace una regla

- **Qué pasó:** el usuario preguntó *«¿cuál es la regla que crea reglas?»*. El capítulo 20 tenía el procedimiento escrito al final, como prosa, y ninguna regla que obligara a seguirlo.
- **Por qué importa:** un procedimiento que no es regla se salta sin incumplir nada — y de hecho se venía saltando: había reglas publicadas sin checklist.
- **Qué lo soluciona:** una regla nueva que cierre el procedimiento con el checklist en CUMPLE.
- **Qué se decidió:** nace [`M14 · Ninguna regla nace fuera del procedimiento`](../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md): sin ese cierre la regla no se publica, se corrige o se retira.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`M14`](../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).
- **Nace en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Cerrado en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Con qué se retoma:** —.

### H-5 · El capítulo 20 no se cumplía a sí mismo

- **Qué pasó:** el usuario lo preguntó directo: *«¿o sea, 20 no se cumple a sí mismo?»*. No: sus propias reglas vivían dentro de `base.md` en vez de una por archivo, y ninguna tenía checklist.
- **Por qué importa:** el capítulo que define cómo son las reglas era el que menos las seguía. Mientras eso pase, el estándar enseña lo contrario de lo que pide.
- **Qué lo soluciona:** bajar sus reglas a `reglas/`, aplicarles `M14` y dejar en `base.md` solo lo que las explica.
- **Qué se decidió:** se hizo. El capítulo `00 · Identidad y rol` recibió el mismo trato en la misma sesión.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/20-meta-reglas/base.md/](../../../base/20-meta-reglas/base.md) y [base/00-identidad-y-rol/base.md/](../../../base/00-identidad-y-rol/base.md). Lo que quedó sin cerrar se cuenta hoy en el [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md): 129 reglas sin checklist y 7 publicadas en «no cumple».
- **Nace en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Cerrado en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Con qué se retoma:** —.

### H-6 · «Suba todo menos lo que dependa de los cambios en base»

- **Qué pasó:** el usuario puso el límite del commit él mismo, dos veces en el día: primero *«suba todo menos lo que dependa de los cambios realizados en base»*, y más tarde *«no toque lo de las otras sesiones ya que queda mal versionado»*.
- **Por qué importa:** es la frase que después se vuelve regla de trabajo. El motivo lo dio el usuario, no el agente: **queda mal versionado**.
- **Qué lo soluciona:** montar solo lo de la sesión.
- **Qué se decidió:** se subió por partes.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [no tocar el trabajo de otras sesiones](../../memory/no-tocar-trabajo-de-otras-sesiones.md).
- **Nace en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Cerrado en:** 2026-08-07 · el checklist de la regla y la carpeta de identidad.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los seis |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ el usuario aprobó y se subió por partes |
