# Estado de fase — Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` (módulo Meta-reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` |
| **Módulo** | Meta-reglas |
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) · [HU-007](../HU-007-regla-de-las-reglas.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-27 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19` |
| 6 | Diseñador | diseño coherente | ✅ No se toca código |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 5 tareas, 5 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-069` |
| 12 | Commit | 👤 autorizado | ☐ **Esperando aprobación del usuario** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 — el `CA-04`, en sus tres exigencias |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · correr y comprobar que da una lista | Terminada | 251 reglas |
| T-02 · que diga cuándo y cuántos | Terminada | `REVISADA` y `FALLA HOY` |
| T-03 · que esté **ordenada** | Terminada | 25 sellos, sin retroceder |
| T-04 · que avise y no corrija | Terminada | Ningún archivo cambia |
| T-05 · declarar el veredicto y el reemplazo | Terminada | — |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Recomendar trabajo sin leer el criterio repite el error que uno acaba de señalar | [`S-069`](../../../../senales.md) |
| Un veredicto puede estar mal el día que se escribe | [`S-063`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del commit**, que se pide aparte de la aprobación del cambio.
- **Revisar reglas de fondo sigue siendo trabajo útil**, y ahora es trabajo normal en vez de deuda. Cuándo empezar lo decide el usuario.

---

## 4. Si se bloqueó

No se bloqueó.

**Lo que más costó no fue medir: fue darse cuenta de que había que leer el criterio.** Este trabajo se recomendó tres veces como «la deuda de las 250 reglas», y se cayó en la primera lectura — la que se hizo **para ejecutarlo**, no para revisarlo.
