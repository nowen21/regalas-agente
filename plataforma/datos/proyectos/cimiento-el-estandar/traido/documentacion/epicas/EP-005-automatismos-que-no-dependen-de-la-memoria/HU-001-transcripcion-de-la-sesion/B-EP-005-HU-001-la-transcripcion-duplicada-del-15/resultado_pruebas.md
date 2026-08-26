# Resultado de Pruebas — Fase B-EP-005-HU-001: la transcripción duplicada del 15

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) v1.0 · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| Caso | Veredicto |
|---|---|
| CP-001 · todo lo que se quita tiene gemelo | ✅ **Pasa** — los 9 |
| CP-002 · los que no tienen gemelo siguen ahí | ✅ **Pasa** — los 16 |
| CP-003 · numeración seguida | ✅ **Pasa** — 1 a 48 |
| CP-004 · la nota advierte de las horas | ✅ **Pasa** |

**4 de 4.** `validar.py estandar` sin incumplimientos.

---

## 2. Lo que se midió, y por qué cambió el plan

| | |
|---|---:|
| Bloques de usuario | 57 |
| Con la marca del enganche | 32 |
| Sin marca | 25 |
| **De esos, repetidos palabra por palabra** | **9** |
| **Sin pareja — mensajes reales** | **16** |

**El pendiente 29 decía «quitar los bloques que escribió el agente a mano y dejar los del enganche».** Aplicado literal, eso borraba los 25 — **dieciséis de ellos mensajes que el usuario escribió de verdad.**

> **La instrucción estaba apoyada en que la marca estuviera siempre, y faltaba en la mitad.** Un criterio que suena limpio puede depender de un supuesto que nadie comprobó, y eso solo se ve midiendo antes de borrar.

---

## 3. Lo que queda abierto · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**No se sabe por qué 16 bloques no llevan marca.** O el enganche no los escribió, o los escribió sin ella. Saberlo diría si el enganche tuvo un defecto ese día — y si lo tuvo, puede tenerlo otra vez.

**Las horas del archivo siguen sin poder leerse en orden.** No tiene arreglo: la mitad son estimaciones y no hay de dónde sacar las reales. Queda dicho en la cabecera.

---

## 4. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **Defectos abiertos aceptados** | dos: por qué faltan 16 marcas, y las horas estimadas |
| **Ciclos** | 1 |
