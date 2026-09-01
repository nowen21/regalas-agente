# Estado de fase — Fase `H-EP-016-HU-002-derogar-marca-y-no-borra` (módulo Reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `H-EP-016-HU-002-derogar-marca-y-no-borra` |
| **Módulo** | Reglas |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-002-escribir-corregir-y-derogar-una-regla/HU-002-escribir-corregir-y-derogar-una-regla.md](../HU-002-escribir-corregir-y-derogar-una-regla.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Verificado el formato canónico y la marca de derogación sobre reglas reales |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-016 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ El límite se declaró antes de construir: no detecta contradicciones |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 14 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **Lo que más cuidado costó no fue el código, sino una frase.** El aviso dice, cada vez, que esto no detecta contradicciones. Sin ella la funcionalidad sería peor que no existir.

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
| T-01 | Terminada | El molde canónico, con sus huecos |
| T-02 | Terminada | Escribir, pidiendo el identificador antes |
| T-03 | Terminada | Derogar: marcar y conservar |
| T-04 | Terminada | Las tres razones por las que no se deroga |
| T-05 | Terminada | Las reglas que hablan de lo mismo |
| T-06 | Terminada | **El aviso de lo que eso no puede decir** |
| T-07 | Terminada | Las dos órdenes de consola |
| T-08 | Terminada | 14 pruebas |
| T-09 | Terminada | **Sobre las 248 vigentes: encontró el duplicado** |

**Hechas:** 9 de 9. **Bloqueadas:** ninguna. Los cuatro bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una ayuda que se presenta como garantía hace que la gente deje de mirar | [`S-109`](../../../../senales.md) |
| Derogar marca y conserva: lo que se borra no se puede volver a leer | [`S-109`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Corregir una regla ya escrita** no está: se escribe y se deroga. Editar su cuerpo se hace por el módulo Ciclo de vida, que llena huecos.
- **`F-007` a `F-010` siguen sin construir.** Sus historias están nombradas en la épica.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
