# Funcionalidad implementada · Fase `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` (módulo `proyectos/cimiento/core/validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` |
| **Módulo** | `proyectos/cimiento/core/validadores/`, `adaptadores/claude-code/` |
| **Especificación del módulo** | Los CA de la [HU-027](../HU-027-una-regla-parecida-se-avisa-al-crearla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-027 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.3.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al escribir una regla de `base/`, el enganche de reglas relacionadas entrega también las que se le parecen por significado, sin frenar. `validar.py parecidas` da lo mismo para una regla o para lo que entra en el commit. Sin la búsqueda de `memoria/` instalada, lo dice.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Enganche | `proyectos/cimiento/core/validadores/relacionadas.py`, `adaptadores/claude-code/hook_relacionadas.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/validadores/parecidas.py`, `proyectos/cimiento/core/herramientas/validar.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/validadores/parecidas.py` | ✅ | CP-003 |
| RNF-01 | No funcional | `Diccionario`, en `parecidas.py` | ✅ | CP-001 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `memoria/diccionario.db` se crea al usarlo y git lo ignora; los guiones de medición van en `historico-chat/scripts/2026-10-05/` (`04·S18`).

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Solo: al escribir una regla de `base/`, una vez por archivo y por sesión.
- `python validadores/validar.py parecidas --regla F25` (se puede repetir `--regla`) o `--preparados`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se compara el título con la exigencia, sin ejemplos ni checklist | Con el texto entero casi todos los pares quedaban entre 0,85 y 0,91, y `02·F4` no salía para `02·F25` | En el comentario de `UMBRAL` |
| Umbral 0,85 y tope de cinco | Con 0,83 cada regla tenía ocho parecidas en promedio y la lista se dejaría de leer | En el comentario de `UMBRAL` |
| La tabla de palabras del modelo en una base de datos | Abrir el modelo tardaba de 2 a 6 s; guardar los vectores de las reglas no servía, porque la regla recién escrita siempre hay que traducirla | En la documentación de `parecidas.py` |
| Queda fuera de `validar.py todo` | Sobre todas las reglas lista casi 150 avisos | En `FUERA_DE_LA_CORRIDA` |

## 6. Deuda técnica y pendientes generados

La tabla copia cómo la librería traduce una frase. Si `memoria/` cambia a un modelo con pesos o remapeo, la tabla no lo reproduce y lo dice al armarse; la prueba que compara las dos traducciones avisa si dejan de coincidir.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `validadores/reglas-validables.md`: `20·M12` pasa a tener control.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 54.3.0. La tabla se arma sola la primera vez que se busca.
