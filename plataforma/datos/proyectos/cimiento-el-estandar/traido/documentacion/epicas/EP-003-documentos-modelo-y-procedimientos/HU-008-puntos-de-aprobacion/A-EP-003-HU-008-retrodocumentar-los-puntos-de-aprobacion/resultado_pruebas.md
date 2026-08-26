# Resultado de Pruebas — Fase A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Ejecución caso por caso

### CA-01 · La lista existe y dice qué se aprueba en cada punto

**El plan decía que la lista solo vivía dentro del procedimiento del director, y que por eso un proyecto que hereda no la recibe. Es falso.**

La lista está en [`plantillas/ciclo-vida-proyectos/10-estado-fase.md`](../../../../../plantillas/ciclo-vida-proyectos/10-estado-fase.md), que **sí** se hereda: es el molde con el que cada fase escribe en qué estación va. Trece estaciones, y las que exigen al usuario llevan su marca:

| Estación | Puerta |
|---|---|
| 2 · Proponente, alcance | 👤 alcance aprobado |
| 3 · Escritor de épica | 👤 épica aprobada |
| 4 · Escritor de historia | 👤 HUs aprobadas |
| 5 · Escritor de especificación | 👤 especificación aprobada |
| 7 · Planificador de tareas | 👤 plan más pruebas aprobados |
| 12 · Commit | 👤 autorizado |
| 13 · Publicación | 👤 autorizado |

**Siete puntos de aprobación**, cada uno diciendo qué se aprueba. Y no es una lista decorativa: cada fase de este repositorio la lleva llena, con las casillas marcadas hasta donde llegó.

**Resultado del criterio: Cumple**, y el plan estaba equivocado sobre dónde vive.

### CA-02 · Una respuesta ambigua no habilita

Lo exige el núcleo, que es lo más fuerte que hay: [`00·N1`](../../../../../base/00-nucleo-blindado.md) pide aprobación **explícita** para todo cambio de estado, y la palabra está en el título de la regla.

**No hay comprobación automática, y no la puede haber:** decidir si un «bueno, dale» es explícito o ambiguo es leer, y un programa no opina. Queda del lado del criterio humano, que es donde `M9` lo pone.

**Resultado del criterio: Cumple**, como regla. Sin quien lo compruebe, y dicho.

### CA-03 · Aprobar una cosa no aprueba la siguiente

Es una regla propia y con nombre: [`02·F25`](../../../../../base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md).

> Decir «arranque con X» autoriza **abrir la fase**, no ejecutar su plan detallado: son dos permisos distintos y el segundo se pide aparte, con el plan a la vista.

**Y esta misma jornada lo usó de verdad.** El usuario aprobó ejecutar dos pendientes; eso no aprobó el commit, que se pidió aparte y sigue sin darse. Siete fases están detenidas en la estación 12 justamente por esto.

**Resultado del criterio: Cumple.**

---

## 2. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Media | El plan afirmaba que la lista no llega a los proyectos que heredan. Llega: está en el molde del estado de fase | **Cerrado** al comprobarlo |
| D-02 | Baja | La lista vive en un **molde**, no en `base/`. Quien busque la exigencia en el cuerpo de reglas no la encuentra como lista; encuentra `N1`, `F4` y `F25` sueltas. Funciona, pero se descubre por casualidad | **Abierto** |

---

## 3. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, la lista existe y dice qué se aprueba | Siete puntos marcados en el molde heredado, y llenos en cada fase real | Cumple |
| CA-02, una respuesta ambigua no habilita | `00·N1`, que pide aprobación explícita. Sin comprobación automática, y dicho | Cumple |
| CA-03, aprobar una cosa no aprueba la siguiente | `02·F25`, y su uso real en esta jornada | Cumple |

---

## 4. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios están cubiertos por documentos que un proyecto sí recibe, y dos de ellos se usaron de verdad esta misma jornada. Queda anotado el D-02: la lista se hereda dentro de un molde y no como parte del cuerpo de reglas, así que se encuentra si uno abre el molde.

---

## 5. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | La lista de siete puntos | `plantillas/ciclo-vida-proyectos/10-estado-fase.md` §1 |
| EV-02 | La exigencia de aprobación explícita | `00·N1` |
| EV-03 | Que un permiso no arrastra al siguiente | `02·F25`, y las siete fases detenidas hoy en la estación 12 |

---

## 6. Ciclos anteriores

Ninguno.
