# HU-027 · El núcleo llega completo, y lo entregado vuelve después de un resumen

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-027 |
| **Épica / Feature** | [EP-005 — Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/herramientas/` y los enganches de `SessionStart` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** dueño del estándar
- **Quiero** que el núcleo esté siempre completo a la vista del agente, también después de que la conversación se resume
- **Para** que la regla que manda sobre todas no se pierda nunca

---

## 3. Contexto y descripción

Sale del [análisis 1 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), acuerdos 4 y 5. El [núcleo](../../../../base/00-nucleo-blindado.md) no llega completo en ningún momento. Y cuando Claude Code resume la conversación, lo que la [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion/HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) ya entregó se pierde, pero su cuenta dice que ya llegó.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El núcleo llega completo al abrir la sesión |
| RN-02 | Después de un resumen (`SessionStart` con origen `compact`) llegan otra vez el núcleo, las de `responder` y las de las tareas ya usadas en la sesión |
| RN-03 | Lo que no cabe en el tope se nombra y llega en la acción siguiente, como en la HU-025 |

### 3.2 Supuestos

- Claude Code corre `SessionStart` con origen `compact` después de resumir (documentación de enganches, consultada el 2026-10-09).

### 3.3 Fuera de alcance

- Decidir qué resume Claude Code.

---

## 4. Criterios de aceptación

### CA-01 · Al abrir la sesión llega el núcleo completo

**Sale de:** análisis 1 del pendiente 133, punto 5 de «Lo que se tiene que hacer»

```gherkin
Dado un proyecto instalado
Cuando se abre una sesión
Entonces el agente recibe el texto completo del núcleo
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### CA-02 · Después de un resumen vuelve lo entregado

**Sale de:** análisis 1 del pendiente 133, punto 5 de «Lo que se tiene que hacer»

```gherkin
Dada una sesión que ya recibió reglas de responder y de cambiar-codigo
Cuando Claude Code resume la conversación
Entonces llegan otra vez el núcleo, las de responder y las de cambiar-codigo
Y lo que no cupo queda pendiente para la acción siguiente
```

**Cómo validarlo:**
1. Correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### Criterios de aceptación transversales

- [ ] No regresión: abrir una sesión sin resumen sigue igual, más el núcleo.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Tamaño** | Lo que entrega cada enganche no pasa del tope de `recuperar.py` |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), acuerdos 4 y 5 |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Entregar el núcleo al abrir la sesión.
- [ ] Volver a entregar lo ya dado después de un resumen.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-027-nucleo-y-resumen`](A-EP-005-HU-027-nucleo-y-resumen/) | CA-01, CA-02 | HU-025 | [plan_trabajo](A-EP-005-HU-027-nucleo-y-resumen/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-027-nucleo-y-resumen/plan_pruebas.md) | [resultado](A-EP-005-HU-027-nucleo-y-resumen/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion/HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) | Lleva la cuenta de lo entregado |
| Riesgo | El núcleo pesa 24 KB y el tope es de unos 8,5 KB | Llega por partes, en la apertura y las acciones siguientes |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Pruebas de las fases pasando
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Depende de la HU-025 |
| **N**egociable | Sí | |
| **V**aliosa | Sí | La regla que manda sobre todas no se pierde |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 1 del pendiente 133 |
