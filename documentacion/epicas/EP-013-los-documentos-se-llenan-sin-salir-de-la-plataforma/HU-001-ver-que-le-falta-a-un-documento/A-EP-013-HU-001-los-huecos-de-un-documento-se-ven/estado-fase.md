# Estado de fase — Fase `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven` (módulo Ciclo de vida)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven` |
| **Módulo** | Ciclo de vida |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/HU-001-ver-que-le-falta-a-un-documento.md](../HU-001-ver-que-le-falta-a-un-documento.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Contado sobre `plantillas/` y sobre los tipos que Importación reconoce |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: se llena por huecos |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-013 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Sin entidades: los huecos se calculan al pedirlos |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 26 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ El defecto grave se encontró midiendo antes de construir |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **Esta fase solo lee.** Escribir es la fase de la `HU-002`. Se separaron porque fallan distinto: contar mal da un número equivocado, escribir mal daña un documento.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | El módulo, registrado |
| T-02 | Terminada | La tabla de moldes: 17 con molde, 2 sin |
| T-03 | Terminada | Las tres clases, y la cita del autor que no es ninguna |
| T-04 | Terminada | Línea, columna y contexto |
| T-05 | Terminada | `que_le_falta`, con las cuentas aparte |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 26 pruebas |
| T-08 | Terminada | **Medido: 54 documentos y 77 huecos**, y comparado con el expediente |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La columna «Depende de» del inventario no es un orden de construcción, y por eso `F-014` nunca estuvo bloqueada | [`S-103`](../../../../senales.md) |
| Una convención de marcado que usa los signos de la prosa no se puede contar: de 341 marcas reales, cero eran huecos | [`S-104`](../../../../senales.md) |
| Medir antes de construir cambió un criterio de aceptación ya aprobado, y costó diez minutos | [`S-104`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Si llenar por huecos resulta cómodo de verdad.** Se responde en la fase de la `HU-002`, llenando un documento real de punta a punta.
- **24 documentos con huecos que el expediente nunca mostró**, todos índices. Aparecieron al comparar las dos cuentas. Llenarlos es trabajo de la `HU-002`; no hace falta pendiente.
- La diferencia con el expediente quedó explicada entera en la §3 del resultado. **El `B-03` está cerrado.**

---

## 4. Si se bloqueó

No se bloqueó.
