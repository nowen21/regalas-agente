# Plan de Pruebas — Fase A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige` |
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
| Recorrido real | Que las estaciones se llamen en orden y que ninguna se salte | Un encargo chico y real, en rama aparte | No |
| Detención en puerta | Que el trabajo pare donde aprueba una persona | Rama aparte | No |
| Retoma a ciegas | Que una sesión nueva siga leyendo solo el estado de la fase | Este repositorio | No |
| Comparación | Que las trece estaciones y las once etapas de `F15` no se contradigan | Lectura | No |

**Por qué con un encargo real y no leyendo el documento.** Leer no prueba que el procedimiento se detenga: hay que **llegar a la puerta**. Cuál es el encargo lo decide la duda 1, elegido chico a propósito (riesgo `R-03`).

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | El CA-01: el salto de estación **no** se concede |
| Recuperación | ☑ | El CA-03: retomar sin la conversación |
| Documento | ☑ | Trece estaciones contra once etapas |

### 3.3 Técnicas de diseño de casos

- **La sesión que no sabe nada** — el CA-03 se prueba con una sesión nueva **a ciegas**. Preguntarle a quien ya participó no prueba nada: esa persona retoma de memoria, y lo que se mide es si el documento alcanza.
- **Bitácora estación por estación** — el CA-01 no se cierra diciendo "se siguió el orden": se anota qué se llamó y qué puerta cerró en cada una, para poder comparar contra el documento.
- **Pedir el salto a propósito** — la conformidad con el orden se prueba pidiendo saltarse una estación, no observando que no se saltó por casualidad.
- **La discrepancia se anota, no se resuelve** — si las trece y las once no coinciden, es un cambio de regla o de procedimiento, y eso pasa por el procedimiento del capítulo `20`.
- **El fallo esperado también es resultado** — el CA-03 ya falló en la práctica. Si vuelve a fallar, lo honesto es escribir **qué le faltó al estado de la fase** para poder retomar (riesgo `R-02`).

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): ninguna suite automática cubre esto. Lo que corre es el procedimiento mismo, sobre el encargo elegido, en rama aparte.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | [CA-01](../HU-007-procedimiento-que-dirige.md#ca-01--llama-a-los-procedimientos-en-orden) | [CP-001](#cp-001--las-estaciones-se-recorren-en-orden-con-bitácora), [CP-002](#cp-002--el-salto-de-estación-no-se-concede) | Funcional | Alta | No | ☐ |
| HU-007 | [CA-02](../HU-007-procedimiento-que-dirige.md#ca-02--se-detiene-donde-aprueba-una-persona) | [CP-003](#cp-003--en-cada-puerta-de-usuario-el-trabajo-se-detiene) | Negativa | Crítica | No | ☐ |
| HU-007 | [CA-03](../HU-007-procedimiento-que-dirige.md#ca-03--el-trabajo-se-retoma-en-otra-sesión-sin-perder-el-hilo) | [CP-004](#cp-004--una-sesión-nueva-retoma-leyendo-solo-el-estado-de-la-fase) | Recuperación | Crítica | No | ☐ |
| HU-007 | RNF — que estaciones y etapas no se contradigan | [CP-005](#cp-005--las-trece-estaciones-contra-las-once-etapas) | Documento | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Las estaciones se recorren en orden, con bitácora

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta: el encargo chico elegido. Rama aparte |
| **Datos de entrada** | El encargo, y la tabla de las trece estaciones |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar la tabla de estaciones antes de empezar | Queda la referencia contra la que se compara |
| 2 | Llevar el encargo por el procedimiento | Avanza estación por estación |
| 3 | En cada estación, anotar qué procedimiento se llamó | Queda la bitácora |
| 4 | En cada estación, anotar qué puerta cerró | Queda con la bitácora |
| 5 | Comparar la bitácora contra la tabla del paso 1 | Mismo orden, ninguna omitida |

**Resultado esperado final:** el orden escrito es el orden que ocurre.

---

### CP-002 — El salto de estación no se concede

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 en curso |
| **Datos de entrada** | Un pedido explícito de saltarse una estación |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir que se salte una estación intermedia | No se salta |
| 2 | Leer la respuesta | Dice por qué, y cita [`02·F15`](../../../../../base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) |
| 3 | Comprobar que el trabajo de esa estación se hizo igual | Se hizo |
| 4 | Pedir reordenar dos estaciones | Tampoco se concede |

**Resultado esperado final:** el orden no depende de que nadie lo empuje.

---

### CP-003 — En cada puerta de usuario, el trabajo se detiene

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | El encargo recorriendo las estaciones |
| **Datos de entrada** | Las puertas que aprueba el usuario, y una respuesta ambigua preparada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar las puertas que aprueba el usuario | Quedan identificadas antes de empezar |
| 2 | Al llegar a cada una, comprobar que el trabajo se detiene | Se detiene en todas |
| 3 | Responder con una frase ambigua en una de ellas | **No habilita**: se vuelve a pedir la aprobación ([`01·C17`](../../../../../base/01-conducta.md)) |
| 4 | Responder afirmativamente | Ahora sí avanza |
| 5 | Comprobar que la aprobación no alcanzó a la puerta siguiente | La siguiente se vuelve a pedir ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)) |

**Resultado esperado final:** las puertas de persona son puertas, no avisos.

> **El paso 4 es el que da valor al 3.** Sin él, el caso pasaría con un procedimiento que nunca avanza.

---

### CP-004 — Una sesión nueva retoma leyendo solo el estado de la fase

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-03 |
| **Tipo** | Recuperación |
| **Prioridad** | Crítica |
| **Precondiciones** | Una fase a medio recorrer, con su estado escrito |
| **Datos de entrada** | El `estado-fase.md` de esa fase, **sin** la conversación |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cerrar la sesión en una puerta intermedia | El estado queda escrito |
| 2 | Abrir una sesión nueva, sin la conversación anterior | Empieza a ciegas |
| 3 | Pedirle que diga en qué estación va y qué falta | Responde leyendo solo el estado |
| 4 | Pedirle que continúe desde ahí | Continúa sin preguntar lo que el documento ya dice |
| 5 | Anotar cada dato que tuvo que preguntar | Cada uno es lo que al estado de la fase le faltó |

**Resultado esperado final:** o el documento alcanza, o queda escrito exactamente qué le falta.

> **El paso 5 convierte el fallo en resultado útil.** Este CA ya falló en la práctica; lo que sirve no es que pase, sino saber qué campo hay que agregar.

---

### CP-005 — Las trece estaciones contra las once etapas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | La tabla del procedimiento y las once etapas de [`02·F15`](../../../../../base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner las dos listas lado a lado | Quedan comparables |
| 2 | Emparejar cada etapa con su estación | Las que emparejan, quedan |
| 3 | Anotar las que no emparejan, en los dos sentidos | Queda la lista de discrepancias |
| 4 | No alinear nada | Alinearlas es cambio de regla o de procedimiento, y pasa por el capítulo `20` |

**Resultado esperado final:** si hay dos verdades sobre el mismo flujo, queda dicho cuáles y dónde.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una puerta de usuario no detenga el trabajo | Inmediato. El CA-02 queda en «No» |
| **Crítica** | Que una respuesta ambigua habilite | Inmediato — es lo que `01·C17` prohíbe |
| **Alta** | Que la sesión nueva no pueda retomar (riesgo `R-02`) | Es el resultado honesto: se escribe qué le faltó al estado de la fase |
| **Media** | Que las trece y las once no coincidan (riesgo `R-01`) | Se anota como hallazgo; alinearlas pasa por el procedimiento del capítulo `20` |
| **Baja** | Que el recorrido consuma más de lo estimado | El encargo se elige chico, con ese límite en mente |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Estaciones recorridas con bitácora | Todas las del encargo |
| Puertas de usuario que no detuvieron | **0** |
| Datos que la sesión nueva tuvo que preguntar | Todos anotados: son el trabajo que sigue |
| Discrepancias entre estaciones y etapas | Todas anotadas, ninguna alineada acá |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
