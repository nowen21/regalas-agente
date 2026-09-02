# Estado de fase — Fase `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que quien la retome no tenga que reconstruirlo leyendo el chat.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | El pendiente [48](../../../../../pendientes/48-inventario-hu.md) y el hallazgo `H-27` · [EP-004](../../epica.md) · [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano.md) |
| **Última actualización** | 2026-08-26 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 12, el commit `ce2246b`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 Commit `ce2246b` | ✅ `ce2246b` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

**La estación 5 pasó sin documento aparte, y la regla que lo permite ya existe.** [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) dice que la redacción del CA es la especificación funcional.

> **Acá se citó la `EP-001 · HU-010` como si estuviera abierta esperando escribir esa regla, y se corrigió el 2026-08-26.** Está cerrada desde el 2026-08-18, y cerró diciendo que no hacía falta regla nueva. Se afirmó sin leer su estado.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple**, en el ciclo 2 |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` y `DEF-02` corregidos y verificados |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) · 373 pruebas, OK |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-11 | Hecha | Las once |

**Hechas:** 11 de 11. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Que la salida no sea generar la tabla sino no tenerla dos veces, porque el programa reporta y no corrige | En el cierre §5 |
| Que el pendiente no cuadraba ni consigo mismo: 78 en el encabezado contra 74 filas, y 4 de ellas dando por completa una historia que no lo estaba | En el cierre §2.3 |
| Que una comprobación puede estar bien escrita y no estar conectada, y sus pruebas no lo notan | `S-043` |
| Que un guion de sabotaje dijo «suite en verde» sin correr una sola prueba | `S-044` |

---

## 3. Pendiente / preguntas abiertas

- **Nada esperando.** Construida, probada, documentada y guardada en `ce2246b`.
- **Una decisión para el usuario, que quedó fuera del alcance a propósito:** la plantilla [`inventario-hu.md`](../../../../../plantillas/inventario-hu.md) sigue describiendo la tabla que acá se quitó, así que un proyecto que herede el estándar arma su inventario a mano con el mismo defecto. No se tocó porque el plan no la declara (`02·F8`) y cambiar `plantillas/` sube `VERSION` (`20·M10`).
- La duda del plan §2.7 **quedó resuelta**: ninguna de las 74 filas guardaba trabajo que no estuviera en el árbol. Está en el cierre §2.3.

---

## 4. Si se bloqueó

No se bloqueó en ningún momento.
