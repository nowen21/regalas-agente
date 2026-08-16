<!-- sesion: 64f7eded-3d44-43ba-aa2b-1b1cdd3598de -->
<!-- nombre: preguntado -->

# 2026-08-14 — H 8 la traduccion quedo a medias

## Conversación

### 1 · Usuario — 2026-08-14 22:32:27
> Cual es el proposito de esto:
>
> H-8 · La traducción quedó a medias

**Agente** — 2026-08-14 22:32:42
<!-- agente: 290fcb35-3c15-456b-b737-1aadc1b256e8 -->

**H-8 es un hallazgo abierto** de la sesión del 2026-08-14, anotado en [hu-de-la-comprobacion-automatica.md:141](historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md#L141).

Su propósito: dejar registrado que la traducción del estándar al español se hizo solo en el texto, pero **quedaron en inglés los nombres de los trece roles** (Explorer, Proposer, Designer, Implementer, Verifier, Spec Writer) y **no existe el glosario** de terminología. Eso es el mismo incumplimiento de `C8` que la sesión acababa de corregir en otra parte.

No se tocaron ahí para no mezclarlo con el cambio de la 10.0.0, así que el hallazgo existe para que no se pierda:

- **Qué lo resuelve:** EP-003 · HU-010, el glosario de la terminología (ya escrita).
- **Orden:** 2 de 7 — primero el glosario, porque con los ~30 términos escritos se ve cuáles siguen en inglés sin necesidad y se cambian todos de una vez en lugar de uno por uno.
- **Dónde vive el pendiente:** [pendientes/21-el-glosario-y-los-terminos-en-ingles.md](pendientes/21-el-glosario-y-los-terminos-en-ingles.md).

### 2 · Usuario — 2026-08-14 22:34:21
> listo entonces démosle solución

**Agente** — 2026-08-14 22:41:52
<!-- agente: 02491c35-2658-439d-8804-1f5a8e330c7a -->

Ya tengo el contexto cargado. Escribo los dos planes de la fase y paro para que los apruebes (`02·F4`, `02·F15` etapas 3–5).

Fase abierta y los dos planes escritos. **Paro acá sin tocar `base/`**, como pide `02·F4`: el plan se aprueba antes de implementar.

**Fase `A-EP-003-HU-010-glosario-de-la-terminologia`** — una sola fase para los tres criterios, porque los tres se validan sobre el mismo documento.

- [plan_trabajo.md](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/plan_trabajo.md) — 15 tareas, 13 archivos declarados, 19 h
- [plan_pruebas.md](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/plan_pruebas.md) — 8 casos, cobertura 100%
- [estado-fase.md](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/estado-fase.md)

**Qué hace la fase:** escribe `base/glosario.md` con los términos en cuatro grupos (la cadena de trabajo, las reglas, lo que comprueba, lo que se guarda), cada uno definido en una línea, con quién lo escribe, dónde vive y qué regla lo manda; lo enlaza desde las tres puertas de entrada; y cierra con la tabla de lo que sigue en inglés. **Renombrar los roles queda fuera** — la propia HU lo excluye, y verifiqué que hoy toca 10 archivos entre `skills/`, `base/` y `plantillas/`.

**Dos dudas que se cierran aprobando** (§2.7 del plan):

1. **¿`base/` o `documentacion/`?** Propongo `base/`, sin número de capítulo y sin checklist: es lo que heredan los proyectos, y recibir las reglas sin la explicación de sus palabras es recibir media cosa.
2. **¿Se trabaja sobre `main` o abro rama de la fase?**

¿Apruebas los dos planes y arranco?

---

Aparte: esta sesión la guardo como `2026-08-14-glosario-de-la-terminologia.md` — solución del hallazgo H-8: se abre la fase A de EP-003 · HU-010. ¿Va? Si sí, corro el renombrado y tú pegas `/rename glosario-de-la-terminologia`.

### 3 · Usuario — 2026-08-14 22:43:19
> nombre de la sesion: H-8-La-traducción-qued-a-medias

**Agente** — 2026-08-14 22:43:52
<!-- agente: a5c16449-ea35-4b6b-bee6-1ec9dd5b5f2b -->

Listo: la sesión quedó como [2026-08-14-h-8-la-traduccion-qued-a-medias.md](historico-chat/2026-08-14-h-8-la-traduccion-qued-a-medias.md), con su línea en el índice.

Para que la pestaña y `/resume` digan lo mismo, pega:

```
/rename h-8-la-traduccion-qued-a-medias
```

Dos cosas:

- En el nombre dice `qued` donde el hallazgo dice `quedó`. Lo dejé tal como lo escribiste; si quieres, lo vuelvo a correr con `h-8-la-traduccion-quedo-a-medias`.
- Los dos planes de la fase siguen esperando tu visto bueno, y las dos dudas: **¿`base/` o `documentacion/`?** y **¿`main` o rama de la fase?**

### 4 · Usuario — 2026-08-14 22:45:01
> 1. base
> 2. en main
>
> h-8-la-traduccion-quedo-a-medias

**Agente** — 2026-08-14 22:45:25
<!-- agente: cb006431-7bf1-42b5-855a-54e6249e4582 -->

Sesión renombrada: [2026-08-14-h-8-la-traduccion-quedo-a-medias.md](historico-chat/2026-08-14-h-8-la-traduccion-quedo-a-medias.md), índice al día.

Dudas cerradas: el glosario va en **`base/glosario.md`** y se trabaja **sobre `main`**.

Falta el sí explícito del plan (`02·F4`, `01·C17`) antes de tocar `base/`. ¿Apruebas los dos planes y arranco con T-01?

### 5 · Usuario — 2026-08-14 22:46:09
> aprobado

**Agente** — 2026-08-14 23:19:18
<!-- agente: ed88c557-b8e6-4205-a210-36285e2a9b5c -->

Aprobado. Ejecuto el plan seguido (`02·F3`). Empiezo por T-01, levantar los términos.

T-01 a T-09: escribo el glosario.

T-06: enlazarlo desde las tres puertas de entrada.

T-07 y CP-005: reviso los enlaces.

F21 me obliga a no repetir un incumplimiento ya identificado. Leo `DOC14`.

F21 aplica, y su propio ejemplo es este caso. Corrijo los enlaces de lo que escribí.

Los enlaces de la misma carpeta quedaron ilegibles. `DOC14` exime justo ese caso: nombre corto cuando quien lee ya sabe dónde vive. Dejo la ruta completa solo donde el enlace cruza de carpeta.

T-01 a T-11 hechos. Ahora ejecuto los casos de prueba.

CP-007 encontró tres definiciones que copiaban texto de su fuente. Las reescribo.

T-12 a T-15: cierre. Actualizo la especificación del módulo.

T-14: HU, su índice y el cierre de la fase.

T-15: cierro el pendiente 21 en su parte del glosario.

Corrida final del validador sobre lo que tocó la fase.

Escribo el resumen de esta sesión (`13·DOC22`).

Fase cerrada. `base/glosario.md` existe y H-8 queda resuelto en su mitad del glosario.

**Lo que entregó** — [base/glosario.md](base/glosario.md): 67 términos en cuatro grupos (la cadena de trabajo, las reglas, lo que comprueba, lo que se guarda). Cada uno en una línea, con quién lo escribe, dónde vive y qué regla lo manda. Se alcanza desde [README.md](README.md), [base/README.md](base/README.md) y [anatomia/mapa-del-sitio.md](anatomia/mapa-del-sitio.md).

**Pruebas:** 8 diseñadas, 7 corridas, 7 aprobadas, 0 rotas. Tres defectos: dos corregidos (30 enlaces que no cumplían `DOC14`, tres definiciones que copiaban su regla) y uno aceptado. Detalle en [resultado_pruebas.md](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md).

**Versión 15.3.0** (MENOR, aditivo). Actualizados: especificación del módulo, `CHANGELOG`, `VERSION`, la HU con su §8 y bitácora, los índices y el [pendiente 21](pendientes/21-el-glosario-y-los-terminos-en-ingles.md).

**Cinco hallazgos** en [el resumen de la sesión](historico-chat/resumenes/2026-08-14/h-8-la-traduccion-quedo-a-medias.md), dos resueltos y tres abiertos:

- **H-2** — quedan 12 términos por traducir (los roles y `spec`), con el archivo de cada uno. Es la otra mitad de H-8 y necesita HU propia: renombrar rompe citas.
- **H-3** — `validadores/enlaces.py` no implementa la excepción que la propia `DOC14` escribe, así que marca los enlaces a la misma carpeta. Apliqué la regla, no el validador: quedan 22 avisos.
- **H-4** — el mapa del sitio se presenta como v1.4.0 con el estándar en 15.3.0.

Falta **CP-006**: que alguien que no escribió el glosario lea cinco entradas y diga con sus palabras qué es cada una. No la puedo correr yo.

¿Reviso contigo el glosario, o hago el commit de la fase?

### 6 · Usuario — 2026-08-15 00:18:13
> en el glosario no dice qué significa esto: Brief

**Agente** — 2026-08-15 00:19:27
<!-- agente: 470ab3f3-dbdb-4cb9-aaed-3135b8840519 -->

Tiene razón: es un defecto de CA-03. Verifico antes de proponer.

Es un defecto mío, y de CA-03. La entrada dice **qué es el documento**, pero nunca dice **qué significa la palabra**, y "brief" es inglés: debió aparecer en una de las dos tablas de cierre y no aparece en ninguna.

Lo que verifiqué:

- `brief` se usa en 9 archivos de [base/](base/README.md), [plantillas/](plantillas/brief.md) y `skills/`.
- El estándar ya usa **"encargo"**, pero no como sinónimo: en [HU-002](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) el encargo son los tres juntos (brief, épica, historia), y el brief es solo el primero. Así que traducción usada, todavía no tiene.

Lo que haría, y es una decisión tuya porque cambia qué se escribe en `base/`:

1. **Dejarlo en inglés y explicarlo**, como `commit` y `push`. La entrada pasaría a: *"El primer papel: qué quiere resolver el negocio, antes de que exista ninguna solución. `Brief` en inglés es 'breve': es el encargo escrito corto"*. Y entra en la tabla de los que se quedan.
2. **Traducirlo**, con "necesidad escrita" o "encargo inicial", y entra en la tabla de los doce que faltan. Toca los 9 archivos, así que se va con la HU de H-2.

Recomiendo la **1** para esta fase y dejar la 2 abierta en H-2: traducirlo ahora abre un renombrado que ya está declarado fuera de alcance.

¿Cuál aplico? Y de paso: le corregí al resumen el encabezado de cierre, que no era el que el programa espera.

### 7 · Usuario — 2026-08-15 00:19:47
> agregue la columna y ya4

**Agente** — 2026-08-15 00:22:21
<!-- agente: ebaf1751-b7ea-4bb7-ae40-c5868d881cf3 -->

Entiendo: una columna que diga qué quiere decir el nombre, no solo qué es la cosa. La agrego a los cuatro grupos.

Las 22 filas de las tablas de cierre también recibieron la columna y ahí no va. Las devuelvo.

Columna puesta en los cuatro grupos, segunda, después de **Término**.

| Término | Qué quiere decir el nombre | Qué es | … |
|---|---|---|---|
| **Brief** | En inglés, «breve». Es el encargo escrito corto | El primer papel: qué quiere resolver el negocio, antes de que exista ninguna solución | … |
| **Enganche** | Traduce el inglés «hook»: el programa queda enganchado a un momento y se dispara solo | El disparador que hace correr un programa solo | … |
| **Señal** | Como la señal de una carretera: avisa algo que no se ve desde el código | Lo aprendido que no se recupera leyendo el código | … |

29 de las 67 entradas la llevan llena: las que vienen de otro idioma (brief, commit, checklist, suite, enganche, meta-regla) y las que son una metáfora que nadie tiene por qué adivinar (estación, puerta, capa, molde, bitácora, señal, triangulación). Las otras 38 llevan `—`, porque el nombre ya dice qué es.

Las dos tablas de cierre no la llevan: ahí el término **es** la palabra extranjera y la columna sería la misma frase dos veces. Quedó anotado en la entrada 15.3.0 del registro de cambios; no subí versión aparte porque es el mismo cambio sin commitear.

Una cosa que dejo sin tocar: `brief` sigue sin aparecer en la tabla *"Se quedan, porque no tienen traducción usada"*, junto a `commit` y `push`. La columna explica la palabra, pero CA-03 pide además que se pueda listar de una pasada qué sigue en otro idioma. ¿Le agrego esa fila?

### 8 · Usuario — 2026-08-15 00:22:24
> en español cómo se traduciría esto:
>  "Brief de Cimiento"

### 9 · Usuario — 2026-08-15 00:22:47
> reponda

**Agente** — 2026-08-15 00:22:54
<!-- agente: 04937c89-2236-4520-b41a-2990ac1f702b -->

**Encargo de Cimiento.**

Si "Cimiento" es el nombre del proyecto, no se traduce: solo cambia `brief`. Y la palabra que el estándar ya usa para eso es **encargo** — así se llama [HU-002 · Modelos del encargo](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md), que cubre justamente el brief.

Otras salidas, por si prefiere otro matiz:

- **Encargo de Cimiento** — la que recomiendo. Corta, y ya está en uso acá.
- **Necesidad escrita de Cimiento** — dice más, pero pesa en un título.
- **Planteamiento de Cimiento** — sirve si el documento es más análisis que pedido.

Lo que no usaría: *"resumen"*, porque un brief no resume nada previo, y *"informe"*, que es lo contrario: va al final, no al principio.

### 10 · Usuario — 2026-08-15 00:24:33
> es: brief el planteamiento del problema ?

**Agente** — 2026-08-15 00:24:47
<!-- agente: 5faf1717-9a44-4eb7-9bb0-f2db76e3009a -->

Casi, pero se queda corto.

El planteamiento del problema **está adentro** del brief: son sus secciones 1 (necesidad en una frase) y 2 (contexto). Pero el brief trae además lo que un planteamiento no trae:

- Objetivo y criterio de éxito (§3)
- El borde inicial de lo que sí y lo que no (§4)
- Restricciones técnicas y **no negociables** (§5, §7)
- Requerimientos funcionales y casos borde (§6, §8)

Su regla de oro lo dice así en [plantillas/brief.md:10](plantillas/brief.md#L10): *"El brief responde **qué** se necesita y **qué no se negocia**. El **cómo** y el **cuándo** los pone el estándar."*

Un planteamiento del problema responde solo la primera mitad. El brief responde las dos: el problema **y** las condiciones bajo las que se acepta la solución.

Por eso "encargo" le queda mejor que "planteamiento": quien encarga dice qué necesita y bajo qué condiciones, sin decir cómo se hace. Si el título de su documento se llama **Brief de Cimiento**, la traducción fiel sigue siendo **Encargo de Cimiento**.

### 11 · Usuario — 2026-08-15 00:25:53
> entonces esto qué sería: Brief de Cimiento dentro del bief?

**Agente** — 2026-08-15 00:26:10
<!-- agente: 90355cda-8e4c-421f-8931-308251c00b08 -->

Depende de qué sea ese "dentro", y hay dos lecturas.

**Si es el encabezado del propio documento:** es el título, no una sección. La plantilla lo escribe así: `# Brief — «Nombre del módulo / épica»` ([plantillas/brief.md:1](plantillas/brief.md#L1)). Traducido: **Encargo — Cimiento**. No va repetido adentro.

**Si es un bloque anidado que nombra una parte del trabajo:** en el estándar un brief no contiene otro brief. Hay uno por módulo o por épica ([plantillas/brief.md:6](plantillas/brief.md#L6)). Lo que sí vive dentro es §10 *Épicas derivadas*, que es donde el brief se parte hacia abajo. Si "Cimiento" es una de esas partes, no es un brief: es una **épica**, y se escribe con [plantillas/epica.md](plantillas/epica.md), apuntando de vuelta al brief padre.

¿Cuál de las dos es? Si me dice el archivo, lo miro y le digo qué es en concreto.

### 12 · Usuario — 2026-08-15 00:26:24
> osea el título?

**Agente** — 2026-08-15 00:26:26
<!-- agente: 48b73f44-054c-4652-9b08-733ec89fabb4 -->

Sí, el título.

**Encargo — Cimiento**, siguiendo el formato de la plantilla: `# Brief — «Nombre del módulo / épica»` ([plantillas/brief.md:1](plantillas/brief.md#L1)).

Va una sola vez, arriba del documento. Dentro no se repite.

### 13 · Usuario — 2026-08-15 00:27:04
> no es un módulo es el proyecto del agente y quiero darle nombre

**Agente** — 2026-08-15 00:27:25
<!-- agente: ead6ba98-b21c-4ba9-9c47-18425be5efed -->

Entonces el título del [brief.md](brief.md), que hoy dice `# Brief del agente`, quedaría:

```
# Encargo — Cimiento
```

Es el mismo formato de la plantilla (`# Brief — «Nombre»`), con `brief` traducido a **encargo** y el nombre del proyecto en el lugar del módulo.

Dos cosas antes de que decida:

- **El nombre no vive solo en el brief.** Hoy el proyecto se llama "el agente" o "el estándar" en el [README.md](README.md), el [CLAUDE.md](CLAUDE.md), el [glosario](base/glosario.md) y las siete épicas. Ponerle "Cimiento" es un cambio de nombre en cadena, no una línea. Vale la pena mirarlo como una fase con su plan.
- **Cimiento choca de frente con un término que ya usa el estándar:** "la base" es la carpeta [base/](base/README.md). Cimiento y base quieren decir lo mismo, y quien lea *"Cimiento hereda su base"* va a tener que preguntar cuál es cuál.

¿Le doy dos o tres alternativas de nombre que no choquen, o se queda con Cimiento y armamos la fase del renombrado?

### 14 · Usuario — 2026-08-15 00:27:59
> pero encargo no es muy diciente y recuerde que es español colombiano

**Agente** — 2026-08-15 00:28:31
<!-- agente: 28f11785-8574-4e59-a68e-4a938853e395 -->

Tiene razón: "encargo" dice quién pide, no qué trae. Y en Colombia suena a mandado.

Tres que sí son dicientes, en español de acá:

| Título | Qué le dice a quien lo ve | Riesgo |
|---|---|---|
| **Planteamiento — Cimiento** | Acá está puesto el problema y las condiciones. Se entiende sin explicar | Ninguno serio |
| **Pedido — Cimiento** | Lo más llano de los tres. Un niño lo entiende | Suena a pedido de tienda o de restaurante |
| **Punto de partida — Cimiento** | Dice **cuándo** se escribe, antes de todo lo demás | No dice qué trae adentro |

Recomiendo **Planteamiento**. Antes le dije que "planteamiento del problema" se quedaba corto, y es cierto — pero lo que lo encogía era el *"del problema"*. Suelto, "el planteamiento de Cimiento" abarca las dos mitades que el brief exige: qué se necesita y qué no se negocia.

Y una cuarta salida legítima: **dejarlo en `brief`**, como `commit` y `push`. Se usa así en las agencias colombianas, y [`01·C20`](base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) lo permite si se explica la primera vez. La diferencia es que `commit` no tiene traducción usada y `brief` sí tiene tres.

¿Con cuál se queda?

### 15 · Usuario — 2026-08-15 00:30:16
> entonces debe haber una parte donde diga nombre del proyecto y ese debe ser: Cimiento

**Agente** — 2026-08-15 00:31:21
<!-- agente: c202a78a-7390-4212-a38d-3e249dd734e4 -->

No la hay: la plantilla solo tiene el título, y ese título nombra el **módulo o la épica**, no el proyecto. Se lo agrego.

Hecho. El proyecto ya tiene dónde llamarse, y se llama **Cimiento**.

- **[plantillas/brief.md](plantillas/brief.md)** gana una sección 0 · Identificación: nombre del proyecto, qué cubre el encargo y fecha. Antes el nombre solo estaba en el título, y ese título nombra el módulo o la épica.
- **[brief.md](brief.md)** la estrena con `Cimiento`.
- **Versión 15.4.0** (MENOR, aditivo) con su entrada en el [CHANGELOG.md](CHANGELOG.md).

Lo que **no** toqué, y por qué:

- **El título del brief** sigue diciendo `# Brief del agente`. Falta que escoja la palabra: Planteamiento, Pedido, Punto de partida, o dejar `brief`.
- **El resto del repositorio** sigue diciendo "el agente" y "el estándar": [README.md](README.md), [CLAUDE.md](CLAUDE.md), el [glosario](base/glosario.md) y las siete épicas. Eso es un renombrado en cadena y merece su fase con plan, no una tanda de reemplazos.

Y le repito la objeción una sola vez, porque después no la vuelvo a sacar: **Cimiento y "base" quieren decir lo mismo**, y `base/` es una carpeta central del proyecto. *"Cimiento hereda su base"* va a obligar a preguntar cuál es cuál. Si aun así le gusta el nombre, seguimos con él.

¿Escojo yo la palabra del título, o me la dice?
