# HU-007 · Cimiento revisa cada programa de un proyecto

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `core/pruebas/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra los proyectos desde Cimiento
- **Quiero** que la revisión cubra cada programa de un proyecto, como el frente y el servidor
- **Para** que ninguno quede sin revisar mientras la página dice que el proyecto está al día

---

## 3. Contexto y descripción

Cimiento reconoce un solo programa por proyecto: en RNI revisa el frente y deja el servidor. Sale del [análisis 4 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md), punto 3 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cimiento encuentra todos los programas de un proyecto, cada uno con su lenguaje (acuerdo 2) |
| RN-02 | Revisa cada uno con su herramienta, y cada revisión queda aparte con el nombre de su carpeta (acuerdo 2) |
| RN-03 | La fila del proyecto muestra el programa con menos pruebas; el que no se pudo medir cuenta como el de menos (acuerdo 2) |
| RN-04 | El detalle muestra cada programa (acuerdo 2) |
| RN-05 | El instalador pone la herramienta en cada programa (acuerdo 2, con el acuerdo 7 del análisis 1) |

### 3.2 Supuestos

- Un programa dentro de otro Django, Laravel o Angular es parte de ese programa.

### 3.3 Fuera de alcance

- Cambiar la herramienta de cada lenguaje.

---

## 4. Criterios de aceptación

### CA-01 · Cimiento encuentra todos los programas

**Sale de:** análisis 4 del pendiente 141, punto 3

```gherkin
Dado un proyecto con proyectos/front (Angular) y proyectos/back (Python)
Cuando Cimiento busca sus programas
Entonces encuentra los dos, cada uno con su lenguaje
Y un requirements.txt dentro de un programa Django no cuenta como otro programa
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-02 · Cada programa se revisa y se guarda aparte

**Sale de:** punto 3

```gherkin
Dado ese proyecto
Cuando se revisa
Entonces quedan dos revisiones con la misma fecha, una por programa, cada una con su herramienta
Y el instalador pone la herramienta en cada uno
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-03 · La fila muestra el de menos pruebas y el detalle cada uno

**Sale de:** punto 3

```gherkin
Dado un proyecto con un programa de 80% y otro de 30%
Cuando se abre «Revisión de pruebas»
Entonces la fila dice 30%
Y el detalle muestra los dos programas
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Las revisiones de antes siguen viéndose, con el programa vacío |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 4 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md) |
| Modelo de datos afectado | `Revision` gana `programa` |

---

## 7. Tareas técnicas derivadas

- [x] Encontrar todos los programas.
- [x] Revisar y poner la herramienta en cada uno.
- [x] La fila y el detalle.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-007-varios-programas` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-029-HU-007-varios-programas/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-007-varios-programas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-007-varios-programas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La HU-006: sin `interfaz/`, el estándar es un solo programa | Ninguno |

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
| **V**aliosa | Sí | Ningún programa queda sin revisar |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django con la herramienta simulada |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 4 del pendiente 141 |
