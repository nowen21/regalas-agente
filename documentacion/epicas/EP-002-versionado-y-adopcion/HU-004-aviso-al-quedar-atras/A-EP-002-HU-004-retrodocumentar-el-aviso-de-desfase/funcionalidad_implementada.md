# Funcionalidad implementada — Fase `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` (módulo Versionado)   ·   `[CAPA 3]`

> **Veredicto de la fase: [No cumple](resultado_pruebas.md).** El `CA-01` salió en rojo: el aviso de desfase **no llegaba al abrir sesión**. Se cierra declarándolo, no aprobándolo. **Lo que faltaba se construyó después**, en la fase [`B`](../B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio/funcionalidad_implementada.md).

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | La propia [HU-004](../HU-004-aviso-al-quedar-atras.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-004](../HU-004-aviso-al-quedar-atras.md): `CA-01`, `CA-02` y `CA-03` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | Por anotar al guardar |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-27.** Entre las dos fechas se construyó la fase `B` que resolvió su rojo. **Este cierre no lo da por resuelto**: dice qué encontró esta fase y adónde fue a parar.

---

## 1. Qué se implementó — resumen

**Nada nuevo: esta fase midió.** Y lo que midió fue que **el aviso de desfase no llegaba**.

La comprobación existía como subcomando y había que pedirla a mano — que es justo lo que la historia venía a evitar. Un proyecto atrasado podía trabajar toda la sesión sin enterarse.

**Los otros dos criterios sí cumplieron:** el que está al día no recibe nada, y el aviso no migra ni detiene.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Estado | Evidencia |
|---|---|---|---|
| `CA-01` llega al abrir sesión | automatismo | ❌ **No cumple** | Lectura de los tres módulos del arranque, y corrida de `sesion.revisar()` |
| `CA-02` el que está al día no recibe nada | comprobación | ✅ | Copia temporal declarando la vigente |
| `CA-03` no migra ni detiene | comprobación | ✅ | Severidad, código de salida y archivos sin tocar |

**El `CA-01` se comprobó leyendo los tres módulos del arranque, no suponiendo.** Y ahí estaba el hueco: la pieza existía y nadie la llamaba.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho: se midió lo que había |
| Lo que se encontró | **Un criterio en rojo**, con su deuda crítica escrita |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cinco días sin cerrar**, y su deuda crítica con ella.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **No cumple** — uno de tres criterios en rojo |
| **Defectos** | `D-01` crítica, `D-02` alta, `D-03` cerrada al comprobarla |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**En el momento de esta fase, había que pedirlo a mano.** Desde la fase `B`, llega solo al abrir sesión.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| El criterio se marcó **en rojo**, no «cumple con matices» | La pieza existía. Pero la historia pedía que **llegara**, y no llegaba. Marcarlo verde por existir habría sido aprobar la mitad |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · El aviso no llega al abrir sesión.** Existe como subcomando y hay que pedirlo a mano | Crítica | **Resuelta** en la fase [`B`](../B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio/funcionalidad_implementada.md), el 2026-08-22 |
| **`D-02` · El aviso no dice qué cambió** entre las dos versiones | Alta | **Resuelta** en la misma fase `B` |
| **`D-03` · El plan afirmaba que el enganche de apertura ya lo entregaba** | Baja | **Cerrada al comprobarlo.** El plan estaba equivocado |

**`D-03` es la que más enseña.** El plan daba por hecho algo del producto **sin haberlo verificado**, y resultó falso. Es el mismo error que se repitió varias veces en este repositorio, y la única defensa que funcionó siempre fue la misma: **leer el código en vez de creerle al plan.**

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-004](../HU-004-aviso-al-quedar-atras.md): su §8 nombra esta fase y la `B`.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. Esta fase no cambió nada: midió.
- **Reversión:** no aplica.
