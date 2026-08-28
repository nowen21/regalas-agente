# Estado de fase — Fase `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito` (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-022](../HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 13 · Publicación. **Última puerta pasada:** 12, en `011754b`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ Las salidas 1 y 3 del pendiente 88 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-27 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ 450 de 450 |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 9 tareas, 9 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ Seis sabotajes, cuatro defectos encontrados |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-060` |
| 12 | Commit | 👤 autorizado | ✅ `011754b` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` a `DEF-04` corregidos |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 · el impacto sobre los árboles de prueba | Terminada | 2.299 literales, **ninguno llega al corte** |
| T-01 · leer los marcadores de las cinco plantillas | Terminada | Una sola vez, `RNF-01` |
| T-02 · decir si conserva tres o más de los suyos | Terminada | `sigue_siendo_el_molde` |
| T-03 · que la fase no cuente terminada | Terminada | `_fase_terminada`, compartida por las dos cuentas |
| T-04 · un aviso por documento | Terminada | Con fase, archivo y un marcador de ejemplo |
| T-05 · los cinco CA y el caso de la prosa | Terminada | 16 pruebas, **6 de que NO señale** |
| T-06 · medir y nombrar los siete | Terminada | §3 del resultado |
| T-07 · `CHANGELOG` y `VERSION` | Terminada | `35.3.0`, MENOR |
| T-08 · sabotear | Terminada | Seis; el quinto obligó a un segundo ciclo |

**Hechas:** 9 de 9. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una medida se valida sobre el conjunto entero, no sobre los casos que la motivaron | [`S-059`](../../../../senales.md) |
| Un guion que rompe a propósito restaura en `finally`, y no se corre por una tubería | [`S-060`](../../../../senales.md) |
| Una comprobación que no puede fallar da la misma señal verde que una que funciona | `DEF-02` del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del `push`**, que se pide aparte del commit.
- **Los siete documentos que quedaron señalados.** No son de esta fase: cinco son planes de pruebas que nunca se escribieron, en fases que sí tienen código.

---

## 4. Si se bloqueó

No se bloqueó.

**La línea base se midió antes de crear esta carpeta**, que era el riesgo `B-04` del plan: `117 en total · 32 sin terminar · 85 terminadas, de las cuales 64 cumplen, 16 no cumplen y 5 no dicen`. Es la primera fase del día en que la medición **no** se movió por debajo.
