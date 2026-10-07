# HU-005 · Cada formulario de Cimiento trae su ayuda

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema](../epica.md) |
| **Módulo / Componente** | Las plantillas de formulario de Cimiento y `core/ayuda/textos.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien llena un formulario de Cimiento
- **Quiero** que cada campo tenga su «?» con una explicación y un ejemplo, y que cada pantalla diga para qué sirve
- **Para** llenarlo sin adivinar

---

## 3. Contexto y descripción

La EP-025·HU-018 pidió ayuda en cada campo y en cada pantalla, pero solo «Configuración» y «Suspensiones» la tienen; los formularios que nacieron después no. Sale del [análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), punto 8, y se hace con la ayuda que ya existe y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §3 y §5).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo campo de un formulario de Cimiento tiene su «?» con texto en `core/ayuda/textos.py` (EP-025·HU-018) |
| RN-02 | Toda pantalla con formulario tiene sus botones de ayuda de pantalla (EP-025·HU-018) |
| RN-03 | Se usa la ayuda que ya existe (`ayuda_campo`, `ayuda_pantalla`), no una nueva (`17·I5`, guía §12) |

### 3.2 Supuestos

- La ayuda de la EP-025·HU-018 funciona.

### 3.3 Fuera de alcance

- Las tablas (HU-006).

---

## 4. Criterios de aceptación

### CA-01 · Cada campo tiene su «?»

**Sale de:** análisis 1 del pendiente 137, punto 8

```gherkin
Dado los formularios de Cimiento
Cuando se abre cada uno
Entonces cada campo tiene su «?» con texto
Y ninguna clave de ayuda queda sin texto
```

**Cómo validarlo:** correr `manage.py test core.ayuda` → resultado esperado: el caso pasa.

### CA-02 · Cada pantalla con formulario dice para qué sirve

**Sale de:** punto 8

```gherkin
Dado una pantalla con formulario
Cuando se abre
Entonces trae el botón «¿Para qué sirve?» con su explicación y un ejemplo
```

**Cómo validarlo:** correr `manage.py test core.ayuda` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | Los textos se escriben para quien no sabe del tema (`00·ID7`) |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| Guía | `base/17-guia-de-pantallas.md`, §3 y §5 |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] El «?» de cada campo y la ayuda de cada pantalla.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-028-HU-005-ayuda-en-formularios` |  | (vacío) | [plan_trabajo.md](A-EP-028-HU-005-ayuda-en-formularios/plan_trabajo.md) | [plan_pruebas.md](A-EP-028-HU-005-ayuda-en-formularios/plan_pruebas.md) | [resultado_pruebas.md](A-EP-028-HU-005-ayuda-en-formularios/resultado_pruebas.md) | Terminada |

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
| **V**aliosa | Sí | Se llena cada formulario sin adivinar |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 137 |
