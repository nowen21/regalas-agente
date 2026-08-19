# Pendiente · Autonomía sin IA — backlog de automatizaciones

**Estado:** cerrado 2026-08-18 · anotado 2026-08-07.

| | |
|---|---|
| **Historia de usuario** | No es un ítem, es un tema. Cada una de sus 16 automatizaciones nombra su historia en su fila; se promueve a pendiente propio al construirse. |

Inventario de todo lo que hoy **depende de que el agente se acuerde** y podría resolverse con un programa. Cada ítem se puede ejecutar sin ninguna IA en el momento de correr: reglas, comparaciones, generadores y enganches.

> **Este archivo es un backlog temático, no un ítem.** Cuando uno de estos se vaya a construir, se promueve a su propio pendiente numerado y aquí se marca como promovido. El número `09` reserva el lugar del tema en la fila, no de las 16 tareas.

## El criterio que ordena todo

Es el mismo del repositorio, aplicado ahora a la ejecución y no solo a la verificación:

> Si el resultado depende de leer, entender o decidir → lo hace la IA.
> Si se puede escribir como una comparación, una plantilla o un disparo → lo hace un programa.

Y el corolario que justifica el backlog completo:

> **Una regla que se cumple cuando alguien se acuerda, no se cumple.** Un `CLAUDE.md` informa; un enganche ejecuta.

---

## Resumen

**Cada uno nombra su historia.** Ninguno se construye desde este archivo: al promoverse a pendiente propio se baja a la historia de su fila y se construye como fase suya ([`02·F23`](../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)). Ninguna de las 16 estrena historia: las 16 caben en las que ya existen, que es la señal de que el tema estaba bien repartido desde el principio.

| # | Funcionalidad | Prioridad | Complejidad | Grupo | Historia donde vive |
|---|---|---|---|---|---|
| 01 | Guardián de versión y CHANGELOG | **Alta** | Baja | Blindaje | [EP-005 · HU-005](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md) |
| 02 | Barrido de secretos en el histórico | **Alta** | Baja | Seguridad | [EP-005 · HU-002](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) |
| 03 | Sello de puerta por CLI (`estado.py`) | **Alta** | Baja | Estado | [EP-004 · HU-014](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md) |
| 04 | Manifiesto de convenciones del proyecto | **Alta** | Media | Puertas | [EP-004 · HU-010](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/HU-010-convencion-declarada-por-el-proyecto.md) |
| 05 | Validador de forma de regla (`M4`/`M5`/`M11`) | **Alta** | Media | Blindaje | [EP-004 · HU-011](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/HU-011-molde-de-las-reglas.md) |
| 06 | Gate `F2` mecánico: código sin spec | **Alta** | Alta | Puertas | [EP-004 · HU-013](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md) |
| 07 | Validador del mapa del sitio | Media | Baja | Blindaje | [EP-005 · HU-011](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md), su `CA-03` |
| 08 | Enganche `pre-push` con la batería completa | Media | Baja | Seguridad | [EP-005 · HU-006](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-006-bateria-antes-de-publicar/HU-006-bateria-antes-de-publicar.md) |
| 09 | Registro de búsquedas de memoria | Media | Baja | Métricas | [EP-006 · HU-003](../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-003-busqueda-por-palabra/HU-003-busqueda-por-palabra.md) |
| 10 | Marca de fase reabierta | Media | Baja | Métricas | [EP-004 · HU-014](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md) |
| 11 | Hallazgos por regla → «puertas que fallan» | Media | Baja | Métricas | [EP-004 · HU-009](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-009-conteo-por-regla/HU-009-conteo-por-regla.md) |
| 12 | Andamiaje de fase y HU (`nueva-fase.py`) | Media | Media | Ciclo de vida | [EP-003 · HU-003](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-003-modelos-de-la-fase/HU-003-modelos-de-la-fase.md) |
| 13 | Actualizador de componentes en proyectos | Media | Media | Ciclo de vida | [EP-007 · HU-006](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/HU-006-poner-al-dia.md) |
| 14 | Generador de índices (modo aparte) | Media | Media | Blindaje | [EP-004 · HU-005](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md), su `RN-02` |
| 15 | Respaldo antes de operación irreversible | Media | Media | Seguridad | [EP-001 · HU-012](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md) |
| 16 | Detección de contradicciones en la memoria | Baja | Alta | Métricas | [EP-006 · HU-007](../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-007-marcar-lo-que-dejo-de-aplicar/HU-007-marcar-lo-que-dejo-de-aplicar.md) |

**Orden sugerido:** 01 → 02 → 03 → 07 → 08 (todo Baja complejidad y alto retorno) → 04 → 05 → 12 → 09/10/11 → 13 → 14 → 15 → 06 → 16.

El 06 va casi al final a pesar de ser prioridad Alta: se apoya en el 04 y en el 12, y sin ellos su tasa de falsos positivos lo vuelve inservible.

---

## Grupo A · Blindaje del propio estándar

### 01 · Guardián de versión y CHANGELOG

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Baja | Ninguna |

**Descripción.** Enganche `pre-commit` que mira el diff: si toca [`base/`](../../base) o [`plantillas/`](../../plantillas) y el mismo commit no sube [`VERSION`](../../VERSION) ni agrega una entrada en [`CHANGELOG.md`](../../CHANGELOG.md), el commit no se crea.

**Problema que resuelve.** `CLAUDE.md §2` y la meta-regla `M10` dicen que versionar no es opcional, pero hoy nada lo impide. Basta un despiste para que un proyecto herede una regla nueva sin que su número de versión cambie — y entonces `version.py`, que compara versiones, deja de detectar el desfase. Es una falla silenciosa que rompe la única garantía de «este proyecto cumple el estándar **de tal fecha**».

**Beneficio esperado.** El versionado deja de ser una promesa. Cualquier proyecto puede confiar en que un `VERSION` distinto significa reglas distintas.

**Cómo se automatiza sin IA.** `git diff --cached --name-only` da los archivos del commit. Si alguno empieza por `base/` o `plantillas/`, se exige que la lista también incluya `VERSION` y `CHANGELOG.md`, y que la primera línea de versión del CHANGELOG coincida con el contenido de `VERSION`. Todo es comparación de cadenas.

**Recomendaciones.** No intentar decidir si el cambio es MAYOR, MENOR o PARCHE — eso sí es criterio, y forzarlo produciría falsos positivos. El guardián exige que **haya** entrada; cuál corresponde lo decide quien escribe. Dejar una salida explícita (`ESTANDAR_SIN_VERSION=1`) para los commits de solo formato, y que la salida diga cuál es.

---

### 05 · Validador de forma de regla (`M4` / `M5` / `M11`)

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Media | [`base/20-meta-reglas/estructura-regla.md`](../../base/20-meta-reglas/estructura-regla.md) |

**Descripción.** Comprobar que cada regla de `base/` respete su propio molde: ID libre del prefijo del capítulo (`M4`), **una sola exigencia** por regla, ejemplo INCORRECTO/CORRECTO presente (`M5`), y ninguna regla borrada o renumerada entre versiones (`M11`).

**Problema que resuelve.** Las meta-reglas del capítulo 20 son las únicas del estándar que nadie comprueba. Se aplican por lectura, y una regla mal formada no se nota hasta que alguien la cita y descubre que exige dos cosas a la vez o que su ID chocó con otro.

**Beneficio esperado.** El estándar deja de poder contradecirse a sí mismo por descuido de forma. Y con `M11` cubierto, ninguna spec o commit histórico queda huérfano por una regla que desapareció.

**Cómo se automatiza sin IA.** El molde de `M5` es un patrón fijo de encabezados y bloques: se comprueba con expresiones regulares sobre cada archivo de `base/`. Los IDs se extraen y se verifica unicidad y prefijo. Para `M11`, se compara el conjunto de IDs contra el del último tag de git: un ID que estaba y ya no está es FALLA salvo que aparezca marcado como derogado.

**Recomendaciones.** Empezar solo por `M4` y `M11` — son binarios y de cero ambigüedad. La «una sola exigencia» de `M5` es la parte fuzzy: aproximarla contando verbos imperativos o conjunciones y reportarla como **AVISO**, nunca FALLA.

---

### 07 · Validador del mapa del sitio

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Baja | [`anatomia/mapa-del-sitio.md`](../../anatomia/mapa-del-sitio.md) |

**Descripción.** Comparar el árbol declarado en el mapa del sitio contra lo que hay en disco y reportar lo que sobra y lo que falta.

**Problema que resuelve.** El mapa dice que se mantiene al día «en el mismo cambio», pero esa regla vive solo en el texto del propio mapa. Un mapa desactualizado es peor que no tener mapa: manda a buscar donde ya no hay nada.

**Beneficio esperado.** La sección más útil para alguien que llega nuevo deja de degradarse sola.

**Cómo se automatiza sin IA.** Extraer del bloque de árbol los nombres de archivo y carpeta con una expresión regular, recorrer el disco con el mismo filtro de exclusiones que ya usa el mapa, y hacer diferencia de conjuntos. Colgarlo del enganche `PostToolUse` que ya existe para `.md`.

**Recomendaciones.** Severidad **AVISO**, no FALLA: el mapa lista archivos representativos, no exhaustivos (`notas/`, `historico-chat/`), y exigir uno a uno lo volvería inmantenible. Marcar las carpetas cuyo contenido sí debe listarse completo (`base/`, `validadores/`, `skills/`) y aplicar la exigencia solo ahí.

---

### 14 · Generador de índices

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Media | `enlaces.py` |

**Descripción.** Programa que **escribe** los índices que hoy `enlaces.py` solo comprueba: el índice de [`historico-chat/README.md`](../../historico-chat/README.md), el de [`notas/`](../../notas), el de [`pendientes/`](..).

**Problema que resuelve.** Cada archivo nuevo obliga a agregar su línea al índice a mano. Es trabajo mecánico que la IA hace con el mismo esfuerzo que cualquier otra edición, y que olvida con la misma facilidad. El validador lo detecta después; nadie lo evita antes.

**Beneficio esperado.** Menos trabajo repetitivo y un tipo de hallazgo que desaparece del todo.

**Cómo se automatiza sin IA.** Listar los archivos de la carpeta, leer el primer encabezado `#` de cada uno como título, y reescribir el bloque entre dos marcas (`<!-- indice:inicio -->` / `<!-- indice:fin -->`). Determinista y reversible.

**Recomendaciones.** **No meterlo en `validadores/`.** El README de esa carpeta establece que los validadores reportan y no arreglan, y romper ese principio haría impredecible el resto. Va en un programa aparte (`herramientas/indices.py`) que se corre a propósito. La descripción de cada entrada sí la escribe quien crea el archivo: eso es criterio.

---

## Grupo B · Seguridad e higiene

### 02 · Barrido de secretos en el histórico

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Baja | `hook_historico.py` · `secretos.py` |

**Descripción.** Antes de escribir un mensaje en `historico-chat/`, revisar que no traiga un secreto con forma real y, si lo trae, guardarlo enmascarado dejando la marca de que se enmascaró.

**Problema que resuelve.** Es un hueco real, no hipotético. El enganche copia el chat **literal** y lo deja en un archivo versionado. Si alguien pega un token, una cadena de conexión o una clave en el chat, queda en el repositorio y en el historial de git para siempre. Y ningún validador actual lo ve: `secretos.py` excluye los `.md` a propósito —la documentación muestra secretos de ejemplo y marcarlos sería ruido— y `versionado.py` mira nombres de archivo, no contenido.

**Beneficio esperado.** Cierra la única vía por la que un secreto real entra al repositorio sin que nada se queje.

**Cómo se automatiza sin IA.** Reutilizar los patrones de severidad FALLA que `secretos.py` ya tiene (los que delatan un proveedor concreto: `sk-`, `AKIA`, tokens con forma fija) y aplicarlos **solo** al texto que va a escribir el enganche. Al detectar uno, sustituirlo por `«secreto enmascarado»` y anotar la línea.

**Recomendaciones.** Usar **solo** los patrones de forma inequívoca, nunca los de AVISO: enmascarar de más corrompe una transcripción que vale precisamente por ser literal. Escribir la marca de enmascaramiento en el archivo para que se note que hubo sustitución. Y avisar al usuario en el momento, porque un secreto pegado en un chat probablemente también haya que rotarlo.

---

### 08 · Enganche `pre-push` con la batería completa

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Baja | `instalar.py` |

**Descripción.** Un tercer enganche de git, hermano de `commit-msg` y `pre-commit`, que corre la batería de validadores que hoy solo se disparan a mano.

**Problema que resuelve.** `pre-commit` revisa secretos y artefactos; `commit-msg` revisa el mensaje. Todo lo demás —fases, trazabilidad, esquema, rendimiento, aislamiento— se corre si alguien lo pide. Publicar es la última puerta antes de que el error salga de la máquina, y hoy está abierta.

**Beneficio esperado.** Lo que no se detectó al escribir se detiene antes de salir, sin costo en cada commit.

**Cómo se automatiza sin IA.** `instalar.py` ya sabe escribir enganches: se agrega la entrada a su lista y llega solo a todos los proyectos. El enganche llama a `validar.py` con el conjunto de comprobaciones rápidas y corta con código 1 si hay FALLA.

**Recomendaciones.** Dejar fuera `linter`, `suite` y `audit` — dependen del toolchain, tardan y `audit` sale a la red; un `pre-push` lento se termina saltando con `--no-verify`, que es peor que no tenerlo. Que el mensaje de error diga siempre cómo saltarlo, porque a veces hay que hacerlo.

---

### 15 · Respaldo antes de operación irreversible

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Media | `.agente/stack.md` · manifiesto (04) |

**Descripción.** Envoltorio que hace el respaldo antes de correr una operación destructiva conocida (migración, `seed`, borrado masivo) y deja el archivo con fecha.

**Problema que resuelve.** `00·N4` exige respaldo antes de una operación irreversible. Hoy lo cumple el agente decidiendo hacerlo, y una regla del núcleo blindado no debería depender de una decisión.

**Beneficio esperado.** La regla más costosa de incumplir del estándar deja de depender del criterio.

**Cómo se automatiza sin IA.** Para el subconjunto de operaciones **nombradas** —`migrate`, `migrate:fresh`, `db:seed`— el comando es reconocible por su texto, y el volcado se hace con la herramienta del stack declarado. Es un envoltorio, no un detector.

**Recomendaciones.** Ser explícito sobre el límite: **«operación irreversible» en general no es detectable sin criterio**. Un `DELETE` sin `WHERE` escrito a mano, un script de limpieza propio o un borrado por API no los va a ver nadie. Automatizar el subconjunto nombrado y dejar escrito en la regla que el resto sigue siendo del agente — un respaldo automático parcial que se anuncia como total es peor que no tenerlo, porque genera confianza donde no la hay.

---

## Grupo C · Cerrar las puertas del flujo

### 04 · Manifiesto de convenciones del proyecto

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Media | Ninguna · es precondición de otros |

**Descripción.** Un archivo declarativo en `.agente/` donde el proyecto dice, en formato legible por máquina, dónde viven sus módulos, qué convención de nombres usa, qué tablas son de dominio y qué entidades son inmutables.

**Problema que resuelve.** Cinco reglas están clasificadas como validables pero bloqueadas por la misma razón: no hay contra qué comparar (`14·EST1`, resto de `14·EST2`, resto de `03·D1`, `15·IM2`, `15·IM5`). Hoy las interpreta el agente en cada sesión, y dos sesiones pueden interpretarlas distinto.

**Beneficio esperado.** Desbloquea cinco validadores de una sola vez. Es el ítem con mejor relación entre esfuerzo y reglas ganadas.

**Cómo se automatiza sin IA.** El manifiesto lo llena una persona una vez (o el agente al analizar el proyecto, que es trabajo de criterio y está bien que lo sea). A partir de ahí, cada validador es una comparación mecánica: la ruta declarada contra la ruta real, el patrón de nombres contra el nombre, la lista de entidades inmutables contra el esquema.

**Recomendaciones.** Formato mínimo y plano; nada de un esquema que haya que aprender. Que `checklist.py` lo incluya como componente del stack de instalación, para que su ausencia se note sola. Y que **la ausencia del manifiesto desactive los validadores que dependen de él en silencio** — no que los haga fallar: un proyecto que no lo declaró no está incumpliendo nada.

---

### 06 · Gate `F2` mecánico — código sin spec

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Alta | 04 · 12 · [pendiente 01](validadores-de-codigo-de-proyecto.md) |

**Descripción.** Detectar que se escribió código de una fase sin que existan su spec y su plan aprobados.

**Problema que resuelve.** Es **la** puerta del estándar: «sin spec acordada no hay código». Es la única de las 13 estaciones del orquestador que nada comprueba mecánicamente. Si el agente se la salta, no queda señal.

**Beneficio esperado.** La regla que define al estándar deja de depender de que se respete voluntariamente.

**Cómo se automatiza sin IA.** Cruzar tres fuentes que ya existen: los archivos tocados en la rama (`git diff` contra la rama base), la fase activa (del `estado-fase.md` del ítem 03) y los archivos que el plan declara intervenir. Código tocado que no aparece en ningún plan aprobado → hallazgo. Sin IA: son tres listas y una diferencia.

**Recomendaciones.** Es el más pesado y el de mayor riesgo de falsos positivos — un refactor legítimo toca archivos que ningún plan nombró. **No construirlo antes que el 03 y el 12**, que son los que hacen fiables las otras dos listas. Empezar en modo AVISO y solo por archivos **nuevos** (los creados en la rama), que es donde el falso positivo es raro. Prever una exención declarada en el plan (`§Fuera-de-plan`) con su justificación.

---

### 03 · Sello de puerta por CLI (`estado.py`)

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Baja | `plantillas/estado-fase.md` |

**Descripción.** Un comando que estampa el paso de cada puerta en `estado-fase.md`: qué estación, qué puertas pasaron, con fecha y hora del reloj de la máquina.

**Problema que resuelve.** El orquestador manda escribir el estado en cada puerta, y hoy lo escribe el agente redactando. Eso tiene tres consecuencias: el formato varía entre sesiones, las horas se estiman en vez de leerse, y si la sesión se corta antes de escribir, el estado se pierde — que es justo lo que el checkpoint venía a evitar.

**Beneficio esperado.** El estado pasa a ser un dato estructurado y no una redacción. Y, sobre todo, se vuelve **legible por otros programas**: los ítems 06, 10 y 11 de este backlog necesitan leerlo.

**Cómo se automatiza sin IA.** `python estado.py sellar --fase F3 --estacion 7 --puerta ok`. Escribe una línea de tabla con la hora del sistema. La parte narrativa (decisiones, preguntas abiertas) la sigue redactando el agente, que para eso sí hace falta.

**Recomendaciones.** Es la pieza más barata con más efecto de arrastre: constrúyalo primero de este grupo. Formato de tabla estable y documentado, porque tres automatizaciones más lo van a leer. Que sea idempotente: sellar dos veces la misma puerta no debe duplicar la fila.

---

## Grupo D · Instrumentar lo que hoy no se puede medir

El [README de métricas](../../metricas/README.md) ya identifica cuatro números que no se pueden derivar porque falta un marcador. Los tres primeros son ese marcador.

### 09 · Registro de búsquedas de memoria

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Baja | `memoria/memoria.py` |

**Descripción.** Que `memoria.py search` deje registro de qué se buscó, cuántos resultados hubo y si alguno se usó.

**Problema que resuelve.** No se sabe si la memoria sirve. Puede tener cientos de señales y no encontrar nunca lo que hace falta, y no habría forma de notarlo.

**Beneficio esperado.** Habilita la métrica «uso real de la memoria» y, con ella, la decisión de si conviene ajustar el índice, los tipos de señal o la búsqueda híbrida.

**Cómo se automatiza sin IA.** Una tabla más en `senales.db`: consulta, filtros, cantidad de resultados, fecha. Una inserción por búsqueda.

**Recomendaciones.** Guardar solo la consulta y el conteo, nunca el resultado completo — la base ya tiene el contenido y duplicarlo la infla sin ganancia. «Si alguno se usó» no es observable desde el CLI: aproximarlo con «hubo cero resultados», que ya dice bastante.

---

### 10 · Marca de fase reabierta

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Baja | 03 |

**Descripción.** Distinguir una fase que se reabre de una fase nueva.

**Problema que resuelve.** Hoy no se diferencian, así que la métrica de retrabajo no existe. Y el retrabajo es la señal más directa de que una spec salió incompleta.

**Beneficio esperado.** Permite ver qué parte del flujo produce retrabajo — que es información para cambiar reglas, no para calificar a nadie.

**Cómo se automatiza sin IA.** Si la fase ya tiene una puerta de cierre sellada y se vuelve a sellar una estación anterior, es una reapertura. Se deriva del propio `estado-fase.md`.

**Recomendaciones.** Que la reapertura pida un motivo de una línea y lo guarde como señal en la memoria. El número solo dice cuántas; el motivo dice qué arreglar.

---

### 11 · Hallazgos por regla — «puertas que fallan»

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Baja | `validar.py` · `metricas.py` |

**Descripción.** Que cada corrida de validadores registre cuántos hallazgos hubo por regla, y que las métricas lo agreguen.

**Problema que resuelve.** No se sabe qué regla se incumple todo el tiempo. Una regla que falla siempre está mal escrita, mal ubicada o de más — y hoy no hay cómo distinguirla de una que nunca falla.

**Beneficio esperado.** Convierte los validadores en fuente de datos sobre el estándar mismo. Es la extensión que el README de métricas ya deja anotada.

**Cómo se automatiza sin IA.** Los hallazgos ya salen etiquetados con su regla. Se agrega una salida `--json` a `validar.py` y una tabla de corridas en `senales.db`.

**Recomendaciones.** Registrar solo cuando se corre la batería completa; las corridas parciales sesgan el conteo hacia lo que se revisa más. Y mantener la advertencia del README de métricas al pie del reporte: sirve para decidir qué reglas cambiar, no para calificar el trabajo.

---

### 16 · Detección de contradicciones en la memoria

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Baja | Alta | [`hecho/memoria-semantica.md`](memoria-semantica.md) |

**Descripción.** Avisar cuando una señal nueva contradice una activa — la decisión contraria a la que ya se tomó, el patrón que niega al anterior.

**Problema que resuelve.** Es lo único que quedó abierto del pendiente 05. Una memoria con dos señales opuestas activas es peor que una memoria vacía: da respuestas seguras y contradictorias según cuál se encuentre primero.

**Beneficio esperado.** La memoria se corrige sola en vez de acumular ruido con apariencia de certeza.

**Cómo se automatiza sin IA.** Parcialmente. Los vectores del módulo semántico ya permiten encontrar señales **muy parecidas** en el mismo scope y tipo, que es donde viven casi todas las contradicciones. Detectar el par candidato es mecánico.

**Recomendaciones.** Prioridad Baja precisamente porque **decidir si dos señales se contradicen o se complementan es criterio, no cálculo**. Lo honesto es que el programa detecte el par sospechoso y lo marque para revisión humana; llamarlo «detección de contradicciones» a secas prometería más de lo que puede dar. Umbral alto y salida en AVISO.

---

## Grupo E · Ciclo de vida

### 12 · Andamiaje de fase y HU (`nueva-fase.py`)

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Media | `plantillas/` · `fases.py` |

**Descripción.** Comando que crea la carpeta de una fase o HU con sus cuatro documentos desde la plantilla, el consecutivo correcto y los enlaces a su épica y su HU ya puestos.

**Problema que resuelve.** Hoy la IA copia plantillas, calcula el siguiente número sin huecos y escribe los enlaces bidireccionales a mano. Es trabajo mecánico, es donde se cometen los errores que `fases.py` y `trazabilidad.py` detectan después, y consume contexto que debería ir al problema real.

**Beneficio esperado.** Desaparece una clase entera de hallazgos —numeración, nomenclatura, enlaces faltantes— porque la estructura nace bien en vez de corregirse. Y el 06 se vuelve viable: si la estructura la genera un programa, cruzarla con el código deja de ser adivinanza.

**Cómo se automatiza sin IA.** `fases.py` ya sabe leer la jerarquía y detectar el consecutivo: se invierte esa lógica para **escribir**. Las plantillas ya existen; solo hay que sustituir los marcadores estructurales (identificadores, rutas, enlaces), no los de contenido.

**Recomendaciones.** Que genere el esqueleto y **nada de contenido**: dejar los marcadores `«…»` intactos para que `plantillas.py` siga exigiendo que se llenen. Un generador que además rellena texto produce documentos que pasan el validador sin decir nada, que es la peor combinación posible.

---

### 13 · Actualizador de componentes en proyectos

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Media | `instalar.py` · `checklist.py` |

**Descripción.** Modo `--actualizar` que lleve al día los componentes ya instalados en un proyecto, no solo los que faltan.

**Problema que resuelve.** `checklist.py` avisa cuando un componente copiado quedó viejo —compara la huella con el original— pero actualizarlo lo tiene que hacer alguien. Mientras tanto el proyecto corre con una copia desactualizada y con un aviso permanente, que es exactamente lo que el README de validadores advierte que se deja de leer.

**Beneficio esperado.** El principio del repositorio —«si exige configurarla a mano, está mal hecha»— pasa a valer también para las actualizaciones, no solo para la primera instalación.

**Cómo se automatiza sin IA.** Comparar huellas y reemplazar el archivo. Los enganches son generados, así que se regeneran sin pérdida.

**Recomendaciones.** Distinguir lo generado de lo editable. Un enganche se pisa sin preguntar; el `CLAUDE.md` del proyecto y las reglas propias **nunca** — ahí hay trabajo del usuario. Para esos, avisar y mostrar el diff. Correr siempre en modo previsualización primero, como ya hace `instalar.py`.

---

## Lo que este backlog deliberadamente no propone

Tres cosas que parecen automatizables y no lo son. Vale dejarlas escritas para no volver a proponerlas:

- **Decidir la severidad de un cambio de versión** (MAYOR/MENOR/PARCHE). Depende de si un proyecto al día queda obligado a algo nuevo — eso es leer la regla y entenderla.
- **Aprobar una puerta de usuario.** Las siete puertas de usuario del orquestador (alcance, épica, HUs, spec, plan, commit, despliegue) existen porque alguien tiene que decir que sí. Automatizarlas sería quitarlas.
- **Evaluar si una spec está bien escrita.** Se puede comprobar que esté **completa** contra su plantilla; que esté **bien** es criterio, y ninguna cantidad de reglas lo reemplaza.

La frontera es la de siempre: **completitud se comprueba, calidad se juzga.**


---

# Medido el 2026-08-18: diez de las dieciséis ya estaban

**Se buscó cada una en el repositorio antes de construir nada**, como con el [01](validadores-de-codigo-de-proyecto.md). El resultado es el mismo: el backlog contaba como trabajo por hacer lo que ya estaba hecho.

| # | Qué es | Qué hay |
|---|---|---|
| 01 | Guardián de versión y CHANGELOG | ✅ `versionado.py` · `numeracion.py` · el enganche de `pre-commit` |
| 02 | Barrido de secretos en el histórico | ✅ [`enmascarar.py`](../../validadores/enmascarar.py) |
| 03 | Sello de puerta por CLI | ✅ `validar.py fases` |
| 04 | Manifiesto de convenciones | ✅ [`declaracion.py`](../../validadores/declaracion.py) |
| 05 | Validador de forma de regla | ✅ [`metareglas.py`](../../validadores/metareglas.py) |
| 06 | Gate `F2` mecánico | ✅ [`flujo.py`](../../validadores/flujo.py) |
| 07 | Validador del mapa del sitio | ✅ [`amarre.py`](../../validadores/amarre.py) |
| **08** | **Enganche `pre-push` con la batería** | ✅ **construido hoy** — ver abajo |
| 09 | Registro de búsquedas de memoria | ✅ `memoria/senales.db` · `recuerdos.py` |
| 11 | Hallazgos por regla | ✅ `metricas/` |
| 13 | Actualizador de componentes | ✅ `instalar.py` · `versiones.py` |
| **10** | **Marca de fase reabierta** | ✅ **construido hoy** — `validar.py reaperturas` |
| **12** | **Andamiaje de fase y HU** | ✅ **construido hoy** — `validadores/andamio.py` |
| **14** | **Generador de índices** | ✅ **construido hoy** — `validar.py indices` |
| **15** | **Respaldo antes de lo irreversible** | ✅ **construido hoy** — `validadores/respaldo.py`, y su regla es [`00·N7`](../../base/00-nucleo-blindado.md) |
| **16** | **Contradicciones en la memoria** | ✅ **construido hoy** — `memoria/parecidas.py` |

**Ninguno. Las dieciséis están.**

## 08 · el enganche de publicar, construido

**Publicar es lo que no se deshace.** Un commit se revierte; lo publicado ya lo tiene otro ([`00·N2`](../../base/00-nucleo-blindado.md)). Por eso la batería va acá y no en cada commit: ahí sería insoportable —minutos por vez— y a la semana alguien la apaga.

**Y hoy se notó la falta:** se publicaron dieciséis commits seguidos sin que corriera nada solo. Corría porque el agente se acordaba, que es exactamente lo que este pendiente dice que no cuenta como cumplir.

### Lo que detiene y lo que no

| | |
|---|---|
| **Detiene** | `estandar` y `versionado` — enlaces rotos, índices viejos, algo sin versionar. Salen del trabajo de hoy |
| **Informa** | `metareglas` — el cuerpo de reglas contra su molde |

**Es la distinción que decide si el enganche sobrevive.** Al construirlo, la primera versión metía `metareglas` en el bucle que detiene, y **rechazó el push con cero fallas**: hay reglas publicadas que no pasan su checklist, deuda conocida del [19](../19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> **Un estándar endeudado consigo mismo no puede impedir publicar cualquier otra cosa.** Eso convierte el enganche en un obstáculo permanente, y así se termina en `--no-verify` para todo — que es apagarlo sin decirlo.

**Tampoco corre lo que necesita un proyecto real** —linter, suite, audit—: fallaría en cualquier repositorio que no los tenga instalados, y un enganche que falla siempre se salta.

**Y dice cómo saltarlo a propósito.** Un enganche sin salida se salta a escondidas; decir cómo hacerlo es lo que convierte saltarlo en una decisión.

**7 casos** en [`validadores/tests/test_el_enganche_de_publicar.py`](../../validadores/tests/test_el_enganche_de_publicar.py).


## 14 · el generador de índices, construido

**Escribe la línea que falta en vez de solo reportarla.** Es `validar.py indices`, y sin `--aplicar` solo dice qué escribiría.

**Hoy se notó la falta dos veces**, las dos en `notas/`: se creó la nota y se olvidó su línea, y las dos las cazó `validar.py estandar` **commits más tarde**, no la mano.

### No regenera el índice, y ahí está la decisión

El pendiente proponía reescribir el bloque entre dos marcas. **Al mirarlo de cerca eso destruía trabajo:** las líneas que ya están llevan una descripción escrita por alguien —*«por qué se confunde de quién es el dato con quién lo tocó»*— que el encabezado del archivo no tiene. Regenerar la cambiaría por el título.

**Lo que hace es agregar lo que falta**, con el título del archivo y la marca `— (por describir)`, y **avisar de las que quedaron sin afinar**. Sin ese aviso, la descripción provisional se queda para siempre y el índice deja de decir nada.

**Y lo que sobra lo reporta y no lo borra:** quitar una línea del índice puede ser el error, no el archivo que ya no está. Hay un caso que lo fija.

**11 casos** en [`validadores/tests/test_el_indice_se_completa_solo.py`](../../validadores/tests/test_el_indice_se_completa_solo.py), incluidos los dos que importan: que la descripción cuidada sobreviva, y que correrlo dos veces no duplique.

### Lo comprobó otro validador de hoy

Al escribir `indices.py`, **el mapa del amarre lo reportó como pieza sin clasificar** — el que se construyó esta misma tarde para el [15](../15-el-estandar-depende-de-una-sola-herramienta.md). Funcionó a la primera y contra un caso real, no contra uno inventado.


## 10 · la marca de fase reabierta, construida

**`validar.py reaperturas`.** Sobre este repositorio encuentra **dos**, y son las dos de verdad: [`A-EP-005-HU-008`](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/estado-fase.md) —el enganche del resumen que no creaba el resumen— y [`A-EP-007-HU-006`](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/estado-fase.md), reabierta hoy.

### Se deriva de la historia, no de las palabras

**Las reaperturas se escriben en prosa y cada una con las suyas** — «reabierta», «se reabrió», «vuelta a cerrar». Buscar la palabra encuentra unas, se pierde otras, y cuenta las que solo **hablan** de reabrir: **cinco archivos la mencionan y solo dos fases se reabrieron**. El texto habría dado más del doble.

**Lo que no se puede escribir de dos formas es una casilla que estaba marcada y dejó de estarlo.** Una reapertura es que una estación de cierre —7 pruebas, 8 cierre documental, 9 commit— pase de ☑ a ☐ en un guardado posterior.

**Y la distinción que evita el falso positivo:** volver atrás **antes** de haber cerrado no es reabrir, es corregir. Hay un caso que lo fija.

### Nunca es una falla, y eso importa

**Reabrir una fase es lo correcto** cuando lo que falla es ese trabajo y su documentación decía que estaba hecho — así se hizo con las dos que encuentra. Lo que se mide **no es un incumplimiento**: es de dónde sale el retrabajo, que es información para cambiar reglas, no para calificar a nadie.

**11 casos** en [`validadores/tests/test_la_fase_reabierta_se_distingue.py`](../../validadores/tests/test_la_fase_reabierta_se_distingue.py).


## 12 · el andamio de fase, construido

**`python validadores/andamio.py EP-001-… HU-003-… descripcion`**, y sin `--aplicar` solo dice qué crearía.

Calcula el consecutivo, arma el nombre según [`02·F12.6`](../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) y copia los cinco documentos desde sus plantillas.

### La advertencia del pendiente era lo más importante que traía

> *Que genere el esqueleto y **nada de contenido**. Un generador que además rellena texto produce documentos que pasan el validador sin decir nada, que es la peor combinación posible.*

**Se respetó al pie de la letra:** los marcadores `«…»` quedan intactos, y hay un caso que **falla si algún documento sale sin ninguno**. Lo único que se sustituye es lo estructural — identificadores, rutas, nombre de la fase—, que es justo lo que un programa sabe y una persona escribe mal.

**Es el patrón del día visto del otro lado.** Todo el día apareció «una comprobación que pasa sin comprobar»; esto habría sido **un documento que cumple sin decir nada**.

### El consecutivo se lee, no se cuenta

Si existen la `A` y la `C` porque la `B` se renombró, **contar cuántas hay daría `C` y pisaría una fase viva**. Se leen las letras usadas y se toma la primera libre. Hay un caso con ese hueco exacto.

### Se corre solo, no por `validar.py`

La separación de siempre: `validar.py` es la puerta de lo que **comprueba**; esto **escribe**, como `cerrar.py` o `historico.py`. **La prueba que exige que todo módulo diga por dónde se corre lo reportó** al escribirlo, y se resolvió declarándolo donde van los que tienen arranque propio.

**9 casos** en [`validadores/tests/test_el_andamio_no_escribe_contenido.py`](../../validadores/tests/test_el_andamio_no_escribe_contenido.py).


## 15 · el respaldo antes de lo irreversible, construido

**`python validadores/respaldo.py --aplicar -- <comando>`.** Respalda con lo que el proyecto declaró y **después** corre la operación. Sin `--aplicar`, dice qué haría.

### El límite es la mitad del trabajo, y va escrito en la salida

El pendiente lo pedía así, y tenía razón:

> *Un respaldo automático parcial que se anuncia como total es peor que no tenerlo, porque genera confianza donde no la hay.*

**Cada corrida empieza diciendo qué no cubre:** un borrado escrito a mano, un guion de limpieza propio o un borrado por interfaz **no los ve nadie**. Eso sigue siendo criterio del agente, y [`00·N7`](../../base/00-nucleo-blindado.md) lo sigue exigiendo.

### Dos negativas que son el programa entero

| Si... | Entonces |
|---|---|
| No hay respaldo declarado | **no se corre la operación** |
| El respaldo falla | **no se corre la operación** |

**La segunda es la que se olvida al escribir esto.** Un respaldo que falló y una operación que corre igual es la peor combinación posible: creer que hay red y no tenerla. Hay un caso para cada una.

### No adivina el comando, y es a propósito

Sin `Respaldo de datos` en el `.agente/stack.md`, no inventa nada. **Adivinar cómo se respalda una base ajena sería equivocarse justo antes de lo irreversible.** Declararlo es de quien conoce el almacén.

**La plantilla del stack ganó dos filas:** el comando de respaldo y el de **restaurar**. El segundo no lo usa ningún programa — se declara para que esté escrito **antes del susto y no durante**.

### Invocarlo es la autorización

[`00·N4`](../../base/00-nucleo-blindado.md) pide autorización para esa operación concreta, y **escribir el comando destructivo dentro del envoltorio es esa autorización**: nadie lo teclea sin querer. Lo que el envoltorio agrega no es permiso — es la red.

**13 casos** en [`validadores/tests/test_el_respaldo_antes_de_lo_irreversible.py`](../../validadores/tests/test_el_respaldo_antes_de_lo_irreversible.py).


## 16 · el detector de señales parecidas, construido

**`python memoria/parecidas.py`.** Sobre la memoria de hoy dice: *ningún par de señales activas se parece lo suficiente*.

### Se llama «parecidas» y no «contradicciones», que era la advertencia del pendiente

> *Decidir si dos señales se contradicen o se complementan es criterio, no cálculo. Llamarlo «detección de contradicciones» a secas prometería más de lo que puede dar.*

**Un aviso que promete de más se termina apagando** — el defecto más caro de este repositorio, encontrado siete veces hoy. Lo que el programa hace es **poner el par delante**; quién decide si chocan es quien lee.

### El umbral se eligió midiendo, y el resultado fue no devolver nada

Sobre **114 señales que deciden**, el corte es abrupto:

| Umbral | Pares |
|---:|---:|
| 0.86 | 6 |
| **0.90** | **0** |
| 0.93 | 0 |

Los seis de 0.86 eran señales **relacionadas** —dos módulos rotos por la misma fase anterior— y ninguna contradecía a la otra.

**Se eligió el umbral que hoy no devuelve nada.** Seis pares que hay que descartar a mano enseñan a no mirar la lista, y entonces el día que aparezca uno de verdad tampoco se mira.

### Lo que destapó medirlo: el título engaña

La primera versión comparaba **título y porqué juntos**, y daba **once** pares — todos falsos. Los títulos de esta casa siguen un molde —*«Módulo X cerrado con Fase Y»*— y **dos señales de temas distintos salen parecidísimas por la forma de la frase**, no por lo que dicen.

**Comparando solo el porqué bajaron a seis.** El porqué es donde está la sustancia.

### Dos cosas que no hace, y las dice

- **Sin el módulo semántico no compara nada** y lo anuncia. No cae en comparar por palabras sueltas: daría pares por casualidad.
- **No mira entre alcances distintos.** Que la organización y un proyecto digan cosas distintas **es como está diseñado** — el proyecto ajusta, no contradice.

**10 casos** en [`memoria/test_parecidas.py`](../../memoria/test_parecidas.py).


---

# Cómo cerró — 2026-08-18

**Las dieciséis están.** Diez ya existían y se descubrieron buscándolas en vez de creerle a la lista; seis se construyeron hoy.

| Construido hoy | Qué quedó |
|---|---|
| **08** · batería antes de publicar | el enganche de `pre-push` |
| **10** · marca de fase reabierta | `validar.py reaperturas` |
| **12** · andamiaje de fase | `validadores/andamio.py` |
| **14** · generador de índices | `validar.py indices` |
| **15** · respaldo antes de lo irreversible | `validadores/respaldo.py` |
| **16** · señales parecidas | `memoria/parecidas.py` |

## Lo que este pendiente enseñó, y vale más que las seis piezas

**Diez de las dieciséis ya estaban construidas.** Igual que en el [01](validadores-de-codigo-de-proyecto.md): el backlog contaba como trabajo por hacer lo que ya estaba hecho, y nadie lo había vuelto a mirar.

**Su propio corolario terminó aplicándose al propio archivo:**

> *Una regla que se cumple cuando alguien se acuerda, no se cumple.*

Un inventario que solo está al día cuando alguien se acuerda de revisarlo, tampoco.

## Las cuatro decisiones que se tomaron construyendo, y por qué

Las cuatro son la misma: **no prometer más de lo que se puede**.

| Pieza | Lo que se decidió |
|---|---|
| `pre-push` | **Lo que informa y lo que detiene, separados.** Meter el cuerpo de reglas en lo que detiene rechazaba el push con cero fallas: hay deuda conocida, y un estándar endeudado consigo mismo no puede impedir publicar |
| `andamio.py` | **Ni una palabra de contenido.** Los marcadores quedan intactos, y hay un caso que falla si algún documento sale sin ellos |
| `respaldo.py` | **Sin respaldo declarado no corre nada.** Y si el respaldo falla, tampoco — creer que hay red y no tenerla es peor |
| `parecidas.py` | **Se llama «parecidas», no «contradicciones».** Y el umbral se puso donde hoy no devuelve nada, porque seis pares falsos enseñan a no mirar la lista |

## El patrón del día, confirmado por octava vez

**Una comprobación que pasa sin comprobar.** Apareció ocho veces:

`avisar()` nunca llamada · `metareglas.py` sin subcomando · `estructura`, `entidades` y `cruces` sin puerta · el `CP-005` del instalador con un solo registro · `secretos` revisando el estándar · el recuento de huérfanas de `acciones.py` · `entidades` con 31 avisos falsos · y los once pares falsos de `parecidas.py`, cazados antes de publicarlo.

**Todos tenían su prueba en verde al lado.** Lo que faltaba siempre era el caso que comprueba **lo contrario**: que cuando no hay defecto, el programa se calle.

## Lo que no se hizo, y se dice

**Nada quedó a medias.** Las seis nuevas tienen sus casos y su límite escrito en la propia salida del programa. Lo que **no** cubren está dicho en cada una — sobre todo en `respaldo.py`, que solo ve lo que se le pasa por la mano.
