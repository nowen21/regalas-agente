# HU-025 · Las reglas de cada tarea llegan antes de la acción, una sola vez, y nada se repite

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-025 |
| **Épica / Feature** | [EP-005 — Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/herramientas/` y los enganches de `adaptadores/claude-code/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** dueño del estándar
- **Quiero** que al agente le lleguen las reglas de lo que va a hacer, justo antes de hacerlo y una sola vez
- **Para** que ninguna tarea se haga sin sus reglas y ningún mensaje pague reglas que no usa

---

## 3. Contexto y descripción

Sale del [análisis 1 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), acuerdos 1, 2 y 6. Las reglas se eligen solo por la palabra clave del mensaje. Antes de cada acción no llega ninguna, aunque [base/tareas.md](../../../../base/tareas.md) dice qué acción pide cada tarea. Por eso `cambiar-codigo`, `tocar-datos`, `ir-afuera` y `cambiar-estandar`, que no tienen palabra clave, no entregan sus reglas nunca. Y con cada mensaje llegan las mismas listas, seis reglas dos veces y el mismo aviso de las señales.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La tarea de una acción sale de la columna «Acciones que la señalan» de `base/tareas.md` |
| RN-02 | Cada regla se entrega una sola vez por sesión y por agente: el principal y cada subagente llevan su cuenta |
| RN-03 | Lo que no cabe en el tope se nombra, y llega completo en la acción siguiente de la misma tarea |
| RN-04 | Con cada mensaje llegan solo las de `responder`, y las de `recibir-pedido` cuando la palabra clave autoriza cambiar algo; las dos, una sola vez por sesión |
| RN-05 | La regla que el mensaje cita llega siempre, y el aviso de `01·C28` sigue cuando falta la palabra |
| RN-06 | La medición de la respuesta anterior sigue llegando con el mensaje siguiente |
| RN-07 | El aviso de las señales llega una vez, al abrir la sesión |

### 3.2 Supuestos

- Claude Code entrega `session_id` y, en los subagentes, `agent_id` a los enganches de `PreToolUse`, y acepta `additionalContext` sin frenar la acción (documentación de enganches, consultada el 2026-10-09).

### 3.3 Fuera de alcance

- Partir las reglas de `cambiar-codigo`: es la [HU-026](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca/HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md).
- El núcleo completo y lo que vuelve después de un resumen: es la [HU-027](../HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen/HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen.md).

---

## 4. Criterios de aceptación

### CA-01 · Antes de la acción llegan las reglas de su tarea

**Sale de:** análisis 1 del pendiente 133, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dado que el agente va a escribir un archivo .py, a correr un git commit o a escribir en base/
Cuando el enganche de antes de la acción la revisa
Entonces le llegan las reglas de cambiar-codigo, de correr-comando y tocar-git, o de cambiar-estandar
Y la acción no se frena por eso
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### CA-02 · Cada regla llega una sola vez por sesión y por agente

**Sale de:** análisis 1 del pendiente 133, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dado que una regla ya le llegó al agente principal en esta sesión
Cuando otra acción pide la misma tarea
Entonces esa regla no vuelve a llegar
Y lo que no cupo la vez anterior llega ahora
Y un subagente recibe las suyas aparte
```

**Cómo validarlo:**
1. Correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### CA-03 · Con cada mensaje llega solo lo que falta

**Sale de:** análisis 1 del pendiente 133, puntos 2 y 3 de «Lo que se tiene que hacer»

```gherkin
Dado un mensaje que abre con una palabra clave
Cuando el enganche de cada mensaje arma lo que recibe el agente
Entonces trae las reglas de responder que aún no llegaron en la sesión
Y las de recibir-pedido solo si la palabra autoriza cambiar algo y aún no llegaron
Y la regla que el mensaje cita, siempre
Y ya no trae el bloque «LAS REGLAS DE CADA TURNO»
Y la medición de la respuesta anterior sigue llegando
```

**Cómo validarlo:**
1. Correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### CA-04 · El aviso de las señales llega una vez, al abrir la sesión

**Sale de:** análisis 1 del pendiente 133, punto 3 de «Lo que se tiene que hacer»

```gherkin
Dado un proyecto instalado
Cuando se abre una sesión
Entonces el aviso de las señales llega una vez
Y no vuelve a llegar con cada mensaje
```

**Cómo validarlo:**
1. Correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### CA-05 · El estándar dice cuándo llegan las reglas

**Sale de:** análisis 1 del pendiente 133, punto 2 de «Lo que se tiene que hacer», y `20·M10`

```gherkin
Dado base/tareas.md
Cuando se lee cómo se elige la tarea
Entonces dice que la acción trae las reglas de su tarea y que el mensaje trae solo las de responder y recibir-pedido
Y el cambio queda con su versión MENOR y su registro
```

**Cómo validarlo:**
1. Leer `base/tareas.md` con `manage.py ver_estandar base/tareas.md`.
- Aprobado cuando lo dice y la versión subió.

### Criterios de aceptación transversales

- [ ] Rendimiento: cuando todas las reglas de la tarea ya llegaron, el enganche de antes de la acción no lee el estándar.
- [ ] No regresión: el freno sigue decidiendo igual sobre cada acción.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Tamaño** | Lo que entrega cada enganche no pasa del tope de `recuperar.py` |
| RNF-02 | **Robustez** | Si la entrega falla, la acción y el mensaje siguen: el enganche sale con código 0 |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), acuerdos 1, 2 y 6 |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno: lo entregado se guarda en `historico-chat/.estado/`, que no se versiona |

---

## 7. Tareas técnicas derivadas

- [ ] Reconocer la tarea de cada acción y entregar sus reglas una sola vez.
- [ ] Que el mensaje traiga solo lo que falta.
- [ ] Que el aviso de las señales vaya al abrir la sesión.
- [ ] Cambiar `base/tareas.md` y subir la versión.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-025-entrega-por-accion`](A-EP-005-HU-025-entrega-por-accion/) | CA-01 a CA-04 | | [plan_trabajo](A-EP-005-HU-025-entrega-por-accion/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-025-entrega-por-accion/plan_pruebas.md) | [resultado](A-EP-005-HU-025-entrega-por-accion/resultado_pruebas.md) | Cerrada |
| [`B-EP-005-HU-025-el-estandar-lo-dice`](B-EP-005-HU-025-el-estandar-lo-dice/) | CA-05 | Fase A | [plan_trabajo](B-EP-005-HU-025-el-estandar-lo-dice/plan_trabajo.md) | [plan_pruebas](B-EP-005-HU-025-el-estandar-lo-dice/plan_pruebas.md) | [resultado](B-EP-005-HU-025-el-estandar-lo-dice/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Un enganche más antes de cada acción demora cada acción | Si todo ya llegó, sale sin leer el estándar |
| Riesgo | Al resumirse la conversación se pierde lo entregado | Lo cubre la HU-027 |

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
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Cada tarea trae sus reglas, y cada mensaje pesa menos |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 1 del pendiente 133 |
