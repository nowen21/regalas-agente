# Estado de fase — Fase B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [prompts/cimiento-planteamiento.md](../../../../../prompts/cimiento-planteamiento.md) · [EP-004](../../epica.md) · [HU-004](../HU-004-forma-de-los-documentos.md) |
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
| 12 | Commit | 👤 autorizado | ✅ `7eaade3` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

**Sobre la puerta 7.** El usuario ordenó ejecutar el [pendiente 77](../../../../../pendientes/hecho/el-planteamiento-conserva-su-encuadre.md), y esa orden se tomó como la aprobación de los dos planes. Quedó dicho al pedirlo y quedó dicho acá.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4, contando el CA-05 y los tres requisitos de la matriz |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | D-04, media: cinco planes de pruebas del repositorio perdieron su línea fija. No es defecto de la fase, es lo primero que encontró el validador que la fase construyó |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Con un ajuste no previsto: saltar las filas de tabla |
| T-02 | Hecha | |
| T-03 | Hecha | El criterio cambió a mitad de camino, de la cita de regla a la fecha |
| T-04 | Hecha | 9 casos, dos más de los planeados |
| T-05 | Hecha | 651 documentos, 5 reprobados, ninguno por error |
| T-06 | Hecha | Sobre `31.12.0`, no `31.10.0` |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El texto fijo se identifica por posición y no por su etiqueta, porque la etiqueta cambió dos veces en un día | En [funcionalidad_implementada.md](funcionalidad_implementada.md) §5 |
| Un criterio semántico no separaba los casos reales, y se supo midiendo antes de elegir | Ídem |
| Un validador que reprueba lo que está bien enseña a ignorar todos los veredictos, y por eso el barrido contra los documentos reales va antes de cerrar, no después | Ídem |
| **Otra sesión commiteó esta fase a medio hacer**, con el criterio equivocado ya publicado. Es el caso borde que el planteamiento lista en §8 y ocurrió de verdad | Hallazgo H-6 del [resumen de la sesión](../../../../../historico-chat/resumenes/2026-08-22/sesion-2.md) |

---

## 3. Pendiente / preguntas abiertas

- Falta la autorización del usuario para el commit. Nada más.
- D-04 espera su pendiente: los cinco planes de pruebas sin línea fija.

---

## 4. Si se bloqueó

No se bloqueó.
