# Pendiente · Las reglas no tienen fecha de revisión

**Estado:** cerrado el 2026-08-19 · anotado 2026-08-13.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-007 — La regla que gobierna cómo se escriben las reglas](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) — la vigencia de una regla es una exigencia sobre cómo se escribe y se mantiene una regla |

Ponerle a cada regla de `base/` una fecha de última revisión, y un reporte que liste las que llevan mucho sin que nadie las vuelva a mirar.

## El problema

Una regla se escribe una vez y se queda. El único momento en que se vuelve a leer es cuando alguien la va a citar o la va a cambiar. Mientras tanto, el mundo que la regla describía se mueve: cambia la herramienta que la regla nombra, cambia la práctica que daba por buena, o el problema que venía a evitar deja de ocurrir.

Cuando eso pasa, no se rompe nada. La regla sigue ahí, sigue pasando su checklist, y el agente la sigue obedeciendo. Ese silencio es el problema: una regla equivocada se comporta exactamente igual que una correcta.

El sello que hoy trae cada regla no cubre esto. Dice:

> Vale mientras el texto de arriba no cambie.

Es decir, protege contra que **la regla** cambie. No dice nada de que cambie **el mundo**.

## De dónde sale

De los apuntes del diplomado, módulo 2, nota de clase sobre la administración de la IA, donde el ciclo de vida termina en dos tramos que el estándar aplica a medias:

- **Monitoreo.** «Un modelo que ayer acertaba puede fallar hoy sin que nada se rompa: cambió la realidad que retrataban los datos, no el código.» Eso allá se llama deriva. Acá es lo mismo con reglas en vez de modelos.
- **Retiro.** «¿Cuándo se apaga?» El estándar ya sabe cómo derogar una regla ([`20·M11`](../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)), pero nada le hace la pregunta.

El estándar ya reconoció este problema una vez, y lo resolvió solo para la memoria: el pendiente 02 le puso vigencia a las señales precisamente para que no se degradaran solas de dato útil a ruido ([pendientes/hecho/vigencia-y-poda-de-memoria.md](vigencia-y-poda-de-memoria.md)). Las reglas, que pesan mucho más, no recibieron el mismo tratamiento.

## Qué habría que construir

**1. La fecha.** Una línea en el bloque de checklist que ya tiene cada regla: cuándo se revisó por última vez contra la realidad, que es distinto de cuándo se aplicó el checklist de forma. Es un dato, no un documento.

**2. El reporte.** Un modo de `validar.py` o de `metricas.py` que liste las reglas ordenadas por antigüedad de esa fecha. Sin umbral fijo al principio: primero se mira la lista y después se decide cada cuánto conviene revisar, porque un umbral inventado produce una alarma que se aprende a ignorar.

**3. Las tres preguntas de la revisión.** Cortas, para que revisar no cueste más que escribir:

- ¿Sigue existiendo el problema que esta regla evita?
- ¿Lo que la regla manda hacer sigue siendo la mejor forma de evitarlo?
- ¿Alguien la incumplió en este período, y por qué?

**4. El cruce con los hallazgos.** El ítem 11 del [pendiente 09](autonomia-sin-ia.md) propone contar hallazgos por regla. Cruzado con la fecha de revisión, sirve para ordenar: una regla vieja que falla todo el tiempo se revisa primero, y una regla vieja que no ha fallado nunca hay que mirarla por el motivo contrario, porque puede que ya nadie la esté aplicando.

## El límite

Decidir si una regla sigue valiendo es criterio, y nada lo automatiza. Lo que un programa hace es lo mecánico: leer la fecha, restar y ordenar la lista. Poner la pregunta enfrente de alguien ya es la mitad del trabajo.

---

## Construido — 2026-08-19

**Los cuatro puntos, y el eslabón que faltaba antes de poder empezar.**

### Primero hubo que escribir el criterio de aceptación

**Ninguno de los tres criterios de [EP-001 · HU-007](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) cubría esto.** `CA-01`, `CA-02` y `CA-03` revisan una regla **al entrar** —dónde va, si es agnóstica, si exige una sola cosa— y ninguno vuelve a mirarla después. Construir sin criterio habría sido saltarse [`02·F18`](../../base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md).

Se escribió el **`CA-04`**, y de ahí salió todo lo demás.

### Qué quedó

| Lo que pedía | Dónde está |
|---|---|
| 1 · La fecha | Una línea al final del sello: `> Revisada contra la realidad el AAAA-MM-DD.` |
| 2 · El reporte | [`validadores/vigencia.py`](../../validadores/vigencia.py) y `validar.py vigencia` |
| 3 · Las tres preguntas | [`base/20-meta-reglas/revision-de-vigencia.md`](../../base/20-meta-reglas/revision-de-vigencia.md) |
| 4 · El cruce con los hallazgos | La columna `FALLA HOY` de la lista, que ordena junto con la fecha |

**La fecha arranca ausente en las 245, a propósito.** Ponérsela de una vez a todas habría sido escribir 245 fechas que no responden por ninguna revisión: el sello vacío que este pendiente viene a evitar. Lo que la lista muestra desde el primer día es cuáles no la tienen, que son todas.

**Sin umbral, como pedía el pendiente.** Y `validar.py vigencia` **nunca falla**: informa. Hay una prueba que lo fija, porque es la decisión que hace útil el reporte y la que se pierde en la primera pasada de "mejorarlo".

**El aviso sale una sola vez, no 245.** Doscientos cuarenta y cinco avisos idénticos entierran los hallazgos que sí piden acción.

### Un intento que salió mal, y qué enseñó

**La primera versión ordenaba por el último commit que tocó el archivo, y salió inservible:** la limpieza tipográfica de esta misma mañana había tocado las 245 reglas, así que **todas parecían recién escritas**.

Una fecha que se mueve cuando se cambia una raya por un guion no mide cuándo alguien miró la regla. **La del sello sí lo mide, y ya estaba escrita en todas** — es el día que alguien se sentó a leerla entera. No es lo mismo que revisarla contra la realidad, por eso este módulo existe; pero para ordenar la fila es exactamente el dato.

Es la misma lección de esta semana, por quinta vez: **la respuesta ya estaba escrita** (`01·C23`).

### Y pedirla destapó otra cosa

**Siete reglas no tienen sello:** `F4.1` a `F4.5`, `F6` y `F7`. Nacieron de partir reglas más grandes y el paso de aplicarles el checklist se saltó. Encabezan la lista, que es donde tienen que estar.

Va anotado acá y no como pendiente nuevo: son siete reglas del [pendiente 19](../19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que es el que lleva la cuenta de las que no cumplen el capítulo 20.

### El límite, dicho claro

**Decidir si una regla sigue valiendo es criterio, y nada lo automatiza.** Lo que el programa hace es lo mecánico: leer la fecha, restar y ordenar. Poner la pregunta enfrente de alguien ya es la mitad del trabajo — y era la mitad que no existía.
