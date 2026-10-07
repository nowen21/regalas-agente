# HU-009 · La pantalla muestra qué reglas llegarían con un mensaje y prende los capítulos opt-in

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-026 · El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/proyectos/`, `core/estandar/` y `core/herramientas/recuperar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra los proyectos en Cimiento
- **Quiero** ver qué reglas le llegarían al agente con un mensaje, y prender o apagar los capítulos opt-in de cada proyecto desde la pantalla
- **Para** saber qué recibe el agente antes de escribirle, y no tener que editar el `CLAUDE.md` de cada proyecto

---

## 3. Contexto y descripción

Hoy los capítulos opt-in (`15`, `16`, `17`, `18`, `19`, `21` y `22`) se leen de la sección 5.1 del `CLAUDE.md` de cada proyecto, y nadie ve qué reglas llegan con un mensaje sino después de mandarlo. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 5, 10 y 11, punto 15 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada capítulo opt-in es un ajuste de las tres capas: el del proyecto, si no el de la configuración de Cimiento, si no el de fábrica, que es `no` (acuerdo 10) |
| RN-02 | Las reglas de un proyecto registrado se eligen con los opt-in de la base, no con su `CLAUDE.md` (acuerdo 5) |
| RN-03 | Un proyecto sin registro, o una base que no responde, sigue con los opt-in de su `CLAUDE.md`: se prefiere ofrecer de más antes que callar una regla que rige |
| RN-04 | Al prepararse la base, cada proyecto registrado pasa a la base los opt-in que dice su `CLAUDE.md`; el que no nombra queda en «sí», porque así regía. Nada cambia el día del paso |
| RN-05 | Cambiar un opt-in sube la versión del proyecto y queda en la historia, como cualquier ajuste (acuerdo 1) |
| RN-06 | La vista previa solo muestra: no guarda nada ni deja historia (acuerdo 21) |

### 3.2 Supuestos

- El proyecto que se mira está registrado en Cimiento.

### 3.3 Fuera de alcance

- Quitar la sección 5.1 de la plantilla del `CLAUDE.md`: sigue sirviendo a los proyectos sin registro.

---

## 4. Criterios de aceptación

### CA-01 · Los opt-in son ajustes del proyecto

**Sale de:** análisis 1 del pendiente 132, punto 15 de «Lo que se tiene que hacer»

```gherkin
Dado un proyecto registrado
Cuando se edita en «Proyectos» y se pone «Sí» en el patrón opt-in 15
Entonces el ajuste queda guardado en el proyecto, con su historia y una versión nueva del proyecto
Y la copia `.agente/configuracion.md` lo lista
```

**Cómo validarlo:** correr `manage.py test core.proyectos.tests_opt_in` → resultado esperado: el caso pasa.

### CA-02 · Las reglas se eligen con los opt-in de la base

**Sale de:** acuerdo 5

```gherkin
Dado un proyecto registrado cuyo CLAUDE.md dice «no» en el 15 y la base dice «sí»
Cuando se piden los capítulos apagados del proyecto
Entonces el 15 no está apagado
Y para una carpeta sin registro se siguen leyendo del CLAUDE.md
```

**Cómo validarlo:** correr `manage.py test core.proyectos.tests_opt_in` → resultado esperado: el caso pasa.

### CA-03 · Lo que dice el CLAUDE.md pasa a la base

**Sale de:** RN-04

```gherkin
Dado un proyecto registrado cuyo CLAUDE.md dice «sí» en el 18
Cuando se pasan los opt-in a la base
Entonces el proyecto queda con el 18 en «sí» en la base
Y el 21, que el CLAUDE.md no nombra, también en «sí»
Y pasarlos otra vez no cambia nada
```

**Cómo validarlo:** correr `manage.py test core.proyectos.tests_opt_in` → resultado esperado: el caso pasa.

### CA-04 · La vista previa

**Sale de:** acuerdo 11

```gherkin
Dado un proyecto registrado
Cuando en «Estándar» → «Vista previa» se elige el proyecto y se escribe un mensaje
Entonces la pantalla muestra el bloque de reglas que le llegaría al agente con ese mensaje
Y la historia no cambia
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_vista_previa` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Leer los opt-in de la base usa la misma conexión de los ajustes: una por mensaje |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Ajustes nuevos en `proyectos_ajustebase` y `proyectos_ajustedelproyecto` |

---

## 7. Tareas técnicas derivadas

- [ ] Los siete opt-in como ajustes.
- [ ] `opt_in_apagados` lee la base.
- [ ] Migración que pasa a la base lo que dice cada `CLAUDE.md`.
- [ ] Pantalla de vista previa.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-009-vista-previa-y-opt-in` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-009-vista-previa-y-opt-in/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-009-vista-previa-y-opt-in/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-009-vista-previa-y-opt-in/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-004 | Terminada |

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
| **V**aliosa | Sí | Se ve qué recibe el agente y los opt-in se manejan sin editar archivos |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
