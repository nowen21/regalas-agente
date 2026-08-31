# Plan de Trabajo — Fase «A-EP-011-HU-002-lo-que-se-repitio-sale-contado» (módulo «Medición»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-011-HU-002-lo-que-se-repitio-sale-contado` |
| **Épica** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) — **una sola** (`F12.1`) |
| **Módulo** | Medición |
| **Especificación del módulo** | [documentacion/medicion/spec.md](../../../../medicion/spec.md), aprobada el 2026-08-31, con su `RN-6` agregada el mismo día |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- ✨ **Funcionalidad nueva:** `F-034`. Es **la razón por la que se pidió todo esto**: la `HU-001` indexó lo conversado para que esta pudiera contarlo.

**CA de la HU que cubre esta fase:**

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01 — El reporte sale por período](../HU-002-ver-que-correccion-se-repite.md#ca-01--el-reporte-sale-por-período) | ☐ |
| [CA-02 — Cada corrección dice cuántas veces y dónde](../HU-002-ver-que-correccion-se-repite.md#ca-02--cada-corrección-dice-cuántas-veces-y-dónde) | ☐ |
| [CA-03 — Lo mismo dicho distinto cuenta como uno](../HU-002-ver-que-correccion-se-repite.md#ca-03--lo-mismo-dicho-distinto-cuenta-como-uno) | ☐ |
| [CA-04 — Sin nada repetido, se dice](../HU-002-ver-que-correccion-se-repite.md#ca-04--sin-nada-repetido-se-dice) | ☐ |
| Transversal — el reporte no propone la regla | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que lo que el usuario tuvo que repetir salga contado, ordenado y con sus sesiones, para que se pueda escribir la regla que falta en vez de volver a corregir lo mismo.

**La línea base.** 3 720 mensajes indexados por la `HU-001`, de 67 sesiones. Formas de saber qué se repitió: ninguna.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Por período, ordenado | Funcional | Media |
| CA-02 | Cuántas veces y en qué sesiones | Funcional | Baja |
| CA-03 | Tres formas de pedir lo mismo cuentan como una | Funcional | **Alta** |
| CA-04 | Sin nada repetido, se dice | **Que NO pase** | Baja |
| RNF | Sin red y sin instalar nada | No funcional | Media |

**Fuera de alcance:**

- **Escribir la regla** que resuelve el patrón. El reporte muestra; la cadena decide.
- Pantalla. Llega cuando la vista de un proyecto la pida; esta fase entrega orden de consola, como la `HU-001`.
- Medir el tiempo de revisión (`F-032`, versión 5).

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**El caso real del `CA-03`, comprobado antes de escribir el plan.** En lo ya indexado hay diez mensajes del usuario que piden lo mismo con palabras distintas:

```
2026-08-28  adapte la plantilla del manual de instalación al español colombiano
2026-08-28  recurede el español colombiano
2026-08-22  pero español colombiano cómo sería no le olvide la regala
2026-08-14  pero encargo no es muy diciente y recuerde que es español colombiano
```

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/medicion/repeticion.py` | Nuevo | Servicio | Qué cuenta como corrección, cómo se agrupa, y el conteo |
| `plataforma/nucleo/medicion/management/commands/correcciones_que_se_repiten.py` | Nuevo | Orden | El reporte |
| `plataforma/nucleo/medicion/tests_repeticion.py` | Nuevo | Prueba | Los cuatro CA y el transversal |

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo y nada cambia de contrato. Lee `Mensaje` y `Sesion`, que la `HU-001` dejó.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican en esta fase. El punto de entrada es una orden de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Qué cuenta como corrección: todo mensaje del usuario menos una lista cerrada de confirmaciones** | Que el programa decida si un mensaje corrige | Ningún programa lee intención. Lo que sí puede es no contar «si» ni «hágale», que son la mitad de lo que se escribe. Decidido con el usuario, y escrito en la `RN-6` |
| **Se agrupa por frase compartida de dos palabras con contenido** | Comparar textos enteros por parecido | «adapte la plantilla al español colombiano» y «recuerde el español colombiano» se parecen poco como textos y son lo mismo. Lo que comparten es la frase |
| **Se agrupa por la frase, no en cadena** | Unir A con B y B con C | Basta una cadena larga para que el reporte diga que todo es lo mismo. Cada frase repetida es una fila, y un mensaje puede estar en dos si repitió dos cosas |
| **Lo que la herramienta le pega al mensaje no se cuenta** | Contar el mensaje tal como quedó guardado | Se midió: sin sacarlo, las catorce primeras filas del reporte eran ruido del editor, con «this may» 139 veces. Eso no lo escribió una persona |
| Las palabras vacías van en una lista declarada | Sin lista | La frase más repetida sería «de la» |
| El reporte cierra diciendo que **no es la regla** | Solo la lista | Una lista ordenada se lee como una lista de tareas, y `RN-1` dice que la regla la decide el usuario |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Qué cuenta como corrección | usuario | **Resuelta** el 2026-08-31; es la `RN-6` de la especificación |

---

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | `es_correccion`: la lista cerrada, y lo que la herramienta pega | Servicio | 2 h | — | RN-6 | EV-01 |
| T-02 | `frases_de`: las parejas de palabras con contenido | Servicio | 2 h | T-01 | CA-03 | EV-01 |
| T-03 | `correcciones`: contar, agrupar, ordenar, recortar por período | Servicio | 3 h | T-02 | CA-01, CA-02 | EV-01 |
| T-04 | `cuantas_correcciones`: separar los dos silencios | Servicio | 1 h | T-03 | CA-04 | EV-01 |
| T-05 | La orden de consola, con la línea que dice que no es la regla | Orden | 1 h | T-03 | Transversal | EV-02 |
| T-06 | Las pruebas, con el caso real del `CA-03` | Test | 3 h | T-04 | Todos | EV-01 |
| T-07 | Correrlo sobre lo indexado de verdad y dejar el reporte escrito | Medición | 1 h | T-05 | CA-01 | EV-02 |

**Total estimado:** 13 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05 → T-07. T-04 y T-06 cuelgan de T-03.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-002-ver-que-correccion-se-repite.md#ca-01--el-reporte-sale-por-período) | Reporte con período y sin período | EV-01, EV-02 | | ☐ |
| [CA-02](../HU-002-ver-que-correccion-se-repite.md#ca-02--cada-corrección-dice-cuántas-veces-y-dónde) | Cada fila con su cuenta y sus sesiones | EV-01 | | ☐ |
| [CA-03](../HU-002-ver-que-correccion-se-repite.md#ca-03--lo-mismo-dicho-distinto-cuenta-como-uno) | **El caso real**: las tres formas de «español colombiano» | EV-01, EV-02 | | ☐ |
| [CA-04](../HU-002-ver-que-correccion-se-repite.md#ca-04--sin-nada-repetido-se-dice) | Período sin nada repetido, y sin nada indexado | EV-01 | | ☐ |
| Transversal | El reporte dice que la decisión es del usuario | EV-02 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del servicio | `plataforma/nucleo/medicion/tests_repeticion.py` |
| EV-02 | El reporte sobre lo indexado de verdad | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

Conversaciones de mentiras que la propia prueba escribe, y **lo indexado de verdad** para el `CA-03`, que es donde está el caso que la HU nombra. Ningún dato real se toca: se lee del índice.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir en datos: el módulo solo lee. El código está versionado.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna tabla nueva, ninguna migración: lee lo que la `HU-001` dejó indexado.

---

## 9. Reglas del estándar aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md).
- Producto: `RN-1` a `RN-6` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que agrupar no salga sin instalar algo que salga a la red | Alto — lo dice la HU | Se agrupa contando palabras, sin red y sin instalar nada. **Salió** | Cerrado |
| B-02 | Que el reporte diga lo obvio | Alto — «si no nace una regla nueva, no sirvió» | Se corre sobre lo real y se mira qué sale. El juicio es del usuario | Abierto hasta T-07 |
| B-03 | Que el reporte se lea como una lista de tareas | Medio | Cierra diciendo que el patrón no es la regla | Cerrado |

---

## 11. Definition of Done

- [ ] Los cuatro CA y el transversal verificados con evidencia
- [ ] El `CA-03` probado con el caso real
- [ ] El reporte corrido sobre lo indexado, y escrito
- [ ] Si la agrupación no hubiera salido, la deuda declarada
- [ ] Pruebas en verde, y las dos baterías sin regresión
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
