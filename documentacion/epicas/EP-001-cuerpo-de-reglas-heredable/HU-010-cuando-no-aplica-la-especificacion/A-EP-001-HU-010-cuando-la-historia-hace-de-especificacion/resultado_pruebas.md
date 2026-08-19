# Resultado de Pruebas — Fase A-EP-001-HU-010: cuando la historia hace de especificación

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| Qué se comprobó | Veredicto |
|---|---|
| `02·F2` dice de qué está hecha la especificación cuando el entregable no es código | ✅ **Pasa** |
| La regla sigue exigiendo lo mismo en todos los casos | ✅ **Pasa** — no se abrió otra excepción |
| Entra en el molde de cuatro líneas | ✅ **Pasa** — 294 caracteres |
| Su checklist se reaplicó | ✅ **Pasa** — 18 ✅ · 0 ❌ · 2 N/A |
| No regresión | ✅ **Pasa** — `tests/` 208 · `pruebas.py` 357 · `estandar` limpio |

---

## 2. Qué se decidió, y por qué no fue una excepción

El [pendiente 20](../../../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md) dejaba dos caminos:

1. Escribirle **otra excepción** a `F2`.
2. Aceptar que **la historia hace de especificación** cuando el entregable no es código.

**Se eligió el 2**, y la diferencia entre los dos no es de forma:

> **Una excepción dice cuándo la regla no rige. Esto dice dónde vive lo que la regla exige.** Con el camino 2, `F2` sigue exigiendo una especificación acordada en todos los casos — lo único que cambia es de qué está hecha.

**Y `F2` ya tenía una excepción.** Abrirle la segunda a una regla que ya trae una es la puerta que después nadie cierra: [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba) es el ejemplo vivo de ese camino — su excepción deja al agente autorizándose a sí mismo a no probar.

---

## 3. Lo que decía y lo que dice

| | |
|---|---|
| **Antes** | *«Ningún desarrollo… sin una especificación acordada… Sin especificación, el código es opinión del agente.»* |
| **Ahora** | Lo mismo, más: *«Si el entregable no es código, la especificación es la historia con sus criterios de aceptación.»* |

**Se acortó la primera frase para que quepa**, y se fue *«sin especificación, el código es opinión del agente»* — que es el porqué, y su sitio es `notas/`.

---

## 4. Lo que esto ordena

Dos fases de este repositorio se habían abierto declarando que no tienen especificación aparte —`A-EP-001-HU-001` y `A-EP-004-HU-010`—, y hasta hoy eso era un incumplimiento silencioso de `F2`. **Ahora es lo que la regla dice.**

---

## 5. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 1 |
