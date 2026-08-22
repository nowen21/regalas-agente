# Estado de fase — Fase B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo (módulo Documentos modelo)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo` |
| **Módulo** | Documentos modelo |
| **Planteamiento / Épica / HU** | [prompts/cimiento-planteamiento.md](../../../../../prompts/cimiento-planteamiento.md) · [EP-004](../../epica.md) · [HU-012](../HU-012-marcas-de-generacion-automatica.md) |
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
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 1 de 1, el CA-04 en sus cuatro pasos |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. El D-04 que se había reportado resultó falso y quedó cerrado por falso el mismo día |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | 213 apariciones clasificadas en 7 clases |
| T-02 | Hecha | 13 citas de regla escritas en formato canónico |
| T-03 | Hecha | 25 líneas, 6 corregidas a mano después |
| T-04 | Hecha | Rompió el marcador `«…»` y hubo que reponerlo en 24 sitios |
| T-05 | Hecha | De 197 a 126 |
| T-06 | Hecha | 47 pruebas de las suites que dependen de los moldes, en verde |
| T-07 | Hecha | Sobre `31.12.0` |

**Hechas:** 7 de 7.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **El plan de esta fase se escribió después de la intervención.** [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) pide lo contrario. Queda dicho en el propio plan, en su primera caja | Sin disimular: es un incumplimiento del agente, no una excepción |
| Clasificar antes de limpiar es lo que salvó los moldes: un reemplazo a ciegas habría quitado las etiquetas de campo y renombrado secciones | [funcionalidad_implementada.md](funcionalidad_implementada.md) §5 |
| El marcador `«…»` se volvió a romper, y ya estaba advertido por escrito en el pendiente 11 | Ídem. La lección no es sobre el marcador: es que lo que un pendiente cerrado dejó escrito hay que leerlo antes de tocar lo mismo |
| Renombrar una sección de un molde rompe la comprobación de forma de 650 documentos, y eso es lo que hace que la limpieza cosmética no sea gratis | Ídem |

---

## 3. Pendiente / preguntas abiertas

- **La decisión que decide si el pendiente 78 cierra:** las cuatro formas de notación que quedan, ¿se declaran en [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md), como se hizo el 2026-08-18 con el punto medio de los encabezados, o se reescriben los moldes asumiendo el daño? Es del usuario.
- Falta la autorización del usuario para el commit.

---

## 4. Si se bloqueó

No se bloqueó.
