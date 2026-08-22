# Plan de Pruebas — Fase A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-011 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-011` · [HU-011](../HU-011-el-inventario-de-funcionalidades.md), `CA-01` a `CA-03` |
| **Fecha** | 2026-08-21 |
| **Elaborado por** | El agente, por orden del usuario |
| **Aprobado por** | Pendiente — el usuario |
| **Estado** | Borrador |

> Formato proporcional a una sola fase: secciones 3, 5, 6, 9 y 12.

---

## 3. Estrategia de pruebas

Aceptación sobre documentos, con dos oráculos que ya existen: el **caso semilla** de `shopnest-mesa` (lo que el usuario aprobó con sus palabras) para el molde, y el **caso histórico** del mismo proyecto (el alcance asumido del 2026-08-15, corregido el 21) para la regla: una puerta que no detiene ese caso no sirve, y una que obligue a rehacer lo ya escrito se pasó de la raya. El veredicto de conducta se juzga releyendo las cuatro reglas del `01` contra el mismo caso.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| [HU-011](../HU-011-el-inventario-de-funcionalidades.md) | [CA-01](../HU-011-el-inventario-de-funcionalidades.md#ca-01--el-molde-del-inventario-existe-y-nace-para-madurar-hasta-manual) | [CP-001](#cp-001--el-molde-contra-el-semilla-en-las-dos-direcciones) | Aceptación | Crítica | Parcial (`validar.py plantilla`) | ☐ |
| [HU-011](../HU-011-el-inventario-de-funcionalidades.md) | [CA-02](../HU-011-el-inventario-de-funcionalidades.md#ca-02--sin-inventario-aprobado-no-se-derivan-épicas) | [CP-002](#cp-002--la-regla-detiene-el-caso-histórico-y-no-reabre-el-presente) | Aceptación | Crítica | Parcial (checklist y enlaces) | ☐ |
| [HU-011](../HU-011-el-inventario-de-funcionalidades.md) | [CA-03](../HU-011-el-inventario-de-funcionalidades.md#ca-03--queda-escrito-si-la-conducta-existente-cubría-preguntar-el-alcance) | [CP-003](#cp-003--el-veredicto-de-conducta-con-citas) | Análisis | Alta | No | ☐ |

**Cobertura:** 3 de 3 exigencias = 100%. Los RNF (legibilidad, neutralidad) se juzgan dentro de CP-001 y CP-002.

---

## 6. Casos de prueba

### CP-001 — El molde contra el semilla, en las dos direcciones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-01 |
| **Tipo** | Aceptación — contenido |
| **Prioridad** | Crítica |
| **Precondiciones** | `plantillas/inventario-funcionalidades.md` escrito (T-01) |
| **Datos de entrada** | El inventario de `shopnest-mesa` (`propuesta-desarrollo/inventario-funcionalidades.md`, solo lectura) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el molde y buscar los cuatro estados por ítem | Existe / Parcial / Por construir / Por confirmar, con «por confirmar» declarado como pregunta |
| 2 | Buscar la sección de lo que el usuario ya definió y la marca de preguntas abiertas | Las dos están, con su instrucción de uso |
| 3 | Leer la caja del molde | Dice que acompaña a la propuesta y que madura hasta ser el manual, escrito para quien usa el producto |
| 4 | Dirección semilla→molde: lo que el semilla tiene, el molde lo pide | Nada del semilla queda sin sitio en el molde |
| 5 | Dirección molde→semilla: lo que el molde pide y el semilla no tiene | Queda anotado para el aviso de cierre (es la comprobación que el pendiente fija) |
| 6 | Buscar dominio del semilla en el molde (ITIL, MAGERIT, prácticas, sus EP/HU) | Cero: el molde es agnóstico (`20·M3`) |
| 7 | Correr `validar.py plantilla` | En verde para el molde nuevo |

**Resultado esperado final:** el molde pide todo lo que el caso real necesitó, sin arrastrar su dominio.

---

### CP-002 — La regla detiene el caso histórico y no reabre el presente

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-02 |
| **Tipo** | Aceptación — la puerta |
| **Prioridad** | Crítica |
| **Precondiciones** | `F26` escrita con su checklist (T-03) |
| **Datos de entrada** | El caso histórico de `shopnest-mesa` como quedó documentado en el pendiente 74, y su estado presente |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que `F26` cumple el molde canónico: una exigencia, ejemplo INCORRECTO/CORRECTO, dependencias declaradas, checklist CUMPLE | Todo presente y sellado |
| 2 | Comprobar la fila y la sección de `F26` en el índice del capítulo `02` | Las dos están |
| 3 | Aplicar `F26` al caso del 2026-08-15: planteamiento asumido, tres épicas derivadas sin inventario aprobado | La regla lo detiene: sin inventario aprobado por el usuario, las épicas no se derivan |
| 4 | Aplicar `F26` al mismo proyecto hoy: inventario escrito, en revisión del usuario | No exige rehacer nada; la puerta queda esperando la aprobación, que el documento ya declara |
| 5 | Comprobar el registro en `reglas-validables.md` con las tres preguntas de `M19` respondidas | Está, y concluye: sin validador todavía — la regla primero demuestra servir a mano |

**Resultado esperado final:** la puerta existe, habría evitado el caso que la originó y no castiga hacia atrás.

---

### CP-003 — El veredicto de conducta, con citas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-03 |
| **Tipo** | Análisis |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna: las cuatro reglas del `01` ya existen |
| **Datos de entrada** | `C4`, `C7`, `C17`, `C21` y el caso: el usuario pidió la propuesta; el agente asumió el techo del alcance |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aplicar cada una de las cuatro al caso y escribir, con cita, si lo habría detenido | Un veredicto por regla, con el porqué |
| 2 | Concluir: ¿hay brecha de conducta que `F26` no cierre? | La conclusión escrita; si hay brecha, dice con qué se cierra (extensión propuesta aparte, `02·F20`, no legislada acá) |

**Resultado esperado final:** la próxima vez que alguien pregunte «¿esto ya lo cubría la conducta?», la respuesta está escrita, con citas.

---

## 9. Gestión de defectos

Un caso que no dé lo esperado se registra en el `resultado_pruebas.md` §4; la fase no cierra con defecto crítico o alto abierto. Si `F26` no detiene el caso histórico, la regla está mal redactada y **se corrige antes de sellarla** (todavía es el entregable de esta fase); si ya estaba sellada, el checklist se anula y se reaplica.

---

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | CA con caso / CA totales | 100% (3 de 3) |
| Casos ejecutados | Ejecutados / diseñados | 100% (3 de 3) |
| Tasa de aprobación | Aprobados / ejecutados | 100% |

El resultado vive en el `resultado_pruebas.md` de la fase.
