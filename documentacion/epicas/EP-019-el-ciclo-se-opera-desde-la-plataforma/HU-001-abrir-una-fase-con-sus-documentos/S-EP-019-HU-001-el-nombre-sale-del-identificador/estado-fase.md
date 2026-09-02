# Estado de fase — Fase `S-EP-019-HU-001-el-nombre-sale-del-identificador` (módulo Ciclo de vida)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `S-EP-019-HU-001-el-nombre-sale-del-identificador` |
| **Módulo** | Ciclo de vida |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-001-abrir-una-fase-con-sus-documentos/HU-001-abrir-una-fase-con-sus-documentos.md](../HU-001-abrir-una-fase-con-sus-documentos.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 209 fases, todas abiertas a mano |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-019 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ El nombre se arma; nada se pisa |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 12 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑  |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **La fase se define por aquello a lo que se niega:** sin historia no se abre, y lo que ya existe no se toca.

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
| T-01 | Terminada | El nombre armado |
| T-02 | Terminada | La carpeta de la historia |
| T-03 | Terminada | Los cinco documentos |
| T-04 | Terminada | No tocar lo que existe |
| T-05 | Terminada | La orden de consola |
| T-06 | Terminada | 12 pruebas |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Lo que más cuidado cuesta de una funcionalidad que crea cosas es aquello a lo que se niega | [`S-114`](../../../../senales.md) |
| Un nombre que se escribe a mano termina no diciendo de dónde cuelga | [`S-114`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Épicas e historias siguen abriéndose a mano.** Se abren una vez cada varias semanas; la fase es la que se repite.
- **Los moldes reales son largos**, y eso no lo mide ninguna prueba.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
