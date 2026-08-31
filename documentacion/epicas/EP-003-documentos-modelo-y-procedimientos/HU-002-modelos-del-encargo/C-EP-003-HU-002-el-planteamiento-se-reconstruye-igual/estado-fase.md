# Estado de fase — Fase C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual (módulo Documentos modelo)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual` |
| **Módulo** | Documentos modelo |
| **Planteamiento / Épica / HU** | [prompts/cimiento-planteamiento.md](../../../../../prompts/cimiento-planteamiento.md) · [EP-003](../../epica.md) · [HU-002](../HU-002-modelos-del-encargo.md) |
| **Última actualización** | 2026-08-22 |

---

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

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
| 12 | Commit | 👤 autorizado | ✅ `9b808e0` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

**De las estaciones 1 a 6.** La épica y la historia ya existían; el CA-04 se agregó a HU-002 el 2026-08-22 con la aprobación del usuario. La especificación del módulo vive en [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../../epica.md) §5.1 y §5.4 fila 10. El diseño de lo que hay que escribir está en §2.6 del [plan de trabajo](plan_trabajo.md), con sus cuatro decisiones y la alternativa que se descartó en cada una.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4 exigencias de la matriz |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | D-03, el caso con lector que no se pudo correr; D-04, `resultado_pruebas.md` sin entrada en la tabla de nombres |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | El campo «Cómo se levantó» en la identificación |
| T-02 | Hecha | El apartado del proyecto ya construido, con sus fuentes |
| T-03 | Hecha | La tabla de traducción, con las cuatro conversiones |
| T-04 | Hecha | La advertencia de que reconstruir es también auditar |
| T-05 | Hecha | «Borrar este recuadro. **Solo este recuadro**» |
| T-05b | Hecha | Tarea que no estaba en el plan original: el encuadre enlaza `02·F0` en vez de copiarle una cadena divergente |
| T-06 | Hecha | Cinco casos en verde, uno no ejecutable |
| T-07 | Hecha | Sobre `31.13.0` |

**Hechas:** 8 de 8.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un solo molde para los dos casos, no dos moldes | [funcionalidad_implementada.md](funcionalidad_implementada.md) §5 |
| La procedencia va en un campo, no en un párrafo de encuadre. El párrafo ya desplazó al encuadre una vez | Ídem |
| Reconstruir el planteamiento de algo ya construido es también auditarlo | Ídem |
| El molde copiaba la cadena de `02·F0` y la copia ya no coincidía. Otra sesión de la jornada lo dio por bueno sin comprobarlo | Hallazgo H-7 del [resumen de la sesión](../../../../../historico-chat/resumenes/2026-08-22/sesion-2.md) |
| La comprobación del encuadre no alcanzaba a ningún planteamiento real, porque el molde manda un nombre que el validador no reconocía | D-01 de [resultado_pruebas.md](resultado_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- Falta la autorización del usuario para el commit. Nada más.
- El CP-003 sigue sin correrse: necesita un lector que no haya participado y hoy no hay quién. Queda como D-03.

---

## 4. Si se bloqueó

No se bloqueó.
