# Estado de fase — Fase `A-EP-003-HU-012-una-sola-palabra-por-estado` (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que quien la retome no tenga que reconstruirlo leyendo el chat.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-012-una-sola-palabra-por-estado` |
| **Módulo** | Documentos modelo |
| **Planteamiento / Épica / HU** | La señal `S-048` · [EP-003](../../epica.md) · [HU-012](../HU-012-una-sola-palabra-para-cada-estado.md) |
| **Última actualización** | 2026-08-26 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 12, el commit `a14f5ed`.

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
| 12 | Commit | 👤 Commit `a14f5ed` | ☑ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

**La estación 5 pasó sin documento aparte**, y la regla que lo permite ya existe: [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), «la redacción del CA es la especificación funcional».

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple**, en el ciclo 2 |
| **CA cumplidos** | 4 de 4 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) · 396 pruebas, OK |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-14 | Terminada | Las catorce |

**Hechas:** 14 de 14. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Que el desorden no era descuido: los moldes del propio estándar enseñaban tres palabras para lo mismo | `S-049` |
| Que el estado de una épica estaba definido dos veces con listas que no coincidían | `S-049` |
| Que un vocabulario sin sitio único no se puede comprobar, y por eso nada cazó el error de `S-048` | `S-049` |
| Que una comprobación que reporta fuera de su tema apaga las demás | `S-050` |

---

## 3. Pendiente / preguntas abiertas

- **Nada esperando.** Construida, probada, documentada y guardada en `a14f5ed`.
- **El vocabulario acabó traducido**, y no quedó aparte como se había pensado: el plan lo forzaba. Escribir `Backlog` en el glosario —que es el documento que lleva la lista de lo que se queda en otro idioma **y por qué**— habría sido incumplir donde más se nota.
- **Dos cosas quedan sin dueño, y están en el cierre §6:** que nadie reporte un campo `Estado` faltante, y que solo se comprueben las historias — épicas y planes tienen vocabulario pero no guardia.

---

## 4. Si se bloqueó

No se bloqueó en ningún momento.
