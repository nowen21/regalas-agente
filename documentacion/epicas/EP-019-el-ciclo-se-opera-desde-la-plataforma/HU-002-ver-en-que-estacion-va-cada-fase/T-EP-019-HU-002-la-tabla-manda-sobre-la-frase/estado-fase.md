# Estado de fase — Fase `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase` (módulo Ciclo de vida)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase` |
| **Módulo** | Ciclo de vida |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-002-ver-en-que-estacion-va-cada-fase/HU-002-ver-en-que-estacion-va-cada-fase.md](../HU-002-ver-en-que-estacion-va-cada-fase.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 209 fases y ninguna forma de mirarlas juntas |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-019 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ El texto es la verdad, y hay que leer el que hay |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 11 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Tres defectos hallados y corregidos dentro de la fase |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Ninguna de las 209 fases se reescribió.** El que se adapta es el que lee.

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
| T-01 | Terminada | La tabla leída |
| T-02 | Terminada | Las dos marcas |
| T-03 | Terminada | «Sin marcar» con su nombre |
| T-04 | Terminada | Comparar solo entre iguales |
| T-05 | Terminada | Los días quietos |
| T-06 | Terminada | La orden y su resumen |
| T-07 | Terminada | 11 pruebas |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Antes de comparar dos documentos, comprobar que hablen del mismo modelo | [`S-114`](../../../../senales.md) |
| Contar cuántos siguen la convención vieja antes de suponer que todos siguen la nueva | [`S-114`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **33 fases siguen con la frase y la tabla en desacuerdo.** Son reales, y arreglarlas es reescribir fases cerradas.
- **3 fases tienen alguna estación sin marcar**, y así quedan declaradas.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
