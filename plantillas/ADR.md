# ADR-000 — «Título de la decisión»   ·   `[CAPA 3]`

> **Architecture Decision Record**: registra una decisión de arquitectura **no obvia** y su porqué ([`13·DOC2`](../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md)), para que no se pierda ni se re-discuta. La produce la estación de diseño (`disenar-arquitectura`) y la referencia la épica (`epica.md §10.2`). Se guarda en `documentacion/adr/ADR-<NNN>-<slug>.md`. Reemplaza los `«…»` y borra esta caja.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | ADR-000 |
| **Título** | «…» |
| **Estado** | Propuesta / **Aceptada** / Reemplazada / Deprecada |
| **Fecha** | AAAA-MM-DD |
| **Decisores** | «quién decide» |
| **Épica / Módulo** | «a qué pertenece» |
| **Reemplaza a** | «ADR-XXX» (si aplica) |
| **Reemplazada por** | «ADR-XXX» (si esta quedó obsoleta) |

---

## 2. Contexto y problema

«La situación que obliga a decidir: qué restricción, requisito o fuerza técnica está en juego. En lenguaje neutro, sin adelantar la solución.»

---

## 3. Opciones consideradas

| Opción | A favor | En contra |
|---|---|---|
| **A — «…»** | «…» | «…» |
| **B — «…»** | «…» | «…» |
| **C — «…»** | «…» | «…» |

---

## 4. Decisión

**Se elige: «Opción X».**

«Por qué esta y no las otras — el criterio que inclinó la balanza (costo, riesgo, simplicidad, reversibilidad, encaje con el resto del sistema).»

---

## 5. Consecuencias

- **Positivas:** «qué mejora o habilita».
- **Negativas / costo:** «qué se sacrifica o se vuelve más difícil».
- **Riesgos y mitigación:** «qué puede salir mal y cómo se acota».
- **Reversibilidad:** «qué tan caro es dar marcha atrás si fue un error».

---

## 6. Enlaces

- **Señal asociada** ([`13·DOC5`](../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)): «id/enlace en la memoria — tipo `decisión`».
- **Afecta a:** «módulos, especificaciones o ADR relacionados».
