# Plan de Trabajo — Fase C-EP-001-HU-009-las-tres-reglas-con-nombre-propio (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-009](../HU-009-reglas-sin-checklist-al-dia.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-001-HU-009-las-tres-reglas-con-nombre-propio` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-009 Poner al día las reglas que no pasan su propio checklist](../HU-009-reglas-sin-checklist-al-dia.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Cuerpo de reglas — la fila 5 del checklist |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** Fase `C` porque la [`A`](../A-EP-001-HU-009-clasificar-las-que-faltan/) cerró el `CA-02` y la [`B`](../B-EP-001-HU-009-el-sello-no-se-contradice/) dejó los sellos coherentes.

**De dónde sale:** el [pendiente 19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) lo pone como **segundo** en su lista de por dónde seguir: *«las tres con nombre propio. Son de una línea cada una y hoy cualquier proyecto que herede el estándar lee el stack de otro»*.

**CA que cubre:** el `CA-01` sobre las reglas que reprueban **la fila 5**, y el transversal de no regresión.

---

## 1. Objetivo y alcance

**Objetivo:** que ninguna regla de `base/` nombre un lenguaje, un framework, un motor, una herramienta del agente ni un módulo de un proyecto real — salvo una, declarada, con su motivo escrito.

**Por qué esta y no el capítulo más grande.** Es el defecto que **daña a quien hereda**, no a quien escribe. Un proyecto que instala el estándar hoy lee reglas redactadas para el stack de otro: no rompe nada, se lee, se entiende a medias y se aplica peor. Y el arreglo es de una línea por regla.

**Fuera de alcance:**

- **Las otras filas.** `C10` sigue teniendo tres exigencias y `C16` sigue duplicando a `C2`. Esta fase toca la fila 5 y nada más; las tres siguen en NO CUMPLE al terminar.
- **[`04·S11`](../../../../../base/04-seguridad.md#s11--escritura-contra-el-almacén-productivo-requiere-autorización-por-operación).** Su propio sello ya decidió que no: ahí el nombre del método **es el argumento** —el punto de la regla es que suena a borrar y escribe—, así que reescribirlo en concepto es parte de partirla. Se respeta esa decisión y no se rehace.
- **Acortar.** Escribir en concepto es más largo que nombrar la herramienta, y se aceptó el costo.

---

## 2. Análisis previo — línea base verificada

**Medido el 2026-08-18, después de que la fase `B` dejara las tablas al día:**

| Regla | Qué nombra |
|---|---|
| [`01·C10`](../../../../../base/01-conducta.md#c10--cada-mensaje-del-usuario-se-evalúa-como-posible-mejora-del-setup) | `SQLite`, `MariaDB`, `React`, `Django` y «este ERP» |
| [`01·C15`](../../../../../base/01-conducta.md#c15--al-replicar-un-patrón-replicar-la-paridad-completa) | «el módulo Aportes», de un proyecto real |
| [`01·C16`](../../../../../base/01-conducta.md#c16--re-lee-justo-antes-de-editar--nunca-sobre-contexto-viejo) | Las órdenes de lectura y edición del agente, y dos del control de versiones |
| [`04·S10`](../../../../../base/04-seguridad.md#s10--no-mates-procesos-globales--solo-pid-exacto-y-estrictamente-necesario) | `node` y `php` — **no estaba en la lista de tres**, lo encontró el programa |

**`C10` es la peor, y por dónde falla.** Es justamente la regla que enseña a decidir si algo es transversal o local, y **su criterio para decidirlo nombraba dos frameworks**: *«¿esta regla tendría sentido en un proyecto React + Django de otra empresa?»*. La pregunta que le pedía al agente hacerse era la que ella misma no pasaba.

**`S10` es la que enseña algo del método.** Su sello **sí había argumentado la fila 5** —para defender `killall`, `pkill` y `taskkill`— y al hacerlo la dio por revisada. Los dos intérpretes estaban tres líneas más arriba. **Un argumento sobre una fila no es una revisión de la fila**, y quien lee el sello ve que alguien la miró sin ver qué parte miró.

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `base/01-conducta.md` | Modificar | Cuerpo y sello de `C10`, `C15`, `C16` |
| `base/04-seguridad.md` | Modificar | Cuerpo y sello de `S10` |
| `validadores/metareglas.py` | Modificar | Lo que al detector se le escapaba |
| `validadores/tests/test_la_base_no_nombra_stack.py` | Nuevo | Los casos |
| `pendientes/19-…md` | Modificar | Lo que esta fase cierra |
| `CHANGELOG.md` · `VERSION` | Modificar | **PARCHE** |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Las órdenes del control de versiones también salen** de `C16` | Dejarlas, por universales | Se comprobó antes de tocar: el capítulo `09` se titula **Control de versiones**, no por la herramienta, y **ninguna otra regla del cuerpo nombraba una orden concreta**. `C16` era la excepción, no la costumbre |
| **`killall`, `pkill` y `taskkill` se quedan** en `S10` | Sacarlos también | No son producto ni framework: son cómo se llama la misma acción en cada sistema, y quitarlos deja la regla sin decir qué prohíbe. Ya estaba razonado el 2026-08-07 y sigue valiendo |
| Al detector se le agrega **solo lo que se le escapó de verdad** | Ampliar la lista por si acaso | `node` y `SoftDeletes` tienen caso real detrás. Una lista inflada por precaución empieza a reportar de más, y una comprobación que reporta de más se apaga |
| La prueba sobre `base/` **no exige cero** | Exigir cero | Queda `S11` vivo a propósito. Exigir cero obligaría a arreglarlo a medias para que la prueba pase, que es justo lo que su sello decidió no hacer |

### 2.7 Dudas por resolver antes de escribir

**Una, y se resolvió mirando el cuerpo:** si las órdenes del control de versiones cuentan como nombre propio. Ver §2.6.

---

## 3. Desglose de tareas

| ID | Tarea | Est. |
|---|---|:--:|
| T-01 | Medir qué reglas reprueban la fila 5, por sello y por programa | 0,5 h |
| T-02 | Reescribir `C10` en concepto | 0,5 h |
| T-03 | `C15` y `C16` | 0,75 h |
| T-04 | `S10`, que no estaba en la lista | 0,25 h |
| T-05 | Resellar las cuatro, remidiendo el largo | 0,75 h |
| T-06 | Lo que al detector se le escapaba | 0,5 h |
| T-07 | Los casos de prueba | 0,75 h |
| T-08 | Versionar y anotar en el 19 | 0,5 h |

**Total estimado:** 4,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02/03/04 → T-05 → T-07.

**T-01 se hace por los dos caminos, sello y programa, y de ahí sale `S10`.** La lista escrita en el pendiente decía tres; el programa encontró una cuarta que ningún sello marcaba.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Estado |
|---|---|---|
| CA-01 · ninguna regla nombra stack, salvo la declarada | `validar.py metareglas`, fila 5 | ☑ |
| Transversal · no regresión | Las dos suites, y el conteo de NO CUMPLE | ☑ |
| Lo que se conserva a propósito queda escrito | Casos dedicados | ☑ |

---

## 6. Datos y ambiente de prueba

El propio cuerpo de reglas, más textos de mentira para los casos del detector.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás.

---

## 8. Producción y migración incremental

**Aditiva y silenciosa.** Un proyecto al día no hace nada; la próxima vez que lea `C10`, `C15`, `C16` o `S10` va a encontrarlas escritas para él y no para otro.

---

## 9. Reglas del estándar aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Que reescribir en concepto cambie lo que la regla exige | Se comparó exigencia por exigencia. Ninguna de las cuatro cambia de norma, y el conteo de NO CUMPLE no se mueve | **Cerrado** |
| B-02 | Que la próxima pasada borre `killall`/`pkill`/`taskkill` creyendo que mejora | Hay caso que lo fija, y el sello dice el motivo | **Cerrado** |
| B-03 | Que el texto en concepto quede más largo y empeore la fila 10 | Pasó en `C10`: de 1724 a 1780. **Se acepta y se dice** — es el precio de que la base sirva a cualquier proyecto, y la fila 10 ya reprobaba | **Cerrado, con costo** |
| B-04 | Que queden nombres que ni el sello ni el programa ven | Es lo que pasó con `S10`. Hoy quedan los que ninguna lista conoce todavía | Abierto — se estrecha cada vez que aparece uno |

---

## 11. Definition of Done

- [x] `C10`, `C15`, `C16` y `S10` sin nombre propio
- [x] Las cuatro reselladas, con el largo remedido
- [x] El detector amplía con lo que se le escapó
- [x] `validar.py metareglas` deja solo `S11`, que está declarado
- [x] Versionada
- [ ] Aceptada por el usuario

---

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
