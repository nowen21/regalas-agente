# 2026-08-06 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-06-la-anatomia-de-la-regla.md](../../2026-08-06-la-anatomia-de-la-regla.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-15.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)), así que los hallazgos se sacaron de la transcripción. «Responde a» y «dispara» van en `—`: las épicas nacieron el 2026-08-13.
>
> **Es la sesión más larga del histórico:** 61 intercambios, del 2026-08-06 a las 17:45 al 2026-08-07 a las 15:50. Cruza dos veces la medianoche y el resumen queda en el día en que empezó.

**Viene de:** —, es trabajo nuevo.

**Propósito:** saber si las meta-reglas ya se cumplen, y de ahí, escribir el molde de cómo es una regla.

---

## Hallazgos de esta sesión

### H-1 · El agente auditó el estándar sin que se lo pidieran

- **Qué pasó:** a la pregunta «¿esto ya se está aplicando a las reglas?», el agente respondió con siete desvíos y una propuesta de trabajo. El usuario: *«yo nunca dije que la aplicara, solo le dije que la creara en el archivo»*.
- **Por qué importa:** una pregunta pide una respuesta. Contestarla con un plan de trabajo empuja a decidir algo que nadie preguntó.
- **Qué lo soluciona:** responder, y esperar.
- **Qué se decidió:** el agente aclaró que no había tocado nada, y de paso separó los dos sentidos de «aplicar» que había mezclado: las reglas **cumplen por origen** —el capítulo se escribió describiendo lo que la base ya hacía— y la auditoría hacia atrás nunca se hizo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [pregunta, afirmación o indicación](../../memory/pregunta-no-es-instruccion.md), que se escribió más adelante en esta misma sesión por el mismo motivo.
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-2 · Estaba la regla de reglas, y no el molde de una regla

- **Qué pasó:** el usuario pidió *«una estructura de lo que debe ser una regla, así como estamos haciendo en F13»*. Lo que había estaba disperso en `M4`, `M5`, `M7`, `M8`, `M9`, `M10` y el procedimiento del final.
- **Por qué importa:** trece reglas sueltas no enseñan a escribir una. El esqueleto sí, y es lo que se usa hoy para revisar cada regla nueva.
- **Qué lo soluciona:** un anexo con la anatomía: encabezado, cuerpo, dependencias, excepción, ejemplo, y lo que la regla obliga fuera de su propio texto.
- **Qué se decidió:** nace `estructura-regla.md`, y el capítulo pasa de archivo a carpeta con el patrón de `F13`: `base.md` para el capítulo y el anexo al lado.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/20-meta-reglas/estructura-regla.md](../../../base/20-meta-reglas/estructura-regla.md) — el capítulo se renumeró de `00` a `20` en esta misma sesión.
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-3 · El agente versionó un cambio que no estaba aprobado

- **Qué pasó:** al escribir el anexo, el agente además enlazó el capítulo, subió `VERSION` a 1.4.0 y escribió la entrada del `CHANGELOG`. El usuario: *«espere, todavía no le he dicho si se aplica, la estoy validando»*.
- **Por qué importa:** versionar publica. Un borrador que sube de versión se vuelve norma vigente sin que nadie lo haya decidido.
- **Qué lo soluciona:** separar redactar de adoptar. `M10` exige versionar **con** el cambio, pero esa exigencia arranca cuando el cambio se adopta, no cuando se escribe.
- **Qué se decidió:** revertido todo menos el archivo nuevo. Y una regla de trabajo: *«mientras estemos trabajando en la carpeta, todo lo que se cree o se edite debe realizarse únicamente dentro de esa carpeta»*.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [trabajo confinado a la carpeta](../../memory/trabajo-confinado-a-la-carpeta.md).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-4 · Un enlace colgado al archivo viejo también es referenciar la carpeta

- **Qué pasó:** al mover el capítulo a su carpeta, el `CLAUDE.md` y el `README.md` quedaron apuntando al path viejo. El agente los llamó «enlaces colgados, no referencias a lo nuevo». El usuario no aceptó la distinción: el archivo es de esa carpeta, así que la referencia es a la carpeta.
- **Por qué importa:** el trabajo en curso no se anuncia al resto del repositorio hasta que se aprueba. Si algo lo nombra, ya está adoptado a medias.
- **Qué lo soluciona:** quitar la mención, no reapuntarla.
- **Qué se decidió:** se borró el enlace del [CLAUDE.md](../../../CLAUDE.md) —quedó *«el procedimiento completo está en las meta-reglas del preámbulo»*, sin path— y el renglón del índice del `README`. Fuera de la carpeta no quedó ni una mención.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la misma memoria de [trabajo confinado](../../memory/trabajo-confinado-a-la-carpeta.md).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-5 · Dos lectores distintos, dos documentos

- **Qué pasó:** el usuario lo dijo y pidió que lo corrigieran si estaba mal: *«la explicación está dirigida a las personas, mientras que la estructura está diseñada para que el agente la entienda e interprete»*. No estaba mal.
- **Por qué importa:** es el reparto que sostiene la carpeta hasta hoy. `base.md` es lo que el agente obedece; el anexo es lo que una persona lee para entenderlo. Mezclarlos deja un documento que no sirve a ninguno de los dos.
- **Qué lo soluciona:** que el anexo se explique en lenguaje simple, con ejemplos y una tabla de qué significa cada prefijo, sin tocarle la estructura.
- **Qué se decidió:** el usuario fijó el límite en tres pedidos seguidos: *«no le cambie la estructura, solo que se entienda»*, *«que un niño entienda»*, *«no necesita extenderse tanto: menos es más»*.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/20-meta-reglas/estructura-regla.md](../../../base/20-meta-reglas/estructura-regla.md), y las memorias de [estilo simple](../../memory/estilo-redaccion-simple.md) y [respuestas cortas](../../memory/respuestas-cortas.md).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-6 · `F0` pedía tres cosas a la vez

- **Qué pasó:** al probar el molde contra una regla real, `F0` resultó ser tres cosas en un bloque: un mapa de siete pasos, la orden de recorrer la cadena y las definiciones de épica, módulo y fase — que además ya tienen dueño en otro capítulo.
- **Por qué importa:** es el ejemplo con el que se explica `M5`. Una regla que necesita repetirse dos veces en su propio texto no tiene clara cuál es su única exigencia.
- **Qué lo soluciona:** la orden se queda como `F0`; el mapa sube al encabezado del capítulo; las definiciones se borran y se enlaza al dueño. El número no cambia, aunque la regla adelgace.
- **Qué se decidió:** quedó como ejemplo desmenuzado, no se aplicó — el usuario estaba validando el molde, no cambiando el capítulo.
- **Estado:** resuelto, pero en otra sesión.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** hoy [`F0`](../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) es solo la cadena, con su excepción y su checklist. Se aplicó el 2026-08-07 al bajar el capítulo 02 al molde (v2.5.0).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-07 · sesión 7.
- **Con qué se retoma:** —.

### H-7 · Lo trabajado en el día no se estaba convirtiendo en reglas

- **Qué pasó:** el usuario pidió releer todas las sesiones del día y sacar qué merece ser regla. Salieron **12 candidatas**: 6 nuevas, 5 mejoras y 1 que el propio agente recomendó dejar fuera de `base/`. Más 11 descartadas por duplicar algo existente y 8 defectos del estándar que no son reglas.
- **Por qué importa:** `01·C10` ya manda evaluar cada mensaje como posible mejora, pero corre en caliente y se le pasan cosas: `M14`, `M15` y `M16` salieron de una sesión donde `C10` estaba activa y no las propuso. El barrido en frío las repesca.
- **Qué lo soluciona:** tres piezas separadas — el análisis del día (un archivo del histórico), el formato del análisis (una plantilla) y la obligación de hacerlo (una regla, `C20`, que se apoya en `C10`).
- **Qué se decidió:** se escribió el análisis. La plantilla y la regla quedaron propuestas, sin construir. Al agente le faltaba lo principal: una regla que corre «cuando el usuario lo pida» es un favor, no una norma, y el disparador quedó sin decidir.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, sería una plantilla y una regla, las dos ya redactadas en el análisis.
- **Orden de resolución:** 1 de 3. Va primero: mientras no se decida, cada sesión sigue dejando candidatas que nadie repesca.
- **Dónde queda:** [historico-chat/reglas-2026-08-06/reglas.md](../../reglas-2026-08-06/reglas.md) y el [pendiente 33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md). De las 12, `M15` se construyó ese mismo día y `M16` el 2026-08-12; `plantillas/candidatas-a-regla.md` no existe.
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿cuándo corre el barrido? La recomendación fue engancharlo al cierre de versión que `M10` ya define, para no inventar un momento nuevo.

### H-8 · Un proyecto con el `CLAUDE.md` viejo figuraba como instalación completa

- **Qué pasó:** el usuario lo pidió directo: *«debe haber algo que valide que el `CLAUDE.md` está actualizado, no puede haber nada viejo en el proyecto»*. Había algo, con tres huecos: quedar viejo era aviso y no reprobaba; un cambio **dentro** de una sección existente no se veía, porque se comparaban títulos; y el único detector que quedaba era la fecha del archivo, que un `git clone` borra.
- **Por qué importa:** el checklist decía «completo» sobre un proyecto que estaba corriendo con documentos viejos.
- **Qué lo soluciona:** la huella. Cada documento heredado lleva sellado el hash **de la plantilla contra la que se sincronizó**, no el suyo propio — el `CLAUDE.md` lo llena cada proyecto y su contenido nunca coincide con el original.
- **Qué se decidió:** nace [`validadores/versiones.py`](../../../validadores/versiones.py); quedar viejo **reprueba**; cada actualización deja su registro. El registro se movió de `.agente/versiones/` a `documentacion/versiones/` porque `.agente/` está en el `.gitignore` y ese historial no viajaba con el repositorio. Una prueba fija la decisión para que no se devuelva sola.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** versión **2.0.0 · MAYOR** del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-9 · La alerta al proyecto era ruido

- **Qué pasó:** el usuario lo vio antes que el agente: *«al proyecto no le interesa conocer todos los cambios del agente, sino únicamente aquellos que debe actualizar»*. El componente `version` reprobaba por cualquier cambio de número, aunque no tocara nada de lo que ese proyecto usa.
- **Por qué importa:** el ruido enseña a ignorar la alerta. Una alerta que se ignora es peor que ninguna.
- **Qué lo soluciona:** que mande el sello y no el número.
- **Qué se decidió:** el número **informa**, el sello **reprueba**. Un proyecto en 1.0.0 con el estándar en 1.6.0 sale en verde si nada de lo suyo cambió. Dos pruebas fijan el criterio.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`checklist.py`](../../../validadores/checklist.py) y [`versiones.py`](../../../validadores/versiones.py).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-10 · Una regla citada sin enlace obliga a salir a buscarla

- **Qué pasó:** el usuario lo pidió en una línea: *«toda regla que se referencie debe tener un link a la parte que referencia para su entendimiento»*. Había 285 citas en 47 archivos, en tres formatos distintos.
- **Por qué importa:** citar por ID no basta: quien lee tiene que llegar a la regla en un clic. Y editarlas a mano no sirve — el capítulo 02 se reorganizó **tres veces** mientras se trabajaba, y cada movimiento habría dejado decenas de enlaces muertos.
- **Qué lo soluciona:** una herramienta que enlace, normalice el formato y **repare** las rutas cuando un capítulo se mueve.
- **Qué se decidió:** nace [`validadores/citas.py`](../../../validadores/citas.py) con modo reparar, y la regla [`M15`](../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md). Las 206 citas de `base/` quedaron enlazadas al archivo y al ancla exacta. `CHANGELOG` 2.3.0.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`M15`](../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md), versión 2.3.0 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-06 · la anatomía de la regla.
- **Con qué se retoma:** —.

### H-11 · Una sesión que cruza la medianoche queda con el nombre de otro día

- **Qué pasó:** el usuario preguntó si al día siguiente seguía siendo la misma sesión. Sí: el enganche busca la sesión por su marca, no por la fecha, así que esta siguió escribiendo en un archivo llamado `2026-08-06` con contenido del 07.
- **Por qué importa:** el nombre del archivo es lo primero que se mira para ubicar cuándo pasó algo, y en esta sesión miente sobre la mitad de su contenido.
- **Qué lo soluciona:** decir en la convención qué se hace: si se parte en un archivo nuevo o si se queda como está.
- **Qué se decidió:** nada. El agente lo dejó anotado y ofreció subirlo como candidata al análisis.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es una línea en el `README` de la carpeta.
- **Orden de resolución:** 3 de 3. Va último: no rompe nada, confunde.
- **Dónde queda:** [pendientes/33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md). Para los **resúmenes** sí quedó resuelto —van al día en que pasaron las cosas, según [resumenes/README.md](../README.md)—; para la transcripción, no.
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿la transcripción se parte a la medianoche, o se queda entera con el nombre del día en que empezó?

### H-12 · La memoria del agente estaba fuera del repositorio

- **Qué pasó:** el usuario pidió que el recuerdo que acababa de guardarse en el almacén local de la herramienta quedara en `historico-chat/memory.md` y que desde el almacén se lo referenciara.
- **Por qué importa:** lo que vive en `~/.claude/` no se ve en git, no se revisa y no viaja. Y había **doce recuerdos más** ahí.
- **Qué lo soluciona:** el texto completo en el repositorio, y en el almacén local solo una frase con el enlace.
- **Qué se decidió:** se movió ese recuerdo. Los otros doce quedaron preguntados y se movieron al día siguiente.
- **Estado:** resuelto, pero en otra sesión.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** hoy es la regla [`01·C19`](../../../base/01-conducta.md) y la carpeta [historico-chat/memory/](../../memory/memory.md), con el almacén local **vacío**; se cerró en la sesión del [2026-08-07](../../2026-08-07-memoria-del-agente-en-el-repo.md), v3.0.0.
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ nueve resueltos; H-6 y H-12 se cerraron al día siguiente |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-7 y H-11 en el [pendiente 33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ el usuario aprobó el commit: 40 archivos, 4114 líneas |
