# Resultado de pruebas — Fase A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |
| **HU** | [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-004-HU-002 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Este repositorio en lectura y carpetas temporales. Estándar 23.2.1 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 2 | 2 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). Ninguna de las reglas que el programa **ve** se queda sin clasificar, y el registro no inventa ninguna. Lo que falla es más de fondo: **el analizador no ve cuatro reglas** que están escritas en `base/`, y **la clasificación no detiene nada** — ni siquiera se ejecuta en una corrida normal.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--toda-regla-está-en-el-registro-y-el-registro-no-inventa-reglas) | CA-01 | Crítica | Las 200 reglas que el analizador ve, contra las 205 entradas del registro | **Falla en la vuelta** | EV-01 | D-01 |
| [CP-002](plan_pruebas.md#cp-002--un-rango-no-clasifica-las-reglas-que-abarca) | CA-01 | Alta | El registro real, buscando rangos | Aprobado | EV-01 | — |
| [CP-003](plan_pruebas.md#cp-003--desde-el-registro-se-llega-al-programa-que-comprueba-la-regla) | CA-02 | Alta | Tres reglas validables, siguiendo el registro hasta el archivo | Aprobado | EV-01 | — |
| [CP-004](plan_pruebas.md#cp-004--hoy-nada-frena-una-regla-nueva-sin-clasificar) | CA-03 | Alta | Una regla inventada en una copia | **Falla** | EV-01 | D-02 |

---

### Detalle de CP-001 — Toda regla está en el registro, y el registro no inventa reglas

**La ida.** De las **200** reglas que `metareglas.reglas()` reconoce, **cero** quedan sin clasificar. La cifra viene de la fase `A-EP-001-HU-009`, que bajó 33 a cero, y sigue en cero.

**La vuelta.** El registro tiene **205 entradas**, y nueve de ellas nombran identificadores que el analizador **no reconoce como reglas**:

| Entrada del registro | ¿Existe en `base/`? | Cómo está escrita |
|---|---|---|
| `CQ1` `CQ2` `CQ3` `CQ4` | **Sí** | `### CQ1 · …` en [`base/16-cumplimiento-y-calidad.md`](../../../../../base/16-cumplimiento-y-calidad.md) — con tres almohadillas |
| `F12.1` `F12.5` `F12.8` `F12.9` `F12.10` | **Sí** | Viñetas dentro de [`F12`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md): `* **F12.1** — …` |

**Ninguna es inventada.** Las nueve existen. Lo que pasa es que **`metareglas.reglas()` solo reconoce lo que empieza por `## `**, así que las cuatro del capítulo 16 y las sub-reglas escritas como viñeta son invisibles para él.

**Por qué importa, y no es un detalle de conteo.** A una regla que el analizador no ve **no se le aplica ninguna de las veinte filas del checklist**: ni el molde de `M5`, ni el identificador de `M4`, ni las dependencias, ni la marca de validable. Las cuatro reglas del capítulo de cumplimiento —las que hablan de para quién se construye, de seguridad por defecto y de atributos de calidad— **nunca han pasado por su propio procedimiento**, y el programa lo reporta todo en verde. Es el defecto `D-01`.

> **Sale en verde por el mismo motivo por el que pasaría un validador que no valida nada.** Contar solo lo que se reconoce y no comprobar la vuelta hace que el hueco sea exactamente invisible.

---

### Detalle de CP-002 — Un rango no clasifica las reglas que abarca

Se buscó en el registro cualquier forma de rango. **No queda ninguno**: `C1` y `C17` aparecen cada una con su fila, y ni `C1–C17` ni `C1-C17` figuran como entrada.

**Es el arreglo de `A-EP-001-HU-009`, y sigue puesto.** Aquel registro decía «C1–C17» y el programa no lee rangos, así que quince reglas figuraban clasificadas sin estarlo. La prueba de esta fase es la que impide que vuelva: un rango no puede valer por diecisiete reglas, porque nadie sabría cuál de las diecisiete falta.

---

### Detalle de CP-003 — Desde el registro se llega al programa que comprueba la regla

| Regla validable | Programa que dice el registro | ¿Existe el archivo? |
|---|---|---|
| `04·S4` | `secretos.py` | Sí |
| `10·DEP2` | `dependencias.py` | Sí |
| `09·G4` | `rama.py` | Sí |

Las tres se resuelven **leyendo solo el registro**: la fila trae la regla, el programa y qué comprueba, y el archivo está donde dice. El CA-02 se cumple.

**Lo que la fase levantó de paso (T-03), contando contra lo que existe:**

| Medición, 2026-08-17 | Valor |
|---|---|
| Subcomandos de `validar.py` | **24** |
| Módulos validadores en `validadores/` | **35** |
| Módulos que el registro **no nombra nunca** | **10** — `cargador`, `citas`, `codigo`, `cruces`, `declaracion`, `entidades`, `estructura`, `historico`, `instalar`, `versiones` |

**Los diez no son un hueco de la clasificación.** Son programas que no comprueban una regla del estándar: unos preparan (`cargador`, `instalar`), otros comprueban documentos y no reglas (`historico`, `citas`, `versiones`). Se anotan para distinguir el hueco real de lo que está bien así, que es lo que el plan pedía en su métrica.

---

### Detalle de CP-004 — Hoy nada frena una regla nueva sin clasificar

| # | Qué se hizo | Qué salió |
|---|---|---|
| 1 | Escribir una regla `ZZ1` en una **copia**, sin clasificarla | Queda escrita |
| 2 | Correr el validador de meta-reglas sobre la copia | **La avisa**, con su archivo y su línea |
| 3 | Mirar con qué severidad | **AVISO**, no falla: no detiene nada |
| 4 | Comprobar si esa corrida ocurre en el trabajo normal | **No ocurre** |

**El paso 4 es el que hunde el CA-03.** `metareglas.py` **no tiene subcomando en `validar.py`**: de los 24 que hay, ninguno lo llama. Así que la vigilancia de que toda regla se clasifique existe, funciona… y **nunca se ejecuta** salvo que alguien la invoque a mano desde Python. Es el punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), y acá se ve el daño concreto: el CA-03 dice «una regla nueva no se publica sin clasificar», y hoy se publica sin que nada chiste.

> **Se escribió en una copia, no en `base/`.** Meter una regla de mentira en el cuerpo real dejaría el repositorio con una regla que nadie aprobó, aunque fuera un minuto.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Cuántas reglas ve el analizador y cuántas hay clasificadas | Corriendo `metareglas` sobre este repositorio | **200 vistas · 205 clasificadas · 0 sin clasificar** |
| 2 | Que las nueve «de más» existan de verdad | Buscándolas en el texto de `base/` | Las nueve existen |
| 3 | Que el capítulo 16 use `###` | Contando los encabezados de regla del árbol | **4 reglas con `###`, todas del 16**; el resto usa `##` |
| 4 | Que `metareglas` no tenga subcomando | Listando los 24 de `validar.py` | No lo tiene |
| 5 | Que la suite siga verde | `python validadores/pruebas.py` | 268 pruebas · verde, con 4 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | `metareglas.reglas()` solo reconoce lo que empieza por `## `. **Las cuatro reglas del capítulo 16 no existen para el programa**, así que nunca se les aplica ninguna de las 20 filas del checklist — y todo sale en verde | Probado con fallo esperado en [`validadores/pruebas.py`](../../../../../validadores/pruebas.py). El arreglo toca `metareglas.py`, que §2.1 del [plan aprobado](plan_trabajo.md) no declara ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Se propone |
| D-02 | **Alta** | La clasificación **no detiene**: sale como AVISO, y además `metareglas.py` **no tiene subcomando**, así que no corre en el trabajo normal. El CA-03 no se cumple de ninguna de las dos formas | Probado con fallo esperado. Es el punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), que ya está abierto |
| D-03 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales** de la HU. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-01--toda-regla-aparece-clasificada) | CP-001, CP-002 | De las que el programa ve, ninguna falta, y no hay rangos. **Pero cuatro reglas escritas en `base/` no las ve** | **No** |
| [CA-02](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-02--la-regla-comprobada-dice-quién-la-comprueba) | CP-003 | Las tres reglas probadas llegan a su programa leyendo solo el registro, y el archivo existe | Sí |
| [CA-03](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-03--una-regla-nueva-no-se-publica-sin-clasificar) | CP-004 | Avisa, pero **no detiene**, y no corre en el trabajo normal | **No** |
| Transversal · Límites | Prueba propia, fuera del plan | La regla derogada **se conserva marcada y no se le exige clasificación nueva**: se comprobó sobre las derogadas reales del árbol | Sí |
| Transversal · No regresión | Verificación 1 | La clasificación existente no se perdió: sigue en 0 sin clasificar tras sumar reglas nuevas desde la 21.x | Sí |

**Los que no cumplen:** el **CA-01** y el **CA-03**. Los dos se trasladan a una fase `B-EP-004-HU-002`, que además cierra el punto 2 del pendiente 53.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Reglas sin clasificar | 0, o listadas | **0** de las 200 que el programa ve | Sí |
| Entradas que nombran reglas inexistentes | 0, o listadas | **0 inventadas**; 9 que el analizador no reconoce, listadas | Sí |
| Rangos en el registro | 0, o anotados | **0** | Sí |
| Reglas validables sin programa identificado | Todas anotadas | 10 módulos que el registro no nombra, anotados y distinguidos del hueco real | Sí |
| Pruebas de la suite | Línea base + 2, en verde | Línea base + **8**, en verde con 2 fallos esperados | Sí |

**Lo que no se cumplió:** ninguna meta. Las siete en verde y la fase no cumple. Ninguna medía si el analizador **ve** todas las reglas, que es donde está el agujero.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el CA-02 quedó verificado, no hay rangos y no falta ninguna clasificación entre las reglas que el programa reconoce. Pero el CA-01 pide que **toda** regla aparezca clasificada, y cuatro reglas del capítulo 16 no pasan siquiera por el analizador — su clasificación en el registro es una fila que nadie comprueba. Y el CA-03 pide que una regla nueva no se publique sin clasificar: hoy sale un aviso que no detiene, desde un programa que en el trabajo normal no se ejecuta.

**Qué falta para que cumpla:**

1. Que `metareglas.reglas()` reconozca también las reglas escritas con `###` y las sub-reglas en viñeta (`D-01`).
2. Que `metareglas.py` tenga su subcomando en `validar.py`, y que la regla sin clasificar sea **falla** y no aviso (`D-02`).

Los dos tocan archivos que el plan aprobado no declara. **Piden una fase `B-EP-004-HU-002`**, que de paso cierra el punto 2 del pendiente 53.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ClasificacionDeCadaRegla`: 8 pruebas — 6 en verde y 2 como fallo esperado, que son `D-01` y `D-02` |
| EV-02 | Mediciones | Las tablas de §2 y §3 |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 268 pruebas, verde, 4 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
