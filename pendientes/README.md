# Pendientes del estándar

Backlog de mejoras del estándar del agente que aún no se implementan. Un archivo por ítem, **numerado en el orden en que conviene ejecutarlos**. Al cerrar un pendiente, se implementa en la base/plantillas/skills y se borra su archivo de aquí (o se marca como hecho con la fecha).

Lo ya cerrado se registra en la carpeta **[hecho/](hecho/)** — un archivo por tema, nombrado por lo que resuelve. Es la contraparte de este backlog: allí se ve lo hecho, aquí lo que falta.

**El número es el orden, no la prioridad.** Los pendientes se ejecutan de menor a mayor porque cada uno se apoya en los anteriores. Al cerrar uno, el número no se reutiliza ni se renumeran los demás: los huecos son historia.

## La prioridad va en la columna `P`

El número dice en qué orden **se puede** construir, o sea qué se apoya en qué. La `P` dice qué tan urgente es **hoy**. No son lo mismo, y por eso son dos columnas y no una: si el número absorbiera la prioridad habría que renumerar, y renumerar rompe los enlaces de los pendientes que se citan entre sí.

| P | Qué significa |
|---|---|
| **P0** | Se está perdiendo algo, o el daño se sigue produciendo cada día que pasa |
| **P1** | Un documento del estándar afirma algo que no es cierto |
| **P2** | Barato, y evita volver a hacer a mano el mismo trabajo |
| **P3** | Falta una decisión escrita: nadie puede construir hasta que se tome |
| **P4** | Limpieza de texto ya escrito. Grande, mecánica, no bloquea nada |
| **P5** | Construcción grande. Se adelanta cuando haya un proyecto que la pida |
| **P6** | Cobertura opt-in sin demanda hoy |
| — | Cerrado |

Priorizado el **2026-08-16** sobre los 31 abiertos. **La `P` envejece:** se revisa al cerrar un pendiente, que es cuando cambia lo que sigue. Dos ítems llevan la `P` de su punto más urgente y no la del archivo entero — el `29` y el `33`, que no son un pendiente sino varios.

## Abiertos

### Garantía y sostenimiento del estándar (01–06, en orden)

| # | P | Pendiente | Qué resuelve | Por qué va aquí |
|---|---|---|---|---|
| 01 | **P5** | [Validadores de código de proyecto](01-validadores-de-codigo-de-proyecto.md) | Los validadores que faltan: los que leen el código/config del proyecto o corren una herramienta (linter, pruebas, audit), más las puertas de flujo. | Primero: cierra la brecha entre "el estándar dice" y "el estándar se cumple", y produce los datos que necesita el 06. La **base ya está hecha** ([hecho/validadores-y-hooks.md](hecho/validadores-y-hooks.md)): hooks + validadores de documentación y estructura. Aquí queda la mitad que necesita un proyecto real. Cinco de los nueve que faltan **no arrancan sin el ítem 04 del [09](09-autonomia-sin-ia.md)** —el manifiesto de convenciones—: sin él no hay contra qué comparar. |
| ~~02~~ | — | **hecho** → [Vigencia y poda de la memoria](hecho/vigencia-y-poda-de-memoria.md) | Vigencia (`revisada`), marca de sin-verificar, recencia en `search`, comandos `revisar`/`archivar`. | Evitaba que la memoria se degrade sola de activo a ruido. Cerrado 2026-08-06 (la detección de contradicciones se movió al 05). |
| ~~03~~ | — | **hecho** → [Ciclo de vida de pendientes y deuda](hecho/ciclo-de-vida-de-pendientes.md) | Estado `cerrada` + `cerrada_en`/`cierra_ref`; comandos `pendientes` / `cerrar`. | Cierra lo que el agente difiere (deuda, preguntas). Cerrado 2026-08-06, sobre el gancho de migración del 02. |
| ~~04~~ | — | **hecho** → [Versión del estándar](hecho/version-del-estandar.md) | `VERSION` + `CHANGELOG`, fijación por proyecto, retroactividad y validador de desfase. | "El proyecto cumple el estándar" pasa a tener fecha. Cerrado 2026-08-06. |
| ~~05~~ | — | **hecho** → [Memoria semántica](hecho/memoria-semantica.md) | Búsqueda híbrida (FTS5 ∪ semántica) local y opcional; `model2vec` + coseno en numpy. | Encuentra por significado lo que la palabra no alcanza. Cerrado 2026-08-06 (la detección de contradicciones queda como mejora sobre esta base). |
| ~~06~~ | — | **hecho** → [Métricas del proceso](hecho/metricas-del-proceso.md) | Lee `senales.db` y reporta deuda abierta/cerrada, vigencia y pulso de señales. | Para decidir qué reglas cambiar, no para calificar. Cerrado 2026-08-06 (falta lo que necesita instrumentación nueva). |

### Patrones opt-in de dominio (07–08 y 12, fuera de la fila)

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| ~~07~~ | — | **hecho** → [Patrones DevOps 18 y 19](hecho/patrones-devops.md) | Capítulos opt-in `18` (despliegue/infra) y `19` (observabilidad/operación) + plantillas. Cerrado 2026-08-06 (v1.1.0). |
| 08 | **P6** | [Patrón RPA](08-patrones-rpa.md) | Patrón opt-in para desarrollar soluciones RPA (bots): diseño, orquestación, resiliencia, credenciales, pruebas y gobernanza. |
| 12 | **P6** | [Patrón IA](12-patron-ia.md) | Capítulo opt-in `21` para proyectos que construyen con IA: ciclo de vida del modelo, inventario, clasificación por riesgo, dueño, explicabilidad, sesgo y monitoreo de deriva. Está casi listo para redactarse, y reusa la tabla de riesgo del [13](13-inventario-y-riesgo-de-las-acciones-del-agente.md). |

Estos tres **no dependen de 01–06 ni entre sí**. Van numerados al final porque agregan *cobertura*, mientras que 01–06 agregan *garantía* sobre la cobertura existente. Si un proyecto real necesita DevOps, RPA o IA, se adelantan sin esperar la fila.

### Backlog temático (09)

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 09 | **P5** | [Autonomía sin IA](09-autonomia-sin-ia.md) | Inventario de 16 automatizaciones para lo que hoy depende de que el agente se acuerde: versionado, secretos en el histórico, sello de puertas, manifiesto de convenciones, gate `F2`, instrumentación de métricas y andamiaje de fases. |

**No es un ítem, es un tema.** Cada una de sus 16 propuestas se promueve a su propio pendiente numerado cuando se vaya a construir; el `09` reserva el lugar del tema en la fila, no de las tareas. Comparte frontera con el 01: aquel cubre los validadores que faltan, este cubre todo lo demás que podría dejar de depender de la IA.

**Tres de sus 16 valen más que el P5 del conjunto**, porque son de prioridad alta y costo bajo: el `01` (guardián de versión y CHANGELOG), el `02` (barrido de secretos en el histórico) y el `03` (sello de puerta por CLI). Suben cuando se promuevan a pendiente propio, y pasan antes por el filtro del [16](16-primero-que-el-proceso-sirva-despues-se-automatiza.md).

### Ideas por desarrollar (10)

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 10 | **P6** | [Ideas](10-ideas.md) | Ideas del usuario todavía sin desarrollar. La 2 —que la sesión pida el nombre con el que se guarda— **quedó hecha** en la v6.1.0: el enganche del histórico lo recuerda una sola vez y `historico.py --renombrar` hace el cambio. |

**Tampoco es un ítem.** Es la libreta: cada idea se promueve a su propio pendiente numerado cuando se vaya a construir. Su idea 1 —que lo del posgrado entre al estándar— ya está produciendo: de ahí salieron los pendientes 12 al 16.

### Deuda que dejó una regla nueva (11)

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 11 | **P4** | [Limpiar los marcadores de IA del texto del estándar](11-limpiar-marcadores-de-ia-del-texto-del-estandar.md) | `00·ID8` (v7.0.0) prohíbe las marcas de generación automática, y el texto ya escrito de `base/` y `plantillas/` las trae. La norma no reabre lo cerrado, pero mientras no se limpie el estándar enseña lo contrario de lo que pide. |

Depende del validador de la parte mecánica de `ID8`: sin él, el recuento sobre 200 archivos se hace a mano. **Bloqueado de hecho** — no se mueve hasta que el script exista.

### El estándar aplicado a sí mismo (13–16)

Cuatro huecos que salieron de leer los apuntes del diplomado de IA (`Escom/.../proyecto-grado/diplomado-ia/`) contra este repo. Son la primera aplicación de la idea 1 de [10-ideas](10-ideas.md): que lo que el usuario aprende en el posgrado entre al estándar. Los cuatro parten de lo mismo, y es que el estándar le exige a los proyectos cosas que no se exige a sí mismo.

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 13 | **P3** | [Inventario y riesgo de las acciones del agente](13-inventario-y-riesgo-de-las-acciones-del-agente.md) | Nadie ha listado todo lo que el agente puede hacer. `N1` a `N6` cubren los casos que dolieron, y todo lo demás cae en una sola exigencia pareja que en la práctica se aprueba en bloque. **El más rentable de su nivel:** es una lista y una tabla, y desbloquea el ítem 15 del 09 y toda la clasificación de riesgo del 12. |
| 14 | **P3** | [Las reglas no tienen fecha de revisión](14-las-reglas-no-tienen-fecha-de-revision.md) | Una regla que dejó de valer se comporta igual que una correcta: nada se rompe. La memoria ya recibió vigencia en el pendiente 02; las reglas no. Real, pero con reglas escritas hace días todavía no hay nada vencido: gana valor con el tiempo. |
| 15 | **P5** | [El estándar depende de una sola herramienta](15-el-estandar-depende-de-una-sola-herramienta.md) | Las reglas son portables, lo que las hace cumplir no. Hoy no hay ni un mapa de cuáles piezas están amarradas a Claude Code. **Su punto 1 —el mapa en `anatomia/`— es de una tarde y sube a P3**; los puntos 2 y 3 son abstracción antes de tener el segundo caso. |
| 16 | **P3** | [Primero que el proceso sirva, después se automatiza](16-primero-que-el-proceso-sirva-despues-se-automatiza.md) | Al 09 le falta el criterio de *si conviene* automatizar, no solo *si se puede*. Automatizar una regla mal escrita la congela y la pone a fallar sola. **Se resuelve escribiéndolo**, no construyendo nada, y es puerta de todo el 09. |

**El 13 conviene primero:** es una lista y una tabla, y el 12 reusa esa misma tabla de riesgo para los modelos de un proyecto. El 16 se resuelve al escribirlo, no construyendo nada.

### Lo que dejaron las sesiones del 2026-08-14 (17–25)

Del 17 al 22 salieron de trabajar el pendiente 01, y quedaron en su [resumen](../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md). Del 23 al 25 salieron de cerrar el hallazgo H-4 de esa sesión, y quedaron en el [suyo](../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 17 | **P3** | [Las señales no tienen dónde escribirse](17-las-senales-no-tienen-donde-escribirse.md) | `13·DOC5` manda registrar lo aprendido y el archivo no existía. Falta el enganche que lo recuerde en el momento. |
| 18 | **P4** | [Los enlaces del estándar no cumplen `DOC14`](18-los-enlaces-del-estandar-no-cumplen-doc14.md) | 354 enlaces del propio estándar cuyo texto no dice dónde vive el archivo. `F21` ya cortó el crecimiento —la cuenta no sube— y quedan unos 200 reales. |
| 19 | **P1** | [El capítulo 20 no se cumple a sí mismo](19-el-capitulo-20-no-se-cumple-a-si-mismo.md) | De 188 reglas, 129 sin checklist, 7 publicadas en "no cumple" y 33 sin clasificar. **Se parte:** clasificar las 33 es una tarde, las 129 es trabajo largo y por capítulo. |
| 20 | **P3** | [`F2` no dice cuándo no aplica](20-f2-no-dice-cuando-no-aplica.md) | Dos fases seguidas se abrieron sin especificación con buenos motivos, y la regla no las contempla. **Va junto con el 30:** las dos son reglas de cadena que la práctica salta. |
| 21 | **P4** | [El glosario, y lo que quedó en inglés](21-el-glosario-y-los-terminos-en-ingles.md) | Los trece roles siguen en inglés y no hay glosario de la terminología del estándar. El glosario —su mitad cara— ya está hecho y dejó el inventario de los 12 que faltan. |
| 22 | **P3** | [Dos sesiones versionando a la vez](22-dos-sesiones-versionando-a-la-vez.md) | Dos sesiones abiertas dejaron dos numeraciones vivas en el mismo archivo. No lo resuelve un validador: hace falta el acuerdo, y son tres opciones sobre la mesa. |
| 23 | **P2** | [La carpeta de plantillas mezcla modelos con procedimientos](23-plantillas-mezcla-modelos-con-procedimientos.md) | Un procedimiento vive entre los modelos; los otros tres archivos sin marca resultaron estar bien. Ya está decidido qué se hace: solo falta ejecutarlo. |
| 24 | **P3** | [Buscar en el repositorio antes de preguntar](24-buscar-en-el-repositorio-antes-de-preguntar.md) | Se preguntó un orden de trabajo que ya estaba escrito en la sección de dependencias de la historia. La HU ya está redactada dentro del pendiente, y es conducta que rinde en cada sesión. |
| ~~25~~ | — | [Las reglas de cómo se escribe llegan en el índice, no puestas](25-las-reglas-de-como-se-escribe-van-en-el-indice.md) | **Cerrado por falso el 2026-08-15:** `ID8` sí llegaba completa y se incumplió igual. Lo que falta quedó en EP-005 · HU-010 y EP-004 · HU-013. |
| 26 | **P4** | [«Corrida» es jerga y no está definida](26-corrida-y-ejecucion-en-el-estandar.md) | El estándar llama «corrida» a ejecutar las pruebas y no dice qué es; en el glosario no existe como término propio. **Conviene hacerlo con el 21:** es el mismo cambio de vocabulario en los mismos archivos. |
| 27 | **P1** | [La fase A de EP-003 · HU-010 cerró sin cumplir](27-la-fase-a-de-hu-010-cerro-sin-cumplir.md) | `RNF-01` sin caso ejecutado y 16 de 35 pasos sin registro de qué salió. El veredicto real es «No cumple». **Ojo:** CP-006 necesita a alguien que no escribió el glosario, y eso no lo agenda el agente. |
| 28 | **P1** | [El veredicto de la fase vive en dos sitios](28-el-veredicto-de-la-fase-vive-en-dos-sitios.md) | El `resultado_pruebas` y el `estado-fase` lo escriben a mano cada uno, y ya dicen cosas distintas. Va justo después del 27, que es el caso que lo destapó. |
| 29 | **P0** | [La transcripción se escribió dos veces, y con horas inventadas](29-la-transcripcion-se-escribio-dos-veces.md) | El enganche ya escribe el histórico y el agente lo escribió otra vez a mano: 61 encabezados de usuario para 30 mensajes, y horas estimadas en vez de leídas del reloj. **El P0 es su punto 2:** mientras el `CLAUDE.md` mande escribir la transcripción a mano, vuelve a pasar, y ya pasó seis veces. Son dos párrafos. Limpiar el archivo (punto 1) es P2. |

**El 21 conviene primero:** con el glosario escrito se ve qué más está en inglés sin necesidad y se cambia todo de una vez.

### Lo que dejó un proyecto real (30, 34–36)

Salieron de instalar el estándar en `shopnest-mesa` y llevarlo hasta el código. Es la primera vez que un pendiente nace de un proyecto ajeno al estándar y no de trabajar el estándar mismo — que es justamente lo que el [pendiente 01](01-validadores-de-codigo-de-proyecto.md) decía que hacía falta.

**Los reporta el proyecto y los corrige el estándar.** Cada uno nombra su proyecto de origen y tiene allá un pendiente de seguimiento que sigue abierto: **al cerrar uno de estos hay que avisarle al proyecto**, o se queda esperando para siempre.

| # | P | Pendiente | Origen | Qué resuelve |
|---|---|---|---|---|
| 30 | **P1** | [El checklist no ve la cadena](30-el-checklist-no-ve-la-cadena.md) | shopnest-mesa | Un proyecto llegó a código commiteado con `prompts/` vacía, sin épica y sin HU, y el arranque decía «13 de 13». `F0` exige la cadena y ningún componente la mira. Es lo que el agente lee en **cada** mensaje para saber si el entorno está completo. |
| 34 | **P0** | [Las plantillas enlazan una carpeta `base/` que el proyecto no tiene](34-las-plantillas-enlazan-una-carpeta-base-que-el-proyecto-no-tiene.md) | shopnest-mesa | Los 77 enlaces `../base/…` de las plantillas nacen rotos al copiarse dentro de un proyecto. **Cada proyecto nuevo nace roto**, y el daño real no son los enlaces: es que `hook_md.py` queda siempre en rojo y se deja de leer. El marcador `«RUTA-ESTANDAR»` ya existe y los arregla. |
| 35 | **P1** | [Renombrar una sesión deja roto el enlace de su resumen](35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) | shopnest-mesa | `historico.py --renombrar` arrastra el resumen pero no corrige el enlace de adentro. **Se reprodujo acá el 2026-08-16**, al nombrar la sesión de esta priorización: deja de ser defecto de un proyecto ajeno y le pasa al estándar cada vez que nombra una sesión, que es lo que el propio enganche pide. Es de los más baratos. |
| 36 | **P0** | [Falta la regla que obliga a reportar lo que es del estándar](36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md) | shopnest-mesa | **Este es el de fondo:** los tres de arriba llegaron acá por criterio de una sesión, no por norma. Falta la regla que fija el procedimiento —los dos pendientes, el proyecto de origen y el aviso de vuelta— y la pieza que manda ese aviso. Sin el aviso, cada reporte deja un pendiente abierto para siempre en el proyecto. |

### Lo que dejó revisar el histórico (31–33)

Salieron de contar qué sesiones tienen resumen y cuáles no, y quedaron en el [resumen de esa sesión](../historico-chat/resumenes/2026-08-15/los-resumenes-que-faltan.md).

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| ~~31~~ | — | **hecho** → [33 de las 39 sesiones no tienen resumen](31-los-resumenes-de-las-sesiones-viejas.md) | Se escribieron los 33 y se renombraron 23 sesiones. Cerrado 2026-08-16; lo que esas sesiones dejaron abierto quedó en el 33. |
| 32 | **P2** | [La carpeta del día nace sin su línea en el índice](32-la-carpeta-del-dia-nace-sin-su-linea-en-el-indice.md) | El enganche crea la carpeta y el archivo, pero no los anota. El 2026-08-15 ya tiene dos resúmenes que el índice no nombra. |
| 33 | **P1** | [Lo que quedó abierto en las sesiones viejas](33-defectos-que-destaparon-los-resumenes-viejos.md) | Siete puntos que las sesiones viejas dejaron preguntados y nadie volvió a mirar. El octavo —la memoria borrada a los proyectos— **salió de acá el 2026-08-16** y es ahora el [39](39-a-que-proyectos-les-borro-la-memoria-el-enganche.md). |

**El 32 sigue abierto:** los 33 resúmenes se anotaron a mano en su índice, uno por uno. Mientras el enganche no escriba esa línea, el próximo vuelve a nacer fuera.

**El 33 no es un pendiente, son siete**, y su `P` es la de su punto más urgente. Por dentro se reparten así:

| Punto | P | Qué es |
|---|---|---|
| ~~6~~ · a qué proyectos les borró la memoria el enganche | — | **Promovido** al [39](39-a-que-proyectos-les-borro-la-memoria-el-enganche.md) el 2026-08-16 |
| 7 · un checklist anulado que nadie volvió a aplicar | **P1** | El sello caduca con el texto y nada lo comprueba. Se cruza con el [19](19-el-capitulo-20-no-se-cumple-a-si-mismo.md) |
| 5 · falta la prueba que protege el `GATE` del arranque | **P2** | Una prueba. Esa puerta ya desapareció en silencio una vez |
| 1 · el validador da por rotos los enlaces con espacios | **P2** | Un `unquote`. Falsos positivos en el validador que más se corre |
| 4 · renombrar deja rotos los enlaces de fuera | **P2** | Ya costó 41 enlaces arreglados a mano. `citas.py` ya tiene el modo que repara. Hermano del [35](35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) |
| 2 · el barrido de candidatas a regla no tiene disparador | **P3** | Falta la plantilla y la regla que obliga al barrido |
| 3 · una sesión que cruza la medianoche queda con el nombre de otro día | **P3** | Decidir si se parte o se queda entera |
| 8 · doce huecos chicos | **P6** | Casi todos son «decidir algo». **Excepción:** si las fases de EP-001 son plan o retrodocumentación **bloquea 24 documentos**, y ese sube a P3 |

**Conviene seguir promoviéndolos a pendientes numerados propios**, como ya se dice del 09 y del 10. El punto 6 fue el primero, el 2026-08-16: mientras vivió dentro de este archivo heredó la prioridad del promedio de los otros siete, y era lo más urgente del backlog.

### Lo más urgente, promovido desde el 33 (39)

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 39 | **P0** | [A qué proyectos les borró la memoria el enganche](39-a-que-proyectos-les-borro-la-memoria-el-enganche.md) | El 2026-08-07 `recuerdos.py` borró memoria de proyectos. El código está corregido desde la 3.1.1, pero **el arreglo no deshace el borrado**, y nadie revisó proyecto por proyecto qué quedó. Es el único pendiente donde se pierde información que no está en ninguna otra parte: lo que no se saque del commit no está en ningún lado, y cada commit nuevo lo entierra más. |

### Lo que dejó la sesión de la derogación (37–38)

Salieron de escribir [`02·F22`](../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md), y quedaron en el [resumen de esa sesión](../historico-chat/resumenes/2026-08-16/sesion.md).

| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 37 | **P3** | [Dónde vive la fuente de las reglas](37-donde-vive-la-fuente-de-las-reglas.md) | Si las reglas pueden guardarse en una base de datos, o el texto sigue mandando y la base se genera de él. Falta la decisión del usuario, y sin ella la discusión vuelve a empezar de cero. |
| 38 | **P1** | [El validador de la F22 se escribió sin su fase](38-el-validador-de-la-f22-se-escribio-sin-su-fase.md) | El programa que comprueba la regla se hizo sin épica, HU ni fase. Hay que retrodocumentarlo como fase de [EP-004 · HU-015](../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md). **Es el mismo hueco del [30](30-el-checklist-no-ve-la-cadena.md), visto desde adentro:** allá un proyecto llegó a código sin cadena, acá el propio estándar. Conviene mirarlos juntos. |

## Dependencias duras

Todo lo demás es preferencia y se puede reordenar:

- **02 → 05.** ✅ resuelta: el 02 (vigencia) ya está, así que la memoria semántica arranca sin recuperar más ruido del necesario.
- **02 → 03.** El 02 dejó el gancho de migración (`memoria.py · migrar()`) y `estado` abierto; el 03 suma `'cerrada'` sin migrar de nuevo.
- **09 · ítem 04 → 01.** Cinco de los nueve validadores que faltan necesitan que el proyecto declare su convención en `.agente/`, y eso es el manifiesto del 09.
- **16 → 09.** Ningún ítem del 09 se promueve sin pasar antes por el criterio de *si conviene* automatizarlo.
- **27 → 28.** Primero hay que saber cuál es el veredicto bueno de esa fase.
- **29 · punto 2 → 29 · punto 1.** Limpiar el archivo antes de quitarle al `CLAUDE.md` la instrucción que lo ensucia es limpiar para volver a ensuciar.
