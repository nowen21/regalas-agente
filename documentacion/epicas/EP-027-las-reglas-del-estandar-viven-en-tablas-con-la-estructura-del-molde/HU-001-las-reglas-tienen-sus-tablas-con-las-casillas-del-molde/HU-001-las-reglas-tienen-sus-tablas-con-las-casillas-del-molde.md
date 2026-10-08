# HU-001 · Las reglas tienen sus tablas, con las casillas del molde

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-027 · Las reglas del estándar viven en tablas con la estructura del molde](../epica.md) |
| **Módulo / Componente** | Estándar en la base: `core/estandar/` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra el estándar
- **Quiero** que cada regla se guarde en casillas, una por cada parte de su molde
- **Para** que cada pantalla y cada programa tome la parte que necesita sin buscarla dentro del texto

---

## 3. Contexto y descripción

Hoy cada regla es un pedazo del texto de un documento. Sale del [análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), acuerdo 1: las reglas viven en tablas, con las casillas del molde (`20·M5`, `base/20-meta-reglas/estructura-regla.md`).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Las tablas son: capítulo, regla, tarea, la relación de cada regla con sus tareas y la dependencia entre reglas |
| RN-02 | La regla tiene una casilla por parte del molde: código, título, marca, exigencia, excepción (con su condición, límite y quién autoriza), ejemplo (incorrecto y correcto), notas, quién la hace cumplir, validable con su programa, a qué tareas aplica, qué autoriza escribir y sello (resultado, versión, fecha y observación) |
| RN-03 | La marca es una de tres, o ninguna: blindada, opt-in o derogada (`20·M5`) |
| RN-04 | La dependencia es de uno de tres tipos: extiende, depende de o deroga (`20·M7`) |
| RN-05 | «Validable» toma uno de tres valores: no, sí falta el programa, o sí con su programa (`20·M9`, S-346) |
| RN-06 | El código de una regla no se repite dentro del estándar ni dentro de un proyecto (`20·M4`) |
| RN-07 | El texto de una regla se lee en casillas y se vuelve a armar desde ellas con el orden del molde, sin perder ni agregar nada |
| RN-08 | La regla guarda en qué documento vive, para armar su texto en su sitio |

### 3.2 Supuestos

- Las reglas siguen el molde con las variaciones que mide el inventario del 2026-10-07: 24 formas, y 179 de 270 exactamente la del molde.

### 3.3 Fuera de alcance

- Pasar las reglas a las tablas: HU-002.
- Armar el texto que recibe el agente: HU-003.
- Las reglas de cada proyecto: HU-006.

---

## 4. Criterios de aceptación

### CA-01 · Las tablas tienen las casillas del molde

**Sale de:** acuerdo 1 del análisis 1 del pendiente 136

```gherkin
Dado la base de Cimiento
Cuando se aplican las migraciones
Entonces existen las tablas de capítulo, regla, tarea, regla-tarea y dependencia
Y la regla tiene una casilla por parte del molde, con marca, dependencia y validable limitados a sus valores
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_tablas_reglas` → resultado esperado: los casos pasan.

### CA-02 · Una regla se lee en casillas y se vuelve a armar igual

**Sale de:** acuerdo 2 del análisis 1 del pendiente 136

```gherkin
Dado el texto de cualquier regla del estándar
Cuando se lee en casillas y se arma de nuevo
Entonces da el mismo texto, escrito con el orden del molde
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_molde_casillas` → resultado esperado: las 270 reglas dan el mismo texto.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Dependencias** | Leer y armar no usan Django: los enganches los pueden llamar |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| El molde | `base/20-meta-reglas/estructura-regla.md` |
| Modelo de datos afectado | Tablas nuevas: capítulo, regla, tarea, regla-tarea, dependencia |

---

## 7. Tareas técnicas derivadas

- [ ] El lector y el armador del molde.
- [ ] Los modelos y su migración.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-027-HU-001-las-casillas` | CA-01, CA-02 | (vacío) | [plan_trabajo.md](A-EP-027-HU-001-las-casillas/plan_trabajo.md) | [plan_pruebas.md](A-EP-027-HU-001-las-casillas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-027-HU-001-las-casillas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-007: el molde ya habla de casillas | Terminada |
| Riesgo | Una regla con una forma que el lector no conoce pierde texto | Se prueba la ida y vuelta de todas las reglas |

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
| **V**aliosa | Sí | Es donde se guarda todo lo demás |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 136 |
