# Funcionalidad implementada — Fase `A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

> **Veredicto de la fase: [No cumple](resultado_pruebas.md).** Cinco de seis criterios en verde; el `CA-04` en rojo, y **sigue en rojo hoy**: `validar.py vigencia` reporta que **250 de 250 reglas no dicen cuándo se revisó si todavía sirven**. Se cierra declarándolo, no aprobándolo.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | La propia [HU-007](../HU-007-regla-de-las-reglas.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-007](../HU-007-regla-de-las-reglas.md): `CA-01` a `CA-06`. Los seis |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | Por anotar al guardar |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-27.** Entre las dos fechas no se tocó nada de esta fase. **Su rojo se volvió a medir al cerrar**, y no solo sigue: pasó de 249 a 250.

---

## 1. Qué se implementó — resumen

**Nada nuevo: esta fase midió el procedimiento con que se escribe una regla.** Cinco de sus seis exigencias se cumplen, y una no.

**Lo que funciona:** una regla se enruta a su capítulo, una atada a un stack no entra, la que exige dos cosas se parte, no se automatiza hasta saber que sirve, y lo pedido dos veces no se pierde.

**Lo que no:** no se sabe qué reglas llevan más tiempo sin revisar. **El programa existe** —`validar.py vigencia` sabe ordenar por antigüedad— **y el dato que necesita, no**: ninguna regla dice cuándo se revisó si todavía hace falta.

**El sello responde por la forma, no por la vigencia.** Una regla puede tener su checklist impecable y estar resolviendo un problema que ya no existe.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Estado | Evidencia |
|---|---|---|---|
| `CA-01` se enruta al capítulo correcto | norma | ✅ | `M13`, `M2`, la fila 1 del checklist, y una decisión real de ese día |
| `CA-02` una regla atada a un stack no entra | comprobación | ✅ | `M3`, con comprobación automática y corrida limpia |
| `CA-03` la que exige dos cosas se parte | norma | ✅ | `M5`, y **las cinco `F4.n` como huella** de haberlo hecho |
| `CA-04` se sabe cuáles llevan más sin revisar | comprobación | ❌ **No cumple** | `validar.py vigencia`: **249 de 249 sin dato** |
| `CA-05` no se automatiza hasta saber que sirve | norma | ✅ | `M9`, las 175 clasificadas, y **dos comprobaciones corregidas ese día antes de dejarlas** |
| `CA-06` lo pedido dos veces no se pierde | norma | ✅ | `01·C10` y su molde |

**El `CA-03` se comprueba con una huella, no con una lectura:** las cinco reglas `F4.n` existen porque una regla que exigía cinco cosas se partió en cinco. El rastro está en los identificadores.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho: se midieron los seis criterios |
| Lo que se encontró | Cinco verdes y **uno en rojo por falta de dato**, no de programa |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cinco días sin cerrar.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **No cumple** — uno de seis criterios en rojo |
| **Defectos** | `D-01` alta, `D-02` baja |

**El rojo se volvió a medir al cerrar, el 2026-08-27:**

```
[AVISO] base — 250 de 250 reglas no dicen cuándo se revisó si siguen sirviendo
```

**Eran 249 hace cinco días.** No solo sigue abierto: **crece con cada regla nueva**, porque nada obliga a poner el dato al escribirla.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py vigencia
```

Ordena las reglas por cuánto llevan sin revisarse. **Hoy no puede ordenar nada**, porque ninguna trae el dato.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| El `CA-04` se marcó **en rojo aunque el programa existe** | La historia pedía **saber cuáles llevan más sin revisar**, no que hubiera un programa capaz de decirlo si tuviera datos |
| El `CA-03` se comprueba por **huella**, no por lectura | Las cinco `F4.n` son el rastro de haber partido una regla. Eso es evidencia; leer `M5` y asentir, no |
| El `CA-05` trae **dos comprobaciones corregidas antes de dejarlas** | Es la evidencia de que la regla se aplicó de verdad, no de que se leyó |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · El sello de una regla responde por su forma, no por si sigue haciendo falta.** El programa sabe ordenar por antigüedad; las reglas no traen el dato | Alta | **Abierta, y creciendo.** De 249 a 250 en cinco días |
| **`D-02` · El conteo de `reglas-validables.md` va con `~` y nadie comprueba que cuadre** | Baja | **Abierta.** Ya anotada también en la fase de `EP-004 · HU-001` |

**`D-01` es la deuda más vieja que sigue viva en este repositorio, y la que más se parece a lo que se arregló el 2026-08-26.** Un dato que hace falta, un programa que lo usaría, y nada que obligue a ponerlo — así fue como el inventario de historias llegó a 34 de retraso.

**La diferencia es que aquella se arreglaba quitando la copia**, y esta se arregla poniendo el dato. **Y el número crece solo**: cada regla nueva nace sin él.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-007](../HU-007-regla-de-las-reglas.md): su §8 nombra esta fase.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. Esta fase no cambió nada: midió.
- **Reversión:** no aplica.
