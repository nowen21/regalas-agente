# Estado de fase — Fase `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo` (módulo Avisos)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo` |
| **Módulo** | Avisos |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/epica.md](../../epica.md) · [documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/HU-001-avisar-lo-que-se-desvia/HU-001-avisar-lo-que-se-desvia.md](../HU-001-avisar-lo-que-se-desvia.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Todo estaba escrito, y nadie lo había leído |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-020 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/avisos/spec.md](../../../../avisos/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Tres clases, y ninguna sin causa |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 13 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ En su primera corrida encontró cinco carpetas que nadie veía |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Una comprobación nueva se estrena mirando lo que ya está**, y esta encontró en su primera corrida cinco carpetas vacías que ni git ni una búsqueda de texto veían.

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
| T-01 | Terminada | Las fases detenidas |
| T-02 | Terminada | Las historias sin fase |
| T-03 | Terminada | Lo construido sin verificar |
| T-04 | Terminada | El orden por gravedad |
| T-05 | Terminada | Lo callado a propósito |
| T-06 | Terminada | El recorte y el cero |
| T-07 | Terminada | La orden de consola |
| T-08 | Terminada | 13 pruebas |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una carpeta vacía no la ve ni el control de versiones ni una búsqueda de texto | [`S-116`](../../../../senales.md) |
| Una comprobación nueva se estrena mirando lo que ya está, no lo que venga después | [`S-116`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Cuántos avisos son demasiados no se sabe**, y es el modo en que esto fracasa.
- **Los 30 días son un número puesto acá**, no acordado por el estándar.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
