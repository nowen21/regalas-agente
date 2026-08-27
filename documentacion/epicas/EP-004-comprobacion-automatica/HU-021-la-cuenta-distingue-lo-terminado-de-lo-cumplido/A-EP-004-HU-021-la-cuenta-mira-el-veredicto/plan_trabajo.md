# Plan de Trabajo — Fase `A-EP-004-HU-021-la-cuenta-mira-el-veredicto` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-021-la-cuenta-mira-el-veredicto` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- ✨ **Funcionalidad nueva:** el conteo mira el veredicto, que hoy no mira.
- 📝 **Corrige dos moldes que se contradicen** sobre el vocabulario del veredicto, y uno que prohíbe lo que en la práctica se hace con razón.

**CA de la HU que cubre esta fase:** los cinco.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que «cuánto falta» deje de contar como hecha una fase que no cumplió, y que el molde del cierre tenga dónde decirlo.

**Fuera de alcance:**

- **Arreglar las 19 fases que no cumplen.** Esta fase las hace visibles.
- **Rellenar el veredicto de los 25 resultados que no lo traen.** Se cuentan aparte.
- **Los veredictos de épicas o planes.** Solo fases.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Medido el 2026-08-27, corriendo los comandos y leyendo los moldes línea por línea.

### 2.0 Lo que dicen hoy los dos moldes

| Molde | Línea | Vocabulario que ofrece |
|---|---|---|
| `09-resultado-pruebas.md` | 165-167 | `Cumple / No cumple`, **«no hay estado intermedio»** |
| `11-funcionalidad-implementada.md` | 74 | `Cumple / Cumple con observaciones` |

**El molde del cierre no tiene forma de decir «No cumple».** Por eso las 19 fases que no cumplen lo escriben en prosa, antes de la identificación, cada una a su manera.

**Y el molde del resultado dice «la fase no cierra con un CA en No»**, mientras 19 cerradas lo hacen con precedente. La práctica es la correcta: **cerrar no es aprobar.**

### 2.1 Lo que dice el árbol

| Qué | Valor verificado | Cómo se obtuvo |
|---|---|---|
| La línea de hoy | `116 en total · 84 completas · 32 incompletas` | `validar.py fases` |
| Cierres que dicen «No cumple» | **19** | Buscando el veredicto en los cierres |
| `resultado_pruebas.md` con veredicto legible | **103 de 128** | Recorriendo el árbol |
| `funcionalidad_implementada.md` con veredicto legible | 55 de 125 | El mismo recorrido |
| Pruebas que dependen de que `inventario` devuelva tres valores | **10** | `grep` sobre `pruebas.py` |

**El dato vive donde debe:** en el resultado, que es quien lo produce. En el cierre está en menos de la mitad **porque ahí no cabe**.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/fases.py` | Modificar | Servicio | Una función nueva que lee el veredicto y cuenta; `linea_inventario` la usa |
| `validadores/pruebas.py` | Modificar | Test | Los casos de las tres cuentas y los bordes |
| `plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md` | Modificar | Documentación | El campo del veredicto, con el vocabulario del otro molde |
| `plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md` | Modificar | Documentación | Quitar la frase que prohíbe cerrar con un rojo |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Documentación | La misma frase, que también está ahí |
| `CHANGELOG.md` · `VERSION` | Modificar | Documentación | `20·M10` |

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `validadores/fases.py` | **`inventario` conserva su firma de tres valores.** La cuenta nueva va en una función aparte | `validadores/pruebas.py`, con **10 pruebas** que esperan tres valores | **No rompen**, y por eso se hace así |
| `linea_inventario` | Devuelve una línea más larga | Una prueba que compara su texto | Se ajusta esa prueba, que es de forma y no de conducta |

**Cambiarle la firma a `inventario` habría roto diez pruebas para no ganar nada.** La cuenta nueva es otra pregunta, y va en otra función.

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

`python validadores/validar.py fases`, el de siempre. La línea del final dice más.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El veredicto se lee del **resultado**, no del cierre | Del cierre | Está en 103 de 128 contra 55 de 125, y es el documento que lo produce |
| La cuenta nueva va en una **función aparte** | Cambiarle la firma a `inventario` | Diez pruebas dependen de los tres valores, y son otra pregunta |
| Lo que no se puede leer se cuenta **en una tercera cuenta** | Repartirlo entre las otras dos | `S-038`. Repartirlo haría que el número mintiera de una forma nueva |
| Una historia **con varias fases** cumple solo si **todas** cumplen | Que baste una | Es la misma regla que ya usa `inventario` para «completa», y por el mismo motivo |
| **El molde de resultados manda** sobre el del cierre en el vocabulario | Al revés, o inventar un tercero | Es quien produce el veredicto, y su vocabulario ya dice «no hay estado intermedio» |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién | Estado |
|---|---|---|---|
| — | Ninguna | — | — |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-04 — Los moldes primero

Van primero porque **el vocabulario que fijen es contra el que va a leer el programa**. Al revés, el programa quedaría leyendo lo que hoy hay, y volverían las dos copias.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Que el molde del cierre tenga campo de veredicto, con `Cumple / No cumple` | Documentación | 1 h | — | EV-01 |
| T-02 | Quitar de los tres moldes la frase que prohíbe cerrar con un rojo, y decir que cierra **declarándolo** | Documentación | 1 h | T-01 | EV-01 |

### CA-01, CA-02 y CA-03 — La cuenta

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Leer el veredicto de una fase desde su resultado | Backend | 2 h | T-01 | EV-02 |
| T-04 | Contar terminadas, cumplidas y sin veredicto legible | Backend | 2 h | T-03 | EV-02 |
| T-05 | Que `linea_inventario` diga las tres, y se entienda sin documentación | Backend | 1 h | T-04 | EV-03 |
| T-06 | Casos de las tres cuentas | Test | 2 h | T-04 | EV-02 |
| T-07 | Bordes: sin fases, sin resultado, veredicto en otra forma | Test | 1,5 h | T-04 | EV-04 |
| T-08 | Una prueba que lo busque **por la corrida**, no llamando a la función | Test | 0,5 h | T-05 | EV-03 |
| T-09 | Que las 10 pruebas de `inventario` sigan pasando sin tocarlas | Test | 0,5 h | T-04 | EV-05 |

### CA-05 — Versionar

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-10 | Medir el número **antes y después**, para que la entrada diga la verdad | Documentación | 0,5 h | T-05 | EV-06 |
| T-11 | `VERSION` y la entrada, **avisando del cambio de significado** | Documentación | 1 h | T-10 | EV-06 |
| T-12 | Correr `validar.py versionado` | Documentación | 0,5 h | T-11 | EV-06 |

### Calidad

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-13 | Sabotear cada pieza | Calidad | 2 h | EV-07 |

**Total estimado:** 17,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-04 → T-05 → T-10 → T-11

**T-01 va antes que T-03 a propósito.** El programa lee contra el vocabulario que el molde fije. Si se escribiera primero, quedaría leyendo lo que hoy hay — y el vocabulario volvería a vivir en dos sitios, que es lo que la `HU-012` vino a cerrar.

**T-10 se mide antes de escribir la entrada.** El número va a bajar, y **cuánto** no se sabe hasta correrlo. Escribir la entrada antes sería inventarlo.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | La línea, leída y con sus números sumados | EV-03 | | ☐ |
| CA-02 | Árbol con dos fases, una que cumple y otra que no | EV-02 | | ☐ |
| CA-03 | Árbol con una fase sin veredicto | EV-04 | | ☐ |
| CA-04 | Lectura de los tres moldes | EV-01 | | ☐ |
| CA-05 | `VERSION`, la entrada y el validador | EV-06 | | ☐ |
| Transversal | Las 10 pruebas de `inventario`, sin tocarlas | EV-05 | | ☐ |

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

Se revierte descartando el commit. **Con la salvedad de siempre:** si la versión ya se publicó, bajarla no deshace que alguien la haya visto.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar verá su número de historias completas bajar.** No porque haya perdido trabajo, sino porque **antes contaba como hechas fases que no cumplieron**. La entrada del `CHANGELOG` lo dice con todas las letras, y es lo que exige `CA-05`.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — todo lo que este plan afirma se midió; los valores están en §2.
- `04·R4` — lo que no se puede leer se cuenta aparte, no se reparte.
- `08·T4` — las pruebas no tocan documentos reales.
- `13·DOC5` — lo decidido se registra como señal.
- `20·M10` — versionar.
- `EP-004 §10.2` y `DA-06` — el programa reporta y no corrige.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el número baje mucho y se lea como retroceso | Desánimo, o desconfianza del conteo | T-10 lo mide y T-11 lo explica **antes** de que se vea. No es retroceso: es la primera medición honesta | Abierto |
| B-02 | Que las 25 sin veredicto se repartan entre las otras dos | El número mentiría de una forma nueva | `CA-03` y su caso propio | Abierto |
| B-03 | Que el programa lea el vocabulario de una lista escrita en el código | Volverían las dos copias | T-01 va primero, y hay un caso que lo fija | Abierto |
| B-04 | Que cambiar `linea_inventario` rompa la prueba que compara su texto | Un rojo que no es defecto | Se ajusta esa prueba, y se declara: es de forma, no de conducta | Abierto |

---

## 11. Definition of Done

- [ ] Los cinco CA verificados con evidencia
- [ ] Pruebas en verde, y **la suite completa al final, con conteo distinto de cero** (`02·F5`)
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
