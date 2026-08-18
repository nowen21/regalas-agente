# Plan de Trabajo — Fase «A-EP-004-HU-014-comparar-los-dos-veredictos» (módulo «Programas de comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-014-comparar-los-dos-veredictos` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-014 — Un solo veredicto por fase](../HU-014-un-solo-veredicto-por-fase.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación (`validadores/fases.py`) |
| **Especificación del módulo** | No existe. Se declara como deuda en §10 (`B-03`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna.
- ✨ **Funcionalidad nueva:** la comprobación que compara los dos veredictos de una fase.

**De dónde sale:** el [pendiente 28](../../../../../pendientes/hecho/un-solo-veredicto-por-fase.md), destapado por el 27. El veredicto de una fase se escribe dos veces a mano —en el §6 del `resultado_pruebas` y en el `estado-fase`— y nada comprueba que digan lo mismo.

**La decisión que faltaba, tomada.** El pendiente dejaba dos salidas sobre la mesa y el usuario no alcanzó a elegir. Se toma **la primera —un programa compara y avisa—** y queda escrito el porqué:

| Salida | Por qué se elige o se descarta |
|---|---|
| **Un programa compara los dos y avisa si difieren** | **Elegida.** No cambia ningún documento ni ningún molde, cabe entera en EP-004 y no obliga a migrar las fases ya escritas |
| El `estado-fase` no escribe el veredicto: lo enlaza | Descartada por ahora. Quita la copia de raíz, pero cambia el molde del `estado-fase`, obliga a reescribir todas las fases cerradas y cambia lo que lee la puerta de verificación. Si un día se hace, esta comprobación sobra y se retira |

**CA de la HU que cubre esta fase:**

| CA de `HU-014` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Avisa cuando los dos veredictos difieren](../HU-014-un-solo-veredicto-por-fase.md#ca-01--avisa-cuando-los-dos-veredictos-difieren) | ☐ |
| [CA-02 — Avisa la fase dada por cumplida con un criterio en «No»](../HU-014-un-solo-veredicto-por-fase.md#ca-02--avisa-la-fase-dada-por-cumplida-con-un-criterio-en-no) | ☐ |
| [CA-03 — Avisa el conteo que no cuadra](../HU-014-un-solo-veredicto-por-fase.md#ca-03--avisa-el-conteo-que-no-cuadra) | ☐ |

---

## 1. Objetivo y alcance

**Objetivo:** que un `estado-fase` desactualizado no pueda pasar la puerta de verificación. Es el archivo que se mira para dar una fase por cerrada; si dice que cumple, la fase pasa sin que nadie abra el resultado — que es donde está la verdad.

**Fuera de alcance:**

- **Cambiar el molde del `estado-fase`.** Es la salida descartada.
- **Corregir los documentos.** La comprobación lee y avisa; escribir el veredicto bueno es de quien cierra la fase.
- **Comprobar el veredicto contra la realidad**, o sea si los criterios de verdad cumplen. Eso no lo puede saber un programa.
- **La especificación del módulo.** Deuda heredada.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/fases.py` | Modificar | Comprobación | La comparación, dentro del recorrido que ya existe |
| `validadores/tests/test_fases_veredicto.py` | Nuevo | Test | Los casos |
| `validadores/docs/fases.md` | Modificar | Documentación | La comprobación nueva |
| `pendientes/README.md` · `pendientes/hecho/` | Modificar / Nuevo | Backlog | Cerrar el 28 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | MENOR |

**Verificado el 2026-08-16 sobre el código real:**

- `fases.py` ya recorre épica → historia → fase y conoce los cinco documentos (`DOCUMENTOS`, línea 29), entre ellos `resultado_pruebas.md` y `estado-fase.md`.
- Los dos documentos escriben el veredicto en una fila de tabla con la forma `| **Concepto** | … |`, y el `resultado_pruebas` viejo lo escribe además como `**Concepto: Cumple.**`. Las dos formas hay que reconocerlas.
- El conteo de criterios aparece en los dos con nombres distintos: `CA cumplidos` en las fases nuevas y `Criterios cumplidos` en las viejas.

### 2.2 Matriz de dependencias del cambio

| Quién | Impacto |
|---|---|
| `validar.py fases` y el enganche que lo llama | Reciben hallazgos nuevos; no cambia la firma |
| Las fases ya escritas de este repositorio | **Van a aparecer las que no cuadren.** Es lo que se busca |
| El molde del `estado-fase` | Ninguno |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se comparan los conceptos normalizados —«cumple» contra «no cumple»— y no el texto entero | Exigir el texto idéntico | Las fases escriben salvedades al lado del concepto («Cumple, con una salvedad»), y eso no es una contradicción |
| Es **FALLA** cuando difieren y **AVISO** cuando uno de los dos no se puede leer | Falla en los dos casos | No poder leerlo puede ser una fase a medio escribir; decir cosas distintas no tiene excusa |
| Se reconocen las dos formas de escribir el concepto | Exigir la nueva | Reprobar por la forma vieja sería reabrir fases cerradas, y el estándar no reabre lo cerrado |
| Se compara también el conteo, no solo el concepto | Solo el concepto | Lo pide el `CA-03`, y el propio pendiente lo advierte: si se compara medio archivo, queda medio verificado |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer el concepto de los dos documentos, en sus dos formas | Comprobación | 1 h | — | EV-01 |
| T-02 | El `CA-01`: avisar cuando difieren | Comprobación | 0,6 h | T-01 | EV-01 |
| T-03 | El `CA-02`: criterio en «No» con la fase dada por cumplida | Comprobación | 0,8 h | T-01 | EV-01 |
| T-04 | El `CA-03`: el conteo que no cuadra | Comprobación | 0,6 h | T-01 | EV-01 |
| T-05 | Los casos de prueba, incluidos los transversales | Test | 1,4 h | T-04 | EV-01 |
| T-06 | Prueba de la prueba: revertir y ver los casos en rojo | Test | 0,2 h | T-05 | EV-01 |
| T-07 | `validadores/docs/fases.md` | Documentación | 0,4 h | T-05 | EV-02 |
| T-08 | Cerrar el 28 en `pendientes/` | Backlog | 0,3 h | T-07 | — |
| T-09 | `CHANGELOG.md` y `VERSION` | Versionado | 0,3 h | T-08 | — |

**Total estimado:** 5,6 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07 → T-08 → T-09

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 | Fase de mentira con los dos veredictos distintos | EV-01 | ☐ |
| CA-02 | Resultado con un requisito en «No» y estado-fase en cumplida | EV-01 | ☐ |
| CA-03 | Conteos distintos en los dos documentos | EV-01 | ☐ |
| Transversales | Sin uno de los dos documentos, y sin poder leerlos | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

Fases de mentira en carpetas temporales. Nunca una fase real ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) — el caso que destapó el pendiente ya se corrigió, y la prueba no puede depender de que alguien lo vuelva a romper.

---

## 7. Reversión / rollback

Se revierte el commit. La comprobación solo lee.

---

## 8. Producción y migración incremental

Los proyectos llaman a los validadores por su dirección en el estándar, así que la reciben sin hacer nada. **Van a aparecer hallazgos en fases que ayer estaban en verde**, y eso es lo esperado: son contradicciones que ya estaban escritas.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC3`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Falsos positivos por las salvedades que las fases escriben junto al concepto | Un validador que se equivoca se deja de leer | Se comparan conceptos normalizados, y hay un caso dedicado a una fase que cumple con salvedad | Abierto hasta la corrida |
| B-02 | Que aparezcan contradicciones en las fases de este repositorio | Trabajo no planeado | Se cuenta cuántas salen y se deja escrito; corregirlas no es de esta fase | Abierto hasta la corrida |
| B-03 | El módulo no tiene especificación | La fase se apoya en el código | Se declara la deuda | Declarado |

---

## 11. Definition of Done

- [ ] Los tres CA verificados con evidencia
- [ ] Los casos se ponen rojos si se revierte la comprobación
- [ ] Documentación, pendiente 28 cerrado, `CHANGELOG` y `VERSION`
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
