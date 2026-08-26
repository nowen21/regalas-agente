# Resultado de pruebas — Fase A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |
| **HU** | [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-006-HU-001 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario ese mismo día |
| **Ambiente y versión** | Bases temporales para lo automatizado y una lectura en solo lectura de `memoria/senales.db` para el inventario. Estándar 23.2.0 · Python 3.11.9 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 2 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). Los tres casos corrieron y los dos CA numerados quedaron verificados; lo que deja la fase en «No cumple» es un criterio **transversal** de la HU que el plan aprobado nunca puso en su alcance. El detalle, en §6.

**Casos no ejecutados y por qué:** ninguno.

**El que falló:** [CP-001](plan_pruebas.md#cp-001--cinco-decisiones-reales-clasificadas-con-el-criterio). No falló el criterio: falló lo que el criterio consigue. Las cinco decisiones se clasificaron sin ambigüedad —el criterio decide—, y **ninguna de las cinco llegó a guardarse**. El paso 3 del caso pide comparar el veredicto contra lo que de verdad se hizo, y ahí la comparación da cero de cinco.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--cinco-decisiones-reales-clasificadas-con-el-criterio) | CA-01 | Alta | 2026-08-17 | Cinco decisiones de fases ya cerradas de este mismo repositorio | **Falla en el paso 3** | EV-02 | D-01 |
| [CP-002](plan_pruebas.md#cp-002--la-señal-sin-tipo-no-entra-y-la-que-no-declara-alcance-entra-con-el-de-proyecto) | CA-02 | Crítica | 2026-08-17 | Bases temporales, por la línea de comandos y por llamada directa | Aprobado | EV-01 | — |
| [CP-003](plan_pruebas.md#cp-003--los-diez-tipos-contra-su-uso-real) | RNF | Media | 2026-08-17 | `memoria/senales.db` abierta en solo lectura: 237 señales | Aprobado | EV-03 | — |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá. Ninguno de más, ninguno de menos.

---

### Detalle de CP-001 — Cinco decisiones reales clasificadas con el criterio

**El problema que resuelve:** que el criterio de [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) —se guarda lo que no se recupera leyendo el código— sirva para decidir sin discutir cada vez.

**La precondición:** ninguna. Se eligieron decisiones **difíciles a propósito**, de fases cerradas de este repositorio.

**Paso 1 — el criterio queda a la vista.** `13·DOC5` pide registrar como señal lo que no se puede reconstruir leyendo el código: la decisión y su motivo, el error resuelto, el supuesto, la alternativa descartada. Con su tipo y a quién sirve.

**Pasos 2 y 3 — las cinco, con su veredicto y contra lo que de verdad pasó:**

| # | Decisión real | De qué fase | Veredicto con el criterio | ¿Se guardó? |
|---|---|---|---|---|
| 1 | «0,21 s al abrir la sesión no se nota» | [A-EP-005-HU-009](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/resultado_pruebas.md) | **Señal** · `decision`, alcance `proyecto:estandar-agente`. Es un juicio del usuario sobre un número: leyendo el código no se recupera ni el número ni el juicio | **No** |
| 2 | El `estado-fase` sigue copiando el veredicto y un programa compara; no se cambia el molde para que lo enlace | [A-EP-004-HU-014](../../../EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/A-EP-004-HU-014-comparar-los-dos-veredictos/funcionalidad_implementada.md) | **Señal** · `alternativa-descartada`. La salida descartada y el motivo no están en ningún programa: el programa solo muestra la elegida | **No** |
| 3 | El [pendiente 25](../../../../../pendientes/hecho/las-reglas-de-como-se-escribe-si-llegaban-puestas.md) se cierra por falso: su causa se dedujo en vez de verificarse | [A-EP-005-HU-009](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/funcionalidad_implementada.md) | **Señal** · `aprendizaje`, alcance `organizacion`. El caso difícil: el motivo **sí** está escrito, en el propio pendiente. Pero el criterio dice «no se recupera leyendo **el código**», y un pendiente cerrado no es código; y lo que sirve a cualquier proyecto —deducir una causa en vez de verificarla— se pierde si vive en el pendiente de este repositorio | **No** |
| 4 | Que `instalar()` prepare su propia salida en vez de depender de `main()` | [A-EP-007-HU-006](../../../EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/funcionalidad_implementada.md) | **No es señal** · es trabajo pendiente, no aprendizaje. Se resolvió abriendo la fase `B-EP-007-HU-001`, y ahí sí se recupera leyendo el código | **No, y correcto** |
| 5 | Los tipos del esquema que no se usan se anotan, no se quitan | §2.6 del [plan_trabajo.md](plan_trabajo.md) de esta fase | **Señal** · `restriccion`, alcance `modulo:memoria`. El motivo —quitar un tipo rompe las señales que ya lo tienen— no está en el esquema, que no tiene lista cerrada en SQL | **No, todavía** |

**Paso 4 — la que no se pudo clasificar:** ninguna quedó sin veredicto. La número 3 fue la que costó, y el criterio alcanzó: la duda era si «leyendo el código» incluye leer un documento del repositorio, y la resuelve la segunda mitad de la regla, la del alcance — lo que sirve a cualquier proyecto no se puede quedar en un archivo de este.

**Paso 5 — dónde dos personas clasificarían distinto:** en la 3 y en la 5. Las dos están escritas en algún documento del repositorio, y quien lea «no se recupera del código» como «no está escrito en ninguna parte» las descartaría. **Ese es el hueco del criterio**, y queda como defecto `D-02`.

**Qué salió distinto de lo esperado:** el paso 3. El caso esperaba «se ve si el criterio reproduce lo que se hizo», y lo que se ve es que **no hubo nada que reproducir**. De las cinco, cuatro son señal y ninguna se guardó. Medido sobre toda la base: `memoria/senales.db` tiene **237 señales**, y del alcance `proyecto:estandar-agente` tiene **una sola**, `S-003`, del 2026-07-25 — antes de que este repositorio abriera ninguna de sus épicas.

---

### Detalle de CP-002 — La señal sin tipo no entra, y la que no declara alcance entra con el de proyecto

**El problema que resuelve:** que ninguna señal quede guardada sin saber de qué tipo es ni a qué alcanza.

**La precondición:** una base temporal creada desde [`memoria/esquema.sql`](../../../../../memoria/esquema.sql).

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Guardar una señal sin tipo | No entra | No entró. `memoria.py add` sin `--tipo` termina con código distinto de cero y la tabla queda en cero filas |
| 2 | Guardar una sin alcance | Entra, con alcance de proyecto | Entró con `scope='proyecto'` |
| 3 | Guardar una con un tipo que no existe | No entra | No entró: `cmd_add` corta con «tipo invalido» y lista los diez válidos |
| 4 | Guardar una completa | Entra, con lo que declaró | Entró con su tipo, su alcance `modulo:memoria` y estado `activa` |
| 5 | Comprobar que la base real no se tocó | Intacta | Intacta. Cada prueba compara la huella SHA-256 de `memoria/senales.db` antes y después |

**Además** se comprobó que los diez tipos declarados son exactamente los diez que el programa acepta: se guardó uno de cada uno y entraron los diez.

> **Quién rechaza el tipo inventado.** No es SQLite: el esquema declara `tipo TEXT NOT NULL` y no tiene lista cerrada. Quien rechaza es `memoria.cmd_add`, en el programa. Una inserción por SQL directo entraría con cualquier texto. La prueba lo dice en su documentación de clase para que nadie lea el verde como una garantía del esquema. Queda como defecto `D-03`.

---

### Detalle de CP-003 — Los diez tipos contra su uso real

**El problema que resuelve:** saber qué parte del esquema está viva, sin romper lo que ya se guardó.

**La precondición:** `memoria/senales.db` abierta con `mode=ro`, en solo lectura.

**Pasos 1 a 4 — los diez tipos declarados y lo que se usó, medido el 2026-08-17 sobre 237 señales:**

| Tipo declarado | Señales | Ejemplo real más antiguo |
|---|---:|---|
| `decision` | 74 | `S-002` · «Terminología: 'el agente' = Claude Code; 'el estándar' = las reglas» |
| `aprendizaje` | 58 | `S-001` · «No usar `git add -A`; stagear por ruta explícita» |
| `error-resuelto` | 28 | `S-065` · «Fix animación mapa GI — sistema cascada replicado 1:1 de TipoA» |
| `restriccion` | 20 | `S-021` · «`schema_manager` borraba TODA la BD por defecto (ya blindado)» |
| `patron` | 20 | `S-066` · «Chip ESTÁS AQUÍ compuesto con icono circular animado + shimmer» |
| `deuda-tecnica` | 19 | `S-023` · «Endurecimiento crítico backend pendiente (grupo C)» |
| `gotcha` | 18 | `S-019` · «`permiso_requerido` await sobre `_impl` síncrono del list genérico» |
| `alternativa-descartada` | **0** | **Nunca usado** |
| `supuesto` | **0** | **Nunca usado** |
| `pregunta-abierta` | **0** | **Nunca usado** |

**Siete de diez tipos vivos. Tres nunca usados**, en 237 señales acumuladas entre el 2026-07-25 y el 2026-08-17. Ninguno se quitó del esquema (riesgo `R-01`): quitar un tipo rompería las señales que lo tienen, y el esquema no las borra nunca.

**Los alcances, que el plan no pidió contar y salen de la misma lectura:**

| Forma de alcance | Señales | Nota |
|---|---:|---|
| `proyecto:<slug>` | 165 | En diez proyectos distintos |
| `organizacion` | 72 | Lo que sirve a cualquier proyecto |
| `modulo:<slug>` | **0** | **Nunca usado**, aunque el esquema lo declara |

**Paso 5 — la copia no se modificó:** la base se abrió con `file:…?mode=ro`, que impide escribir. La huella SHA-256 del archivo es la misma antes y después, y las pruebas automatizadas la comprueban en cada caso.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que la base real no se tocara | Huella SHA-256 de `memoria/senales.db` comparada en cada prueba de la clase nueva | Igual antes y después |
| 2 | Cuántas señales tiene este repositorio | `SELECT` por alcance sobre la base en solo lectura | 1 de 237, la `S-003` |
| 3 | Que los diez tipos del programa sean los diez del esquema | `memoria.TIPOS` contra el comentario de `esquema.sql` | Coinciden |
| 4 | Que la suite entera siga en verde | `python memoria/pruebas.py` | 21 pruebas, en verde |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | El criterio está escrito y decide, pero **en este repositorio no se aplica**: cuatro decisiones de fases cerradas eran señal y ninguna se guardó. Una sola señal de alcance `proyecto:estandar-agente` en 237 | Se reporta al usuario. No se corrige acá: guardar señales retroactivamente por decisión del agente es exactamente lo que `RN-04` prohíbe —«lo que se guarda se decide al guardarlo, no automáticamente» |
| D-02 | Media | «No se recupera leyendo **el código**» deja fuera lo que sí está escrito en un documento del repositorio. Dos de las cinco se clasificarían distinto según cómo se lea | Se reporta. Cambiar el texto de `13·DOC5` es cambio de `base/` y no estaba en el alcance de esta fase (`02·F20`) |
| D-03 | Baja | La lista de tipos es cerrada **en el programa**, no en el esquema. Una inserción por SQL directo entra con cualquier tipo | Dicho en la documentación de la clase de pruebas y acá. El RNF de estabilidad de la HU pide lista cerrada y hoy lo cumple una sola de las dos puertas |
| D-04 | Media | Los dos **criterios de aceptación transversales** de la HU —límites y privacidad— **no tienen ningún caso** en el plan de pruebas, que aun así declara 100% de cobertura | El plan aprobado no se modifica. Queda dicho acá y en el veredicto: la cobertura real es 2 de 2 CA numerados, y 0 de 2 transversales |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-01--el-criterio-de-qué-se-guarda-está-escrito) | CP-001 | El criterio existe y clasificó las cinco sin quedarse sin veredicto. Su tercer paso de validación —«los tres se resuelven sin discusión»— se cumple; el que no se cumple es el uso | **Sí**, con la salvedad `D-02` |
| [CA-02](../HU-001-que-se-guarda-tipos-y-alcances.md#ca-02--cada-cosa-guardada-tiene-tipo-y-alcance) | CP-002 | Tipo obligatorio y validado contra lista; alcance con valor por omisión. Ninguna señal puede quedar sin los dos | **Sí** |
| RNF · Claridad | CP-001 | Se aplicó sin haber diseñado ningún método nuevo | Sí |
| RNF · Estabilidad | CP-002, CP-003 | Lista cerrada de diez, cerrada en el programa (`D-03`). Tres tipos sin usar nunca | Sí, con `D-03` |
| Transversal · Límites | **Ninguno** | El plan no escribió caso para «algo que parece de dos tipos a la vez» | **No probado** |
| Transversal · Privacidad | **Ninguno** | `13·DOC5` **no dice** que no se guardan datos personales ni claves. Se leyó el texto completo de la regla | **No** |

**Los que no cumplen:** el transversal de **privacidad** — falta que `13·DOC5` diga que no se guardan datos personales ni claves. El de **límites** quedó sin probar: falta el caso de qué se hace cuando algo parece de dos tipos a la vez. Los dos se trasladan a una fase `B-EP-006-HU-001`, porque el plan aprobado de esta no los declara y `02·F8` no deja salirse de él.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias con caso | Plan de pruebas §5 | 100% | 100% de los CA numerados y los RNF; **0% de los dos transversales**, que el plan no contó | **No** — `D-04` |
| Casos ejecutados | Plan de pruebas §12 | 3 de 3 | 3 de 3 | Sí |
| Señales de la base real modificadas | Plan de pruebas §12 | 0 | 0, comprobado por huella | Sí |
| Decisiones que no se pudieron clasificar | Plan de pruebas §12 | Todas anotadas, con el motivo | Ninguna quedó sin clasificar; las dos discutibles están anotadas | Sí |
| Tipos del esquema quitados | Plan de pruebas §12 | 0 | 0 | Sí |
| Tipos sin uso | Plan de pruebas §12 | Contados, con su fecha | 3 de 10, contados el 2026-08-17 | Sí |

**Lo que no se cumplió:** la cobertura, y no porque falte correr un caso sino porque el plan aprobado contó mal lo que había que cubrir. El plan no se reescribe (`02·F4`): queda dicho acá y arrastra a `D-04`.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** los dos criterios de aceptación numerados quedaron verificados —el criterio decide y el esquema obliga a tipo y alcance—, y el inventario dejó el número que la fase venía a buscar: siete tipos vivos, tres nunca usados, y una sola señal de este repositorio en 237. Pero el criterio transversal de **privacidad** de la HU está en «No»: `13·DOC5` no dice que no se guarden datos personales ni claves. La [plantilla del resultado](../../../../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) no admite estado intermedio —«si algo de lo pedido falta, es No cumple»— y una fase no cierra con un CA en «No».

**Que el plan aprobado no lo hubiera puesto en su alcance no lo convierte en cumplido.** Esta es la **única** fase de HU-001 (§8 de la HU): si cerrara en «Cumple», los dos transversales quedarían sin verificar y sin que nadie los vuelva a mirar. Es el mismo error que `13·DOC20` y `00·ID3` vienen a impedir.

**Qué falta para que cumpla:**

1. Que `13·DOC5` diga que no se guardan datos personales ni claves — es cambio de `base/`, y lo decide el usuario (`02·F20`).
2. Que se escriba y se corra el caso del transversal de **límites**: qué se hace cuando algo parece de dos tipos a la vez.
3. Los dos anteriores no caben en esta fase: su plan aprobado no los declara y `02·F8` prohíbe salirse de él. **Piden una fase `B-EP-006-HU-001`**, y esa es la propuesta que esta fase deja sobre la mesa.

**Lo que no falta para cerrar la fase, y sí queda abierto:** `D-01` —el criterio funciona y este repositorio no lo usa— no es un criterio de aceptación de la HU. Es un hallazgo de la corrida, y va al usuario como reporte.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `TiposYAlcances`: 5 pruebas, en verde |
| EV-02 | Clasificación a mano | La tabla de cinco filas de §2, con el enlace a la fase de la que sale cada decisión |
| EV-03 | Inventario de la base | La tabla de diez tipos de §2, contada el 2026-08-17 sobre 237 señales |
| EV-04 | Corrida completa | `python memoria/pruebas.py` — 21 pruebas, en verde |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
