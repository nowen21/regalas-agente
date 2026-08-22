# Resultado de Pruebas — Fase A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas` |
| **HU** | [HU-011](../HU-011-el-inventario-de-funcionalidades.md) — `CA-01`, `CA-02`, `CA-03` |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), aprobado por el usuario el 2026-08-21 («si», junto con la HU) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-21 |
| **Ejecutado por** | El agente; cada comprobación con su comando o lectura registrada |
| **Ambiente y versión** | Este repositorio (árbol sin commitear, estándar 28.2.0) y `shopnest-mesa` en solo lectura |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

**CA-01 · CP-001 — el molde contra el semilla, en las dos direcciones**

**El problema que resuelve:** un molde que pida menos que el caso real deja huecos por donde vuelve el alcance asumido; uno que arrastre el dominio del semilla viola la base agnóstica.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir [`plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`](../../../../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) y buscar los cuatro estados | Existe / Parcial / Por construir / Por confirmar, con «por confirmar» como pregunta | Los cuatro están, en la nota del §1; la cabecera dice «lo que diga "por confirmar" es una pregunta, no una decisión» |
| 2 | Buscar la sección de lo que el usuario ya definió y la marca de preguntas abiertas | Las dos están, con su instrucción | §0 con su nota («nada que no esté acá se da por decidido») y §3 con las `P-n` numeradas |
| 3 | Leer la caja | Acompaña a la propuesta; madura hasta manual | Lo dice, y agrega el rasgo del proyecto chico: la puerta es la aprobación, no el tamaño |
| 4 | Dirección semilla→molde | Nada del semilla sin sitio | Las seis secciones del semilla caben: sus §0-§3 en los §0-§1 del molde (grupos), su §4 en el §2 (proyección), su §5 en el §3 (preguntas), su §6 en el §4 (qué pasa al aprobar), su firma en la nota final |
| 5 | Dirección molde→semilla | Lo que el molde pide y el semilla no tiene, anotado para el aviso | Una cosa: el molde pide la **cuenta por grupo** y el semilla la trae solo global (§3: «9 existen, 4 parciales, 21 por construir»). Queda anotado para el aviso de cierre |
| 6 | Buscar dominio del semilla | Cero | `grep -ci "itil\|magerit\|shopnest"` dio **0** |
| 7 | Correr la comprobación por programa | En verde para el molde | **Distinto de lo esperado, y se declara:** `validar.py plantilla` valida un **documento contra** un molde, no moldes (exige el argumento `documento`); el paso se cubrió con `validar.py estandar` (enlaces y marcas del archivo nuevo: sin fallas) y el trinquete de marcas (0 rayas, 0 semirayas) |

**Cómo se verificó que la pareja cumple:** los pasos 4 y 5 son los que deciden (el molde pide todo lo que el caso real necesitó, y lo que agrega quedó anotado); el 6 protege `20·M3`. El desvío del paso 7 es del plan, no del molde: el programa citado no aplica a moldes, y la comprobación equivalente corrió y está en verde. Evidencia EV-01.

---

**CA-02 · CP-002 — la regla detiene el caso histórico y no reabre el presente**

**El problema que resuelve:** una puerta que no habría detenido el caso que la originó es decorativa; una que castigue hacia atrás reabre trabajo cerrado.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar el molde canónico de [`F26`](../../../../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) | Una exigencia, ejemplo, dependencias, excepción completa, checklist CUMPLE | Todo presente. `validar.py metareglas` no la nombra (el primer borrador midió 401 caracteres contra 320 del molde y se acortó **antes** de sellar el checklist) |
| 2 | Comprobar fila e índice en el capítulo `02` | Están | La fila de `F26` está tras la de `F25` en [`base.md`](../../../../../base/02-flujo-de-trabajo/base.md) |
| 3 | Aplicarla al caso del 2026-08-15 | La regla lo detiene | Lo detiene: el planteamiento asumido no tenía inventario aprobado por el usuario, así que las tres épicas no se habrían derivado; la corrección habría llegado en la aprobación, no con 21 historias escritas |
| 4 | Aplicarla al mismo proyecto hoy | No exige rehacer nada | Su excepción lo dice explícito: épicas ya derivadas al adoptar no se reabren; el inventario que ya escribieron queda esperando la aprobación, que su propio encabezado declara («BORRADOR · en revisión del usuario») |
| 5 | Comprobar el registro con las tres preguntas de `M19` | Está y concluye sin validador todavía | Está en [`reglas-validables.md`](../../../../../validadores/reglas-validables.md): la regla es de hoy (no se ha cumplido a mano ni una vez), el incumplimiento medido fue por regla inexistente, y automatizar sin formato fijo de la cita ítem→épica daría falsas alarmas. Primero que sirva a mano — `M19` estrena aplicándose |

**Cómo se verificó que la pareja cumple:** los pasos 3 y 4 son el oráculo histórico en sus dos direcciones (detiene lo que debía, no reabre lo cerrado); el 1 y el 2 aseguran que la regla nació por el procedimiento; el 5 deja respondida la pregunta que `M19` exige antes de que alguien proponga el validador. Evidencia EV-02.

---

**CA-03 · CP-003 — el veredicto de conducta, con citas**

**El problema que resuelve:** sin el veredicto escrito, la próxima sesión vuelve a preguntarse si la conducta ya cubría esto, y la respuesta se paga otra vez.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Aplicar cada regla del `01` al caso | Un veredicto por regla, con cita | **`C4` (no decidas por tu cuenta):** lo roza — asumir el techo fue decidir — pero no dice qué hacer al armar una propuesta; prohíbe sin dar la conducta. **`C7` (ante dos lecturas, pregunta):** no aplica: el pedido no tenía dos lecturas; tenía una, y el agente le agregó un techo. **`C17` (reformula ante dos lecturas):** no aplica, por lo mismo. **`C21` (pide el dato que falte):** no aplica: los cuatro campos del pedido estaban; el techo del alcance no es ninguno de los cuatro |
| 2 | Concluir si hay brecha que `F26` no cierre | La conclusión escrita | Había brecha (ninguna conducta detenía el caso) y **`F26` la cierra en la estación correcta**: la puerta obliga a que el alcance lo confirme el usuario en un documento, que es más fuerte que una conducta de «pregunta antes» — la pregunta queda escrita, con estados y respuesta registrada. No se propone extensión del `01`: sería la misma exigencia dicha dos veces (`20·M12`) |

**Cómo se verificó que la pareja cumple:** el veredicto está escrito acá con las cuatro citas y la conclusión dice con qué se cierra la brecha. Es el entregable del CA, no un paso hacia otra cosa. Evidencia EV-03.

---

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | [CA-01](../HU-011-el-inventario-de-funcionalidades.md#ca-01--el-molde-del-inventario-existe-y-nace-para-madurar-hasta-manual) | Crítica | 2026-08-21 | El molde contra el inventario real de `shopnest-mesa` en las dos direcciones; `grep` de dominio en 0; enlaces y marcas en verde | Aprobado | EV-01 | — |
| CP-002 | [CA-02](../HU-011-el-inventario-de-funcionalidades.md#ca-02--sin-inventario-aprobado-no-se-derivan-épicas) | Crítica | 2026-08-21 | `F26` contra el caso del 2026-08-15 (lo detiene) y el estado presente (no reabre); checklist CUMPLE; registro `M19` | Aprobado | EV-02 | — |
| CP-003 | [CA-03](../HU-011-el-inventario-de-funcionalidades.md#ca-03--queda-escrito-si-la-conducta-existente-cubría-preguntar-el-alcance) | Alta | 2026-08-21 | `C4`/`C7`/`C17`/`C21` releídas contra el caso; conclusión: brecha real, cerrada por `F26`, sin extensión del `01` | Aprobado | EV-03 | — |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el paso 7 de CP-001 (el programa citado no valida moldes; corrió el equivalente) y el paso 1 de CP-002 registra que el cuerpo de `F26` se acortó de 401 a menos de 320 caracteres antes de sellar. Ninguno toca el veredicto.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La comparación bidireccional molde↔semilla | Lectura lado a lado | Un solo faltante del semilla (cuenta por grupo), anotado para el aviso |
| 2 | La aplicación de `F26` a los dos momentos del caso | Juicio documentado en CP-002 | Detiene el histórico, no reabre el presente |
| 3 | Que la lectura de `shopnest-mesa` fue solo eso | Ningún archivo de aquel proyecto se editó | Confirmado |

---

## 4. Defectos encontrados

Ninguno.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-011-el-inventario-de-funcionalidades.md#ca-01--el-molde-del-inventario-existe-y-nace-para-madurar-hasta-manual) | CP-001 | Molde completo, agnóstico y nacido para madurar hasta manual | Sí |
| [CA-02](../HU-011-el-inventario-de-funcionalidades.md#ca-02--sin-inventario-aprobado-no-se-derivan-épicas) | CP-002 | `F26` publicada con checklist CUMPLE; detiene el caso histórico y no reabre el presente | Sí |
| [CA-03](../HU-011-el-inventario-de-funcionalidades.md#ca-03--queda-escrito-si-la-conducta-existente-cubría-preguntar-el-alcance) | CP-003 | Veredicto escrito con las cuatro citas; brecha cerrada por `F26`, sin extensión del `01` | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12 | 100% (3 de 3) | 3 de 3 | Sí |
| Casos ejecutados | Plan §12 | 100% | 3 de 3 | Sí |
| Tasa de aprobación | Plan §12 | 100% | 3 de 3 | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres CA en «Sí» (§5): el molde pide lo que el caso real necesitó, la regla habría evitado el caso que la originó sin castigar hacia atrás, y el veredicto de conducta deja la pregunta contestada por escrito. Los dos desvíos de ejecución quedaron declarados y no tocan lo exigido.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El molde y sus comprobaciones | [`plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`](../../../../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md); salida del `grep` (0) y de `validar.py estandar` en la sesión del 2026-08-21 |
| EV-02 | La regla, su checklist y su registro | [`F26`](../../../../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) · [`base.md` del 02](../../../../../base/02-flujo-de-trabajo/base.md) · [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) |
| EV-03 | El veredicto de conducta | El bloque CP-003 de este documento, §2 |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-21 | 3 | 0 | Primera ejecución |
