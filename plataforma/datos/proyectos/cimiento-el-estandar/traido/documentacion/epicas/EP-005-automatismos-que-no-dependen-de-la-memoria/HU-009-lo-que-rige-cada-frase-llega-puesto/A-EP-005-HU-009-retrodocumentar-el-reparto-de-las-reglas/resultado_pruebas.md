# Resultado de pruebas — Fase A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas` |
| **HU** | [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-005-HU-009 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-15 |
| **Ejecutado por** | Cimiento, con el usuario aprobando el plan |
| **Ambiente y versión** | Este repositorio para las mediciones y carpetas temporales para los bordes. Estándar 15.4.2 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**El que estuvo en duda:** [CP-004](plan_pruebas.md#cp-004--lo-que-cuesta-el-arranque). Su paso 2 no dio lo que el plan esperaba, y la decisión no era del que ejecuta. El usuario la tomó el 2026-08-15: **0,21 s al abrir la sesión no se nota**. Con eso queda aprobado.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) | CA-01 | Crítica | 2026-08-15 | Cuerpos de reglas temporales con archivos `00-`, `01-` y `05-`, y el reparto roto a propósito | Aprobado | EV-01 | — |
| [CP-002](plan_pruebas.md#cp-002--el-contexto-dice-qué-llegó-puesto-y-qué-hay-que-abrir) | CA-02 · RNF-02 | Alta | 2026-08-15 | El texto entregado por el cargador, buscando sus dos encabezados | Aprobado | EV-01 | — |
| [CP-003](plan_pruebas.md#cp-003--sin-cuerpo-de-reglas-no-entrega-nada) | Transversales | Crítica | 2026-08-15 | Una carpeta temporal sin `base/`, y otra con `base/` vacía | Aprobado | EV-01 | — |
| [CP-004](plan_pruebas.md#cp-004--lo-que-cuesta-el-arranque) | CA-03 · RNF-01 | Media | 2026-08-15 | Este repositorio: 73 KB inyectados de 369 KB, y los tiempos de los dos enganches de apertura | Aprobado, con la decisión del usuario sobre el paso 2 | EV-02 | — |
| [CP-005](plan_pruebas.md#cp-005--con-el-gate-sin-pasar-entrega-solo-esa-regla) | Transversales | Crítica | 2026-08-15 | Un cuerpo de reglas temporal con el archivo del gate, declarando que el gate no pasa | Aprobado | EV-01 | — |

**Correspondencia con el plan:** 5 casos en el plan, 5 acá. Ninguno de más, ninguno de menos.

**Detalle de CP-001**

**El problema que resuelve:** que el agente arranque con las reglas que gobiernan cada frase que escribe, y no con una lista de títulos.

**La precondición:** un cuerpo de reglas con archivos de los dos tipos, los que empiezan por `00-` o `01-` y los demás.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedirle al cargador el contexto de arranque | Devuelve texto | Lo devolvió |
| 2 | Buscar el cuerpo de un archivo de identidad, uno suelto y otro dentro de su carpeta | Están completos, no como título | Los dos completos. El de la carpeta también, que es el que se caería si el reparto mirara el nombre del archivo |
| 3 | Buscar el cuerpo de un archivo de conducta, incluido uno nuevo del mismo prefijo | Está completo, y el nuevo entra sin tocar el programa | Los dos completos |
| 4 | Buscar un archivo de otro capítulo | Aparece solo su línea de índice, con ruta y título | Solo la línea, con su ruta y su título |

**Además se rompió el reparto a propósito**, dejando fuera el prefijo de conducta, y se comprobó que con eso el capítulo deja de llegar. Sin esa comprobación, una prueba en verde no diría si de verdad vigila algo.

**Detalle de CP-002**

**El problema que resuelve:** que se sepa cuál regla ya está leída y cuál hay que abrir antes de tocar su tema. Sin eso se trabaja de memoria sobre reglas que solo se nombraron.

**La precondición:** el contexto que entrega el cargador, con las dos partes.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el encabezado de lo que llegó completo | Dice que rige la sesión y que es obligatorio | Dice «reglas base del estándar — cargadas, obligatorias» |
| 2 | Leer el encabezado del índice | Dice que eso no está cargado y que hay que abrirlo antes de tocar el tema | Lo dice, y agrega que no se suponga qué manda la regla |

**Detalle de CP-003**

**El problema que resuelve:** que un proyecto sin cuerpo de reglas no se vea afectado ni reciba mensajes que no le tocan.

**La precondición:** una carpeta temporal sin nada.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedirle el contexto a una carpeta sin `base/` | Devuelve vacío, sin fallar | Vacío |
| 2 | Mirar la carpeta | Sigue vacía: no escribió nada | Vacía |
| 3 | Repetirlo con una `base/` que existe pero no tiene reglas | Devuelve vacío | Vacío |

**Detalle de CP-004**

**El problema que resuelve:** que lo que se gana en cumplimiento no se pague con una espera al abrir cada sesión.

**La precondición:** este repositorio, con su cuerpo de reglas completo: 369 KB en 188 reglas.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Medir cuánto pesa lo que se inyecta | Un número, en KB, escrito con su fecha | **73 KB de 369 KB**, medido el 2026-08-15. Armar ese texto tarda 0,049 s |
| 2 | Medir cuánto tarda el enganche que lo entrega | Queda por debajo de lo que ya tardan los otros enganches de apertura | **No dio lo esperado.** `hook_sesion.py` tarda 0,21 s y `hook_recuerdos.py` 0,13 s: es el más lento de los dos, no el más rápido |

**Detalle de CP-005**

**El problema que resuelve:** que cuando el arranque está detenido no lleguen las reglas de trabajo, porque leerlas ahí invita a trabajar sobre una estructura que el estándar manda detener.

**La precondición:** un cuerpo de reglas temporal que incluye el archivo del gate.

**Los pasos, qué tenía que pasar en cada uno y qué salió:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedir el contexto declarando que el gate no pasa | Entrega la regla del gate y nada más | Entregó esa regla, con el aviso de arranque detenido |
| 2 | Buscar cualquier otra regla en lo entregado | No está | No estaba |

**Qué salió distinto de lo esperado:** el paso 2 de CP-004. El plan pedía que el enganche que entrega las reglas fuera más rápido que los otros de apertura, y es el más lento: 0,21 s contra 0,13 s. La medición es la que es, y el criterio dice "que no se note", que no es un número. **El usuario decidió el 2026-08-15 que no se nota**, así que `CA-03` cumple. Lo que estaba mal era el resultado esperado del plan, que comparó contra otro enganche en vez de contra lo que se siente al abrir.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Lo que pesa el arranque | Midiendo el contexto entregado sobre este repositorio | 73 KB de 369 KB, el 2026-08-15 |
| 2 | Lo que tarda | Corriendo los dos enganches de apertura como órdenes del sistema | `hook_sesion.py` 0,21 s · `hook_recuerdos.py` 0,13 s |
| 3 | Que las pruebas cacen un reparto roto | Cambiando el reparto en memoria y volviendo a pedir el contexto | El capítulo de conducta deja de llegar, y la prueba lo detecta |

---

## 4. Defectos encontrados

Ninguno en el programa. Lo de CP-004 no es un defecto: es una medición que el plan esperaba de otra forma.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) | CP-001 | Los capítulos `00` y `01` llegan completos; el resto, como índice | Sí |
| [CA-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-02--se-dice-qué-llegó-puesto-y-qué-llegó-como-índice) | CP-002 | Los dos encabezados dicen qué es cada cosa | Sí |
| [CA-03](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-03--el-arranque-no-se-vuelve-lento) | CP-004 | 73 KB y 0,21 s. El usuario decidió que no se nota | Sí |
| [RNF-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#5-requisitos-no-funcionales) | CP-004 | Lo mismo | Sí |
| [RNF-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#5-requisitos-no-funcionales) | CP-002 | Queda dicho qué se cargó completo y qué no | Sí |
| Transversales | CP-003 y CP-005 | No escribe nada donde no lo llaman, y con el gate detenido entrega solo esa regla | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias con caso | Plan §5 | 100% | 100%: 5 de 5 | Sí |
| Peso de lo inyectado | Plan §12 | Anotado con su fecha | 73 KB, 2026-08-15 | Sí |
| Tiempo del enganche de apertura | Plan §12 | Por debajo del más lento que ya corre | 0,21 s, y es el más lento | **No**, y decidido |

**Lo que no se cumplió:** la meta del tiempo, escrita comparando contra otros enganches. No se reescribe el plan. La decisión está tomada y escrita: el usuario dijo el 2026-08-15 que 0,21 s no se nota, así que el criterio de la HU se cumple aunque la meta del plan quedara corta. La meta estaba mal enunciada, no el programa.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los cinco casos pasaron, las seis exigencias quedaron verificadas, y el reparto que llevaba diez versiones sin documentar quedó escrito, probado y medido. La única duda era si 0,21 s al abrir la sesión se nota; el usuario decidió el 2026-08-15 que no.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `RepartoDeLasReglas`: 10 casos, en verde |
| EV-02 | Medición a mano | §3 de este documento |
| EV-03 | Comprobación del estándar | `validar.py estandar` |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
