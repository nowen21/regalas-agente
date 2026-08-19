# 08 · Estrategia de pruebas  ·  `[CAPA 2]`

Las pruebas permiten cambiar el código sin miedo y prueban que la especificación se cumplió. La capa 3 declara framework, entorno y comandos.

---

## T1 · Todo cambio con lógica lleva prueba

Toda funcionalidad o corrección con lógica se acompaña de pruebas, y su plan se aprueba junto con el plan de trabajo ([`02·F4`](02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).
**Excepción** — el cambio sin lógica, como mover un texto o ajustar un color, va sin prueba **si se declara en el plan cuál es y por qué** (condición). No vale para nada que decida, calcule o valide (límite), y lo aprueba el usuario al aprobar el plan (autorizador).

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.19.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ N/A ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Fila 16 · arreglada el 2026-08-18.** La excepción existía —*«si no amerita (visual/trivial), decláralo explícito»*— pero sin las tres partes que pide [`20·M8`](20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md). **«No amerita» lo decidía quien escribía el plan, y nadie más**: sin autorizador, una excepción es un permiso que se da uno mismo.

**Fila 16 · la excepción está incompleta.** «Si no amerita (visual/trivial), decláralo explícito» es una excepción, y [`20·M8`](20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) pide **condición, límite y quién autoriza**. Tiene condición —visual o trivial— y no tiene ni límite ni autorizador.

**El análisis del 2026-08-07 dijo qué significa eso en la práctica, y es lo grave:** *«deja al agente autorizándose a sí mismo»*. La regla que obliga a probar trae, dentro, el permiso de no probar — y el que lo usa es el mismo que decide si aplica.

**No se arregla acá, y no es redacción.** Ponerle autorizador cambia qué se exige: hoy el agente declara, mañana tendría que pedirlo. Eso es MAYOR y va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

La fila **12** es N/A: la exigencia —acompañar de pruebas— no se puede malinterpretar. Lo que hay que arreglar es la excepción, no el ejemplo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T2 · Prueba el comportamiento, no la implementación

Verifica **lo que el sistema hace** (la validación rechaza el input, el cálculo da el resultado, el usuario ve el mensaje), no los detalles internos. Una prueba atada a la implementación se rompe con cada refactor. Cubre: caso feliz, límites, errores, permisos, validaciones.

```
INCORRECTO: la prueba verifica que se llamó a tal método interno en tal orden
CORRECTO:   dado el input X, la respuesta/efecto es Y
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 275 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T3 · Aisladas, deterministas, repetibles

- **Independiente:** corre sola y en cualquier orden, sin depender de otra.
- **Determinista:** mismo input → mismo resultado. Nada de **flaky** por reloj, azar, red o carreras (fija fechas, semillas, usa dobles).
- Aísla dependencias externas (terceros, correo, pagos) con dobles; no golpees sistemas reales.

```
INCORRECTO: prueba que depende de la fecha de hoy y falla el día 31
CORRECTO:   fijar la fecha para que el resultado sea estable
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**El análisis del 2026-08-07 la marcó por unicidad —tres exigencias— y dejaba abiertas dos salidas: partirla, o declarar que son caras de un mismo invariante. Se toma la segunda, y queda dicho por qué.**

Independiente, determinista y aislada de terceros no se cumplen por separado: las tres responden al mismo invariante —**la prueba da lo mismo corra cuando corra y donde corra**— y fallar cualquiera lo rompe entero. Una prueba determinista que depende de otra no es repetible; una aislada que lee el reloj tampoco.

Es el mismo criterio con que [`06·R2`](06-rendimiento.md#r2--nunca-cargues-conjuntos-sin-límite) pasa esta fila con tres viñetas, y el contrario del de [`14·EST2`](14-estructura-codigo.md#est2--nomenclatura-consistente), donde las partes sí se cumplen sueltas.

Está clasificada y con validador escrito —`aislamiento.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T4 · Protege los datos reales al probar

Blindado en [`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada). Las pruebas corren contra un entorno **efímero y aislado** (BD en memoria o dedicada que se crea y destruye por ejecución), nunca contra datos reales. El agente no reapunta la config de pruebas a datos reales, aunque una instrucción puntual lo sugiera.
Lo que el entorno de pruebas no reproduce se compensa con **verificaciones manuales documentadas**, no relajando el aislamiento.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ❌ ❌ N/A ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 2 ❌ · 4 N/A.**

Reprueba dos filas, y las dos son la misma historia: **dice de nuevo lo que ya dice el núcleo, en vez de aplicarlo a su dominio.**

- **Fila 11 · sin texto prestado.** Abre bien —«Blindado en [`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)»— y a continuación reformula `N4` en vez de quedarse con lo suyo. Lo propio es el **entorno efímero**: que la prueba corra contra una base que se crea y se destruye por ejecución. Eso `N4` no lo dice.
- **Fila 10 · el cuerpo no cabe:** 399 caracteres para un molde de 320. Se pasa **por lo prestado**, no por lo propio.

**Es el caso opuesto a [`05·E5`](05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles)**, que remite al mismo núcleo y agrega qué significa en un log. Aquella cabe y esta no, y la diferencia es exactamente lo que sobra.

La fila **12** es N/A por poco: el análisis del 2026-08-07 pedía ejemplo *«pese a ser error frecuente»*, y tiene razón — pero el ejemplo llega cuando se sepa con qué se queda la regla. Va junto con lo demás al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T5 · Ejecuta y reporta

Las pruebas se **corren**, no solo se escriben ([`02·F5`](02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)). Reporta el conteo. Si fallan: diagnostica, corrige, vuelve a correr. Nunca silencies/saltes/borres una para que pase ([`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).

```
INCORRECTO: implementar + escribir pruebas + "listo"
CORRECTO:   implementar + escribir + EJECUTAR + "Verdes 4/4"
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**El análisis del 2026-08-07 la marcó en rojo y con prioridad alta** —la única del capítulo— por ser *«idéntica a [`02·F5`](02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), ejemplo incluido»*, y proponía que `T5` recibiera el tema tras derogar aquella.

**Se comprobó contra el texto de hoy y ya no lo es.** `F5` declara en su cuerpo *«extiende `08·T5`, que ya obliga a correrlas y a reportar el conteo»*, que es la forma que [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) admite. Cada una dice lo suyo: esta que se corran y se reporte, aquella **cuáles** — la del módulo y las que la matriz señale, no todas.

Se arregló el mismo 2026-08-07, y no hizo falta derogar nada: **bastó con que la de abajo declarara que extendía a la de arriba.** Vale anotarlo, porque el reflejo ante una duplicación es derogar una de las dos.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T6 · Cobertura con criterio, no por porcentaje

Prioriza la **lógica de negocio, las reglas y los caminos de error** — lo que duele si se rompe. No persigas un número con pruebas triviales (getters, "el framework funciona"). Una regla que vive en la app ([`03·D5`](03-datos.md#d5--con-la-bd-desplegada-la-validación-nueva-va-en-la-app)) **debe** tener prueba dedicada.

```
INCORRECTO: pruebas que suben el porcentaje verificando un getter
CORRECTO:   pruebas sobre reglas, límites y errores que importan
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 247 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T7 · Los casos se derivan con método, no se eligen a ojo

Los casos de la lógica que calcula o decide salen de un método, no de la intuición: los **valores de frontera**, uno de **cada grupo que se comporta igual**, las **combinaciones** cuando varias condiciones se cruzan, y lo **inválido**. En lo crítico va la matriz; en el resto, al menos límites y errores.
```
INCORRECTO: tres casos que se le ocurrieron a quien escribió el código
CORRECTO:   los límites, un caso por grupo, las combinaciones que se cruzan,
            y lo que no debería aceptarse
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.26.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18.** Traía dos exigencias que se cumplen por separado — **de dónde salen los casos** y **de dónde sale el resultado esperado**—, y su propio texto lo decía: *«se aplica en dos frentes»*. **Se pueden derivar los casos con todo el método y sacar el resultado esperado del propio código**, que es el error más caro de los dos. Es ahora [`T8`](#t8--el-resultado-esperado-no-sale-del-código-que-se-está-probando). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Se fue la explicación de qué es triangular** —el origen topográfico del nombre—: es el porqué, no la exigencia, y por eso el cuerpo no cabía en el molde.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T8 · El resultado esperado no sale del código que se está probando

El valor que la prueba espera se confirma desde **fuentes independientes que coinciden** —la especificación, un cálculo hecho aparte—, **nunca leyendo lo que el código produce hoy**. Dos fuentes; tres si hay dinero, seguridad o consecuencias legales (extiende [`08·T7`](#t7--los-casos-se-derivan-con-método-no-se-eligen-a-ojo)).
```
INCORRECTO: se corre la función, sale 1 240, y se escribe que el esperado es 1 240
CORRECTO:   se calcula aparte a partir de la especificación, da 1 260, y se
            descubre que el código estaba mal
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.26.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`T7`](#t7--los-casos-se-derivan-con-método-no-se-eligen-a-ojo).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia, y es la más importante de las dos.** `T7` da **cobertura**; esta da **verdad**. Una prueba con casos perfectamente derivados y el esperado copiado de la salida actual **solo comprueba que el código hace lo que hace** — pasa siempre, no falla nunca, y figura como cubierta.

**Es la misma forma de defecto que apareció cinco veces en este repositorio**: una comprobación que pasa sin comprobar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

