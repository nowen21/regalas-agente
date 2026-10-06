# HU-023 · El análisis se prende desde un turno anterior


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-023 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/enganches/analisis_en_curso.py`, `proyectos/cimiento/core/proyectos/` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien analiza un pendiente con el agente
- **Quiero** prender el análisis desde un turno que ya pasó, y que su estado viva en la base de Cimiento
- **Para** no perder lo que se habló antes de prenderlo, y no editar a mano el archivo del estado

---

## 3. Contexto y descripción

El 2026-10-05 el análisis 3 del pendiente 119 se prendió tarde y hubo que editar a mano `historico-chat/.estado/analisis-en-curso/«sesión».txt` para que la conversación entrara desde el principio ([análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdos 3 y 4, punto 10).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | «Analicemos: el pendiente N desde el turno T» prende el análisis con la conversación desde el turno T. Si ya estaba prendido, lo corre hasta T | Acuerdo 4 |
| RN-02 | T va de 1 al turno actual; uno fuera de ese rango se rechaza y se dice | Propuesta del agente |
| RN-03 | El estado del análisis prendido de un proyecto registrado vive en la base de Cimiento, una fila por sesión | Acuerdo 3 |
| RN-04 | Si el proyecto no está registrado o la base no responde, el estado sigue en su archivo: pasar la conversación no se cae nunca | Propuesta del agente (el histórico no se suspende, acuerdo 5) |
| RN-05 | Un estado que quedó en archivo pasa solo a la base en la siguiente lectura, y el archivo se borra | Acuerdo 3 |

### 3.2 Supuestos

- La base de Cimiento corre con la migración de esta HU.

### 3.3 Fuera de alcance

- Que el freno lea el estado de su propia sesión: es la fila 11 del análisis, en la HU-024.

---

## 4. Criterios de aceptación

### CA-01 · Prender desde un turno anterior

**Sale de:** análisis 3 del pendiente 119, punto 10.

```gherkin
Dado una conversación en el turno 12
Cuando el usuario escribe «Analicemos: el pendiente 7 desde el turno 4»
Entonces el análisis queda prendido desde el turno 4
Y si ya estaba prendido desde el 10, pasa a estar desde el 4
Y «desde el turno 20» se rechaza con el motivo
```

**Cómo validarlo:**
1. Correr `python -m unittest core.enganches.tests_analisis_desde` desde `proyectos/cimiento/` → pasan los casos de prender.

**Aprobado cuando:** el estado guarda el turno pedido.

### CA-02 · El estado vive en la base

**Sale de:** análisis 3 del pendiente 119, punto 10.

```gherkin
Dado un proyecto registrado en Cimiento
Cuando se prende, se pausa o se apaga un análisis
Entonces la fila de su sesión en la base cambia, y no se escribe archivo
Y un estado que estaba en archivo pasa a la base y el archivo se borra
Y un proyecto sin registro sigue con su archivo
```

**Cómo validarlo:**
1. Correr `python manage.py test core.proyectos.tests_analisis_prendido` → pasan los casos de la base.

**Aprobado cuando:** la tabla tiene la fila y el archivo no existe.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Disponibilidad** | Sin base, la conversación sigue pasando al análisis |

---

## 6. Diseño y referencias

Documento funcional: [análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdos 3 y 4. Modelo de datos: tabla nueva `proyectos_analisisprendido`.

---

## 7. Tareas técnicas derivadas

- [x] «desde el turno T».
- [x] El modelo, su migración y el estado en la base.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-023-desde-un-turno-y-en-la-base` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-023-desde-un-turno-y-en-la-base/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-023-desde-un-turno-y-en-la-base/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-023-desde-un-turno-y-en-la-base/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que sin base deje de pasar la conversación | Sin base sigue en archivo |
| Riesgo | Que las pruebas escriban en la base real | Solo usa la base un proyecto registrado; las pruebas usan carpetas temporales sin registro |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 3 del pendiente 119 |
