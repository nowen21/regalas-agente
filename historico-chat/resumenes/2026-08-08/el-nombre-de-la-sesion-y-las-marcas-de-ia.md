# 2026-08-08 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-08-el-nombre-de-la-sesion-y-las-marcas-de-ia.md](../../2026-08-08-el-nombre-de-la-sesion-y-las-marcas-de-ia.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).
>
> Empezó el 2026-08-08 a las 23:01 y siguió hasta el 2026-08-12. El resumen queda en el día en que empezó.

**Viene de:** —, es trabajo nuevo. La abre la idea 2 de la [libreta](../../../pendientes/10-ideas.md).

**Propósito:** que la sesión quede guardada con un nombre que diga de qué trató.

---

## Hallazgos de esta sesión

### H-1 · Ocho sesiones quedaron llamándose «sesión del 2026-08-07»

- **Qué pasó:** el usuario preguntó si al abrir una sesión se le puede pedir el nombre con el que se va a guardar. No: un `SessionStart` corre sin consola y no puede preguntar nada. Y aunque pudiera, al minuto cero **ninguno de los dos sabe de qué va a tratar**.
- **Por qué importa:** el nombre y su línea del índice son lo único que la próxima sesión ve de esta. Ocho sesiones ya habían quedado sin tema, y hoy son la mitad del histórico.
- **Qué lo soluciona:** proponer el nombre **después** del primer intercambio, cuando el tema ya está claro, y que el usuario apruebe.
- **Qué se decidió:** el enganche del mensaje del usuario recuerda **una sola vez** que hay que proponer nombre y resumen —nunca en el primer mensaje— y no renombra nada solo. El cambio lo hace `--renombrar`, que mueve el archivo, el título y la línea del índice a la vez: a mano se olvidaba el índice y quedaba apuntando a un archivo que ya no estaba. Versión **6.1.0**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`historico.py`](../../../validadores/historico.py) y [`hook_historico.py`](../../../validadores/hook_historico.py), versión 6.1.0 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Cerrado en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Con qué se retoma:** —.

### H-2 · El nombre del archivo y el de la pestaña son dos cosas, y el agente dijo primero que no se podía

- **Qué pasó:** el usuario insistió en que la pestaña también mostrara el nombre. El agente había respondido que no existía forma de fijarlo; después se corrigió: **sí existe**, `claude --name` al arrancar y `/rename` a mitad de sesión.
- **Por qué importa:** lo que el agente no puede hacer es escribirlo — `/rename` es un comando del usuario y ningún enganche lo alcanza. Lo que sí se puede automatizar es que **los dos nombres salgan de la misma propuesta y en el mismo momento**.
- **Qué lo soluciona:** que el recordatorio traiga las dos líneas: el comando de renombrar, que corre el agente, y el `/rename`, que pega el usuario.
- **Qué se decidió:** eso mismo, probado.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [historico-chat/README.md](../../README.md), donde quedó escrito el par de líneas.
- **Nace en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Cerrado en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Con qué se retoma:** —.

### H-3 · El comportamiento replica solo; el texto que lo explica, no

- **Qué pasó:** el usuario preguntó si esto se replica en los proyectos. Sí, sin reinstalar: los proyectos no copian los validadores, su configuración llama al estándar por ruta absoluta. Pero el `README` del histórico de cada proyecto **es de los que el instalador no pisa**: los proyectos nuevos nacen con la plantilla nueva y los viejos se quedan con la redacción vieja.
- **Por qué importa:** el mecanismo llega completo, así que no afecta el funcionamiento. Lo que envejece es la explicación — y con el tiempo el documento del proyecto cuenta un estándar que ya no es.
- **Qué lo soluciona:** que el instalador **agregue** al `README` del proyecto la sección nueva sin tocar el resto, como ya hace con el `CLAUDE.md`.
- **Qué se decidió:** nada. El agente lo ofreció y quedó sin respuesta.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es aplicar al `README` lo que el instalador ya hace con otro archivo.
- **Orden de resolución:** 1 de 2.
- **Dónde queda:** [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Nace en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿los documentos heredados que el proyecto puede editar reciben las secciones nuevas, o se quedan como quedaron?

### H-4 · Nada prohibía escribir como escribe una máquina

- **Qué pasó:** el usuario buscó un archivo suyo sobre las marcas que delatan un texto redactado por IA. No estaba en este repositorio: apareció en el histórico crudo de Claude Code, en otro proyecto. Con él pidió una regla, y que **todos los proyectos la repliquen**.
- **Por qué importa:** `00·ID7` mandaba escribir claro, pero no decía nada de la raya larga, los emojis o el cierre servicial. Y `notas/` no viaja a los proyectos: una lista guardada ahí no obliga a nada.
- **Qué lo soluciona:** la regla en el capítulo que se carga literal en cada sesión, y la lista como anexo de ese capítulo — el cuerpo de una regla son cuatro líneas.
- **Qué se decidió:** nace [`00·ID8`](../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), que extiende a `ID7` y alcanza a todo texto que una persona lea como trabajo terminado. La lista creció de 30 marcas en seis secciones a **62 en ocho**, con dos nuevas: las marcas **invisibles** —espacio duro, ancho cero, guion suave, que son las únicas que un script cuenta sin equivocarse— y **el español que no es de acá**. Se borró la copia de `notas/` para no tener dos listas que se desincronicen. Versión **7.0.0 · MAYOR**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`ID8`](../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) y el anexo [base/00-identidad-y-rol/marcadores-de-ia.md](../../../base/00-identidad-y-rol/marcadores-de-ia.md).
- **Nace en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Cerrado en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Con qué se retoma:** —.

### H-5 · El estándar no cumple su propia regla nueva

- **Qué pasó:** el texto ya escrito de `base/`, `plantillas/` y los `README` usa la raya larga como inciso en todas partes, y esa es la marca número uno de la lista.
- **Por qué importa:** mientras no se limpie, **el estándar enseña lo contrario de lo que pide**. Por la cláusula de retroactividad la regla solo rige para lo que se escriba desde entonces, así que nada se rompe — y por eso se queda así.
- **Qué lo soluciona:** limpiarlo, pero no a mano: son unos 200 archivos y depende del validador mecánico de `ID8`, que no existe.
- **Qué se decidió:** abrir el pendiente en vez de hacerlo. Dice qué contar, por dónde empezar, qué no tocar —el histórico es transcripción literal— y que reescribir una regla anula su checklist.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, ya está anotado.
- **Orden de resolución:** 2 de 2.
- **Dónde queda:** [pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md](../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md).
- **Nace en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Cerrado en:** —.
- **Con qué se retoma:** el validador mecánico primero; sin él, el recuento sobre 200 archivos se hace a mano.

### H-6 · Nadie exige que el texto esté bien escrito en español

- **Qué pasó:** el usuario preguntó si se tiene en cuenta que los textos vayan en español colombiano, con su ortografía, gramática y sintaxis. No: lo único que hay es `01·C8`, que fija **el idioma** y nada más.
- **Por qué importa:** es un hueco distinto al de `ID8`. Aquella dice cómo **no** escribir; esta diría cómo sí. Hoy no hay ninguna.
- **Qué lo soluciona:** una regla propia. En el anexo entró solo la cara que le corresponde: el español neutro de traducción y el léxico de España como delatores.
- **Qué se decidió:** dejarlo escrito como hueco. El usuario pidió no tocar la regla mientras se construía el documento.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, sería una regla nueva del capítulo `01`.
- **Orden de resolución:** —, no bloquea nada.
- **Dónde queda:** la sección «Lo que este anexo no cubre» de [base/00-identidad-y-rol/marcadores-de-ia.md](../../../base/00-identidad-y-rol/marcadores-de-ia.md).
- **Nace en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿se escribe la regla del español correcto, o alcanza con lo que el anexo ya dice?

### H-7 · Otra vez un solo commit por culpa de dos archivos compartidos

- **Qué pasó:** el árbol traía sin commitear la 6.0.0 de otra sesión, que comparte `CHANGELOG.md` y `VERSION`. Separar los commits habría exigido partir esos dos archivos por mitades.
- **Por qué importa:** es la tercera vez en cuatro días. El problema no es el descuido: son dos archivos que **todas** las sesiones tocan a la vez.
- **Qué lo soluciona:** que cada sesión suba lo suyo apenas termina, antes de que se acumule.
- **Qué se decidió:** un solo commit, con el cuerpo diciendo primero lo del usuario y después lo que arrastraba el árbol. El agente además le puso al `10-ideas.md` de otra sesión su línea de índice, que faltaba y hacía fallar al validador, y lo dijo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** commit `ab314a1`, y el [pendiente 22](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md), que recoge el mismo choque.
- **Nace en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Cerrado en:** 2026-08-08 · el nombre de la sesión y las marcas de IA.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1, H-2, H-4 y H-7 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-3 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), H-5 en el [11](../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md); H-6 queda escrito en el anexo |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ commit `ab314a1` |
