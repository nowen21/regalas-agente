# Plan de Trabajo — Fase `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta` |
| **Épica** | [EP-019](../../epica.md) |
| **HU** | [HU-003 Impedir avanzar sin la puerta cumplida](../HU-003-impedir-avanzar-sin-la-puerta-cumplida.md), una sola (`F12.1`) |
| **Módulo** | Ciclo de vida |
| **Especificación del módulo** | [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-013`:** *«que las puertas se cumplan sin depender de que alguien las recuerde»*, y su advertencia: *«una puerta que estorba se termina saltando»*.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** no dejar pasar a la estación siguiente mientras falte lo que esa puerta exige, diciendo cuál falta.

**Son tres puertas y no trece.** Se comprueban las que dejan daño cuando se saltan; las otras diez se marcan a mano y esta comprobación no opina sobre ellas.

**Fuera de alcance:** impedirlo de verdad —el archivo se puede escribir a mano— y las otras diez estaciones.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** la lectura de la tabla que dejó la fase `T`.

**Lo verificado:** los `estado-fase.md` traen el veredicto escrito de tres formas distintas según la época, y la que se lee acá —`Concepto`— es la que usan todas.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/ciclo_de_vida/puertas.py` | Crear | Servicio | Las tres puertas |
| `plataforma/nucleo/ciclo_de_vida/management/commands/puerta_de_fase.py` | Crear | Consola | La orden |
| `plataforma/nucleo/ciclo_de_vida/tests_operacion.py` | Modificar | Prueba | Los tres CA |
| `documentacion/ciclo-de-vida/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

`estaciones.py` no cambia: esta fase lo usa.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Tres puertas, no trece** | Comprobar las trece | Una puerta que estorba se termina saltando, y entonces se saltan todas |
| **El motivo va siempre, también en el sí** | Motivo solo al rechazar | Quien lee un sí tiene que poder comprobarlo sin volver al documento |
| **Una estación sin puerta comprobable lo dice** | Dejarla pasar en silencio | Un sí callado se lee como «lo comprobé», y no lo comprobó |
| **Se declara que no es un candado** | Presentarlo como que impide | Una ayuda que se presenta como garantía hace que la gente deje de mirar (`S-109`) |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Las tres puertas comprobables | Servicio | 1,5 h | — | CA-01 y CA-03 | EV-01 |
| T-02 | El veredicto de las pruebas | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-03 | El motivo, siempre | Servicio | 30 min | T-02 | CA-03 | EV-01 |
| T-04 | La orden de consola | Consola | 1 h | T-03 | — | EV-01 |
| T-05 | Las pruebas de los tres CA | Test | 1,5 h | T-04 | Todos | EV-01 |

**Total estimado:** 5,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con la estación 7 marcada y sin marcar | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Con los tres veredictos posibles | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Leyendo los motivos de los tres rechazos | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/ciclo_de_vida/tests_operacion.py` |

---

## 6. Datos y ambiente de prueba

Tablas de estaciones de mentiras, de trece y de menos, con las dos marcas. Y **la corrida contra las 209 fases reales del repositorio**, que es de solo lectura.

---

## 7. Reversión / rollback  ·  Q11

**Estas dos fases solo leen.** Se quita el archivo y no queda rastro; ninguna fase del repositorio se modifica.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `02·F0`, y `02·F7`, que prohíbe cerrar una fase con trazabilidad incompleta.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que se presente como candado y la gente deje de mirar** | **Alto** | Se declara en el código y en la documentación que no lo es | Cerrado |
| B-02 | Que trece puertas estorben y se salten todas | Alto | Se comprueban tres | Cerrado |
| B-03 | Que un sí se lea como «lo comprobé» sin haberlo hecho | Medio | La estación sin puerta comprobable lo dice | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que el rechazo nombra la puerta
- [x] Escrito que no es un candado
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
