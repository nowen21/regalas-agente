# HU-006 · Las reglas de cada proyecto viven en la misma tabla

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-027 · Las reglas del estándar viven en tablas con la estructura del molde](../epica.md) |
| **Módulo / Componente** | Historia, estándar en la base, enganches, validadores, instalador y la plantilla `CLAUDE.md` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra los proyectos desde Cimiento
- **Quiero** que las reglas propias de cada proyecto vivan en la misma tabla que las del estándar
- **Para** verlas, cambiarlas y versionarlas en un solo sitio, y que el agente de cada proyecto las reciba de ahí

---

## 3. Contexto y descripción

Cinco proyectos registrados tienen reglas propias en `.agente/reglas-proyecto.md`, dentro de su repositorio: AgroSystem (56), dp_card (1), Gestión de Servicios Tecnológicos (7), LocalHub (10) y RNI (5). El agente las lee porque la plantilla `CLAUDE.md` se lo ordena (punto 4). Sale del [análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), acuerdo 1, y de la decisión del usuario del 2026-10-07 («Apruebo las recomendaciones» y «apruebo»): las reglas pasan a la tabla y el archivo se borra.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada regla de un proyecto queda en la tabla de reglas, marcada con su proyecto, con las mismas casillas que las del estándar |
| RN-02 | Una regla de un proyecto se escribe con `##` o con `###`; las dos formas se leen |
| RN-03 | La sección donde estaba la regla queda en su casilla «grupo» |
| RN-04 | El archivo entero queda en la historia del proyecto antes de borrarlo: nada se pierde |
| RN-05 | Un cambio de una regla de un proyecto sube la versión de ese proyecto, no la del estándar |
| RN-06 | El agente de un proyecto registrado recibe al abrir la sesión el índice de sus reglas, y lee cada una con un comando de Cimiento |
| RN-07 | Lo que una regla del proyecto autoriza escribir sale de la tabla |
| RN-08 | El proyecto que Cimiento no tiene registrado sigue con su archivo |
| RN-09 | La plantilla `CLAUDE.md` dice dónde viven las reglas del proyecto; es un cambio MAYOR del estándar |

### 3.2 Supuestos

- Los cinco proyectos están registrados y activos en Cimiento.

### 3.3 Fuera de alcance

- Hacer commit en los repositorios de los proyectos: lo aprueba el usuario en cada uno.

---

## 4. Criterios de aceptación

### CA-01 · La regla del proyecto versiona su proyecto

**Sale de:** RN-05

```gherkin
Dado una regla de un proyecto
Cuando se guarda
Entonces sube la versión de ese proyecto y no la del estándar
```

**Cómo validarlo:** correr `manage.py test core.historia.tests_regla_del_proyecto` → resultado esperado: el caso pasa.

### CA-02 · Las reglas del proyecto pasan a la tabla sin perder nada

**Sale de:** acuerdo 1 del análisis 1 del pendiente 136; RN-01 a RN-04

```gherkin
Dado un proyecto con su archivo de reglas, con reglas en ## o en ###
Cuando se pasan a la tabla
Entonces cada regla queda con su proyecto, sus casillas y su grupo
Y el archivo entero queda en la historia del proyecto, y se borra
Y se ven y se cambian en Cimiento
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_reglas_del_proyecto` → resultado esperado: los casos pasan.

### CA-03 · El agente del proyecto las recibe de la base

**Sale de:** RN-06, RN-07

```gherkin
Dado un proyecto registrado con reglas en la tabla
Cuando se abre una sesión en ese proyecto
Entonces llega el índice de sus reglas con el comando para leer cada una
Y el freno deja escribir lo que esas reglas autorizan
```

**Cómo validarlo:** correr `manage.py test core.enganches.tests_reglas_del_proyecto` → resultado esperado: los casos pasan.

### CA-04 · El validador del catálogo lee la tabla

**Sale de:** RN-07; `20·M16`

```gherkin
Dado un proyecto registrado con reglas en la tabla
Cuando corre el validador del catálogo del proyecto
Entonces revisa las reglas de la tabla, sin pedir el archivo
```

**Cómo validarlo:** correr `manage.py test core.validadores.tests_catalogo_en_base` → resultado esperado: los casos pasan.

### CA-05 · La plantilla y el instalador dicen dónde viven

**Sale de:** RN-08, RN-09

```gherkin
Dado el estándar con la plantilla CLAUDE.md cambiada
Cuando se instala o se pone al día un proyecto registrado
Entonces su CLAUDE.md dice que sus reglas viven en Cimiento
Y el instalador no crea el archivo de reglas en un proyecto registrado
```

**Cómo validarlo:** correr `manage.py test core.herramientas.tests_reglas_en_cimiento` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | El índice de reglas al abrir la sesión es una consulta |
| RNF-02 | **Auditoría** | El paso queda en la historia, en una versión por proyecto |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| Modelo de datos afectado | `estandar_regla` (casilla «grupo») |

---

## 7. Tareas técnicas derivadas

- [ ] Fase A, `core/historia/`: la versión de la regla del proyecto.
- [ ] Fase B, `core/estandar/`: leer las reglas del proyecto, la casilla «grupo», los comandos y la pantalla.
- [ ] Fase C, `core/enganches/` y su adaptador: el índice al abrir la sesión y lo que autorizan.
- [ ] Fase D, `core/validadores/`: el catálogo desde la tabla.
- [ ] Fase E, `core/herramientas/` y la plantilla: el instalador, el `CLAUDE.md` y el paso de los cinco proyectos.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-027-HU-006-version-del-proyecto` | CA-01 | (vacío) | [plan_trabajo.md](A-EP-027-HU-006-version-del-proyecto/plan_trabajo.md) | [plan_pruebas.md](A-EP-027-HU-006-version-del-proyecto/plan_pruebas.md) | [resultado_pruebas.md](A-EP-027-HU-006-version-del-proyecto/resultado_pruebas.md) | Terminada |
| `B-EP-027-HU-006-reglas-en-la-tabla` | CA-02 | CA-01 | [plan_trabajo.md](B-EP-027-HU-006-reglas-en-la-tabla/plan_trabajo.md) | [plan_pruebas.md](B-EP-027-HU-006-reglas-en-la-tabla/plan_pruebas.md) | [resultado_pruebas.md](B-EP-027-HU-006-reglas-en-la-tabla/resultado_pruebas.md) | Terminada |
| `C-EP-027-HU-006-el-agente-las-recibe` | CA-03 | CA-02 | [plan_trabajo.md](C-EP-027-HU-006-el-agente-las-recibe/plan_trabajo.md) | [plan_pruebas.md](C-EP-027-HU-006-el-agente-las-recibe/plan_pruebas.md) | [resultado_pruebas.md](C-EP-027-HU-006-el-agente-las-recibe/resultado_pruebas.md) | Terminada |
| `D-EP-027-HU-006-el-catalogo` | CA-04 | CA-02 | [plan_trabajo.md](D-EP-027-HU-006-el-catalogo/plan_trabajo.md) | [plan_pruebas.md](D-EP-027-HU-006-el-catalogo/plan_pruebas.md) | [resultado_pruebas.md](D-EP-027-HU-006-el-catalogo/resultado_pruebas.md) | Terminada |
| `E-EP-027-HU-006-la-plantilla-y-el-paso` | CA-05 | CA-03 | [plan_trabajo.md](E-EP-027-HU-006-la-plantilla-y-el-paso/plan_trabajo.md) | [plan_pruebas.md](E-EP-027-HU-006-la-plantilla-y-el-paso/plan_pruebas.md) | [resultado_pruebas.md](E-EP-027-HU-006-la-plantilla-y-el-paso/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001 a HU-003 | Terminadas |
| Riesgo | Si el archivo se borra antes de que el agente reciba las reglas de la base, el proyecto trabaja sin ellas | El archivo se borra al final, en la fase E |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Las reglas de todos en un solo sitio |
| **E**stimable | Sí | |
| **S**mall (pequeña) | No | Cinco fases, una por módulo |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 136 y las decisiones del usuario del 2026-10-07 |
