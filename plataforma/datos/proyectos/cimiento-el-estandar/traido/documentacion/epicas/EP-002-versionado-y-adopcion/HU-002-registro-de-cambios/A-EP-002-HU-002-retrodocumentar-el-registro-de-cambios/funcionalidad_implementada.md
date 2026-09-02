# Funcionalidad implementada — Fase `A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios` (módulo Versionado)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios` |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | La propia [HU-002](../HU-002-registro-de-cambios.md). El entregable es texto normativo y su comprobación |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-002](../HU-002-registro-de-cambios.md): `CA-01`, `CA-02` y `CA-03`. Los tres |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `b19ca91` |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-26.** Entre las dos fechas no se tocó nada de esta fase: faltaba este documento.

---

## 1. Qué se implementó — resumen

**El registro de cambios tiene quien lo vigile, y se comprobó que ya lo tenía.** Cada versión publicada tiene su entrada, un cambio sin entrada no pasa el enganche, y las entradas se entienden sin haber seguido el cambio.

**Lo que esta fase agregó de código es una prueba**: que la versión declarada en `VERSION` tenga entrada en el registro, y que ninguna entrada del registro sea de una versión que no existe.

**Lo demás ya funcionaba**, y lo que faltaba era la cadena que lo respalda.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` cada versión tiene su entrada | comprobación | `validar.py versionado` | ✅ | Corrido: **0 fallas** |
| `CA-02` un cambio sin entrada no pasa | automatismo | El enganche de pre-commit | ✅ | Sus 7 pruebas, más **cinco versiones subidas ese mismo día** |
| `CA-03` se entiende sin haber seguido el cambio | norma | `20·M17`, corriendo sobre el registro real | ✅ | Una entrada de ese día **reprobada y corregida** |

**La evidencia del `CA-02` no es una prueba sintética:** son cinco versiones subidas de verdad ese día, cada una pasando por el enganche.

**Y la del `CA-03` incluye un fallo propio.** `20·M17` corrió sobre el registro real y reprobó una entrada escrita ese mismo día. Se corrigió, y quedó anotado. **Un criterio que solo trae ejemplos que salieron bien no dice nada.**

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado |
|---|---|
| Las 7 tareas del plan | ✅ hechas |

**Correspondencia con el plan:** 7 tareas, 7 con resultado.

**Lo que no se hizo:** cerrar la trazabilidad, que es este documento. **La fase quedó cuatro días en la estación 11**, y por eso el inventario la contaba entre las incompletas.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, los tres criterios |
| **Defectos abiertos que se aceptaron** | Ninguno. `D-01` se corrigió el mismo día |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py versionado
```

Comprueba que la versión de [VERSION](../../../../../VERSION) tenga su entrada en el [CHANGELOG](../../../../../CHANGELOG.md), y que ninguna entrada sea de una versión que no existe.

**Y corre solo** en el enganche de pre-commit: un cambio de `base/` o `plantillas/` sin entrada no pasa.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué | Dónde quedó |
|---|---|---|
| La prueba se escribe en `pruebas.py`, **no dentro de `metareglas.py`** | Ese archivo no se puede correr, y **una comprobación que no corre no comprueba nada** | §2.6 del plan |
| Las entradas incompletas **se listan, no se completan** | El registro es **rastro**: reescribirlo borra lo que pasó. Se dice cuáles están incompletas y se dejan | §2.6 del plan |
| El caso del `CA-02` se escribe **esperando que nada frene el cambio** | Escrito al revés, el rojo se leería como defecto de esta fase en vez de como la conducta correcta | §2.6 del plan |

**La segunda es la que más cuesta aceptar** y la más importante: un registro histórico que se corrige deja de ser registro.

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| `D-01` · La entrada de la `32.0.1`, escrita ese día, abría con una ruta y con el nombre de un archivo del proyecto — que es justo lo que `20·M17` prohíbe | Baja | **Corregida el mismo día** |
| Las entradas incompletas que el resultado listó | — | **Se dejan a propósito.** No es deuda por hacer: es la decisión de no reescribir el rastro |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-002](../HU-002-registro-de-cambios.md): su §7 nombra esta fase.
- [x] `validadores/pruebas.py`: la prueba de la versión contra su entrada.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** nada nuevo que hacer. La comprobación ya corría; lo que se agrega es una prueba que la vigila.
- **Reversión:** se descarta el commit. No hay estado que reconstruir.
