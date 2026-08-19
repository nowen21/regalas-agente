# Plan de Trabajo — Fase A-EP-001-HU-012-inventario-de-acciones-y-riesgo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer, en qué orden y sobre qué archivos**, antes de tocar código. Se presenta al usuario y **no se ejecuta nada hasta su OK explícito** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-012-inventario-de-acciones-y-riesgo` |
| **Módulo** | Capítulo `00 · Núcleo blindado` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-012](../HU-012-inventario-de-acciones-y-riesgo.md) |
| **CA que cubre** | `CA-01`, `CA-02`, `CA-03`, `CA-04` — los cuatro |
| **Rama** | la de trabajo actual |
| **Fecha** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **funcionalidad nueva**. No existe ninguna lista de lo que el agente puede hacer. Baja del [pendiente 13](../../../../../pendientes/hecho/inventario-y-riesgo-de-las-acciones-del-agente.md) por [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md).

---

## 1. Objetivo y alcance

**Objetivo.** Escribir el inventario de lo que el agente puede hacer, clasificado por **qué tan difícil es deshacerlo**, y que de esa clasificación se siga **qué exige cada clase antes de ejecutarse**.

**El problema, en una línea.** Hoy [`00·N1`](../../../../../base/00-nucleo-blindado.md) pide aprobación para **todo** cambio de estado. Corregir una coma en un README y borrar un archivo que no está en git piden exactamente lo mismo.

> **Y un control parejo no protege más, protege menos.** Cuando la misma exigencia cubre lo trivial y lo grave, lo que pasa en la práctica es que se aprueba **en bloque** — y entonces también quedó aprobado lo grave. El pendiente lo dice así: *«la rigidez pareja no protege más»*.

**Entra en esta fase**

- El anexo del capítulo `00` con la lista de clases de acción y su nivel.
- La escala fija de tres niveles, y qué exige cada uno.
- La cláusula de lo que la lista no nombra.
- La comprobación de que la lista no tiene huecos.

**No entra**

- **Cambiar `N1` a `N6`.** Siguen vigentes tal como están: la lista los **organiza**, no los reemplaza. Es el criterio transversal de no regresión de la historia.
- Aplicar la clasificación a los enganches. Eso es otra fase.

---

## 2. Análisis previo — línea base verificada

**Comprobado el 2026-08-18 contra el repositorio, no de memoria** ([`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)):

| Qué se comprobó | Qué hay |
|---|---|
| ¿Existe alguna lista de acciones? | **No.** Ni en `base/`, ni en `anatomia/`, ni en `validadores/` |
| ¿Qué cubre hoy el núcleo? | Seis reglas: `N1` general, y `N2` git, `N4` datos reales, `N5` masivas, `N6` secretos, `N3` no romper para pasar |
| ¿Qué queda sin nombrar? | Borrar un archivo **no versionado**, escribir configuración de la máquina, correr un guion del proyecto que **sale a la red** |
| ¿Dónde caen hoy esas tres? | En `N1`, junto con cambiarle una coma a un README |

**El anexo va en `base/00-identidad-y-rol/`, al lado del de marcadores.** El capítulo `00 · Núcleo blindado` es un archivo suelto sin carpeta propia, y [`base/00-identidad-y-rol/marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md) es el precedente de un anexo del `00` que vive ahí. **No se abre carpeta nueva para el núcleo en esta fase**: sería reestructurar el capítulo más delicado del repositorio para colgarle un anexo.

---

## 3. Desglose de tareas por criterio de aceptación

| # | Tarea | CA | Sobre qué archivo |
|---|---|---|---|
| T-01 | Escribir las **diez clases de acción** que la historia enumera en su `CA-01`, cada una con lo que incluye y lo que no | CA-01 | `base/00-identidad-y-rol/acciones-y-riesgo.md` (nuevo) |
| T-02 | Fijar la **escala de tres niveles** — se deshace sola · se deshace con trabajo · no se deshace — y qué exige cada uno | CA-02 | el mismo |
| T-03 | Poner a cada clase su nivel y **su ejemplo de qué pasa si sale mal**, que es lo que `CA-02` exige junto al nivel | CA-02 | el mismo |
| T-04 | Escribir, para dos filas de niveles opuestos, **qué pide cada una** — y que sea distinto | CA-03 | el mismo |
| T-05 | Escribir la cláusula de **lo que la lista no nombra**: se trata como el nivel más alto, se dice, y se anota para clasificarla | CA-04 | el mismo |
| T-06 | Enlazar el anexo desde `00-nucleo-blindado.md` y desde el índice del capítulo `00` | los cuatro | `base/00-nucleo-blindado.md` · `base/00-identidad-y-rol/base.md` |
| T-07 | Comprobación: **ninguna clase sin nivel, ninguna sin ejemplo, ningún nivel fuera de la escala** | CA-01, CA-02 | `validadores/acciones.py` (nuevo) |
| T-08 | Subcomando `validar.py acciones` y su registro en `reglas-validables.md` | CA-01, CA-02 | `validadores/validar.py` · `validadores/reglas-validables.md` |
| T-09 | Casos automatizados | todos | `validadores/tests/test_las_acciones_tienen_su_riesgo.py` (nuevo) |
| T-10 | Versionar y cerrar la trazabilidad | — | `VERSION` · `CHANGELOG.md` · la HU |

---

## 4. Secuencia de ejecución

`T-01` → `T-02` → `T-03` → `T-04` → `T-05` → `T-06` → `T-07` → `T-08` → `T-09` → `T-10`.

**El anexo primero y el validador después, a propósito.** Escribir el programa antes obligaría a inventar la forma de la tabla desde el código, y la forma la decide lo que hay que decir.

---

## 5. Verificación de criterios de aceptación

| CA | Cómo se verifica |
|---|---|
| CA-01 | Las diez herramientas de la historia se buscan en la lista; el conteo de huérfanas tiene que dar **cero** |
| CA-02 | Se recorre la tabla: ninguna fila con nivel y sin ejemplo, ningún nivel fuera de la escala |
| CA-03 | Se comparan dos filas de niveles opuestos: **lo que exigen tiene que ser distinto**. Si es igual, la clasificación no sirvió |
| CA-04 | El caso está escrito y dice las tres cosas: tratarla como lo peor, decirlo, y anotarla |

---

## 6. Datos y ambiente de prueba

Carpetas temporales desechables. **Nunca sobre un proyecto real** ([`00·N4`](../../../../../base/00-nucleo-blindado.md)).

---

## 7. Reversión

Un anexo nuevo y un validador nuevo: se borran los archivos y se revierte el commit. **Nada de lo existente cambia de exigencia**, así que no hay estado que restaurar.

---

## 9. Reglas aplicadas

`00·N1` (lo que esta fase organiza) · `20·M2` (un tema, un capítulo, un dueño) · `20·M5` (el anexo no es una regla: no lleva molde de regla) · `20·M9` (declarar si es validable) · `20·M10` (versionar) · `02·F17` (la línea base se comprobó contra el repositorio).

---

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| R-01 | Que el anexo termine **contradiciendo** a `N1`–`N6` en vez de organizarlos | Cada clase **cita** la regla del núcleo que la cubre, si la hay. Ninguna clase inventa exigencia nueva sobre lo ya blindado |
| R-02 | Que la escala tenga tantos niveles que nadie la use | **Tres**, que es lo que el pendiente propone y lo que se puede recordar sin abrir el archivo |
| R-03 | Que quede como una tabla bonita que el agente no mira | Se declara en `reglas-validables.md` qué se comprueba y qué no. **Lo que no se comprueba se dice** |

---

## 11. Definition of Done

- [ ] Las diez clases están, ninguna sin nivel ni sin ejemplo
- [ ] Dos niveles opuestos exigen cosas distintas
- [ ] La cláusula de lo no nombrado está escrita
- [ ] `validar.py acciones` da cero sobre el anexo
- [ ] `tests/` y `pruebas.py` en verde
- [ ] Versión y registro al día

---

## 13. Cierre

Se llena al cerrar la fase.
