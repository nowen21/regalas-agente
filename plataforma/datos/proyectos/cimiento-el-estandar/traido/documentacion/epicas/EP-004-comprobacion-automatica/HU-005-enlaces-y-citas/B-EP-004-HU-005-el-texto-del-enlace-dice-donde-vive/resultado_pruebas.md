# Resultado de Pruebas — Fase B-EP-004-HU-005: el texto del enlace dice dónde vive

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-B-EP-004-HU-005](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

**11 de 11 ejecutados. 11 pasan.** 14 casos automatizados en [validadores/tests/test_el_texto_del_enlace_dice_donde_vive.py](../../../../../validadores/tests/test_el_texto_del_enlace_dice_donde_vive.py).

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **168 · OK** — eran 154 |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados) |
| `validar.py estandar` | **Sin incumplimientos** — ningún enlace roto |
| Enlaces entre carpetas mal escritos | **284 → 0** |
| Archivos de `prompts/` tocados | **0** |

---

## 2. Lo que se arregló

| Dónde | Enlaces |
|---|---:|
| `historico-chat/` (resúmenes) | 145 |
| `documentacion/` | 127 |
| `pendientes/` | 9 |
| `plantillas/` | 2 |
| `base/` | 1 |
| **Total, en 89 archivos** | **284** |

---

## 3. Lo que los casos encontraron **antes** de tocar el repositorio

Los casos se escribieron antes de aplicar nada, y encontraron dos defectos reales:

**1 · La exclusión de `prompts/` se contaba contra la raíz equivocada.** Usaba `relativo()`, que resuelve contra la raíz del repositorio y no contra la que se recibe. Sobre un árbol de prueba **no reconocía nada y escribía justo donde no debía**. Es la clase de error que en producción no se ve: en el repositorio real la raíz coincide, así que habría funcionado hasta el día que no.

**2 · El texto entre comillas invertidas nunca se veía.** `comun.enlaces()` borra esos trozos antes de buscar enlaces —para no leer los ejemplos de cómo se escribe uno— y con eso el texto queda vacío y deja de parecer una ruta. **No es un defecto de esta fase**: quitarlo cambiaría cómo se leen los enlaces en todo el repositorio. Quedó declarado en [CP-010](plan_pruebas.md#cp-010--el-texto-entre-comillas-invertidas-no-se-ve).

---

## 4. Lo que se aplicó, se revirtió, y por qué  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**La primera corrida aplicó los 1031 y se revirtió entera.**

`13·DOC14` pide la ruta desde la raíz *«para saber dónde vive sin abrirlo»*. Para el archivo de **la misma carpeta** ese propósito ya está cumplido —quien lee está parado ahí— y la regla no distingue el caso. Aplicada literal, la tabla de contenidos de una fase quedaba así:

```
| [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/E-EP-001-HU-009-las-que-solo-sobraban-de-largo/plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer |
```

**132 caracteres de media para nombrar al vecino**, y son **747 de los 1031**.

**Se revirtieron los 347 archivos** y se aplicó solo a los 284 de entre carpetas, que son los que la regla resuelve de verdad. **Si `DOC14` exceptúa al vecino es un cambio de la regla, y eso lo decide el usuario.**

> **La lección no es que la regla esté mal.** Es que una regla puede tener razón en el caso para el que se escribió y volverse contraproducente en el que no se miró — y que **eso solo se ve aplicándola**, no leyéndola. El validador llevaba días contando 1031 sin que nadie viera que tres de cada cuatro eran de otro tipo.

---

## 5. Lo que queda abierto

- **La decisión sobre el vecino de la misma carpeta.** 747 enlaces esperan.
- **El punto ciego de las comillas invertidas**, declarado en un caso.
- **El punto 3 del pendiente 18** — si el validador entra en la corrida de todos los días. Con 284 en cero y 747 esperando decisión, hoy todavía sepultaría lo demás.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `RN-03` en su parte reparable |
| **Defectos abiertos aceptados** | dos: el vecino, y el punto ciego de las comillas |
| **Ciclos** | 1 |
