# Funcionalidad implementada — Fase A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra (módulo Memoria)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** La búsqueda encuentra, filtra, ignora acentos y mantiene el índice al día. No dice **dónde** está lo que encontró, y eso es la mitad del CA-01. Este documento cierra lo que la fase hizo; lo que falta pide una fase `B-EP-006-HU-003`.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |
| **Módulo** | Memoria — [`memoria/memoria.py`](../../../../../memoria/memoria.py) · [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) |
| **Especificación del módulo** | No la hay aparte: la especificación son los CA de [HU-003](../HU-003-busqueda-por-palabra.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-003: [CA-01](../HU-003-busqueda-por-palabra.md#ca-01--se-busca-por-palabra-y-aparece-dónde-está), [CA-02](../HU-003-busqueda-por-palabra.md#ca-02--se-puede-filtrar-por-tipo-y-por-alcance), sus tres RNF y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 |
| **Commit** | Pendiente de autorización del usuario |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió las pruebas que faltaban y encontró dos defectos que llevaban ahí desde que existe la búsqueda.** El subcomando `search`, el índice de texto completo y sus tres triggers están en producción; lo que no existía era una sola prueba que los vigilara.

Ahora hay dieciocho. Dos de ellas están rojas a propósito, porque los dos defectos son reales.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Buscar por palabra sobre lo activo | programa | [`memoria/memoria.py`](../../../../../memoria/memoria.py) · `cmd_search` | ✅ Ya existía | CP-001 |
| **Decir dónde está lo encontrado** | programa | `cmd_search` — el `SELECT` no trae `where_` | ❌ **No existe** | CP-001, paso 2 |
| Ignorar acentos en los dos sentidos | datos | [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) · `remove_diacritics 2` | ✅ Ya existía | CP-002 |
| Filtrar por tipo y por alcance | programa | `cmd_search`, filtro parametrizado | ✅ Ya existía | CP-003 |
| Que lo archivado no aparezca y no se pierda | programa + datos | `estado='activa'` en el filtro; `cmd_archivar` no borra | ✅ Ya existía | CP-004 |
| Mantener el índice al día | datos | Los tres triggers `senales_ai` · `senales_au` · `senales_ad` | ✅ Ya existía | CP-005 |
| **Cerrar la conexión cuando no hay resultados** | programa | `cmd_search`, camino de salida temprana | ❌ **Falta** | CP-005, borde |
| Las siete exigencias, con red | pruebas | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `BusquedaPorPalabra` | ✅ Escritas acá | 18 pruebas |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | Encuentra por palabra y con acentos; **no dice dónde está** | ❌ |
| CA-02 | Filtros de tipo y alcance, combinables; lo archivado fuera y conservado | ✅ |
| RNF · Autonomía · Rendimiento · Inocuidad | Nada instalado; 0,0046 s sobre 237 señales; buscar no escribe | ✅ |
| Transversal · Privacidad | Se cortó el socket y la búsqueda encontró igual | ✅ |
| Transversal · Límites | Memoria vacía, término vacío y término de solo signos: sin error | ✅ |

---

## 3. Qué se probó

Dieciocho casos automatizados y cuatro verificaciones a mano. Los tres que importan:

- **La ubicación**, que es la que destapó `D-01`. Sin ese paso, «la búsqueda encuentra» habría pasado por CA-01 cumplido.
- **Los acentos en los dos sentidos.** Un índice que normaliza solo al guardar, o solo al buscar, pasa la mitad de los casos.
- **Que la archivada siga en la base.** Con solo comprobar que no aparece, un programa que borrara pasaría igual.

Detalle en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 4. Los dos defectos, y por qué no se arreglaron acá

| Defecto | Qué le falta | Por qué no se tocó |
|---|---|---|
| `D-01` · la búsqueda no dice dónde | Agregar `where_` al `SELECT` y a la línea impresa | §2.1 del [plan aprobado](plan_trabajo.md) dice: «`memoria.py` y el esquema no se tocan». [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) no deja salirse del plan, y ampliarlo es del usuario |
| `D-02` · conexión sin cerrar | `con.close()` antes del `return` del camino vacío | Lo mismo |

**Los dos quedaron probados, no anotados.** Cada uno tiene su prueba marcada `expectedFailure`: la suite se queda verde, el defecto queda escrito con su evidencia, y el día que alguien lo arregle la prueba pasa a «éxito inesperado» y obliga a volver a este documento. Una prueba borrada o comentada no habría hecho ninguna de las tres cosas.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| Todo se corre en modo léxico: la HU pide que funcione **sin instalar nada**, y dejar entrar la semántica ataría el resultado a que el modelo esté puesto | §0 del [resultado](resultado_pruebas.md) |
| Los dos defectos se prueban con fallo esperado en vez de arreglarse, para no salirse del plan aprobado | §4 de este documento |
| Los dos transversales se comprueban aunque el plan no les escribió caso, y se dice que el plan no los cubría | `D-03` del resultado |
| La privacidad se prueba **cortando el socket**, no leyendo el código: así falla si algo intenta salir, en vez de pasar callada | Prueba `test_privacidad_la_busqueda_lexica_no_abre_ninguna_conexion` |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que la búsqueda diga dónde está lo encontrado (`D-01`) | Fase `B-EP-006-HU-003`, propuesta |
| Que el camino sin resultados cierre su conexión (`D-02`) | La misma |
| Buscar por significado | [HU-004](../../HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md) |
| Marcar lo que dejó de aplicar | [HU-007](../../HU-007-marcar-lo-que-dejo-de-aplicar/HU-007-marcar-lo-que-dejo-de-aplicar.md) |

**La advertencia que deja esta fase:** las seis metas del plan de pruebas quedaron en verde y la fase no cumple. Las métricas medían cobertura, acentos, señales perdidas y herramientas instaladas — ninguna medía lo único que falla. Un tablero verde no es un veredicto.
