# Resultado de Pruebas — Fase `A-EP-004-HU-021-la-cuenta-mira-el-veredicto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-021-la-cuenta-mira-el-veredicto` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 2. El ciclo 1 dejó un sabotaje en verde que sí saboteaba |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cinco criterios quedaron comprobados sobre el árbol real y sobre árboles de prueba, y el número se midió antes de escribir nada sobre él.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 7 de 7 | 7 de 7 |
| Criterios en verde | 5 de 5 | 5 de 5 |
| Pruebas de `inventario` que hubo que tocar | 0 | **1**, y solo su texto — ver §4.3 |
| Historias sin veredicto repartidas entre las otras cuentas | 0 | **0** |
| Sabotajes cazados | Todos | 6 de 6, **en el ciclo 2** |
| Fallas en la suite completa | 0 | 0, sobre **417 pruebas** |

---

## 3. Resultado por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 | La línea dice las tres cuentas y cuadran | ✅ |
| CP-002 | Una fase que no cumple no cuenta cumplida | ✅ |
| CP-003 | Lo que no se puede leer se cuenta aparte | ✅ |
| CP-004 | Los moldes usan un solo vocabulario | ✅ |
| CP-005 | Los bordes | ✅ |
| CP-006 | Lo de antes no se rompió | ✅ |
| CP-007 | La versión sube y avisa del cambio de significado | ✅ |

### CP-001 — El número real, medido antes de escribir sobre él

| Antes | Ahora |
|---|---|
| `117 en total · 85 completas · 32 incompletas` | `117 en total · 32 sin terminar · 85 terminadas, de las cuales 51 cumplen, 11 no cumplen y 23 no dicen si cumplen` |

**Las tres cuentas suman las terminadas:** 51 + 11 + 23 = 85. Comprobado sobre el árbol real, que es el único con la variedad de redacciones de verdad.

**De 85 terminadas, 51 cumplen.** El número anterior estaba sobrestimado en un **40%** — más de lo que se había estimado al planearlo, que eran 23%.

### CP-002 y CP-003 — Las particiones

| Situación | Cuenta como |
|---|---|
| Dos fases, las dos cumplen | Cumple |
| Dos fases, una no cumple | **No cumple** |
| Dos fases, ninguna cumple | No cumple |
| Una fase sin veredicto legible | **No dice**, y **ni cumple ni no cumple** |
| Dos fases, una cumple y otra ilegible | **No dice** |

**El último es el que sostiene el criterio.** Si no se puede leer una fase, no se puede afirmar nada de la historia entera — y afirmarlo igual habría sido `04·R4` incumplido en el mismo programa que existe para comprobar.

### CP-004 — Un solo vocabulario

| Molde | Antes | Ahora |
|---|---|---|
| `09-resultado-pruebas` | `Cumple / No cumple` | Igual |
| `11-funcionalidad-implementada` | `Cumple / Cumple con observaciones` | **`Cumple / No cumple`, como campo** |
| Los tres | Decían «la fase no cierra con un CA en rojo» | Dicen que **cierra declarándolo** |

**El veredicto pasó de prosa a campo.** Eso es lo que hacía que 70 de 125 cierres no se pudieran leer: no que la gente no lo escribiera, sino que **no tenía dónde**.

### CP-005 — Los bordes

| Borde | Resultado |
|---|---|
| Historia a medias | No entra en ninguna de las tres cuentas |
| Fase sin `resultado_pruebas.md` | Cuenta como sin veredicto, y no revienta |
| Veredicto con texto detrás: `Cumple, en el ciclo 2` | Se lee como `Cumple` |
| Veredicto en otra caja: `no cumple` | **Se lee igual.** A diferencia del estado, acá la caja no cambia el sentido |
| Árbol vacío | Ceros, sin línea |

### CP-006 — Lo de antes no se rompió

`inventario` **sigue devolviendo tres valores**, y el total y las sin terminar dan lo mismo. La cuenta nueva vive en otra función, que era la decisión del plan §2.6.

### CP-007 — La versión

`35.1.0` → **`35.2.0`**, **MENOR**: nadie tiene que hacer nada. La entrada trae **los dos números**, y dice con todas las letras que **no se perdió trabajo: antes se contaba de más**.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Seis, restaurados **con copia**.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | Lo ilegible se reparte entre las que cumplen | Cazado (2) | Cazado (2) |
| 2 | Basta una que cumpla, en vez de todas | Cazado | Cazado |
| 3 | Cuenta también las historias a medias | Cazado (2) | Cazado (2) |
| 4 | El veredicto se lee del cierre, no del resultado | Cazado (5) | Cazado (5) |
| 5 | La línea vuelve a decir «completas» | Cazado (2) | Cazado (2) |
| 6 | El molde vuelve a ofrecer un tercer valor | **En verde** | Cazado |

### 4.2 El sabotaje que pasó en verde, y sí saboteaba

Devolverle al molde del cierre su tercer valor **dejaba las doce pruebas en verde**. El `CA-04` solo tenía comprobación a mano, y **un molde sin guardia vuelve a lo de antes en la primera edición**.

Se agregaron dos pruebas: que el campo del veredicto no ofrezca un tercer valor, y que ninguno de los tres moldes vuelva a prohibir cerrar con un rojo.

**Es el mismo hueco que la `HU-020` encontró con la plantilla del inventario**, y por segunda vez lo destapó un sabotaje y no una lectura.

### 4.3 La prueba de `inventario` que hubo que tocar

La meta era **cero** y fue **una**: `test_con_dos_hu_una_completa_y_otra_no_la_linea_dice_2_1_y_1`, que compara el **texto** de la línea y afirmaba «1 completas».

**Estaba previsto** — es el riesgo `B-04` del plan — y **es de forma, no de conducta**: lo que la prueba vigila, que la línea reporte las dos cuentas, sigue igual. Se ajustó el texto contra el que compara, con el porqué escrito al lado.

**Las otras nueve pasaron sin tocarse.**

### 4.4 La mejor prueba de que hacía falta, y no la escribió nadie

**La historia que se creó para arreglar esto contaba como terminada.** Sin una línea de trabajo hecha: el andamio le creó los cinco documentos vacíos, y el conteo viejo mira que estén.

Con la cuenta nueva **cae donde corresponde**: entre las 23 que no dicen si cumplen.

### 4.5 Rastros

Ninguno. Los seis sabotajes editan un archivo que se restaura con copia, y las pruebas escriben solo en carpeta temporal.

### 4.6 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Trazabilidad criterio a evidencia

| CA | Evidencia | Estado |
|---|---|---|
| CA-01 — la línea dice las dos cosas | CP-001, con las tres cuentas sumando | ✅ |
| CA-02 — una fase que no cumple no cuenta cumplida | CP-002 | ✅ |
| CA-03 — lo ilegible se cuenta aparte | CP-003 | ✅ |
| CA-04 — el molde puede decir «No cumple» | CP-004, y las dos pruebas del §4.2 | ✅ |
| CA-05 — la versión sube y avisa | CP-007 | ✅ |

---

## 6. Defectos encontrados

| ID | Qué era | Cómo se cazó | Estado |
|---|---|---|---|
| DEF-01 | El `CA-04` no tenía comprobación automática: el molde podía volver a su tercer valor sin que nada fallara | Sabotaje 6 | Corregido, con dos pruebas |

**Ninguno del código.** El único defecto fue de cobertura, y lo encontró un sabotaje.

---

## 7. Evidencias

- `veredicto_de` y `por_veredicto` en `validadores/fases.py`
- `LaCuentaMiraElVeredicto` en `validadores/pruebas.py`: **14 pruebas**
- Los tres moldes de `plantillas/ciclo-vida-proyectos/`
- La entrada `35.2.0` del `CHANGELOG`, con los dos números
