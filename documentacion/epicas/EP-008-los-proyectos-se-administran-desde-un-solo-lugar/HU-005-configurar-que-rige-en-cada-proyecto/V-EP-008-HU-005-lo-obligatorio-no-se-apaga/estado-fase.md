# Estado de fase — Fase `V-EP-008-HU-005-lo-obligatorio-no-se-apaga` (módulo Proyectos)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `V-EP-008-HU-005-lo-obligatorio-no-se-apaga` |
| **Módulo** | Proyectos |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md](../../epica.md) · [documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-005-configurar-que-rige-en-cada-proyecto/HU-005-configurar-que-rige-en-cada-proyecto.md](../HU-005-configurar-que-rige-en-cada-proyecto.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 49 de 257 reglas son opcionales, y no había forma de elegirlas |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-008 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/proyectos/spec.md](../../../../proyectos/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Ante la duda, obligatoria |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 14 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Un defecto crítico hallado leyendo la lista nombre por nombre |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **El número no delataba al que sobraba.** 52 y 49 se parecen; `02·F0` en la lista de lo que se puede apagar, no.

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
| T-01 | Terminada | La lista de opcionales, y su corrección |
| T-02 | Terminada | El estado con fecha y quién |
| T-03 | Terminada | El rechazo con su porqué |
| T-04 | Terminada | Lo que recibe cada proyecto |
| T-05 | Terminada | La orden de consola |
| T-06 | Terminada | 14 pruebas |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una marca vale donde está escrita, no en el archivo que la contiene | [`S-115`](../../../../senales.md) |
| Cuando una lista decide qué se puede apagar, se lee nombre por nombre | [`S-115`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Elegir moldes por proyecto se dejó para después**, cuando haya más de uno por documento.
- **Cada opción aleja dos proyectos**, y eso está declarado en la ficha.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
