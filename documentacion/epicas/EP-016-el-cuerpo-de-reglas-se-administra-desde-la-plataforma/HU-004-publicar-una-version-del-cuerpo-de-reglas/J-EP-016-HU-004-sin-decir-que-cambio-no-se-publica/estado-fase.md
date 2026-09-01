# Estado de fase — Fase `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica` (módulo Reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica` |
| **Módulo** | Reglas |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-004-publicar-una-version-del-cuerpo-de-reglas/HU-004-publicar-una-version-del-cuerpo-de-reglas.md](../HU-004-publicar-una-version-del-cuerpo-de-reglas.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 197 entradas en el registro, y el tipo escrito en dos órdenes |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-016 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Usa la puerta de `F-022`; no la reescribe |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 13 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `4c0de39` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Con esta fase se cierra la vuelta de la columna de dependencias** que parecía impedir arrancar la versión 3.

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
| T-01 | Terminada | La entrada del registro, recortada |
| T-02 | Terminada | Su tipo, **en los dos órdenes** |
| T-03 | Terminada | El número libre |
| T-04 | Terminada | La puerta |
| T-05 | Terminada | Todo lo que falte, junto |
| T-06 | Terminada | Escribir solo si no falta nada |
| T-07 | Terminada | La orden de consola |
| T-08 | Terminada | 13 pruebas |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La entrada del registro es prosa y no se genera: generada diría lo mismo siempre | [`S-110`](../../../../senales.md) |
| Lo que falta se dice todo junto: de a uno obliga a intentar tres veces | [`S-110`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La puerta se simula en las pruebas.** Correrla de verdad tarda dos minutos por prueba.
- **Sin pantalla**, como el resto del módulo.

---

## 4. Si se bloqueó

No se bloqueó.
