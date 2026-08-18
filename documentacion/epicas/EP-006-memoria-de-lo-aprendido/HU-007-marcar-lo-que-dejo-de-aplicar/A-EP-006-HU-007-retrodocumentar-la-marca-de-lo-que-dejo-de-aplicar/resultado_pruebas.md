# Resultado de pruebas — Fase A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` |
| **HU** | [HU-007](../HU-007-marcar-lo-que-dejo-de-aplicar.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-006-HU-007 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario ese mismo día |
| **Ambiente y versión** | Bases temporales. Estándar 23.2.0 · Python 3.11.9 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 2 | 2 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). Nada se borra —eso quedó comprobado señal por señal—, y lo marcado no se confunde con lo vigente. Lo que falla es la otra mitad del CA-01: **de una señal marcada no se sabe cuándo se marcó ni qué la reemplazó.** El dato se imprime en la consola y no se guarda en ninguna parte.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-reemplazo-conserva-la-vieja-marcada-y-enlazada) | CA-01 | Alta | 2026-08-17 | Dos señales, una reemplazando a la otra | **Falla en el paso 6** | EV-01 | D-01 |
| [CP-002](plan_pruebas.md#cp-002--lo-archivado-se-puede-seguir-leyendo-si-se-lo-busca-a-propósito) | CA-01 | Alta | 2026-08-17 | Una señal archivada, buscada de las dos formas | **Falla en el paso 4** | EV-01 | D-02 |
| [CP-003](plan_pruebas.md#cp-003--los-cinco-estados-uno-por-uno) | CA-02 | Crítica | 2026-08-17 | Cinco señales, una en cada estado | Aprobado | EV-01 | — |
| [CP-004](plan_pruebas.md#cp-004--la-señal-sin-revisar-hace-meses-se-distingue-de-una-fresca) | CA-02 · RNF | Alta | 2026-08-17 | Una señal fresca y una de hace 300 días | Aprobado | EV-01 | — |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

---

### Detalle de CP-001 — El reemplazo conserva la vieja, marcada y enlazada

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar las señales de la base | Sale un número | 1 |
| 2 | Reemplazar la señal por una nueva | Entra la nueva | Entró |
| 3 | Contar otra vez | El número subió en uno: nada se borró | 2. Nada se borró |
| 4 | Comprobar que la vieja quedó marcada | Marcada | `estado='reemplazada'` |
| 5 | Comprobar que desde la nueva se llega a la vieja | Se llega | Se llega: la columna `reemplaza` de la nueva trae `S-001`, porque la pone `add --reemplaza` |
| 6 | Comprobar que desde la vieja se sabe cuál la reemplazó | Se sabe | **No se sabe.** `cmd_supersede` imprime «S-001 marcada reemplazada por S-002» y **no guarda el `--by` en ninguna columna**. La vieja queda con `reemplaza = NULL` y sin fecha de reemplazo |

**Qué salió distinto y por qué.** El enlace existe en un solo sentido. Quien tiene la señal nueva llega a la vieja; quien abre la vieja ve que la reemplazaron y **no puede saber por cuál ni cuándo**. Es el defecto `D-01`, y el caso lo pedía explícitamente en su paso 6.

> **El dato se imprime y se pierde.** La consola lo dice, y al cerrarla no queda nada. Es exactamente lo que [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) viene a evitar, aplicado al programa que implementa esa misma regla.

---

### Detalle de CP-002 — Lo archivado se puede seguir leyendo si se lo busca a propósito

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Archivar una señal | Queda marcada | `estado='archivada'` |
| 2 | Buscarla en la búsqueda normal | No aparece | No apareció |
| 3 | Pedirla a propósito, incluyendo lo archivado | Aparece, con su contenido entero | Apareció con `memoria.py list`, que sí muestra el estado. El contenido está intacto: se comparó campo por campo antes y después de archivar |
| 4 | Comprobar que dice desde cuándo está archivada | Lo dice | **No lo dice.** Archivar no escribe fecha en ninguna columna. `cerrada_en` existe y se llena solo al **cerrar**, no al archivar |

**Qué salió distinto y por qué.** El esquema tiene dónde ponerlo —`cerrada_en` y `cierra_ref`— y el camino de archivar no los usa. Es el defecto `D-02`, y es el que deja en «No» el transversal de trazabilidad, que pide «quién lo marcó y cuándo».

---

### Detalle de CP-003 — Los cinco estados, uno por uno

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Poner una señal en cada uno de los cinco estados | Quedan las cinco | Quedaron: `activa`, `archivada`, `reemplazada`, `cerrada`, `revertida` |
| 2 | Buscar con la búsqueda normal | Aparece **solo** la activa | Solo la activa |
| 3 | Comprobar que las otras cuatro siguen en la tabla | Las cuatro | Las cuatro |
| 4 | Por cada estado, comprobar que hace lo que dice su nombre | Los cinco | Los cinco. `cerrada` además deja fecha y referencia |
| 5 | Contar el total antes y después del recorrido | El mismo | El mismo. **Ninguna se borró** |

---

### Detalle de CP-004 — La señal sin revisar hace meses se distingue de una fresca

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Poner las dos señales con sus fechas fijas | Quedan puestas | Una de hoy, otra de hace 300 días |
| 2 | Buscar y mirar cómo se muestra cada una | La vieja se distingue | La vieja sale con «sin verificar»; la fresca, sin marca |
| 3 | Revisar la vieja y volver a buscar | Ahora se muestra como fresca | Se muestra fresca |
| 4 | Comprobar que no depende de la fecha de hoy ni del huso | No depende | No depende: `meses_desde` compara fechas ISO, no instantes. Se probó el borde de los 181 días y una fecha que no es fecha |
| 5 | Comprobar que ninguna se borró ni cambió de estado | Ninguna | Ninguna |

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que ninguna prueba tocara la base real | Huella SHA-256 de `memoria/senales.db` en cada prueba | Igual antes y después |
| 2 | Qué guarda de verdad el reemplazo | Reemplazando y leyendo la fila completa | `estado='reemplazada'`, `reemplaza=NULL`, sin fecha |
| 3 | Que marcar no cambie el contenido | Comparando `titulo`, `what`, `why`, `learned`, `tipo`, `scope` y `creada` antes y después de archivar | Idénticos |
| 4 | Que la suite entera siga verde | `python memoria/pruebas.py` | 52 pruebas · verde, con 4 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | `cmd_supersede` no guarda **qué reemplazó** a la señal ni **cuándo**. Lo imprime en consola y lo pierde. El enlace queda en un solo sentido | Probado con fallo esperado en [`memoria/pruebas.py`](../../../../../memoria/pruebas.py). El arreglo —escribir `reemplaza` y una fecha en el `UPDATE`— toca `memoria.py`, que §2.1 del [plan aprobado](plan_trabajo.md) excluye. Se propone al usuario |
| D-02 | Media | **Archivar no deja fecha.** El esquema tiene `cerrada_en` y el camino de archivar no la usa, así que de una señal podada no se sabe cuándo se podó | Igual: probado con fallo esperado y propuesto |
| D-03 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a ninguno de los dos transversales** de la HU. Se probaron igual, y están en §5 | El plan aprobado no se modifica. Es el mismo defecto de molde que traen las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-01--lo-que-dejó-de-aplicar-queda-marcado-y-visible) | CP-001, CP-002 | Sigue existiendo y queda marcado, sí. **Con la fecha y qué lo reemplazó, no**: ninguna de las dos cosas se guarda | **No** |
| [CA-02](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-02--lo-marcado-no-se-confunde-con-lo-vigente) | CP-003, CP-004 | Los cuatro estados no vigentes quedan fuera de la búsqueda, y lo viejo sin revisar se distingue de lo fresco | Sí |
| RNF · nada se borra | CP-001, CP-003 | El total no bajó en ningún recorrido | Sí |
| Transversal · No regresión | Verificación 3 | Marcar no altera el contenido original: siete campos idénticos antes y después | Sí |
| Transversal · Trazabilidad | CP-001 p.6, CP-002 p.4 | Al **cerrar** queda quién y cuándo. Al **archivar** y al **reemplazar**, no | **No** |

**Los que no cumplen:** el **CA-01** y el transversal de **trazabilidad**, los dos por la misma causa: dos de los tres caminos que marcan una señal no dejan rastro de cuándo ni de qué. Se trasladan a una fase `B-EP-006-HU-007`.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 100% de lo que el plan contó, más los dos transversales que no contó | Sí |
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| Señales borradas | Plan §12 | **0** | 0, contado antes y después de cada recorrido | Sí |
| Señales de la base real modificadas | Plan §12 | 0 | 0, comprobado por huella | Sí |

**Lo que no se cumplió:** ninguna meta del plan — y aun así la fase no cumple. Igual que en `A-EP-006-HU-003`: las metas medían que nada se perdiera, y lo que falla es que nada se **anote**.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el CA-02 quedó verificado a fondo —los cuatro estados salen de la búsqueda, ninguna señal se borra en ningún recorrido, y la vigencia distingue lo viejo de lo fresco sin depender del huso—. El CA-01 no: pide que lo marcado quede «con la fecha y qué lo reemplazó», y ni archivar ni reemplazar guardan ninguna de las dos cosas. `cmd_supersede` lo dice por consola y no lo escribe.

**Qué falta para que cumpla:**

1. Que `cmd_supersede` guarde el `--by` y la fecha en la señal marcada (`D-01`).
2. Que archivar deje fecha (`D-02`).

Los dos tocan `memoria.py`, que el plan aprobado excluye. **Piden una fase `B-EP-006-HU-007`.**

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `MarcarLoQueDejoDeAplicar`: 13 pruebas — 11 en verde y 2 como fallo esperado, que son `D-01` y `D-02` |
| EV-02 | Corrida completa | `python memoria/pruebas.py` — 52 pruebas, verde, 4 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
