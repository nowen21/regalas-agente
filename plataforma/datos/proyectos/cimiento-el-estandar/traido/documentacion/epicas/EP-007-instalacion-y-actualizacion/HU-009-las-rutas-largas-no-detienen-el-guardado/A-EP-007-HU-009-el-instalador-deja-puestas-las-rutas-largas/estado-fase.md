# Estado de fase — Fase `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` (módulo Instalación) · `[CAPA 3]`

> **Retrodocumentado el 2026-08-27.** La fase se construyó y se cerró el 2026-08-26 bajo la versión `35.1.0`, y **este documento se quedó siendo la plantilla en blanco**. Lo destapó la [HU-022](../../../EP-004-comprobacion-automatica/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md).
>
> **No se inventa nada:** todo sale del [plan_trabajo.md](plan_trabajo.md), del [resultado_pruebas.md](resultado_pruebas.md) y del [cierre](funcionalidad_implementada.md), que sí se escribieron. **Este documento es un seguimiento en vivo, y en vivo no se llevó** — se deja dicho en vez de fingir que sí.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` |
| **Módulo** | Instalación |
| **Planteamiento / Épica / HU** | [EP-007](../../epica.md) · [HU-009](../HU-009-las-rutas-largas-no-detienen-el-guardado.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 13 · Publicación. **Última puerta pasada:** 12, en `dab3872`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 11 tareas, 11 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ Sabotajes, con dos hallazgos que valieron |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-042`, `S-051` |
| 12 | Commit | 👤 autorizado | ✅ `dab3872` |
| 13 | Publicación / despliegue | 👤 autorizado | ✅ Publicada el 2026-08-26 |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 y §6 |

---

## 1.2 Avance de las tareas del plan

> **Consolidado al cerrar, no llevado en vivo.** Sale del [cierre](funcionalidad_implementada.md).

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · leer el valor actual del ajuste, sin escribir | Terminada | |
| T-02 · ponerlo si no está, y decirlo entre los pasos | Terminada | |
| T-03 · si está en `false`, decirlo y **no pisarlo** | Terminada | Es una decisión de quien lo puso |
| T-04 · que el modo que muestra **no escriba** | Terminada | |
| T-05 · casos de los cuatro escenarios | Terminada | |
| T-06 · que las clases de `EP-007` sigan pasando | Terminada | |
| T-07 a T-09 · qué hacer al ver el error, en el documento de despliegue | Terminada | Los dos comandos, y cuál es opcional y por qué |
| T-10 · `VERSION` y la entrada | Terminada | `35.1.0` |
| T-11 · sabotear cada pieza | Terminada | |

**Hechas:** 11 de 11. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| `core.longpaths` en vez de acortar nombres. **Medido:** la holgura del peor caso son 8 caracteres y anidar necesita 55; acortar la convención ahorra 14, y ninguna combinación crea los 55 | [`S-042`](../../../../senales.md) |
| La prueba pregunta por el valor **local**, no compara el global consigo mismo — comparar antes y después pasa si otra prueba ya lo cambió | [`S-051`](../../../../senales.md) |
| El guion limpia el rastro **tras cada sabotaje**, no al final: cae fuera del repositorio, donde ningún `git status` lo muestra | `S-051` |

---

## 3. Pendiente / preguntas abiertas

Ninguna de esta fase.

---

## 4. Si se bloqueó

No se bloqueó.

**Lo que más costó no fue construirlo:** fue descartar la explicación cómoda. Se afirmó dos veces que acortar los nombres resolvía el tope de ruta, **y las dos veces era falso** — se supo restando, no releyendo. Está en `S-042`.
