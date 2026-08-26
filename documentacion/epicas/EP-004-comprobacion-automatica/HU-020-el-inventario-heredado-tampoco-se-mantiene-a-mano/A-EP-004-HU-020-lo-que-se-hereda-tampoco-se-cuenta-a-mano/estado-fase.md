# Estado de fase — Fase `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que quien la retome no tenga que reconstruirlo leyendo el chat.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | El hallazgo `H-31` · [EP-004](../../epica.md) · [HU-020](../HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md) |
| **Última actualización** | 2026-08-26 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 12, el commit `31d556f`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 Commit `31d556f` | ☑ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

**La estación 5 pasó sin documento aparte, y es la cuarta vez.** La historia trae alcance, reglas, criterios con pasos y requisitos no funcionales; una especificación separada la repetiría. Sigue siendo el caso que la [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) está abierta para escribir. **Cuatro fases declarándolo ya no es un caso suelto: es la regla que falta.**

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple**, en el ciclo 2 |
| **CA cumplidos** | 4 de 4 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Los tres corregidos |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) · 381 pruebas, OK |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-16 | Hecha | Las dieciséis |

**Hechas:** 16 de 16. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Que un estándar puede arreglar algo para sí mismo y no repartirlo, y que eso pesa más que en un proyecto porque lo que reparte se multiplica | `S-045` |
| Que la comprobación de la fase anterior nació atada a una ruta fija, y nadie lo declaró | `S-045` |
| Que el mismo defecto tiene dos formas: el valor puesto y el hueco por llenar, y una sola expresión no caza las dos | `S-046` |
| Que «no dupliques lo derivable» no aplica a un hecho histórico: la versión al cerrar es una foto, no una cuenta | `S-047` |

---

## 3. Pendiente / preguntas abiertas

- **Nada esperando.** Construida, probada, documentada y guardada en `31d556f`.
- **Nada abierto.** El defecto que quedó fuera de lo declarado —el cierre de la fase anterior apuntando a `VERSION` en vez de decir su número— se paró, se reportó, **el usuario autorizó ampliar el plan**, y se corrigió. Está en el cierre §6 y en `S-047`.

---

## 4. Si se bloqueó

No se bloqueó en ningún momento.
