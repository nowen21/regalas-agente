# Estado de fase — Fase `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta` (módulo Expediente)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta` |
| **Módulo** | Expediente |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/epica.md](../../epica.md) · [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md](../HU-001-armar-el-expediente-de-un-proyecto.md) |
| **Última actualización** | 2026-08-31 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 1 002 documentos traídos, 19 tipos, ninguna forma de juntarlos |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-08-31 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-012, escrita y aprobada el mismo día |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-08-31 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/expediente/spec.md](../../../../expediente/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ El orden vive declarado; el expediente se calcula |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-31 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 20 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Dos defectos, los dos cerrados acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **La cadena se recorrió entera y en el día**: épica, historias, especificación y fase, cada una aprobada antes de la siguiente. Es la primera vez en esta sesión que se abre una épica desde cero.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 | Terminada | 1 002 documentos traídos, en 19 tipos |
| T-01 | Terminada | `orden.py`: ocho grupos declarados |
| T-02 | Terminada | `armar`, con el orden del ciclo también dentro de cada fase |
| T-03 | Terminada | 22 faltantes sobre lo real, todos el mismo documento |
| T-04 | Terminada | 31 a medio llenar, contando solo la marca de la casa |
| T-05 | Terminada | La memoria fuera, por tipo |
| T-06 | Terminada | Lo que no encaja: vacío sobre lo real |
| T-07 | Terminada | El alcance acotado, diciendo qué dejó fuera |
| T-08 | Terminada | `armar_expediente`, con `--hasta` y `--detalle` |
| T-09 | Terminada | 20 pruebas |
| T-10 | Terminada | Armado sobre este repositorio: 762 documentos |

**Hechas:** 11 de 11. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Contar las comillas de cita como huecos daba 559 documentos incompletos donde hay 31: la marca de un hueco es una convención, no una forma tipográfica | [`S-101`](../../../../senales.md) |
| Ordenar «por el ciclo» se cae dentro del grupo, no entre grupos: los cinco documentos de una fase salían al revés | [`S-101`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **El expediente refleja lo que Importación trajo**, no lo que el proyecto tiene hoy. Lo traído es del 25 de agosto. Volver a traerlo antes de armar es una mejora que no está en esta historia; queda dicho.
- **Los 22 faltantes son un hallazgo sobre el propio repositorio**, no sobre el módulo: veintidós fases nunca escribieron su documento de cierre.

---

## 4. Si se bloqueó

No se bloqueó.
