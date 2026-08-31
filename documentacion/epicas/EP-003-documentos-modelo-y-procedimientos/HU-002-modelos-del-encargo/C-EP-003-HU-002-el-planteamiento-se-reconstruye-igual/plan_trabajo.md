# Plan de Trabajo — Fase C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual` |
| **Épica** | `EP-003` Documentos modelo y procedimientos |
| **HU** | `HU-002` Modelos del encargo — **una sola** (`F12.1`) |
| **Módulo** | Documentos modelo ([`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)) |
| **Especificación del módulo** | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../../epica.md) §5.1 y §5.4 fila 10 ([`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)) |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` (repositorio del estándar, sin ramas de fase) |

**ORIGEN** (1 de 3, o híbrido · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- ✨ **Funcionalidad nueva:** el modelo de la necesidad gana el caso que hoy no contempla, el del proyecto que ya está construido. Salió de reconstruir el planteamiento de este mismo repositorio: como el molde no decía nada, el documento se escribió describiendo lo hecho en vez de planteando lo que se necesita, y hubo que rehacerlo dos veces. Queda registrado en el resumen de sesión [2026-08-22 · sesión 2](../../../../../historico-chat/resumenes/2026-08-22/sesion-2.md), hallazgos H-1 y H-2.

**CA de la HU que cubre esta fase** (una sola HU · `02·F12.1` · trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) | ☐ |

---

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el modelo de la necesidad sirva igual para un proyecto que empieza y para uno que ya está construido, sin partirse en dos variantes, y que el documento resultante sea el mismo en los dos casos.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) | Reconstruir el planteamiento de un proyecto ya construido | Funcional | Media |

**Fuera de alcance** (qué explícitamente NO entra en esta fase · cierra expectativas):

- El validador que comprueba que un planteamiento conserva su encuadre. Es comprobación automática, pertenece a EP-004, y queda anotado en el [pendiente 77](../../../../../pendientes/hecho/el-planteamiento-conserva-su-encuadre.md).
- Limpiar las marcas de generación automática que traen los moldes del ciclo. Es trabajo aparte y grande, anotado en el [pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md). Esta fase no agrega marcas nuevas, pero tampoco quita las que ya están en el molde.
- Los otros dos modelos del encargo, el de la épica y el de la historia. El caso del proyecto ya construido también los toca, y se atiende cuando este quede probado.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo verificado el 2026-08-22 contra el repositorio:**

1. [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md) tiene 10 secciones numeradas, un recuadro de instrucciones que manda borrarse, y en la línea 12 el renglón «Encuadre para el agente», que queda fuera de ese recuadro y no dice si se conserva o se reemplaza.
2. Ninguna de las 10 secciones pregunta cómo se levantó la información. La tabla de identificación tiene tres campos: nombre, qué cubre y fecha.
3. El único planteamiento reconstruido que existe hoy es [`prompts/cimiento-planteamiento.md`](../../../../../prompts/cimiento-planteamiento.md), y es el que dejó ver la falla.
4. El molde no lo copia ningún programa: llega a los proyectos por el instalador, que lo copia tal cual. No hay código que dependa de su contenido, solo del nombre del archivo.
5. El encuadre de la línea 12 **copia** la cadena y la copia diverge de la regla: dice «análisis → alcance → épica/HU → especificación → plan aprobado → implementación», y [`02·F0`](../../../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) dice «planteamiento → épica → HU → especificación → plan → código». Otra sesión del 2026-08-22 registró que el molde estaba bien en este punto; no lo está.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/ciclo-vida-proyectos/01-planteamiento.md` | Modificar | Molde | El trabajo de la fase |
| `CHANGELOG.md` | Modificar | Versionado | Entrada de la versión menor (`20·M10`) |
| `VERSION` | Modificar | Versionado | `31.11.0` → `31.12.0` |
| `documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md` | Modificar | Historia | Ya modificado: CA-04, RN-06, RN-07 y la fila de esta fase |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

No aplica. El molde es un documento de texto, no expone contrato de código, y ningún programa lee su contenido.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque la fase no toca código que se sirva por red.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque la fase no introduce interfaz. El molde llega a quien lo usa por el instalador y se abre como archivo.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Un solo molde con instrucciones para los dos casos | Dos moldes, uno por caso | Dos moldes divergen: se corrige uno y el otro queda viejo. Además el resultado debe ser el mismo documento, así que partir el molde sugiere lo contrario |
| La procedencia va en un campo de la identificación | Un párrafo de encuadre que la cuente | Ya se probó el párrafo y fue lo que desplazó al encuadre del molde. Un campo tiene un solo lugar y no compite con nada |
| Las instrucciones de reconstrucción van dentro del recuadro que se borra | Dejarlas en el cuerpo del documento | El recuadro es lo que se borra al llenar. Instrucción que sobrevive al llenado es texto que después hay que limpiar a mano |
| El encuadre se declara texto fijo | Dejarlo como está y confiar en quien llena | Confiar ya falló una vez, en el único planteamiento reconstruido que existe |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | ¿La misma exigencia se extiende ya a los moldes de la épica y de la historia, o se prueba primero en este? | usuario | Resuelta: se prueba primero en este, y queda declarado en §1 como fuera de alcance |

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) — El modelo sirve igual para un proyecto que empieza y para uno que ya existe

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Agregar a la tabla de identificación el campo «Cómo se levantó», con sus dos valores posibles y el espacio para las fuentes | Molde | 0,5 h | — | EV-01 |
| T-02 | Escribir dentro del recuadro de instrucciones el apartado del proyecto ya construido: de dónde se saca la información y qué se hace con ella | Molde | 1 h | T-01 | EV-01 |
| T-03 | Escribir la tabla de traducción, con las cuatro conversiones que hoy fallan, cada una con lo que uno encuentra y lo que va escrito | Molde | 1 h | T-02 | EV-02 |
| T-04 | Escribir la advertencia de que reconstruir es también auditar: lo construido que no cabe en el alcance o choca con un no negociable se anota como hallazgo y lo decide el usuario | Molde | 0,5 h | T-02 | EV-02 |
| T-05 | Declarar el renglón del encuadre como texto fijo que se conserva al llenar, y decirlo donde se dice qué se borra | Molde | 0,5 h | — | EV-03 |
| T-05b | Hacer que el encuadre **enlace** `02·F0` en vez de copiarle la cadena. Hoy copia una versión divergente, y otra sesión de la jornada dio el molde por bueno sin comprobarlo | Molde | 0,5 h | — | EV-03 |
| T-06 | Correr el plan de pruebas de la fase y anotar el resultado | Prueba | 1 h | T-01 a T-05 | EV-04 |
| T-07 | Sumar la entrada al `CHANGELOG.md` y subir `VERSION` a `31.12.0` | Versionado | 0,5 h | T-06 | EV-05 |

**Total estimado:** 5,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-06 → T-07
**Paralelizables:** T-04 y T-05 no dependen de T-03 y pueden ir en cualquier momento después de T-02.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK, no editar por iniciativa.

---

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-04](../HU-002-modelos-del-encargo.md#ca-04--el-modelo-de-la-necesidad-sirve-igual-para-un-proyecto-que-empieza-y-para-uno-que-ya-existe) | Lectura del molde contra los cuatro pasos del CA, más la prueba de reconstrucción con un proyecto real | EV-01 a EV-04 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | El molde con el campo y el apartado nuevos | `plantillas/ciclo-vida-proyectos/01-planteamiento.md` |
| EV-02 | La tabla de traducción y la advertencia de auditoría | El mismo archivo |
| EV-03 | La declaración de que el encuadre no se sustituye | El mismo archivo |
| EV-04 | Resultado de las pruebas de la fase | `resultado_pruebas.md` de esta carpeta |
| EV-05 | Entrada de versión | `CHANGELOG.md` y `VERSION` |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio del estándar, en la máquina del usuario. No hay datos reales de por medio ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) |
| Usuarios de prueba | Ninguno |
| Datos precargados | El planteamiento reconstruido de este repositorio, [`prompts/cimiento-planteamiento.md`](../../../../../prompts/cimiento-planteamiento.md), sirve de caso ya resuelto contra el cual medir el molde |

---

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit de la fase. El molde vuelve a su versión anterior, y `VERSION` con él. No hay dato que migrar ni estado que reconstruir: son cuatro archivos de texto bajo control de versiones.

---

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

El cambio es **aditivo**: agrega un campo y unas instrucciones. Los planteamientos ya escritos en los proyectos instalados siguen siendo válidos y no hay que rehacerlos; les faltará el campo «Cómo se levantó», que se llena la próxima vez que se toquen. Por eso la versión sube en el dígito menor y no en el mayor.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- [`02·F0`](../../../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), porque el cambio del molde entra por la cadena y no desde el hallazgo.
- [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), porque no se toca el molde hasta que este plan y su plan de pruebas estén aprobados.
- [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), por los cuatro archivos de §2.1.
- [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), porque lo que se escriba en el molde se relee contra la lista de marcas antes de entregarlo.
- `20·M10`, porque el cambio de `plantillas/` suma entrada en el `CHANGELOG.md` y sube `VERSION`.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que las instrucciones nuevas alarguen tanto el recuadro que nadie lo lea | El molde queda peor que antes | Las instrucciones van en tabla, no en prosa, y el apartado no pasa de media pantalla | Abierto |
| R-02 | Que el campo «Cómo se levantó» se llene con una palabra y nadie escriba las fuentes | La procedencia se pierde igual que antes | El campo pide las dos cosas en su marca de espacio por llenar: el caso y de dónde salió | Abierto |
| R-03 | Que el molde se corrija y los otros dos del encargo queden desparejos | Un encargo con tres modelos que no se parecen | Declarado en §1 como fuera de alcance, con la HU que lo retoma | Abierto |

---

## 11. Definition of Done

- [ ] El CA-04 verificado con evidencia (§5)
- [ ] Pruebas de la fase en verde ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Trazabilidad HU → fase escrita en los dos lados ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))
- [ ] El molde releído contra la lista de marcas de `00·ID8`, sin sumar marcas nuevas
- [ ] `CHANGELOG.md` con su entrada y `VERSION` en `31.12.0`
- [ ] Señales registradas ([`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md))
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

No aplica: el trabajo lo lleva una sola persona y el avance vive en el `estado-fase.md`.

---

## 13. Cierre

**No se escribe acá.** El cierre de la fase vive en el `funcionalidad_implementada.md`: qué se hizo de cada tarea (§2.2), qué se probó (§3), qué se decidió (§5) y qué deuda quedó (§6). Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
