# Estado de fase — Fase `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras` (módulo Aprobaciones)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras` |
| **Módulo** | Aprobaciones |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/epica.md](../../epica.md) · [documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-002-ver-que-esta-aprobado-y-que-no/HU-002-ver-que-esta-aprobado-y-que-no.md](../HU-002-ver-que-esta-aprobado-y-que-no.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ La ficha exige decirlo con palabras, no con color |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-017 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Tres estados, no dos |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 4 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Ninguno de los tres estados es «rechazado».** La plataforma no rechaza nada: registra lo que pasó.

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
| T-01 | Terminada | Los tres estados, con su frase |
| T-02 | Terminada | La comparación de huellas |
| T-03 | Terminada | Desde cuándo y por quién |
| T-04 | Terminada | Que lo sin aprobación aparezca |
| T-05 | Terminada | La orden de consola |
| T-06 | Terminada | 4 pruebas |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un estado que admite «hubo un juicio y ya no vale» necesita su propio nombre | [`S-111`](../../../../senales.md) |
| Lo que se comunica solo con color no lo puede leer todo el mundo | [`S-111`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Sin pantalla**, como el resto de los módulos de esta etapa.
- **Solo se listan los documentos con alguna aprobación.** Listar todos es del módulo Expediente.

---

## 4. Si se bloqueó

No se bloqueó.
