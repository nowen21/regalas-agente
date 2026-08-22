# Funcionalidad implementada — Fase «A-EP01-HU03-Descripción» (módulo «M»)   ·   `[CAPA 3]`

> Documento de **cierre de una fase** ([`02·F6`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md)/[`02·F7`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)). Consolida qué se implementó, la **trazabilidad especificación → código** ([`13·DOC11`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)), qué se probó y qué quedó. Se escribe en la estación de cierre, **antes del commit** de la fase. Se guarda en la carpeta de la fase (ruta `02·F12.13`, identificador `02·F12.6`), como `funcionalidad_implementada.md`. Reemplaza los `«…»` y borra esta caja.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `«A-EP01-HU03-Descripción»` |
| **Módulo** | «M» |
| **Especificación del módulo** | «enlace · [`02·F2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)» |
| **Plan de trabajo** | «enlace · `plan_trabajo.md`» |
| **HU / CA cubiertas** | HU-«NNN» (CA-01, CA-02) · HU-«NNN» (CA-01). Cada `CA-0N`, enlazado a su criterio en la HU |
| **Fecha de cierre** | AAAA-MM-DD |
| **Versión del estándar al cerrar** | «X.Y.Z», del archivo `VERSION` en el momento de cerrar |
| **Commit** | «hash — se completa al commitear» |

> **Para qué el sello de versión.** Dice **bajo qué reglas** se cerró este trabajo. Sin él, una regla nueva de mañana parece incumplida hoy, y hay que reabrir lo cerrado para averiguar si lo estaba: [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) dice que un cambio de norma **no reabre** lo cerrado, y este campo es lo que lo hace comprobable. Va solo en el cierre: al abrir la fase todavía no hay nada que sellar.

---

## 1. Qué se implementó — resumen

«2-4 líneas en lenguaje claro: qué quedó funcionando y para quién. Sin detalle de código.»

---

## 2. Trazabilidad  ·  [`13·DOC11`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

Dos trazabilidades, que responden preguntas distintas y **ninguna reemplaza a la otra**: la especificación dice **qué había que lograr**, el plan dice **qué se iba a hacer para lograrlo**. Una fase puede cumplir todos los criterios y haber dejado tareas del plan sin tocar, o haber tocado archivos que el plan no declaraba.

### 2.1 Especificación → implementación

> Una fila por **afirmación técnica del especificación**. No se cierra con faltantes sin justificar.
>
> **Estados:** ✅ implementado · ❌ pendiente (con destino explícito) · N/A (con motivo) · parcial (qué queda y a dónde va). Si aparece un faltante que **debía** estar en esta fase, se corrige in situ — no se difiere como N/A.

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| (frase literal o resumida) | esquema · modelo · servicio · vista · prueba · permiso · ruta · doc | `«ruta real»` | ✅ / ❌ / N/A / parcial | (prueba concreta o commit) |

**Faltantes / diferimientos** (si hay `❌` o parcial): «qué queda y a qué fase se traslada».

### 2.2 Plan de trabajo → ejecución

> **Aquí se verifica que se hizo lo que se dijo que se iba a hacer.** Una fila por **tarea del `plan_trabajo` §3**, copiada de allá con su identificador: el plan aprobado **no se modifica** para marcarle avances, igual que el `plan_pruebas`. Una tarea que esté acá y no en el plan, o al revés, se explica antes de cerrar.

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | (resumen de la tarea, tomado del plan) | ✅ hecha / ❌ no se hizo / parcial | `«ruta real»` | (commit, prueba, archivo) |

**Correspondencia con el plan:** «N tareas en el plan, N acá». Si no cuadra, cuáles bailan y por qué.

**Tareas que no se hicieron:** «cuáles, por qué, y a qué fase o pendiente se trasladan. "Ninguna" si se hicieron todas».

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `«ruta»` | | |

> "Ninguno" es la respuesta esperada. Si la lista trae algo, el plan se amplió sobre la marcha, y [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) pide pausar y pedir el visto bueno en vez de editar por iniciativa. Que quede escrito es lo que permite ver si eso pasa seguido y por qué.

**Esfuerzo real contra estimado:** «horas reales» contra «horas del plan». «Qué se subestimó, en una línea».

---

## 3. Qué se probó  ·  `08` / [`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

> **Se resume de acá, no se redacta:** el detalle vive en el `resultado_pruebas.md` de la fase. Si esta sección dice algo que aquel documento no respalda, manda aquel.

- **Fuente:** «`resultado_pruebas.md`» · **Veredicto:** «Cumple / Cumple con observaciones».
- **Suites ejecutadas + resultado:** «X/X verdes» (alcance quirúrgico — solo las suites que la fase toca).
- **Verificaciones manuales** — lo que el entorno automático **no** reproduce ([`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)):
  - «Lista de comprobaciones hechas a mano y su resultado.»
- **Defectos abiertos que se aceptaron:** «cuáles y quién los aceptó, o "ninguno"».

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada** (UI / endpoint / comando): «dónde y cómo se accede».
- **Permisos o datos base sembrados:** «si aplica».

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| | | «id / enlace en la memoria» |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino (fase futura / ticket / `pendientes/`) |
|---|---|---|
| | No previsto / Atajo decidido / Cambio del entorno / Diferido por el plan | |

**Los cuatro orígenes**, y qué dice cada uno:

| Origen | Qué pasó | Qué significa |
|---|---|---|
| **No previsto** | No se vio lo que se iba a romper, se descubrió a mitad y se parchó | La línea base de [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/base.md) se hizo floja. Es el único origen que un análisis mejor habría evitado |
| **Atajo decidido** | Se vio el camino correcto y se tomó el corto, por tiempo o por alcance | El análisis estuvo bien; la deuda se decidió. Debe decir **quién** la decidió |
| **Cambio del entorno** | Cambió la librería, el requerimiento o el cliente después de planear | Nadie lo pudo anticipar. No es defecto de nadie |
| **Diferido por el plan** | El propio [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) mandó dejarlo fuera de esta fase y así se declaró | La produjo el análisis, a propósito. Ya estaba en el fuera-de-alcance del plan |

> **Para qué sirve la columna.** Un análisis bueno no elimina la deuda: convierte la **descubierta** en **declarada**. Si fase tras fase el origen que se repite es *"no previsto"*, el problema no es la deuda, es que la línea base se está haciendo por encima.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

- [ ] Mapa de dependencias vivo actualizado ([`13·DOC9`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md)).
- [ ] Catálogo de módulos actualizado, si se creó o cambió un módulo ([`13·DOC13`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)).
- [ ] Índice `README.md` de la carpeta de docs actualizado ([`13·DOC15`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md)).
- [ ] Especificación del módulo actualizado con lo realmente implementado.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

Pasos **auto-suficientes y ejecutables** para producción (quien despliega lo hace leyendo esto, sin mirar el código):

- Cambios de esquema / migraciones a correr: «orden».
- Datos base / permisos a sembrar: «comandos».
- Comandos post-deploy: «si aplica».
- Reversión: «rollback previsto · ver §7 del `plan_trabajo`».
