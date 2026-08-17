# Plan de Pruebas — Fase A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Los avisos de `F18` de otras fases no se arreglan acá.** Cada uno pertenece a la fase de otra HU, y tocarlo sería editar trabajo ajeno. Se cuentan como línea base.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Solape entre modelos | Que ninguna de las cinco preguntas la responda más de un modelo | Lectura de `plantillas/` | Sí |
| Rastro del control de versiones | Que el plan aprobado no se haya reescrito después | Historial de este repositorio | No |
| Programa | Que `validar.py flujo` detecte la tarea sin criterio y el criterio sin desglose | Este repositorio y carpetas temporales | Sí |

**Por qué el CA-02 se prueba por el historial y no por el contenido.** El control de versiones ya guarda cada versión del archivo. Una copia paralela del plan aprobado sería otro archivo más, y se desincronizaría.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Documento | ☑ | El solape entre los cinco modelos |
| Negativa | ☑ | Tarea sin criterio y criterio sin desglose tienen que salir reportados |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Solape por pregunta, no por sección** — dos modelos pueden compartir una sección y contestar preguntas distintas; lo que no puede repetirse es la **pregunta**. La lista de las cinco preguntas se toma de la tabla que ya traen las HU, no se inventa (riesgo `R-03`).
- **El historial como oráculo** — arriba. El resultado esperado del CA-02 no sale de mirar el plan de hoy: sale de comparar las versiones que el historial ya guardó.
- **La ausencia como comprobación** — el plan **no lleva** columna de estado, a propósito. El caso comprueba que no la tiene y que el avance en vivo aparece donde corresponde, en el estado de la fase.
- **Línea base antes de medir** — la cuenta de avisos de `F18` que hay hoy se anota para que las fases que los arreglen tengan contra qué comparar.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py flujo` y `fases` sobre este repositorio, más `validadores/pruebas.py` entera.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-01](../HU-003-modelos-de-la-fase.md#ca-01--los-documentos-de-la-fase-existen-y-no-se-pisan) | [CP-001](#cp-001--ninguna-de-las-cinco-preguntas-la-responde-más-de-un-modelo), [CP-002](#cp-002--la-fase-a-la-que-le-falta-un-documento-sale-reportada) | Documento | Alta | Sí | ☐ |
| HU-003 | [CA-02](../HU-003-modelos-de-la-fase.md#ca-02--el-plan-se-aprueba-antes-y-no-se-reescribe-después) | [CP-003](#cp-003--el-plan-aprobado-no-cambió-después-según-el-historial), [CP-004](#cp-004--el-plan-no-lleva-columna-de-estado) | Funcional | Crítica | No | ☐ |
| HU-003 | [CA-03](../HU-003-modelos-de-la-fase.md#ca-03--cada-criterio-de-aceptación-tiene-su-caso-y-cada-tarea-su-criterio) | [CP-005](#cp-005--la-tarea-sin-criterio-y-el-criterio-sin-desglose-salen-reportados) | Negativa | Alta | Sí | ☐ |
| HU-003 | RNF — que no haya dos documentos con la misma respuesta | [CP-001](#cp-001--ninguna-de-las-cinco-preguntas-la-responde-más-de-un-modelo) | Documento | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Ninguna de las cinco preguntas la responde más de un modelo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 y RNF |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los cinco modelos de la fase, y la lista de las cinco preguntas tomada de la tabla de la HU |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la lista de las cinco preguntas | Sale de la tabla de la HU, no se inventa |
| 2 | Por cada modelo, anotar qué pregunta responde | Cada modelo con una |
| 3 | Cruzar modelos contra preguntas | Correspondencia uno a uno |
| 4 | Anotar el solape que aparezca, con el párrafo que lo produce | Queda citable, sin editar los modelos |

**Resultado esperado final:** los cinco documentos no se pisan, y el que se pise queda señalado con su párrafo.

---

### CP-002 — La fase a la que le falta un documento sale reportada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal con una fase de mentira |
| **Datos de entrada** | Una fase con los cinco documentos y otra a la que le falta uno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py fases` sobre la fase completa | No sale reportada |
| 2 | Quitarle un documento y volver a correr | Sale reportada, y dice cuál falta |
| 3 | Repetir quitando cada uno de los cinco | Los cinco se detectan |
| 4 | Comprobar que la ruta y los nombres exigidos son los de `F12.13` | Coinciden |

**Resultado esperado final:** lo que falta se ve, y se ve cuál.

---

### CP-003 — El plan aprobado no cambió después, según el historial

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Una fase ya cerrada de este repositorio |
| **Datos de entrada** | Las versiones del `plan_trabajo.md` que guarda el historial |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ubicar en el historial el punto en que se aprobó el plan | Queda identificado, con su fecha |
| 2 | Listar los cambios del archivo posteriores a esa fecha | Ninguno de fondo |
| 3 | Clasificar los que aparezcan: corrección de enlace o cambio de alcance | Solo los primeros son admisibles |
| 4 | Anotar con fase y fecha el que sea cambio de alcance | Queda como hallazgo de incumplimiento de [`02·F9`](../../../../../base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md); corregirlo es de esa fase |

**Resultado esperado final:** el plan aprobado sirve para comparar lo dicho contra lo hecho, porque no se movió.

---

### CP-004 — El plan no lleva columna de estado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | El modelo del plan de trabajo y el del estado de la fase |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el modelo del plan una columna de estado por tarea | No la tiene |
| 2 | Buscar dónde se lleva el avance en vivo | En el estado de la fase, §1.2 |
| 3 | Comprobar en una fase real que el avance se anota ahí y no en el plan | Se anota ahí |

**Resultado esperado final:** el plan queda como se aprobó porque no hay dónde tocarlo mientras la fase corre.

> **Esta es una prueba de ausencia**, y por eso el paso 2 dice dónde sí vive el dato: si no, "no está" se leería como "falta".

---

### CP-005 — La tarea sin criterio y el criterio sin desglose salen reportados

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un plan con una tarea que no cuelga de ningún CA, y otro con un CA sin tareas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar cuántos avisos de `F18` hay hoy en el repositorio | Queda la línea base, con la fecha |
| 2 | Correr `validar.py flujo` sobre el plan con la tarea suelta | Sale el aviso |
| 3 | Correr sobre el plan con el CA sin tareas | Sale el aviso |
| 4 | Correr sobre un plan correcto | No sale ninguno |
| 5 | Comprobar que la cuenta del repositorio no cambió | Los avisos de otras fases siguen ahí, sin tocar |

**Resultado esperado final:** el revisor ve los dos huecos, y los de otras fases quedan contados, no arreglados.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el plan de una fase cerrada haya cambiado de alcance después de aprobado (riesgo `R-01`) | Se anota con fase y fecha. Corregirlo es de esa fase, no de esta |
| **Alta** | Que dos modelos respondan la misma pregunta | Se anota con el párrafo. Cambiar un modelo sube versión y se propone |
| **Media** | Cruce con la fase de EP-002 · HU-005, que toca dos de estos modelos (riesgo `R-02`) | La que llegue segunda relee antes de escribir |
| **Media** | Que el revisor no detecte la tarea suelta o el criterio sin desglose | Antes de cerrar — el CA-03 quedaría en «No» |
| **Baja** | Avisos de `F18` en fases viejas | Se cuentan como línea base |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Preguntas respondidas por más de un modelo | **0** |
| Documentos de fase de otras HU modificados | **0** |
| Avisos de `F18` del repositorio | Anotados como línea base, con su fecha |
| Pruebas de la suite | Las de la línea base, más la nueva, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
