# Resultado de Pruebas — Fase A-EP-001-HU-010: cuando la historia hace de especificación

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| Qué se comprobó | Veredicto |
|---|---|
| ¿Hace falta una regla nueva? | ❌ **No** — [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) ya lo dice desde la v3.1.0 |
| Lo que se escribió primero, ¿chocaba? | **Sí** — con [`02·F0`](../../../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), que prohíbe fusionar eslabones |
| `02·F2` vuelta a su texto y su sello | ✅ **Pasa** |
| No regresión | ✅ **Pasa** — `tests/` 222 · `pruebas.py` 357 · `estandar` limpio |

---

## 2. La respuesta estaba dos reglas más abajo

> **`02·F19` · La redacción del CA es la especificación funcional**

El pendiente 20 preguntaba si hay que escribir una especificación aparte cuando el entregable no es código. **El capítulo `02` ya lo contestaba**, y desde la v3.1.0.

---

## 3. Cómo se descubrió, que es lo que vale

**Primero se hizo mal.** Se le agregó a `F2` una frase que decía lo mismo con otras palabras, y esa frase **fusionaba la historia con la especificación** — justo lo que `F0` prohíbe con esa palabra.

**Lo vio el usuario preguntando**, no el agente comprobando. La fila 2 del checklist —`20·M12`, *«se leyó entero el capítulo dueño»*— se selló en verde sin leerlo. Al leerlo, `F19` apareció en la misma pasada.

**De ahí salió [`A-EP-005-HU-010`](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo/)**: al tocar una regla ahora llegan las que se relacionan con ella, y `F0` sale tercera al tocar `F2`.

---

## 4. Lo que ordena

Las dos fases que se abrieron declarando que no tienen especificación aparte **no estaban incumpliendo nada**. `F19` ya las cubría; lo que faltaba era que alguien lo mirara.

---

## 5. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** — sin escribir ninguna regla |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 2 — el primero se revirtió entero |
