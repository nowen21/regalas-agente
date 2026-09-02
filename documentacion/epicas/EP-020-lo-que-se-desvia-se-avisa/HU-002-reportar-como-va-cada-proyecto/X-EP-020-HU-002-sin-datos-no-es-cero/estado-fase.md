# Estado de fase — Fase `X-EP-020-HU-002-sin-datos-no-es-cero` (módulo Avisos)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `X-EP-020-HU-002-sin-datos-no-es-cero` |
| **Módulo** | Avisos |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/epica.md](../../epica.md) · [documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/HU-002-reportar-como-va-cada-proyecto/HU-002-reportar-como-va-cada-proyecto.md](../HU-002-reportar-como-va-cada-proyecto.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Hoy se decide con impresión, no con datos |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-020 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/avisos/spec.md](../../../../avisos/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ La definición viaja con la tabla |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 7 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑  |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Con esta fase cierra `EP-020`.** Y queda dicho lo que el avance no mide: funcionalidad entregada.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | La fila de cada proyecto |
| T-02 | Terminada | El avance, o «sin datos» |
| T-03 | Terminada | La deuda y la vencida |
| T-04 | Terminada | La definición impresa |
| T-05 | Terminada | La orden de consola |
| T-06 | Terminada | 7 pruebas |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una comparación sin su definición al lado engaña, y la definición que vive aparte no se lee | [`S-116`](../../../../senales.md) |
| Cero y «no se sabe» se escriben distinto o no se distinguen nunca | [`S-116`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La misma medida entre proyectos muy distintos puede engañar**, y solo se contrarresta con la definición impresa.
- **El avance mide fases cerradas**, no funcionalidad entregada.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
