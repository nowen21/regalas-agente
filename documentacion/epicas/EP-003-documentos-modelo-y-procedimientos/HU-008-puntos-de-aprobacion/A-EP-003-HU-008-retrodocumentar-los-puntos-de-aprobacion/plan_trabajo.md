# Plan de Trabajo — Fase A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-008](../HU-008-puntos-de-aprobacion.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-008 Declarar los puntos donde aprueba una persona](../HU-008-puntos-de-aprobacion.md) — una sola (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Cubre los entregables de EP-003 y crece por incrementos; este es el de los puntos de aprobación (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta lo que existe: la tabla de estaciones de [`skills/sdd-orchestrator`](../../../../../skills/sdd-orchestrator/SKILL.md) dice cuál puerta aprueba el usuario, `01·C17` dice que solo su palabra afirmativa cuenta, y `00·N2` que la autorización es de un solo uso. ✨ Y construye lo que falta: **la lista no vive en `base/`**, sino dentro de un procedimiento, así que un proyecto que herede el estándar recibe las reglas sueltas y no la lista. Sale de la fila de HU-008 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-008 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-008-puntos-de-aprobacion.md#ca-01--la-lista-existe-y-dice-qué-se-aprueba-en-cada-punto) | La lista existe y dice qué se aprueba en cada punto | **A medias.** Existe como tabla de un procedimiento, no como documento de la capa que se hereda |
| [CA-02](../HU-008-puntos-de-aprobacion.md#ca-02--una-respuesta-ambigua-no-habilita) | Una respuesta ambigua no habilita | Es regla: `01·C17`. Sin prueba |
| [CA-03](../HU-008-puntos-de-aprobacion.md#ca-03--aprobar-una-cosa-no-aprueba-la-siguiente) | Aprobar una cosa no aprueba la siguiente | Es regla y está blindada: `00·N2` dice que la autorización es de un solo uso. Sin prueba |

**Por qué una sola fase.** Los tres CA son la misma lista vista desde tres ángulos: qué se aprueba, qué cuenta como aprobación y hasta dónde alcanza (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que los puntos de aprobación queden en una lista que viaje con el estándar, y que las dos reglas que la sostienen queden probadas.

**Fuera de alcance:**

- **El procedimiento que dirige,** que es [HU-007](../../HU-007-procedimiento-que-dirige/HU-007-procedimiento-que-dirige.md). Acá se toma su tabla como fuente de la lista.
- **Cambiar quién aprueba qué.** La lista se escribe con los puntos que ya rigen; agregar o quitar uno es decisión del usuario.
- **La aprobación del commit y del despliegue como reglas.** Ya son `00·N2`: la lista las enlaza, no las repite.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 buscando «puntos de aprobación» en `base/`, `plantillas/` y `skills/`.

**Lo que ya existe:** la tabla de trece estaciones del director, con seis puertas de usuario —alcance, épica, historias, especificación, plan con pruebas, guardado y publicación—; `01·C17`, que exige palabra afirmativa del usuario y no da por aprobado un silencio ni un «ok, pero…»; `00·N2`, blindada, que hace la autorización de un solo uso; `02·F4`, que fija la secuencia de aprobación de los dos planes.

**Lo que no existe:**

1. **La lista en `base/`.** Buscada en los tres sitios: solo aparece dentro del procedimiento del director. Un proyecto que hereda recibe `base/`, así que hereda las reglas y no la lista.
2. **La prueba del CA-02.** Que una respuesta ambigua no habilite es regla y nadie lo comprobó.
3. **La prueba del CA-03.** Que aprobar una cosa no apruebe la siguiente tampoco.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `base/02-flujo-de-trabajo/` | Nuevo o modificar | Donde caiga la lista según el enrutado de [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md): el flujo de trabajo es el dueño de las etapas |
| `validadores/reglas-validables.md` | Modificar | Si la lista entra como regla, declara si es comprobable |
| `documentacion/documentos-modelo/spec.md` | Modificar | Le entra el incremento: los puntos de aprobación y qué se aprueba en cada uno |
| `…/A-EP-003-HU-008-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-003-HU-008-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `HU-008-puntos-de-aprobacion.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Si entra en `base/`: entrada y subida ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `skills/` no se toca: la lista se **copia hacia** `base/` y el procedimiento queda enlazándola, no al revés.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| La lista nueva en `base/` | Pasa a ser la fuente de los puntos de aprobación | La tabla de estaciones del director, que hoy es la única fuente | El procedimiento tendría que enlazarla en vez de repetirla ([`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md)); si eso se hace en esta fase o en otra, lo decide la duda 2 |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable es texto normativo. La «autorización» de esta HU es la de una persona, no un permiso de sistema.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. La lista se lee al abrir la sesión, con el capítulo de flujo de trabajo.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La lista se escribe con los puntos que ya rigen | Rediseñar los puntos de aprobación | Retro-documentar es fotografiar; cambiar quién aprueba qué es decisión del usuario |
| La lista enlaza `00·N2` y `01·C17` en vez de repetirlas | Copiar su texto dentro de la lista | La fila 11 del checklist prohíbe el texto prestado: lo que ya dice otra regla se enlaza |
| El CA-02 se prueba con respuestas ambiguas de verdad | Probar solo con un «sí» y un «no» | Lo que la regla ataja es el «ok, pero…», el silencio y el «me parece bien»: son esos los casos |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si la lista entra a `base/` como regla nueva del capítulo de flujo, o como documento del capítulo sin ser regla | Usuario | Pendiente |
| 2 | Si en esta fase el procedimiento del director pasa a enlazar la lista, o eso queda para otra | Usuario | Pendiente |

Las dos bloquean T-01 y T-02. Los CA-02 y CA-03 no dependen de ellas.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La lista existe y dice qué se aprueba en cada punto

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir la lista en `base/` con la forma que decida la duda 1: punto, qué se aprueba y qué habilita | `base/02-flujo-de-trabajo/` | 2,5 |
| T-02 | Escribir el incremento en la especificación del módulo | `documentos-modelo/spec.md` | 1,5 |
| T-03 | Caso de prueba: alguien que no participó dice, leyendo solo la lista, qué falta aprobar para poder implementar | `plan_pruebas.md` | 1,5 |

### CA-02 — Una respuesta ambigua no habilita

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: con «ok, pero…», con silencio y con «me parece bien», el trabajo no arranca | `plan_pruebas.md` | 2,0 |

### CA-03 — Aprobar una cosa no aprueba la siguiente

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: aprobado el plan, el guardado se pide aparte; aprobado un cambio, el commit se pide aparte | `plan_pruebas.md` | 2,0 |

### RNF — Que la lista no repita lo que ya dicen las reglas

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Comprobar que la lista enlaza `00·N2`, `01·C17` y `02·F4` en vez de copiarlas | Sin texto prestado | 1,0 |
| T-07 | Versionar si tocó `base/`, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 7 tareas · 12,5 horas.**

---

## 4. Secuencia de ejecución

T-04 → T-05 primero: prueban reglas que ya existen. T-01 → T-02 → T-03 → T-06 con las dudas resueltas. T-07 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Lectura por alguien ajeno, que responde qué falta aprobar | T-03 |
| CA-02 | Tres respuestas ambiguas, una por caso | T-04 |
| CA-03 | Dos aprobaciones consecutivas pedidas aparte | T-05 |
| RNF | Revisión de que la lista enlaza y no copia | T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio. Las pruebas de conducta se hacen sobre un cambio de mentira en carpeta temporal: lo que se comprueba es que **no** se ejecute. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase: saca la lista, la entrada del registro y la subida de `VERSION`, todo junto.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Se asume que el estándar está en producción. Si la lista solo reúne puntos que ya regían, la subida es **MENOR**: nadie tiene que hacer algo nuevo. Si al escribirla aparece un punto que hoy no se pide, es **MAYOR** y se declara así.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N1`](../../../../../base/00-nucleo-blindado.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md), [`01·C17`](../../../../../base/01-conducta.md), [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F15`](../../../../../base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean el CA-01 | Se presentan al usuario: escribir en `base/` sube versión | Abierto |
| R-01 | Que queden dos listas, la de `base/` y la del director | Dos verdades sobre lo mismo | Es la duda 2, y por eso se pregunta antes de escribir | Abierto |
| R-02 | Que al escribirla aparezca un punto de aprobación que hoy no se pide | Cambia el tipo de subida a MAYOR | Se declara y se decide antes de cerrar | Abierto |
| R-03 | Que la prueba del CA-02 se lea como que el agente puede juzgar la intención | Riesgo de dar por aprobado un «bueno…» | La lista dice qué **no** cuenta como aprobación, con los tres casos escritos | Abierto |

---

## 11. Definition of Done

- [ ] La lista de puntos de aprobación existe en la capa que se hereda.
- [ ] Alguien ajeno pudo decir qué falta aprobar leyendo solo la lista.
- [ ] Está probado que una respuesta ambigua no habilita.
- [ ] Está probado que aprobar una cosa no aprueba la siguiente.
- [ ] La lista enlaza las reglas que la sostienen, sin copiarlas.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida, si tocó `base/`.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
