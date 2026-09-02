# Estado de fase — Fase `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida` (módulo Medición)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida` |
| **Módulo** | Medición |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) · [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-003-medir-el-tiempo-que-se-gasta-revisando/HU-003-medir-el-tiempo-que-se-gasta-revisando.md](../HU-003-medir-el-tiempo-que-se-gasta-revisando.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ La ficha advertía que la medición inicial no se tomó, y era cierto |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-011 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/medicion/spec.md](../../../../medicion/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ La mediana, y la advertencia impresa |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 14 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑  |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Con esta fase cierra la versión 5.** Y lo que deja escrito es una restricción, no una promesa: la medición inicial no existe.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Queda una restricción declarada: la medición inicial no existe |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | Los huecos |
| T-02 | Terminada | Los descartes |
| T-03 | Terminada | La mediana por mes |
| T-04 | Terminada | La línea base marcada |
| T-05 | Terminada | La negativa a comparar |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 14 pruebas |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una medición inicial no se puede reconstruir después: lo único honesto es decir que la que hay no lo es | [`S-117`](../../../../senales.md) |
| En un proyecto que va a querer demostrar que mejoró, la primera medida se toma antes de la primera línea de código | [`S-117`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La medición inicial no existe**, y no tiene arreglo. Queda declarado.
- **Bajar el tiempo puede no querer decir que se mejoró**: puede ser costumbre.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
