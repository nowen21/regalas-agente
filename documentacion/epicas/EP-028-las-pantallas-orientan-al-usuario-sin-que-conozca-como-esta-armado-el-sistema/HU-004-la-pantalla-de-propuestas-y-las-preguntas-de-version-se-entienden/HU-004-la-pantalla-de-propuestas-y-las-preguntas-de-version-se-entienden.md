# HU-004 · La pantalla de propuestas y las preguntas de versión se entienden

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/estandar/` y `core/historia/templates/historia/_tipo_de_version.html` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien aprueba lo que propone el agente
- **Quiero** ver qué cambia cada propuesta, entender las preguntas de versión y dar el motivo cuando rechazo
- **Para** decidir sin tener que preguntar en el chat qué hacer

---

## 3. Contexto y descripción

«Propuestas» muestra el documento entero sin marcar qué cambió, las preguntas del tipo de versión no se entienden y rechazar no pide motivo. Sale del [análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), puntos 6 y 7, y se hace con los recursos de Tabler y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §5, §8 y §11).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada propuesta muestra qué cambia: lo que se quita y lo que se agrega (guía §11) |
| RN-02 | Rechazar pide el motivo, y queda guardado (guía §11) |
| RN-03 | Las preguntas de versión se escriben para quien no conoce `20·M10`, con su «?» y el tipo que resulta a la vista (guía §5) |
| RN-04 | La pantalla dice para qué sirve y cuál es el paso siguiente (`17·I7`) |
| RN-05 | Con los componentes de Tabler: `card`, `alert`, `badge`, `collapse`, el «?» de ayuda (acuerdo 3) |

### 3.2 Supuestos

- La ayuda por campo de la EP-025·HU-018 está disponible.

### 3.3 Fuera de alcance

- Mostrar las reglas por su nombre en lugar de su ruta (EP-027·HU-005).

---

## 4. Criterios de aceptación

### CA-01 · Se ve qué cambia y rechazar pide el motivo

**Sale de:** análisis 1 del pendiente 137, punto 6

```gherkin
Dado una propuesta que cambia una línea de un documento
Cuando se abre «Propuestas»
Entonces la tarjeta muestra la línea que sale y la que entra
Y rechazar sin motivo no se acepta
Y rechazar con motivo guarda el motivo
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_propuestas_claras` → resultado esperado: el caso pasa.

### CA-02 · Las preguntas de versión se entienden

**Sale de:** punto 7

```gherkin
Dado un formulario que sube una versión
Cuando se abre
Entonces las dos preguntas tienen su «?» con ejemplo
Y la pantalla dice qué tipo de versión resulta de las respuestas
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_propuestas_claras` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Dependencias** | Lo que cambia se calcula con `difflib`, que trae Python |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| Guía | `base/17-guia-de-pantallas.md`, §5, §8 y §11 |
| Modelo de datos afectado | Campo nuevo `motivo_rechazo` en `estandar_propuesta` |

---

## 7. Tareas técnicas derivadas

- [ ] Qué cambia y motivo al rechazar.
- [ ] Preguntas de versión con ayuda.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-028-HU-004-propuestas-claras` |  | (vacío) | [plan_trabajo.md](A-EP-028-HU-004-propuestas-claras/plan_trabajo.md) | [plan_pruebas.md](A-EP-028-HU-004-propuestas-claras/plan_pruebas.md) | [resultado_pruebas.md](A-EP-028-HU-004-propuestas-claras/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-002 | Terminada |

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
| **V**aliosa | Sí | Se aprueba sin preguntar en el chat |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 137 |
