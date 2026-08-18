# Resultado de pruebas — Fase A-EP-002-HU-001-retrodocumentar-el-numero-de-version

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |
| **HU** | [HU-001](../HU-001-numero-de-version-y-que-significa.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-002-HU-001 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Este repositorio: `VERSION` y las **73 entradas** del registro. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 4 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). El número existe, sale de un solo archivo, y las 73 entradas del registro declaran su tipo. Lo que falla es CP-005: **`15.4.0` aparece dos veces**, con fechas y contenidos distintos.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | `VERSION` y `version.version_estandar()` | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-01 | Alta | El registro contra el archivo | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-02 | Alta | Tres entradas MAYOR | Aprobado | EV-02 |
| [CP-004](plan_pruebas.md) | CA-03 | Alta | Tres entradas PARCHE | Aprobado | EV-02 |
| [CP-005](plan_pruebas.md) | CA-01 | Crítica | Las 73 entradas, una tras otra | **Falla** | EV-01 |

---

### Detalle de CP-001 y CP-002 — El número existe y manda uno solo

| Qué se probó | Qué salió |
|---|---|
| `VERSION` trae tres partes | `23.3.0` |
| Es el que devuelve el programa | El mismo |
| Coincide con la primera entrada del registro | Coincide |

**Un solo lugar manda**, y eso se comprueba de la forma que importa: si el archivo y la cabeza del registro se separaran, habría **dos verdades** y un proyecto que declare su versión no sabría cuál adoptó.

---

### Detalle de CP-003 y CP-004 — Qué significa cada parte

**Las 73 entradas declaran su tipo** —MAYOR, MENOR o PARCHE—, salvo la `1.0.0`, que es la primera y no tiene nada anterior contra lo que compararse.

| Tres entradas MAYOR revisadas | ¿Obliga a un proyecto al día a hacer algo? |
|---|---|
| `23.0.0` · el histórico se escribe solo | Sí: el proyecto recibe enganches nuevos |
| `20.0.0` · decir lo mismo en menos palabras | Sí: es norma nueva de conducta |
| `6.0.0` · deroga `ID2` por `ID7` | Sí: hay que adoptar la derogación (`02·F22`) |

| Tres entradas PARCHE revisadas | ¿Cambió qué se exige? |
|---|---|
| `23.2.1` · el enganche prepara su salida | No: arregla un programa, no una regla |
| `23.1.1` · clasificar las reglas que faltaban | No: completa un registro |
| `21.2.1` · el instalador prepara su salida | No |

**Los dos criterios se cumplen**, y la distinción es la que hace útil el número: quien lee «subió a MAYOR» sabe que tiene trabajo, y quien lee PARCHE sabe que no.

---

### Detalle de CP-005 — Las tres partes avanzan sin saltos ni reinicios

Se recorrieron las 73 entradas de la más vieja a la más nueva, comprobando en cada salto que o sube la mayor y las otras van a cero, o sube la menor y el parche va a cero, o sube el parche. **Y que el número nunca baja.**

**Falla en un punto, y es un choque, no un salto:**

| Entrada | Fecha | Tipo | De qué trata |
|---|---|---|---|
| `## 15.4.0` | 2026-08-14 | MENOR | El enganche que sostenía el resumen no creaba el resumen |
| `## 15.4.0` | 2026-08-15 | MENOR | Una sección más en una plantilla |

**Dos cambios distintos comparten número.** La segunda tendría que haber sido `15.5.0`.

**Por qué importa, y no es cosmético.** Un proyecto declara qué versión adoptó, y el aviso de desfase compara ese número contra el del estándar. Con dos `15.4.0`, un proyecto que diga «adopté la 15.4.0» **no puede saber cuál de las dos tiene** — ni él ni el validador. Es exactamente el problema que el número existe para resolver.

Es el defecto `D-01`.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que `VERSION` y el registro coincidan | Comparándolos | Coinciden: `23.3.0` |
| 2 | Cuántas entradas hay | Contando en el registro | **73** |
| 3 | Cuántas no declaran tipo | Recorriéndolas | **1**, la `1.0.0`, y está bien |
| 4 | Números repetidos | Recorriendo los 73 saltos | **1**: `15.4.0`, dos veces |
| 5 | Que la suite siga verde | `python validadores/pruebas.py` | 357 pruebas · verde, con 7 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | **`15.4.0` aparece dos veces**, con fechas y contenidos distintos. Un proyecto que declare haberla adoptado no puede saber cuál de las dos tiene | Probado con fallo esperado en [`validadores/pruebas.py`](../../../../../validadores/pruebas.py). **No se corrige acá**: renumerar una versión ya publicada es decisión del usuario, y hay que revisar qué la cita antes de tocarla ([`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)) |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-001-numero-de-version-y-que-significa.md#ca-01--el-número-existe-y-se-lee-en-un-solo-lugar) | CP-001, CP-002, CP-005 | Tres partes, un solo archivo, coincide con el registro. **Pero un número está repetido** | **No** |
| [CA-02](../HU-001-numero-de-version-y-que-significa.md#ca-02--un-cambio-que-obliga-sube-la-parte-mayor) | CP-003 | Las tres entradas MAYOR revisadas obligan a hacer algo | Sí |
| [CA-03](../HU-001-numero-de-version-y-que-significa.md#ca-03--una-corrección-de-redacción-no-sube-la-parte-mayor) | CP-004 | Las tres PARCHE revisadas no cambian qué se exige | Sí |
| Transversal · Límites | CP-003 | Está escrito que cuando un cambio parece de dos tipos manda el más alto, y las entradas revisadas lo siguen | Sí |
| Transversal · No regresión | CP-005 | **El número nunca baja** en 73 entradas | Sí |

**El que no cumple:** el **CA-01**. «Se lee en un solo lugar» no se cumple mientras un número apunte a dos cosas.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 5 de 5 | 5 de 5 | Sí |
| Otros números de versión que manden | **0** | **0** | Sí |
| Saltos o reinicios en el registro | **0** | **0 saltos**, pero **1 número repetido** | **No** |
| Veces que el número baja | **0** | **0** | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el número existe, tiene tres partes, sale de un solo archivo y coincide con la cabeza del registro; las 73 entradas declaran su tipo salvo la primera, y las seis revisadas —tres MAYOR y tres PARCHE— hacen lo que su tipo promete. El número nunca baja.

Pero el CA-01 dice «se lee en **un solo lugar**», y hay un número que apunta a **dos**: `15.4.0` figura dos veces, con contenidos distintos. Un proyecto que declare haberla adoptado no puede saber cuál tiene, ni él ni el validador de desfase — que es justo lo que el número existe para resolver.

**Qué falta para que cumpla:** decidir qué se hace con la segunda `15.4.0`. **No lo decide el agente**: renumerar una versión publicada obliga a revisar qué la cita, y `20·M11` es explícito en que nada se renumera a la ligera.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `NumeroDeVersion`: 4 pruebas — 3 en verde y 1 como fallo esperado, que es `D-01` |
| EV-02 | Revisión de seis entradas | §2, las tablas de CP-003 y CP-004 |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 357 pruebas, verde, 7 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
