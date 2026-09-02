# Funcionalidad implementada — Fase `B-EP-006-HU-004-degradar-sin-el-modelo` (módulo Memoria)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-004-degradar-sin-el-modelo` |
| **Módulo** | Memoria |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-004](../HU-004-busqueda-por-significado.md): el CA-02, sin el modelo la búsqueda sigue funcionando |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |

> **Por qué se declara el reemplazo:** el defecto que dejó aquella fase en rojo está arreglado y su prueba corre. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**El más grave de los tres, porque rompía lo que no dependía de él.**

Saber si las librerías opcionales están puestas no es lo mismo que poder cargar el modelo: puede faltar el archivo, o no haber red la primera vez. Con las librerías instaladas y el modelo ausente, la búsqueda **se caía entera y se llevaba por delante la búsqueda por palabra**, que no necesita ni modelo ni red.

Esa es la promesa que la historia hace: que instalar lo semántico sea opcional **de verdad**. Una parte opcional que al fallar tumba la que no lo es, no es opcional.

| Antes | Ahora |
|---|---|
| Con el modelo ausente, la búsqueda entera se cae | Degrada a búsqueda por palabra |
| El error no se explicaba | El modo lo dice: «léxica (el modelo no se pudo cargar)» |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado |
|---|---|---|---|
| CA-02, sin el modelo la búsqueda sigue funcionando | servicio | `memoria/` | ✅ |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
| T-01 · atrapar el fallo al cargar o al indexar | CP-002 |
| T-02 · seguir con lo léxico | CP-002 |
| T-03 · decirlo en el modo, sin callarlo | CP-002 |
| T-04 · destapar la prueba | 59 en verde |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | Las 59 pruebas de la memoria, 59 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin punto de entrada nuevo.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se atrapa cualquier error, no una clase concreta | Quien falla es una librería de terceros bajando un modelo; el día que le cambien el nombre a su excepción, la memoria no puede dejar de servir |
| El fallo se dice en el modo, no se calla | Degradar en silencio deja al que busca creyendo que buscó de las dos formas |
| No se comprueba el modelo al arrancar | Cargarlo para saber si carga cuesta lo mismo que usarlo, y la mayoría de las búsquedas no lo necesitan |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Ninguna | — |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
