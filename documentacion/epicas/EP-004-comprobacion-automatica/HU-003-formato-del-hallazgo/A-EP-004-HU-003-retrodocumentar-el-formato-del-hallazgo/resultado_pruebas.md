# Resultado de pruebas — Fase A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` |
| **HU** | [HU-003](../HU-003-formato-del-hallazgo.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-004-HU-003 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Este repositorio, con corridas reales de `validar.py`. Estándar 23.2.1 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). Los tres criterios numerados quedaron verificados —207 hallazgos con archivo y regla, los dos códigos de salida correctos, y dos defectos reales arreglados sin abrir ningún validador—. Lo que falla es el criterio **transversal de errores**: un `.md` que no se puede decodificar **tumba la corrida entera con un volcado de Python**.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--cada-hallazgo-de-la-corrida-trae-archivo-línea-y-regla) | CA-01 | Crítica | 207 hallazgos de `flujo`, `fases` y `trazabilidad` | Aprobado | EV-01 | — |
| [CP-002](plan_pruebas.md#cp-002--dos-defectos-se-arreglan-sin-abrir-el-programa) | CA-01 | Alta | Dos defectos reales de esta sesión | Aprobado | EV-02 | — |
| [CP-003](plan_pruebas.md#cp-003--con-solo-avisos-el-código-de-salida-es-0) | CA-02 | Crítica | `validar.py flujo`, con 151 avisos | Aprobado | EV-01 | — |
| [CP-004](plan_pruebas.md#cp-004--con-una-falla-el-código-de-salida-es-1-aunque-haya-avisos) | CA-03 | Crítica | Hallazgos armados, y la corrida real | Aprobado | EV-01 | — |

---

### Detalle de CP-001 — Cada hallazgo de la corrida trae archivo, línea y regla

**Se corrieron tres validadores sobre este repositorio y salieron 207 hallazgos.** De los tres se midió cada parte:

| Parte del hallazgo | De 207 | Lectura |
|---|---:|---|
| Con **archivo** | **207** | Ninguno sin él |
| Con **regla** nombrada en el mensaje | **207** | Ninguno sin ella |
| Con **línea** concreta | 122 | Los otros **85 son de archivo entero** |

**Los 85 sin línea no son un hueco: son la forma definida del hallazgo de archivo completo**, y es el criterio transversal de límites de la HU. «Al plan le faltan secciones de las 13 preguntas» no ocurre en una línea. La ficha guarda `linea = 0` y al imprimir se omite el número — no se inventa un 1, que mandaría a mirar donde el problema no está.

**La regla aparece en tres formas, y las tres cuentan:** sola —`(F18)`—, con varias —`(F4/F14)`— y con su porqué al lado —`(F2: sin especificación acordada no hay código)`—. La primera versión de la prueba solo aceptaba la primera forma y reprobó la tercera; **el que estaba mal era el patrón de la prueba, no el hallazgo**, y se corrigió la prueba.

---

### Detalle de CP-002 — Dos defectos se arreglan sin abrir el programa

**Los dos son reales y de esta misma sesión**, no armados para el caso. Aparecieron al correr `validar.py estandar` antes de empezar a ejecutar las fases:

| Defecto que reportó el validador | Qué hizo falta para arreglarlo | ¿Se abrió el programa? |
|---|---|---|
| `historico-chat/resumenes/2026-08-17/retrodocumentar-ep-001.md:126 — enlace roto: ../../2026-08-17-sesion-2.md` | Abrir ese archivo en esa línea y apuntar al nombre nuevo de la sesión renombrada | **No** |
| `pendientes/README.md — el índice no menciona pendientes/58-nada-hace-cumplir-id9.md` | Abrir el índice y agregarle su fila | **No** |

**Los dos traían archivo, línea cuando aplicaba, y qué se esperaba.** Ninguno obligó a abrir `enlaces.py` ni `estandar` para entender qué se pedía. **Cero veces hizo falta abrir el programa**, que era la métrica del plan.

> **De paso, la medición de fondo:** en esa misma tanda se arreglaron **cinco** defectos leyendo solo la salida del validador, y `validar.py estandar` pasó de 5 fallas a 0.

---

### Detalle de CP-003 y CP-004 — Los dos códigos de salida

| Caso | Qué se probó | Qué salió |
|---|---|---|
| Solo avisos | Dos hallazgos `AVISO` a `reportar` | **0** |
| Sin hallazgos | Lista vacía | **0** |
| Un aviso y una falla | Los dos a `reportar` | **1** — basta una falla |
| Corrida real, `validar.py flujo` | 151 avisos, ninguna falla | **0** |
| Corrida real, `validar.py estandar` | Sin fallas tras la limpieza | **0** |

**Se probó por los dos caminos:** llamando a `reportar` con hallazgos armados, y corriendo `validar.py` como orden del sistema. El segundo es el que importa, porque es el que usa quien trabaja: un código de salida correcto en la función y roto en el arranque no serviría de nada.

**Lo dudoso sale como aviso y no detiene** (CA-02): las 151 líneas de `flujo` son avisos, incluidas las que son falsos positivos conocidos, y la corrida termina en 0. Es la decisión de diseño que hace que el validador se pueda seguir usando: uno que reprueba por algo discutible se vuelve ruido, y lo que se ignora después no son solo sus avisos, también sus fallas.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Cuántos hallazgos y qué traen | Corriendo tres validadores y contando parte por parte | 207 · archivo 207 · regla 207 · línea 122 |
| 2 | Que el hallazgo de archivo entero deje la línea en 0 | Revisando los 85 | Los 85 en 0, todos con archivo |
| 3 | Que dos defectos se arreglen sin abrir el programa | Arreglándolos de verdad | Arreglados; el programa no se abrió |
| 4 | Que un `.md` mal codificado no tumbe la corrida | Corriendo `validar.py estandar` sobre un árbol con uno | **La tumba**: código 1 y traza de Python, sin salida útil |
| 5 | Que la suite siga verde | `python validadores/pruebas.py` | 276 pruebas · verde, con 5 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | **Un `.md` que no se puede decodificar tumba la corrida entera.** `comun.leer` abre sin red; el `UnicodeDecodeError` sube hasta arriba y la corrida termina en 1 **sin una sola línea de salida útil**, perdiendo todos los hallazgos ya encontrados. Se comprobó corriendo `validar.py estandar` sobre un árbol con un archivo mal codificado | Probado con fallo esperado en [`validadores/pruebas.py`](../../../../../validadores/pruebas.py). El arreglo toca `comun.py`, que §2.1 del [plan aprobado](plan_trabajo.md) no declara. Se propone |
| D-02 | Baja | **El contrato de la salida estaba en el código y no estaba escrito.** Qué trae un hallazgo y qué hace cada severidad se deducía leyendo `comun.py` | **Corregido en esta fase**: escrito en [`validadores/docs/comun.md`](../../../../../validadores/docs/comun.md), que §2.1 del plan sí declara |
| D-03 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales** de la HU. Se probaron igual, y por eso apareció `D-01` | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

**`D-01` es el que deja un criterio en «No»**, y no lo habría encontrado nadie: es justo el transversal al que el plan no le escribió caso.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-003-formato-del-hallazgo.md#ca-01--el-hallazgo-alcanza-para-arreglar-sin-abrir-el-programa) | CP-001, CP-002 | 207 de 207 con archivo y regla; dos defectos reales arreglados sin abrir ningún validador | Sí |
| [CA-02](../HU-003-formato-del-hallazgo.md#ca-02--lo-dudoso-sale-como-aviso-y-no-detiene) | CP-003 | 151 avisos y código 0, por el camino real | Sí |
| [CA-03](../HU-003-formato-del-hallazgo.md#ca-03--una-falla-detiene) | CP-004 | Basta una falla entre avisos para terminar en 1 | Sí |
| Transversal · Límites | CP-001 | El hallazgo de archivo entero tiene forma definida: `linea = 0`, y al imprimir se omite | Sí |
| Transversal · Errores | Prueba propia, fuera del plan | **`comun.leer` abre sin red.** Un `.md` mal codificado revienta con `UnicodeDecodeError` y se lleva la corrida entera, con todos los hallazgos ya encontrados. Es lo contrario de «mensaje entendible, no volcado técnico» | **No** |

**El que no cumple:** el transversal de **errores**. Se traslada a una fase `B-EP-004-HU-003`: el arreglo toca `comun.py`, que §2.1 del plan no declara.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Subcomandos revisados | Todos los que produjeron hallazgos | `flujo`, `fases`, `trazabilidad` y `estandar` | Sí |
| Hallazgos sin archivo, sin línea o sin regla | 0, o anotados | 0 sin archivo · 0 sin regla · **85 sin línea, todos de archivo entero y anotados** | Sí |
| Veces que hizo falta abrir el programa para arreglar | **0** | **0** | Sí |
| Pruebas de la suite | Línea base + 2, en verde | Línea base + **8**, en verde | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** los tres criterios de aceptación numerados quedaron verificados sobre una corrida real, no sobre un ejemplo: 207 hallazgos con archivo y regla, los 85 de archivo entero con su forma definida, y los dos códigos de salida comprobados por el camino que usa quien trabaja. El CA-01 se probó de la única forma que de verdad lo prueba — **arreglando dos defectos reales sin abrir el validador que los reportó**. Y el contrato que faltaba quedó escrito.

Lo que no cumple es el **transversal de errores**: un archivo que no se puede leer no da «un mensaje entendible» sino un volcado de Python que además **borra todo el trabajo de esa corrida**. Es el peor momento posible para caerse — cuando ya hay hallazgos que reportar.

**Qué falta para que cumpla:** que `comun.leer` maneje el archivo ilegible y lo convierta en un hallazgo en vez de en una excepción (`D-01`). Toca `comun.py`, que el plan aprobado no declara: **pide una fase `B-EP-004-HU-003`**.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `FormatoDelHallazgo`: 8 pruebas — 7 en verde y 1 como fallo esperado, que es `D-01` |
| EV-02 | Arreglos reales | Los cinco defectos de `validar.py estandar` corregidos esta sesión, dos de ellos usados como caso |
| EV-03 | El contrato escrito | [`validadores/docs/comun.md`](../../../../../validadores/docs/comun.md), sección «El contrato de la salida» |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 276 pruebas, verde, 5 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
