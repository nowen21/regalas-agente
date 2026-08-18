# Plan de Pruebas — Fase B-EP-001-HU-009: el sello no se contradice

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-001-HU-009 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que cada comprobación reporte lo que debe **y calle lo que no** | Sellos de mentira armados en el caso |
| Sobre el cuerpo real | Que `base/` quede en cero | El repositorio |
| Regresión | Que ninguna regla cambie de texto ni de veredicto | Las dos suites |

**Lo que hay que probar acá no es que encuentre: es que no invente.** Una comprobación sobre 200 sellos que reporte de más se apaga a la semana, y apagada no encuentra nada. La mitad de los casos son de **silencio**.

### 3.2 Técnicas

- **Sellos armados por bloques**, para poder poner un ❌ en una fila exacta sin escribir la tabla entera a mano en cada caso.
- **El caso real como caso de prueba**: cada uno reproduce un sello que de verdad estaba mal, no uno inventado.
- **Una prueba contra `base/`**, que es la que envejece con el repositorio.

### 3.5 Alcance de la corrida

`validadores/tests/` entera, `validadores/pruebas.py` entera —se toca `metareglas.py`, que ya tiene sus casos—, `validar.py metareglas` y `validar.py estandar`.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| CA-01 · el texto y la tabla dicen lo mismo | [CP-001](#cp-001--el-texto-reprueba-una-fila-que-la-tabla-da-por-buena) | ☐ |
| CA-01 · el mensaje se entiende | [CP-002](#cp-002--varias-filas-se-nombran-en-plural) | ☐ |
| CA-01 · las formas de escribir la prosa | [CP-003](#cp-003--el-texto-agrupado-también-cuenta) | ☐ |
| Ruido · no se reporta al revés | [CP-004](#cp-004--la-tabla-puede-marcar-más-de-lo-que-el-texto-desglosa) | ☐ |
| Ruido · el CUMPLE que narra lo corregido | [CP-005](#cp-005--un-cumple-que-cuenta-lo-que-corrigió-no-se-reporta) | ☐ |
| CA-01 · el CUMPLE con ❌ en la tabla | [CP-006](#cp-006--un-cumple-con-una-cruz-en-la-tabla-sí-se-reporta) | ☐ |
| CA-01 · la línea de totales | [CP-007](#cp-007--los-totales-cuadran-con-su-tabla) | ☐ |
| Límites · la tabla incompleta | [CP-008](#cp-008--una-tabla-que-no-suma-veinte-se-dice-así) | ☐ |
| CA-01 · un solo sello por regla | [CP-009](#cp-009--dos-bloques-apilados-se-reportan) | ☐ |
| CA-01 · el cuerpo real en cero | [CP-010](#cp-010--ningún-sello-del-estándar-se-contradice) | ☐ |
| No regresión | [CP-011](#cp-011--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 11 de 11 exigencias con caso = 100%.

---

## 6. Casos de prueba

### CP-001 — El texto reprueba una fila que la tabla da por buena

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un sello con `**Fila 5 ·**` en el texto y ✅ en la casilla 5 | Se reporta, y el mensaje nombra la fila 5 |
| 2 | El mismo con ❌ en la casilla 5 | No se reporta |

> Es el caso de `C15`, `C16` y `C10` — los tres del capítulo `01`, y en los tres **la fila que se perdió fue la 5**: la que dice que la base no nombra tecnología.

---

### CP-002 — Varias filas se nombran en plural

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un sello con dos filas sueltas en el texto | El mensaje dice «las filas 5 y 10» |

> Es el de `C10`. Un mensaje que diga «la fila 5, 10» se lee como un número raro y no como dos filas, y quien lo lee va a buscar la fila 510.

---

### CP-003 — El texto agrupado también cuenta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `**Filas 8, 9 y 10 ·** son tres reglas en una` | Se reporta |

> Es la forma que usa la mitad de los sellos del cuerpo. Leer solo `**Fila N**` dejaría fuera justo a los peores, que son los que reprueban varias.

---

### CP-004 — La tabla puede marcar más de lo que el texto desglosa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tabla con tres ❌ y un texto que dice «son tres reglas en una» sin numerarlas | **No se reporta** |

> **No se comprueba al revés, a propósito.** El texto agrupa y no tiene por qué desglosar cada fila que la tabla ya marcó. Exigirlo convertiría esto en ruido sobre sellos correctos, que es como se apaga una comprobación.

---

### CP-005 — Un CUMPLE que cuenta lo que corrigió no se reporta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sello en CUMPLE, tabla sin ❌, y el texto dice «**Fila 8 · el título manda.** Se corrigió» | **No se reporta** |

> **Es el falso positivo que salió en la primera corrida**, sobre [`17·I6`](../../../../../base/17-interfaz.md#i6--funciona-en-los-tamaños-de-pantalla-que-el-proyecto-soporta). Un sello en CUMPLE suele contar qué reprobaba **antes** de corregirlo; compararlo contra la tabla daría contradictorio justo lo contrario de lo que pasó.

---

### CP-006 — Un CUMPLE con una cruz en la tabla sí se reporta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sello en CUMPLE con un ❌ en la tabla | Se reporta, y el mensaje dice CUMPLE |

> El único borde del caso anterior. Un CUMPLE no puede tener ni un ❌: eso no es historia, es contradicción.

---

### CP-007 — Los totales cuadran con su tabla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tabla con 15 ✅ · 3 ❌ · 2 N/A y la línea dice `14 ✅ · 3 ❌ · 3 N/A` | Se reporta, con las dos cuentas |
| 2 | Los dos iguales | No se reporta |

> El paso 1 es exactamente lo que decía `C15`, y por el mismo lado que los otros nueve: **una N/A de más y un ✅ de menos**.

---

### CP-008 — Una tabla que no suma veinte se dice así

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una tabla con dos casillas | Se reporta que la tabla no tiene 20, **no** que el total esté mal |

> Corregir un total contra una tabla incompleta manda a arreglar lo que no es.

---

### CP-009 — Dos bloques apilados se reportan

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una regla con dos bloques de checklist | Se reporta, y dice cuántos |
| 2 | Con uno | No se reporta |

> Lo de `M14`: el sello de la `v2.1.0` encima del de la `v2.2.0`. Quien lee de arriba abajo se queda con el viejo — que además tenía la cuenta mal.

---

### CP-010 — Ningún sello del estándar se contradice

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las tres comprobaciones sobre las 200 reglas de `base/` | Cero |

> Es la que envejece con el repositorio, y la que se cae cuando alguien vuelva a escribir un sello a mano.

---

### CP-011 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa, con los casos nuevos |
| 2 | `validadores/pruebas.py` entera | Igual que antes |
| 3 | `validar.py estandar` | Sin incumplimientos |
| 4 | Contar las reglas en NO CUMPLE antes y después | **El mismo número** — se corrigen sellos, no reglas |

> El paso 4 es el que fija el alcance: si el conteo bajara, esta fase habría cambiado una norma sin decirlo.

---

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que corregir un sello cambie el veredicto de una regla | Inmediato |
| **Alta** | Falsos positivos sobre sellos correctos | Antes de cerrar |
| **Media** | La redacción del mensaje | Se reporta |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Sellos del estándar que se contradicen | **0** |
| Sellos correctos reportados por error | **0** |
| Reglas cuyo texto cambia en esta fase | **0** |
| Pruebas del repositorio que dejan de pasar | **0** |
| Cobertura de exigencias | 100% — 11 de 11 |

Un solo concepto: **Cumple** o **No cumple**.
