# Resultado de pruebas — Fase A-EP-004-HU-018-el-numero-de-pendiente-libre

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-018-el-numero-de-pendiente-libre` |
| **HU** | [HU-018](../HU-018-numero-de-pendiente-ya-tomado.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-004-HU-018 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Carpetas de pendientes de mentira, y este repositorio. Estándar 23.3.0 |

**Esta fase construye:** nace [`validadores/pendientes.py`](../../../../../validadores/pendientes.py) y su subcomando.

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). Los tres criterios quedaron construidos y verificados. Y al construirlo apareció algo que la HU no preveía y que cambia la respuesta: **al cerrarse, un pendiente pierde su número**, así que la carpeta sola no sabe cuáles están tomados.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Carpetas con y sin huecos, y un cerrado sin número | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-02 | Crítica | Dos archivos con el mismo número, y con ceros a la izquierda | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-03 | Alta | Carpeta e índice descuadrados en los dos sentidos | Aprobado | EV-01 |

---

### Detalle de CP-001 — Dice cuál es el próximo número libre

| # | Qué se comprobó | Qué salió |
|---|---|---|
| 1 | Con `01`, `02` y `03`, el próximo es el 4 | **4** |
| 2 | Con `01` y `05`, **no** entrega el hueco | **6**, no 2 |
| 3 | Con un cerrado que perdió su número, ese número sigue tomado | **Sigue tomado** |
| 4 | Que la línea salga en la corrida de verdad | Sale, y termina en 0 |

**Por qué no se entrega el hueco.** El índice dice que «el número no se reutiliza ni se renumeran los demás: los huecos son historia», y los pendientes se citan entre sí por número — «hermano del 33», «el punto 2 del 53». Entregar un hueco haría que «el 02» apuntara a dos cosas distintas según cuándo se leyera.

---

### El hallazgo que cambió el diseño

**La primera versión leía solo la carpeta, y dijo que el próximo libre era el 02.** El 02 existió: era «vigencia y poda de la memoria», cerrado el 2026-08-06.

**Qué pasa al cerrar un pendiente:** su archivo se mueve a `hecho/` **y se renombra**, perdiendo el número. `02-vigencia-y-poda.md` pasa a `vigencia-y-poda-de-memoria.md`. Mirando los archivos, el 02 parece libre.

**Dónde sobrevive la numeración:** solo en el **índice**, en su fila tachada `| ~~02~~ |`. Por eso el programa lee **la carpeta y el índice juntos**.

| Medición, 2026-08-17 | Valor |
|---|---:|
| Pendientes con archivo | **39** |
| Números tomados de verdad | **54** |
| Números que existen **solo** en el índice | **15** |
| Próximo libre | **59** |

**Si esta fase hubiera cerrado con la primera versión**, el siguiente pendiente habría nacido con el número 02 y habría roto silenciosamente toda cita al 02 anterior — que es exactamente el daño que la HU viene a evitar. Lo destapó el caso del paso 3, que el plan de pruebas sí había escrito.

---

### Detalle de CP-002 — Avisa del número repetido

| Qué se probó | Qué salió |
|---|---|
| Dos abiertos con el número `07` | **Falla**, nombrando los dos archivos |
| Uno abierto y uno cerrado con `07` | **Falla** |
| `07-uno.md` y `7-otro.md` | **Falla** — los ceros a la izquierda no hacen dos números |
| Este repositorio | **Cero repetidos** |

**El tercero es el transversal de límites**, y es el que de verdad importa: tratar `07` y `7` como distintos dejaría pasar justo el choque que esta comprobación busca.

**Es falla y no aviso** porque no hay forma de resolverlo leyendo: los dos archivos existen, ninguno pisa al otro, y quien cite «el 07» no puede saber a cuál se refiere.

---

### Detalle de CP-003 — Cruza la carpeta con el índice

| Sentido | Qué se probó | Qué salió |
|---|---|---|
| Carpeta → índice | Un pendiente sin su línea | **Aviso**, con el archivo |
| Índice → carpeta | Una línea que enlaza un archivo que no está | **Aviso**, con el índice |

**En los dos sentidos, por lo mismo que en el índice de recuerdos:** con uno solo pasa la mitad de los errores. Y son **avisos**, no fallas: se arreglan editando un `.md` y no rompen nada mientras tanto.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Qué dice la corrida en este repositorio | `python validadores/validar.py pendientes` | Sin incumplimientos · **39 con archivo · 54 tomados · próximo el 59** |
| 2 | Que los cerrados pierdan el número | Listando `pendientes/hecho/` | **Los 17 sin número** |
| 3 | Que `validar.py estandar` siga igual | Corriéndolo antes y después | **0 fallas**, igual |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 314 pruebas · verde, con 5 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | **La carpeta sola no sabe qué números están tomados**, porque al cerrarse un pendiente pierde el suyo. Una comprobación que solo mirara los archivos entregaría números ya usados | **Corregido en esta misma fase**, antes de cerrarla: el programa lee la carpeta **y** el índice. Escrito en [`docs/pendientes.md`](../../../../../validadores/docs/pendientes.md) |
| D-02 | Media | `comun.leer` revienta con un archivo que no existe, así que no se pudo usar para leer el índice de una carpeta que aún no lo tiene | Esquivado dentro de `pendientes.py`, con su propia lectura y el motivo escrito. El arreglo de fondo es `D-01` de la fase [`A-EP-004-HU-003`](../../HU-003-formato-del-hallazgo/A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md) |
| D-03 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los tres transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

**Ninguno deja un criterio de aceptación en «No».**

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-018-numero-de-pendiente-ya-tomado.md#ca-01--dice-cuál-es-el-próximo-número-libre) | CP-001 | Dice el próximo libre, no entrega huecos, y cuenta los números que solo viven en el índice | Sí |
| [CA-02](../HU-018-numero-de-pendiente-ya-tomado.md#ca-02--avisa-del-número-repetido) | CP-002 | Falla con el repetido, entre abiertos, entre abierto y cerrado, y con ceros a la izquierda | Sí |
| [CA-03](../HU-018-numero-de-pendiente-ya-tomado.md#ca-03--cruza-la-carpeta-con-el-índice) | CP-003 | Los dos sentidos, como aviso | Sí |
| Transversal · Límites | CP-002, y pruebas propias | Carpeta vacía, archivo sin número y ceros a la izquierda: los tres definidos | Sí |
| Transversal · Errores | Prueba propia | El nombre que no se puede interpretar sale como **aviso** y la corrida sigue contando los demás | Sí |
| Transversal · No regresión | Verificación 3 | `validar.py estandar` da lo mismo que antes | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los tres transversales | Sí |
| Casos ejecutados | 3 de 3 | 3 de 3 | Sí |
| Números repetidos en este repositorio | 0, o listados | **0** | Sí |
| Lo que `estandar` reportaba, sin cambios | Igual | Igual: 0 fallas | Sí |
| Pruebas de la suite | Línea base + las nuevas, en verde | Línea base + **14**, en verde | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los tres criterios quedaron construidos y verificados, y los tres transversales que el plan no cubrió también. Lo que hace valiosa a esta fase no es el programa sino lo que descubrió al construirlo: **la carpeta de pendientes no es la fuente de la numeración**, porque cerrar un pendiente le quita el número. Quince de los cincuenta y cuatro números tomados existen solo en el índice, y una comprobación que no lo leyera habría entregado el 02 al siguiente pendiente — rompiendo en silencio toda cita al 02 anterior, que es justo el daño que esta HU viene a evitar.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `NumeracionDePendientes`: 14 pruebas, en verde |
| EV-02 | Lo construido | [`validadores/pendientes.py`](../../../../../validadores/pendientes.py) y el subcomando `pendientes` de [`validar.py`](../../../../../validadores/validar.py) |
| EV-03 | Lo escrito | [`validadores/docs/pendientes.md`](../../../../../validadores/docs/pendientes.md) |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 314 pruebas, verde, 5 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
