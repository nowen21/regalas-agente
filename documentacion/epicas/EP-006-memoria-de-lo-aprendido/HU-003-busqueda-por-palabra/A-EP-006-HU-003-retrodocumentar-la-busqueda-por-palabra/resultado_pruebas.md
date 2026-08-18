# Resultado de pruebas — Fase A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |
| **HU** | [HU-003](../HU-003-busqueda-por-palabra.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-006-HU-003 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario ese mismo día |
| **Ambiente y versión** | Bases temporales, y una **copia** de `memoria/senales.db` para medir el tiempo. Estándar 23.2.0 · Python 3.11.9 · SQLite con FTS5 |

**Todo se corrió en modo léxico** (`--lexica`). Lo que esta HU pide es que la búsqueda funcione **sin instalar nada**; dejar entrar la semántica —que en esta máquina sí está— probaría otra cosa y ataría el resultado a que el modelo esté puesto.

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 3 | 2 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). La búsqueda encuentra, filtra, ignora acentos y mantiene el índice al día. Lo que no hace es **decir dónde está lo que encontró**, que es la mitad del CA-01.

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--la-palabra-buscada-devuelve-la-señal-con-su-ubicación) | CA-01 | Alta | 2026-08-17 | Base temporal con tres señales, una con `where_` puesto | **Falla en el paso 2** | EV-01 | D-01 |
| [CP-002](plan_pruebas.md#cp-002--encuentra-igual-con-acentos-y-sin-ellos) | CA-01 | Alta | 2026-08-17 | «Facturación» y «Factura», buscadas en los dos sentidos | Aprobado | EV-01 | — |
| [CP-003](plan_pruebas.md#cp-003--los-filtros-de-tipo-y-alcance-devuelven-solo-lo-que-corresponde) | CA-02 | Alta | 2026-08-17 | Tres señales de dos tipos y dos alcances | Aprobado | EV-01 | — |
| [CP-004](plan_pruebas.md#cp-004--la-señal-archivada-no-aparece-y-sigue-existiendo) | CA-02 | Alta | 2026-08-17 | Una archivada y una vigente con la misma palabra | Aprobado | EV-01 | — |
| [CP-005](plan_pruebas.md#cp-005--el-índice-está-al-día-y-nada-se-instaló) | RNF | Crítica | 2026-08-17 | Alta, modificación y borrado, buscando después de cada uno | **Falla en el borde** | EV-01 | D-02 |

**Correspondencia con el plan:** 5 casos en el plan, 5 acá. Ninguno de más, ninguno de menos.

---

### Detalle de CP-001 — La palabra buscada devuelve la señal, con su ubicación

**El problema que resuelve:** que buscar sirva **para llegar**, no solo para saber que algo existe. El CA-01 se da por aprobado «cuando el resultado alcanza para abrir lo que se encontró».

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar una palabra que está en una sola señal | Devuelve esa señal | La devolvió, y solo esa |
| 2 | Comprobar que dice dónde está: archivo o área | Lo dice | **No lo dice.** La señal se guardó con `where_ = infra/redis.conf:12` y la salida es `S-001 · decision · [proyecto:x] Redis se cae` |
| 3 | Buscar una palabra que no está en ninguna | No devuelve nada, sin error | «(sin señales relevantes)», sin error |
| 4 | Comprobar que la base real no se tocó | Intacta | Intacta, comprobado por huella SHA-256 en cada prueba |

**Qué salió distinto de lo esperado y por qué:** `cmd_search` selecciona `rowid, id, tipo, titulo, scope, revisada` e imprime esos cinco. **`where_` no está ni en el `SELECT` ni en la línea impresa**, aunque el esquema lo guarda y `memoria.py add` lo pide con `--where`. El dato existe, se guarda, y la búsqueda no lo saca. Es el defecto `D-01`.

> **Qué se probó y qué no.** La prueba automatizada queda como **fallo esperado** (`unittest.expectedFailure`), no borrada ni comentada: el día que alguien arregle `cmd_search`, la prueba pasa a «éxito inesperado» y obliga a volver a este documento. Arreglarlo no cabía acá — §2.1 del [plan aprobado](plan_trabajo.md) dice que `memoria.py` no se toca, y [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) no deja salirse.

---

### Detalle de CP-002 — Encuentra igual con acentos y sin ellos

**El problema que resuelve:** que el acento no decida si se encuentra lo que se guardó.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar **sin** acento lo guardado con acento | Lo devuelve | «facturacion» encontró «Facturación electrónica» |
| 2 | Buscar **con** acento lo guardado sin acento | Lo devuelve | «factúra» encontró «Factura de compra» |
| 3 | Comprobar que los dos sentidos dan el mismo conjunto | Lo dan | El mismo |

**Por qué funciona:** el índice se declara con `tokenize='unicode61 remove_diacritics 2'`, que normaliza **al indexar y al consultar**. Los dos sentidos importaban justamente porque un índice que normaliza en un solo lado pasa la mitad de los casos.

---

### Detalle de CP-003 — Los filtros de tipo y alcance devuelven solo lo que corresponde

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar sin filtro | Todas las que coinciden | Las tres |
| 2 | Filtrar por un tipo | Solo las de ese tipo | Solo `S-002`, la de tipo `gotcha` |
| 3 | Filtrar por un alcance | Solo las de ese alcance | Solo `S-003`, la de `organizacion` |
| 4 | Combinar los dos | La intersección | Solo `S-001` |
| 5 | Filtrar por un tipo sin señales | Vacío, sin error | «(sin señales relevantes)», sin error |

---

### Detalle de CP-004 — La señal archivada no aparece, y sigue existiendo

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar la palabra | Devuelve la vigente | Devolvió `S-002` |
| 2 | Comprobar que la archivada no aparece | No aparece | No apareció |
| 3 | Comprobar que **sigue en la base** | Sigue: archivar no es borrar | Sigue, con `estado='archivada'` |
| 4 | Desarchivarla y buscar otra vez | Ahora aparece | Apareció |

**El paso 3 es el que separa archivar de borrar**, y por eso se comprueba que la fila siga ahí, no solo que no salga. Con el paso 2 solo, un programa que borrara pasaría el caso igual.

---

### Detalle de CP-005 — El índice está al día, y nada se instaló

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Guardar una señal nueva | Entra a la tabla | Entró |
| 2 | Buscarla de inmediato | Aparece: el índice se actualizó solo | Apareció. El trigger `senales_ai` la indexa en el mismo `INSERT` |
| 3 | Modificar su texto y buscar por la palabra nueva | Aparece | Apareció por la nueva, y **dejó de aparecer por la vieja**: `senales_au` borra y reinserta |
| 4 | Borrar la señal y buscar | Ya no aparece | Ya no aparecía: `senales_ad` la saca del índice |
| 5 | Comprobar que no hizo falta instalar nada | Nada instalado | Nada. Todo corrió con el `sqlite3` que trae Python 3.11.9; FTS5 viene compilado |

**El borde que el caso destapó, fuera de sus cinco pasos:** cuando la búsqueda **no encuentra nada**, `cmd_search` imprime «(sin señales relevantes)» y retorna **sin cerrar la conexión**. En Windows el archivo queda tomado y no se puede borrar. Es el defecto `D-02`, y también quedó como fallo esperado.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que ninguna prueba tocara la base real | Huella SHA-256 de `memoria/senales.db` comparada en cada prueba | Igual antes y después |
| 2 | Qué imprime de verdad la búsqueda | Corriendo `cmd_search` y leyendo la línea | `S-001 · decision · [proyecto:x] Redis se cae` — sin `where_` |
| 3 | Cuánto tarda con el volumen real | Cinco búsquedas sobre una **copia** de la base de 237 señales | **0,0046 s** de promedio |
| 4 | Que la suite entera siga en verde | `python memoria/pruebas.py` | 39 pruebas · verde, con 2 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | La búsqueda **no dice dónde está** lo que encontró. El dato está guardado en `where_` y `cmd_search` ni lo selecciona ni lo imprime. Deja el CA-01 a medias: encuentra, pero no alcanza para abrir | Probado con fallo esperado en [`memoria/pruebas.py`](../../../../../memoria/pruebas.py). El arreglo —agregar `where_` al `SELECT` y a la línea— **no cabe en esta fase**: §2.1 del plan dice que `memoria.py` no se toca. Se propone al usuario |
| D-02 | Media | El camino «sin resultados» de `cmd_search` retorna **sin cerrar la conexión**. En Windows deja el archivo tomado; en cualquier sistema es un descriptor filtrado por búsqueda vacía | Igual: probado con fallo esperado y propuesto. Es una línea |
| D-03 | Baja | El plan de pruebas declara «cobertura 100%» y **no le escribe caso a ninguno de los dos criterios transversales** de la HU. Se probaron igual, y están en §5 marcados como lo que son | El plan aprobado no se modifica ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)). Es el mismo defecto de molde que aparece en las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-003-busqueda-por-palabra.md#ca-01--se-busca-por-palabra-y-aparece-dónde-está) | CP-001, CP-002 | Encuentra por palabra, con acentos y sin ellos, y calla sin error cuando no hay nada. **Pero no dice dónde está**, y así el resultado no alcanza para abrir lo que se encontró | **No** |
| [CA-02](../HU-003-busqueda-por-palabra.md#ca-02--se-puede-filtrar-por-tipo-y-por-alcance) | CP-003, CP-004 | Los filtros de tipo y alcance acotan, se combinan, y el vacío es un resultado válido. Lo archivado no aparece y sigue en la base | Sí |
| RNF · Autonomía | CP-005 | Todo corrió con el `sqlite3` de Python. Nada instalado, nada de red | Sí |
| RNF · Rendimiento | Verificación 3 | 0,0046 s por búsqueda sobre las 237 señales reales | Sí |
| RNF · Inocuidad | CP-005, prueba de huella | Buscar no cambia el archivo de la base | Sí |
| Transversal · Privacidad | Prueba propia, fuera del plan | Se cortó el socket durante la búsqueda léxica: encontró igual. El contenido no sale de la máquina | Sí |
| Transversal · Límites | Prueba propia, fuera del plan | Memoria vacía, término vacío, y términos de solo signos: los tres responden sin error | Sí |

**Los que no cumplen:** el **CA-01**, en su segunda mitad. Falta que la búsqueda imprima `where_`. El arreglo es de una línea y está fuera del alcance aprobado de esta fase: se traslada a una fase `B-EP-006-HU-003`, junto con `D-02`.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% — los 2 CA y los RNF | 100% de lo que el plan contó, **y además** los dos transversales que no contó | Sí |
| Casos ejecutados | Plan §12 | 5 de 5 | 5 de 5 | Sí |
| Señales de la base real modificadas | Plan §12 | 0 | 0, comprobado por huella | Sí |
| Señales perdidas al archivar | Plan §12 | 0 | 0 — CP-004 paso 3 | Sí |
| Diferencias de resultado por acentos | Plan §12 | 0 | 0, en los dos sentidos | Sí |
| Herramientas que hubo que instalar | Plan §12 | 0 | 0 | Sí |

**Lo que no se cumplió:** ninguna meta del plan. Todas las metas se cumplieron y aun así la fase **no cumple**, porque lo que falla es el CA-01 y ninguna métrica del plan lo medía. Es la advertencia que deja: un tablero de métricas en verde no es un veredicto.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** cuatro de las cinco exigencias funcionales quedaron verificadas, los tres RNF también y los dos transversales que el plan no cubrió se probaron y pasan. Pero el CA-01 pide que el resultado diga **dónde está** lo que se encontró, y la búsqueda no lo dice: `cmd_search` guarda el dato y no lo saca. La [plantilla del resultado](../../../../../plantillas/planes/resultados.md) §6 no admite estado intermedio.

**Qué falta para que cumpla:**

1. Que `cmd_search` seleccione `where_` y lo imprima en la línea del resultado (`D-01`).
2. Que el camino sin resultados cierre su conexión (`D-02`).

Los dos son de una línea y los dos tocan `memoria.py`, que el plan aprobado excluye. **Piden una fase `B-EP-006-HU-003`**, y esa es la propuesta que esta fase deja.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `BusquedaPorPalabra`: 18 pruebas — 16 en verde y 2 como fallo esperado, que son `D-01` y `D-02` |
| EV-02 | Medición de tiempo | §3, verificación 3: 0,0046 s sobre 237 señales |
| EV-03 | Corrida completa | `python memoria/pruebas.py` — 39 pruebas, verde, 2 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
