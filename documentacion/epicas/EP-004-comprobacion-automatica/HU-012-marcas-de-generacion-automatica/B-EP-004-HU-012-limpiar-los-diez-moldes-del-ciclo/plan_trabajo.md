# Plan de Trabajo — Fase B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

> **Este plan se escribió después de la intervención, y hay que decirlo.** [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) pide plan aprobado antes de tocar nada, y acá el agente ejecutó primero. Queda anotado en el `estado-fase.md` §2 y no se disimula: el documento describe lo que de verdad se hizo, no lo que se pensaba hacer.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo` |
| **Épica** | `EP-004` Comprobación automática |
| **HU** | `HU-012` Marcas de generación automática — **una sola** (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../../epica.md) |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:**

- 📝 **Modifica fase:** retoma lo que la fase A dejó abierto. Aquella contó las marcas y puso el trinquete; el [pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) cerró diciendo que las marcas de prosa quedaban para una decisión del usuario. El usuario la tomó el 2026-08-22 al ordenar ejecutar el [pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md): la voz de esta casa no lleva la raya larga ni el punto medio en prosa.

**CA de la HU que cubre esta fase:**

| CA de `HU-012` que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-012-marcas-de-generacion-automatica.md#ca-04--los-moldes-del-ciclo-no-llevan-adorno-de-prosa) | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que los moldes del ciclo de vida no le pasen adorno de prosa al proyecto que los copia.

**Fuera de alcance:**

- Las marcas que son notación del formulario. Se clasificaron y se dejaron: son 126, y quitarlas daña el molde. La decisión de declararlas notación en el anexo es del usuario, y el pendiente 78 ya la anticipaba.
- `base/`, `skills/`, `notas/` y los 21 moldes de `plantillas/` fuera del ciclo.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Verificado el 2026-08-22 con `python validadores/marcas.py --raiz plantillas/ciclo-vida-proyectos`:** 197 marcas en 10 archivos. Repartidas en 92 rayas largas de inciso, 62 puntos medios fuera de una cita y 43 viñetas que abren con negrita y dos puntos.

**Clasificadas una por una**, que es lo que decidió el alcance:

| Clase | Cuántas | Qué se hace |
|---|---|---|
| Adorno de prosa: inciso, separador entre frases, puntos suspensivos en un carácter | 71 | Se limpia |
| Citas de regla escritas fuera del formato canónico (`` `01`·C3 ``) | 13 | Se escriben bien, y dejan de contar |
| Etiqueta de campo del formulario (`- **Objetivo:** «…»`) | 43 | No se toca: es notación |
| Celda de tabla | 40 | No se toca |
| Título y nombre de sección | 23 | No se toca |
| Identificador con su enunciado (`**CAE-01** — «texto»`) | 21 | No se toca |

**Lo que impide tocar los títulos y los nombres de sección, y es comprobable:** `validar.py plantilla` compara los encabezados del documento con los de su molde y avisa «sección de la plantilla ausente». Renombrar una sección del molde hace que todos los documentos ya escritos con él reporten esa ausencia. Son 651 los documentos que `deducir_plantilla()` resuelve hoy.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los 21 moldes de `plantillas/ciclo-vida-proyectos/*.md` | Modificar | Molde | 10 traían marcas; los demás solo tenían el marcador `«…»` intacto |
| `validadores/tests/test_plantillas_origen_regla.py` | Modificar | Prueba | Su fixture copia literal una línea del molde de la especificación |
| `CHANGELOG.md` | Modificar | Versionado | Entrada de la versión |
| `VERSION` | Modificar | Versionado | Sube el dígito menor |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Clasificar antes de limpiar | Correr un reemplazo sobre las tres marcas | El reemplazo habría quitado las etiquetas de campo y renombrado secciones, y eso daña el molde y rompe la comprobación de forma de 650 documentos |
| Las citas mal escritas se corrigen, no se les quita el punto | Cambiar `` `01`·C3 `` por `01 C3` | El formato canónico ya está exento. Escribirlas bien baja el recuento y además las vuelve enlazables |
| Se para en la notación y se le lleva la decisión al usuario | Seguir limpiando | Es el mismo camino que el estándar ya recorrió el 2026-08-18 con el punto medio de los encabezados, y quedó escrito en el anexo |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | ¿La voz del estándar lleva la raya larga y el punto medio, o no? | usuario | Resuelta el 2026-08-22: no los lleva. La orden de ejecutar el pendiente 78 es la decisión |
| 2 | ¿Las cuatro formas de notación se declaran en el anexo o se reescriben los moldes? | usuario | **Abierta.** Es lo que decide si esta fase cierra o queda a medias |

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-04](../HU-012-marcas-de-generacion-automatica.md#ca-04--los-moldes-del-ciclo-no-llevan-adorno-de-prosa) — Los moldes no llevan adorno de prosa

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Volcar cada marca con su archivo y su línea, y clasificarla | Análisis | 1 h | — | EV-01 |
| T-02 | Escribir en formato canónico las citas de regla del molde de la especificación | Molde | 0,5 h | T-01 | EV-02 |
| T-03 | Reemplazar la raya de inciso por coma, paréntesis o dos puntos, y revisar una por una las que quedaron mal | Molde | 2 h | T-01 | EV-02 |
| T-04 | Reemplazar el punto medio de prosa, y reponer el marcador `«…»` si el reemplazo lo tocó | Molde | 1 h | T-03 | EV-02 |
| T-05 | Recontar y volver a clasificar lo que queda | Análisis | 0,5 h | T-04 | EV-03 |
| T-06 | Correr las suites que dependen de los moldes: las de marcas, el trinquete, el andamio, el instalador y el origen de las reglas | Prueba | 1 h | T-05 | EV-04 |
| T-07 | Sumar la entrada al `CHANGELOG.md` y subir `VERSION` | Versionado | 0,5 h | T-06 | EV-05 |

**Total estimado:** 6,5 h

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-04](../HU-012-marcas-de-generacion-automatica.md#ca-04--los-moldes-del-ciclo-no-llevan-adorno-de-prosa) | Recuento antes y después, clasificación de lo que queda, y comparación sección por sección | EV-01 a EV-04 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Volcado clasificado de las 197 | `resultado_pruebas.md` de esta carpeta |
| EV-02 | Los moldes corregidos | `plantillas/ciclo-vida-proyectos/` |
| EV-03 | Recuento final con su reparto | `resultado_pruebas.md` |
| EV-04 | Las suites que dependen de los moldes | `resultado_pruebas.md` |
| EV-05 | Entrada de versión | `CHANGELOG.md` y `VERSION` |

---

## 7. Reversión / rollback  ·  Q11

Revertir el commit de la fase. Son archivos de texto bajo control de versiones y no hay estado que reconstruir.

---

## 8. Producción y migración incremental  ·  Q12

Aditivo en el sentido que importa: los documentos ya escritos con estos moldes **no cambian ni se invalidan**. Lo que cambia es lo que se escriba de aquí en adelante. Ninguna sección se renombró, justamente para que la comprobación de forma de los documentos existentes siga dando lo mismo.

---

## 9. Reglas del estándar aplicadas  ·  Q13

- [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), que es la exigencia que se está cumpliendo.
- [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), porque el pendiente baja a fase.
- `20·M10`, por la versión y el registro.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que el reemplazo automático toque el marcador `«…»` | Lo leen `flujo.py`, `comun.py` y `andamio.py`; romperlo rompe los tres | Ocurrió: se rompió en 24 sitios y se repuso. El pendiente 11 lo advertía por escrito | Cerrado |
| R-02 | Que la coma quede donde iban dos puntos | El molde queda peor escrito que antes | Revisión línea por línea de las 25 que cambiaron; 6 se corrigieron a mano | Cerrado |
| R-03 | Que un fixture de prueba copie literal una línea del molde | La batería falla sin que haya defecto | Ocurrió con `test_plantillas_origen_regla`; el fixture se puso al día | Cerrado |

---

## 11. Definition of Done

- [ ] CA-04 verificado con evidencia
- [ ] Ninguna marca de adorno de prosa en los moldes del ciclo
- [ ] Ningún molde pide menos que antes
- [ ] Las suites que dependen de los moldes, en verde
- [ ] `CHANGELOG.md` y `VERSION` al día
- [ ] Aceptada por el usuario

---

## 13. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
