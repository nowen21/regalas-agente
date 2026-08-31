# Plan de Trabajo — Fase C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion` |
| **Épica** | `EP-004` Comprobación automática |
| **HU** | `HU-012` Marcas de generación automática |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../../epica.md) |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:**

- 📝 **Modifica fase:** cierra lo que la fase B dejó abierto. Aquella limpió el adorno de prosa de los moldes, de 197 marcas a 126, y se detuvo porque las 126 restantes no eran adorno. El usuario ordenó terminar el [pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md).

**CA de la HU que cubre esta fase:**

| CA de `HU-012` | Estado |
|---|---|
| [CA-03](../HU-012-marcas-de-generacion-automatica.md#ca-03--la-notación-del-estándar-no-se-cuenta-como-marca) | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que el recuento cuente lo que el anexo dice que es marca, y nada más.

**Lo que hace falta entender antes de leer el resto.** No es una excepción nueva. El anexo escribe «la raya larga **como inciso**» y «el punto medio separando frases **en prosa**», y el programa contaba las dos en sitios que no son ni inciso ni prosa. Es el mismo hallazgo del 2026-08-18 con el punto medio de los encabezados, y quedó registrado en el propio anexo: *«el código ya lo tenía decidido y no lo había implementado»*.

**Fuera de alcance:** cambiar lo que el anexo exige. Ninguna de las tres filas se toca; lo que cambia es el programa que las cuenta.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Las 126 que quedaban en los moldes del ciclo, clasificadas una por una el 2026-08-22:**

| Forma | Cuántas | Por qué no es marca |
|---|---|---|
| Raya en el título de un documento o el nombre de una sección | 23 | Un encabezado no es un inciso. Es el mismo caso del `·`, ya eximido |
| Raya tras un identificador o una etiqueta en negrita | 21 | Separa el nombre de la cosa de lo que enuncia, no interrumpe una frase |
| Raya o punto medio dentro de una celda de tabla | 39 | Una celda es un dato, no un párrafo |
| Viñeta con negrita y dos puntos cuyo valor es el espacio por llenar | 43 | Es el rótulo de un campo de formulario. La marca del anexo es la uniformidad de la prosa |

**Y cuatro que sí eran adorno**, y no aparecían en esa cuenta porque el clasificador de la fase B las agrupó mal: dos incisos en prosa dentro de recuadros de instrucciones, y dos viñetas de prosa. Se reescriben.

**El efecto sobre el trinquete, verificado antes de tocar:** el trinquete falla cuando la cuenta **sube**. Esta fase la baja en todas partes, así que no puede romperlo. Se comprueba corriendo su suite.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/marcas.py` | Modificar | Validador | Tres expresiones nuevas y su uso en `marcas_de_linea()` |
| `base/00-identidad-y-rol/marcadores-de-ia.md` | Modificar | Regla | La decisión escrita, junto a la del 2026-08-18 |
| `plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md` | Modificar | Molde | Una viñeta de prosa |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Molde | Un inciso y dos viñetas de prosa |
| `plantillas/ciclo-vida-proyectos/08-plan-pruebas.md` | Modificar | Molde | Un inciso en prosa |
| `CHANGELOG.md` y `VERSION` | Modificar | Versionado | `20·M10` |

### 2.2 Matriz de dependencias del refactor

`marcas_de_linea()` cambia lo que devuelve, y de ella dependen `contar()`, `validar()`, `validar_preparados()` y el trinquete. Ninguna cambia de firma: todas reciben menos marcas, que es el objetivo. Sus dos suites se corren enteras.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se implementa lo que el anexo ya dice | Declarar cuatro excepciones nuevas | No son excepciones. «Como inciso» y «en prosa» están escritos desde que se escribió el anexo |
| El campo de formulario se reconoce por su **valor**, no por su rótulo | Eximir toda viñeta con negrita dentro de `plantillas/` | Por la carpeta, un molde podría meter prosa y quedar exento. Por el valor, la misma línea llenada con prosa vuelve a contar, que es lo correcto |
| Un valor que quedó vacío al quitarle el código también es un campo | Mirar la línea original | `marcas_de_linea()` recibe la línea ya sin código, y el valor `` `«slug»` `` llega vacío. Pedir la línea original obligaría a cambiar la firma y todos sus llamadores |
| Las cuatro de prosa se reescriben | Dejarlas | Son adorno de verdad, y el pendiente pedía llegar a cero |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | ¿Se declara notación, o se reescriben los moldes asumiendo el daño? | usuario | Resuelta el 2026-08-22: el usuario ordenó hacer el pendiente 78, y esta es la vía que no daña los moldes ni rompe la comprobación de forma de 651 documentos |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Clasificar las 126 y medir cuántas caen en cada forma | Análisis | 1 h | — | EV-01 |
| T-02 | Las tres expresiones, y su uso en el recuento de la raya, el punto medio y la viñeta | Validador | 1,5 h | T-01 | EV-02 |
| T-03 | Reescribir las cuatro que sí eran adorno | Molde | 0,5 h | T-02 | EV-02 |
| T-04 | Escribir la decisión en el anexo, junto a la del 2026-08-18 | Regla | 0,5 h | T-02 | EV-03 |
| T-05 | Correr las dos suites que dependen del recuento, y volver a medir | Prueba | 0,5 h | T-03 | EV-04 |
| T-06 | `CHANGELOG` y `VERSION` | Versionado | 0,25 h | T-05 | EV-05 |

**Total estimado:** 4,25 h

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-03](../HU-012-marcas-de-generacion-automatica.md#ca-03--la-notación-del-estándar-no-se-cuenta-como-marca) | Recuento antes y después, y las dos suites del recuento en verde | EV-01 a EV-04 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | La clasificación de las 126 | `resultado_pruebas.md` §2 |
| EV-02 | El código y los moldes | `validadores/marcas.py`, `plantillas/ciclo-vida-proyectos/` |
| EV-03 | La decisión escrita | `base/00-identidad-y-rol/marcadores-de-ia.md` |
| EV-04 | Las suites | `test_las_marcas_de_ia_se_cuentan`, `test_el_trinquete_de_las_marcas` |
| EV-05 | Versión | `CHANGELOG.md` y `VERSION` |

---

## 6. Datos y ambiente de prueba

El repositorio, en la máquina del usuario. Sin datos reales.

---

## 7. Reversión / rollback  ·  Q11

Revertir el commit. El recuento vuelve a contar de más, que es lo que hacía.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo en el sentido que importa, y hay que decir por qué.** La cuenta baja en todas partes, y el trinquete falla cuando **sube**: ningún commit que hoy pasa va a empezar a fallar. Al revés, los proyectos instalados que arrastraban deuda de notación la ven desaparecer sin tocar un archivo, porque nunca fue deuda.

---

## 9. Reglas del estándar aplicadas  ·  Q13

- [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), que es la regla que el recuento sirve.
- [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), por el alcance de la corrida.
- `20·M10`, por la versión y el registro.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que se deje de contar adorno de prosa de verdad | La regla queda escrita y sin quien la cuente | Las tres expresiones se atan a la forma, no a la carpeta. La misma línea llenada con prosa vuelve a contar | Cerrado |
| R-02 | Que el trinquete se rompa | Los commits empiezan a fallar sin motivo | La cuenta solo baja, y el trinquete falla cuando sube. Su suite se corre entera | Cerrado |

---

## 11. Definition of Done

- [x] CA-03 verificado con evidencia
- [x] Las suites que la fase toca, en verde
- [x] La decisión escrita en el anexo
- [x] `CHANGELOG.md` y `VERSION` al día
- [ ] Aceptada por el usuario

---

## 13. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
