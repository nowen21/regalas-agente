# Resultado de pruebas — Fase A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |
| **HU** | [HU-002](../HU-002-modelos-del-encargo.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-003-HU-002 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Este repositorio, con su árbol real de 7 épicas y 68 HU. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 3 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). Los tres modelos existen, se encadenan en los dos sentidos sin una sola falla, y el de la historia obliga a decir cómo se valida cada criterio. Lo que falla es CP-004: **este repositorio no tiene planteamiento**, que es el primer eslabón del encargo.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | El árbol real: 7 épicas, 68 HU | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-02 | Alta | El modelo de la historia de usuario | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-03 | Alta | Un encargo a medias y uno completo | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md) | CA-01 | Media | El planteamiento de esta casa | **Falla** | EV-02 |

---

### Detalle de CP-001 — Toda HU nombra su épica, y toda épica lista sus HU

Se corrió `trazabilidad.py` sobre el árbol real, que es el que comprueba `DOC16` — el enlace bidireccional.

| Medición, 2026-08-17 | Valor |
|---|---:|
| Épicas | **7** |
| Historias de usuario | **68** |
| Fallas de encadenamiento épica ↔ HU | **0** |

**En los dos sentidos, y no es redundante.** Con un solo lado escrito, borrar el otro no deja rastro: una HU huérfana sigue existiendo y su épica no la extraña. Es la misma razón por la que el índice de recuerdos y el de pendientes se comprueban también en las dos direcciones.

---

### Detalle de CP-002 — Cada criterio dice cómo se valida y cuándo se aprueba

El modelo de la historia de usuario obliga a escribir, por cada criterio, **«Cómo validarlo»** y **«Aprobado cuando»**.

**Sin esas dos, un criterio no se puede comprobar** y la historia entera se vuelve opinión: dos personas leen «el sistema debe ser rápido» y aprueban cosas distintas. Con ellas, el criterio dice qué hacer y qué tiene que salir.

---

### Detalle de CP-003 — El encargo a medias sale reportado

| Qué se probó | Qué salió |
|---|---|
| Una épica sin su documento | Reportada |
| Una HU sin su documento | Reportada |
| Una épica sin historias todavía | **Su sección existe y dice que no hay**: no es lo mismo que falte |
| Una HU sin fases todavía | Igual |

**El tercer y cuarto caso son el transversal de límites**, y la distinción vale: «todavía no hay» es un estado normal al empezar; «falta la sección» es un documento incompleto.

---

### Detalle de CP-004 — El planteamiento que le falta a esta casa

**El modelo existe** —[`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md)— y **este repositorio no lo tiene lleno**.

Es el primer eslabón del encargo: el documento que dice **qué es este proyecto** antes de que haya ninguna épica. Sin él, las 7 épicas cuelgan de nada.

**Ya está anotado**, en el [pendiente 56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md), con una frase que esta fase confirma: *«esta casa reprueba el punto de la cadena que ella misma acaba de escribir»*. Lo que esta fase agrega es que **el modelo funciona**: lo que falta no es el molde, es llenarlo — y eso, dice el pendiente, «no es tarea de código: es decidir qué es este proyecto, y sale de una conversación».

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que los tres modelos existan | Buscándolos en `plantillas/` | Los tres |
| 2 | Cuántas épicas y HU, y si se encadenan | `validar.py trazabilidad` | 7 y 68 · **0 fallas** |
| 3 | Si esta casa tiene planteamiento | Mirándolo | **No** |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 348 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Media | **Este repositorio no tiene planteamiento**, que es el primer eslabón del encargo. Las 7 épicas cuelgan de nada | Ya anotado en el [pendiente 56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md). **No es tarea de esta fase**: llenar el planteamiento es decidir qué es el proyecto, y sale de una conversación con el usuario |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-002-modelos-del-encargo.md#ca-01--los-tres-modelos-existen-y-se-encadenan) | CP-001, CP-004 | Los tres modelos existen y el encadenamiento no tiene fallas. **Pero el primer eslabón está vacío en esta casa** | **No** |
| [CA-02](../HU-002-modelos-del-encargo.md#ca-02--la-historia-trae-criterios-que-se-pueden-comprobar) | CP-002 | El modelo obliga a «cómo validarlo» y «aprobado cuando» | Sí |
| [CA-03](../HU-002-modelos-del-encargo.md#ca-03--un-encargo-llenado-a-medias-se-nota) | CP-003 | El documento que falta se reporta | Sí |
| Transversal · Límites | CP-003 | La épica sin historias y la historia sin fases tienen su sección, diciendo que todavía no hay | Sí |
| Transversal · No regresión | CP-001 | Los 68 documentos ya escritos con estos modelos siguen siendo válidos: 0 fallas | Sí |

**El que no cumple:** el **CA-01**, y no por el modelo sino por su uso en esta casa.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Fallas de encadenamiento | **0** | **0** de 68 HU | Sí |
| Documentos que dejen de ser válidos | **0** | **0** | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** los tres modelos existen, el encadenamiento se comprueba en los dos sentidos y **no tiene una sola falla en 68 historias** — que es la mejor prueba de que los moldes funcionan. Y el de la historia obliga a decir cómo se valida cada criterio, que es lo que separa un requisito de una opinión.

Lo que no se cumple es el CA-01 en su primera mitad: **el planteamiento de esta casa está vacío**. Los modelos se encadenan bien entre sí, y la cadena empieza en un eslabón que nadie llenó.

**Qué falta para que cumpla:** llenar el planteamiento. **No es tarea de esta fase ni de ninguna otra de código**: es decidir qué es este proyecto, y eso sale de una conversación con el usuario. Está anotado en el [pendiente 56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md).

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ModelosDelEncargo`: 4 pruebas, en verde |
| EV-02 | El planteamiento que falta | [Pendiente 56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md) |
| EV-03 | Lo escrito | [`documentacion/documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md) §4.1 |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 348 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
