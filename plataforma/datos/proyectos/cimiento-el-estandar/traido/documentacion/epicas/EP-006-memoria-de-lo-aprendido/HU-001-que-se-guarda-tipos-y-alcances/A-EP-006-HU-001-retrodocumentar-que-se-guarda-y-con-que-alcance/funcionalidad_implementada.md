# Funcionalidad implementada — Fase A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance (módulo Memoria)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |
| **Módulo** | Memoria — [`memoria/memoria.py`](../../../../../memoria/memoria.py) · [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) |
| **Especificación del módulo** | No la hay aparte: la especificación son los CA de [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md) y [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md). Es uno de los casos que viene a resolver [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-001: [CA-01](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-01--el-criterio-de-qué-se-guarda-está-escrito), [CA-02](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-02--cada-cosa-guardada-tiene-tipo-y-alcance), sus dos RNF y —lo que la fase descubre— sus dos criterios transversales, que **no** quedaron cubiertos |
| **Fecha de cierre** | 2026-08-17 |
| **Commit** | Pendiente de autorización del usuario |

---

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los dos CA numerados quedaron verificados; los dos **transversales** de la HU, no — uno está en «No» y el otro sin probar, y ninguno cabía en el plan aprobado. Este documento cierra lo que la fase hizo; lo que falta pide una fase `B-EP-006-HU-001`.

---

## 1. Qué se implementó — resumen

**Casi nada de programa: la fase escribió la prueba y el número que faltaban.** Los diez tipos y los tres alcances están en producción desde que existe [`memoria/esquema.sql`](../../../../../memoria/esquema.sql), y el criterio de qué merece guardarse está escrito en `13·DOC5`. Lo que no existía era una sola prueba de que el tipo sea obligatorio, ni la cuenta de cuáles de los diez tipos se usan de verdad.

Ahora los dos existen. Y la cuenta trajo lo que la HU misma había puesto como riesgo: **tres de los diez tipos no se han usado nunca**, y el `modulo:` de los tres alcances tampoco.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · se guarda lo que no se recupera del código | documentación | [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) | ✅ Ya existía | CP-001 |
| RN-02 · cada señal tiene tipo | programa | [`memoria/memoria.py`](../../../../../memoria/memoria.py) · `TIPOS` y `cmd_add` | ✅ Ya existía | CP-002 |
| RN-03 · cada señal tiene alcance | datos | [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) · `scope … DEFAULT 'proyecto'` | ✅ Ya existía | CP-002 |
| RN-04 · se decide al guardar, no automáticamente | programa | `memoria.py add` es una orden explícita | ✅ Ya existía | — |
| RN-05 · dice también por qué | datos | Columna `why` del esquema | ✅ Ya existía | — |
| Las dos exigencias, con red | pruebas | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `TiposYAlcances` | ✅ Escritas acá | 5 casos en verde |
| Que la prueba no toque la base real | pruebas | `_huella()` en el mismo archivo | ✅ Escrito acá | CP-002, paso 5 |
| El uso real de los diez tipos | medición | §2 del [resultado_pruebas.md](resultado_pruebas.md) | ✅ Medido acá | CP-003 |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | El criterio clasificó cinco decisiones reales difíciles sin quedarse sin veredicto | ✅ con salvedad `D-02` |
| CA-02 | Tipo obligatorio y contra lista; alcance con valor por omisión; ninguna señal sin los dos | ✅ |
| Transversal · Límites | Ningún caso lo probó: el plan no lo escribió | ❌ **No probado** |
| Transversal · Privacidad | `13·DOC5` no dice que no se guardan datos personales ni claves | ❌ **No cumple** |

---

## 3. Qué se probó

Cinco casos automatizados y cuatro verificaciones a mano. Los dos que importan:

- **La huella de la base real.** Cada prueba de la clase nueva compara el SHA-256 de `memoria/senales.db` antes y después. Sin eso, una prueba que tocara el aprendizaje del proyecto pasaría en verde igual.
- **Los diez tipos se guardan de verdad, uno por uno.** Sin ese caso, los tres que rechazan (`sin tipo`, `tipo inventado`, y el de la lista) los pasaría también un esquema que rechaza todo.

Detalle en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 4. Lo que la fase midió, que es lo que venía a buscar

| Medición, el 2026-08-17 | Número |
|---|---|
| Señales guardadas en total | 237 |
| Tipos declarados por el esquema | 10 |
| Tipos con al menos una señal | **7** |
| Tipos nunca usados | **3** — `alternativa-descartada`, `supuesto`, `pregunta-abierta` |
| Formas de alcance declaradas | 3 |
| Formas de alcance nunca usadas | **1** — `modulo:<slug>` |
| Señales de alcance `proyecto:estandar-agente` | **1** de 237 |

**La última fila es el hallazgo de la fase.** El repositorio que define el criterio es el que menos lo aplica: una sola señal, del 2026-07-25, anterior a que se abriera ninguna de sus épicas. Cuatro de las cinco decisiones que se clasificaron en CP-001 eran señal y ninguna llegó a guardarse.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| Los tres tipos sin uso **no se quitan** del esquema: quitar uno rompe las señales que lo tienen, y ninguna se borra | §2.6 del [plan_trabajo.md](plan_trabajo.md) y §2 del [resultado](resultado_pruebas.md) |
| Las cuatro decisiones de CP-001 que son señal **no se guardan retroactivamente**: `RN-04` dice que lo que se guarda se decide al guardarlo | `D-01` del [resultado](resultado_pruebas.md) |
| La lista cerrada de tipos vive en el programa, no en el esquema, y eso se dice en vez de taparse | Documentación de la clase `TiposYAlcances` y `D-03` |
| El plan de pruebas aprobado **no se reescribe** para agregarle los transversales que le faltaban | `D-04` del [resultado](resultado_pruebas.md) |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Dónde se guarda lo aprendido | [HU-002](../../HU-002-guardar-en-el-repositorio/HU-002-guardar-en-el-repositorio.md) |
| Buscar por palabra y por significado | [HU-003](../../HU-003-busqueda-por-palabra/HU-003-busqueda-por-palabra.md) y [HU-004](../../HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md) |
| Separar el aprendizaje del proyecto de la preferencia del usuario | [HU-005](../../HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md) |
| Marcar lo que dejó de aplicar | [HU-007](../../HU-007-marcar-lo-que-dejo-de-aplicar/HU-007-marcar-lo-que-dejo-de-aplicar.md) |
| Que `13·DOC5` diga que no se guardan datos personales ni claves — **transversal de privacidad, en «No»** | Fase `B-EP-006-HU-001`, propuesta. Toca `base/`, así que abrirla la decide el usuario |
| El caso del **transversal de límites**: qué se hace cuando algo parece de dos tipos a la vez | La misma fase `B-EP-006-HU-001` |
| Que el criterio cubra lo escrito en un documento, no solo en el código | **Sin destino todavía** — `D-02` |

**La advertencia que deja esta fase:** un criterio escrito, probado y que decide bien no sirve de nada si nadie lo aplica. Este repositorio lleva 23 versiones y una señal.
