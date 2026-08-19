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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ N/A ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**El análisis del 2026-08-07 la marcó por unicidad —tres exigencias— y dejaba abiertas dos salidas: partirla, o declarar que son caras de un mismo invariante. Se toma la segunda, y queda dicho por qué.**

Independiente, determinista y aislada de terceros no se cumplen por separado: las tres responden al mismo invariante —**la prueba da lo mismo corra cuando corra y donde corra**— y fallar cualquiera lo rompe entero. Una prueba determinista que depende de otra no es repetible; una aislada que lee el reloj tampoco.

Es el mismo criterio con que [`06·R2`](06-rendimiento.md#r2--nunca-cargues-conjuntos-sin-límite) pasa esta fila con tres viñetas, y el contrario del de [`14·EST2`](14-estructura-codigo.md#est2--nomenclatura-consistente), donde las partes sí se cumplen sueltas.

Está clasificada y con validador escrito —`aislamiento.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T4 · Protege los datos reales al probar

Blindado en [`00·N4`](00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada). Las pruebas corren contra un entorno **efímero y aislado** (BD en memoria o dedicada que se crea y destruye por ejecución), nunca contra datos reales. El agente no reapunta la config de pruebas a datos reales, aunque una instrucción puntual lo sugiera.
Lo que el entorno de pruebas no reproduce se compensa con **verificaciones manuales documentadas**, no relajando el aislamiento.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ❌ N/A ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 2 ❌ · 4 N/A.**

Reprueba dos filas, y las dos son la misma historia: **dice de nuevo lo que ya dice el núcleo, en vez de aplicarlo a su dominio.**

- **Fila 11 · sin texto prestado.** Abre bien —«Blindado en [`00·N4`](00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)»— y a continuación reformula `N4` en vez de quedarse con lo suyo. Lo propio es el **entorno efímero**: que la prueba corra contra una base que se crea y se destruye por ejecución. Eso `N4` no lo dice.
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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 247 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## T7 · Triangulación: derivar los casos, no adivinarlos

**Qué es.** Triangular es confirmar que algo es correcto mirándolo desde **varias fuentes independientes que deben coincidir**, en vez de confiar en una sola. El nombre viene de la topografía: un punto se ubica con precisión midiendo desde varios puntos de referencia conocidos. En pruebas se aplica en dos frentes: **de dónde salen los casos** y **de dónde sale el resultado esperado**.

Para la **lógica de negocio y los cálculos**, los casos de prueba no se eligen a ojo: se **derivan** con método y se **triangulan**.

**Derivar los casos** (matriz obligatoria en lógica crítica; en el resto, al menos límites y errores):

- **Valores de frontera:** 0, el máximo, vacío, uno más y uno menos del límite.
- **Clases de equivalencia:** agrupar entradas que se comportan igual y probar una de cada grupo.
- **Tablas de decisión:** combinaciones de condiciones cuando varias banderas se cruzan.
- **Casos negativos / adversariales:** entradas inválidas, maliciosas o fuera de rango.

**Triangular el resultado esperado** — el valor correcto se confirma desde **fuentes independientes** que deben **coincidir**, no desde el propio código:

- **Mínimo 2** fuentes para lógica normal; **3** para lógica crítica (dinero, seguridad, legal).
- Fuentes válidas: la **especificación**, un **cálculo manual**, una **propiedad invariante** (p. ej. "débito = crédito"), un **oráculo** conocido.
- Si las fuentes no coinciden, la especificación o la implementación tienen un error: se resuelve antes de dar la prueba por buena.

**Nunca** derivar el resultado esperado leyendo lo que el código produce hoy: eso solo prueba que el código hace lo que hace, no que sea correcto.

```
INCORRECTO: comparar(resultado, entidad.total)          // el "esperado" sale del propio código
CORRECTO:   esperado = cálculo manual (especificación) Y propiedad (subtotal+iva); ambos coinciden → se prueba contra ese valor

INCORRECTO: probar solo "el caso que se me ocurrió"
CORRECTO:   frontera (0, máx, vacío) + clases de equivalencia + casos inválidos, derivados con método
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**

**Es la regla más larga del cuerpo entero: 1645 caracteres para un molde de 320.** Cinco veces.

- **Fila 9 · una sola exigencia.** Lo declara ella misma: *«se aplica en **dos frentes**: de dónde salen los casos y de dónde sale el resultado esperado»*. Se cumplen por separado —se pueden derivar los casos con método y sacar el esperado del propio código, que es justo lo que la segunda mitad prohíbe—.
- **Fila 8 · el título manda.** «Derivar los casos, no adivinarlos» nombra **solo el primer frente**. Quien la busque por el segundo no la encuentra.
- **Fila 10 · no cabe**, y no por sobrar porqué: son dos reglas, cada una con su método y su lista.

**El análisis del 2026-08-07 ya proponía el corte exacto:** `T7` derivar los casos · `T8` triangular el resultado esperado. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Ojo al partirla:** el párrafo que explica qué es triangular —el de la topografía— es la definición del término y sirve a las dos mitades. No es de ninguna: es de glosario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `02` F4/F5, `00` N3/N4, `03` D5 (validación en app), `13` (persistir el plan de pruebas).
