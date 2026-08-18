# 2026-08-14 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-14-h-8-la-traduccion-quedo-a-medias.md](../../2026-08-14-h-8-la-traduccion-quedo-a-medias.md), con la plantilla [`plantillas/sesion.md`](../../../plantillas/sesion.md). La conversación está allá; acá queda lo que la sesión dejó.

Se anotan todos, resueltos y abiertos.

**Viene de:** 2026-08-14 · hu-de-la-comprobacion-automatica · [H-8 · La traducción quedó a medias](hu-de-la-comprobacion-automatica.md#h-8--la-traducción-quedó-a-medias), cerrado en su primera mitad por esta sesión.

---

## Hallazgos de esta sesión

### H-1 · El glosario no existía, y ahora sí

- **Qué pasó:** la terminología del estándar estaba repartida en las reglas que usan cada palabra. Para saber qué es una especificación había que encontrar la regla que la exige; para saber qué es una señal, otra; para saber qué es una fase, un capítulo entero.
- **Por qué importa:** era la mitad del hallazgo H-8, el que quedó abierto el 2026-08-14 por no mezclarlo con el cambio de la 10.0.0. Sin glosario, entrar al estándar exigía leerlo entero.
- **Qué lo soluciona:** la fase [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/README.md](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/README.md), que entregó [base/glosario.md](../../../base/glosario.md): 72 términos en cuatro grupos, cada uno en una línea, con quién lo escribe, dónde vive y qué regla lo manda. Enlazado desde las tres puertas de entrada.
- **Qué se decidió:** vive en `base/`, porque es lo que heredan los proyectos; sin número de capítulo y sin checklist, porque es anexo y no exige nada; en cuatro grupos temáticos y no en una lista alfabética, porque la lista alfabética sirve para buscar lo que ya se sabe cómo se llama.
- **Estado:** resuelto.
- **Responde a:** [EP-003 · HU-010](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md), sus tres criterios.
- **Dispara:** H-2 de esta misma sesión.
- **Orden de resolución:** hecho.
- **Dónde queda:** estándar 15.3.0 · [base/glosario.md](../../../base/glosario.md).
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica, como H-8.
- **Cerrado en:** 2026-08-14 · h-8-la-traduccion-quedo-a-medias.
- **Con qué se retoma:** nada. La otra mitad es H-2.

### H-2 · Doce términos siguen en inglés, y ya se sabe cuáles

- **Qué pasó:** el glosario dejó el inventario de lo que falta traducir: doce términos con traducción usada que siguen en inglés, en trece nombres repartidos por diez archivos entre `base/`, `plantillas/`, `skills/` y `notas/`. Los nombres de los roles (Explorer, Proposer, Spec Writer, Designer, Task Planner, Implementer, Verifier, Reviewer, Orchestrator, Researcher) y la palabra `spec`, que se tradujo en el texto de las reglas pero quedó en las descripciones de las skills y en nombres de archivo.
- **Por qué importa:** es la segunda mitad de H-8, y el incumplimiento de [`01·C8`](../../../base/01-conducta.md#c8--habla-el-idioma-del-proyecto) sigue vivo mientras no se cambien.
- **Qué lo soluciona:**

  **EP-003 · HU nueva — traducir los nombres que quedaron en inglés**
  - **Como** quien lee el estándar en español
  - **Quiero** que los nombres de los roles y de los archivos estén en español
  - **Para** no tropezar con la mitad del vocabulario en otro idioma
  - **Contexto:** el inventario ya está levantado en el cierre de [base/glosario.md](../../../base/glosario.md), con el archivo donde vive cada uno. Renombrar un archivo rompe todo enlace que apunte a él, así que va de una vez y con su plan, no de a poco. Toca además decidir qué pasa con `documentacion/*/spec.md`, que es nombre de archivo y no de rol.
- **Qué se decidió:** no tocarlos en esta fase. Estaba declarado fuera de alcance desde el plan, y la propia HU-010 lo excluye en §3.3.
- **Estado:** abierto.
- **Responde a:** [`01·C20`](../../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica), la palabra de otro idioma se traduce.
- **Dispara:** una HU de EP-003 que todavía no está escrita.
- **Orden de resolución:** 1 de 3 · es lo único que queda del hallazgo original.
- **Dónde queda:** [pendientes/21-el-glosario-y-los-terminos-en-ingles.md](../../../pendientes/21-el-glosario-y-los-terminos-en-ingles.md), en su punto 2.
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica, como H-8.
- **Cerrado en:** —
- **Con qué se retoma:** ¿se renombran también los archivos que llevan `spec` en el nombre, o solo el texto? Renombrar el archivo rompe las citas; dejarlo deja la palabra a la vista.

### H-3 · El validador de enlaces no conoce la excepción que la propia `DOC14` escribe

- **Qué pasó:** [`13·DOC14`](../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) termina diciendo: *"No aplica a los nombres cortos usados como identificador en medio de una frase, cuando quien lee ya sabe dónde viven"*. [`validadores/enlaces.py`](../../../validadores/enlaces.py) no implementa esa salida: marca aviso también cuando el enlace apunta a un archivo de la misma carpeta. En esta fase salieron 22 avisos de ese tipo.
- **Por qué importa:** obedecer al validador al pie de la letra obliga a escribir la ruta completa de 130 caracteres dentro de una frase, y eso choca con [`00·ID7`](../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md). Un validador que contradice la excepción escrita de su propia regla enseña a ignorarlo, y un validador que se ignora no sirve para nada.
- **Qué lo soluciona:**

  **EP-004 · HU nueva — el validador de enlaces respeta la excepción de `DOC14`**
  - **Como** quien escribe documentos dentro de una carpeta de fase
  - **Quiero** que el validador no marque los enlaces a la misma carpeta
  - **Para** que la regla y el programa digan lo mismo
  - **Contexto:** hoy el validador compara el texto del enlace contra la ruta desde la raíz, sin mirar si el destino está en la misma carpeta que el archivo. La excepción de `DOC14` es exactamente ese caso. Falta decidir si la excepción se implementa tal cual o si se le escribe a `DOC14` un límite más preciso que un programa pueda leer.
- **Qué se decidió:** en esta fase se aplicó la excepción de la regla y no la del validador: ruta completa para los enlaces que cruzan de carpeta, nombre corto para los de la misma. Los 22 avisos quedan.
- **Estado:** abierto.
- **Responde a:** [`13·DOC14`](../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) y [`20·M9`](../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md).
- **Dispara:** una HU de EP-004 que todavía no está escrita.
- **Orden de resolución:** 2 de 3 · mientras siga así, cada fase nueva suma avisos que nadie va a poder distinguir de los de verdad.
- **Dónde queda:** cerca de [pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md](../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md), que cuenta los 354 viejos.
- **Nace en:** 2026-08-14 · h-8-la-traduccion-quedo-a-medias.
- **Cerrado en:** —
- **Con qué se retoma:** ¿se le enseña la excepción al validador, o se le escribe a `DOC14` un límite que un programa pueda comprobar sin interpretar?

### H-4 · El mapa del sitio dice v1.4.0 con el estándar en 15.3.0

- **Qué pasó:** el encabezado de [anatomia/mapa-del-sitio.md](../../../anatomia/mapa-del-sitio.md) dice *"Estándar v1.4.0 · actualizado el 2026-08-07"*. Van catorce versiones desde entonces. Su propia tabla de mantenimiento incluye la fila *"sube la versión del estándar → el encabezado del documento"*.
- **Por qué importa:** el documento que existe para decir dónde está cada cosa se presenta con una versión de hace catorce números. Quien lo abra no sabe si el árbol de abajo está igual de viejo.
- **Qué lo soluciona:** ponerle el enganche que ya tienen la transcripción y el resumen, o al menos comprobarlo con un validador. Sin eso depende de que alguien se acuerde, que es la lección que el estándar ya aprendió dos veces.
- **Qué se decidió:** no tocarlo. Está fuera de los archivos que el plan de la fase declara ([`02·F8`](../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)); lo único que se le agregó fue la línea del glosario en el árbol, que sí estaba en el plan.
- **Estado:** abierto.
- **Responde a:** —
- **Dispara:** una HU de EP-004 o EP-005 que todavía no está escrita.
- **Orden de resolución:** 3 de 3 · no rompe nada, pero deja mintiendo al documento que existe para orientar.
- **Dónde queda:** sin pendiente propio todavía.
- **Nace en:** 2026-08-14 · h-8-la-traduccion-quedo-a-medias.
- **Cerrado en:** —
- **Con qué se retoma:** ¿un enganche que actualice el encabezado al subir `VERSION`, o un validador que falle cuando los dos números no coinciden?

### H-5 · La historia estimaba treinta términos y salieron sesenta y siete

- **Qué pasó:** el supuesto §3.2 de [EP-003 · HU-010](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md) decía *"unos treinta términos"*. Al recorrer `base/`, `plantillas/` y `skills/` salieron 67 que cumplen la regla de entrada de la propia historia: aparecer en una regla o en una plantilla.
- **Por qué importa:** no cambia lo que se entregó, pero sí lo que se creía del tamaño del vocabulario del estándar. Un supuesto que se desvía al doble merece quedar anotado: la próxima estimación parte de 67, no de 30.
- **Qué lo soluciona:** nada por construir. Es un dato.
- **Qué se decidió:** no recortar. La regla de entrada es RN-05 de la historia y las 67 la cumplen; lo que estaba mal era la estimación, no el contenido.
- **Estado:** resuelto.
- **Responde a:** [EP-003 · HU-010](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md), supuesto §3.2.
- **Dispara:** —
- **Orden de resolución:** hecho.
- **Dónde queda:** defecto D-01 del [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md) de la fase.
- **Nace en:** 2026-08-14 · h-8-la-traduccion-quedo-a-medias.
- **Cerrado en:** 2026-08-14 · h-8-la-traduccion-quedo-a-medias.
- **Con qué se retoma:** nada.

### H-6 · El glosario no se entendía, y lo probó quien no lo escribió

- **Qué pasó:** el usuario leyó el glosario para entender una frase y no pudo. La entrada de `brief` decía *"el primer papel"* y la columna del nombre decía *"quiere decir breve"*. Ninguna de las dos le decía qué es. Lo resumió así: *"para qué tener un glosario si tengo que ir a buscar significados en otro lado porque no lo entendí"*.
- **Por qué importa:** era la prueba CP-006 de la fase, la única que el agente no podía correr, y salió negativa. Un glosario que no resuelve la palabra ahí mismo no cumple para lo que existe.
- **Qué lo soluciona:** ya hecho. Las 72 definiciones se reescribieron con la prueba de reemplazo: cambiar la palabra por su definición y que la frase siga teniendo sentido. 48 de 72 no la pasaban.
- **Qué se decidió:** el molde de la definición lo puso el usuario con sus palabras, y no se toca: *"El documento donde se escribe qué se necesita, antes de que exista una solución"*. Cada definición empieza diciendo qué clase de cosa es.
- **Estado:** resuelto.
- **Responde a:** [EP-003 · HU-010 · RNF-01](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md).
- **Dispara:** H-7 y H-8 de esta sesión.
- **Orden de resolución:** hecho.
- **Dónde queda:** estándar 17.0.2 · ciclo 3 del [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md).
- **Nace en:** 2026-08-16 · h-8-la-traduccion-quedo-a-medias.
- **Cerrado en:** 2026-08-16 · h-8-la-traduccion-quedo-a-medias.
- **Con qué se retoma:** falta probar las otras cuatro entradas con lector de fuera. Se probó una de cinco.

### H-7 · "Brief" nombraba el largo del documento, no lo que trae

- **Qué pasó:** traducir `brief` literal da "breve", que habla del tamaño. Lo que hay que entender de ese documento es que va primero y trae lo que no se negocia. La traducción no ayudaba, y la palabra seguía en inglés.
- **Por qué importa:** era el primer término de la cadena de trabajo. Quien no lo entiende no entiende por dónde arranca todo.
- **Qué lo soluciona:** ya hecho. `brief` pasa a **planteamiento** en toda la zona normativa, estándar 18.0.0. Se renombraron `plantillas/brief.md` y el `brief.md` de la raíz, cambió la ruta `prompts/<slug>-planteamiento.md`, y se corrigieron los enlaces en 13 archivos, incluidas fases cerradas.
- **Qué se decidió:** entre planteamiento, pedido y punto de partida, el usuario escogió **planteamiento**. "Encargo" se había descartado antes por poco diciente y por sonar a mandado.
- **Estado:** resuelto en la zona normativa, abierto en el resto.
- **Responde a:** [`01·C20`](../../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica).
- **Dispara:** limpiar la palabra en `documentacion/` (18 archivos), `pendientes/` (5), `analisis/` (1) e `historico-chat/` (22).
- **Orden de resolución:** 1 de 2 · las épicas son documentos vivos y hoy nombran algo que ya no se llama así.
- **Dónde queda:** estándar 18.0.0.
- **Nace en:** 2026-08-16 · h-8-la-traduccion-quedo-a-medias.
- **Cerrado en:** —
- **Con qué se retoma:** ¿se cambia la palabra en las épicas y los pendientes, que son documentos vivos, o solo se deja en la norma?

### H-8 · Un glosario obligatorio para cada proyecto no tenía regla

- **Qué pasó:** el glosario del estándar define las palabras del estándar. Las del negocio de cada proyecto no las definía nadie. La sección Glosario de `plantillas/dominio.md` existía desde antes, vacía, sin ninguna regla que obligara a llenarla.
- **Por qué importa:** dos documentos del mismo proyecto pueden llamarle distinto a la misma cosa sin que nadie lo note.
- **Qué lo soluciona:** ya hecho. Nace [`13·DOC23`](../../../base/13-documentacion/reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md), estándar 17.0.0, MAYOR.
- **Qué se decidió:** se buscó antes de crear (`20·M12`). `DOC10` cataloga las reglas del proyecto y `DOC13` sus módulos; `mapeo-nombres.md` hace lo contrario, traduce un concepto de la base al nombre de acá. Ninguna servía.
- **Estado:** resuelto.
- **Responde a:** el usuario, que lo pidió así: *"cada proyecto debe tener su glosario y debe ser establecido mediante regla"*.
- **Dispara:** todo proyecto al día tiene que llenar su glosario.
- **Orden de resolución:** hecho.
- **Dónde queda:** estándar 17.0.0.
- **Nace en:** 2026-08-16 · h-8-la-traduccion-quedo-a-medias.
- **Cerrado en:** 2026-08-16 · h-8-la-traduccion-quedo-a-medias.
- **Con qué se retoma:** nada.

---

## ¿Se puede cerrar la sesión?

**Sí.** La fase A de EP-003 · HU-010 cierra con veredicto **Cumple**, y lo que quedó abierto está anotado con dónde se retoma.

| Para cerrar | Estado |
|---|---|
| Los tres criterios de aceptación y los dos requisitos no funcionales | Cumplen |
| CP-006, la prueba de legibilidad | Corrida el 2026-08-16 por el usuario. Destapó tres defectos, los tres corregidos |
| Los documentos de cierre alineados con el veredicto | Hecho |
| Commit de la fase y de las versiones 17.0.0 a 18.0.0 | Autorizado por el usuario |
| H-2, H-3, H-4 y H-7 | Abiertos, y así se quedan: cada uno con dónde se retoma |

