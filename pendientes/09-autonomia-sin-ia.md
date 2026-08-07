# Pendiente · Autonomía sin IA — backlog de automatizaciones

**Estado:** abierto · anotado 2026-08-07.

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

| # | Funcionalidad | Prioridad | Complejidad | Grupo |
|---|---|---|---|---|
| 01 | Guardián de versión y CHANGELOG | **Alta** | Baja | Blindaje |
| 02 | Barrido de secretos en el histórico | **Alta** | Baja | Seguridad |
| 03 | Sello de puerta por CLI (`estado.py`) | **Alta** | Baja | Estado |
| 04 | Manifiesto de convenciones del proyecto | **Alta** | Media | Puertas |
| 05 | Validador de forma de regla (`M4`/`M5`/`M11`) | **Alta** | Media | Blindaje |
| 06 | Gate `F2` mecánico: código sin spec | **Alta** | Alta | Puertas |
| 07 | Validador del mapa del sitio | Media | Baja | Blindaje |
| 08 | Enganche `pre-push` con la batería completa | Media | Baja | Seguridad |
| 09 | Registro de búsquedas de memoria | Media | Baja | Métricas |
| 10 | Marca de fase reabierta | Media | Baja | Métricas |
| 11 | Hallazgos por regla → «puertas que fallan» | Media | Baja | Métricas |
| 12 | Andamiaje de fase y HU (`nueva-fase.py`) | Media | Media | Ciclo de vida |
| 13 | Actualizador de componentes en proyectos | Media | Media | Ciclo de vida |
| 14 | Generador de índices (modo aparte) | Media | Media | Blindaje |
| 15 | Respaldo antes de operación irreversible | Media | Media | Seguridad |
| 16 | Detección de contradicciones en la memoria | Baja | Alta | Métricas |

**Orden sugerido:** 01 → 02 → 03 → 07 → 08 (todo Baja complejidad y alto retorno) → 04 → 05 → 12 → 09/10/11 → 13 → 14 → 15 → 06 → 16.

El 06 va casi al final a pesar de ser prioridad Alta: se apoya en el 04 y en el 12, y sin ellos su tasa de falsos positivos lo vuelve inservible.

---

## Grupo A · Blindaje del propio estándar

### 01 · Guardián de versión y CHANGELOG

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Baja | Ninguna |

**Descripción.** Enganche `pre-commit` que mira el diff: si toca [`base/`](../base/) o [`plantillas/`](../plantillas/) y el mismo commit no sube [`VERSION`](../VERSION) ni agrega una entrada en [`CHANGELOG.md`](../CHANGELOG.md), el commit no se crea.

**Problema que resuelve.** `CLAUDE.md §2` y la meta-regla `M10` dicen que versionar no es opcional, pero hoy nada lo impide. Basta un despiste para que un proyecto herede una regla nueva sin que su número de versión cambie — y entonces `version.py`, que compara versiones, deja de detectar el desfase. Es una falla silenciosa que rompe la única garantía de «este proyecto cumple el estándar **de tal fecha**».

**Beneficio esperado.** El versionado deja de ser una promesa. Cualquier proyecto puede confiar en que un `VERSION` distinto significa reglas distintas.

**Cómo se automatiza sin IA.** `git diff --cached --name-only` da los archivos del commit. Si alguno empieza por `base/` o `plantillas/`, se exige que la lista también incluya `VERSION` y `CHANGELOG.md`, y que la primera línea de versión del CHANGELOG coincida con el contenido de `VERSION`. Todo es comparación de cadenas.

**Recomendaciones.** No intentar decidir si el cambio es MAYOR, MENOR o PARCHE — eso sí es criterio, y forzarlo produciría falsos positivos. El guardián exige que **haya** entrada; cuál corresponde lo decide quien escribe. Dejar una salida explícita (`ESTANDAR_SIN_VERSION=1`) para los commits de solo formato, y que la salida diga cuál es.

---

### 05 · Validador de forma de regla (`M4` / `M5` / `M11`)

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| **Alta** | Media | [`base/20-meta-reglas/estructura-regla.md`](../base/20-meta-reglas/estructura-regla.md) |

**Descripción.** Comprobar que cada regla de `base/` respete su propio molde: ID libre del prefijo del capítulo (`M4`), **una sola exigencia** por regla, ejemplo INCORRECTO/CORRECTO presente (`M5`), y ninguna regla borrada o renumerada entre versiones (`M11`).

**Problema que resuelve.** Las meta-reglas del capítulo 20 son las únicas del estándar que nadie comprueba. Se aplican por lectura, y una regla mal formada no se nota hasta que alguien la cita y descubre que exige dos cosas a la vez o que su ID chocó con otro.

**Beneficio esperado.** El estándar deja de poder contradecirse a sí mismo por descuido de forma. Y con `M11` cubierto, ninguna spec o commit histórico queda huérfano por una regla que desapareció.

**Cómo se automatiza sin IA.** El molde de `M5` es un patrón fijo de encabezados y bloques: se comprueba con expresiones regulares sobre cada archivo de `base/`. Los IDs se extraen y se verifica unicidad y prefijo. Para `M11`, se compara el conjunto de IDs contra el del último tag de git: un ID que estaba y ya no está es FALLA salvo que aparezca marcado como derogado.

**Recomendaciones.** Empezar solo por `M4` y `M11` — son binarios y de cero ambigüedad. La «una sola exigencia» de `M5` es la parte fuzzy: aproximarla contando verbos imperativos o conjunciones y reportarla como **AVISO**, nunca FALLA.

---

### 07 · Validador del mapa del sitio

| Prioridad | Complejidad | Dependencias |
|---|---|---|
| Media | Baja | [`anatomia/mapa-del-sitio.md`](../anatomia/mapa-del-sitio.md) |

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

**Descripción.** Programa que **escribe** los índices que hoy `enlaces.py` solo comprueba: el índice de [`historico-chat/README.md`](../historico-chat/README.md), el de [`notas/`](../notas/), el de [`pendientes/`](../pendientes/).

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
| **Alta** | Alta | 04 · 12 · [pendiente 01](01-validadores-de-codigo-de-proyecto.md) |

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

El [README de métricas](../metricas/README.md) ya identifica cuatro números que no se pueden derivar porque falta un marcador. Los tres primeros son ese marcador.

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
| Baja | Alta | [`hecho/memoria-semantica.md`](hecho/memoria-semantica.md) |

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
