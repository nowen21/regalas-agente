# 2026-08-08 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-08-escribir-para-que-lo-entienda-quien-no-sabe.md](../../2026-08-08-escribir-para-que-lo-entienda-quien-no-sabe.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Arranca con una frase suelta de la documentación recién escrita y termina cambiando cómo escribe el agente.

**Propósito:** que lo que el agente escribe se entienda sin saber del tema.

---

## Hallazgos de esta sesión

### H-1 · Una frase de la documentación no la entendía un niño

- **Qué pasó:** el usuario tomó una línea de un documento recién escrito —*«Entrega, uno por uno, los archivos de código de un proyecto ya leídos y listos para revisar»*— y preguntó si se entiende. No: no dice a quién entrega, ni quién revisa, y «ya leídos» cuelga mal.
- **Por qué importa:** la documentación se había escrito ese mismo día pidiendo lenguaje claro, y aun así salió así. La claridad no se consigue pidiéndola una vez.
- **Qué lo soluciona:** decir quién recibe, qué recibe y para qué.
- **Qué se decidió:** la frase quedó *«abre los archivos de código del proyecto y los va pasando de a uno, con su nombre y su contenido, a los programas que los revisan»*.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [validadores/docs/codigo.md](../../../validadores/docs/codigo.md).
- **Nace en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Cerrado en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Con qué se retoma:** —.

### H-2 · A una pregunta de sí o no, el agente respondió con un análisis

- **Qué pasó:** *«le estoy preguntando si lo van a entender, no que me haga división etimológica»*. El agente había contestado con tres puntos de análisis y una propuesta de redacción.
- **Por qué importa:** la respuesta correcta cabía en cuatro palabras — *«quien sabe, sí; un niño, no»*—, y es la que el usuario necesitaba para decidir.
- **Qué lo soluciona:** responder lo que se preguntó, y guardar el detalle para cuando lo pidan.
- **Qué se decidió:** el agente respondió en una línea.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [respuestas cortas](../../memory/respuestas-cortas.md).
- **Nace en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Cerrado en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Con qué se retoma:** —.

### H-3 · La regla que había mandaba lo contrario

- **Qué pasó:** el usuario pidió una regla general de redacción, con doce puntos. Al buscar dónde ponerla apareció el choque: [`00·ID2`](../../../base/00-identidad-y-rol/reglas/ID2-escribe-en-registro-tecnico-sin-adornos.md) ocupaba ese lugar diciendo *«escribe para quien lee código: preciso, técnico»*.
- **Por qué importa:** no era un matiz. Sobre el mismo tema, una mandaba una cosa y la otra la opuesta — y la vieja seguía rigiendo.
- **Qué lo soluciona:** derogar, no reescribir. Reescribir `ID2` en su sitio habría sido peor: un commit viejo que la cita quería decir *«escribí técnico»*, y al leerlo hoy diría lo contrario. Derogar deja el rastro intacto.
- **Qué se decidió:** nace [`00·ID7`](../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) —todo lo que el agente escribe, **las reglas mismas incluidas**, se entiende sin saber del tema— e `ID2` queda `[DEROGADA en 6.0.0]` con su texto entero. También hubo que corregir dos capítulos que decían lo viejo, y el recuerdo de estilo, que decía justo lo contrario. Versión **6.0.0 · MAYOR**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`ID7`](../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) y la memoria [estilo de redacción simple](../../memory/estilo-redaccion-simple.md).
- **Nace en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Cerrado en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Con qué se retoma:** —.

### H-4 · El agente se puso CUMPLE de más en su propio checklist

- **Qué pasó:** el usuario preguntó si `ID7` cumplía el capítulo 20. El agente lo revisó y encontró que **dos filas no se sostenían**: el cuerpo pedía cuatro cosas que se cumplen por separado —eso son cuatro reglas, no una— y ocupaba seis frases donde caben cuatro líneas.
- **Por qué importa:** el checklist es lo que decide si una regla se publica. Si quien lo llena se aprueba a sí mismo, deja de decidir nada. El propio agente lo dijo: *«me pasé de generoso»*.
- **Qué lo soluciona:** una sola exigencia —que el texto lo entienda quien no sabe del tema— y lo demás subordinado a ella como el cómo, el límite y la comprobación.
- **Qué se decidió:** se reescribió el cuerpo sin perder ninguno de los doce puntos pedidos, y el checklist quedó reaplicado: 19 ✅, 0 ❌, 1 N/A.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** el bloque de checklist de [`ID7`](../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md). Que nadie comprueba esos bloques sigue abierto en el [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).
- **Nace en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Cerrado en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Con qué se retoma:** —.

### H-5 · La documentación usaba palabras que nunca explicaba

- **Qué pasó:** con la regla aprobada, el usuario pidió aplicarla a los 41 documentos de `validadores/docs/`. Lo que las rompía eran dos cosas: las **frases de apertura**, comprimidas hasta volverse ambiguas, y los **términos técnicos sueltos** que nadie explicaba nunca.
- **Por qué importa:** explicar un término es decir qué es **y por qué importa**, no traducir su nombre. *Llave foránea sin política de borrado* pasó a *«cada factura apunta a un cliente; si borran ese cliente, hay que haber dicho antes qué pasa con sus facturas»*.
- **Qué lo soluciona:** explicar cada término la primera vez que aparece en su documento, y dejar los nombres del código como están, que son identificadores y no prosa.
- **Qué se decidió:** los 41 documentos pasaron por la regla.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [validadores/docs/](../../../validadores/docs/README.md).
- **Nace en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Cerrado en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Con qué se retoma:** —.

### H-6 · «¿Cuáles carpetas?» — la documentación decía en vago lo que el código dice exacto

- **Qué pasó:** el usuario preguntó dónde está la regla que manda detenerse cuando al proyecto le faltan sus carpetas, y **cuáles carpetas**. Era una sola: `proyectos/`, la del código. Lo dice el código, no la documentación.
- **Por qué importa:** un plural vago obliga a abrir el código para saber qué se exige — que es exactamente lo que la documentación existe para evitar.
- **Qué lo soluciona:** nombrarla, y decir además **por qué** importa que falte: si no está, el estándar nunca se instaló ahí.
- **Qué se decidió:** corregido en los dos documentos donde aparecía.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [validadores/docs/cargador.md](../../../validadores/docs/cargador.md).
- **Nace en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Cerrado en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Con qué se retoma:** —.

### H-7 · El índice de las reglas no decía qué guarda la carpeta

- **Qué pasó:** el usuario lo cerró señalando lo de fondo: *«pensé que en esa carpeta se almacenan las reglas del agente, de hecho el README lo dice… a todas estas, le falta describir lo que hace esa carpeta»*. El `README.md` de `base/` era **una sola línea, con una falta de ortografía**.
- **Por qué importa:** el agente venía respondiendo por la forma —que los capítulos son archivos o carpetas— cuando la pregunta era por el contenido: `base/` guarda **las reglas**; los capítulos son solo cómo están repartidas.
- **Qué lo soluciona:** un índice que diga qué es la carpeta, cómo está organizada, qué es el código corto de una regla, las tres clases de capítulo y qué puede tocar un proyecto de cada una.
- **Qué se decidió:** se escribió completo, con los 22 capítulos agrupados por para qué sirven.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/README.md](../../../base/README.md).
- **Nace en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Cerrado en:** 2026-08-08 · escribir para que lo entienda quien no sabe.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los siete |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ la 6.0.0 se subió con el commit `ab314a1` de la sesión vecina, que compartía `CHANGELOG` y `VERSION` |
