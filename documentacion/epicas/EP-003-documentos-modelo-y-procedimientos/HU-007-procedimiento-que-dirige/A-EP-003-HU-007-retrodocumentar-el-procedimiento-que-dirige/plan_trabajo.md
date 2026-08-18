# Plan de Trabajo — Fase A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-007](../HU-007-procedimiento-que-dirige.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-007 Escribir el procedimiento que dirige a los demás y controla los cortes](../HU-007-procedimiento-que-dirige.md) — una sola (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Cubre los entregables de EP-003 y crece por incrementos; este es el del procedimiento que dirige (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El procedimiento existe: [`skills/sdd-orchestrator/SKILL.md`](../../../../../skills/sdd-orchestrator/SKILL.md) trae las trece estaciones con su puerta y dice cuál aprueba el usuario y cuál es interna. Sale de la fila de HU-007 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-007 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-007-procedimiento-que-dirige.md#ca-01--llama-a-los-procedimientos-en-orden) | Llama a los procedimientos en orden | Escrito: las trece estaciones, en orden, con la regla de no saltar ni reordenar ([`02·F15`](../../../../../base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)). Sin prueba |
| [CA-02](../HU-007-procedimiento-que-dirige.md#ca-02--se-detiene-donde-aprueba-una-persona) | Se detiene donde aprueba una persona | Escrito: seis de las trece puertas las aprueba el usuario. Sin prueba |
| [CA-03](../HU-007-procedimiento-que-dirige.md#ca-03--el-trabajo-se-retoma-en-otra-sesión-sin-perder-el-hilo) | El trabajo se retoma en otra sesión sin perder el hilo | Escrito: el estado se persiste en cada puerta. **Y es lo que más falla en la práctica** |

**Por qué una sola fase.** Los tres CA se comprueban sobre el mismo procedimiento, llevando un encargo por sus estaciones (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que el director llama en orden, se detiene donde aprueba una persona y deja el estado escrito de forma que otra sesión retome sin releer la conversación.

**Fuera de alcance:**

- **Los diez procedimientos de rol,** que son [HU-006](../../HU-006-procedimientos-por-rol/HU-006-procedimientos-por-rol.md).
- **La lista de puntos de aprobación como documento propio,** que es [HU-008](../../HU-008-puntos-de-aprobacion/HU-008-puntos-de-aprobacion.md). Acá se prueba que el director se detiene; qué se aprueba en cada punto lo declara esa HU.
- **Reescribir el procedimiento.** Lo que falte se numera y se propone.
- **Las once etapas de `F15` contra las trece estaciones del director.** Si no coinciden, es hallazgo, no corrección de esta fase.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo el procedimiento y las 32 fases del árbol.

**Lo que ya existe:** las trece estaciones con su puerta y quién aprueba —usuario en alcance, épica, historias, especificación, plan con pruebas, guardado y publicación; interna en las demás—; la regla de no saltar ni reordenar; la orden de persistir el estado en cada puerta para sobrevivir a que se pierda el contexto; el modelo del estado de la fase, que es donde ese estado se escribe.

**Lo que no existe:**

1. **La prueba del orden.** Ninguna corrida registrada muestra las estaciones recorridas una por una.
2. **La prueba de que se retoma sin perder el hilo.** Y hay evidencia en contra: varias veces una sesión no supo lo que otra estaba haciendo — los cinco casos del pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md), incluida una en que casi se hace el mismo trabajo dos veces.
3. **El incremento en la especificación.**

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/documentos-modelo/spec.md` | Modificar | Le entra el incremento: las trece estaciones, sus puertas y qué se persiste en cada una |
| `…/A-EP-003-HU-007-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-003-HU-007-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con la comparación entre las trece estaciones y las once etapas de `F15` |
| `HU-007-procedimiento-que-dirige.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `skills/` no se toca.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no se cambia el procedimiento.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable es un procedimiento escrito.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada:** el procedimiento se invoca por su nombre cuando se pide llevar una fase de principio a fin. Esta fase no lo cambia.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El CA-03 se prueba con una sesión nueva que retoma a ciegas | Preguntarle a quien ya sabía en qué iba | Quien participó retoma de memoria: la prueba es que el documento alcance |
| La comparación con las once etapas de `F15` se anota, no se resuelve | Alinear las trece con las once ahora | Si no coinciden, es un cambio de regla o de procedimiento, y eso pasa por su procedimiento |
| Las estaciones se prueban sobre un encargo real, aunque sea chico | Simularlas leyendo el documento | Leer no prueba que se detenga: hay que llegar a la puerta |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Con qué encargo chico se recorren las estaciones | Usuario | Pendiente |

La duda 1 bloquea T-01 y T-02. El CA-03 y la comparación no dependen de ella.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 15 | 👤 **Propuesta: `shopnest-mesa`.** **Falta el encargo chico**, igual que la 14. |
---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Llama a los procedimientos en orden

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: recorrer un encargo chico y anotar estación por estación qué se llamó y qué puerta cerró | `plan_pruebas.md` | 2,5 |
| T-02 | Caso de prueba: pedir saltarse una estación y comprobar que no se salta | `plan_pruebas.md` | 1,5 |

### CA-02 — Se detiene donde aprueba una persona

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: en cada puerta de usuario, comprobar que el trabajo se detiene y que una respuesta ambigua no habilita | `plan_pruebas.md` | 2,0 |

### CA-03 — El trabajo se retoma en otra sesión sin perder el hilo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: una sesión nueva, sin la conversación, retoma leyendo solo el estado de la fase | `plan_pruebas.md` | 2,0 |
| T-05 | Anotar los casos en que esto ya falló, con el pendiente 22 como evidencia | `resultado_pruebas.md` | 1,5 |

### RNF — Que las estaciones y las etapas de la regla no se contradigan

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Comparar las trece estaciones con las once etapas de `F15` y anotar dónde no coinciden | `resultado_pruebas.md` | 1,5 |
| T-07 | Escribir el incremento en la especificación, correr lo que haya y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,5 |

**Total: 7 tareas · 13,5 horas.**

---

## 4. Secuencia de ejecución

T-05 → T-06 primero: son lectura y no dependen de la duda. T-04 después. T-01 → T-02 → T-03 con la duda 1 resuelta. T-07 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Bitácora de estaciones de un encargo real, y el intento de salto | T-01, T-02 |
| CA-02 | Detención en cada puerta de usuario, con respuesta ambigua incluida | T-03 |
| CA-03 | Sesión nueva que retoma con solo el estado de la fase | T-04, y los casos de T-05 |
| RNF | Comparación trece estaciones contra once etapas | T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio y un encargo chico y real, en rama aparte. Ningún dato real de cliente y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Solo entran documentos.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: el procedimiento no se toca. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N1`](../../../../../base/00-nucleo-blindado.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md), [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F15`](../../../../../base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea el CA-01 y el CA-02 | Elegir el encargo con el usuario | Abierto |
| R-01 | Que las trece estaciones y las once etapas no coincidan | Dos verdades sobre el mismo flujo | Se anota como hallazgo; alinearlas pasa por el procedimiento del capítulo `20` | Abierto |
| R-02 | Que el CA-03 falle, porque ya falló en la práctica | El criterio quedaría sin cumplir | Es el resultado honesto: se escribe qué faltó en el estado de la fase para poder retomar | Abierto |
| R-03 | Que recorrer las estaciones con un encargo real consuma más de lo estimado | La fase se alarga | El encargo lo elige el usuario con ese límite en mente | Abierto |

---

## 11. Definition of Done

- [ ] Hay bitácora de un encargo recorriendo las estaciones en orden.
- [ ] Está probado que no se salta una estación y que se detiene en cada puerta de usuario.
- [ ] Está probado si una sesión nueva puede retomar con solo el estado de la fase — con el resultado que dé.
- [ ] La comparación con las once etapas de `F15` está anotada.
- [ ] La especificación tiene el incremento del procedimiento que dirige.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
