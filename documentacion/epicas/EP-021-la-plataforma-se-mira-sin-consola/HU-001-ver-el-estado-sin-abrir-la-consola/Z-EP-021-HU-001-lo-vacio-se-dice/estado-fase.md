# Estado de fase — Fase `Z-EP-021-HU-001-lo-vacio-se-dice` (módulo Avisos, Ciclo de vida, Comprobaciones, Aprobaciones y Memoria)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `Z-EP-021-HU-001-lo-vacio-se-dice` |
| **Módulo** | Avisos, Ciclo de vida, Comprobaciones, Aprobaciones y Memoria |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-021-la-plataforma-se-mira-sin-consola/epica.md](../../epica.md) · [documentacion/epicas/EP-021-la-plataforma-se-mira-sin-consola/HU-001-ver-el-estado-sin-abrir-la-consola/HU-001-ver-el-estado-sin-abrir-la-consola.md](../HU-001-ver-el-estado-sin-abrir-la-consola.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Trece módulos, dos con pantalla |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-021 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/avisos/spec.md](../../../../avisos/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Solo mirar, y las vistas no calculan |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 15 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ La ruta comodín se vio a tiempo |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Lo que costó no fue mostrar: fue el caso vacío.** Son cinco, y es lo primero que ve un proyecto recién conectado.

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
| T-01 | Terminada | El tablero |
| T-02 | Terminada | Las fases |
| T-03 | Terminada | Las funcionalidades |
| T-04 | Terminada | Las aprobaciones y la memoria |
| T-05 | Terminada | El caso vacío de cada una |
| T-06 | Terminada | Ningún cero donde no se sabe |
| T-07 | Terminada | Las rutas y los enlaces |
| T-08 | Terminada | 15 pruebas |
| T-09 | Terminada | Las cinco §7 |

**Hechas:** 9 de 9. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una pantalla en blanco se lee como un error de la plataforma, y casi nunca lo es | [`S-119`](../../../../senales.md) |
| Una advertencia que vive en otro archivo no se lee: viaja impresa con los datos | [`S-119`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Seis módulos siguen sin pantalla:** Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén.
- **No se puede cambiar nada desde la pantalla**, y así se quiso.
- **No hay prueba de cómo se ven**, solo de lo que dicen.

---

## 4. Si se bloqueó

No se bloqueó.
