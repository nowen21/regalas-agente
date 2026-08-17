# Plan de Trabajo — Fase «A-EP-007-HU-007-la-revision-ve-la-cadena» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-007-la-revision-ve-la-cadena` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-007 — Revisar qué le falta al proyecto](../HU-007-revisar-que-falta.md) — **una sola** (`F12.1`) |
| **Módulo** | Instalación (`validadores/checklist.py`) |
| **Especificación del módulo** | No existe. Se declara como deuda en §10 (`B-03`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna. La HU-007 no tenía fases.
- ✨ **Funcionalidad nueva:** un punto más en la revisión, el primero que mira **proceso** y no instalación.

**De dónde sale:** el [pendiente 30](../../../../../pendientes/hecho/la-revision-ve-la-cadena.md), reportado por `shopnest-mesa`. Un proyecto llegó a código commiteado con `prompts/` vacía, sin épica y sin historia, y la revisión decía «13 de 13, instalación completa». Lo notó el usuario preguntando, no el estándar.

**CA de la HU que cubre esta fase:**

| CA de `HU-007` que cierra esta fase | Estado |
|---|---|
| [CA-01 — La revisión dice qué falta, componente por componente](../HU-007-revisar-que-falta.md#ca-01--la-revisión-dice-qué-falta-componente-por-componente) | ☐ |
| [CA-02 — El aviso se apaga solo cuando ya no falta nada](../HU-007-revisar-que-falta.md#ca-02--el-aviso-se-apaga-solo-cuando-ya-no-falta-nada) | ☐ |

**Por qué estos dos y no un CA nuevo.** Acá no hace falta inventar criterio: el `CA-01` ya dice que la revisión nombra lo que falta y el `CA-02` que el aviso se apaga cuando no falta nada. Lo que cambia es **qué cuenta como faltar**, y eso lo declara la lista de componentes, que vive fuera del programa (`RN-02` de la historia).

---

## 1. Objetivo y alcance

**Objetivo:** que la revisión deje de decir «completo» cuando la cadena de [`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) está vacía. Mientras diga «completo» con `prompts/` sin un solo planteamiento, está afirmando algo que `F0` contradice — y el proyecto se entera cuando ya hay código escrito, que es cuando la trazabilidad hacia atrás cuesta.

**Fuera de alcance:**

- **Que el instalador deje el planteamiento puesto.** No puede: lo escribe el agente con lo que el usuario quiere, y el instalador no pregunta. Copiar la plantilla con los marcadores sin llenar sería peor — parecería un planteamiento y la revisión lo daría por cumplido.
- **Comprobar la cadena entera hacia abajo** (que cada historia tenga fase, que cada fase tenga plan). Eso ya lo mira `flujo.py`, y meterlo acá sería tenerlo en dos sitios.
- **Detener el trabajo.** La `RN-06` de la historia lo prohíbe: el aviso no detiene.
- **La especificación del módulo.** Deuda heredada.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/stack-instalacion.md` | Modificar | Lista | La fila del punto nuevo, y la nota de qué lo distingue |
| `validadores/checklist.py` | Modificar | Instalación | La comprobación y su entrada en el mapa |
| `validadores/tests/test_checklist_cadena.py` | Nuevo | Test | Los casos |
| `validadores/docs/checklist.md` | Modificar | Documentación | El punto nuevo |
| `pendientes/README.md` · `pendientes/hecho/` | Modificar / Nuevo | Backlog | Cerrar el 30 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | **MAYOR** |

**Verificado el 2026-08-16 sobre el código real:**

- La lista de componentes **no vive en el programa**: `componentes()` la lee de `plantillas/stack-instalacion.md` con la expresión de la línea 42, que toma las filas de la tabla.
- `COMPROBACIONES` (línea 250) es el mapa de identificador a función. Un identificador que esté en la lista y no en el mapa **ya se reporta como faltante**, así que las dos mitades hay que ponerlas juntas.
- `instalar.py` crea `prompts/` en `CARPETAS_BASE` y la deja vacía, que es exactamente lo que el pendiente describe.

### 2.2 Matriz de dependencias del cambio

| Quién | Impacto |
|---|---|
| La huella del stack | **Cambia**, porque cambia la lista. Todo proyecto instalado va a decir que tiene una actualización pendiente, y al correr el instalador se pone al día |
| El aviso de cada sesión | Un proyecto sin planteamiento pasa a decir «13 de 14» en vez de «13 de 13» |
| `instalar.py` | Ninguno: no instala este punto y no debe. Su columna de la lista lo dice |
| `flujo.py` | Ninguno: sigue mirando la cadena hacia abajo, desde la épica |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Entra como un punto más de la revisión | Esperar al validador de flujo del pendiente 01 | El 01 es obra grande y no tiene fecha. Lo que hoy dice una falsedad es la revisión, y es donde se arregla |
| El punto dice explícitamente que **no lo instala el instalador** | Dejar la columna igual que los demás | Si no lo dice, alguien va a correr el instalador esperando que aparezca el planteamiento |
| Se exige al menos un planteamiento en `prompts/` | Exigir uno por módulo | Un proyecto arranca con un planteamiento; exigir más es inventar una regla que `F0` no pide |
| La épica solo se exige **si hay código** en `proyectos/` | Exigirla siempre | Un proyecto recién instalado no tiene código, y pedirle épica el primer día es ruido que se aprende a ignorar |
| Es **MAYOR** | MENOR | Un proyecto al día tiene que hacer algo nuevo: escribir su planteamiento. Que sea un aviso y no un bloqueo no lo vuelve opcional |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | La fila del punto nuevo en `plantillas/stack-instalacion.md` | Lista | 0,4 h | — | EV-01 |
| T-02 | La comprobación en `checklist.py` y su entrada en el mapa | Instalación | 1 h | T-01 | EV-01 |
| T-03 | Los casos de prueba | Test | 1,2 h | T-02 | EV-01 |
| T-04 | Prueba de la prueba: quitar el punto y ver el caso en rojo | Test | 0,2 h | T-03 | EV-01 |
| T-05 | `validadores/docs/checklist.md` | Documentación | 0,4 h | T-03 | EV-02 |
| T-06 | Cerrar el 30, con el aviso a `shopnest-mesa` anotado | Backlog | 0,4 h | T-05 | — |
| T-07 | `CHANGELOG.md` y `VERSION` (MAYOR) | Versionado | 0,4 h | T-06 | — |

**Total estimado:** 4 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 | Proyecto de mentira sin planteamiento: la revisión lo nombra y dice cómo se arregla | EV-01 | ☐ |
| CA-02 | Se escribe el planteamiento y el punto deja de reportarse | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con proyectos de mentira. Nunca un proyecto real ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

---

## 7. Reversión / rollback

Se revierte el commit. La revisión solo lee y reporta.

---

## 8. Producción y migración incremental

**Toca a todo proyecto instalado.** La huella del stack cambia, así que cada uno va a avisar que tiene una actualización pendiente y se pone al día corriendo el instalador — el camino que la v21.2.0 dejó hecho. Después, el que no tenga planteamiento va a decir «13 de 14» hasta que lo escriba, **que es el punto**.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el aviso se vuelva permanente en proyectos que nunca van a escribir planteamiento | Se aprende a ignorar la revisión entera | El aviso se apaga escribiendo el planteamiento, que es lo que `F0` pide. Si un proyecto no lo va a escribir nunca, el problema no es el aviso | Aceptado |
| B-02 | Que este repositorio reprueba su propio punto nuevo | El estándar exigiendo lo que no cumple | Se comprueba contra esta casa y se deja escrito el resultado, salga lo que salga | Abierto hasta la corrida |
| B-03 | El módulo no tiene especificación | La fase se apoya en el código | Se declara la deuda | Declarado |

---

## 11. Definition of Done

- [ ] La revisión nombra la cadena vacía y dice cómo se arregla
- [ ] El punto se apaga al escribir el planteamiento
- [ ] La prueba se pone roja si se quita el punto
- [ ] Documentación, pendiente 30 cerrado, `CHANGELOG` y `VERSION`
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
