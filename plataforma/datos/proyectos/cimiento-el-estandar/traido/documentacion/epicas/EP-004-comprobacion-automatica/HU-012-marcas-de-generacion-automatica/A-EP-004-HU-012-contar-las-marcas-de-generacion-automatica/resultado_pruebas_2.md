# Segundo ciclo — Fase A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica   ·   `[CAPA 3]`

**Para qué sirve este documento.** La fase A cerró el 2026-08-18 con veredicto **Cumple** y su [`resultado_pruebas.md`](resultado_pruebas.md) sigue siendo el de aquel ciclo, intacto. Esto es lo que pasó cuando su §2.7 se desbloqueó el 2026-08-22 y se volvió a mirar: **lo que se contaba entonces no era lo que la regla decía.**

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica` |
| **Ciclo** | Segundo, del 2026-08-22 |
| **Primer ciclo** | 2026-08-18, veredicto Cumple, 16 477 marcas contadas |

---

## 1. Qué se revisó

La duda de su §2.7 quedó resuelta el 2026-08-18 —el recuento no toca el histórico, y ya estaba construido así— y con eso la fase no tenía nada pendiente. Pero al ejecutar el [pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md) el 2026-08-22 apareció otra cosa: **el recuento era más ancho que la regla que servía.**

El anexo dice «la raya larga **como inciso**» y «el punto medio separando frases **en prosa**». El programa las contaba también en títulos, en celdas de tabla, detrás de un identificador en negrita y en los rótulos de campo de los formularios, que no son ninguna de las dos cosas.

---

## 2. Lo que cambió el número

| Dónde | Primer ciclo | Hoy |
|---|---|---|
| El árbol entero, sin el histórico | 16 477 → 15 485 | **6 440** |
| Los moldes del ciclo de vida | 197 | **0** |

**Nueve mil de aquellas 15 485 nunca fueron marcas.** El primer ciclo contó bien lo que el programa contaba; lo que no se había comprobado es que el programa contara lo que la regla pedía.

---

## 3. Los cuatro criterios, revisados

| CA | Estado tras el segundo ciclo |
|---|---|
| CA-01, las marcas de tipografía se cuentan | **Sigue cumpliendo**, y ahora con su pareja: cada forma exenta tiene una prueba de que la misma línea en prosa sí cuenta |
| CA-02, las marcas invisibles se encuentran | Sin cambio |
| CA-03, la notación del estándar no se cuenta como marca | **Es el que se rompía sin que se supiera.** Cumple desde la [fase C](../C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion/funcionalidad_implementada.md) |
| CA-04, los moldes del ciclo no llevan adorno | Nuevo, de las fases B y C. Cumple, con los moldes en 0 |

---

## 4. Lo que esto deja dicho

**Un recuento que se da por bueno porque corre no está comprobado.** El primer ciclo verificó que el programa contara y que el número saliera; nadie verificó que lo contado fuera lo que el anexo llama marca. Es la segunda vez que ocurre en esta misma HU: el 2026-08-18 pasó con el punto medio de los encabezados, y el propio anexo lo dejó escrito.

**Dos veces es un patrón.** Vale la pena mirar si hay una tercera antes de dar por buena cualquier otra cifra que este repositorio publique sobre sí mismo.

---

## 5. Veredicto

**Concepto:** Cumple.

**Justificación:** los cuatro criterios quedan verdes tras las fases B y C del 2026-08-22. El veredicto del primer ciclo no se toca: era correcto sobre lo que entonces se sabía.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El recuento de hoy | `python validadores/marcas.py` |
| EV-02 | Las parejas de prueba | `test_las_marcas_de_ia_se_cuentan.py`, clase `LaNotacionNoEsAdorno` |
| EV-03 | La decisión escrita | [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md), sección del 2026-08-22 |
