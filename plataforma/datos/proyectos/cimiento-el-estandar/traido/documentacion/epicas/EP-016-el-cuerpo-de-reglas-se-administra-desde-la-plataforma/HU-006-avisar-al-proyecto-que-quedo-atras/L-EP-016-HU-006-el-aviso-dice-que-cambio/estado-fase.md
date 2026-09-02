# Estado de fase — Fase `L-EP-016-HU-006-el-aviso-dice-que-cambio` (módulo Reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `L-EP-016-HU-006-el-aviso-dice-que-cambio` |
| **Módulo** | Reglas |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-006-avisar-al-proyecto-que-quedo-atras/HU-006-avisar-al-proyecto-que-quedo-atras.md](../HU-006-avisar-al-proyecto-que-quedo-atras.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ **143 de 197 entradas reconocidas**, la más reciente la 34.2.0 |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-016 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Tres respuestas, no dos |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 5 pruebas nuevas, **y el estándar tocado y versionado** |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `4c0de39` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Esta fase tocó el estándar**, y por eso se versionó como **PARCHE 37.2.1**, con su entrada en el registro. `20·M10` lo exige.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Uno, declarado: 35 entradas viejas del registro siguen sin reconocerse |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | **La medición que explica la fase**: 143 de 197 |
| T-02 | Terminada | El lector con los dos órdenes |
| T-03 | Terminada | Versionado como PARCHE 37.2.1 |
| T-04 | Terminada | Comprobar que la versión existió |
| T-05 | Terminada | Las versiones del tramo |
| T-06 | Terminada | Cuáles obligan a migrar |
| T-07 | Terminada | La orden de consola |
| T-08 | Terminada | 5 pruebas |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un aviso que sale vacío se ve igual que uno que no tiene nada que decir, y así llevaba 54 versiones | [`S-110`](../../../../senales.md) |
| Tercera vez en el día: una convención cambió y el lector se quedó atrás | [`S-110`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **35 entradas viejas del registro siguen sin reconocerse.** Están declaradas: no afectan el tramo de nadie que esté al día.
- **Enchufarlo al aviso que ya da el módulo Proyectos** no está: hoy es una orden aparte.
- **Sin pantalla**, como el resto del módulo.

---

## 4. Si se bloqueó

No se bloqueó.
