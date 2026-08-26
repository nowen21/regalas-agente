# Resultado de Pruebas — Fase B-EP-003-HU-010: los nombres de rol en español

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| Caso | Veredicto |
|---|---|
| CP-001 · ningún término en inglés | ✅ **Pasa** |
| CP-002 · el reemplazo no toca de más | ✅ **Pasa** |
| CP-003 · sin enlaces rotos | ✅ **Pasa** |
| CP-004 · `ID6` resellada | ✅ **Pasa** |
| CP-005 · no regresión | ✅ **Pasa** — `tests/` 187 · `pruebas.py` 357 · `validar.py estandar` limpio |

**5 de 5.**

---

## 2. Qué cambió

**211 apariciones en 39 archivos.** Trece nombres de rol y la palabra «spec».

| Antes | Ahora |
|---|---|
| Explorer · Proposer · Designer | Explorador · Proponente · Diseñador |
| Épica Writer · HU Writer · Spec Writer | Escritor de épica · de historia · de especificación |
| Task Planner · Implementer · Verifier | Planificador de tareas · Implementador · Verificador |
| Reviewer · Orchestrator · Researcher | Crítico · Orquestador · Investigador |
| spec | especificación |

**Cuatro archivos renombrados** con `cerrar.mover`, que arrastró **149 enlaces**: `02·F2`, `13·DOC3`, `13·DOC6` y la plantilla de especificación de módulo.

---

## 3. Lo que apareció · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**Ocho enlaces rotos que `mover` no ve.** Las plantillas citan con el marcador `«RUTA-ESTANDAR»`, que se resuelve al instalar y no en el repositorio, así que para el arrastre de citas esas rutas no existen. Se arreglaron a mano.

> **Es un punto ciego del arrastre**, no de esta fase: cualquier renombre futuro va a dejar rotas las referencias de `plantillas/` sin que nada avise.

**Y una traducción de más:** el reemplazo dejó *«la especificación (especificación)»* donde el original decía *«la especificación (spec)»*. Lo encontró releer, no un programa.

---

## 4. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **Defectos abiertos aceptados** | dos: la carpeta `skills/generar-spec-modulo/`, y el punto ciego del marcador |
| **Ciclos** | 1 |
