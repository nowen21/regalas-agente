# HU-002 · El estándar tiene su guía de diseño de pantallas

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema](../epica.md) |
| **Módulo / Componente** | El capítulo `17` del estándar, en la base de Cimiento |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien construye o arregla una pantalla de cualquier proyecto
- **Quiero** una guía que diga qué componente usar, cuándo y cómo, aprovechando la plantilla instalada
- **Para** no inventar cada pantalla por separado ni depender de que alguien diga «haga esto»

---

## 3. Contexto y descripción

El estándar no tiene guía de diseño de pantallas, y `17·I5` pide usar la plantilla instalada antes de crear nada. Sale del [análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), punto 4 de «Lo que se tiene que hacer», y del encargo [`prompts/prompt-guia-estilo.md`](../../../../prompts/prompt-guia-estilo.md).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La guía es un documento único del estándar y rige igual para todos (acuerdo 1) |
| RN-02 | Cubre las 14 secciones del encargo (acuerdo 1) |
| RN-03 | Cada sección dice qué se exige, sin atarse a una librería, y cómo se hace con la plantilla instalada; Tabler es el ejemplo porque es la de Cimiento (acuerdo 3) |
| RN-04 | No repite lo que ya dicen las reglas `17·I1` a `17·I7`: las enlaza y desarrolla el cómo (`20·M2`) |
| RN-05 | Se propone y se aprueba en la pantalla (análisis 1 del pendiente 132, acuerdo 3) |

### 3.2 Supuestos

- Cimiento usa Tabler 1.6.1, con sus librerías instaladas.

### 3.3 Fuera de alcance

- Arreglar las pantallas de Cimiento (HU-003 a HU-006).

---

## 4. Criterios de aceptación

### CA-01 · La guía cubre el encargo

**Sale de:** análisis 1 del pendiente 137, punto 4

```gherkin
Dado el estándar en la base
Cuando se lee la guía de diseño de pantallas
Entonces trae las 14 secciones del encargo
Y el capítulo 17 la enlaza
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_guia` → resultado esperado: el caso pasa.

### CA-02 · La plantilla instalada va primero

**Sale de:** acuerdo 3

```gherkin
Dado la guía
Cuando se lee una sección de componentes
Entonces dice qué se exige y con qué recurso de la plantilla instalada se hace en Tabler
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_guia` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | La guía se escribe para quien no sabe del tema (`00·ID7`) |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| Encargo | [`prompts/prompt-guia-estilo.md`](../../../../prompts/prompt-guia-estilo.md) |
| Inspiración | tabler.io/admin-template y adminlte.io/themes/v4 |

---

## 7. Tareas técnicas derivadas

- [ ] Redactar la guía y el enlace desde el capítulo 17, y proponerlos.
- [ ] Prueba que lee la guía aprobada.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-028-HU-002-la-guia` |  | (vacío) | [plan_trabajo.md](A-EP-028-HU-002-la-guia/plan_trabajo.md) | [plan_pruebas.md](A-EP-028-HU-002-la-guia/plan_pruebas.md) | [resultado_pruebas.md](A-EP-028-HU-002-la-guia/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001 | Terminada |
| Dependencia | La aprobación del usuario en «Propuestas» | Sin ella, la fase no cierra |

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
| **V**aliosa | Sí | Ninguna pantalla se inventa por separado |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Prueba de Django sobre el estándar en la base |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 137 |
