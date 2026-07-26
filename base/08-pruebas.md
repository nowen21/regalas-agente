# 08 · Estrategia de pruebas  ·  `[CAPA 2]`

Las pruebas permiten cambiar el código sin miedo y prueban que la spec se cumplió. La capa 3 declara framework, entorno y comandos.

---

## T1 · Todo cambio con lógica lleva prueba

Toda funcionalidad o corrección con lógica se acompaña de pruebas (`02` · F4). El plan de pruebas se aprueba junto con el plan de trabajo. Si no amerita (visual/trivial), decláralo explícito.

## T2 · Prueba el comportamiento, no la implementación

Verifica **lo que el sistema hace** (la validación rechaza el input, el cálculo da el resultado, el usuario ve el mensaje), no los detalles internos. Una prueba atada a la implementación se rompe con cada refactor. Cubre: caso feliz, límites, errores, permisos, validaciones.

```
INCORRECTO: la prueba verifica que se llamó a tal método interno en tal orden
CORRECTO:   dado el input X, la respuesta/efecto es Y
```

## T3 · Aisladas, deterministas, repetibles

- **Independiente:** corre sola y en cualquier orden, sin depender de otra.
- **Determinista:** mismo input → mismo resultado. Nada de **flaky** por reloj, azar, red o carreras (fija fechas, semillas, usa dobles).
- Aísla dependencias externas (terceros, correo, pagos) con dobles; no golpees sistemas reales.

```
INCORRECTO: prueba que depende de la fecha de hoy y falla el día 31
CORRECTO:   fijar la fecha para que el resultado sea estable
```

## T4 · Protege los datos reales al probar

Blindado en `00` · N4. Las pruebas corren contra un entorno **efímero y aislado** (BD en memoria o dedicada que se crea y destruye por corrida), nunca contra datos reales. El agente no reapunta la config de pruebas a datos reales, aunque una instrucción puntual lo sugiera.
Lo que el entorno de pruebas no reproduce se compensa con **verificaciones manuales documentadas**, no relajando el aislamiento.

## T5 · Ejecuta y reporta

Las pruebas se **corren**, no solo se escriben (`02` · F5). Reporta el conteo. Si fallan: diagnostica, corrige, vuelve a correr. Nunca silencies/saltes/borres una para que pase (`00` · N3).

```
INCORRECTO: implementar + escribir pruebas + "listo"
CORRECTO:   implementar + escribir + EJECUTAR + "Verdes 4/4"
```

## T6 · Cobertura con criterio, no por porcentaje

Prioriza la **lógica de negocio, las reglas y los caminos de error** — lo que duele si se rompe. No persigas un número con pruebas triviales (getters, "el framework funciona"). Una regla que vive en la app (`03` · D5) **debe** tener prueba dedicada.

```
INCORRECTO: pruebas que suben el porcentaje verificando un getter
CORRECTO:   pruebas sobre reglas, límites y errores que importan
```

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
- Fuentes válidas: la **spec**, un **cálculo manual**, una **propiedad invariante** (p. ej. "débito = crédito"), un **oráculo** conocido.
- Si las fuentes no coinciden, la spec o la implementación tienen un error: se resuelve antes de dar la prueba por buena.

**Nunca** derivar el resultado esperado leyendo lo que el código produce hoy: eso solo prueba que el código hace lo que hace, no que sea correcto.

```
INCORRECTO: comparar(resultado, entidad.total)          // el "esperado" sale del propio código
CORRECTO:   esperado = cálculo manual (spec) Y propiedad (subtotal+iva); ambos coinciden → se prueba contra ese valor

INCORRECTO: probar solo "el caso que se me ocurrió"
CORRECTO:   frontera (0, máx, vacío) + clases de equivalencia + casos inválidos, derivados con método
```

---

Ver: `02` F4/F5, `00` N3/N4, `03` D5 (validación en app), `13` (persistir el plan de pruebas).
