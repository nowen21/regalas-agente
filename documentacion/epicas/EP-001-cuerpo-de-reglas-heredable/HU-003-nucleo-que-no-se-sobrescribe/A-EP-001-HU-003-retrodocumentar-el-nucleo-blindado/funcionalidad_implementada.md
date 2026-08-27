# Funcionalidad implementada — Fase `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

> **Veredicto de la fase: [No cumple](resultado_pruebas.md).** El `CA-02` salió en rojo: **una clave pegada sin comillas quedaba escrita en claro**. Se cierra declarándolo, no aprobándolo. **Lo que faltaba se construyó después**, en la fase [`B-EP-005-HU-002`](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa/funcionalidad_implementada.md).

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | La propia [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md): `CA-01`, `CA-02` y `CA-03` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | Por anotar al guardar |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-27.** Entre las dos fechas se construyó la fase que resolvió su rojo. **Este cierre no lo da por resuelto**: dice qué encontró esta fase y adónde fue a parar.

---

## 1. Qué se implementó — resumen

**Nada nuevo: esta fase midió el núcleo blindado contra la realidad.** Y de sus tres exigencias, una no se cumplía.

**Una clave pegada sin comillas quedaba escrita en claro.** Se probaron seis formas: **tres se enmascaraban y tres no**. Las que no, son justamente como se pega una clave de verdad en un chat: `API_KEY=valor`, sin comillas.

**Las otras dos sí cumplieron**, y con evidencia de conducta real del mismo día: el agente se detuvo ante lo irreversible en dos casos, y reportó tres tropiezos propios en vez de disimularlos.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Estado | Evidencia |
|---|---|---|---|
| `CA-01` se detiene ante lo irreversible | norma | ✅ | `00·N1`, la escala del anexo, y **dos casos reales de ese día** |
| `CA-02` la clave no queda en claro | automatismo | ❌ **No cumple** | **Seis formas probadas: tres se enmascaran, tres no** |
| `CA-03` el error no se disimula | norma | ✅ | `01·C9`, y **tres tropiezos reportados ese día** |

**Los criterios verdes se comprobaron con conducta, no con lectura.** Que el `CA-03` traiga tres tropiezos propios como evidencia es lo que hace creíble el resto: un resultado donde todo sale bien no dice nada.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho: se midió el núcleo contra la realidad |
| Lo que se encontró | **Un criterio en rojo**, con su deuda crítica |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cinco días sin cerrar**, y con ella una deuda crítica sobre claves en claro.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **No cumple** — uno de tres criterios en rojo |
| **Defectos** | `D-01` crítica, `D-02` media |

**Probar seis formas y no una es lo que convirtió esto en un hallazgo.** Con una sola —de las tres que sí se enmascaraban— el criterio habría salido verde y la clave habría seguido quedando en claro.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No hay punto de entrada: el entregable es el **núcleo blindado**, que se carga solo al abrir sesión y no se contradice nunca.

El enmascarador que le da cuerpo al `CA-02` corre solo, en el enganche del histórico.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se probaron **seis formas** de escribir una clave, no una | Una sola forma habría dado verde. El rojo salió de la variedad |
| El `CA-03` se comprueba con **tropiezos propios del día** | Es la única evidencia honesta de que el error no se disimula: mostrarlo |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · El enmascarador no reconoce una clave pegada sin comillas**, que es como se pega en un chat | Crítica | **Resuelta** en [`B-EP-005-HU-002`](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa/funcionalidad_implementada.md), el 2026-08-22 |
| **`D-02` · El patrón se tomó prestado de la búsqueda de secretos en código**, sin revisar si servía para el texto de una conversación | Media | **Resuelta en la misma fase**, que probó nueve formas y cinco de lo que **no** debe tapar |

**`D-02` explica `D-01`, y es la lección que queda.** El patrón funcionaba para código porque en código las claves van entrecomilladas. **En una conversación se pegan crudas.** Reusar la herramienta sin revisar si el terreno era el mismo es lo que dejó el agujero.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md): su §8 nombra esta fase.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. Esta fase no cambió nada: midió.
- **Reversión:** no aplica.
