# Estado de fase · Fase `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto` (módulo Automatismos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto` |
| **Módulo** | Automatismos: `validadores/andamio.py`, `validadores/estacion_commit.py` y `02·F23` |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-022](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md) · [pendiente 97](../../../../../pendientes/97-andamio-impone-un-orden-de-trabajo-incorrecto.md) |
| **Última actualización** | 2026-09-27 |

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ `--hu` obligatorio en `andamio.py:366`; el enganche marca toda fase cuyo cierre esté en git |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ Pendiente 97 aprobado el 2026-09-27 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ EP-005 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ HU-022, 2026-09-27; el CA-07 entró a pedido del usuario |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ Las RN-01 a RN-06 de HU-022 |
| 6 | Diseñador | diseño coherente | ✅ `--hu` opcional, `F23` precisada y el cierre comparado contra el molde |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-09-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ Las 14 tareas hechas |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 9 de 9 exigencias con caso aprobado |
| 10 | Crítico | sin hallazgos graves | ✅ Sin defectos |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `funcionalidad_implementada.md` escrito |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 7 de 7 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-14 | Terminada | Ver `funcionalidad_implementada.md` §2.2 |

**Hechas:** 14 de 14. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El enganche `post-commit` se corrige en esta fase y no como pendiente | Decisión del usuario, 2026-09-27 |
| Un pendiente sin historia no entra al mapa de historias | En el plan §2.6 |

## 3. Pendiente / preguntas abiertas

- El commit, que autoriza el usuario.
