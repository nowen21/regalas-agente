# HU-032 · Cada momento de cada enganche y cada revisión de git se puede suspender desde Cimiento

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-032 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | Las suspensiones (`core/comun`, `core/proyectos`), los enganches (`core/enganches`, `adaptadores/claude-code`) y las revisiones de git (`core/herramientas`) |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz, desde el proyecto scilit |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra un proyecto desde Cimiento
- **Quiero** apagar un tiempo cualquier momento de un enganche o cualquier revisión de git, con motivo y vencimiento
- **Para** que lo que estorba se pueda apagar sin dejar la instalación incompleta ni saltar todas las revisiones con `--no-verify`

---

## 3. Contexto y descripción

Hoy solo el freno se puede suspender. Sale del [análisis 1 del pendiente 149](../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md), acuerdos 1 a 5, puntos 1 a 3 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada momento de un enganche (evento y guion) y cada revisión de git tiene un nombre fijo; los dos del freno se suspenden juntos como «freno» (acuerdo 1) |
| RN-02 | Todos se pueden suspender, el histórico incluido; la pantalla muestra la recomendación de no suspender y el motivo (acuerdo 2) |
| RN-03 | El freno suspendido sigue deteniendo lo que viole el núcleo (acuerdo 2) |
| RN-04 | En cada mensaje, el primero que gana el turno consulta la base y deja la lista; los demás esperan hasta 2 segundos y la leen; la lista vale hasta el mensaje siguiente (acuerdo 3) |
| RN-05 | Si la espera se cumple sin lista, el enganche corre como si nada estuviera suspendido (acuerdo 3) |
| RN-06 | Cada revisión de git suspendida no detiene y dice que está suspendida; en cada guardado se consulta la base una vez (acuerdo 4) |
| RN-07 | Suspensión: motivo, vencimiento de hasta 30 días, y se levanta cuando se quiera (`02·F30`) |

### 3.2 Supuestos

- Claude Code le pasa a cada enganche el nombre del evento (`hook_event_name`) en el JSON de entrada.

### 3.3 Fuera de alcance

- Quitar `--no-verify`: es de git.

---

## 4. Criterios de aceptación

### CA-01 · Cada momento y cada revisión tiene nombre y se suspende desde la pantalla

**Sale de:** análisis 1 del pendiente 149, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado el catálogo de los enganches y de las revisiones de git
Cuando se abre la pantalla de suspensiones de un proyecto
Entonces se puede escoger cualquier momento o revisión, el histórico incluido
Y junto a los que no conviene suspender sale la recomendación y el motivo
Y no se acepta un nombre que no esté en el catálogo
```

**Cómo validarlo:** correr `manage.py test core.proyectos.tests_suspender_enganches` → resultado esperado: los casos pasan.

### CA-02 · El enganche suspendido no hace nada, con una sola consulta por mensaje

**Sale de:** punto 2

```gherkin
Dado un momento suspendido
Cuando arrancan a la vez los enganches de un mensaje
Entonces uno solo consulta la base y los demás leen su lista
Y el suspendido sale sin hacer nada
Y el freno suspendido sigue deteniendo lo que viole el núcleo
```

**Cómo validarlo:** correr `manage.py test core.enganches.tests_suspendidos` → resultado esperado: los casos pasan.

### CA-03 · La revisión de git suspendida no detiene

**Sale de:** punto 3

```gherkin
Dada una revisión de git suspendida
Cuando git corre sus revisiones al guardar
Entonces esa no detiene y dice que está suspendida, con su motivo y su vencimiento
Y las demás corren igual, con una sola consulta a la base por guardado
```

**Cómo validarlo:** correr `manage.py test core.herramientas.tests_validar_suspendida` → resultado esperado: los casos pasan.

### CA-04 · La pantalla de suspensiones va en tres pestañas

**Sale de:** análisis 3 del pendiente 149, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dada la pantalla de suspensiones de un proyecto
Cuando se abre
Entonces muestra tres pestañas, con «Suspensiones» abierta: «Suspensiones», «Reglas» y «Enganches»
Y en «Suspensiones», un botón al principio de la tabla abre el formulario en un modal, que vuelve abierto si hay errores
Y en «Reglas» y en «Enganches», una tabla igual a la de suspensiones
Y el botón solo sale a quien puede cambiar
```

**Cómo validarlo:** correr `manage.py test core.proyectos.tests_suspender_enganches` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Sin nada suspendido, un mensaje hace una sola consulta a la base para saberlo |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 149](../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md) |
| Modelo de datos afectado | `Suspension.nombre` guarda el nombre del momento o de la revisión; sin migración |

---

## 7. Tareas técnicas derivadas

- [x] El catálogo y la pantalla.
- [x] Los enganches leen lo suspendido.
- [x] Las revisiones de git leen lo suspendido.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-032-catalogo-y-pantalla` | CA-01 | (vacío) | [plan_trabajo.md](A-EP-025-HU-032-catalogo-y-pantalla/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-032-catalogo-y-pantalla/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-032-catalogo-y-pantalla/resultado_pruebas.md) | Terminada |
| `B-EP-025-HU-032-enganches-leen-lo-suspendido` | CA-02 | (vacío) | [plan_trabajo.md](B-EP-025-HU-032-enganches-leen-lo-suspendido/plan_trabajo.md) | [plan_pruebas.md](B-EP-025-HU-032-enganches-leen-lo-suspendido/plan_pruebas.md) | [resultado_pruebas.md](B-EP-025-HU-032-enganches-leen-lo-suspendido/resultado_pruebas.md) | Terminada |
| `C-EP-025-HU-032-revisiones-de-git` | CA-03 | (vacío) | [plan_trabajo.md](C-EP-025-HU-032-revisiones-de-git/plan_trabajo.md) | [plan_pruebas.md](C-EP-025-HU-032-revisiones-de-git/plan_pruebas.md) | [resultado_pruebas.md](C-EP-025-HU-032-revisiones-de-git/resultado_pruebas.md) | Terminada |
| `D-EP-025-HU-032-pantalla-en-pestanas` | CA-04 | (vacío) | [plan_trabajo.md](D-EP-025-HU-032-pantalla-en-pestanas/plan_trabajo.md) | [plan_pruebas.md](D-EP-025-HU-032-pantalla-en-pestanas/plan_pruebas.md) | [resultado_pruebas.md](D-EP-025-HU-032-pantalla-en-pestanas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que cada mensaje se demore esperando la lista | Espera de 2 s como máximo, y solo si el que ganó el turno no termina |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Todos los criterios de aceptación verificados
- [x] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Lo que estorba se apaga con registro |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Tres fases, una por módulo |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 1 del pendiente 149 |
| 2026-10-09 | El agente | Se suma el CA-04, del análisis 3 del pendiente 149: la pantalla en tres pestañas |
