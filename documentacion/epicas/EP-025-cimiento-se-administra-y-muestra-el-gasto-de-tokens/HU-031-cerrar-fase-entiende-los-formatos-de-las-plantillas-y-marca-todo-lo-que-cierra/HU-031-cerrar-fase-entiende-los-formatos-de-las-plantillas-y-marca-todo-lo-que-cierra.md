# HU-031 · `cerrar_fase` entiende los formatos de las plantillas y marca todo lo que cierra

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-031 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | Herramientas de Cimiento: `core/herramientas/fase.py` |
| **Tipo** | Bug |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien cierra una fase con `cerrar_fase`
- **Quiero** que lea los planes en el formato de sus plantillas y deje marcado todo lo que la fase cierra
- **Para** que el resultado de las pruebas diga todos los casos y nada quede por marcar a mano

---

## 3. Contexto y descripción

`cerrar_fase` solo entiende un caso por fila de la matriz, sin enlace, y los CA del plan como «CA-01 · nombre». Las plantillas piden varios casos por fila, con enlace, filas de RNF y CA sin nombre: 15 de 333 fases tienen filas con varios casos y 160 escriben los CA como enlace. Además, la segunda pasada deja sin marcar la sección 5 del plan y las Definition of Done. Sale del [análisis 1 del pendiente 150](../../../../historico-chat/resumenes/2026-10-09/pendientes/150-cerrar-fase-lee-todos-los-casos-y-marca-todo-lo-que-cierra/analisis-1.md), acuerdos 1 a 3, puntos 1 y 2 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | De cada fila de la matriz se toman todos los casos `CP-NNN`, con enlace o sin él; las filas de RNF cuentan como las de CA (acuerdo 1) |
| RN-02 | Los CA del plan se reconocen como `CA-01 · nombre`, `CA-01` o `[CA-01](…)`; el nombre que falte sale de la HU (acuerdo 1) |
| RN-03 | La segunda pasada marca todas las filas de la matriz, los CA del plan, la sección 5 del plan («Verificado» con la fecha y «Estado») y su Definition of Done (acuerdo 2) |
| RN-04 | Si la HU queda terminada, se marcan sus tareas técnicas y su Definition of Done (acuerdo 2) |
| RN-05 | `reabrir_fase` desmarca lo mismo (acuerdo 2) |
| RN-06 | Las fases ya cerradas no se tocan (acuerdo 3) |

### 3.2 Supuestos

- Los planes siguen las plantillas de `plantillas/ciclo-vida-proyectos/`.

### 3.3 Fuera de alcance

- Marcar las fases ya cerradas.
- Pasar los documentos de la fase a la base: es EP-030·HU-004.

---

## 4. Criterios de aceptación

### CA-01 · Lee los planes en el formato de las plantillas

**Sale de:** análisis 1 del pendiente 150, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado un plan de pruebas con «[CP-001](#…), [CP-002](#…)» en una fila y una fila de RNF
Y un plan de trabajo con los CA como «| CA-01 | ☐ |» y como «| [CA-02](…) | ☐ |»
Cuando se cierra la fase
Entonces el resultado trae todos los casos y todos los CA y RNF
Y los CA sin nombre llevan el de la HU
```

**Cómo validarlo:** correr `manage.py test core.herramientas.tests_fase` → resultado esperado: los casos pasan.

### CA-02 · Marca todo lo que cierra, y reabrir lo desmarca

**Sale de:** punto 2

```gherkin
Dada una fase sin marcas por llenar
Cuando se cierra
Entonces quedan marcadas la matriz, los CA del plan, su sección 5 y su Definition of Done
Y, si la HU queda terminada, sus tareas técnicas y su Definition of Done
Cuando se reabre
Entonces todo eso vuelve a quedar sin marcar
```

**Cómo validarlo:** correr `manage.py test core.herramientas.tests_fase` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Las fases escritas en el formato viejo (un caso por fila, CA con nombre) se siguen cerrando igual |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 150](../../../../historico-chat/resumenes/2026-10-09/pendientes/150-cerrar-fase-lee-todos-los-casos-y-marca-todo-lo-que-cierra/analisis-1.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] Leer la matriz y los CA en el formato de las plantillas.
- [x] Marcar y desmarcar todo lo que cierra.
- [x] Pruebas con el formato de las plantillas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-031-formatos-de-las-plantillas` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-031-formatos-de-las-plantillas/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-031-formatos-de-las-plantillas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-031-formatos-de-las-plantillas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Cambiar cómo cierran las fases que ya usan el formato viejo | Se cubre con el RNF-01 |

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
| **V**aliosa | Sí | El cierre dice la verdad sobre las pruebas |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas sobre una fase de juguete en el formato de las plantillas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 1 del pendiente 150 |
