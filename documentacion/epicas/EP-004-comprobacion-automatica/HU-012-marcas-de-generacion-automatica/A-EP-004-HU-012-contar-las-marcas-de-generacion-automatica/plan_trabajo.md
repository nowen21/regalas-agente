# Plan de Trabajo — Fase A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-012](../HU-012-marcas-de-generacion-automatica.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-012 Comprobar las marcas de generación automática en lo que se entrega](../HU-012-marcas-de-generacion-automatica.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-012](../HU-012-marcas-de-generacion-automatica.md). El entregable es un programa de comprobación: sus criterios de aceptación y la lista de [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md) son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** La exigencia existe —[`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), con su lista en [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md)— y **ningún programa la comprueba**: buscado en los 24 subcomandos, no hay ninguno. El registro de reglas validables la tiene marcada como validable en seco y parcial, es decir: pendiente. Sale de la fila de HU-012 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-012 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-012-marcas-de-generacion-automatica.md#ca-01--las-marcas-de-tipografía-se-cuentan) | Las marcas de tipografía se cuentan | **No está.** Nadie las cuenta, y el pendiente [11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) está abierto justamente porque el propio estándar las tiene |
| [CA-02](../HU-012-marcas-de-generacion-automatica.md#ca-02--las-marcas-invisibles-se-encuentran) | Las marcas invisibles se encuentran | **No está.** Son las que nadie ve al leer, y por eso son las que sobreviven a una revisión a ojo |
| [CA-03](../HU-012-marcas-de-generacion-automatica.md#ca-03--la-notación-del-estándar-no-se-cuenta-como-marca) | La notación del estándar no se cuenta como marca | **Es el criterio que decide si el programa sirve.** El estándar usa a propósito el punto medio, las comillas angulares y las casillas: contarlas sería reportar el estándar entero |

**Por qué una sola fase.** Los tres CA los comprueba el mismo programa, y el tercero es lo que separa un reporte útil de uno que nadie lee (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que la exigencia de no entregar texto con marcas de generación automática se pueda comprobar, sin que la notación del propio estándar cuente como marca.

**Fuera de alcance:**

- **Limpiar las marcas que el estándar ya tiene.** Es el pendiente [11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md): esta fase da la herramienta y mide, no limpia.
- **Juzgar el estilo.** Que un texto se lea bien es criterio humano; acá se cuentan marcas concretas de una lista cerrada.
- **Los términos en inglés,** que son los pendientes [21](../../../../../pendientes/hecho/los-nombres-de-rol-en-espanol.md) y [26](../../../../../pendientes/hecho/corrida-y-ejecucion-en-el-estandar.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: ningún archivo de `validadores/` menciona la lista de marcadores, y `validar.py --help` no ofrece nada parecido.

**Lo que ya existe:** la regla que lo exige y la lista de marcas, escrita y mantenida en el capítulo de identidad; el formato común del hallazgo, con archivo y línea; el pendiente 11, que dice que el propio estándar las tiene y por eso hay algo que medir; y el registro de reglas validables, que ya clasificó esta regla como comprobable en seco y parcial.

**Lo que no existe:**

1. **El programa.** Ninguno de los 24 subcomandos mira esto.
2. **La lista de notación propia.** Qué símbolos usa el estándar a propósito no está escrito en ninguna parte como lista, así que un programa ingenuo reportaría casi cada línea.
3. **La medida de cuántas marcas hay hoy.** El pendiente 11 afirma que hay; nadie las contó.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/marcas.py` | Nuevo | El programa, con las tres comprobaciones |
| `validadores/validar.py` | Modificar | Su subcomando |
| `validadores/docs/marcas.md` | Nuevo | Qué mira, qué no y por qué |
| `validadores/pruebas.py` | Modificar | Los casos de los tres CA |
| `validadores/reglas-validables.md` | Modificar | `00·ID8` pasa de validable pendiente a validador escrito |
| `base/00-identidad-y-rol/marcadores-de-ia.md` | Modificar | Le entra la lista de notación propia que no cuenta como marca |
| `pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md` | Modificar | Se le suma la cuenta real |
| `…/A-EP-004-HU-012-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-012-marcas-de-generacion-automatica.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Toca `base/`: entrada y subida ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> El programa lee la lista del capítulo, no una copia: si la lista cambia, la comprobación cambia con ella.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `base/00-identidad-y-rol/marcadores-de-ia.md` | Le entra la lista de notación propia | El programa nuevo, que la lee | Es un agregado: nada de lo que ya cita ese documento cambia de sentido |
| `validadores/validar.py` | Un subcomando nuevo | Los enganches que llaman por nombre | Solo se agrega |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tendrá punto de entrada:** su subcomando en `validar.py`. Sin él, el programa sería uno más de los que callan.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La lista de marcas se lee del capítulo | Copiarla dentro del programa | Dos listas de lo mismo se separan solas, y la del capítulo es la que manda |
| La notación propia se declara en el mismo capítulo | Meterla como excepción dentro del programa | Quien reciba un hallazgo tiene que poder leer por qué su símbolo sí cuenta y otro no |
| El programa cuenta y no corrige | Que borre las marcas que encuentra | Corregir texto ajeno sin aprobación es cambiar el entregable: se reporta |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si la comprobación aplica a todo el repositorio o solo a lo que se entrega — el histórico, por ejemplo, es transcripción y no entregable | Usuario | **Resuelta el 2026-08-18** —el recuento no toca el histórico, y ya estaba construido así— y revisada el 2026-08-22: ver el segundo ciclo en `resultado_pruebas_2.md` |

La duda 1 bloquea T-01: cambia qué archivos recorre el programa.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 21 | **Ya estaba contestada** en el pendiente 11, paso 3: no se toca el histórico. Construido así el 2026-08-18. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Las marcas de tipografía se cuentan

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir la comprobación de las marcas de tipografía, leyendo la lista de `marcadores-de-ia.md` y no una copia | `validadores/` | 3,0 |
| T-02 | Caso de prueba: un texto con marcas se reporta con archivo y línea; uno sin ellas, no | `plan_pruebas.md` | 1,5 |

### CA-02 — Las marcas invisibles se encuentran

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Escribir la comprobación de los caracteres invisibles | `validadores/` | 2,0 |
| T-04 | Caso de prueba: un espacio que no se ve y un separador invisible se reportan por su posición | `plan_pruebas.md` | 1,5 |

### CA-03 — La notación del estándar no se cuenta como marca

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Escribir la lista de lo que es notación del estándar y no marca, y comprobar que no se reporta | `validadores/` | 2,0 |
| T-06 | Caso de prueba: correr sobre `base/` y comprobar que la notación propia no aparece en el reporte | `plan_pruebas.md` | 2,0 |

### RNF — Que el reporte se pueda creer

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 13,5 horas.**

---

## 4. Secuencia de ejecución

T-05 primero —la lista de notación propia—, porque sin ella el programa reporta todo. Después T-01 → T-02, T-03 → T-04, y T-06 sobre `base/`. T-07 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Texto con marcas y texto sin ellas | T-02 |
| CA-02 | Caracteres invisibles reportados por su posición | T-04 |
| CA-03 | Corrida sobre `base/`, sin reportar la notación propia | T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. El programa es **aditivo**, pero el agregado a `marcadores-de-ia.md` toca `base/`: subida **MENOR** si solo declara la notación que ya se usaba. Un proyecto que se actualice va a empezar a ver hallazgos que antes nadie contaba, y la entrada del registro tiene que decirlo.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·ID7`](../../../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Cambia qué recorre el programa | Se presenta al usuario antes de escribirlo |
| R-01 | Que el programa reporte cientos de marcas en el propio estándar | Parece inservible y es el dato que el pendiente 11 necesita | El resultado separa la cuenta del estándar de la de un entregable nuevo |
| R-02 | Que la notación propia y una marca real coincidan en el mismo símbolo | Falso positivo imposible de arreglar | Se resuelve por contexto y, si no se puede, esa marca se declara no comprobable |
| R-03 | Que el programa se vuelva un corrector de estilo | Reportes que nadie acepta | La lista es cerrada: lo que no está en ella, no se cuenta |

---

## 11. Definition of Done

- [ ] El programa corre por su subcomando y dice qué encontró.
- [ ] Las marcas de tipografía y las invisibles se detectan, con archivo y línea.
- [ ] La notación del estándar no aparece en el reporte, con prueba sobre `base/`.
- [ ] La cuenta real quedó anotada en el pendiente 11.
- [ ] `00·ID8` quedó registrada como validador escrito.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
