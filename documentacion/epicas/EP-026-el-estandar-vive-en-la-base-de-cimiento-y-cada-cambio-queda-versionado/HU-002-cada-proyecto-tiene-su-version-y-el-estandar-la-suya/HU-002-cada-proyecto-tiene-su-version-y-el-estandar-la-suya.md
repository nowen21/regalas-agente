# HU-002 · Cada proyecto tiene su versión y el estándar la suya

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/historia/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra Cimiento
- **Quiero** que todo cambio de configuración suba una versión, la del proyecto o la del estándar
- **Para** saber en qué versión está cada uno y qué cambió en cada una

---

## 3. Contexto y descripción

No hay versión para lo que cambia en la base. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 1, 7, 12, 13 y 14, puntos 5 y 6 de «Lo que se tiene que hacer», y de `20·M10`.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo cambio de configuración, por mínimo que sea, sube una versión (acuerdo 1) |
| RN-02 | Lo que es solo de un proyecto (su ficha, sus ajustes, sus niveles, sus suspensiones) sube la versión de ese proyecto; lo común a todos (ajustes de capa 1 y el estándar) sube la del estándar (acuerdos 12 y 14) |
| RN-03 | Al guardar, dos preguntas fijan el tipo: ¿un proyecto que hoy cumple deja de cumplir? `MAYOR`; ¿se agrega algo que nadie está obligado a usar? `MENOR`; si no, `PARCHE` (acuerdo 7) |
| RN-04 | Lo que se guarda en un mismo envío es una sola versión |
| RN-05 | La versión del estándar arranca desde la del archivo `VERSION`; la de un proyecto, desde 1.0.0 |
| RN-06 | El estado del análisis y las cuentas tienen historia pero no versión: no son configuración del estándar ni de un proyecto (`20·M10`) |

### 3.2 Supuestos

- La versión que sube por un reporte llega con la HU-008.

### 3.3 Fuera de alcance

- Las tablas del estándar: llegan con la HU-003 y usan lo de esta HU.

---

## 4. Criterios de aceptación

### CA-01 · Un cambio de un proyecto sube su versión, no la del estándar

**Sale de:** análisis 1 del pendiente 132, punto 5 de «Lo que se tiene que hacer»

```gherkin
Dado un proyecto en la versión 1.0.0
Cuando se cambia uno de sus niveles respondiendo «no» a las dos preguntas
Entonces el proyecto queda en 1.0.1, PARCHE, y el cambio apunta a esa versión
Y la versión del estándar no cambia
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: el caso pasa.

### CA-02 · Las dos preguntas fijan el tipo

**Sale de:** análisis 1 del pendiente 132, punto 6 de «Lo que se tiene que hacer»

```gherkin
Dado el formulario de un cambio
Cuando se responde «sí» a la primera pregunta
Entonces sube MAYOR; con «no» y «sí», MENOR; con «no» y «no», PARCHE
Y los formularios de niveles, configuración, proyecto y suspensiones traen las dos preguntas
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: los tres tipos pasan y los formularios muestran las preguntas.

### CA-03 · Un ajuste común sube la versión del estándar

**Sale de:** análisis 1 del pendiente 132, acuerdos 12 y 14

```gherkin
Dado el estándar en la versión del archivo VERSION
Cuando se cambia un ajuste de capa 1
Entonces el estándar sube una versión
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: el caso pasa.

### CA-04 · Las versiones se ven

**Sale de:** análisis 1 del pendiente 132, punto 5 de «Lo que se tiene que hacer»

```gherkin
Dado que hubo cambios en el estándar y en un proyecto
Cuando se abre «Historia» → «Versiones»
Entonces se ve cada versión con su número, tipo, fecha, quién y sus cambios
```

**Cómo validarlo:** abrir `/historia/versiones/` → resultado esperado: lista las versiones.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | Todo cambio de configuración apunta a su versión |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Tabla nueva `historia_version`; columna `version` en `historia_cambio` |

---

## 7. Tareas técnicas derivadas

- [ ] Modelo `Version` y su número por ámbito.
- [ ] Las dos preguntas en los formularios.
- [ ] Pantalla «Versiones».

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-002-las-versiones` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-002-las-versiones/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-002-las-versiones/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-002-las-versiones/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001, el registro de cambios | Terminada |

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
| **I**ndependiente | Sí | Usa la HU-001 ya terminada |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Cada proyecto sabe en qué versión está |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Un modelo y una pantalla |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
