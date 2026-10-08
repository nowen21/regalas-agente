# HU-003 · El texto que recibe el agente se arma desde las tablas

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
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

- **Como** el agente que recibe las reglas en cada mensaje
- **Quiero** que el texto que me llega salga siempre de las tablas
- **Para** recibir la regla tal como está guardada, con la forma de siempre

---

## 3. Contexto y descripción

La HU-002 pasó las reglas a las tablas y armó el texto desde ellas una vez. Falta que todo cambio siguiente pase por las tablas: si alguien cambia el texto de un documento, las tablas quedan atrás y el texto deja de salir de ellas. Sale del [análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), acuerdo 2: el texto se arma desde las tablas, con la forma de hoy.

Los enganches y el freno leen `estandar_documento` sin Django, en cada mensaje (`core/estandar/en_base.py`). Por eso el texto armado se guarda en el documento: así siguen leyendo de donde leen, sin demora.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Guardar un documento, desde la pantalla o al aprobar una propuesta, pasa sus reglas a las tablas y guarda el texto armado desde ellas |
| RN-02 | Lo que trae git al sincronizar pasa por las tablas igual |
| RN-03 | Quitar un documento no borra sus reglas: quedan sin documento (`20·M11`) |
| RN-04 | Una regla que sale del texto queda sin documento, no se borra (`20·M11`) |
| RN-05 | Lo que reciben el agente, el freno y `ver_estandar` es el texto armado desde las tablas |

### 3.2 Supuestos

- Ninguno.

### 3.3 Fuera de alcance

- Dejar de guardar `base/reglas-por-tarea/` (acuerdo 1): armarlas al vuelo tarda 0,8 s por mensaje, medido el 2026-10-07. El usuario decidió el 2026-10-07 («Apruebo las recomendaciones») que siguen guardadas, armadas solas desde las tablas cuando una regla cambia.
- Cambiar una regla por sus casillas desde la pantalla.

---

## 4. Criterios de aceptación

### CA-01 · Cambiar un documento pasa por las tablas

**Sale de:** acuerdo 2 del análisis 1 del pendiente 136

```gherkin
Dado una regla en las tablas
Cuando se guarda su documento con la exigencia cambiada, desde la pantalla, una propuesta o git
Entonces la fila de la regla tiene la exigencia nueva
Y el texto guardado del documento es el armado desde las tablas
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_texto_desde_tablas` → resultado esperado: los casos pasan.

### CA-02 · Nada se borra

**Sale de:** `20·M11`

```gherkin
Dado una regla en las tablas
Cuando su documento se quita, o la regla sale del texto
Entonces la regla sigue en las tablas, sin documento
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_texto_desde_tablas` → resultado esperado: los casos pasan.

### CA-03 · El agente recibe el texto armado

**Sale de:** acuerdo 2 del análisis 1 del pendiente 136

```gherkin
Dado una regla cambiada en las tablas
Cuando el agente lee el estándar, o se pide con ver_estandar
Entonces recibe el texto armado desde las tablas
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_texto_desde_tablas` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Lo que leen los enganches en cada mensaje no se demora |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| Modelo de datos afectado | Las tablas de la HU-001 y `estandar_documento` |

---

## 7. Tareas técnicas derivadas

- [ ] Guardar, quitar y sincronizar pasan por las tablas.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-027-HU-003-todo-pasa-por-las-tablas` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-027-HU-003-todo-pasa-por-las-tablas/plan_trabajo.md) | [plan_pruebas.md](A-EP-027-HU-003-todo-pasa-por-las-tablas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-027-HU-003-todo-pasa-por-las-tablas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-002 | Terminada |
| Riesgo | Un cambio que no pasa por las tablas deja el texto atrás | Los tres caminos que cambian un documento pasan por las tablas, con su prueba |

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
| **V**aliosa | Sí | Las tablas no quedan atrás |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 136 |
