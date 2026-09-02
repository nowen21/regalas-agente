# Estado de fase — Fase `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente` (módulo Memoria)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente` |
| **Módulo** | Memoria |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/epica.md](../../epica.md) · [documentacion/epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/HU-001-guardar-lo-aprendido/HU-001-guardar-lo-aprendido.md](../HU-001-guardar-lo-aprendido.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ La memoria ya vive en el repositorio: `01·C19` lo decidió |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-018 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/memoria/spec.md](../../../../memoria/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Sin entidad: el texto es la verdad |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 6 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `d4bf878` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Ninguna prueba toca la carpeta real de recuerdos.** Todas trabajan sobre carpetas temporales.

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
| T-01 | Terminada | Leer la carpeta y el índice |
| T-02 | Terminada | Separar vigentes de dados de baja |
| T-03 | Terminada | Buscar por palabra |
| T-04 | Terminada | Guardar sin pisar |
| T-05 | Terminada | El resumen |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 6 pruebas |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna. Dos bloqueos cerrados y uno declarado.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Cuando el hecho **es** el texto, guardar una copia en la base crea dos verdades | [`S-112`](../../../../senales.md) |
| Un módulo que solo tiene que no perder nada necesita una prueba de que no pisa | [`S-112`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Nada revisa si un recuerdo sigue siendo cierto.** Declarado y aceptado.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
