# 22 · Sistemas que aprenden de datos  ·  `[CAPA 2 · opt-in]`

> **Historia dueña del texto:** [EP-001 HU-035](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-035-el-capitulo-22-sistemas-que-aprenden-de-datos/HU-035-el-capitulo-22-sistemas-que-aprenden-de-datos.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

**Opt-in.** Reglas agnósticas para construir un producto donde **un modelo estadístico decide o sugiere algo**: el que se entrena con datos propios, el que llama al modelo de un tercero, o el que deja que una respuesta automática entre al flujo del negocio. Aplican a esos proyectos; el resto las omite.

**El agente construye el sistema, no responde por sus decisiones.** Produce el diseño, la ficha del modelo, las mediciones y sus pruebas; **quién autoriza que decida sobre alguien es del humano** ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), [`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)). Qué modelo y dónde corre lo declara la capa 3 (`.agente/stack.md`).

**Lo que lo separa del software corriente:** acá el sistema **puede dejar de acertar sin que nada se rompa**. El código sigue igual, las pruebas siguen verdes, no hay error en los registros, y las respuestas ya no sirven, porque cambió la realidad de la que se aprendieron. Casi todas estas reglas salen de eso.

**El capítulo [`19`](19-observabilidad-y-operacion.md) dice cómo se vigila un servicio; acá se agrega qué se vigila de un modelo, que es distinto.** El [`12`](12-privacidad-datos.md) cubre los datos personales y el [`16`](16-cumplimiento-y-calidad.md) el cumplimiento: ninguno pregunta con qué se entrenó ni quién responde cuando se equivoca.

---

## IA1 · Todo modelo en marcha está en un inventario antes de recibir tráfico

El inventario dice **qué modelos hay corriendo**, y de cada uno: qué decide, quién lo puso, con qué datos aprendió y desde cuándo. Un modelo que no está en el inventario no se despliega.

```
INCORRECTO: el modelo entró con la funcionalidad; qué hay corriendo se
            averigua leyendo el código de cada servicio
CORRECTO:   el modelo está en el inventario antes de recibir su primera
            petición, con qué decide y de qué datos aprendió
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Es la primera del capítulo porque sin ella ninguna otra se puede aplicar.** No se le pone dueño, ni riesgo, ni vigilancia a lo que no se sabe que existe.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA2 · Cada modelo tiene a cargo una persona con nombre, no un área

En el inventario, la casilla de responsable lleva **el nombre de alguien**. Un área no lee un aviso de desvío ni decide apagar un modelo: eso lo hace una persona, y si no está escrita, no lo hace nadie.

```
INCORRECTO: responsable: equipo de datos
CORRECTO:   responsable: «nombre de la persona», y su reemplazo mientras
            no esté
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Depende de [`IA1`](#ia1--todo-modelo-en-marcha-está-en-un-inventario-antes-de-recibir-tráfico)** ([`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md)): la casilla vive en el inventario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA3 · El control se gradúa por lo que la decisión puede dañar

Cada modelo del inventario lleva **qué tan grave es que se equivoque con una persona**, y de ahí sale cuánto control se le pone. Ordenar un catálogo y negarle algo a alguien no llevan la misma revisión.

```
INCORRECTO: todos los modelos pasan la misma aprobación, porque la
            aprobación es del área y no del daño
CORRECTO:   el que ordena un catálogo se aprueba una vez; el que le niega
            algo a una persona lleva revisión humana y medición de sesgo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Es la misma graduación que [`00·N1`](00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada) le aplica a las acciones del agente**, aplicada acá a las decisiones del modelo: el riesgo lo fija lo que pasa si sale mal, no quién lo hizo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA4 · Que el modelo sugiera y que el modelo ejecute se aprueban por separado

Pasar de **proponer** a **hacer** es una autorización nueva, aunque el modelo sea el mismo y acierte igual. Mientras sugiere, una persona filtra el error; cuando ejecuta, el error ya ocurrió.

```
INCORRECTO: el modelo venía sugiriendo bien seis meses, así que se le
            conecta la ejecución directa
CORRECTO:   ejecutar directo se autoriza aparte, con quién lo autorizó y
            qué pasa cuando se equivoque
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Es el mismo corte que [`02·F25`](02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md) hace con los planes:** que algo esté autorizado no autoriza el paso siguiente, por parecido que sea.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA5 · Un modelo que sigue aprendiendo se vuelve a revisar en un plazo escrito

Si el modelo cambia después de aprobado, **la aprobación de una sola vez no vale**: lo que se revisó ya no es lo que está corriendo. El plazo de la próxima revisión se escribe el día que se aprueba.

```
INCORRECTO: se aprobó en marzo y sigue aprendiendo de lo que entra; la
            aprobación de marzo se sigue citando en diciembre
CORRECTO:   se aprobó en marzo, se revisa cada tres meses, y la fecha de
            la próxima está en la ficha
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Depende de [`IA6`](#ia6--el-modelo-en-marcha-se-vigila-por-si-sigue-acertando-no-solo-por-si-responde)**, que es lo que da el dato con el que se revisa.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA6 · El modelo en marcha se vigila por si sigue acertando, no solo por si responde

La vigilancia de [`19`](19-observabilidad-y-operacion.md) dice si el servicio está en pie. Acá se agrega **si las respuestas siguen sirviendo**: un modelo se desvía sin lanzar un solo error, porque cambió la realidad y no el código.

```
INCORRECTO: el tablero muestra disponibilidad y tiempo de respuesta, y
            de ahí se concluye que el modelo está bien
CORRECTO:   además se mide si acierta como el día que se aprobó, y hay un
            umbral con un aviso a la persona a cargo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Es el tramo que se olvida**, y el único que no avisa solo: los otros cinco del ciclo tienen a alguien esperándolos, este no.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA7 · La ficha del modelo dice de dónde salieron los datos y qué permiten hacer

De cada conjunto con el que el modelo aprendió se escribe **su origen y bajo qué términos se puede usar**. Es lo más barato de conseguir y lo más caro de arreglar: cuando el problema aparece, el modelo ya está entrenado.

```
INCORRECTO: la ficha dice «datos históricos de la operación» y ahí
            termina
CORRECTO:   dice de qué sistema salieron, de qué periodo, quién los cedió
            y para qué usos
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Concreta [`12`](12-privacidad-datos.md) para el caso del entrenamiento**, donde el dato no se consulta: queda incorporado y no se puede sacar de vuelta.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA8 · Se escribe qué medida se le pidió optimizar y por qué esa

Un modelo entrenado por resultados persigue **la medida que se le escribió**, no la que se tenía en la cabeza. Cuando el comportamiento sale absurdo, casi siempre la medida estaba mal escrita, y eso lo escribió alguien.

```
INCORRECTO: se optimiza «tiempo en la aplicación» y nadie anotó por qué
            se eligió esa medida
CORRECTO:   se optimiza «tiempo en la aplicación» porque se buscaba X, y
            queda escrito qué comportamiento indeseado podría producir
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Aplica solo a los modelos que aprenden por consecuencias**, no a todos: para los demás la fila queda sin caso y la regla no se invoca.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IA9 · Retirar un modelo se registra con qué queda en su lugar

Un modelo se apaga, y lo que decidía **lo sigue decidiendo algo**: otro modelo, una regla escrita, o una persona. Se escribe cuál de las tres antes de apagarlo.

```
INCORRECTO: se apagó el modelo y las peticiones empezaron a devolver el
            valor por defecto, que nadie había pensado como decisión
CORRECTO:   se apagó, y queda escrito que desde esa fecha lo decide una
            regla fija, con cuál
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v25.0.0**, el **2026-08-19**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Cierra el ciclo que abre [`IA1`](#ia1--todo-modelo-en-marcha-está-en-un-inventario-antes-de-recibir-tráfico)**: el inventario dice qué hay corriendo, y sin esta regla nunca dice qué dejó de correr.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

## El ciclo, y quién responde en cada tramo

Las nueve reglas de arriba caen sobre seis tramos. La tabla no exige nada por sí sola: **es el mapa de dónde aplica cada una**.

| Tramo | La pregunta que hay que responder | Regla |
|---|---|---|
| Caso de uso | ¿Qué problema resuelve y cuánto vale resolverlo? | `IA3` |
| Datos | ¿De dónde salen y qué permiten hacer con ellos? | `IA7` |
| Modelo | ¿Qué método, y qué medida se le pidió perseguir? | `IA8` |
| Despliegue | ¿Quién lo usa, con qué límites, y sugiere o ejecuta? | `IA1`, `IA2`, `IA4` |
| Vigilancia | ¿Sigue acertando? ¿Se desvió? | `IA6`, `IA5` |
| Retiro | ¿Cuándo se apaga, y qué queda decidiendo? | `IA9` |

## Los cuatro insumos, y el riesgo que trae cada uno

| Insumo | Riesgo que introduce |
|---|---|
| Datos | Sesgo, datos de personas, calidad, y bajo qué términos se pueden usar. |
| Método | Opacidad: modelos que aciertan sin poder decir por qué. |
| Capacidad de cómputo | Dependencia de quien la presta, costo que sube con el uso, y en qué país queda el dato. |
| Personas | Quién responde. Sin alguien a cargo, no responde nadie. |

**La mayoría de estos proyectos no fracasa por el método.** Fracasa por los datos, lo más barato de conseguir y lo más caro de arreglar, o por las personas, que es el único de los cuatro que no se compra hecho.

## Plantillas

- [`plantillas/ficha-modelo.md`](../plantillas/ficha-modelo.md): qué decide, con qué datos, qué medida persigue, quién responde y cómo se mide.
- El registro de por qué se aprobó va en el [`ADR`](../plantillas/ADR.md), que ya existe: una decisión de modelo es una decisión de arquitectura y no necesita documento propio ([`20·M12`](20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)).
