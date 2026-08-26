# Resultado de pruebas — Fase A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |
| **HU** | [HU-002](../HU-002-mostrar-antes-de-hacer.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-007-HU-002 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Proyectos temporales con git, instalados de verdad. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 3 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). **El modo que muestra existe y no toca nada** — eso quedó comprobado archivo por archivo. Lo que falla es el CA-02: la simulación dice que **no hay registro de versión que escribir**, y al aplicar lo escribe.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Alta | Una corrida real, anotada línea por línea | Aprobado | EV-02 | — |
| [CP-002](plan_pruebas.md) | CA-01 | Crítica | El instalador sin `--aplicar` | Aprobado | EV-01 | — |
| [CP-003](plan_pruebas.md) | CA-02 | Crítica | Lo anunciado contra lo que aparece al aplicar | **Falla** | EV-01 | D-01 |
| [CP-004](plan_pruebas.md) | CA-01 | Alta | El proyecto antes y después de simular | Aprobado | EV-01 | — |

---

### Detalle de CP-001 y CP-002 — Sí existe una forma de ver el plan sin ejecutarlo

**La hay, y es el comportamiento por omisión.** `python validadores/instalar.py <ruta>` **simula**; hay que agregar `--aplicar` para que escriba. Lo primero que imprime es `MODO SIMULACIÓN — no se modifica nada. Agrega --aplicar.`

**La bitácora de una corrida real sobre un proyecto vacío: 27 líneas**, todas prefijadas `(simulado)`, en este orden:

| Grupo | Qué anuncia |
|---|---|
| Estructura | crear `proyectos/`, `documentacion/`, `prompts/` |
| Control de versiones | agregar al `.gitignore`; escribir `.githooks/commit-msg` y `pre-commit`; apuntar `core.hooksPath` |
| Enganches | nueve líneas, una por enganche y momento |
| Histórico y memoria | crear los tres `README`/`memory.md` |
| Capa de proyecto | copiar `stack-instalacion.md`; crear `stack`, `dominio`, `mapeo-nombres`, `marco-normativo` |
| Cierre | crear `CLAUDE.md`; anotar el proyecto en el registro; la línea de versiones; «la comprobación final corre al aplicar» |

**Y no escribió nada.** Se listaron todos los archivos del proyecto antes y después de simular: **idénticos**. El CA-01 se cumple.

---

### Detalle de CP-003 — Lo que muestra **no** es todo lo que hace

Se comparó lo anunciado con lo que aparece al aplicar. Al aplicar nacen **13 archivos**, y **uno de ellos no estaba anunciado**:

> `documentacion/versiones/2026-08-17-23.3.0.md`

Y no es que se le olvidara nombrarlo: la simulación dice **lo contrario**.

> `(simulado) versiones: ni las plantillas ni la versión cambiaron, no hay actualización que registrar`

**Por qué pasa.** El registro de versión se decide comparando huellas. En simulación **todavía no se ha copiado nada**, así que la comparación no ve cambios y concluye que no hay nada que registrar. Al aplicar, los archivos ya están puestos cuando llega ese paso, la comparación sí ve cambios, y el registro se escribe.

**Por qué importa más de lo que parece.** El archivo que aparece sin anunciarse es justamente **el que deja constancia de qué se instaló**. Quien lea la simulación para decidir si autoriza no verá que se va a escribir un documento nuevo en `documentacion/`, que es una carpeta del proyecto, no del estándar.

Es el defecto `D-01`, y deja el CA-02 en «No».

---

### Detalle de CP-004 — Cancelar en la autorización no deja nada escrito

**No hay un paso de autorización interactivo: hay dos órdenes distintas.** «Cancelar» equivale a no escribir `--aplicar`, y eso no deja nada — comprobado archivo por archivo en CP-002.

**Es mejor que un aviso interactivo**, y conviene dejarlo dicho: un mensaje de «¿seguro?» se contesta que sí sin leerlo. Dos órdenes distintas obligan a escribir algo distinto para que pase algo.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que simular no escriba | Listando todos los archivos antes y después | **Idénticos** |
| 2 | Cuántas líneas anuncia y cuántos archivos crea | Contando | **27 anunciadas · 13 archivos creados** |
| 3 | Cuál aparece sin anunciarse | Comparando los dos conjuntos | **1**: el registro de versión |
| 4 | Que un proyecto al día muestre lista vacía | Simulando después de instalar | Ninguna línea de «crear» |
| 5 | Que la suite siga verde | `python validadores/pruebas.py` | 328 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | **La simulación dice que no hay registro de versión que escribir, y al aplicar lo escribe.** Un archivo aparece en el proyecto sin haber sido anunciado, y es justo el que deja constancia de qué se instaló | Probado con fallo esperado en [`validadores/pruebas.py`](../../../../../validadores/pruebas.py). El arreglo toca `instalar.py`, que §2.1 del [plan aprobado](plan_trabajo.md) **no declara** ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Se propone |
| D-02 | Baja | Una línea del plan es la orden literal de git —`git config core.hooksPath .githooks`—: se entiende sin conocer el instalador, pero sí hay que conocer git | Anotado. No deja ningún CA en «No» |
| D-03 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual, y por eso apareció `D-02` | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-002-mostrar-antes-de-hacer.md#ca-01--el-modo-que-muestra-no-toca-nada) | CP-001, CP-002, CP-004 | Simular **no escribe ni un archivo**, y lo dice en su primera línea | Sí |
| [CA-02](../HU-002-mostrar-antes-de-hacer.md#ca-02--lo-que-muestra-es-lo-que-hace) | CP-003 | 12 de 13 archivos anunciados. **El registro de versión aparece sin anunciarse, y la simulación afirma lo contrario** | **No** |
| Transversal · Límites | Verificación 4 | Un proyecto al día no anuncia trabajo, y lo dice | Sí |
| Transversal · Claridad | Prueba propia, fuera del plan | Cada línea dice qué se va a hacer y sobre qué, no solo una ruta. La de `git config` es la única que pide saber de git (`D-02`) | Sí |

**El que no cumple:** el **CA-02**. Se traslada a una fase `B-EP-007-HU-002`.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Archivos escritos en modo simulación | **0** | **0** | Sí |
| Archivos que aparecen sin anunciarse | **0** | **1** | **No** |
| Bitácora de la corrida | Anotada paso por paso | 27 líneas, agrupadas | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el CA-01 quedó verificado a fondo: la simulación es el comportamiento por omisión, lo anuncia en su primera línea, y **no escribe ni un archivo** — comprobado listando el proyecto entero antes y después. El CA-02 no: de los 13 archivos que aparecen al aplicar, uno no estaba anunciado, y la simulación **afirma explícitamente que no hay nada que registrar** justo sobre ese archivo. Mostrar mal es peor que no mostrar, porque quien lee decide creyendo que ya vio todo.

**Qué falta para que cumpla:** que la decisión del registro de versión no dependa de un estado que la simulación todavía no tiene (`D-01`). Toca `instalar.py`, que el plan aprobado no declara: **pide una fase `B-EP-007-HU-002`**.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `MostrarAntesDeHacer`: 4 pruebas — 3 en verde y 1 como fallo esperado, que es `D-01` |
| EV-02 | Bitácora de la corrida | §2, las 27 líneas agrupadas |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 328 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
