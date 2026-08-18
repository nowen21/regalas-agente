# Resultado de pruebas — Fase A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase` |
| **HU** | [HU-017](../HU-017-inventario-de-hu-sin-fase.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-004-HU-017 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Árboles de mentira en carpetas temporales, y este repositorio para el cruce. Estándar 23.3.0 |

**Esta fase construye**, no retro-documenta: la línea del inventario no existía.

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). La corrida termina diciendo `HU: 68 en total · 25 completas · 43 incompletas`, y esos tres números **coinciden exactamente** con los que el pendiente 48 lleva a mano — cruce que además quedó como prueba permanente.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Un árbol con dos HU, una completa y otra no | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-02 | Crítica | Las carpetas reales de este repositorio | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-03 | Alta | Una HU con dos fases, con y sin un documento | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md) | CA-04 | Alta | Épica sin HU, carpeta HU sin su archivo, árbol vacío | Aprobado | EV-01 |

---

### Detalle de CP-001 — La línea dice el total, las completas y las incompletas

| # | Qué se comprobó | Qué salió |
|---|---|---|
| 1 | Con dos HU, una completa y otra no, la cuenta da 2, 1 y 1 | **(2, 1, 1)** |
| 2 | Que la línea traiga los tres números escritos | «2 en total · 1 completas · 1 incompletas» |
| 3 | Que la línea salga en la corrida de verdad | Sale, corriendo `validar.py fases` como orden del sistema |

**Dónde va la línea, y por qué ahí.** Al final, **después** de los hallazgos y **aunque no haya ninguno**. Es el resumen de cuánto falta, no un incumplimiento más — y cuando no hay hallazgos es justo cuando se quiere saber cuánto queda.

---

### Detalle de CP-002 — El total coincide con las carpetas que hay

Se contaron las carpetas `HU-` del árbol real **por fuera del programa**, recorriendo el sistema de archivos, y se comparó con lo que el programa dice.

| Fuente | Total de HU |
|---|---:|
| Contando carpetas a mano en la prueba | **68** |
| `fases.inventario()` | **68** |

**Y el cruce que de verdad importa:** el [pendiente 48](../../../../../pendientes/48-inventario-hu.md) lleva los mismos tres números a mano, casilla por casilla:

| | Programa | Pendiente 48 |
|---|---:|---:|
| Total | 68 | 68 |
| Completas | 25 | 25 |
| Incompletas | 43 | 43 |

**Los tres coinciden**, y quedó una prueba que los compara en cada corrida: si alguna vez se separan, una de las dos cuentas está mal y la suite lo dice. Es lo que convierte al inventario escrito de «una tabla que alguien mantiene» en «una tabla verificada».

---

### Detalle de CP-003 — La HU con dos fases cuenta completa solo si las dos lo están

| Qué se probó | Qué salió |
|---|---|
| Dos fases, las dos con sus cinco documentos | **(1, 1, 0)** — completa |
| Dos fases, una con cuatro documentos | **(1, 0, 1)** — incompleta |
| Una HU sin ninguna carpeta de fase | **(1, 0, 1)** — incompleta |

**Por qué «todas» y no «alguna».** Con dos fases y una a medias la historia no está terminada. Contarla completa escondería justo el trabajo que falta, que es lo único que este inventario viene a hacer visible. Y una HU sin ninguna fase incumple `F12.2` de entrada.

---

### Detalle de CP-004 — Los bordes

| Borde | Qué tenía que pasar | Qué salió |
|---|---|---|
| Épica **sin HU** | No rompe la cuenta | No aporta ninguna; el resto se cuenta igual |
| Carpeta `HU-` **sin su archivo `.md`** | Cuenta como incompleta | **(1, 0, 1)** |
| Árbol **vacío** | No revienta | `(0, 0, 0)` y **no imprime línea** |
| Carpetas que no son épica ni HU | No se cuentan | Una carpeta `notas/` y otra `borradores/` se ignoran |

**El segundo borde es una decisión, no un detalle.** Una carpeta `HU-` sin su documento existe **como trabajo** aunque le falte el papel. No contarla la volvería invisible — que es exactamente lo contrario de lo que este inventario hace. Se cuenta, y como incompleta.

**El tercero también.** Sin `documentacion/epicas/` el inventario calla en vez de fallar, porque quien reporta la falta de esa carpeta es `validar()`: dos hallazgos por lo mismo es ruido, y el ruido es lo que hace que se deje de leer.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que la línea salga por el camino real | `python validadores/validar.py fases` | `HU: 68 en total · 25 completas · 43 incompletas (F12.2)` |
| 2 | Que los avisos de antes sigan saliendo igual | Comparando la salida antes y después | **43 avisos, los mismos**, uno por uno |
| 3 | Que el cruce con el pendiente 48 dé | Comparando los tres números | Coinciden los tres |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 300 pruebas · verde, con 5 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

**Ninguno deja un criterio de aceptación en «No».**

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-017-inventario-de-hu-sin-fase.md#ca-01--la-corrida-dice-el-total-las-completas-y-las-incompletas) | CP-001 | La corrida termina con los tres números, y salen por el camino real | Sí |
| [CA-02](../HU-017-inventario-de-hu-sin-fase.md#ca-02--el-total-coincide-con-las-carpetas-que-hay) | CP-002 | 68 contadas a mano, 68 del programa, y los tres coinciden con el pendiente 48 | Sí |
| [CA-03](../HU-017-inventario-de-hu-sin-fase.md#ca-03--una-hu-con-dos-fases-cuenta-como-completa-solo-si-las-dos-lo-están) | CP-003 | Con una de las dos a medias, la HU cuenta incompleta | Sí |
| [CA-04](../HU-017-inventario-de-hu-sin-fase.md#ca-04-caso-borde-la-épica-sin-hu-y-la-carpeta-hu-sin-su-archivo) | CP-004 | Los dos bordes tienen comportamiento definido y escrito | Sí |
| Transversal · Límites | CP-004 | Árbol vacío, épica sin HU y HU sin archivo: los tres definidos, ninguno revienta | Sí |
| Transversal · No regresión | Verificación 2 | Los 43 avisos siguen saliendo uno por uno. `validar()` y el inventario son dos caminos separados sobre el mismo árbol | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Diferencia entre el total del programa y las carpetas | **0** | **0** | Sí |
| Avisos que dejaron de salir | **0** | **0** | Sí |
| Pruebas de la suite | Línea base + las nuevas, en verde | Línea base + **11**, en verde | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los cuatro criterios de aceptación quedaron construidos y verificados, y los dos transversales también. Lo que más valor tiene no es la línea en sí sino el cruce: **los tres números del programa coinciden con los tres que el pendiente 48 lleva a mano**, y esa comparación quedó como prueba permanente. El inventario escrito deja de ser una tabla que alguien mantiene y pasa a ser una tabla verificada — y el día que se separen, la suite lo dice antes que nadie.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `InventarioDeHU`: 11 pruebas, en verde |
| EV-02 | Lo construido | [`validadores/fases.py`](../../../../../validadores/fases.py) · `inventario()` y `linea_inventario()`; [`validadores/validar.py`](../../../../../validadores/validar.py) · `cmd_fases` |
| EV-03 | Lo escrito | [`validadores/docs/fases.md`](../../../../../validadores/docs/fases.md), sección «El inventario de HU» |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 300 pruebas, verde, 5 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
