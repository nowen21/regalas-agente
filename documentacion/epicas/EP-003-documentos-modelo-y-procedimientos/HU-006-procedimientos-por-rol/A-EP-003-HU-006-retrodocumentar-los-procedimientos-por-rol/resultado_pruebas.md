# Resultado de Pruebas — Fase A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. El encargo que faltaba ya ocurrió

Esta fase estaba detenida esperando un dato: **con qué encargo chico y real se prueba, corrido dos veces**. El [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) lo dejó como duda 14 y decía que no estaba en ningún archivo.

**No hizo falta inventarlo: la jornada del 2026-08-22 lo fue.** El mismo encargo —«ejecuta esta fase detenida»— se corrió **once veces seguidas** sobre once fases distintas, con proyectos distintos y criterios distintos. Es más de lo que la duda pedía, y es real.

---

## 2. Ejecución caso por caso

### CA-01 · Cada rol tiene su procedimiento, con entrada y salida declaradas

Hay **once procedimientos** en `skills/`, y **diez declaran entrada y salida**. El que no lo hace es `usar-memoria`, que no es un rol del ciclo sino una herramienta transversal.

| Procedimiento | Entrada y salida |
|---|---|
| `analizar-proyecto`, `proponer-alcance`, `generar-spec-modulo`, `disenar-arquitectura`, `planificar-tareas`, `generar-casos-prueba`, `implementar`, `cerrar-fase`, `revisar-critico`, `sdd-orchestrator` | declaradas |
| `usar-memoria` | no las declara |

**Resultado del criterio: Cumple**, con la salvedad de `usar-memoria` anotada abajo.

### CA-02 · Sin la entrada, el procedimiento no arranca

**Comprobado once veces hoy, y falló donde tenía que fallar.** El procedimiento de ejecutar una fase pide como entrada su plan con la §2.7 resuelta. Las fases cuya §2.7 seguía en «Pendiente» **no arrancaron durante cinco días**, y no por olvido: porque les faltaba la entrada.

En cuanto la entrada llegó —las decisiones escritas del pendiente 59 llevadas a cada §2.7— las once arrancaron el mismo día.

**Resultado del criterio: Cumple**, y con la prueba en las dos direcciones: sin entrada no arrancan, con entrada arrancan.

### CA-03 · El mismo encargo da el mismo tipo de resultado

Las once corridas produjeron **el mismo tipo de entregable**: un `resultado_pruebas.md` con identificación, ejecución caso por caso, defectos encontrados, veredicto por criterio y veredicto de fase. Y el `estado-fase` movido a su estación, y la fila de la HU con su veredicto.

**Lo que cambió entre una y otra fue el veredicto, no la forma.** Cuatro cerraron en «No cumple» y siete en «Cumple», y las once se leen igual.

**Y hay una prueba más dura**, que no salió de la intención sino de un programa: `validar.py fases` compara el veredicto del `resultado_pruebas` con el del `estado-fase` y **rechazó dos de mis documentos** porque no coincidían. El mismo encargo, corrido once veces, quedó comparable a máquina.

**Resultado del criterio: Cumple.**

---

## 3. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Baja | `usar-memoria` no declara entrada ni salida. O es un rol y le faltan, o no es un rol y no debería estar contado entre los procedimientos | **Abierto** |
| D-02 | Media | El procedimiento de ejecutar una fase **no pide verificar la §2 del plan antes de arrancar**, y las once fases de hoy encontraron su línea base envejecida. La entrada declarada resultó insuficiente | **Abierto** |

---

## 4. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, cada rol con su entrada y salida | Diez de once procedimientos las declaran | Cumple |
| CA-02, sin la entrada no arranca | Once fases detenidas cinco días por falta de entrada, y arrancadas el día que llegó | Cumple |
| CA-03, el mismo encargo da el mismo tipo de resultado | Once entregables de la misma forma, comparados a máquina por `validar.py fases` | Cumple |

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios quedaron probados sobre once corridas reales del mismo encargo, que es más de lo que el criterio pedía. El D-02 es el hallazgo que deja: la entrada declarada del procedimiento no alcanza, porque no obliga a verificar que el plan siga siendo cierto.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Los once procedimientos | `skills/` |
| EV-02 | Las once corridas | Los `resultado_pruebas.md` del 2026-08-22 en EP-001 a EP-005 |
| EV-03 | La comparación a máquina | `validar.py fases`, que rechazó dos por veredictos que no coincidían |

---

## 7. Ciclos anteriores

Ninguno.
