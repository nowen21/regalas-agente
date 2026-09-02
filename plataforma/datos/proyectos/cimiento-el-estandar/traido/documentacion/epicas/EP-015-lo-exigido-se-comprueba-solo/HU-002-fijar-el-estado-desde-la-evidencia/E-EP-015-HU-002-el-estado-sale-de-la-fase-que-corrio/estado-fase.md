# Estado de fase — Fase `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio` (módulo Comprobaciones)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio` |
| **Módulo** | Comprobaciones |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/epica.md](../../epica.md) · [documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-002-fijar-el-estado-desde-la-evidencia/HU-002-fijar-el-estado-desde-la-evidencia.md](../HU-002-fijar-el-estado-desde-la-evidencia.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 35 funcionalidades, las 35 sin verificar; 7 filas nombran la fase por su letra |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-015 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Se sigue una cadena que ya existía escrita |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 11 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Dos defectos, los dos cerrados acá |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `e4c1808` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — la plataforma corre en la máquina del usuario |

> **Los dos defectos venían de lo mismo:** la convención cambió con el tiempo, y lo escrito antes sigue escrito como antes. Ninguna fase cerrada se reescribió.

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
| T-01 | Terminada | Las funcionalidades del inventario |
| T-02 | Terminada | La trazabilidad, hasta la fase |
| T-03 | Terminada | **Las dos formas de veredicto** |
| T-04 | Terminada | El estado, con su porqué |
| T-05 | Terminada | Las siete filas completadas, con su registro |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 11 pruebas |
| T-08 | Terminada | **14 verificadas de 35** |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un lector que sigue documentos viejos tiene que leer las convenciones viejas | [`S-108`](../../../../senales.md) |
| Una fase cerrada no se reescribe para que un programa la entienda | [`S-108`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **21 funcionalidades sin verificar**, y está bien: nadie las ha construido. Es la respuesta correcta, no una deuda.
- **La columna «Verificado» del inventario** ya no se mantiene a mano.
- **Sin pantalla**, como el resto del módulo.

---

## 4. Si se bloqueó

No se bloqueó.
