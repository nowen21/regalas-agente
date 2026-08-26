# Funcionalidad implementada — Fase A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar (módulo Memoria)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Nada se borra y lo marcado no se confunde con lo vigente. Pero de una señal marcada **no se sabe cuándo se marcó ni qué la reemplazó**, y eso es la otra mitad del CA-01. Lo que falta pide una fase `B-EP-006-HU-007`.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` |
| **Módulo** | Memoria — [`memoria/memoria.py`](../../../../../memoria/memoria.py) · [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) |
| **Especificación del módulo** | No la hay aparte: la especificación son los CA de [HU-007](../HU-007-marcar-lo-que-dejo-de-aplicar.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-007: [CA-01](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-01--lo-que-dejó-de-aplicar-queda-marcado-y-visible), [CA-02](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-02--lo-marcado-no-se-confunde-con-lo-vigente), su RNF y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 |
| **Commit** | Pendiente de autorización del usuario |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió las trece pruebas que faltaban y encontró dos defectos.** Los cinco estados y sus tres comandos —`archivar`, `supersede`, `cerrar`— están en producción desde el pendiente 02 y el 03. Lo que no había era una prueba que comprobara la regla del esquema: **ninguna señal se borra**.

Ahora se comprueba señal por señal, contando el total antes y después de cada recorrido.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Los cinco estados, y que solo `activa` se busque | datos + programa | [`esquema.sql`](../../../../../memoria/esquema.sql) · filtro de `cmd_search` | ✅ Ya existía | CP-003 |
| Archivar sin borrar | programa | `cmd_archivar` | ✅ Ya existía | CP-002 |
| Reemplazar sin borrar | programa | `cmd_supersede` | ✅ Ya existía | CP-001, pasos 1–4 |
| **Que la marcada diga qué la reemplazó y cuándo** | programa | `cmd_supersede` no guarda el `--by` ni fecha | ❌ **No existe** | CP-001, paso 6 |
| **Que archivar deje fecha** | programa | `cmd_archivar` no toca `cerrada_en` | ❌ **Falta** | CP-002, paso 4 |
| Cerrar con fecha y referencia | programa | `cmd_cerrar` | ✅ Ya existía | CP-003 |
| Distinguir lo viejo sin revisar de lo fresco | programa | `marca_vigencia` · `meses_desde` | ✅ Ya existía | CP-004 |
| Las siete exigencias, con red | pruebas | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `MarcarLoQueDejoDeAplicar` | ✅ Escritas acá | 13 pruebas |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | Queda marcado y sigue existiendo; **sin fecha y sin decir qué lo reemplazó** | ❌ |
| CA-02 | Los cuatro estados no vigentes fuera de la búsqueda; la vigencia distingue viejo de fresco | ✅ |
| RNF · nada se borra | El total no bajó en ningún recorrido | ✅ |
| Transversal · No regresión | Siete campos idénticos antes y después de marcar | ✅ |
| Transversal · Trazabilidad | Al cerrar sí; al archivar y al reemplazar, no | ❌ |

---

## 3. Qué se probó

Trece casos automatizados y cuatro verificaciones a mano. Los tres que importan:

- **El total, antes y después.** Es lo único que comprueba de verdad la regla «ninguna se borra»; mirar solo el estado la daría por buena aunque la fila desapareciera.
- **El contenido, campo por campo.** Marcar no puede alterar lo marcado, y sin comparar los siete campos eso se supone en vez de comprobarse.
- **El huso horario.** `meses_desde` compara fechas ISO, no instantes: se probó el borde de los 181 días y una entrada que no es fecha.

Detalle en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 4. Los dos defectos, y por qué no se arreglaron acá

| Defecto | Qué le falta | Por qué no se tocó |
|---|---|---|
| `D-01` · el reemplazo no deja rastro | Que `cmd_supersede` escriba el `--by` y la fecha en el `UPDATE` | §2.1 del [plan aprobado](plan_trabajo.md) declara solo `memoria/pruebas.py`. [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) no deja salirse, y ampliar el plan es del usuario |
| `D-02` · archivar no deja fecha | Escribir `cerrada_en` al archivar, o una columna propia | Lo mismo |

**Los dos quedaron probados con `expectedFailure`**, no anotados: la suite sigue verde, el defecto queda con evidencia, y el día que se arreglen las pruebas pasan a «éxito inesperado» y obligan a volver acá.

**Lo que `D-01` tiene de particular:** `cmd_supersede` **imprime** «S-001 marcada reemplazada por S-002» y no lo guarda. Es un dato que existe, se muestra, y se pierde al cerrar la consola — que es literalmente lo que [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) manda evitar, incumplido por el programa que implementa esa misma regla.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| La regla «ninguna se borra» se prueba **contando**, no mirando el estado | CP-001 y CP-003 del [resultado](resultado_pruebas.md) |
| Los dos defectos se prueban con fallo esperado en vez de arreglarse, para no salirse del plan aprobado | §4 de este documento |
| Los dos transversales se comprueban aunque el plan no les escribió caso | `D-03` del resultado |
| El enlace del reemplazo existe **en un solo sentido**, y se deja dicho: desde la nueva se llega a la vieja, al revés no | CP-001, paso 6 |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el reemplazo guarde qué y cuándo (`D-01`) | Fase `B-EP-006-HU-007`, propuesta |
| Que archivar deje fecha (`D-02`) | La misma |
| Buscar por palabra y por significado | [HU-003](../../HU-003-busqueda-por-palabra/HU-003-busqueda-por-palabra.md) y [HU-004](../../HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md) |

**La advertencia que deja esta fase:** el sistema está construido para no perder nada, y pierde justo lo que explica por qué algo dejó de aplicar. Conserva el texto viejo y no conserva el motivo del cambio.
