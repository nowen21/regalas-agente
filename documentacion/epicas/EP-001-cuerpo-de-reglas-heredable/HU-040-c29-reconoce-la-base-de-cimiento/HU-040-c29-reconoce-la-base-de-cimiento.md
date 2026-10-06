# HU-040 · `01·C29` reconoce la base de Cimiento como parte del proyecto

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-040 |
| **Épica / Feature** | [EP-001 — Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Capítulo `01 · Conducta de la IA`, regla `C29` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | En prueba |

---

## 2. Narrativa

- **Como** dueño del estándar
- **Quiero** que `01·C29` cuente la base de Cimiento como parte del proyecto
- **Para** guardar ahí lo que Claude Code deja afuera, sin incumplir la regla

---

## 3. Contexto y descripción

Leer el gasto de afuera incumple `01·C29`, y guardarlo en la base no estaba previsto por la regla. Sale del [análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdo 5: Claude Code escribe los `.jsonl` en `~/.claude/projects/`, no deja cambiar ese lugar sin mover toda su configuración y los borra a los 30 días. Por eso el vigilante los guarda en la base de Cimiento en cuanto cambian, y la regla tiene que reconocer esa base.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo del agente o del proyecto vive en el repositorio o en la base de Cimiento, y a su contenido se llega por un enlace o por Cimiento |
| RN-02 | Lo que la herramienta guarda afuera y no se puede corregir en su origen se trae a la base en el momento en que aparece; después se lee solo de la base |
| RN-03 | Lo que entra a la base pasa antes por el tapado de claves de `00·N6` |

### 3.2 Supuestos

- La base de Cimiento es la MariaDB que ya usa Cimiento, con su respaldo propio.

### 3.3 Fuera de alcance

- Construir el guardado de los `.jsonl` en la base: es EP-025·HU-025.
- Cambiar `04·S9`, que cubre lo que escribe el agente.

---

## 4. Criterios de aceptación

### CA-01 · La regla nombra la base de Cimiento

**Sale de:** análisis 1 del pendiente 124, punto 12 de «Lo que se tiene que hacer»

```gherkin
Dado que algo del proyecto lo guarda la herramienta afuera y no se puede corregir en su origen
Cuando se lee `01·C29`
Entonces la regla dice que se trae a la base de Cimiento en cuanto aparece
Y que después se lee solo de la base
```

**Cómo validarlo:**
1. Abrir `base/01-conducta.md` y buscar `## C29`.
2. Leer el cuerpo de la regla → resultado esperado: dice «repositorio o base de Cimiento» y la salida de RN-02, con una sola exigencia.
3. Leer su ejemplo → resultado esperado: un INCORRECTO y un CORRECTO sobre el `.jsonl`.
Aprobado cuando el cuerpo y el ejemplo dicen lo de RN-01 y RN-02.

### CA-02 · La regla pasa sus comprobaciones

**Sale de:** análisis 1 del pendiente 124, punto 12 de «Lo que se tiene que hacer»

```gherkin
Dado que `01·C29` cambió
Cuando se corren los validadores del estándar
Entonces no dan fallas
Y la regla tiene su checklist vuelto a aplicar, el CHANGELOG y la versión nueva
```

**Cómo validarlo:**
1. En la raíz del repositorio, correr `python validadores/validar.py metareglas` → resultado esperado: sin fallas.
2. Correr `python validadores/validar.py estandar` → resultado esperado: sin fallas.
3. Abrir `CHANGELOG.md` y `VERSION` → resultado esperado: una entrada MENOR que nombra `01·C29` y la versión subida.
Aprobado cuando los tres pasos dan lo esperado.

### Criterios de aceptación transversales

- [x] No regresión: `01·C19` y `04·S9` siguen diciendo lo suyo; `C29` las sigue enlazando.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | La regla cita el acuerdo del que sale |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] Reescribir el cuerpo y el ejemplo de `01·C29`.
- [x] Volver a aplicar su checklist.
- [x] CHANGELOG y VERSION, MENOR (`20·M10`).

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-001-HU-040-c29-nombra-la-base-de-cimiento`](A-EP-001-HU-040-c29-nombra-la-base-de-cimiento/) | CA-01, CA-02 | | [plan_trabajo](A-EP-001-HU-040-c29-nombra-la-base-de-cimiento/plan_trabajo.md) | [plan_pruebas](A-EP-001-HU-040-c29-nombra-la-base-de-cimiento/plan_pruebas.md) | [resultado](A-EP-001-HU-040-c29-nombra-la-base-de-cimiento/resultado_pruebas.md) · **Cumple** | Cumple, falta el commit |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que «la base» se lea como permiso para guardar afuera cualquier cosa | La regla nombra solo la base de Cimiento y solo para lo que no se corrige en su origen |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Todos los criterios de aceptación verificados
- [x] Documentación actualizada: regla, checklist, CHANGELOG y VERSION

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No depende de otra HU |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Deja guardar el gasto sin incumplir la regla |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Una regla |
| **T**esteable | Sí | Se lee la regla y se corren los validadores |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | El agente | Creación de la HU, desde el análisis 1 del pendiente 124 |
| 2026-10-06 | El agente | Fase `A` con veredicto Cumple: `01·C29` en la versión 55.1.0 |
