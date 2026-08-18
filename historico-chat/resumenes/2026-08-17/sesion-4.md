# 2026-08-17 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-17-sesion-4.md](../../2026-08-17-sesion-4.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «[sesión 3](sesion-3.md)» — allá se ejecutaron 25 de las 51 fases aprobadas y quedaron 26 detenidas por 42 dudas del usuario. Acá se pidió resolver los pendientes, y el pedido se volvió otro: **que ninguno quede suelto**.

---

## Hallazgos de esta sesión

### 1 · El pedido cambió al mirar el backlog, y el cambio fue el hallazgo

**Qué pasó.** Se pidió «resolver los pendientes». Al triar los 30 abiertos, el agente los separó en tres montones —los que solo esperan una decisión, los que se construyen, los de limpieza— y propuso empezar por el más urgente. El usuario cortó eso con una sola línea:

> *«todos los pendientes deben estar dentro de una HU, nada puede estar suelto»*

**Por qué importa.** El triaje del agente era por urgencia; el del usuario es por **cadena**. Son preguntas distintas y la segunda va primero: da igual cuál pendiente sea el más urgente si al construirlo se salta la historia. [`02·F23`](../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) ya lo decía —un pendiente se baja a historia y se construye como fase—, pero lo decía **para el momento de construir**. El usuario lo corrió al momento de **abrir**.

**Dónde queda.** En el trabajo entero de esta sesión, y en las `RN-06` a `RN-08` de [EP-004 · HU-016](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md).

### 2 · Seis pendientes no tenían ninguna historia que los recibiera

**Qué se midió.** Se enrutaron los 33 archivos de [pendientes/](../../../pendientes/README.md) contra las 68 historias del árbol de épicas. **Veintisiete cabían** en una historia que ya existía. **Seis no cabían en ninguna**, y hubo que escribirlas:

| Historia nueva | Recibe |
|---|---|
| [EP-001 · HU-011 — Buscar antes de preguntar](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md) | el 24, que ya la traía redactada adentro |
| [EP-001 · HU-012 — Inventario de acciones y riesgo](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md) | el 13 |
| [EP-001 · HU-013 — Capítulos opt-in de dominio](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md) | el 08 y el 12 |
| [EP-005 · HU-011 — Dónde termina el estándar](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) | el 15 |
| [EP-005 · HU-012 — Hacer cumplir lo que solo se recuerda](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) | el 58 |
| [EP-007 · HU-008 — El proyecto reporta al estándar](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md) | el 36 |

**Por qué importa.** Seis es la medida del hueco. No es que faltaran seis documentos: es que **seis pendientes se iban a construir sin que nadie hubiera escrito cuándo se dan por aceptados**. El 36 y el 58 son los peores del grupo, porque los dos son defectos reportados por un proyecto real y llevaban días esperando.

**Y hay una lectura al revés que también sirve:** las 16 automatizaciones del [09](../../../pendientes/09-autonomia-sin-ia.md) cupieron **todas** en historias que ya existían. Ese tema estaba bien repartido desde el principio, y ahora se puede demostrar.

**Dónde queda.** Las seis escritas con el molde completo, en su épica y en los dos índices.

### 3 · El campo que la HU-016 pedía ya existía a medias, y en el sitio equivocado

**Qué se encontró.** [EP-004 · HU-016](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md) decía desde el 2026-08-16 que faltaba «una pieza antes del programa: un sitio fijo donde el pendiente declare su fase». Al enrutar se vio que el [52](../../../pendientes/52-el-sello-del-checklist-caduca-con-el-texto.md) ya traía una fila `Historia que lo recibiría` y ningún otro la tenía. Un solo archivo de 33 con el campo, y con otro nombre.

**Por qué importa.** Es el patrón que este repositorio ya conoce: **una buena costumbre de un solo archivo no es una convención**. Mientras viva en uno solo, el programa que la lea no encuentra nada que leer, y quien escriba el siguiente pendiente no la va a copiar porque no la va a ver.

**Dónde queda.** El campo quedó fijo y con un solo nombre —`Historia de usuario`— en la ficha de cabecera de los **33** archivos. La tarea de la HU-016 que pedía fijarlo está marcada como hecha.

### 4 · El script de enrutamiento metió la fila dentro de la tabla equivocada, en tres archivos

**Qué pasó.** El programa que escribió las 33 filas buscaba «la primera tabla de las 15 primeras líneas». En el [18](../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md), el [19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) y el [23](../../../pendientes/23-plantillas-mezcla-modelos-con-procedimientos.md) esa tabla no era la ficha: era una tabla de contenido. La fila quedó entre los datos.

**Por qué importa.** Ningún validador lo habría visto: el enlace resuelve, la tabla sigue siendo tabla y el conteo daba 33 de 33. **Lo destapó una comprobación escrita a propósito** —que la fila estuviera precedida por el encabezado vacío `| | |`—, no la corrida de siempre. Una comprobación que se escribe para dudar del propio trabajo encuentra lo que las otras no buscan.

**Dónde queda.** Los tres archivos revertidos y rehechos. La regla del programa quedó siendo «encabezado sin nombres de columna», que es lo que distingue la ficha de una tabla cualquiera.

### 5 · El nombre de la HU-016 se quedó corto y no se cambia

**Qué se decidió.** La historia se llama «el pendiente **cerrado** nombra su fase» y desde hoy cubre también al abierto. Renombrar la carpeta habría dejado rotos todos los enlaces que la citan.

**Por qué importa.** Eso es exactamente el [pendiente 54](../../../pendientes/54-cerrar-un-pendiente-rompe-sus-citas.md) —cerrar un pendiente dejó 12 enlaces huérfanos en un solo día—, y no tenía ningún sentido reproducirlo dentro del trabajo que lo enruta. **El nombre queda; el alcance lo dicen las `RN` y los `CA`**, que es el mismo criterio con que [`20·M11`](../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) prohíbe renumerar una regla.

**Dónde queda.** Escrito dentro de la propia historia y en su `README`, para que nadie lo «arregle» después.

### 6 · Lo que esta sesión **no** hizo, y por qué

**Ningún pendiente se cerró.** El pedido inicial era resolverlos; el segundo fue enrutarlos, y eso es lo que se hizo. Los 30 siguen abiertos.

**No se tocó `base/` ni `plantillas/`**, así que no hubo entrada de `CHANGELOG` ni subida de `VERSION`: lo que cambió es `documentacion/` y `pendientes/`, y [`20·M10`](../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) pide versión cuando cambia lo que se le exige a un proyecto. Acá no cambió.

**La regla no está escrita todavía.** «Todo pendiente nombra su historia» vive hoy en las `RN` de una HU, no en `base/`. Escribirla allá es una fase con su plan y sus pruebas, y esa fase necesita aprobación: es el eslabón que [`02·F23`](../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) exige y que esta sesión no puede saltarse justamente por lo que vino a arreglar.

**Lo que quedó comprobado:** `validar.py estandar` da **0 fallas** con los mismos 5 avisos conocidos —los falsos positivos del [55](../../../pendientes/55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md)—, y las 36 pruebas del repositorio pasan.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ los 30 siguen abiertos, cada uno con su historia declarada |
| Toda historia disparada está escrita en su épica | ☑ las seis nuevas, con su fila en la épica y en los dos índices |
| Lo que se hizo está aprobado y guardado | ☐ **falta:** el usuario no ha revisado ni autorizado el commit |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

**Lo que sigue, cuando se retome:** construir la fase que escribe la regla en `base/` y el programa que la comprueba (los `CA-05` a `CA-07` de la HU-016). Sin eso, el enrutamiento de hoy es un estado que nada sostiene, y el pendiente 60 nace suelto.
