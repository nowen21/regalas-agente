# HU-041 · Las reglas reconocen la base de Cimiento como fuente del estándar

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-041 |
| **Épica / Feature** | [EP-001 — Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Reglas `20·M10` y `01·C19`; `CLAUDE.md`, secciones 2 y 4; nota de la fuente de las reglas; EP-016 |
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
- **Quiero** que las reglas digan que el estándar vive en la base de Cimiento y que todo cambio queda versionado ahí
- **Para** construir la EP-026 sin incumplir las reglas que hoy exigen archivos

---

## 3. Contexto y descripción

`20·M10`, `01·C19`, `CLAUDE.md` y EP-016 dicen que la fuente es el texto. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md): la pantalla de Cimiento es el estándar (acuerdo 2), el estándar deja de escribirse en archivos (acuerdo 15) y todo cambio sube una versión, la del estándar o la del proyecto (acuerdos 1, 12, 13 y 14).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo cambio, por mínimo que sea, sube una versión y queda registrado en la base (acuerdo 1) |
| RN-02 | Un cambio que es solo de un proyecto sube la versión de ese proyecto; un cambio del estándar, hecho o reportado desde un proyecto, sube la del estándar cuando se corrige (acuerdos 12, 13 y 14) |
| RN-03 | El tipo se decide con dos preguntas: ¿un proyecto que hoy cumple deja de cumplir? (`MAYOR`); ¿se agrega algo que nadie está obligado a usar? (`MENOR`); si no, `PARCHE` (acuerdo 7) |
| RN-04 | La memoria del agente pasa a la pantalla (acuerdo 17) |
| RN-05 | Se deroga «la fuente es el texto»: la decisión del 2026-08-18 y la restricción de EP-016 (acuerdo 2) |
| RN-06 | El commit lo hace un botón de la pantalla, aprobado ahí (acuerdos 3 y 22) |

### 3.2 Supuestos

- Mientras se construye la EP-026, `CHANGELOG.md` y `VERSION` siguen al día en archivos; la regla dice desde cuándo rige la base.

### 3.3 Fuera de alcance

- Construir el registro, las versiones y la pantalla: son las HU de EP-026.

---

## 4. Criterios de aceptación

### CA-01 · `20·M10` pone la versión y su registro en la base

**Sale de:** análisis 1 del pendiente 132, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dado que algo cambia en el estándar o en un proyecto
Cuando se lee `20·M10`
Entonces la regla dice que el cambio sube una versión, la del estándar o la del proyecto, y queda registrado en la base de Cimiento
Y que el tipo sale de las dos preguntas de RN-03
```

**Cómo validarlo:**
1. Abrir la regla `M10` en `base/20-meta-reglas/reglas/`.
2. Leer el cuerpo y el ejemplo → resultado esperado: dicen RN-01, RN-02 y RN-03, con una sola exigencia.
Aprobado cuando el cuerpo y el ejemplo dicen lo esperado.

### CA-02 · Lo que decía «la fuente es el texto» queda derogado

**Sale de:** análisis 1 del pendiente 132, punto 3 de «Lo que se tiene que hacer»

```gherkin
Dado que la pantalla es el estándar
Cuando se leen la nota de la fuente de las reglas, EP-016, `01·C19` y `CLAUDE.md`
Entonces ninguno dice que la fuente es el texto
Y cada uno enlaza el análisis 1 del pendiente 132
```

**Cómo validarlo:**
1. Abrir `notas/la-fuente-de-las-reglas-es-el-texto.md` → resultado esperado: marcada como derogada, con el enlace.
2. Abrir `documentacion/epicas/EP-016-…/epica.md`, secciones 7, 10 y 13 → resultado esperado: la restricción derogada, con el enlace.
3. Leer `01·C19` → resultado esperado: la memoria vive en la base de Cimiento.
4. Leer `CLAUDE.md`, secciones 2 y 4 → resultado esperado: versionar y hacer commit se hacen desde la pantalla.
Aprobado cuando los cuatro dan lo esperado.

### CA-03 · Las reglas pasan sus comprobaciones

**Sale de:** `20·M10` y `20·M5`

```gherkin
Dado que `20·M10` y `01·C19` cambiaron
Cuando se corren los validadores del estándar
Entonces no dan fallas
Y cada regla tiene su checklist vuelto a aplicar, el CHANGELOG y la versión nueva
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py metareglas` → resultado esperado: sin fallas.
2. Correr `python validadores/validar.py estandar` → resultado esperado: sin fallas.
3. Abrir `CHANGELOG.md` y `VERSION` → resultado esperado: una entrada `MAYOR` y la versión subida.
Aprobado cuando los tres pasos dan lo esperado.

### Criterios de aceptación transversales

- [x] No regresión: `01·C29` y `04·S9` siguen diciendo lo suyo.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | Cada regla cambiada cita el acuerdo del que sale |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] Reescribir `20·M10` y `01·C19`, y volver a aplicar su checklist.
- [x] Marcar como derogada la nota de la fuente de las reglas y la restricción de EP-016.
- [x] Ajustar `CLAUDE.md`, secciones 2 y 4.
- [x] CHANGELOG y VERSION, `MAYOR`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-001-HU-041-las-reglas-nombran-la-base`](A-EP-001-HU-041-las-reglas-nombran-la-base/) | CA-01, CA-02, CA-03 | | [plan_trabajo](A-EP-001-HU-041-las-reglas-nombran-la-base/plan_trabajo.md) | [plan_pruebas](A-EP-001-HU-041-las-reglas-nombran-la-base/plan_pruebas.md) | [resultado](A-EP-001-HU-041-las-reglas-nombran-la-base/resultado_pruebas.md) · **Cumple** | Cumple, falta el commit |
| `B-EP-001-HU-041-los-totales-del-sello-se-leen` |  | (vacío) | [plan_trabajo.md](B-EP-001-HU-041-los-totales-del-sello-se-leen/plan_trabajo.md) | [plan_pruebas.md](B-EP-001-HU-041-los-totales-del-sello-se-leen/plan_pruebas.md) | [resultado_pruebas.md](B-EP-001-HU-041-los-totales-del-sello-se-leen/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la regla rija antes de que exista la pantalla | La regla dice desde cuándo rige; hasta entonces siguen los archivos |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Todos los criterios de aceptación verificados
- [x] Documentación actualizada: reglas, checklist, CHANGELOG y VERSION

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No depende de otra HU |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Deja construir la EP-026 sin incumplir reglas |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Dos reglas y tres documentos |
| **T**esteable | Sí | Se leen las reglas y se corren los validadores |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
| 2026-10-06 | El agente | Fase `A` con veredicto Cumple: `20·M10` y `01·C19` en la versión 56.0.0 |
