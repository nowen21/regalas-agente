# Plan de Trabajo — Fase A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-006](../HU-006-procedimientos-por-rol.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-006 Escribir los procedimientos de cada rol del trabajo](../HU-006-procedimientos-por-rol.md) — una sola (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Cubre los entregables de EP-003 y crece por incrementos; los procedimientos son la parte que **todavía no cubre**, y este es su incremento (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). Los procedimientos existen y se invocan: son los diez de [`skills/`](../../../../../skills/), uno por rol, cada uno con su archivo y su descripción de cuándo usarlo. Sale de la fila de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-006 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-006-procedimientos-por-rol.md#ca-01--cada-rol-tiene-su-procedimiento-con-entrada-y-salida-declaradas) | Cada rol tiene su procedimiento, con entrada y salida declaradas | Los diez existen. Que cada uno **declare su entrada y su salida** no está comprobado |
| [CA-02](../HU-006-procedimientos-por-rol.md#ca-02--sin-la-entrada-el-procedimiento-no-arranca) | Sin la entrada, el procedimiento no arranca | Escrito dentro de cada procedimiento. Sin prueba |
| [CA-03](../HU-006-procedimientos-por-rol.md#ca-03--el-mismo-encargo-da-el-mismo-tipo-de-resultado) | El mismo encargo da el mismo tipo de resultado | **Sin comprobar.** Nadie corrió dos veces el mismo encargo para ver si el tipo de salida es el mismo |

**Por qué una sola fase.** Los tres CA se comprueban leyendo y corriendo los mismos diez procedimientos (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar escrito, procedimiento por procedimiento, qué recibe y qué entrega cada rol, y probar que sin su entrada no arranca y que el mismo encargo da el mismo tipo de resultado.

**Fuera de alcance:**

- **El procedimiento que dirige a los demás,** que es [HU-007](../../HU-007-procedimiento-que-dirige/HU-007-procedimiento-que-dirige.md).
- **Los puntos donde aprueba una persona,** que son [HU-008](../../HU-008-puntos-de-aprobacion/HU-008-puntos-de-aprobacion.md).
- **Reescribir los procedimientos.** Si a alguno le falta declarar su entrada, se anota y se propone.
- **Agregar roles nuevos.** Son los diez que hay.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 listando [`skills/`](../../../../../skills/) y leyendo la cabecera de cada procedimiento.

**Lo que ya existe:** diez procedimientos, uno por rol — analizar el proyecto, proponer el alcance, diseñar la arquitectura, generar la especificación de un módulo, planificar tareas, implementar, generar casos de prueba, cerrar la fase, revisar de forma crítica y usar la memoria — más el que dirige, que es de HU-007. Cada uno declara en su cabecera cuándo se usa y qué rol toma, y respeta el núcleo por encima de todo.

**Lo que no existe:**

1. **La declaración uniforme de entrada y salida.** Cada procedimiento dice cuándo usarlo; que diga con qué no puede arrancar y qué deja al terminar no está garantizado en los diez.
2. **El incremento en la especificación.** La spec cubre modelos, no procedimientos.
3. **La prueba del CA-03.** El mismo encargo, corrido dos veces, tendría que dar el mismo **tipo** de resultado; nadie lo midió.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/documentos-modelo/spec.md` | Modificar | Le entra el incremento: los diez roles, con la entrada y la salida de cada uno |
| `…/A-EP-003-HU-006-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-003-HU-006-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con la tabla rol → entrada → salida |
| `HU-006-procedimientos-por-rol.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `skills/` no se toca. Lo que le falte a un procedimiento se anota y se propone.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no se cambia ningún procedimiento, así que nada de lo que los invoca cambia.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son procedimientos escritos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tienen punto de entrada:** cada procedimiento se invoca por su nombre, y su descripción dice cuándo. Esta fase no lo cambia.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno. Los «roles» de esta HU son roles de trabajo, no permisos de un sistema.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La tabla rol → entrada → salida se levanta leyendo los diez, no se diseña | Escribir la tabla ideal y comparar | Retro-documentar es fotografiar lo que hay; lo ideal se propone después, con los huecos numerados |
| El CA-03 se prueba por **tipo** de resultado, no por texto | Comparar dos salidas palabra por palabra | Dos corridas nunca dan el mismo texto; lo que tiene que repetirse es qué documento sale y qué secciones trae |
| Lo que falte se numera como hueco | Corregirlo de paso | Es el paso 5 del procedimiento de [retro-documentación](../../../../../base/13-documentacion/retrodocumentacion.md) |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Con qué encargo se prueba el CA-03 — tiene que ser uno real y chico, corrido dos veces | Usuario | Pendiente |

La duda 1 bloquea T-04. Los otros dos CA no dependen de ella.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Cada rol tiene su procedimiento, con entrada y salida declaradas

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Levantar la tabla rol → qué recibe → qué entrega, leyendo los diez procedimientos | `resultado_pruebas.md` | 3,0 |
| T-02 | Escribir el incremento en la especificación con esa tabla y el criterio de qué es un rol | `documentos-modelo/spec.md` | 2,5 |

### CA-02 — Sin la entrada, el procedimiento no arranca

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: invocar dos procedimientos sin su entrada y comprobar que piden el dato en vez de inventarlo | `plan_pruebas.md` | 2,0 |

### CA-03 — El mismo encargo da el mismo tipo de resultado

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: el mismo encargo corrido dos veces entrega el mismo tipo de documento, con las mismas secciones | `plan_pruebas.md` | 2,0 |

### RNF — Que los huecos queden citables

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Numerar los procedimientos a los que les falta declarar entrada o salida | `resultado_pruebas.md` | 1,0 |
| T-06 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 12,0 horas.**

---

## 4. Secuencia de ejecución

T-01 abre, y de ahí sale T-05. T-03 en paralelo. T-04 espera la duda 1. T-02 con la tabla ya levantada. T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Tabla rol → entrada → salida sobre los diez, con los huecos numerados | T-01, T-05 |
| CA-02 | Dos procedimientos invocados sin su entrada | T-03 |
| CA-03 | El mismo encargo corrido dos veces, comparado por tipo de salida | T-04 |

---

## 6. Datos y ambiente de prueba

Este repositorio y un encargo chico y real para el CA-03, trabajado en rama aparte. Ningún dato real de cliente y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Solo entran documentos: no hay comportamiento que deshacer.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: los procedimientos no se tocan, así que nada cambia en los proyectos que los usan. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·ID6`](../../../../../base/00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md), [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F15`](../../../../../base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea el CA-03 | Elegir el encargo con el usuario | Abierto |
| R-01 | Que a varios procedimientos les falte declarar su entrada | Se destapa trabajo sobre `skills/` | Se numeran y se propone una fase que los complete | Abierto |
| R-02 | Que el CA-03 dependa de la conducta y no se pueda medir | El criterio quedaría con evidencia leída | Se acepta: se compara el tipo de salida, que sí es observable | Abierto |
| R-03 | Que la tabla salga sesgada por lo que el revisor espera encontrar | Retro-documentación que describe lo ideal | Cada fila cita el párrafo del procedimiento que la sostiene | Abierto |

---

## 11. Definition of Done

- [ ] La tabla rol → entrada → salida cubre los diez procedimientos, cada fila con su cita.
- [ ] La especificación del módulo tiene el incremento de los procedimientos.
- [ ] Está probado que sin la entrada el procedimiento pide el dato en vez de inventarlo.
- [ ] El mismo encargo dio el mismo tipo de resultado en dos corridas.
- [ ] Los procedimientos incompletos están numerados.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
