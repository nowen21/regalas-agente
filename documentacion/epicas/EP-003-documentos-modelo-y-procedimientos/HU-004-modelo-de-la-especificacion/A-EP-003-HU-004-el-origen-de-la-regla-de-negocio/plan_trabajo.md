# Plan de Trabajo — Fase «A-EP-003-HU-004-el-origen-de-la-regla-de-negocio» (módulo «Documentos modelo»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-004-el-origen-de-la-regla-de-negocio` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-004 — Modelo de la especificación](../HU-004-modelo-de-la-especificacion.md) — **una sola** (`F12.1`) |
| **Módulo** | Documentos modelo (`plantillas/plantilla-spec-modulo.md`) |
| **Especificación del módulo** | No existe. Se declara como deuda en §10 (`B-02`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna. La HU-004 no tenía fases: el modelo se escribió antes de que la épica se descompusiera.
- ✨ **Funcionalidad nueva:** el §4 del modelo pasa a pedir **dos** datos por regla, no uno.

**De dónde sale:** el [pendiente 43](../../../../../pendientes/hecho/el-origen-de-la-regla-de-negocio.md), reportado por `shopnest-mesa`.

**CA de la HU que cubre esta fase:**

| CA de `HU-004` que cierra esta fase | Estado |
|---|---|
| **CA-04 — Toda regla de negocio dice de dónde baja** — se agrega a la HU en esta fase (T-01) | ☐ |

**Por qué un CA nuevo.** Los tres que hay miran que el modelo **tenga** las secciones (`CA-01`), que lo que no aplica quede dicho (`CA-02`) y que el cruce entre módulos quede en los dos lados (`CA-03`). Ninguno mira **qué se pide adentro** de una sección. Sin criterio no hay de dónde derivar el plan ([`02·F18`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)).

**Redacción propuesta del CA-04:**

```gherkin
Dado que se escribe una regla de negocio en la especificación de un módulo
Cuando se llena el §4 del modelo
Entonces la regla dice de dónde baja, con el identificador del requisito, la historia o la decisión
Y la que no tenga procedencia no se escribe ahí: se sube a la historia que corresponda
```

---

## 1. Objetivo y alcance

**Objetivo:** que una regla de negocio sin procedencia no pueda entrar sin que se note. Hoy el §4 pide **el porqué** y nunca **el de dónde**, así que una regla con buena justificación y ninguna fuente entra sin resistencia — y baja sola a decisión, trazabilidad, pruebas y criterio de aceptación.

**Fuera de alcance:**

- **El programa que lo comprueba.** Vive en otro módulo y va en su propia fase, bajo [EP-004 · HU-004](../../../EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/HU-004-forma-de-los-documentos.md) ([`02·F11`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md)).
- **Revisar los §4 ya escritos** en las especificaciones vivas. El estándar no reabre lo cerrado; queda anotado como lo que sigue.
- **La columna `Origen` de la tabla de campos** del §5.1, que `shopnest-mesa` inventó por su cuenta. Es la misma idea aplicada a otra sección, y merece su propia decisión.
- **La especificación del módulo de documentos modelo.** Deuda heredada.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/.../HU-004-modelo-de-la-especificacion.md` | Modificar | HU | El `CA-04`, la fase en §8 y la bitácora |
| `plantillas/plantilla-spec-modulo.md` | Modificar | Modelo | El §4 pide las dos cosas |
| `pendientes/README.md` · `pendientes/hecho/` | Modificar / Nuevo | Backlog | Cerrar el 43 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | **MAYOR** |

**Verificado el 2026-08-16:** el §4 de [`plantillas/plantilla-spec-modulo.md`](../../../../../plantillas/plantilla-spec-modulo.md) está en la línea 30 y hoy pide `1. «Regla — por qué existe.»`.

### 2.2 Matriz de dependencias del cambio

| Quién | Impacto |
|---|---|
| Las especificaciones ya escritas | **Ninguno automático.** El modelo cambia para lo que se escriba de acá en adelante; lo viejo no se reabre |
| El programa que compara documento contra modelo | Hoy compara secciones, no el contenido de una lista. No se entera de este cambio |
| La fase del validador, en EP-004 | Se apoya en esta: sin el formato fijado no hay qué comprobar |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El origen va **en la misma línea** de la regla | Una columna aparte, o una tabla de cuatro columnas | El §4 es una lista numerada y las reglas se citan por su número; volverla tabla obliga a reescribir todas las especificaciones vivas |
| Se exige un identificador, no una frase | Aceptar «viene del taller» | Un identificador se puede comprobar; una frase no. El validador de la otra fase depende de esto |
| La regla sin procedencia **no se escribe ahí** | Dejarla con el origen en blanco | Un hueco se llena con cualquier cosa; una prohibición manda a subirla a la historia, que es de donde tenía que bajar |
| Es **MAYOR** | MENOR, por ser una plantilla | Un proyecto al día tiene que hacer algo nuevo: escribir la procedencia en cada regla que agregue. Eso es exactamente lo que `20·M10` llama obligar |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El `CA-04` en la HU-004, con su fase en §8 y su bitácora | HU | 0,4 h | — | EV-02 |
| T-02 | El §4 del modelo pide las dos cosas, con la nota de la regla sin procedencia | Modelo | 0,6 h | T-01 | EV-01 |
| T-03 | Comprobar el modelo llenándolo con una regla con origen y otra sin él | Prueba manual | 0,5 h | T-02 | EV-01 |
| T-04 | Cerrar el 43 en `pendientes/`, con el aviso a `shopnest-mesa` anotado | Backlog | 0,4 h | T-03 | — |
| T-05 | `CHANGELOG.md` y `VERSION` (MAYOR) | Versionado | 0,4 h | T-04 | — |

**Total estimado:** 2,3 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-04 | Se llena el §4 con el caso real que lo destapó y con una regla sin fuente; se mira si el modelo deja pasar la segunda | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Lo que se escribió al llenar el modelo | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

Un §4 de mentira escrito dentro del `resultado_pruebas`, con la regla real de `shopnest-mesa` que destapó el pendiente. No se toca ninguna especificación viva.

---

## 7. Reversión / rollback

Se revierte el commit. Las especificaciones escritas con el formato nuevo siguen siendo válidas con el viejo: tienen un dato de más, no uno de menos.

---

## 8. Producción y migración incremental

**Toca a todo proyecto instalado**, porque el modelo se hereda. La migración es incremental por definición: aplica a las reglas que se escriban de acá en adelante, y las ya escritas quedan selladas con la versión bajo la que se escribieron ([`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)). Ningún proyecto tiene que reescribir su §4 para seguir cumpliendo.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F11`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), [`02·F18`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md), [`13·DOC2`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el identificador se vuelva un trámite y se escriba cualquier cosa | La procedencia diría algo que no se puede seguir | El validador de la otra fase comprueba que el identificador **exista**; acá se fija el formato para que se pueda | Abierto, se cierra en la otra fase |
| B-02 | El módulo de documentos modelo no tiene especificación | La fase se apoya en el archivo | Se declara la deuda | Declarado |

---

## 11. Definition of Done

- [ ] El `CA-04` escrito en la HU-004 y esta fase nombrada en su §8
- [ ] El §4 del modelo pide la procedencia, con la nota de qué hacer si no la hay
- [ ] Comprobado llenándolo
- [ ] Pendiente 43 cerrado, `CHANGELOG` y `VERSION`
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
