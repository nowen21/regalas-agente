# Pendientes del estándar

Backlog de mejoras del estándar del agente que aún no se implementan. Un archivo por ítem, **numerado en el orden en que conviene ejecutarlos**. Al cerrar un pendiente, se implementa en la base/plantillas/skills y se borra su archivo de aquí (o se marca como hecho con la fecha).

Lo ya cerrado se registra en la carpeta **[hecho/](hecho/)** — un archivo por tema, nombrado por lo que resuelve. Es la contraparte de este backlog: allí se ve lo hecho, aquí lo que falta.

**El número es el orden, no la prioridad.** Los pendientes se ejecutan de menor a mayor porque cada uno se apoya en los anteriores. Al cerrar uno, el número no se reutiliza ni se renumeran los demás: los huecos son historia.

## Abiertos

### Garantía y sostenimiento del estándar (01–06, en orden)

| # | Pendiente | Qué resuelve | Por qué va aquí |
|---|---|---|---|
| 01 | [Validadores de código de proyecto](01-validadores-de-codigo-de-proyecto.md) | Los validadores que faltan: los que leen el código/config del proyecto o corren una herramienta (linter, pruebas, audit), más las puertas de flujo. | Primero: cierra la brecha entre "el estándar dice" y "el estándar se cumple", y produce los datos que necesita el 06. La **base ya está hecha** ([hecho/validadores-y-hooks.md](hecho/validadores-y-hooks.md)): hooks + validadores de documentación y estructura. Aquí queda la mitad que necesita un proyecto real. |
| ~~02~~ | **hecho** → [Vigencia y poda de la memoria](hecho/vigencia-y-poda-de-memoria.md) | Vigencia (`revisada`), marca de sin-verificar, recencia en `search`, comandos `revisar`/`archivar`. | Evitaba que la memoria se degrade sola de activo a ruido. Cerrado 2026-08-06 (la detección de contradicciones se movió al 05). |
| ~~03~~ | **hecho** → [Ciclo de vida de pendientes y deuda](hecho/ciclo-de-vida-de-pendientes.md) | Estado `cerrada` + `cerrada_en`/`cierra_ref`; comandos `pendientes` / `cerrar`. | Cierra lo que el agente difiere (deuda, preguntas). Cerrado 2026-08-06, sobre el gancho de migración del 02. |
| ~~04~~ | **hecho** → [Versión del estándar](hecho/version-del-estandar.md) | `VERSION` + `CHANGELOG`, fijación por proyecto, retroactividad y validador de desfase. | "El proyecto cumple el estándar" pasa a tener fecha. Cerrado 2026-08-06. |
| ~~05~~ | **hecho** → [Memoria semántica](hecho/memoria-semantica.md) | Búsqueda híbrida (FTS5 ∪ semántica) local y opcional; `model2vec` + coseno en numpy. | Encuentra por significado lo que la palabra no alcanza. Cerrado 2026-08-06 (la detección de contradicciones queda como mejora sobre esta base). |
| ~~06~~ | **hecho** → [Métricas del proceso](hecho/metricas-del-proceso.md) | Lee `senales.db` y reporta deuda abierta/cerrada, vigencia y pulso de señales. | Para decidir qué reglas cambiar, no para calificar. Cerrado 2026-08-06 (falta lo que necesita instrumentación nueva). |

### Patrones opt-in de dominio (07–08 y 12, fuera de la fila)

| # | Pendiente | Qué resuelve |
|---|---|---|
| ~~07~~ | **hecho** → [Patrones DevOps 18 y 19](hecho/patrones-devops.md) | Capítulos opt-in `18` (despliegue/infra) y `19` (observabilidad/operación) + plantillas. Cerrado 2026-08-06 (v1.1.0). |
| 08 | [Patrón RPA](08-patrones-rpa.md) | Patrón opt-in para desarrollar soluciones RPA (bots): diseño, orquestación, resiliencia, credenciales, pruebas y gobernanza. |
| 12 | [Patrón IA](12-patron-ia.md) | Capítulo opt-in `21` para proyectos que construyen con IA: ciclo de vida del modelo, inventario, clasificación por riesgo, dueño, explicabilidad, sesgo y monitoreo de deriva. |

Estos tres **no dependen de 01–06 ni entre sí**. Van numerados al final porque agregan *cobertura*, mientras que 01–06 agregan *garantía* sobre la cobertura existente. Si un proyecto real necesita DevOps, RPA o IA, se adelantan sin esperar la fila.

### Backlog temático (09)

| # | Pendiente | Qué resuelve |
|---|---|---|
| 09 | [Autonomía sin IA](09-autonomia-sin-ia.md) | Inventario de 16 automatizaciones para lo que hoy depende de que el agente se acuerde: versionado, secretos en el histórico, sello de puertas, manifiesto de convenciones, gate `F2`, instrumentación de métricas y andamiaje de fases. |

**No es un ítem, es un tema.** Cada una de sus 16 propuestas se promueve a su propio pendiente numerado cuando se vaya a construir; el `09` reserva el lugar del tema en la fila, no de las tareas. Comparte frontera con el 01: aquel cubre los validadores que faltan, este cubre todo lo demás que podría dejar de depender de la IA.

### Ideas por desarrollar (10)

| # | Pendiente | Qué resuelve |
|---|---|---|
| 10 | [Ideas](10-ideas.md) | Ideas del usuario todavía sin desarrollar. La 2 —que la sesión pida el nombre con el que se guarda— **quedó hecha** en la v6.1.0: el enganche del histórico lo recuerda una sola vez y `historico.py --renombrar` hace el cambio. |

**Tampoco es un ítem.** Es la libreta: cada idea se promueve a su propio pendiente numerado cuando se vaya a construir.

### Deuda que dejó una regla nueva (11)

| # | Pendiente | Qué resuelve |
|---|---|---|
| 11 | [Limpiar los marcadores de IA del texto del estándar](11-limpiar-marcadores-de-ia-del-texto-del-estandar.md) | `00·ID8` (v7.0.0) prohíbe las marcas de generación automática, y el texto ya escrito de `base/` y `plantillas/` las trae. La norma no reabre lo cerrado, pero mientras no se limpie el estándar enseña lo contrario de lo que pide. |

Depende del validador de la parte mecánica de `ID8`: sin él, el recuento sobre 200 archivos se hace a mano.

### El estándar aplicado a sí mismo (13–16)

Cuatro huecos que salieron de leer los apuntes del diplomado de IA (`Escom/.../proyecto-grado/diplomado-ia/`) contra este repo. Son la primera aplicación de la idea 1 de [10-ideas](10-ideas.md): que lo que el usuario aprende en el posgrado entre al estándar. Los cuatro parten de lo mismo, y es que el estándar le exige a los proyectos cosas que no se exige a sí mismo.

| # | Pendiente | Qué resuelve |
|---|---|---|
| 13 | [Inventario y riesgo de las acciones del agente](13-inventario-y-riesgo-de-las-acciones-del-agente.md) | Nadie ha listado todo lo que el agente puede hacer. `N1` a `N6` cubren los casos que dolieron, y todo lo demás cae en una sola exigencia pareja que en la práctica se aprueba en bloque. |
| 14 | [Las reglas no tienen fecha de revisión](14-las-reglas-no-tienen-fecha-de-revision.md) | Una regla que dejó de valer se comporta igual que una correcta: nada se rompe. La memoria ya recibió vigencia en el pendiente 02; las reglas no. |
| 15 | [El estándar depende de una sola herramienta](15-el-estandar-depende-de-una-sola-herramienta.md) | Las reglas son portables, lo que las hace cumplir no. Hoy no hay ni un mapa de cuáles piezas están amarradas a Claude Code. |
| 16 | [Primero que el proceso sirva, después se automatiza](16-primero-que-el-proceso-sirva-despues-se-automatiza.md) | Al 09 le falta el criterio de *si conviene* automatizar, no solo *si se puede*. Automatizar una regla mal escrita la congela y la pone a fallar sola. |

**El 13 conviene primero:** es una lista y una tabla, y el 12 reusa esa misma tabla de riesgo para los modelos de un proyecto. El 16 se resuelve al escribirlo, no construyendo nada.

### Lo que dejaron las sesiones del 2026-08-14 (17–25)

Del 17 al 22 salieron de trabajar el pendiente 01, y quedaron en su [resumen](../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md). Del 23 al 25 salieron de cerrar el hallazgo H-4 de esa sesión, y quedaron en el [suyo](../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

| # | Pendiente | Qué resuelve |
|---|---|---|
| 17 | [Las señales no tienen dónde escribirse](17-las-senales-no-tienen-donde-escribirse.md) | `13·DOC5` manda registrar lo aprendido y el archivo no existía. Falta el enganche que lo recuerde en el momento. |
| 18 | [Los enlaces del estándar no cumplen `DOC14`](18-los-enlaces-del-estandar-no-cumplen-doc14.md) | 354 enlaces del propio estándar cuyo texto no dice dónde vive el archivo. |
| 19 | [El capítulo 20 no se cumple a sí mismo](19-el-capitulo-20-no-se-cumple-a-si-mismo.md) | De 188 reglas, 129 sin checklist, 7 publicadas en "no cumple" y 33 sin clasificar. |
| 20 | [`F2` no dice cuándo no aplica](20-f2-no-dice-cuando-no-aplica.md) | Dos fases seguidas se abrieron sin especificación con buenos motivos, y la regla no las contempla. |
| 21 | [El glosario, y lo que quedó en inglés](21-el-glosario-y-los-terminos-en-ingles.md) | Los trece roles siguen en inglés y no hay glosario de la terminología del estándar. |
| 22 | [Dos sesiones versionando a la vez](22-dos-sesiones-versionando-a-la-vez.md) | Dos sesiones abiertas dejaron dos numeraciones vivas en el mismo archivo. |
| 23 | [La carpeta de plantillas mezcla modelos con procedimientos](23-plantillas-mezcla-modelos-con-procedimientos.md) | Un procedimiento vive entre los modelos; los otros tres archivos sin marca resultaron estar bien. |
| 24 | [Buscar en el repositorio antes de preguntar](24-buscar-en-el-repositorio-antes-de-preguntar.md) | Se preguntó un orden de trabajo que ya estaba escrito en la sección de dependencias de la historia. |
| 25 | [Las reglas de cómo se escribe llegan en el índice, no puestas](25-las-reglas-de-como-se-escribe-van-en-el-indice.md) | **Cerrado por falso el 2026-08-15:** `ID8` sí llegaba completa y se incumplió igual. Lo que falta quedó en EP-005 · HU-010 y EP-004 · HU-013. |
| 26 | [«Corrida» es jerga y no está definida](26-corrida-y-ejecucion-en-el-estandar.md) | El estándar llama «corrida» a ejecutar las pruebas y no dice qué es; en el glosario no existe como término propio. |
| 27 | [La fase A de EP-003 · HU-010 cerró sin cumplir](27-la-fase-a-de-hu-010-cerro-sin-cumplir.md) | `RNF-01` sin caso ejecutado y 16 de 35 pasos sin registro de qué salió. El veredicto real es «No cumple». |
| 28 | [El veredicto de la fase vive en dos sitios](28-el-veredicto-de-la-fase-vive-en-dos-sitios.md) | El `resultado_pruebas` y el `estado-fase` lo escriben a mano cada uno, y ya dicen cosas distintas. |
| 29 | [La transcripción se escribió dos veces, y con horas inventadas](29-la-transcripcion-se-escribio-dos-veces.md) | El enganche ya escribe el histórico y el agente lo escribió otra vez a mano: 61 encabezados de usuario para 30 mensajes, y horas estimadas en vez de leídas del reloj. |

**El 21 conviene primero:** con el glosario escrito se ve qué más está en inglés sin necesidad y se cambia todo de una vez.

### Lo que dejó revisar el histórico (31–32)

Salieron de contar qué sesiones tienen resumen y cuáles no, y quedaron en el [resumen de esa sesión](../historico-chat/resumenes/2026-08-15/los-resumenes-que-faltan.md).

| # | Pendiente | Qué resuelve |
|---|---|---|
| 31 | [33 de las 39 sesiones no tienen resumen](31-los-resumenes-de-las-sesiones-viejas.md) | El enganche solo cubre la sesión que corre; de las anteriores no se ocupa nadie. Antes hay que nombrar 22 sesiones y decidir cómo se llenan cuatro campos hacia atrás. |
| 32 | [La carpeta del día nace sin su línea en el índice](32-la-carpeta-del-dia-nace-sin-su-linea-en-el-indice.md) | El enganche crea la carpeta y el archivo, pero no los anota. El 2026-08-15 ya tiene dos resúmenes que el índice no nombra. |

**El 32 va antes del 31:** si no, los 33 resúmenes nacen fuera del índice y hay que volver a pasar por todos.

## Dependencias duras

Todo lo demás es preferencia y se puede reordenar:

- **02 → 05.** ✅ resuelta: el 02 (vigencia) ya está, así que la memoria semántica arranca sin recuperar más ruido del necesario.
- **02 → 03.** El 02 dejó el gancho de migración (`memoria.py · migrar()`) y `estado` abierto; el 03 suma `'cerrada'` sin migrar de nuevo.
