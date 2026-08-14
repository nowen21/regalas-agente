# Plan de Trabajo — Fase A-EP-004-HU-010-declaracion-y-comprobacion (módulo Programas de comprobación)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-010](../HU-010-convencion-declarada-por-el-proyecto.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que dieron al correrlas, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-010-declaracion-y-comprobacion` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-010 Comprobar el código contra la convención que el proyecto declara](../HU-010-convencion-declarada-por-el-proyecto.md) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay especificación aparte. El entregable son programas de comprobación cuya especificación son los criterios de aceptación de la HU y las cinco reglas de la base que comprueban. Es el mismo caso que la fase `A-EP-001-HU-001-molde-de-regla` y se resuelve igual: la HU hace de especificación |
| **Fecha apertura** | 2026-08-14 |
| **Rama** | `feature/A-EP-004-HU-010-declaracion-y-comprobacion` |

**ORIGEN** (`DOC12`): ✨ **Funcionalidad nueva.** Levanta el diferido §5.3 de la épica, que dejaba en espera las comprobaciones que necesitan que el proyecto declare sus convenciones. Nace del pendiente [pendientes/01-validadores-de-codigo-de-proyecto.md](../../../../../pendientes/01-validadores-de-codigo-de-proyecto.md), que registra estas cinco reglas como lo que falta.

**Por qué una sola fase para los cinco CA.** Los cinco se apoyan en la misma declaración, y ninguno se puede probar sin ella. Partirlos daría cuatro fases que esperan a la primera sin poder ejecutarse, que es lo que `02·F12.10` manda evitar.

**CA de la HU que cubre esta fase** (una sola HU · `02·F12.1` · trazabilidad `DOC11`)

| CA de HU-010 | Qué valida | Estado |
|---|---|---|
| CA-01 | Sin declaración no se comprueba, y se dice qué quedó sin comprobar | Pendiente |
| CA-02 | Un nombre fuera de la convención declarada se reporta | Pendiente |
| CA-03 | Una tabla de dominio sin auditoría se reporta | Pendiente |
| CA-04 | Una entidad inmutable sin estados ni permiso se reporta | Pendiente |
| CA-05 | Un módulo del código sin declarar se reporta | Pendiente |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar corriendo las comprobaciones de `14·EST1`, `14·EST2`, el resto de `03·D1`, `15·IM2` y `15·IM5` contra lo que el proyecto declara, y dejar el formato de esa declaración instalado en los proyectos.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Sin declaración, ningún hallazgo y aviso de lo que no se comprueba | Funcional | Baja |
| CA-02 | Nombre fuera de convención, con respeto por el código heredado | Funcional | Media |
| CA-03 | Auditoría de tabla de dominio, sin tocar las del marco de trabajo | Funcional | Media |
| CA-04 | Estados, campos de anulación y permiso de una entidad inmutable | Funcional | Alta |
| CA-05 | Módulo sin declarar y módulo declarado sin código | Funcional | Media |
| RNF-01 | Todo hallazgo es aviso y ninguna comprobación modifica archivos | No funcional | Baja |

**Fuera de alcance** (qué explícitamente NO entra en esta fase):

- Las cinco reglas escritas en `base/`. Ya existen; esta fase no cambia ninguna norma.
- Llenar la declaración de un proyecto concreto. Eso lo hace el agente al abrir sesión en ese proyecto.
- Renombrar nada de lo que se encuentre. Los programas reportan.
- Las comprobaciones de las otras HU de la épica: F2 y F18 son de HU-004, DOC7 y el formato de enlace son de HU-005, el molde de las reglas es de HU-011 y las marcas de generación automática son de HU-012.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-14. La sesión que abrió esta fase ya escribió una primera versión de casi todos los archivos de §2.1, **sin plan aprobado**. Esa versión vale como línea base verificada, no como trabajo hecho: se revisa contra este plan y se corrige o se descarta lo que no encaje.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/mapeo-nombres.md` | Modificar | Plantilla | Suma la tabla de claves fijas y el vocabulario de cada valor. Ya escrito en la línea base |
| `plantillas/dominio.md` | Modificar | Plantilla | Entidades con tabla, clave natural e inmutable; módulos con carpeta y especificación. Ya escrito en la línea base |
| `plantillas/stack-instalacion.md` | Modificar | Plantilla | Deja dicho que los dos archivos anteriores traen la declaración que leen los validadores |
| `validadores/comun.py` | Modificar | Programa | Lectura de tablas markdown, compartida. Ya escrito en la línea base |
| `validadores/declaracion.py` | Nuevo | Programa | Lee la declaración. No comprueba nada. Ya escrito en la línea base |
| `validadores/estructura.py` | Nuevo | Programa | EST1 y EST2. Ya escrito en la línea base |
| `validadores/entidades.py` | Nuevo | Programa | Resto de D1, IM2 e IM5. Ya escrito en la línea base |
| `validadores/esquema.py` | Modificar | Programa | Suma la lectura de qué tablas crea una migración y con qué columnas. Ya escrito en la línea base |
| `validadores/validar.py` | Modificar | Programa | Subcomandos `declaracion`, `estructura` y `entidades` |
| `validadores/pruebas.py` | Modificar | Pruebas | Casos de esta fase |
| `validadores/README.md` | Modificar | Documentación | Qué comprueba cada programa nuevo |
| `validadores/reglas-validables.md` | Modificar | Documentación | Las cinco reglas pasan de pendientes a hechas |
| `pendientes/01-validadores-de-codigo-de-proyecto.md` | Modificar | Documentación | Se descuentan las cinco reglas de lo que falta |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | Entrada MENOR y subida de versión (`20·M10`) |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/comun.py` | Solo agrega funciones; ninguna existente cambia de firma | Ninguno | No rompe |
| `validadores/esquema.py` | Solo agrega funciones; `validar` y `revisar_esquema` no cambian | `validadores/validar.py` · `validadores/pruebas.py` | No rompen: lo que usan sigue igual |
| `plantillas/mapeo-nombres.md` · `plantillas/dominio.md` | Cambia el contenido de la plantilla, no su ruta | `validadores/instalar.py` | No rompe: las copia sin leerlas |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica: son programas de línea de comandos, sin rutas ni autenticación. La entrada es la carpeta del proyecto y la salida es texto.

### 2.4 Punto de entrada en la UI  ·  `F14` Q7

No aplica porque la fase no introduce interfaz. El punto de entrada es `python validadores/validar.py <subcomando> --raiz <proyecto>`, que es donde ya viven las demás comprobaciones.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La declaración va en los dos archivos que ya existen | Un archivo nuevo, `.agente/convenciones.md` | Un archivo nuevo diría lo mismo que la prosa de `mapeo-nombres.md` y de `dominio.md`. Dos sitios con el mismo dato terminan diciendo cosas distintas |
| La declaración se escribe en tablas markdown | Un archivo de datos aparte, tipo lista de claves y valores | Todo lo que el proyecto llena es markdown, y una persona tiene que poder leerlo y corregirlo sin herramienta |
| Lo no declarado se salta y se avisa | Suponer una convención por defecto | Suponerla es inventar la norma desde el código, que es lo que el criterio prohíbe |
| Todo hallazgo de esta familia es aviso | Marcar falla cuando el incumplimiento es claro | Un nombre puede tener un motivo que el programa no ve, y el riesgo R-01 de la épica es perder la confianza por falsos positivos |
| El proyecto declara qué código queda fuera | Detectar solo el código nuevo por fecha | La fecha del archivo no dice si es heredado, y `14·EST3` ya pone la decisión del lado del proyecto |

> Las decisiones no obvias se registran también como señal (`13·DOC5`).

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Que la HU haga de especificación, como en la fase `A-EP-001-HU-001` | usuario | Pendiente |
| 2 | Si estas comprobaciones entran en la corrida automática o se corren a demanda | usuario | Pendiente |

> Ninguna tarea de construcción inicia con una duda abierta que la bloquee.

---

## 3. Desglose de tareas por criterio de aceptación

> Cada CA se descompone en tareas atómicas. **Depende de** ordena la ejecución; **Ev.** referencia la evidencia de §5.

### CA-01 — Sin declaración no se comprueba, y se dice

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Definir las claves de la declaración y qué se escribe en cada una, en `plantillas/mapeo-nombres.md` | Documentación | 2 h | — | ☐ | |
| T-02 | Definir las tablas de entidades y de módulos en `plantillas/dominio.md` | Documentación | 1 h | T-01 | ☐ | |
| T-03 | Leer tablas markdown por nombre de columna, en `comun.py` | Backend | 2 h | — | ☐ | EV-01 |
| T-04 | Escribir `declaracion.py`: lee y no comprueba | Backend | 2 h | T-01, T-02, T-03 | ☐ | EV-01 |
| T-05 | Reportar como aviso cada clave sin declarar, con la regla que queda sin comprobar | Backend | 1 h | T-04 | ☐ | EV-01 |
| T-06 | Prueba: proyecto sin declaración no produce hallazgos de nombres | Test | 1 h | T-05 | ☐ | EV-01 |

### CA-02 — Un nombre fuera de la convención declarada se reporta

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-07 | Leer de una migración qué tablas crea y con qué columnas, en `esquema.py` | Backend | 3 h | — | ☐ | EV-02 |
| T-08 | Comprobar el caso de tablas, columnas y clases en `estructura.py` | Backend | 3 h | T-04, T-07 | ☐ | EV-02 |
| T-09 | Comprobar sufijo de clave foránea, prefijo de booleano y sufijo de fecha de evento | Backend | 2 h | T-08 | ☐ | EV-02 |
| T-10 | Saltar lo que el proyecto declara como código heredado | Backend | 1 h | T-08 | ☐ | EV-02 |
| T-11 | Prueba: nombre malo se reporta, nombre bueno no, heredado no | Test | 2 h | T-09, T-10 | ☐ | EV-02 |

### CA-03 — Una tabla de dominio sin auditoría se reporta

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-12 | Comprobar columnas de auditoría, o el mecanismo declarado, en `entidades.py` | Backend | 2 h | T-04, T-07 | ☐ | EV-03 |
| T-13 | Comprobar el `UNIQUE` de la clave natural declarada | Backend | 2 h | T-12 | ☐ | EV-03 |
| T-14 | Comprobar el índice de las claves foráneas, sin marcar las que el marco de trabajo indexa solo | Backend | 2 h | T-12 | ☐ | EV-03 |
| T-15 | Prueba: tabla de dominio sin auditoría se reporta; tabla no declarada no | Test | 2 h | T-13, T-14 | ☐ | EV-03 |

### CA-04 — Una entidad inmutable sin estados ni permiso se reporta

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-16 | Comprobar los tres estados declarados en el esquema de la entidad inmutable | Backend | 2 h | T-12 | ☐ | EV-04 |
| T-17 | Comprobar los campos de anulación declarados | Backend | 1 h | T-16 | ☐ | EV-04 |
| T-18 | Buscar el permiso propio de anular en el código, una sola pasada para todas las entidades | Backend | 2 h | T-16 | ☐ | EV-04 |
| T-19 | Prueba: entidad inmutable a la que le falta cada cosa, una por una | Test | 2 h | T-17, T-18 | ☐ | EV-04 |

### CA-05 — Un módulo del código sin declarar se reporta

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-20 | Encontrar los módulos del código según la ruta declarada | Backend | 2 h | T-04 | ☐ | EV-05 |
| T-21 | Comparar contra los módulos declarados, en los dos sentidos | Backend | 2 h | T-20 | ☐ | EV-05 |
| T-22 | Prueba: módulo sin declarar y módulo declarado sin código | Test | 1 h | T-21 | ☐ | EV-05 |

### RNF — Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Estado | Ev. |
|---|---|---|:--:|---|---|
| T-23 | Sumar los tres subcomandos a `validar.py` y decidir si entran en la corrida automática | Usabilidad | 1 h | ☐ | EV-06 |
| T-24 | Comprobar que ninguna de las tres comprobaciones escribe en disco | Seguridad | 1 h | ☐ | EV-06 |
| T-25 | Documentar en `validadores/README.md` qué comprueba cada una | Documentación | 1 h | ☐ | EV-06 |
| T-26 | Pasar las cinco reglas a la lista de hechas en `reglas-validables.md` y descontarlas del pendiente 01 | Documentación | 1 h | ☐ | EV-06 |
| T-27 | Entrada MENOR en `CHANGELOG.md` y subida de `VERSION` (`20·M10`) | Documentación | 1 h | ☐ | EV-06 |

**Total estimado:** 47 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-07 → T-08 → T-12 → T-16 → T-23 → T-27

**Paralelizables:** T-20 y T-21 (módulos) no dependen de T-07; las pruebas de cada CA avanzan apenas su comprobación está.

> Solo se tocan los archivos declarados en §2.1 (`F8`). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK, no editar por iniciativa.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

> Un CA no se marca cumplido sin evidencia. La fase no cierra con algún CA en rojo. El detalle de casos vive en el `plan_pruebas`.

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba automática sobre un proyecto de prueba sin declaración | EV-01 | | ☐ |
| CA-02 | Prueba automática con migraciones sembradas de nombres buenos y malos | EV-02 | | ☐ |
| CA-03 | Prueba automática con tabla de dominio y tabla del marco de trabajo | EV-03 | | ☐ |
| CA-04 | Prueba automática con entidad inmutable incompleta | EV-04 | | ☐ |
| CA-05 | Prueba automática con módulo sin declarar | EV-05 | | ☐ |
| RNF-01 | Corrida completa de la suite y revisión de que no se escribe nada | EV-06 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la suite, casos de declaración | `validadores/pruebas.py` |
| EV-02 | Salida de la suite, casos de convención de nombres | `validadores/pruebas.py` |
| EV-03 | Salida de la suite, casos de tabla de dominio | `validadores/pruebas.py` |
| EV-04 | Salida de la suite, casos de entidad inmutable | `validadores/pruebas.py` |
| EV-05 | Salida de la suite, casos de módulos | `validadores/pruebas.py` |
| EV-06 | Corrida completa de la suite y de los tres subcomandos | Terminal |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales creadas por la propia suite. Nunca datos reales (`00·N4` · `08·T4`) |
| Usuarios de prueba | No aplica: no hay autenticación |
| Datos precargados | Proyectos de prueba armados por la suite: sin declaración, con declaración a medias y completa |

> El detalle completo va en el [plan_pruebas.md](plan_pruebas.md).

---

## 7. Reversión / rollback  ·  `F14` Q11

Todo lo de esta fase es aditivo y no toca datos: se revierte con la reversión del commit. Los archivos nuevos se borran y los modificados vuelven a su versión anterior. Las plantillas cambian de huella, así que la copia local de cada proyecto queda marcada vieja hasta la siguiente corrida del instalador; revertir la deja marcada vieja otra vez, y eso se arregla solo al correrlo.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Aditivo. Un proyecto ya instalado no tiene la declaración: sus comprobaciones nuevas no reportan nada y avisan qué falta por declarar. Nadie queda obligado a llenarla para seguir trabajando, que es lo que hace que el cambio sea MENOR y no MAYOR.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  `F14` Q13

- Base: `02·F2`, `02·F8`, `02·F17`, `03·D1`, `08·T4`, `13·DOC11`, `14·EST1`, `14·EST2`, `14·EST3`, `15·IM2`, `15·IM5`, `20·M3`, `20·M9`, `20·M10`.
- Proyecto: no aplica. Este repositorio es el estándar y no tiene catálogo de reglas propias.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dudas de §2.7 sin responder | Detiene la construcción | Se resuelven al aprobar el plan | Abierto |
| B-02 | La lectura de migraciones solo entiende dos formas de escribirlas | Un proyecto con otra forma no se comprueba | Se declara qué formas se reconocen y se avisa cuando no se reconoce ninguna | Abierto |
| B-03 | Que la línea base ya escrita se dé por buena sin revisarla contra este plan | Entra código que nadie aprobó | Cada tarea revisa lo escrito y lo corrige o lo descarta | Abierto |

---

## 11. Definition of Done

- [ ] Todos los CA de §0 verificados con evidencia (§5)
- [ ] Requisitos no funcionales validados
- [ ] Pruebas de la fase en verde (alcance quirúrgico · `F5`)
- [ ] Trazabilidad especificación → implementación sin faltantes (`DOC11`)
- [ ] Sin errores de linter / análisis estático (`07`)
- [ ] Documentación e índices/mapas del proyecto actualizados (`13`)
- [ ] Señales registradas (`DOC5`)
- [ ] Rama lista para el commit único de la fase (`G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

| Fecha | Tareas cerradas | Avance CA | Bloqueos | Ajuste al plan |
|---|---|---|---|---|
| 2026-08-14 | Ninguna | Sin empezar | Plan sin aprobar | — |

---

## 13. Cierre

**Resultado:** sin ejecutar. **Esfuerzo real vs. estimado:** sin ejecutar.

**Lecciones aprendidas:** se escriben al cerrar.

**Deuda técnica generada:**

| Descripción | Registro / ticket |
|---|---|
| Sin ejecutar | |
