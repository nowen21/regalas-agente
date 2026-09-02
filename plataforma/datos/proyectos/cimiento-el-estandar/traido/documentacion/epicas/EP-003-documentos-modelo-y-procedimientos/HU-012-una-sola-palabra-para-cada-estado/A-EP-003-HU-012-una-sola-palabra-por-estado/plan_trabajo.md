# Plan de Trabajo — Fase `A-EP-003-HU-012-una-sola-palabra-por-estado` (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-012-una-sola-palabra-por-estado` |
| **Épica** | [EP-003](../../epica.md) |
| **HU** | [HU-012](../HU-012-una-sola-palabra-para-cada-estado.md) — **una sola** (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | No hay documento aparte. [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) dice que **la redacción del CA es la especificación funcional**, y la historia trae alcance, reglas, criterios con pasos y requisitos no funcionales |
| **Fecha apertura** | 2026-08-26 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- ✨ **Funcionalidad nueva:** el glosario gana los estados, que hoy no define, y aparece una comprobación que hoy no existe.
- 📝 **Corrige cuatro moldes que se contradicen entre sí**, y de paso uno que se contradice con otro sobre el mismo concepto.

**CA de la HU que cubre esta fase:**

| CA de `HU-012` | Estado |
|---|---|
| CA-01 — el glosario define los estados, una vez | ☐ |
| CA-02 — los documentos usan el vocabulario | ☐ |
| CA-03 — escribir un estado inventado se avisa | ☐ |
| CA-04 — la versión sube, porque cambiaron los moldes | ☐ |

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que «terminado» se escriba de una sola forma, definido en un solo sitio, y que un programa pueda comprobarlo.

**Fuera de alcance:**

- **Cambiar qué significa cada estado.** Se unifica cómo se escribe.
- **Los estados de documentos que no sean épica, historia o tarea.**
- **La regla de no citar como abierto lo cerrado**, que depende de esta.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Leído línea por línea el 2026-08-26, corriendo los comandos.

### 2.0 Lo que dice hoy cada molde

| Molde | Línea | Qué estado define | Vocabulario |
|---|---|---|---|
| `03-epica.md` | 21 | El de una **épica** | Propuesta / Aprobada / En curso / Completada / Cancelada |
| `01-planteamiento.md` | 93 | El de una **épica**, otra vez | Propuesta / Aprobada / En curso / Completada |
| `04-HU.md` | 20 | El de una **historia** | Backlog / Ready / En curso / En QA / Done |
| `10-estado-fase.md` | 60 | El de una **tarea** | Pendiente / En curso / Hecha / Bloqueada |

**Dos problemas distintos, y conviene no confundirlos.** Que los tres conjuntos difieran es correcto. Lo que no: que «terminado» sea `Completada`, `Done` y `Hecha`; y que **la lista de la épica esté escrita dos veces sin coincidir** — `01-planteamiento` no trae `Cancelada`.

### 2.1 Lo que dice el árbol

| Qué | Valor verificado | Cómo se obtuvo |
|---|---|---|
| Historias con campo `Estado` | **115 de 115**, ninguna sin él | Recorriendo `documentacion/epicas` |
| Dentro del vocabulario que se acordó | **4** | Las que ya dicen `Terminada` |
| Fuera | **111** | El mismo recorrido |
| Entradas del glosario | 95, **ninguna de estados** | `base/glosario.md` |
| Validadores que hoy leen el campo | **Ninguno** | `grep` sobre `validadores/*.py` |

**Las 111, y a qué palabra van:**

| Dice hoy | Pasa a | Cuántas |
|---|---|---|
| `Backlog` | `Pendiente` | 54 |
| `En implementación` | `En curso` | 19 |
| `Cumplida` | `Terminada` | 11 |
| `Done` | `Terminada` | 8 |
| `Cerrada` | `Terminada` | 6 |
| `Hecha` | `Terminada` | 5 |
| `Aprobada` | `Lista` | 2 |
| `Escrita` | `Pendiente` | 2 |
| `**Cumplida.**`, en negrita | `Terminada` | 2 |
| `Ready` | `Lista` | 1 |
| `En curso` | no cambia | 1 |
| `Terminada` | **no cambia** | 4 |

**Las dos en negrita son de hoy, y las escribí yo** en las fases de la `HU-019` y la `HU-020`. Se anotan aparte porque el texto trae marcado y no basta comparar el principio de la línea.

**Ninguna queda sin mapa.** Dos son juicio y no mecánica, y quedan declarados acá para que se puedan discutir sin leer el código: `Aprobada` a `Lista` (aprobada para construir) y `Escrita` a `Pendiente` (existe, no empezó).

**Que el número pasara de 51 a 111 es el costo de traducir**, y estaba dicho antes de empezar: `Backlog` solo son 54.

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `base/glosario.md` | Gana filas. No pierde ninguna | Ningún programa lo lee | — |
| Los cuatro moldes | Dejan de listar y citan | Ningún programa los lee | — |
| Las 115 historias | Cambia el valor del campo `Estado` | **Ningún validador lee ese campo hoy** | — |
| `validadores/fases.py` | Gana una función. Las demás conservan su firma | `validadores/pruebas.py` | Las pruebas de `InventarioDeHU` tienen que seguir pasando |

**Que ningún validador lea hoy el campo es justamente el problema**, y por eso normalizar no rompe nada: no hay nada apoyado en él.

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

`python validadores/validar.py fases`, el de siempre. El aviso nuevo sale en su reporte.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El glosario es el único sitio donde se definen | Que cada molde mantenga la suya, acordadas | Es lo que ya se intentó sin querer, y produjo cuatro listas y una contradicción. El propósito escrito del glosario es exactamente este |
| Los tres conjuntos siguen siendo distintos | Un único conjunto para épica, historia y tarea | Una épica se cancela y una tarea se bloquea. Forzar un solo conjunto obligaría a estados que no aplican |
| Se normaliza **la palabra**, no la frase | Reemplazar el campo entero | Varias traen texto útil después: «Cumplida — los tres CA verificados el...». Eso se conserva |
| Se avisa, no se falla | Falla | Un estado mal escrito no rompe nada, y detener el commit por eso es como se desactivan los enganches |
| La comprobación vive en `fases.py` | Un validador nuevo | Ya recorre las historias. `EP-004 §10.2`: un insumo, un resultado |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si `Aprobada` significa «lista para construir» o algo distinto en las 2 que lo usan | Se resuelve leyendo esas dos, en T-04 | Pendiente, bloquea a T-05 |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El glosario define, los moldes citan

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir en el glosario los tres conjuntos **en español**, con qué significa cada estado | Documentación | 2 h | — | EV-01 |
| T-02 | Unificar la palabra de «terminado» entre los tres | Documentación | 0.5 h | T-01 | EV-01 |
| T-03 | Que los cuatro moldes citen el glosario en vez de listar | Documentación | 1.5 h | T-02 | EV-01 |

### CA-02 — Los documentos usan el vocabulario

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Guardar el estado que declara hoy cada una de las 115 | Documentación | 0.5 h | — | EV-02 |
| T-05 | Normalizar las **111 de 115**, conservando el texto que sigue a la palabra | Documentación | 3 h | T-04, T-02 | EV-02 |
| T-06 | Comparar par por par contra lo guardado | Documentación | 1 h | T-05 | EV-02 |
| T-07 | Contar las completas antes y después: **tiene que dar igual** | Documentación | 0.5 h | T-05 | EV-03 |

### CA-03 — El estado inventado se avisa

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-08 | Comprobar que el estado esté en el vocabulario de su clase | Backend | 2 h | T-01 | EV-04 |
| T-09 | Que el aviso diga cuál escribió y cuáles valen | Backend | 0.5 h | T-08 | EV-04 |
| T-10 | Casos: válido, inventado, sin campo, con texto detrás | Test | 2 h | T-08 | EV-04 |
| T-11 | Una prueba que lo busque **a través de `validar`**, no llamando a la función | Test | 0.5 h | T-08 | EV-05 |

### CA-04 — Versionar

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-12 | Subir `VERSION` y escribir la entrada del `CHANGELOG` | Documentación | 1 h | T-05 | EV-06 |
| T-13 | Correr `validar.py versionado` | Documentación | 0.5 h | T-12 | EV-06 |

### RNF y calidad

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-14 | Sabotear cada pieza y comprobar que las pruebas cazan | Calidad | 2 h | EV-07 |

**Total estimado:** 17 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05 → T-06 → T-12

**T-04 va antes que todo lo que toque documentos.** Es la foto contra la que se compara, y sin ella `CA-02` no se puede comprobar: no habría con qué contrastar.

**T-08 depende de T-01**, no al revés: el programa comprueba contra lo que el glosario diga, no contra una lista escrita en el código. Si se hiciera al revés, el vocabulario volvería a vivir en dos sitios — que es el problema que esta fase viene a arreglar.

**T-11 existe porque en la fase anterior faltó.** Un sabotaje mostró que descolgar una comprobación de `validar` dejaba todas sus pruebas en verde (`S-043`).

> Solo se tocan los archivos declarados (`02·F8`). Descubrir uno nuevo: PAUSAR, reportar, ampliar el plan con aprobación.

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Lectura del glosario y de los cuatro moldes | EV-01 | | ☐ |
| CA-02 | Comparación par por par, y el conteo antes/después | EV-02, EV-03 | | ☐ |
| CA-03 | Pruebas del vocabulario y de los bordes | EV-04, EV-05 | | ☐ |
| CA-04 | `VERSION`, `CHANGELOG` y el validador | EV-06 | | ☐ |

**Registro de evidencias:** EV-01 a EV-07, en el `resultado_pruebas.md` de esta fase.

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La máquina de quien trabaja, con la biblioteca estándar |
| Usuarios de prueba | No aplica. **Ninguna prueba usa credenciales** (`00·N6`) |
| Datos precargados | Árboles de mentira en carpeta temporal |

**Ningún documento real se edita para probar** (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. **Con la misma salvedad de la fase anterior:** si la versión ya se publicó, bajarla no deshace que un proyecto la haya visto; la reversión sería una versión nueva que restituye.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Un proyecto que ya tenga el estándar** verá los moldes citando el glosario, y un aviso si alguno de sus documentos usa un estado fuera del vocabulario. **Sus documentos no se tocan ni se migran**: el aviso informa. Eso queda escrito en la entrada del `CHANGELOG`.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — todo lo que este plan afirma se verificó leyendo o corriendo; los valores están en §2.
- `04·R4` — no se afirma sobre lo que no se leyó: por eso T-04 guarda la foto **antes** de que T-05 toque nada.
- `08·T4` — las pruebas no tocan documentos reales.
- `13·DOC5` — lo decidido se registra como señal.
- `20·M10` — versionar es la condición para que el cambio de `base/` y `plantillas/` exista.
- `EP-004 §10.2` y `DA-06` — el programa reporta y no corrige.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que normalizar cambie el sentido de un estado sin que nadie lo note | Un documento diría algo falso | T-06 compara par por par y T-07 cuenta las completas antes y después. **Si el número se mueve, algo cambió de sentido** | Abierto |
| B-02 | Que se pierda el texto que sigue a la palabra | Se perdería la fecha o el detalle del cierre | Se normaliza la palabra, no la frase. Es un caso de prueba propio | Abierto |
| B-03 | Que tocar historias de fases cerradas se lea como reabrirlas | Confusión sobre qué está sellado | No se reabren: el campo es un índice. Queda dicho en el cierre y en el `CHANGELOG` | Abierto |
| B-04 | Que el vocabulario quede escrito en el código y no en el glosario | Volverían las dos copias | T-08 depende de T-01 a propósito, y hay un caso de prueba que lo fija | Abierto |

---

## 11. Definition of Done

- [ ] Los cuatro CA verificados con evidencia
- [ ] Pruebas de la fase en verde, y **la suite completa al final, con conteo distinto de cero** (`02·F5`)
- [ ] Trazabilidad sin faltantes (`13·DOC11`)
- [ ] `VERSION` y `CHANGELOG` al día (`20·M10`)
- [ ] Señales registradas (`13·DOC5`)
- [ ] Rama lista para el commit único (`09·G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
