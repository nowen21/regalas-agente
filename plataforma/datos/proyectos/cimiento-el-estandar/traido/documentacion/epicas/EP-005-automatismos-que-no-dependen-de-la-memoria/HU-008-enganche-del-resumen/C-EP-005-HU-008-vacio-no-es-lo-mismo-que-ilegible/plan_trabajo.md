# Plan de Trabajo — Fase C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible (módulo Enganche del resumen)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-008](../HU-008-enganche-del-resumen.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-008 Enganche del resumen](../HU-008-enganche-del-resumen.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Enganche del resumen (`validadores/resumen.py`, `validadores/hook_resumen.py`) |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto** del `CA-02`, que la fase [`A`](../A-EP-005-HU-008-enganche-del-resumen/) dio por cerrado.

**De dónde sale:** el enganche avisó *«el resumen de esta sesión sigue vacío»* sobre un archivo con **quince hallazgos escritos**. No se equivocaba al mirar: estaban escritos como `### 1 ·` y el programa busca `### H-1 ·`.

**CA que cubre:** el `CA-02` —*«avisa cuando la sesión ya produjo algo y el resumen sigue vacío»*— en el caso que no distinguía.

---

## 1. Objetivo y alcance

**Objetivo:** que el enganche distinga **un resumen vacío** de **un resumen que no puede leer**, porque las dos cosas piden trabajo distinto: uno, escribir; el otro, renumerar lo que ya está escrito.

**Queda mudo por partida doble, y ese es el tamaño real del defecto.** El resumen se cuenta como vacío; y como la comprobación del cierre **necesita encontrar un hallazgo antes de mirar**, esa tampoco corre nunca. Encima el aviso de «sigue vacío» se marca a sí mismo como ya dado: se ve **una vez** y después calla para siempre.

**Y el aviso equivocado es peor que ninguno.** Quien lee «este resumen sigue vacío» con quince hallazgos delante concluye que el enganche se equivocó, y sigue. Un aviso que se puede desmentir de un vistazo se deja de leer.

**Fuera de alcance:**

- **Escribir la `H-` sola.** El programa dice qué le falta; renumerar es de quien escribe. Corregirlo solo tapa el caso de hoy y deja el de mañana.
- **Cambiar el molde** para aceptar las dos formas. El molde ya está, lo siguen 44 resúmenes, y aflojarlo por tres es premiar al que no lo miró.

---

## 2. Análisis previo — línea base verificada

**Medido el 2026-08-18:**

| Qué | Cuánto |
|---|---|
| Resúmenes del histórico | 47 |
| Que siguen el molde `### H-N ·` | **44** |
| Escritos como `### N ·` | **3**, todos del 2026-08-17 |
| Hallazgos invisibles en esos tres | **29** |

Los tres: [`sesion-3.md`](../../../../../historico-chat/resumenes/2026-08-17/sesion-3.md) con 10, [`sesion-4.md`](../../../../../historico-chat/resumenes/2026-08-17/sesion-4.md) con 15, y [`plan-de-pruebas-y-estado-de-las-51-fases.md`](../../../../../historico-chat/resumenes/2026-08-17/plan-de-pruebas-y-estado-de-las-51-fases.md) con 4.

**Los tres son de la misma jornada.** No es un descuido repetido: es una forma que se adoptó en una sesión y se copió a la siguiente, porque **nada la contradijo**. El aviso que debía contradecirla es justamente el que se apagó solo.

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/resumen.py` | Modificar | `_CASI_HALLAZGO`, `MARCA_MOLDE`, `hallazgos_fuera_del_molde()` |
| `validadores/hook_resumen.py` | Modificar | El aviso nuevo, antes del de vacío |
| `validadores/tests/test_el_resumen_ilegible_no_es_vacio.py` | Nuevo | Los casos |
| `historico-chat/resumenes/2026-08-17/*.md` | Modificar | Los tres, renumerados |

**No se toca `base/` ni `plantillas/`**, así que no hay versión que subir: el molde no cambia — lo que cambia es que ahora se avisa cuando no se sigue.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Dos avisos distintos, con dos marcas distintas** | Un aviso para los dos casos | Piden trabajo distinto. Y con una sola marca, avisar de uno apagaría el otro para siempre — hay caso que lo fija |
| Solo se mira **cuando no hay ni un `H-`** | Mirar siempre | Un resumen correcto puede tener secciones numeradas que no son hallazgos. Si ya sigue el molde, un `### 2 ·` suelto es otra cosa |
| El aviso **dice cuántos hay** | Decir solo que están mal | «Renumerar los tres que ya están» y «escribir el resumen» son órdenes distintas, y el número es lo que las separa |
| El aviso nuevo va **antes** del de vacío | Después | El de vacío captura el caso también; el orden es lo que hace que gane el mensaje preciso |
| Se renumeran los tres, no se aflojan las reglas | Aceptar las dos formas en el molde | 44 resúmenes siguen el molde. Cambiarlo por tres es premiar al que no lo miró |

### 2.7 Dudas por resolver antes de escribir

**Ninguna.** El molde está escrito en [`plantillas/sesion.md`](../../../../../plantillas/sesion.md) y 44 resúmenes lo confirman.

---

## 3. Desglose de tareas

| ID | Tarea | Est. |
|---|---|:--:|
| T-01 | Medir cuántos resúmenes están fuera del molde y cuántos hallazgos se pierden | 0,25 h |
| T-02 | Distinguir vacío de ilegible en `resumen.py` | 0,5 h |
| T-03 | El aviso nuevo en el enganche | 0,25 h |
| T-04 | Renumerar los tres | 0,25 h |
| T-05 | Los casos de prueba | 0,75 h |

**Total estimado:** 2 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05.

**T-04 va después de T-02**, para que la comprobación se estrene sobre los tres archivos que estaban mal. Renumerarlos primero la dejaría sin nada que encontrar.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Estado |
|---|---|---|
| CA-02 · vacío sigue diciendo vacío | Caso dedicado | ☑ |
| CA-02 · ilegible dice ilegible, y cuántos | Caso dedicado | ☑ |
| CA-02 · el aviso no se repite, y las marcas no se pisan | Dos casos | ☑ |
| Lo que el defecto tapaba · el cierre ahora se mira | Dos casos, con y sin `H-` | ☑ |
| No regresión | Las dos suites | ☑ |

---

## 6. Datos y ambiente de prueba

Resúmenes de mentira en carpetas temporales, más **una prueba sobre los 47 del repositorio**. Esa última es la que se cae cuando alguien escriba el próximo a mano sin la `H-`, que es exactamente cuando hace falta que se caiga.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. Los tres resúmenes renumerados no pierden nada: solo cambia el encabezado.

---

## 8. Producción y migración incremental

**Aditiva.** Un proyecto al día no hace nada; la próxima vez que escriba un resumen con la numeración equivocada, se lo van a decir.

---

## 9. Reglas del estándar aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Que el aviso nuevo salte en resúmenes correctos con secciones numeradas | Solo se mira cuando no hay ni un `H-`. Con caso | **Cerrado** |
| B-02 | Que marcar un aviso apague el otro | Dos marcas distintas. Con caso que lo comprueba | **Cerrado** |
| B-03 | Que el de «vacío» gane por orden y el preciso no se vea | El nuevo va antes. Con caso | **Cerrado** |
| B-04 | Que el próximo resumen se escriba mal igual | Ahora se avisa. **Lo que no se puede es forzarlo**: escribir el resumen es criterio, no automatismo | Abierto por diseño |

---

## 11. Definition of Done

- [x] Vacío e ilegible se distinguen, con marca propia cada uno
- [x] El aviso dice cuántos hallazgos hay que renumerar
- [x] Los tres resúmenes del 2026-08-17 renumerados — 29 hallazgos legibles
- [x] La prueba sobre los 47 del repositorio, en verde
- [ ] Aceptada por el usuario

---

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
