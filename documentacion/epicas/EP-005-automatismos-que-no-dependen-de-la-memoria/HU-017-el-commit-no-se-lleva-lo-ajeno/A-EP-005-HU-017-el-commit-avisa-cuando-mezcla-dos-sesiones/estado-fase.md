# Estado de fase — Fase A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones (módulo Enganches de git)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones` |
| **Módulo** | Enganches de git |
| **Planteamiento / Épica / HU** | [prompts/cimiento-planteamiento.md](../../../../../prompts/cimiento-planteamiento.md) · [EP-005](../../epica.md) · [HU-017](../HU-017-el-commit-no-se-lleva-lo-ajeno.md) |
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

**Sobre las estaciones 3 y 4.** La épica ya existía. La HU-017 nace con esta fase, escrita antes de tocar código, y el usuario había ordenado resolver el pendiente del que sale.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4 exigencias de la matriz |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | |
| T-02 | Hecha | |
| T-03 | Hecha | Y quedó fuera de la corrida completa, con su motivo |
| T-04 | Hecha | Antes del filtro de `.md`, protegida para no tumbar el enganche |
| T-05 | Hecha | Sin cortar el commit |
| T-06 | Hecha | |
| T-07 | Hecha | 10 casos, 5 de lo que no debe avisar |

**Hechas:** 7 de 7.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La pregunta imposible se dio vuelta: no «quién commitea», que `git` no sabe, sino «mezcla el commit», que se ve desde los archivos | [funcionalidad_implementada.md](funcionalidad_implementada.md) §5 |
| Avisa y no rechaza, porque un enganche que rechaza siempre se apaga, y eso ya está medido | Ídem |
| El registro no se versiona: versionarlo lo volvería el próximo archivo que dos sesiones se pisan | Ídem |
| Esta fase sí escribió su plan antes de tocar nada, a diferencia de la de los moldes en esta misma jornada | Queda dicho en los dos documentos, para que la comparación sea posible |

---

## 3. Pendiente / preguntas abiertas

- Falta la autorización del usuario para el commit. Nada más.

---

## 4. Si se bloqueó

No se bloqueó.
