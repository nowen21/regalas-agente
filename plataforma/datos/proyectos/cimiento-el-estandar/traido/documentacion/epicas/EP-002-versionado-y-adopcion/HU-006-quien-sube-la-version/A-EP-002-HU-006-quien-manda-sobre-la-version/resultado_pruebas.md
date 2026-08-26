# Resultado de Pruebas — Fase A-EP-002-HU-006: quién manda sobre la versión

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| CA | Veredicto |
|---|---|
| **CA-01** · dos sesiones no dejan dos numeraciones | ✅ **Pasa** — simulado con dos copias |
| **CA-02** · nadie arrastra el trabajo de otro | ✅ **Pasa** — cada copia subió lo suyo |
| **Límites** · qué pasa si las dos suben la misma parte | ✅ **Definido** — la segunda lee lo guardado y sube desde ahí |
| No regresión | ✅ **Pasa** — `tests/` **241 · OK** · `pruebas.py` 357 · `metareglas` sin hallazgos de `M18` |

**19 casos automatizados** en [validadores/tests/test_una_sola_numeracion.py](../../../../../validadores/tests/test_una_sola_numeracion.py).

---

## 2. La simulación, con las dos copias y el mismo día

Dos copias del mismo repositorio, cada una cambiando **su** archivo, las dos subiendo versión el mismo día. Se corrió dos veces: eligiendo el número al editar y eligiéndolo al guardar.

| | El número se elige **al editar** | El número se elige **al guardar** |
|---|---|---|
| Lo que eligió la primera | `9.1.0`, guardado limpio | `9.1.0`, guardado limpio |
| Lo que eligió la segunda | `9.1.0` — **chocó** | `9.2.0`, guardado limpio |
| Cómo quedó el número | `9.1.0` | `9.2.0` |
| Entradas del registro | **una** | **dos** |
| El trabajo de cada una | llegó | llegó |

**La segunda columna es el criterio cumplido:** una sola numeración, sin huecos, sin repetidos, y las dos entradas puestas.

---

## 3. El hallazgo que no se buscaba: hay dos formas de romperse, no una

La primera columna terminó con **una sola entrada donde tenía que haber dos**. La de la segunda sesión se perdió al resolver el choque, y **eso incumple la `RN-04`** de la HU — *«el registro de cambios no pierde ninguna entrada por el cruce»*.

**Y `validar.py versionado` lo dio por limpio.** Con razón: no hay número repetido ni hueco. Lo que hay es una entrada que ya no está, y de eso no queda rastro.

Osea que el cruce se rompe de dos maneras según cómo lo resuelva quien lo encuentre:

| Cómo se resuelve el choque | Qué queda | ¿Se ve? |
|---|---|---|
| Se conserva una de las dos entradas | **falta una entrada** | ❌ no |
| Se conservan las dos con el mismo número | **número repetido** | ✅ sí |

**El repositorio real tiene la segunda:** dos entradas para la `15.4.0`, del 14 y del 15 de agosto. La primera no se puede contar — no se sabe cuántas entradas se perdieron así, porque perderse es justamente no dejar rastro.

**Lo que esto cambia:** `M18` no es una comodidad, es lo único que actúa **antes** del choque. La comprobación llega después y solo ve la mitad de los casos.

**Y es la razón de que la regla no se acotara a `VERSION`.** Si lo único que protege es releer antes de escribir, tiene que valer para todo lo que dos sesiones comparten — el registro, un índice, el número de un pendiente. En esos tres no hay número repetido que contar: solo queda la regla.

---

## 4. El número repetido que ya existe no se renumera

La `15.4.0` está usada dos veces. **Se deja, y se marca.**

Renumerar una versión que un proyecto pudo haber adoptado le movería el piso sin que se entere: quien adoptó «15.4.0» tiene **las dos cosas**, y el registro ahora lo dice en el título de la entrada. El validador la reporta como **aviso** en vez de falla, así que sigue a la vista y deja de detener. Está fijado en dos casos de prueba.

Es lo que [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) ya pedía: un cambio de norma no reabre lo cerrado.

---

## 5. El primer falso positivo, y por qué queda escrito

La comprobación nació diciendo que `VERSION` tiene que **avanzar** desde lo guardado. Contra el repositorio real reportó falla de inmediato: recién guardado, los dos números coinciden, y eso es lo normal.

**La falla es quedar por debajo, no quedar igual.** Corregido, y con su caso: `test_igual_a_lo_guardado_no_es_falla`.

---

## 6. Lo que queda abierto · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

- **Dos sesiones que guardan en el mismo minuto siguen pudiendo chocar.** `M18` reduce la ventana de horas a segundos; no la cierra. Cerrarla del todo pide bloqueo, y eso vale más de lo que cuesta el defecto.
- **La entrada perdida no se detecta.** Se acepta y queda escrito acá; contar entradas contra los guardados anteriores es trabajo aparte.
- **Elegir el número al guardar no se puede comprobar con un programa** — es un hábito. Declarado como parcial en [`reglas-validables.md`](../../../../../validadores/reglas-validables.md).

---

## 7. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2, más el transversal de límites |
| **Defectos abiertos aceptados** | tres, los de arriba |
| **Ciclos** | 1 — con una corrección de falso positivo dentro del ciclo |
