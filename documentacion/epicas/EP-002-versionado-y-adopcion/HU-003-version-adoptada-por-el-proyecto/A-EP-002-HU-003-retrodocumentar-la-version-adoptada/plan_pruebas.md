# Plan de Pruebas — Fase A-EP-002-HU-003-retrodocumentar-la-version-adoptada   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-002-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Condición de arranque, no negociable.** Todo se hace sobre una **copia local** del proyecto elegido. No se escribe en la carpeta viva de ningún proyecto ajeno ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada) · riesgo `R-03` del plan).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Programa | Que `validar.py version` lea la versión declarada y su fecha | Copia local del proyecto | Sí |
| Unitario | Que una versión declarada que no existe en el registro se detecte | Este repositorio | Sí |
| Reconstrucción | Que desde el historial se pueda decir bajo qué versión cerró una fase | Copia local | No |

**De dónde sale la lista de versiones que existieron.** Del [`CHANGELOG.md`](../../../../../CHANGELOG.md). **No** de una lista aparte: dos listas de lo mismo se separan solas.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | El CA-02: una versión inventada tiene que salir reportada |
| Trazabilidad | ☑ | El CA-03 y el RNF: el historial sirve para reconstruir |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Reconstrucción hacia atrás** — el CA-03 no se prueba mirando si el archivo existe: se prueba **usándolo**, para responder bajo qué versión cerró una fase concreta. Un historial que existe y no permite responder eso no cumple el CA.
- **La versión que no existe, a propósito** — el CA-02 se prueba declarando una versión inventada. Sin ese caso, la comprobación pasaría igual sin comprobar nada.
- **El hallazgo se mide, no se arregla** — el registro de adopciones tiene dos pendientes abiertos, el [44](../../../../../pendientes/hecho/el-registro-no-se-escribe-si-no-cambia-la-huella.md) y el [46](../../../../../pendientes/hecho/el-registro-se-escribe-antes-de-contarse.md). Esta fase produce la evidencia que esos pendientes necesitan; no los cierra.
- **El aviso no se silencia** — el propio estándar no declara versión adoptada y recibe el aviso igual. Queda como hallazgo escrito: silenciar un aviso es cambiar un validador, y eso se decide con el plan ampliado.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py version` sobre la copia del proyecto elegido y sobre este repositorio, más `validadores/pruebas.py` entera.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-01](../HU-003-version-adoptada-por-el-proyecto.md#ca-01--el-proyecto-declara-su-versión-y-su-fecha) | [CP-001](#cp-001--el-proyecto-declara-versión-y-fecha-y-el-programa-las-lee) | Funcional | Alta | Sí | ☐ |
| HU-003 | [CA-02](../HU-003-version-adoptada-por-el-proyecto.md#ca-02--una-versión-que-no-existe-se-detecta) | [CP-002](#cp-002--la-versión-declarada-que-no-existe-en-el-registro-se-detecta), [CP-003](#cp-003--la-versión-inventada-declarada-en-copia-sale-reportada) | Negativa | Crítica | Parcial | ☐ |
| HU-003 | [CA-03](../HU-003-version-adoptada-por-el-proyecto.md#ca-03--queda-el-historial-de-adopciones) | [CP-004](#cp-004--desde-el-historial-se-dice-bajo-qué-versión-cerró-una-fase) | Trazabilidad | Alta | No | ☐ |
| HU-003 | RNF — que la declaración se versione con el proyecto | [CP-005](#cp-005--el-registro-de-adopciones-vive-en-carpeta-versionada) | Trazabilidad | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El proyecto declara versión y fecha, y el programa las lee

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta. Copia local del proyecto elegido |
| **Datos de entrada** | El `CLAUDE.md` del proyecto, con su línea de versión adoptada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py version` sobre la copia | Lee la versión declarada y la fecha |
| 2 | Comprobar que lo leído coincide con la línea del `CLAUDE.md` | Coincide |
| 3 | Quitar la línea en la copia y volver a correr | Avisa que falta |
| 4 | Correr sobre este repositorio, que no declara versión adoptada | Avisa igual; queda escrito como hallazgo, sin silenciarlo |
| 5 | Comprobar que ninguna corrida escribió | Ningún archivo modificado |

**Resultado esperado final:** la declaración se lee de un solo lugar, y su ausencia se nota.

> **El paso 3 es el que da valor al 1.** Sin él, el caso pasaría con un programa que devuelve algo fijo.

---

### CP-002 — La versión declarada que no existe en el registro se detecta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna: la prueba lee el registro |
| **Datos de entrada** | Una versión declarada que no está en el `CHANGELOG` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la lista de versiones del registro | Queda leída del `CHANGELOG`, no de una lista aparte |
| 2 | Comprobar que una versión declarada que está en la lista, pasa | Pasa |
| 3 | Comprobar que una que no está, se detecta | Se detecta, y el mensaje dice cuál |
| 4 | Probar con una versión con forma válida pero futura | Se detecta igual |

**Resultado esperado final:** declarar una versión no es lo mismo que declarar una versión que existe.

---

### CP-003 — La versión inventada, declarada en copia, sale reportada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Copia local del proyecto |
| **Datos de entrada** | Una versión inventada escrita en el `CLAUDE.md` de la copia |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Declarar la versión inventada en la copia | Queda escrita |
| 2 | Correr `validar.py version` | Se anota qué reporta **hoy** |
| 3 | Comparar con lo que el CA exige | Si no lo detecta, queda como hallazgo y el CA en «No» |
| 4 | Devolver la copia a su estado y borrarla | No queda rastro |

**Resultado esperado final:** queda medido si el CA-02 está cumplido de verdad o solo escrito.

> Si cerrarlo obliga a tocar `version.py` (riesgo `R-01`), **se para y se propone** con el plan ampliado ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).

---

### CP-004 — Desde el historial se dice bajo qué versión cerró una fase

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta. Copia con su historial de adopciones |
| **Datos de entrada** | Una fase cerrada del proyecto elegido, con su fecha |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la fecha de cierre de la fase | Queda a la vista |
| 2 | Buscar en el historial qué versión estaba adoptada ese día | Sale una, y solo una |
| 3 | Responder bajo qué versión cerró, **usando solo el historial** | Se puede responder sin preguntarle a nadie |
| 4 | Anotar contra los pendientes [44](../../../../../pendientes/hecho/el-registro-no-se-escribe-si-no-cambia-la-huella.md) y [46](../../../../../pendientes/hecho/el-registro-se-escribe-antes-de-contarse.md) lo que se encuentre mal | Queda la evidencia que esos pendientes necesitan |

**Resultado esperado final:** el historial existe y **sirve**, o queda dicho en qué falla.

> **El paso 3 es el CA.** Que el archivo exista no basta: lo que la HU pide es poder reconstruir.

---

### CP-005 — El registro de adopciones vive en carpeta versionada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / RNF |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | Copia local del proyecto |
| **Datos de entrada** | La ruta donde el instalador escribe el historial |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ubicar dónde vive el registro de adopciones | Queda la ruta |
| 2 | Comprobar que esa carpeta está versionada | Lo está: no se queda en una sola máquina |
| 3 | Comprobar que no está en una carpeta ignorada ni local | No lo está |

**Resultado esperado final:** el historial viaja con el proyecto, que es lo que lo hace revisable.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que se escriba en la carpeta viva del proyecto ajeno | Inmediato. Se detiene la fase y se restaura |
| **Alta** | Que una versión inventada pase sin reporte | Se anota, el CA queda en «No» y se propone la corrección aparte |
| **Media** | Que el historial no permita reconstruir bajo qué versión cerró una fase | Se anota contra los pendientes 44 y 46 |
| **Media** | Que el registro del proyecto elegido traiga el defecto del 46 (riesgo `R-02`) | Se prueba igual: es la evidencia que ese pendiente necesita |
| **Baja** | Que el propio estándar reciba el aviso por no declarar versión | Se deja escrito. Silenciarlo sería cambiar un validador |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Archivos modificados en la carpeta viva del proyecto ajeno | **0** |
| Listas de versiones mantenidas aparte del `CHANGELOG` | **0** |
| Validadores modificados en esta fase | **0** — lo que haga falta se propone |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
