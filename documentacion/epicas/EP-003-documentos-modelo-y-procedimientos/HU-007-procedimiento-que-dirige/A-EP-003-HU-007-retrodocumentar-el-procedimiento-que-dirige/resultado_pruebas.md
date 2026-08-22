# Resultado de Pruebas — Fase A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

**El encargo que esta fase esperaba también ocurrió solo:** la jornada del 2026-08-22 recorrió las estaciones sobre once fases, cuatro de ellas construyendo de cero.

---

## 1. Ejecución caso por caso

### CA-01 · Llama a los procedimientos en orden

El procedimiento que dirige es [`skills/sdd-orchestrator`](../../../../../skills/sdd-orchestrator/SKILL.md), y su tabla nombra las trece estaciones con el procedimiento de cada una y quién cierra su puerta:

| Estación | Procedimiento | Puerta |
|---|---|---|
| 1 | `analizar-proyecto` | interna |
| 2 | `proponer-alcance` | **usuario** |
| 7 | `planificar-tareas` | **usuario** |
| 8 | `implementar` | interna |
| 9 | `cerrar-fase` | interna |

**Y hoy se recorrió en ese orden.** Las cuatro fases construidas de cero —el guardián de sesiones, la comprobación del encuadre, la limpieza de los moldes y el recuento— pasaron por análisis, plan, implementación y cierre, en ese orden, cada una con sus documentos.

**Resultado del criterio: Cumple.**

### CA-02 · Se detiene donde aprueba una persona

**Es el criterio que más veces se ejecutó hoy, y siempre paró donde debía.**

| Momento | Qué pasó |
|---|---|
| Estación 7, plan aprobado | El usuario ordenó ejecutar dos pendientes, y esa orden se tomó como la aprobación de sus planes. Quedó dicho en cada fase |
| Estación 12, commit | **Once fases están detenidas ahí.** El usuario aprobó el trabajo varias veces y **nunca aprobó el commit**, y el agente no lo hizo |
| Una decisión que no era del agente | La del capítulo completo al escribir un archivo se **devolvió** al usuario, porque contradecía el `CA-01` de su historia |

Que once fases lleven horas paradas en la estación 12 no es una falla: **es el criterio funcionando**.

**Resultado del criterio: Cumple.**

### CA-03 · El trabajo se retoma en otra sesión sin perder el hilo

**Comprobado sobre cinco días de distancia, que es lo más lejos que se ha probado.**

Los planes de estas once fases se escribieron y aprobaron el **2026-08-17**. Sus dudas se decidieron el **2026-08-18**, en otra sesión. Se ejecutaron el **2026-08-22**, en una tercera. Ninguna de las tres compartió memoria con las otras, y el hilo se retomó leyendo lo escrito: el plan, la §2.7 y el estado de fase.

**Y salió un límite que hay que decir.** El hilo se retomó, pero **la línea base de cada plan había envejecido**: las once encontraron que su §2 afirmaba cosas que ya no eran ciertas. El documento sirvió para saber qué había que hacer; **no sirvió para saber qué era verdad**.

**Resultado del criterio: Cumple**, con el límite anotado como defecto.

---

## 2. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Alta** | El procedimiento que dirige no manda **verificar la línea base del plan** al retomarlo. Un plan aprobado se lee como verdad, y a los cinco días ya no lo es. Las once fases de hoy lo encontraron | **Abierto** |
| D-02 | Baja | La estación 12 no tiene forma de saber cuánto lleva esperando. Once fases detenidas ahí se ven igual que una | **Abierto** |

---

## 3. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, llama a los procedimientos en orden | La tabla de trece estaciones, y cuatro fases construidas hoy en ese orden | Cumple |
| CA-02, se detiene donde aprueba una persona | Once fases paradas en la estación 12, y una decisión devuelta | Cumple |
| CA-03, se retoma sin perder el hilo | Tres sesiones distintas en cinco días, sobre los mismos once planes | Cumple |

---

## 4. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios quedaron probados sobre trabajo real repartido en tres sesiones y cinco días, no sobre un ejemplo. El D-01 es lo que la fase deja como aprendizaje, y es de fondo: **retomar el hilo y retomar la verdad no son lo mismo**, y el procedimiento solo garantiza lo primero.

---

## 5. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Las trece estaciones con su procedimiento | `skills/sdd-orchestrator/SKILL.md` |
| EV-02 | Las once fases detenidas en la estación 12 | Sus `estado-fase.md` del 2026-08-22 |
| EV-03 | Los cinco días entre el plan y su ejecución | Fecha de aprobación 2026-08-17, ejecución 2026-08-22 |
| EV-04 | La línea base envejecida | El §1 de cada `resultado_pruebas.md` de hoy |

---

## 6. Ciclos anteriores

Ninguno.
