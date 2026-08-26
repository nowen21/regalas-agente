# Estado de fase — Fase `A-EP-003-HU-001-marca-de-espacio-por-llenar` (módulo Documentos modelo)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-001-marca-de-espacio-por-llenar` |
| **Módulo** | Documentos modelo |
| **Brief / Épica / HU** | [EP-003](../../epica.md) · [HU-001](../HU-001-marca-de-espacio-por-llenar.md) |
| **Última actualización** | 2026-08-14 |

---

## 1. En qué estación va

**Estación actual:** 13 — Publicación. **Última puerta pasada:** 12.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorer · análisis | contexto entendido | ☑ |
| 2 | Proposer · alcance | 👤 alcance aprobado | ☑ |
| 3 | Épica Writer | 👤 épica aprobada | ☑ |
| 4 | HU Writer | 👤 HUs aprobadas | ☑ |
| 5 | Spec Writer | 👤 especificación aprobada | ☑ [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md), aprobada el 2026-08-14 |
| 6 | Designer | diseño coherente | ☑ las decisiones están en §2.6 del plan de trabajo |
| 7 | Task Planner | 👤 plan + pruebas aprobados | ☑ aprobados, con dos ampliaciones también aprobadas |
| 8 | Implementer | implementado + pruebas verdes | ☑ tres reglas nuevas y 179 huecos convertidos |
| 9 | Verifier | trazabilidad sin faltantes | ☑ los tres CA y los tres RNF en verde |
| 10 | Crítico | sin hallazgos graves | ☑ un defecto aceptado, DEF-03, que no toca ningún CA |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☑ `b877f37`, autorizado el 2026-08-14 |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ sin `push` |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 3 de 3, y los 3 requisitos no funcionales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | DEF-03, el `«ADR-XXX»` de `ADR.md`. Cumple la regla; queda anotado por si se prefiere `«ADR-NNN»` |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-12, más T-03b y T-06b | Hecha | Las catorce |

**Hechas:** 14 de 14. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La marca es `«…»` porque ya se usa en 25 de 30 plantillas: cambiarla costaría 25 archivos en vez de 5 | [`notas/marca-del-espacio-por-llenar.md`](../../../../../notas/marca-del-espacio-por-llenar.md) |
| La especificación del módulo sí va aparte: [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) se cumple y no lleva excepción | Cierra el H-7 del [resumen del 2026-08-14](../../../../../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md) · señal S-003 |
| La sintaxis de un comando no es un hueco por llenar | Escrita dentro de [`13·DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) |
| Una sección que no aplica se escribe `N/A` | [`13·DOC21`](../../../../../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) |

---

## 3. Pendiente / preguntas abiertas

- **`validadores/reglas-validables.md` quedó fuera del commit**: ese archivo lo está editando otra sesión, y commitearlo arrastraría su trabajo. Las tres filas de [`DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), [`DOC20`](../../../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) y [`DOC21`](../../../../../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) están escritas pero sin guardar.
- Las tres dudas de §2.7 del plan de trabajo quedaron respondidas el 2026-08-14 y escritas en la especificación §12.

---

## 4. Si se bloqueó

- **Estación:** 13. **Motivo:** no se ha publicado. **Qué falta para desbloquear:** que el usuario autorice el `push`.
