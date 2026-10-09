# HU-028 · El trabajo de cada mensaje sale de lo que está abierto

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-028 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | El gasto: `core/consumo/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mira el gasto de tokens
- **Quiero** que cada mensaje quede con el trabajo en que se estaba
- **Para** saber cuánto costó cada fase y cada análisis, también en las preguntas y las aprobaciones

---

## 3. Contexto y descripción

El 2026-10-08 el usuario preguntó qué significa «(sin trabajo)» en «Dónde se gasta». De 1.985 mensajes de 7 días, 1.842 (93 %) quedaban así. El trabajo se deducía solo de los archivos que tocaba el turno, y solo se reconocían las fases `A-`: una pregunta, un «Apruebo» o una fase B no tenían trabajo. El usuario aprobó las opciones 1 y 2 de la respuesta: tomar el trabajo de lo que está abierto y reconocer todas las fases.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Si el aviso de cada mensaje dice que la conversación entra a un análisis, ese análisis es el trabajo del mensaje. Manda sobre lo demás |
| RN-02 | Si no, el trabajo es la fase o el análisis que más aparece en los archivos y órdenes de consola del turno. Se reconocen las fases de cualquier letra (`A-`, `B-`, `C-`...) |
| RN-03 | Si el turno no da ninguno, el mensaje sigue en el trabajo del mensaje anterior de la misma conversación |
| RN-04 | Cada mensaje guarda de dónde salió su trabajo: del análisis, de los archivos o de la conversación. El que sigue de la conversación se reemplaza si su turno trae algo propio |
| RN-05 | Los mensajes ya guardados se recalculan con las líneas de sesión que hay en la base |
| RN-06 | Ningún mensaje queda sin trabajo. El que no tiene fase ni análisis por RN-01 a RN-03 queda en su conversación: «Conversación «título»», con el título que Claude Code le pone, o con el comienzo de su código si no tiene título |

### 3.2 Supuestos

- El aviso «[ANÁLISIS EN CURSO]» llega en cada mensaje y queda en el `.jsonl`, después del mensaje.

### 3.3 Fuera de alcance

- Enlazar cada mensaje con su línea de la transcripción (la opción 3).

---

## 4. Criterios de aceptación

### CA-01 · El análisis prendido es el trabajo del mensaje

**Sale de:** RN-01

```gherkin
Dado un mensaje cuyo aviso dice «La conversación entra al análisis pendientes/119-x/analisis-2.md»
Cuando Cimiento lo guarda
Entonces su trabajo es «análisis 2 del pendiente 119», aunque el turno no toque archivos
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_trabajo_abierto` → resultado esperado: los casos pasan.

### CA-02 · Se reconocen todas las fases y las órdenes de consola

**Sale de:** RN-02

```gherkin
Dado un turno que toca la carpeta de la fase B-EP-028-HU-007-x o la nombra en una orden de consola
Cuando Cimiento lo guarda
Entonces su trabajo es esa fase
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_trabajo_abierto` → resultado esperado: los casos pasan.

### CA-03 · El mensaje sin rastro sigue en el trabajo de la conversación

**Sale de:** RN-03, RN-04

```gherkin
Dado un «Apruebo» que no toca archivos, después de un mensaje de la misma conversación con trabajo
Cuando Cimiento lo guarda
Entonces su trabajo es el del mensaje anterior, marcado como que sigue de la conversación
Y si después su turno toca una fase, el trabajo pasa a esa fase
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_trabajo_abierto` → resultado esperado: los casos pasan.

### CA-04 · Lo ya guardado se recalcula

**Sale de:** RN-05

```gherkin
Dado los mensajes guardados antes de este cambio
Cuando se corre manage.py recalcular_trabajo
Entonces cada uno queda con el trabajo que le dan RN-01 a RN-03
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_trabajo_abierto` y la orden en la base real → resultado esperado: los casos pasan y baja la parte «(sin trabajo)».

### CA-05 · Ningún mensaje queda sin trabajo

**Sale de:** orden del usuario del 2026-10-08 («se necesita erradicar esto: (sin trabajo); se tiene que identificar qué lo genera»), RN-06

```gherkin
Dado un mensaje sin análisis prendido, sin fase ni análisis en lo que tocó, y sin un mensaje anterior con trabajo
Cuando Cimiento lo guarda
Entonces su trabajo es «Conversación «título»», con el título de su conversación
Y cuando llega el título, los mensajes que quedaron con el código pasan al título
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_trabajo_abierto` y el diagnóstico en la base real → resultado esperado: los casos pasan y ningún mensaje queda «(sin trabajo)».

### Criterios de aceptación transversales

- [ ] No regresión: `core.consumo` y `core.ayuda` quedan verdes.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Costo** | No se agrega texto a ningún aviso: el trabajo sale de lo que ya queda en el `.jsonl` |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Deducción del trabajo | `core/consumo/trabajo.py` |
| Lectura del `.jsonl` | `core/consumo/lector.py` |
| Modelo afectado | `Pedido`: campo nuevo `origen` |

---

## 7. Tareas técnicas derivadas

- [ ] Leer el aviso del análisis y las órdenes de consola.
- [ ] El origen del trabajo y la herencia en la conversación.
- [ ] La orden que recalcula y la ayuda de la pantalla.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-028-el-trabajo-abierto` | CA-01, CA-02, CA-03, CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-028-el-trabajo-abierto/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-028-el-trabajo-abierto/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-028-el-trabajo-abierto/resultado_pruebas.md) | Terminada |
| `B-EP-025-HU-028-ningun-mensaje-sin-trabajo` | CA-05 | `A-EP-025-HU-028-el-trabajo-abierto` | [plan_trabajo.md](B-EP-025-HU-028-ningun-mensaje-sin-trabajo/plan_trabajo.md) | [plan_pruebas.md](B-EP-025-HU-028-ningun-mensaje-sin-trabajo/plan_pruebas.md) | [resultado_pruebas.md](B-EP-025-HU-028-ningun-mensaje-sin-trabajo/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Una pregunta sobre otro tema queda contada en el trabajo de la conversación | Se ve: el mensaje queda marcado como que sigue de la conversación |

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
| **V**aliosa | Sí | Hoy el 93 % del gasto queda sin trabajo |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Una fase |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde la aprobación del usuario del 2026-10-08 |
