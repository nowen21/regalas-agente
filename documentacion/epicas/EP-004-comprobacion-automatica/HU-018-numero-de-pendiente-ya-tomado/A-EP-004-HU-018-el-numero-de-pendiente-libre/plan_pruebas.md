# Plan de Pruebas — Fase A-EP-004-HU-018-el-numero-de-pendiente-libre   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-018 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-018-el-numero-de-pendiente-libre` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El programa avisa y no asigna.** Avisar deja la decisión en quien abre el pendiente y no pisa lo que otra sesión esté haciendo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que el próximo libre sea el siguiente al mayor | Carpetas temporales | Sí |
| Detección | Que dos archivos con el mismo número se reporten | Carpetas temporales | Sí |
| Cruce | Que la carpeta y el índice se comparen en los dos sentidos | Este repositorio y temporales | Sí |

**Por qué el próximo libre es el siguiente al mayor y no el primer hueco.** Un hueco puede ser un pendiente cerrado y movido a `hecho/`; reusar su número rompe las citas que lo nombran.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | Numeración con huecos, y el número cerrado que ya no está en la carpeta viva |
| Negativa | ☑ | El número repetido, que ya pasó de verdad |
| Medición | ☑ | El desfase de hoy entre carpeta e índice |

### 3.3 Técnicas de diseño de casos

- **El hueco que no se reusa** — el caso principal del CA-01 tiene huecos a propósito, porque el error natural sería ofrecerlos.
- **El cruce en los dos sentidos** — archivo sin línea y línea sin archivo. El segundo es el síntoma de un pendiente movido a `hecho/` sin actualizar el índice, y es el que hoy se da.
- **El caso ocurrido como dato** — el 2026-08-16 dos sesiones tomaron el número 52 y dos archivos numerados 40 convivieron media hora. El caso del CA-02 reproduce esa situación.
- **Línea base antes de medir** — el riesgo `R-02`: hoy `validar.py estandar` ya reporta dos pendientes que la carpeta tiene y el índice no. Se anota **antes**, para no confundirlo con lo nuevo.
- **El límite del aviso, dicho** — el riesgo `R-01`: avisar no evita el choque, lo muestra. Repartir turnos es la decisión del pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md), y eso queda escrito.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y el subcomando nuevo sobre este repositorio y sobre las carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-018 | [CA-01](../HU-018-numero-de-pendiente-ya-tomado.md#ca-01--dice-cuál-es-el-próximo-número-libre) | [CP-001](#cp-001--el-próximo-libre-es-el-siguiente-al-mayor-no-el-del-hueco) | Límites | Alta | Sí | ☐ |
| HU-018 | [CA-02](../HU-018-numero-de-pendiente-ya-tomado.md#ca-02--avisa-del-número-repetido) | [CP-002](#cp-002--dos-archivos-con-el-mismo-número-se-reportan-con-los-dos-nombres) | Negativa | Crítica | Sí | ☐ |
| HU-018 | [CA-03](../HU-018-numero-de-pendiente-ya-tomado.md#ca-03--cruza-la-carpeta-con-el-índice) | [CP-003](#cp-003--el-cruce-se-reporta-en-los-dos-sentidos) | Funcional | Alta | Sí | ☐ |
| HU-018 | RNF — que el aviso llegue antes de escribir el archivo | [CP-004](#cp-004--el-aviso-llega-antes-y-su-límite-queda-escrito) | Funcional | Media | Parcial | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El próximo libre es el siguiente al mayor, no el del hueco

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Una carpeta de pendientes con huecos en la numeración, y algunos ya en `hecho/` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre la carpeta con huecos | Dice el próximo libre |
| 2 | Comprobar que es el siguiente al mayor | Lo es, no el del hueco |
| 3 | Comprobar que los números de `hecho/` **también** cuentan como tomados | Cuentan |
| 4 | Agregar un pendiente con ese número y volver a correr | Ahora ofrece el siguiente |

**Resultado esperado final:** el número deja de elegirse a ojo, y ninguna cita se rompe por reuso.

> **El paso 3 es el que evita el error caro.** Un pendiente cerrado y movido deja un hueco que parece libre y no lo está.

---

### CP-002 — Dos archivos con el mismo número se reportan, con los dos nombres

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Dos archivos de pendiente con el mismo número, como pasó el 2026-08-16 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner dos archivos con el mismo número | Quedan los dos |
| 2 | Correr | Se reporta la repetición |
| 3 | Comprobar que el hallazgo nombra **los dos** archivos | Los dos |
| 4 | Renumerar uno y volver a correr | Deja de reportarse |
| 5 | Probar con uno en la carpeta viva y otro en `hecho/` | También se detecta |

**Resultado esperado final:** el choque que ya pasó se ve en la corrida, no media hora después.

---

### CP-003 — El cruce se reporta en los dos sentidos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal, y el estado actual del repositorio anotado |
| **Datos de entrada** | Un pendiente sin línea en el índice, y una línea del índice sin su archivo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar cuántos desfases reporta hoy el repositorio | Queda la línea base, con su fecha |
| 2 | Correr sobre el pendiente sin línea en el índice | Se reporta |
| 3 | Correr sobre la línea sin archivo | Se reporta, y se distingue del caso anterior |
| 4 | Correr sobre una carpeta y un índice que coinciden | No sale nada |
| 5 | Comprobar que ninguna corrida escribió en el índice | Ningún archivo modificado |

**Resultado esperado final:** el índice y la carpeta dejan de separarse en silencio.

> **La línea sin archivo es el caso que hoy se da**, cuando un pendiente se mueve a `hecho/` y el índice queda con la línea vieja.

---

### CP-004 — El aviso llega antes, y su límite queda escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-018 / RNF |
| **Tipo** | Funcional |
| **Prioridad** | Media |
| **Precondiciones** | Los tres casos anteriores corridos |
| **Datos de entrada** | El flujo de abrir un pendiente nuevo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir el próximo libre **antes** de escribir el archivo | Se puede: la comprobación corre sola |
| 2 | Comprobar que el programa no crea ni renombra archivos | No los crea |
| 3 | Simular dos sesiones que piden el número a la vez | Las dos reciben el mismo: el aviso no reparte turnos |
| 4 | Dejar escrito ese límite, atado al pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) | Queda escrito |

**Resultado esperado final:** el aviso sirve para lo que sirve, y lo que no resuelve queda dicho.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el programa ofrezca un número ya usado por un pendiente cerrado | Inmediato. Reusar el número rompe las citas |
| **Alta** | Que dos archivos con el mismo número no se reporten | Inmediato — es el caso que motivó la HU |
| **Media** | Que el programa asigne en vez de avisar | Se corrige: asignar pisa lo que otra sesión esté haciendo |
| **Media** | Que el desfase de hoy se confunda con lo nuevo (riesgo `R-02`) | Se anota el estado antes de empezar |
| **Baja** | Cruce con la fase de [HU-016](../../HU-016-el-pendiente-cerrado-nombra-su-fase/A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/plan_trabajo.md), que puede crear el mismo archivo (riesgo `R-03`) | La segunda relee y se suma en vez de reescribir |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Números de pendientes cerrados ofrecidos como libres | **0** |
| Repeticiones no detectadas | **0** |
| Archivos creados o renombrados por el programa | **0** |
| Desfase carpeta ↔ índice de hoy | Anotado como línea base, con su fecha |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
