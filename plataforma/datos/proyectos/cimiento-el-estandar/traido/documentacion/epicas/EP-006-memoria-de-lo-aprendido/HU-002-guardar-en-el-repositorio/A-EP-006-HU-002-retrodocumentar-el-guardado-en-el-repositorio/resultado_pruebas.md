# Resultado de pruebas — Fase A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |
| **HU** | [HU-002](../HU-002-guardar-en-el-repositorio.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-006-HU-002 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario ese mismo día |
| **Ambiente y versión** | Este repositorio, en lectura, y carpetas temporales. Estándar 23.2.1 · Python 3.11.9 · git |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 3 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). Los **18 recuerdos** viven en el repositorio, se ven en el historial línea por línea y su índice cuadra en los dos sentidos. Lo que no cumple el CA-01 son las **237 señales**: `memoria/senales.db` **no está versionada** —está en `.gitignore` a propósito— y no tiene ningún historial.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-recuerdo-nuevo-se-ve-como-texto-en-el-historial) | CA-01 | Alta | 2026-08-17 | El historial real de `historico-chat/memory/respuestas-cortas.md` | Aprobado | EV-02 | — |
| [CP-002](plan_pruebas.md#cp-002--qué-se-puede-leer-del-historial-de-la-base-de-señales) | CA-01 | Alta | 2026-08-17 | El historial de `memoria/senales.db` | **Falla** | EV-02 | D-01 |
| [CP-003](plan_pruebas.md#cp-003--la-carpeta-y-el-índice-coinciden-en-los-dos-sentidos) | CA-02 | Crítica | 2026-08-17 | Los 18 recuerdos de esta casa, contra su índice | Aprobado | EV-01 | — |
| [CP-004](plan_pruebas.md#cp-004--por-el-índice-se-llega-al-recuerdo-sin-abrir-los-otros) | CA-02 | Alta | 2026-08-17 | El índice `memory.md`, buscando cuatro temas | Aprobado | EV-01 | — |

---

### Detalle de CP-001 — El recuerdo nuevo se ve como texto en el historial

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribir el recuerdo | Queda como archivo de texto | Queda: 18 archivos `.md` en `historico-chat/memory/` |
| 2 | Mirar el historial | Se ve qué se agregó, línea por línea | Se ve. Tres commits en `respuestas-cortas.md`, con fecha y autor |
| 3 | Cambiar una línea y mirar | El historial muestra exactamente qué cambió | Lo muestra: el último cambio es **un párrafo agregado**, con su `+` y el contexto de las líneas de al lado |
| 4 | Comprobar que se revisa sin herramientas extra | Se puede | `git log -p` y nada más. Es texto plano |

---

### Detalle de CP-002 — Qué se puede leer del historial de la base de señales

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Guardar una señal en la copia | La base cambia | Cambia |
| 2 | Mirar el historial de ese cambio | Se anota qué se ve | **No se ve nada. No hay historial**: `git log -- memoria/senales.db` devuelve **cero commits** |
| 3 | Responder «qué se aprendió ese día» con solo el historial | Se anota si se puede | **No se puede.** El archivo no está versionado |
| 4 | Escribir el límite con lo medido | Queda escrito | Escrito acá |
| 5 | Proponer las salidas **sin decidir** | Queda como propuesta | Abajo |

**Lo medido, no lo supuesto.** El plan preveía el caso «el historial dice solo que el archivo cambió, porque es binario». Lo que hay es más fuerte: `.gitignore` línea 10 excluye `memoria/senales.db`, con el motivo escrito al lado — *«Datos locales de la memoria por señales (la base es del usuario, no del estándar)»*.

**No es un descuido: es una decisión tomada.** Y tiene sentido para un proyecto cualquiera, donde la base es del usuario. En **este** repositorio deja algo distinto: las 237 señales existen solo en esta máquina, sin historial, sin revisión y sin copia.

**Las salidas, sin decidir ninguna** (paso 5):

| Salida | Qué gana | Qué cuesta |
|---|---|---|
| **A · Exportar a texto junto a la base.** Un `senales.md` o un `.jsonl` versionado que se regenera al guardar | El historial vuelve: se ve qué señal entró y qué día, línea por línea. Y hay copia | Hay que mantener el export al día, y decidir si se versiona en cada proyecto o solo acá |
| **B · Declararlo como límite.** Escribir en la HU que el CA-01 aplica a los recuerdos y no a las señales | Cuesta cero, y deja de haber un CA que nadie va a cumplir | Las señales siguen sin historial ni copia — que es justo lo que la HU quería evitar |
| **C · Versionar la base tal cual**, quitándola del `.gitignore` | Historial y copia sin trabajo extra | El historial de un `.db` no se puede leer: diría «cambió» y nada más. Y en un proyecto cualquiera metería datos del usuario al repositorio |

**La decisión es del usuario.** La fase la deja planteada con lo que cuesta cada una, que es lo que su tarea T-03 pedía.

---

### Detalle de CP-003 — La carpeta y el índice coinciden en los dos sentidos

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los archivos de recuerdo | Sale un número, con su fecha | **18**, el 2026-08-17 |
| 2 | Comprobar que cada uno tiene su línea en el índice | Todos | **Los 18** |
| 3 | Comprobar que cada línea tiene su archivo | Todas | **Las 18** |
| 4 | Listar los que fallen en cualquier sentido | Se anotan | **Ninguno**, en ninguno de los dos sentidos |
| 5 | Corregir el índice si hiciera falta | Se corrige | **No hizo falta** |

> **Por qué se comprueba en los dos sentidos.** Con uno solo pasa la mitad de los errores: mirando solo que cada archivo tenga su línea, una línea que apunta a un archivo borrado sobrevive; mirando solo al revés, un recuerdo nuevo sin indexar tampoco se ve. La prueba automatizada hace las dos, y además comprueba que un índice **vacío** sea válido — un proyecto sin recuerdos todavía no está en falta.

---

### Detalle de CP-004 — Por el índice se llega al recuerdo sin abrir los otros

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Por cada tema, buscar en el índice cuál lo trata | Se llega a uno | Se llegó, en los cuatro temas probados: aprobar antes de commitear, decidir es del usuario, respuestas cortas, y no tocar el trabajo de otras sesiones |
| 2 | Contar cuántos archivos hubo que abrir | Uno | **Uno** en los cuatro |
| 3 | Comprobar que el índice dice **de qué trata**, no qué exige | Lo dice | Lo dice. Se comprobó además con una prueba automatizada: ninguna fila del índice se queda en el enlace pelado |
| 4 | Anotar el tema que no se pueda ubicar | Queda como hueco | **Ninguno** de los cuatro |

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Si `senales.db` está versionada | `git ls-files memoria/` y `git check-ignore -v` | **No lo está**, y está excluida a propósito |
| 2 | Que el historial de un recuerdo se lea | `git log -p` sobre un archivo real | Se lee, con el párrafo agregado y su contexto |
| 3 | Cuántos recuerdos hay y si cuadran con el índice | Contando la carpeta y el índice | 18 y 18, sin sobrantes ni faltantes |
| 4 | Que la suite entera siga verde | `python validadores/pruebas.py` | 260 pruebas · verde, con 2 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | Las **237 señales no tienen historial**: `memoria/senales.db` está en `.gitignore`. El CA-01 pide que lo guardado viva en el repositorio y se vea en el historial, y de las dos mitades de la memoria solo una lo cumple | Medido acá, con las tres salidas planteadas y **ninguna decidida**: cambiar el `.gitignore` o el alcance del CA es del usuario |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales** de la HU. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-002-guardar-en-el-repositorio.md#ca-01--lo-guardado-vive-en-el-repositorio-y-se-ve-en-el-historial) | CP-001, CP-002 | Los **18 recuerdos** sí: texto plano, con fecha, autor y diferencia línea por línea. Las **237 señales**, no: sin versionar y sin historial | **No** |
| [CA-02](../HU-002-guardar-en-el-repositorio.md#ca-02--hay-un-índice-que-dice-de-qué-trata-cada-cosa) | CP-003, CP-004 | 18 de 18 en los dos sentidos, y por el índice se llega abriendo un solo archivo | Sí |
| Transversal · Privacidad | Prueba propia, fuera del plan | **0 hallazgos** al correr el detector de secretos (`04·S4`) sobre los 18 recuerdos. Se probó con el mismo programa que vigila el código, no a ojo: a ojo, un recuerdo nuevo con una clave pegada pasaría el día que nadie mire | Sí |
| Transversal · Límites | Prueba propia, fuera del plan | Un proyecto sin nada guardado tiene índice válido y vacío: se probó, y no es un error | Sí |

**Los que no cumplen:** el **CA-01**, en la mitad de las señales. No se corrige acá: las tres salidas están escritas en §2 y elegir es del usuario.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| Recuerdos sin línea en el índice | Plan §12 | **0** | **0** de 18 | Sí |
| Líneas del índice sin archivo | Plan §12 | **0** | **0** de 18 | Sí |
| Señales exportadas o movidas en esta fase | Plan §12 | **0** | **0** — la salida se propuso, no se ejecutó | Sí |
| Archivos que hubo que abrir para ubicar un tema | Plan §12 | 1 | **1**, en los cuatro temas | Sí |

**Lo que no se cumplió:** ninguna meta. Las seis en verde, y la fase no cumple — otra vez las métricas medían el índice de los recuerdos y lo que falla son las señales, que ninguna métrica miraba.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el CA-02 quedó verificado a fondo: 18 recuerdos, 18 líneas, cuadre en los dos sentidos, y por el índice se llega abriendo un solo archivo. El CA-01 se cumple para los recuerdos y **no para las señales**: `memoria/senales.db` está excluida del control de versiones, así que 237 señales no tienen historial, ni revisión, ni copia. Están solo en esta máquina.

**Qué falta para que cumpla:** que se elija una de las tres salidas de §2 —exportar a texto, declarar el límite en la HU, o versionar la base tal cual—. **Es decisión del usuario**, y la tarea T-03 del plan pedía exactamente proponerlas sin decidirlas.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `IndiceDeLosRecuerdos`: 5 pruebas, en verde |
| EV-02 | Lectura del historial real | §2 y §3: `git log -p` sobre un recuerdo, y `git ls-files`/`git check-ignore` sobre la base |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 260 pruebas, verde, 2 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
