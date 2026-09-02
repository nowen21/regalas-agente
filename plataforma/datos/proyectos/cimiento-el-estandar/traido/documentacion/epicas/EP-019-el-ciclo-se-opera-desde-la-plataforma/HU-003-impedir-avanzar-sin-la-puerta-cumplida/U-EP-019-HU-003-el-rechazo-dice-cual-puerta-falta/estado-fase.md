# Estado de fase — Fase `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta` (módulo Ciclo de vida)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta` |
| **Módulo** | Ciclo de vida |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-003-impedir-avanzar-sin-la-puerta-cumplida/HU-003-impedir-avanzar-sin-la-puerta-cumplida.md](../HU-003-impedir-avanzar-sin-la-puerta-cumplida.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Las puertas dependen hoy de que alguien las recuerde |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-019 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Tres puertas, no trece |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 7 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑  |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `e6afdf0` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Con esta fase cierra `EP-019`.** Y queda escrito lo que no hace: no impide, avisa.

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
| T-01 | Terminada | Las tres puertas |
| T-02 | Terminada | El veredicto |
| T-03 | Terminada | El motivo, siempre |
| T-04 | Terminada | La orden de consola |
| T-05 | Terminada | 7 pruebas |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una puerta que estorba se termina saltando, y con ella las que sí importaban | [`S-114`](../../../../senales.md) |
| Un veredicto que deja pasar también necesita decir por qué | [`S-114`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **No impide de verdad**, y así se declara.
- **Las otras diez estaciones no se comprueban**, a propósito.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
