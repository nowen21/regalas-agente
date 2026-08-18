# Resultado de Pruebas — Fase A-EP-001-HU-011: la regla de buscar antes de preguntar

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-A-EP-001-HU-011](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |
| **Ejecutado por** | El agente |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--la-regla-cubre-los-tres-ca) — cubre los tres CA | ✅ **Pasa**, tras corregir | Ver §2 |
| [CP-002](plan_pruebas.md#cp-002--el-checklist-de-las-veinte-filas) — el checklist | ✅ **Pasa** | 20 filas: 19 ✅ · 0 ❌ · 1 N/A. `validar.py metareglas` no reporta `C23` |
| [CP-003](plan_pruebas.md#cp-003--cabe-en-el-molde) — cabe | ✅ **Pasa**, tras recortar | 368 → 271 → **311** de 320 |
| [CP-004](plan_pruebas.md#cp-004--el-identificador-no-estaba-tomado) — el identificador | ✅ **Pasa** | El mayor del capítulo era `C22`; `C23` no existía |
| [CP-005](plan_pruebas.md#cp-005--queda-clasificada-con-su-motivo) — clasificada | ✅ **Pasa** | En `reglas-validables.md`, con el motivo de por qué es a medias |
| [CP-006](plan_pruebas.md#cp-006--ninguna-corrida-se-rompió) — no regresión | ✅ **Pasa** | Ver §3 |

**6 de 6 ejecutados. 6 pasan. Dos pasaron después de corregir lo que ellos mismos destaparon.**

---

## 2. CP-001 · El caso que el plan marcó como dudoso, y tenía razón

El plan de pruebas escribió, **antes de ejecutar**, que el paso del `CA-03` era el que había que mirar con cuidado y que si no quedaba cubierto se anotara **sin ajustar el criterio para que encajara**.

No estaba cubierto. La primera redacción decía *«si está, se sigue citando dónde»* —el caso en que lo escrito **responde** la pregunta— y no decía nada del caso en que lo escrito **contradice** lo que el usuario acaba de pedir, que es lo que el `CA-03` exige.

**Se corrigió la regla, no el criterio.** El cuerpo pasa a decir *«se sigue citando dónde —o se muestra, si contradice lo pedido—»*, y con eso los tres criterios quedan cubiertos.

> **Es el argumento del plan de pruebas escrito antes.** Leyendo la regla contra la historia sin ese caso escrito, el `CA-03` se habría dado por cubierto: la regla *habla* de lo que está escrito, y de un vistazo parece que lo cubre todo.

---

## 3. CP-006 · No regresión

| Qué se corrió | Resultado |
|---|---|
| `validar.py estandar` | **Sin incumplimientos** |
| `validar.py metareglas` | `C23` no aparece en ningún hallazgo |
| `citas.py` en simulación | **0 enlazadas · 0 reparadas · 0 archivos** |
| `validadores/tests/` | **99 · OK** |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados, los de siempre) |

---

## 4. Lo que apareció y no se arregló  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**La mitad comprobable de `C23` no tiene programa.** Que la respuesta traiga su cita **sí** se puede comprobar, y hoy nada lo hace. Queda declarado en `reglas-validables.md` y es su propia fase.

Es el riesgo `B-03` del plan, y el mismo que el [pendientes/58-nada-hace-cumplir-id9.md](../../../../../pendientes/58-nada-hace-cumplir-id9.md) describe para `ID9`: **una regla de conducta que solo se recuerda no se cumple siempre.**

---

## 5. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | uno: la comprobación de la cita, fuera del alcance declarado en el plan §1 |
| **Ciclos** | 1 |
