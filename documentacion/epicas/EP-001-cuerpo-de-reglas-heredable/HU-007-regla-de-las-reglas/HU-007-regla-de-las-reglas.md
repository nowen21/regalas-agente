# HU-007 — La regla que gobierna cómo se escriben las reglas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | Quien define el estándar |
| **Estado** | Backlog |

## 2. Narrativa

- **Como** quien agrega y cambia reglas con el tiempo
- **Quiero** que esté escrito el procedimiento para hacerlo
- **Para** que el cuerpo no se degrade a punta de reglas mal ubicadas, repetidas o que exigen dos cosas

## 3. Contexto y descripción

El molde de HU-001 dice cómo se ve una regla. Falta lo otro: qué se hace antes de escribirla. Buscar si ya existe, decidir en qué capítulo va, comprobar que sirva a cualquier proyecto, elegir un identificador libre, declarar de qué depende, decidir si se puede comprobar con un programa.

Sin ese procedimiento, el cuerpo crece torcido: la misma exigencia en dos capítulos, reglas que solo sirven a un stack, identificadores que chocan.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Antes de crear una regla se busca si ya existe una que cubra el caso |
| RN-02 | Un tema tiene un solo capítulo dueño |
| RN-03 | Una regla que solo sirve a un lenguaje o a un cliente no entra al cuerpo central |
| RN-04 | El identificador es único, estable y no repite el prefijo del capítulo |
| RN-05 | La regla declara de cuál depende y qué excepciones tiene, con quién las autoriza |
| RN-06 | Se decide y se marca si la regla se puede comprobar con un programa |
| RN-07 | Ninguna regla de proyecto existe sin una regla de la base que la respalde |

### 3.2 Supuestos

- Este procedimiento se aplica también a sí mismo: las reglas de este capítulo cumplen el molde igual que las demás.

### 3.3 Fuera de alcance

- El programa que comprueba que el procedimiento se cumplió. Eso es EP-004.
- La derogación, que va en HU-008.
- El versionado del cuerpo, que es EP-002.

## 4. Criterios de aceptación

### CA-01 — Una regla nueva se enruta al capítulo correcto

```gherkin
Dado que existe el procedimiento para agregar una regla
Cuando se quiere agregar una exigencia nueva
Entonces el procedimiento lleva a buscar primero si ya existe
Y si no existe, indica en qué capítulo va y por qué
```

**Cómo validarlo:**

1. Escoger una exigencia nueva de cualquier tema, por ejemplo algo sobre manejo de archivos temporales.
2. Seguir el procedimiento paso a paso. Resultado esperado: el primer paso es buscar si ya existe algo que la cubra.
3. Continuar hasta el paso de enrutamiento. Resultado esperado: queda decidido el capítulo dueño con el motivo escrito.
- **Aprobado cuando:** la regla queda en un solo capítulo y el motivo está escrito.

### CA-02 — Una regla atada a un stack no entra

```gherkin
Dado que el procedimiento exige que la regla sirva a cualquier proyecto
Cuando alguien propone una regla que nombra un framework
Entonces el procedimiento la rechaza para el cuerpo central
Y la manda a la capa del proyecto
```

**Cómo validarlo:**

1. Proponer a propósito una regla que nombre un framework concreto.
2. Aplicarle el paso del procedimiento que revisa si es agnóstica. Resultado esperado: no pasa, y dice por qué.
3. Reescribirla sin nombrar la tecnología, dejando solo la exigencia de fondo. Resultado esperado: ahora sí pasa, y el detalle concreto queda como ajuste del proyecto.
- **Aprobado cuando:** la versión con framework no entra y la agnóstica sí.

### CA-03 — Una regla que exige dos cosas se parte antes de entrar

```gherkin
Dado que el molde exige una sola exigencia por regla
Cuando el procedimiento revisa una regla candidata con dos exigencias
Entonces indica partirla antes de aceptarla
```

**Cómo validarlo:**

1. Proponer una regla que diga dos cosas distintas.
2. Aplicarle el paso del procedimiento que revisa el molde. Resultado esperado: señala que hay dos exigencias.
3. Partirla en dos y volver a aplicar el procedimiento a cada una. Resultado esperado: las dos pasan y cada una tiene su propio identificador.
- **Aprobado cuando:** la candidata doble no entra, y las dos partidas sí.

### CA-04 — Se sabe qué reglas llevan más tiempo sin que nadie las revise

```gherkin
Dado que una regla equivocada se comporta igual que una correcta
Cuando se pregunta qué reglas llevan más tiempo sin revisarse de fondo
Entonces se obtiene la lista ordenada de la más vieja a la más nueva
Y cada una dice cuándo se revisó y cuántos incumplimientos produce hoy
```

**Por qué no lo cubría ninguno de los tres anteriores.** `CA-01`, `CA-02` y
`CA-03` revisan una regla **al entrar**: dónde va, si es agnóstica, si exige una
sola cosa. Ninguno vuelve a mirarla después. El sello que dejan dice *«vale
mientras el texto no cambie»*, y lo que cambia sin avisar no es el texto: es el
mundo que la regla describía.

**Cómo validarlo:**

1. Pedir la lista sobre el estándar. Resultado esperado: sale ordenada, encabezada por las que **nunca** se revisaron de fondo.
2. Escribirle a una regla la línea de revisión con la fecha de hoy y volver a pedirla. Resultado esperado: esa regla deja de encabezar y aparece con su fecha.
3. Comprobar que no hay umbral: ninguna corrida falla por antigüedad. Resultado esperado: informa, no detiene.
- **Aprobado cuando:** la lista existe, ordena de la más vieja a la más nueva, y **no bloquea nada**.

### CA-05 — Una regla validable no se automatiza hasta que se sepa que sirve

```gherkin
Dado que una regla quedó declarada validable
Cuando alguien va a construir el programa que la comprueba
Entonces el procedimiento exige responder antes, por escrito, si la regla se cumple hoy a mano, cuántas veces se incumplió y por qué, y cuántas falsas alarmas daría
Y si se incumplió por estar mal escrita, manda corregir la regla antes que construir el validador
Y si solo falla acordarse, no lo detiene
```

**Por qué no lo cubría ninguno de los cuatro anteriores.** `CA-01` a `CA-03`
revisan la regla **al entrar**; `CA-04` pregunta si **sigue sirviendo** después.
Ninguno se para en el momento en que una regla pasa de texto a programa. Y ese
momento tiene su propio defecto: `RN-06` manda marcar si la regla **se puede**
comprobar con un programa, y de ahí se saltaba a construirlo, sin preguntar si
**convenía**. Una regla mal escrita se automatiza perfectamente, y entonces
falla sola, en cada commit, sin que nadie la haya vuelto a leer.

**Cómo validarlo:**

1. Tomar un ítem del backlog de automatizaciones que la casa ya haya pospuesto por falsas alarmas (el 06, la puerta `F2` mecánica) y aplicarle las tres preguntas. Resultado esperado: la tercera lo detiene, con el mismo motivo que el backlog anotó caso por caso.
2. Tomar una regla que hoy se cumple y cuyo único defecto es que hay que acordarse (el 01, el guardián de versión) y aplicarle las tres preguntas. Resultado esperado: pasa; el criterio no la frena.
3. Tomar una regla que reprobó su checklist por exigir dos cosas (`F4` antes de partirse) y aplicarle la segunda pregunta. Resultado esperado: manda corregir la regla, no construir el validador.
- **Aprobado cuando:** el criterio está escrito como regla del capítulo `20`, detiene el caso que debía detener, deja pasar el que debía pasar, y manda corregir antes que automatizar el que estaba mal escrito.

### CA-06 — Lo que se pidió dos veces no se pierde entre sesiones

```gherkin
Dado que el usuario pidió un mismo criterio en dos sesiones distintas y en el momento nadie lo notó
Cuando se va a publicar la versión que cierra ese tramo
Entonces el procedimiento obliga a releer el tramo y a escribir ese criterio como candidata a regla, con las veces que se pidió
Y la candidata sale con una de cuatro salidas: cubierta, regla nueva, afinar una existente, o no es regla del estándar
Y ninguna candidata se convierte en regla desde ese documento: eso lo decide el usuario
```

**Por qué no lo cubría ninguno de los cinco anteriores, ni `01·C10`.** `C10` atrapa el patrón **en el momento** en que el pedido llega, y lo que se pierde es justamente lo que en el momento no se notó: dos pedidos parecidos, con otras palabras, separados por diez sesiones. `CA-01` a `CA-03` revisan la regla cuando ya alguien decidió escribirla; este se para antes, cuando todavía nadie la propuso.

**Cómo validarlo:**

1. Tomar el barrido que se hizo a mano el 2026-08-13 ([prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md](../../../../prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md)) y comprobar que el molde del estándar habría producido lo mismo: 27 fichas, cada una con una de las cuatro salidas. Resultado esperado: ninguna de las 27 se queda sin salida posible.
2. Comprobar que el disparo existe en el flujo: la regla nombra el momento de publicar la versión, que `20·M10` ya obliga a atravesar. Resultado esperado: el barrido no depende de que alguien se acuerde de pedirlo.
- **Aprobado cuando:** el molde está en `plantillas/`, la regla del capítulo `20` lo exige antes de publicar, y las cuatro salidas están escritas y son excluyentes.

### Criterios de aceptación transversales

- [ ] **Validación** — el procedimiento dice qué hacer cuando falta un dato, por ejemplo cuando no hay ejemplo posible.
- [ ] **No regresión** — aplicar el procedimiento a las reglas ya escritas no obliga a renumerarlas.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Aplicabilidad | El procedimiento se puede seguir sin haber escrito reglas antes |
| Autocumplimiento | Las reglas de este capítulo cumplen su propio procedimiento |
| Comprobabilidad | Los pasos binarios quedan marcados como comprobables por un programa |

## 6. Tareas técnicas derivadas

- [ ] Escribir los pasos del procedimiento, en orden.
- [ ] Escribir el criterio de enrutamiento entre capítulos.
- [ ] Escribir la exigencia de que una regla de proyecto nombre la de la base que concreta.
- [ ] Marcar cuáles pasos puede comprobar un programa.
- [ ] Aplicar el procedimiento a las reglas ya escritas y anotar el resultado.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla](A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |
| [B-EP-001-HU-007-primero-que-el-proceso-sirva](B-EP-001-HU-007-primero-que-el-proceso-sirva/README.md) | CA-05 | **Cerrada 2026-08-21 — Cumple** (3 de 3 casos aprobados; v28.1.0). Nace `20·M19`, desde el [pendiente 16](../../../../pendientes/hecho/primero-que-el-proceso-sirva.md) |
| [C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador](C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador/README.md) | CA-06 | **Cerrada 2026-08-22 — Cumple** (5 de 5; v31.0.0). Nace `20·M20` y el molde del barrido, desde el punto 2 del [pendiente 33](../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md) |

**La fase retro-documenta y no toca el capítulo `20`.** El procedimiento existe y se usa en cada cambio: dieciséis meta-reglas, el molde y un checklist de veinte filas. Lo que falta es el caso escrito que muestre una candidata enrutada, otra rechazada por nombrar una tecnología y otra partida en dos.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta historia de usuario |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada criterio | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el criterio quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001, porque el procedimiento se apoya en el molde | Alto |
| Dependencia | HU-002, por el enrutamiento entre capas | Alto |
| Riesgo | Que el procedimiento sea tan largo que se salte | Los pasos se ordenan del más barato al más costoso |
| Riesgo | Que las reglas de este capítulo no cumplan su propio molde | Se aplican a sí mismas como parte de la definición de terminado |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Molde de regla ya definido
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] El procedimiento está escrito paso a paso
- [ ] Las reglas del capítulo cumplen su propio procedimiento
- [ ] Cada paso binario está marcado como comprobable
- [ ] Todos los criterios de aceptación verificados

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Parcial | Necesita el molde y las capas |
| Negociable | Sí | El orden de los pasos se discute |
| Valiosa | Sí | Es lo que evita que el cuerpo se degrade con el tiempo |
| Estimable | Sí | Un capítulo |
| Pequeña | Sí | Pocos pasos, bien definidos |
| Testeable | Sí | Se verifica proponiendo reglas malas a propósito |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-20 | El agente, por orden del usuario | `CA-05` y fase B, desde el pendiente 16: el criterio de si conviene automatizar, que ningún CA cubría |
| 2026-08-21 | El agente, con la opción 1 y los planes aprobados por el usuario | Fase B cerrada en Cumple: los tres casos del `CA-05` aprobados, versión 28.1.0, pendiente 16 a `hecho/`. El usuario confirmó la elección (CA nuevo en HU-007) que la sesión cortada del 20 había tomado sin registro |
