# HU-005 · Las propuestas, la historia y la memoria muestran nombres legibles

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-027 · Las reglas del estándar viven en tablas con la estructura del molde](../epica.md) |
| **Módulo / Componente** | Estándar en la base (`core/estandar/`) e historia (`core/historia/`) |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien aprueba propuestas, revisa la historia o lee la memoria de un proyecto
- **Quiero** ver el nombre de cada cosa, y no su ruta, su nombre de archivo o su número de fila
- **Para** saber de qué se trata sin conocer cómo está guardado

---

## 3. Contexto y descripción

Las propuestas dicen «Cambiar: base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md»; la historia dice «estandar.documento» en la tabla y «135» en la fila; la memoria lista «aprendizaje_compactar_al_promover.md». Sale del [análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), acuerdo 4.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Una propuesta de un documento se nombra con el título del documento, y con el código de la regla si es una |
| RN-02 | Un recuerdo se nombra con el título de su texto o, si no tiene, con su nombre escrito con espacios; su descripción va debajo |
| RN-03 | En la historia, la tabla se nombra con lo que guarda («Documento del estándar», «Regla») y la fila con el nombre de lo que cambió |
| RN-04 | La ruta, el nombre de archivo y el número de fila no se muestran como nombre; quien administra los ve donde los necesita: al crear un documento o un recuerdo |

### 3.2 Supuestos

- Ninguno.

### 3.3 Fuera de alcance

- Cambiar cómo se guardan los recuerdos.

---

## 4. Criterios de aceptación

### CA-01 · Propuestas y memoria con nombres legibles

**Sale de:** acuerdo 4 del análisis 1 del pendiente 136

```gherkin
Dado una propuesta que cambia la regla F8 y un recuerdo con nombre de archivo
Cuando se abren «Propuestas» y la memoria del proyecto
Entonces la propuesta dice «F8 · Edita solo los archivos que el plan aprobado declara»
Y el recuerdo se ve con su nombre legible y su descripción, sin «.md»
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_nombres_legibles` → resultado esperado: los casos pasan.

### CA-02 · La historia con nombres legibles

**Sale de:** acuerdo 4 del análisis 1 del pendiente 136

```gherkin
Dado un cambio de un documento del estándar en la historia
Cuando se abre «Historia»
Entonces la tabla dice «Documento del estándar» y la fila dice el título del documento
```

**Cómo validarlo:** correr `manage.py test core.historia.tests_nombres_legibles` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Nombrar las filas de una página de la historia no hace una consulta por fila |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| Guía | `base/17-guia-de-pantallas.md`, §6 y §8 |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Propuestas y memoria (fase A, `core/estandar/`).
- [ ] Historia (fase B, `core/historia/`).

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-027-HU-005-propuestas-y-memoria` | CA-01 | (vacío) | [plan_trabajo.md](A-EP-027-HU-005-propuestas-y-memoria/plan_trabajo.md) | [plan_pruebas.md](A-EP-027-HU-005-propuestas-y-memoria/plan_pruebas.md) | [resultado_pruebas.md](A-EP-027-HU-005-propuestas-y-memoria/resultado_pruebas.md) | Terminada |
| `B-EP-027-HU-005-historia` | CA-02 | (vacío) | [plan_trabajo.md](B-EP-027-HU-005-historia/plan_trabajo.md) | [plan_pruebas.md](B-EP-027-HU-005-historia/plan_pruebas.md) | [resultado_pruebas.md](B-EP-027-HU-005-historia/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-004: el título de cada documento | Terminada |

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
| **V**aliosa | Sí | Se entiende qué cambia sin conocer cómo se guarda |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 136 |
