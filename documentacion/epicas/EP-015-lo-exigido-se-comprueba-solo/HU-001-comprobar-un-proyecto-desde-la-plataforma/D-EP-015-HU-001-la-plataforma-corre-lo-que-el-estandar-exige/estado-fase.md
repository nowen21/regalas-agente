# Estado de fase — Fase `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige` (módulo Comprobaciones)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige` |
| **Módulo** | Comprobaciones |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/epica.md](../../epica.md) · [documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-001-comprobar-un-proyecto-desde-la-plataforma/HU-001-comprobar-un-proyecto-desde-la-plataforma.md](../HU-001-comprobar-un-proyecto-desde-la-plataforma.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 32 comprobaciones existen; la plataforma no corría ninguna |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-015 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Sin entidades; se corre el punto de entrada del estándar |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 13 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ El tiempo queda declarado, no escondido |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **La fase encontró un incumplimiento real en su primera corrida:** dos enlaces rotos de su propio trabajo. Es la mejor evidencia de que sirve.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Queda un dato declarado: los 116,9 segundos |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | La detección previa: no existe, no está, o no tiene el estándar |
| T-02 | Terminada | El punto de entrada, en un proceso aparte |
| T-03 | Terminada | El resumen y las fallas, con archivo y línea |
| T-04 | Terminada | La salida tapada antes de devolverla |
| T-05 | Terminada | El veredicto, con «cero es rojo» adentro |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 13 pruebas |
| T-08 | Terminada | **32 comprobaciones en 116,9 s**, y dos fallas reales |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna. De los cuatro bloqueos, tres cerrados y el `B-01` declarado.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| «Sin comprobar» no es «no cumple», y confundirlas hace que nadie mire el rojo | [`S-107`](../../../../senales.md) |
| Una cadena de necesidades puede tener vueltas; una de construcción, no | [`S-107`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Los 116,9 segundos.** Se aguantan para pedirlo a mano; no para pedirlo seguido. Quien lo enchufe en algún sitio lo decide con el número delante. Declarado, sin pendiente: hoy no está enchufado en ninguna parte.
- **`F-021` y `F-022` siguen sin construir.** Sus historias están nombradas en la épica y sin escribir.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
