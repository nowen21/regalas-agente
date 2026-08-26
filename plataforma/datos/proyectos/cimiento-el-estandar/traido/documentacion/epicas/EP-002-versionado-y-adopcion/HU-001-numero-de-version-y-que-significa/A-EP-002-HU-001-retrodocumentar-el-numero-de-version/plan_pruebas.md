# Plan de Pruebas — Fase A-EP-002-HU-001-retrodocumentar-el-numero-de-version   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-002-HU-001 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que `VERSION` traiga tres partes y sea lo que devuelve `version_estandar()` | Lectura del repositorio | Sí |
| Recorrido del registro | Que entre entradas consecutivas ninguna parte salte ni reinicie | Lectura del [`CHANGELOG.md`](../../../../../CHANGELOG.md) | Sí |
| Revisión por tipo | Que MAYOR obligue y PARCHE no cambie qué se exige | Este repositorio | No — hay que leer qué exigía cada versión |

**De dónde sale el número.** Del propio [`VERSION`](../../../../../VERSION). **No** se escribe dentro de la prueba: una versión escrita a mano envejece en la subida siguiente y la prueba pasa a mentir.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Continuidad | ☑ | El RNF: ninguna parte salta ni reinicia |
| Documento | ☑ | La clasificación de cada entrada del registro |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Número leído, no escrito** — arriba.
- **Muestra por clase, no al azar** — los CA-02 y CA-03 se prueban con **tres** entradas de cada tipo, elegidas por ser las más discutibles, no las más cómodas. Una sola entrada bien clasificada no dice nada del criterio.
- **El contraste que define el tipo** — para una MAYOR se pregunta qué tiene que hacer un proyecto **al día** que antes no hacía; para una PARCHE, qué exigencia cambió. Si la respuesta a la segunda es "ninguna", la clasificación era correcta.
- **La excepción documentada** — el tramo de las dos numeraciones vivas del 2026-08-14 (pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md)) se declara como excepción **en el caso**, no se silencia en la prueba. Un hecho conocido que rompe una prueba se documenta; no se tapa.
- **Hallazgo anotado, entrada intacta** — una subida mal clasificada se anota. El registro es rastro y no se reescribe (RN-04 de [HU-002](../../HU-002-registro-de-cambios/HU-002-registro-de-cambios.md)).

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera —las que ya están más las dos nuevas— y `validar.py versiones` como línea base.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | [CA-01](../HU-001-numero-de-version-y-que-significa.md#ca-01--el-número-existe-y-se-lee-en-un-solo-lugar) | [CP-001](#cp-001--el-número-tiene-tres-partes-y-sale-de-version), [CP-002](#cp-002--ningún-otro-número-de-versión-manda-en-el-repositorio) | Funcional | Alta | Parcial | ☐ |
| HU-001 | [CA-02](../HU-001-numero-de-version-y-que-significa.md#ca-02--un-cambio-que-obliga-sube-la-parte-mayor) | [CP-003](#cp-003--cada-mayor-obliga-a-un-proyecto-al-día-a-hacer-algo-nuevo) | Documento | Alta | No | ☐ |
| HU-001 | [CA-03](../HU-001-numero-de-version-y-que-significa.md#ca-03--una-corrección-de-redacción-no-sube-la-parte-mayor) | [CP-004](#cp-004--ninguna-parche-cambió-qué-se-exige) | Documento | Alta | No | ☐ |
| HU-001 | RNF — que ninguna parte se salte | [CP-005](#cp-005--las-tres-partes-avanzan-sin-saltos-ni-reinicios) | Continuidad | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El número tiene tres partes y sale de `VERSION`

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna: la prueba lee y no escribe |
| **Datos de entrada** | El archivo `VERSION` tal como esté el día de la corrida |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `VERSION` | Trae una sola línea |
| 2 | Comprobar que tiene tres partes numéricas | Las tres, separadas por punto |
| 3 | Pedir `version.version_estandar()` | Devuelve exactamente lo mismo que el archivo |
| 4 | Cambiar el archivo en copia y volver a pedirlo | Devuelve lo cambiado: lo lee, no lo tiene escrito adentro |

**Resultado esperado final:** hay un solo lugar donde vive el número, y el programa lo lee de ahí.

> **El paso 4 es el que da valor al 3.** Sin él, el caso pasaría con una función que devuelve una constante que hoy coincide.

---

### CP-002 — Ningún otro número de versión manda en el repositorio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Todo el repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el repositorio números con forma de versión del estándar | Queda la lista de apariciones, con archivo y línea |
| 2 | Separar las que **citan** —registro, fases selladas, checklists— de las que **declaran** | Solo el `VERSION` declara |
| 3 | Comprobar que ninguna de las que citan se usa como fuente | Ninguna manda |

**Resultado esperado final:** una sola fuente de verdad, y las citas son citas.

> **El paso 2 evita el falso positivo.** El registro y las fases cerradas están llenos de números de versión, y eso es correcto: son rastro, no declaración.

---

### CP-003 — Cada MAYOR obliga a un proyecto al día a hacer algo nuevo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Tres entradas MAYOR del registro, elegidas por ser las más discutibles |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la definición de MAYOR de la cabecera del registro | Queda a la vista, y es el oráculo del caso |
| 2 | Por cada una de las tres, responder qué tiene que hacer un proyecto al día que antes no hacía | Hay una respuesta concreta para las tres |
| 3 | Comprobar que esa respuesta no es "nada" ni "actualizar el número" | Ninguna de las tres |
| 4 | Anotar como hallazgo la que no cumpla, sin tocar la entrada | Queda citable; el registro no se reescribe |

**Resultado esperado final:** la parte mayor significa lo que el registro dice que significa.

---

### CP-004 — Ninguna PARCHE cambió qué se exige

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-03 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-003 corrido, con el mismo oráculo |
| **Datos de entrada** | Tres entradas PARCHE del registro |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Por cada una, leer qué texto cambió | Queda identificado el cambio |
| 2 | Preguntar qué exigencia cambió con él | La respuesta es "ninguna" en las tres |
| 3 | Comprobar que un proyecto al día no tiene nada que hacer con esa subida | Nada |
| 4 | Anotar como hallazgo la que no cumpla | Sin tocar la entrada |

**Resultado esperado final:** una corrección de redacción no obliga a nadie, y por eso no sube la parte mayor.

---

### CP-005 — Las tres partes avanzan sin saltos ni reinicios

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / RNF |
| **Tipo** | Continuidad |
| **Prioridad** | Media |
| **Precondiciones** | El número de pruebas de la suite anotado antes de tocarla |
| **Datos de entrada** | La secuencia de versiones del registro |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las versiones en orden | Queda la secuencia |
| 2 | Comprobar entrada contra entrada que ninguna parte salta | Cada subida es de una sola parte, y de a uno |
| 3 | Comprobar que al subir una parte, las de abajo vuelven a cero | Sin excepción |
| 4 | Declarar el tramo de las dos numeraciones vivas del 2026-08-14 como excepción documentada | Queda atado al pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md), no silenciado en la prueba |
| 5 | Correr la suite completa y comparar contra la línea base | Ninguna prueba que pasaba, falla |

**Resultado esperado final:** la numeración es una secuencia, y el único hueco conocido está declarado.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que `version_estandar()` no lea el archivo sino una constante | Inmediato. El CA queda en «No» |
| **Alta** | Que una MAYOR no obligue a nada, o una PARCHE haya cambiado una exigencia (riesgo `R-01`) | Se anota como hallazgo. **Corregirlo no es de esta fase**: el registro no se reescribe |
| **Media** | Que la prueba de continuidad falle fuera del tramo conocido | Antes de cerrar |
| **Baja** | Números de versión citados en documentos que se confundan con declaraciones | Se anota en el resultado |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Entradas revisadas por tipo | 3 MAYOR y 3 PARCHE |
| Versiones escritas a mano dentro de una prueba | **0** |
| Entradas del registro reescritas | **0** |
| Pruebas de la suite | Las de la línea base, más 2, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
