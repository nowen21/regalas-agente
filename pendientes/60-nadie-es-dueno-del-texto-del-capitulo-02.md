# Pendiente · Ninguna historia es dueña del texto del capítulo `02`

**Estado:** abierto · anotado 2026-08-17.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-007 — La regla que gobierna cómo se escriben las reglas](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) — decidir quién es dueño del texto de un capítulo es meta-regla: gobierna dónde se escribe una regla, que es lo que esa historia cubre |
| **De dónde sale** | El bloqueo `B-02` de la fase [`B-EP-004-HU-016`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia/plan_trabajo.md), al buscar dónde escribir un cambio de `02·F23` |
| **Proyecto de origen** | El estándar mismo |

## El problema

Se necesitaba agregarle una frase a [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) — que el pendiente nombre su historia **desde que se abre**, no solo al construirse. Y no hubo dónde ponerlo, porque **ninguna historia de usuario declara el capítulo `02` como su módulo**.

Se buscó el 2026-08-17 en las siete épicas. Esto es lo que hay:

| Módulo declarado | Historias |
|---|---|
| Capítulo `00 · Núcleo blindado` | EP-001 · HU-003, HU-012 |
| Capítulo `01 · Conducta de la IA` | EP-001 · HU-004, HU-011 |
| Cuerpo de reglas (en general) | EP-001 · HU-001, HU-002, HU-005 a HU-010 |
| Cuerpo de reglas — capa opt-in | EP-001 · HU-013 |
| **Capítulo `02 · Flujo de trabajo`** | **ninguna** |

Siete historias **citan** el capítulo `02` —en EP-004, EP-005 y EP-007—, pero todas para **comprobarlo** o para **dispararlo**. Ninguna para escribirlo.

## Por qué importa

El `02` es el capítulo de la cadena: `F0`, `F2`, `F4`, `F8`, `F11`, `F12`, `F15`, `F20`, `F22`, `F23`. Es el que más se cita en todo el repositorio y el que gobierna cómo se hace cualquier trabajo.

**Cambiarlo hoy es exactamente lo que el estándar prohíbe hacer.** [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) manda bajar todo cambio a una historia y construirlo como fase suya; si no hay historia que reciba un cambio del `02`, entonces **todo cambio del `02` se ha estado haciendo sin cadena** — incluida la regla que exige la cadena.

Y no es hipotético: `F22` y `F23` nacieron en agosto, las dos sin historia propia. `F23` sí terminó documentada, pero en [EP-004 · HU-016](../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md), que es la historia de **comprobarla**, no la de escribirla. La comprobación quedó con dueño y el texto no.

## Qué falta

Decidir cuál de las tres, y escribirlo:

**A · Una historia nueva en EP-001 para el capítulo `02`.** Es lo simétrico: el `00` y el `01` tienen la suya y el `02` no. Cuesta una historia y deja el patrón parejo.

**B · Ampliar el módulo de [EP-001 · HU-007](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md)**, que ya es «cuerpo de reglas» y es la historia de cómo se escribe una regla. Es lo más barato, y es donde este pendiente queda enrutado mientras se decide. Riesgo: esa historia pasa a ser el cajón de todo lo que no tiene dueño.

**C · Revisar los 21 capítulos.** El `02` es el que se destapó, pero **no se comprobó si los otros dieciocho tienen dueño** — solo se vio que el `00` y el `01` lo tienen. Si faltan más, la decisión no es sobre el `02`: es sobre cómo se reparten los capítulos entre historias, y conviene tomarla una sola vez.

**La C es la que corresponde**, y empieza por medir. Las otras dos tapan el caso que se vio.

## El límite

No es urgente **hoy** porque nada está roto: las reglas del `02` funcionan. Lo que está roto es la trazabilidad hacia arriba — no se puede decir de dónde bajó ninguna de ellas.

## Con qué se cruza

- La fase [`B-EP-004-HU-016`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia/plan_trabajo.md), cuyo `B-01` espera esta decisión para poder escribirse.
- El [47](47-las-reglas-de-negocio-del-estandar-no-dicen-de-donde-bajan.md), que es el mismo hueco un piso más abajo: allá son 31 reglas de negocio que no dicen de dónde bajan, acá es un capítulo entero.
- El [56](56-el-estandar-no-tiene-planteamiento.md), que es el mismo hueco en la cabeza de la cadena.

**Los tres dicen lo mismo con distinto tamaño:** este repositorio exige trazabilidad hacia arriba y no la tiene sobre sí mismo.

## Cómo se sabrá que cerró

Se puede nombrar, para cualquier capítulo de `base/`, la historia de usuario donde se escribe su texto. Y un cambio de `02·F23` tiene dónde bajarse.
