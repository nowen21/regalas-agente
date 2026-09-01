# Estado de fase — Fase `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba` (módulo Comprobaciones)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba` |
| **Módulo** | Comprobaciones |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/epica.md](../../epica.md) · [documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-003-no-publicar-lo-que-rompe-lo-anterior/HU-003-no-publicar-lo-que-rompe-lo-anterior.md](../HU-003-no-publicar-lo-que-rompe-lo-anterior.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Medido qué subcomando corre la suite de un proyecto y cuál no |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-015 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Junta lo que aportan `F-020` y `F-021` |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 14 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ El rojo falso se encontró y se cerró acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **La puerta dio un rojo falso en su primera corrida**, y es el defecto exacto que viene a evitar. Está contado entero en la §3 del resultado.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | La puerta que junta veredicto, suite y estado |
| T-02 | Terminada | La suite del proyecto, no la del estándar |
| T-03 | Terminada | Un «no se pudo» no pasa |
| T-04 | Terminada | La orden, con el tiempo |
| T-05 | Terminada | 14 pruebas |
| T-06 | Terminada | **118,6 s, y pasa** |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un código de salida distinto de cero puede ser «falló» o «no entendí el argumento», y tratarlos igual da un rojo falso | [`S-108`](../../../../senales.md) |
| Un rojo falso es peor que no tener puerta: enseña a ignorarla | [`S-108`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La puerta no impide publicar todavía**, porque publicar es `F-008` y no está construido. Hoy es una orden que se pide; cuando exista `F-008`, se enchufa.
- **118,6 segundos.** Es el precio de correr todo, y se aguanta antes de publicar.
- **Sin pantalla**, como el resto del módulo.

---

## 4. Si se bloqueó

No se bloqueó.
