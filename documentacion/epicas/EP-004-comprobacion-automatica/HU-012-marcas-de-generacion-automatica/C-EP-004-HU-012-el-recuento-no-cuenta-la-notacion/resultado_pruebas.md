# Resultado de Pruebas — Fase C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), PP-C-EP-004-HU-012 v1.0 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Resumen de la ejecución

| Dónde | Antes | Después |
|---|---|---|
| `plantillas/ciclo-vida-proyectos/` | 126 | **0** |
| El árbol entero, sin el histórico | 15 485 | **6 440** |

**Nueve mil marcas que nunca fueron marcas.** Es la misma clase de hallazgo del 2026-08-18, cuando eximir el punto medio de los encabezados bajó el recuento de 16 477 a 15 485. Aquella vez el comentario del código ya nombraba la exención y la expresión no la implementaba; esta vez lo mismo, pero con las tres filas del anexo.

---

## 2. Ejecución caso por caso

| Caso | Qué salió | Concepto |
|---|---|---|
| CP-001 | Título y nombre de sección con raya: 0 | Pasa |
| CP-002 | Identificador con su enunciado: 0 | Pasa |
| CP-003 | Celda de tabla con raya y con punto medio: 0 | Pasa |
| CP-004 | Campo con su hueco, y campo cuyo valor iba en código: 0 | Pasa |
| CP-005 | Inciso entre rayas en prosa: 2, como antes | Pasa |
| CP-006 | Negrita con enunciado más un inciso: 2. Se descuenta una sola raya, la del enunciado | Pasa |
| CP-007 | Punto medio entre frases: 1, como antes | Pasa |
| CP-008 | La misma viñeta con prosa: 1, como antes | Pasa |
| CP-009 | El recuento baja en todas las carpetas; en ninguna sube | Pasa |
| CP-010 | `test_el_trinquete_de_las_marcas`, 10 pruebas en verde | Pasa |

**Corridas:** `test_las_marcas_de_ia_se_cuentan`, 34 pruebas, y `test_el_trinquete_de_las_marcas`, 10. Las dos en verde.

**La clasificación de las 126 que quedaban**, que es lo que decidió el diseño:

| Forma | Cuántas |
|---|---|
| Raya en un título o en el nombre de una sección | 23 |
| Raya tras un identificador o una etiqueta en negrita | 21 |
| Raya o punto medio dentro de una celda de tabla | 39 |
| Viñeta con negrita cuyo valor es el espacio por llenar | 43 |

**Y cuatro que sí eran adorno**, que la clasificación de la fase B había agrupado mal y aquí se reescribieron: dos incisos en prosa dentro de recuadros de instrucciones, y dos viñetas de prosa en el plan de trabajo.

---

## 3. Verificaciones manuales

Las tres expresiones se probaron una por una contra cinco líneas de ejemplo **antes** de conectarlas al recuento. Es a propósito: en esta misma jornada se escribió un criterio y se midió después, y hubo que rehacerlo dos veces.

---

## 4. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Alta | La expresión del campo de formulario no reconocía el valor entre comillas invertidas: `marcas_de_linea()` recibe la línea con el código ya quitado, y el valor llegaba vacío | **Corregido.** Un valor vacío también es un campo, con el motivo escrito en el código |
| D-02 | Baja | Una expectativa de prueba estaba mal contada: la línea del CP-006 trae tres rayas y se esperaban dos menos | **Corregido.** La prueba dice ahora por qué son dos |

---

## 5. Veredicto por criterio de aceptación

| Exigencia | Casos | Concepto |
|---|---|---|
| CA-03, la notación no se cuenta | CP-001 a CP-004 | Cumple |
| CA-01, la tipografía sí se cuenta | CP-005 a CP-008 | Cumple |
| No regresión | CP-009, CP-010 | Cumple |

## 5.1 Lo que el plan exigía

Se cumplió. Y con esto el [pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md) llega a la meta que se había puesto y que la fase B no pudo alcanzar: **cero marcas en los moldes del ciclo**, sin que ninguno pida nada distinto de lo que pedía y sin renombrar una sola sección.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** las cuatro formas de notación dejaron de contarse, sus cuatro parejas en prosa siguen contándose igual que antes, y las 44 pruebas de las dos suites que dependen del recuento quedaron en verde.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | La clasificación | Este documento, §2 |
| EV-02 | El código y los moldes | [`validadores/marcas.py`](../../../../../validadores/marcas.py) |
| EV-03 | La decisión escrita | [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md) |
| EV-04 | Las suites | 34 y 10 pruebas, en verde |

---

## 8. Ciclos anteriores

La fase B de esta misma HU limpió el adorno de prosa el mismo día, de 197 a 126, y se detuvo justo donde empezaba la notación.
