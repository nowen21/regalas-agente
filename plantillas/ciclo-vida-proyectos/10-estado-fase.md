# Estado de fase — Fase «A-EP01-HU03-Descripción» (módulo «M»)   ·   `[CAPA 3]`

> **Checkpoint del orquestador** (`sdd-orchestrator`): el estado persistido en cada puerta para **sobrevivir a la compactación** ("la compactación mata decisiones"). Se escribe/actualiza en **cada puerta** que pasa. Al reanudar, el director lee este archivo y continúa desde la última puerta pasada. Se guarda en `documentacion/<modulo>/estado-fase.md`. Reemplaza los `«…»` y borra esta caja.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `«A-EP01-HU03-Descripción»` |
| **Módulo** | «M» |
| **Planteamiento / Épica / HU** | «punteros» |
| **Última actualización** | AAAA-MM-DD |

---

## 1. En qué estación va

**Estación actual:** «N — nombre». **Última puerta pasada:** «N».

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☐ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☐ |
| 3 | Escritor de épica | 👤 épica aprobada | ☐ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☐ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☐ |
| 6 | Diseñador | diseño coherente | ☐ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☐ |
| 8 | Implementador | implementado + pruebas verdes | ☐ |
| 9 | Verificador | trazabilidad sin faltantes | ☐ |
| 10 | Crítico | sin hallazgos graves | ☐ |
| 11 | Cierre documental + señales | docs y señales al día | ☐ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

> De dónde sale el estado de la estación 9. **No se escribe de memoria ni "porque se vio funcionar"**: se copia del `resultado_pruebas.md` de la fase, §6.

| Campo | Valor |
|---|---|
| **Concepto** | «Cumple / No cumple / Todavía no se ejecutó». Sin estado intermedio: lo que falta hace que sea No cumple |
| **CA cumplidos** | «cuántos de cuántos» |
| **CA en "No"** | «cuáles. Con uno solo, la fase no cierra» |
| **Defectos abiertos aceptados** | «cuáles y quién los aceptó» |
| **Fuente** | «`resultado_pruebas.md`» |

---

## 1.2 Avance de las tareas del plan

> El seguimiento **en vivo**, mientras la fase corre. Los identificadores se copian del `plan_trabajo` §3, que no se toca. Al cerrar, esto se consolida en el `funcionalidad_implementada.md` §2.2, que es la verificación de registro.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente / En curso / Hecha / Bloqueada | «si está bloqueada, por qué» |

**Hechas:** «N de N». **Bloqueadas:** «cuáles».

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| | |

---

## 3. Pendiente / preguntas abiertas

- «Qué falta, qué se está esperando (una aprobación, una respuesta del usuario, una dependencia).»

---

## 4. Si se bloqueó

- **Estación:** «N». **Motivo:** «pruebas rojas / hallazgo grave del Crítico / alcance rechazado / dependencia faltante». **Qué falta para desbloquear:** «…».
