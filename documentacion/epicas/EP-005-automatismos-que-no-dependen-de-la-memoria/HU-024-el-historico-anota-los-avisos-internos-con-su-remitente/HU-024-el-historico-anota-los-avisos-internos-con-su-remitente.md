# HU-024 · El histórico anota los avisos internos con su remitente

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-024 |
| **Épica / Feature** | [EP-005 — Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/enganches/historico.py` y `core/herramientas/recuperar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** dueño del estándar
- **Quiero** que los avisos internos de Claude Code queden anotados como «Aviso del sistema», no como mensajes míos
- **Para** que la trazabilidad no ponga en mi boca lo que no escribí

---

## 3. Contexto y descripción

El histórico firma como del usuario los avisos internos. Sale del [análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdo 8: Claude Code entrega por `UserPromptSubmit` sus avisos `<task-notification>` (algo que corría en segundo plano terminó) y `<agent-message` (un agente auxiliar entregó su informe), y el enganche del histórico los anota como «Usuario». Pasó en el turno 2 de la transcripción del 2026-10-05 y en el turno 21 del análisis.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un mensaje que abre con `<task-notification>` o `<agent-message` es un aviso interno |
| RN-02 | El histórico lo anota como «Aviso del sistema», con su hora y sin claves |
| RN-03 | El enganche de reglas no le aplica las reglas del usuario, ni el aviso de `01·C28` |
| RN-04 | No se borra nada de lo ya registrado |

### 3.2 Supuestos

- Claude Code mantiene esas marcas al comienzo de sus avisos.

### 3.3 Fuera de alcance

- Volver a firmar los avisos que ya quedaron anotados como «Usuario».

---

## 4. Criterios de aceptación

### CA-01 · El histórico lo firma como aviso

**Sale de:** análisis 1 del pendiente 124, punto 13 de «Lo que se tiene que hacer»

```gherkin
Dado un mensaje que abre con <task-notification> o <agent-message
Cuando el histórico lo anota
Entonces queda como «Aviso del sistema» y no como «Usuario»
Y un mensaje del usuario sigue quedando como «Usuario»
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `.venv/Scripts/python manage.py test core.enganches.tests_avisos_internos`.
- Aprobado cuando las pruebas pasan.

### CA-02 · Las reglas del usuario no se le aplican

**Sale de:** análisis 1 del pendiente 124, punto 13 de «Lo que se tiene que hacer»

```gherkin
Dado un aviso interno
Cuando el enganche de reglas arma lo que recibe el agente
Entonces no trae reglas ni el aviso de 01·C28
```

**Cómo validarlo:**
1. Correr `manage.py test core.herramientas.tests_avisos_internos`.
- Aprobado cuando las pruebas pasan.

### Criterios de aceptación transversales

- [x] Privacidad: el aviso pasa por el tapado de claves, igual que un mensaje del usuario.
- [x] No regresión: el histórico y el enganche de reglas siguen igual para los mensajes del usuario.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | El aviso queda en la transcripción con su texto y su hora |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdo 8 |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Reconocer el aviso y firmarlo en el histórico.
- [ ] Que el enganche de reglas no le aplique nada.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-024-el-historico-los-firma-como-aviso`](A-EP-005-HU-024-el-historico-los-firma-como-aviso/) | CA-01 | | [plan_trabajo](A-EP-005-HU-024-el-historico-los-firma-como-aviso/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-024-el-historico-los-firma-como-aviso/plan_pruebas.md) | | En curso |
| [`B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos`](B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos/) | CA-02 | CA-01 | [plan_trabajo](B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos/plan_trabajo.md) | [plan_pruebas](B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos/plan_pruebas.md) | | Sin empezar |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Claude Code cambia las marcas de sus avisos | El aviso volvería a anotarse como «Usuario»; las marcas quedan en una sola lista para ajustarlas en un sitio |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Pruebas de las dos fases pasando
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | La trazabilidad deja de atribuir al usuario lo que no escribió |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 124 |
