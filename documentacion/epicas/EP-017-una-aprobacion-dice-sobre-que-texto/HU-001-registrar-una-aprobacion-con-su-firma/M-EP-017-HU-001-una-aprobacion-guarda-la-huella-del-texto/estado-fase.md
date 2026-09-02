# Estado de fase — Fase `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto` (módulo Aprobaciones)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto` |
| **Módulo** | Aprobaciones |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/epica.md](../../epica.md) · [documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-001-registrar-una-aprobacion-con-su-firma/HU-001-registrar-una-aprobacion-con-su-firma.md](../HU-001-registrar-una-aprobacion-con-su-firma.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 21 aprobaciones escritas a mano, y **ninguna dice sobre qué texto** |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-017 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ **Es el segundo módulo con entidad propia**, y se explica por qué |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 7 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **El texto no sabe quién lo aprobó.** Es la razón de que esta sí guarde, cuando ningún otro módulo lo hace.

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
| T-01 | Terminada | La entidad, con su huella y su tamaño |
| T-02 | Terminada | Aprobar, leyendo el texto que hay |
| T-03 | Terminada | Rechazar lo que no existe |
| T-04 | Terminada | El registro en la auditoría |
| T-05 | Terminada | La historia |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 7 pruebas |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Lo que se puede derivar del texto se calcula; lo que ocurrió y el texto no sabe, se guarda | [`S-111`](../../../../senales.md) |
| Una aprobación sin la huella del texto es lo mismo que una marca escrita a mano | [`S-111`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Las 21 marcas escritas a mano siguen ahí.** Migrarlas sería inventar aprobaciones.
- **No se comprueba quién aprueba.** Es la misma confianza que rige el resto.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
