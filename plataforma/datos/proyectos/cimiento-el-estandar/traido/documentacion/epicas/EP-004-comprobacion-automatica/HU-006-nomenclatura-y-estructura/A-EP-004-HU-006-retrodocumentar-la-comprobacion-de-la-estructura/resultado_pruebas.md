# Resultado de pruebas — Fase A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura` |
| **HU** | [HU-006](../HU-006-nomenclatura-y-estructura.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-004-HU-006 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Árboles de mentira en carpetas temporales, y este repositorio para la línea base. Estándar 23.2.1 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). Los tres criterios se comprueban y los tres se probaron, incluido el que faltaba: que la fase incompleta **diga cuáles** documentos le faltan. Los dos transversales también pasan.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Nombres de fase mal armados y con complemento válido | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-02 | Alta | Una HU con fases `A` y `C`, y otra con `A` y `B` | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-03 | Alta | Una fase con solo su `plan_trabajo.md` | Aprobado | EV-01 |

---

### Detalle de CP-001 — El identificador fuera de convención se reporta

Ya estaba cubierto por la clase `Fases`, y se comprobó que sigue en pie:

| Qué se probó | Qué salió |
|---|---|
| Un nombre que no sigue `<LETRA>-EP-<n>-HU-<n>-<descripción>` | **Falla**, con su archivo |
| Un nombre con complemento válido | **No se reporta** |
| El ancho de los números (`EP-1` contra `EP-001`) | **No importa**: los dos valen |
| Una fase guardada bajo la HU equivocada | **Falla** |

**El tercero es el que evita el falso positivo**, que es lo que hace que un validador se termine ignorando.

---

### Detalle de CP-002 — El hueco en la numeración se reporta

| Qué se probó | Qué salió |
|---|---|
| Una HU con fases `A` y `C` | **Aviso** del hueco |
| Una HU con fases `A` y `B` | **No se reporta** |
| Dos fases de la misma HU con la misma letra | **Falla** |

**El hueco es aviso y la repetición es falla**, y la diferencia tiene sentido: un hueco puede ser una fase que se descartó, y dos fases con la misma letra es una ambigüedad que no se puede resolver leyendo.

---

### Detalle de CP-003 — La fase sin sus documentos se reporta diciendo qué le falta

**Este era el caso que faltaba.** Se armó una fase con **solo** su `plan_trabajo.md`:

| # | Qué se comprobó | Qué salió |
|---|---|---|
| 1 | Que se reporte | Se reporta, un solo hallazgo |
| 2 | Que **nombre los cuatro** que faltan | Los nombra: `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md`, `funcionalidad_implementada.md` |
| 3 | Que **no** nombre el que sí está | No nombra `plan_trabajo.md` |
| 4 | Que una fase con los cinco no se reporte | No se reporta |

**El paso 3 es el que separa un hallazgo útil de una lista genérica.** Decir «faltan documentos» obliga a abrir la carpeta y comparar; decir cuáles cuatro alcanza para arreglar sin abrirla — que es el CA-01 de [HU-003](../../HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md), aplicado acá.

---

## 3. La línea base, y por qué cambió mientras se medía

**El plan pedía anotar los 54 avisos de hoy como línea base** (`T-04`). Al ejecutar, ya no eran 54:

| Momento | Avisos de `validar.py fases` |
|---|---|
| Cuando se escribió el plan, el 2026-08-17 | **54** |
| Al empezar a ejecutar las fases del pendiente 48 | **53** |
| Al cerrar esta fase, el mismo día | **45** |

**Los 45 son todos del mismo tipo:** «faltan documentos de la fase (`F12.13`)». Ninguno es de nomenclatura, ninguno de consecutivo, ninguno de estructura. **Cero fallas.**

**Bajaron nueve porque nueve fases se ejecutaron esta sesión** y estrenaron sus dos documentos que faltaban. Es decir: **el número no es una línea base estable, es un contador de trabajo pendiente**, y cada fase que cierra lo baja en uno. Queda anotado así, con su fecha, en vez de como una cifra fija que envejecería mal.

---

## 4. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Cuántos avisos y de qué tipo | Corriendo `fases` sobre este repositorio y agrupando | **45, todos de documentos faltantes. 0 fallas** |
| 2 | Que lo ya cerrado siga pasando | Buscando hallazgos sobre tres fases cerradas | **Ninguno** |
| 3 | Que los bordes no revienten | Épica sin HU, HU sin fases, carpeta vacía y árbol sin `epicas/` | Ninguno revienta; el árbol vacío da falla, los otros avisan |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 281 pruebas · verde, con 5 fallos esperados |

---

## 5. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | **Qué parte de `F12` se comprueba y qué parte no estaba repartido entre el código y las pruebas**, y en ningún documento | **Corregido en esta fase**: escrito en [`validadores/docs/fases.md`](../../../../../validadores/docs/fases.md), que §2.1 del plan declara |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

**Ninguno deja un criterio de aceptación en «No».**

---

## 6. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-006-nomenclatura-y-estructura.md#ca-01--un-identificador-fuera-de-convención-se-reporta) | CP-001 | El nombre mal armado y la fase bajo la HU equivocada dan falla; el complemento válido y el ancho de los números, no | Sí |
| [CA-02](../HU-006-nomenclatura-y-estructura.md#ca-02--un-hueco-en-la-numeración-se-reporta) | CP-002 | El hueco avisa, la letra repetida falla, y el consecutivo contiguo no se reporta | Sí |
| [CA-03](../HU-006-nomenclatura-y-estructura.md#ca-03--una-fase-sin-sus-documentos-se-reporta) | CP-003 | Se reporta y **nombra los cuatro** que faltan, sin nombrar el que está | Sí |
| Transversal · Límites | Prueba propia, fuera del plan | Épica sin HU y HU sin fases **avisan**; el árbol sin `documentacion/epicas/` **falla**; ninguno revienta | Sí |
| Transversal · No regresión | Verificación 2 | Tres fases ya cerradas siguen sin producir ningún hallazgo | Sí |

**Los que no cumplen:** ninguno.

---

## 6.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 3 de 3 | 3 de 3 | Sí |
| Avisos de línea base anotados | Los 54, con su fecha | Anotados **45**, con su fecha y con el motivo del cambio | Sí |
| Fallas de estructura en este repositorio | 0 | **0** | Sí |
| Fases cerradas que empiecen a reportarse | 0 | **0** | Sí |

**Lo que no se cumplió:** ninguna meta. La de la línea base se cumplió con un número distinto del que el plan esperaba, y el porqué está escrito: bajó mientras se medía, porque las fases que se ejecutaron esta sesión estrenaron sus documentos.

---

## 7. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los tres criterios de aceptación quedaron verificados, incluido el que no tenía caso —que la fase incompleta diga **cuáles** documentos le faltan, y no solo que le faltan—. Los dos transversales que el plan no cubrió también pasan: los tres bordes tienen comportamiento definido y ninguna fase cerrada empezó a reportarse. Y quedó escrito, por primera vez, **qué parte de `F12` comprueba el programa y qué parte no**, con el motivo de cada exclusión.

**Qué falta para que cumpla:** nada.

---

## 8. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clases `EstructuraYNomenclatura` (5 pruebas nuevas) y `Fases` (11, ya existentes) |
| EV-02 | Lo que se comprueba y lo que no | [`validadores/docs/fases.md`](../../../../../validadores/docs/fases.md), sección escrita en esta fase |
| EV-03 | Línea base | §3, con los tres momentos y su fecha |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 281 pruebas, verde, 5 fallos esperados |

---

## 9. Ciclos anteriores

Ninguno: es el primero.
