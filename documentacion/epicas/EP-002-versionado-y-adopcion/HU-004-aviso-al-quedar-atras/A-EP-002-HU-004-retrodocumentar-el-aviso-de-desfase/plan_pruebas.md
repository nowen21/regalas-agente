# Plan de Pruebas — Fase A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-002-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**El texto del mensaje no cambia acá.** Completarlo es la duda 1 del plan, y cambia lo que el usuario ve en cada apertura de sesión: se propone y se decide, no se hace de oficio.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que `comparar` decida bien el desfase en los tres estados | En memoria — la función no toca disco | Sí |
| Integración | Que con desfase el trabajo siga, y que con derogación sin adoptar se detenga | Carpeta temporal con proyectos de mentira | Sí |
| Legibilidad | Que el aviso salga una vez por apertura y no en cada mensaje | Este repositorio | No |

**Por qué las pruebas van contra `comparar` y no contra el enganche entero.** `comparar` está aislado de disco a propósito: probarlo ahí no obliga a montar un proyecto, y los tres estados —atrasado, al día, sin versión declarada— son aritmética pura.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | Sin `CLAUDE.md`, y con `CLAUDE.md` sin versión declarada |
| Negativa | ☑ | El CA-02: al día, **no** sale nada |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Partición por estado del proyecto** — atrasado, al día, y sin versión declarada. Los tres se prueban; el tercero es el que más se olvida y el que más rompe.
- **El par que separa el CA-03 de su excepción** — con desfase simple el trabajo **sigue**; con una derogación dentro del desfase, **se detiene** ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)). Sin los dos casos, la HU y la regla se leen como contradicción.
- **Comprobar que no migró** — el CA-03 no se cierra leyendo la respuesta: se cierra comparando los archivos del proyecto contra su línea base. Avisar no es actualizar.
- **La carencia se documenta, no se corrige** — el mensaje no dice qué cambió entre las dos versiones. Eso queda escrito con lo que costaría cada opción, para que el usuario decida.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y `validar.py version` sobre los proyectos temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | [CA-01](../HU-004-aviso-al-quedar-atras.md#ca-01--el-proyecto-atrasado-recibe-el-aviso-al-abrir-sesión) | [CP-001](#cp-001--el-proyecto-atrasado-recibe-el-aviso-con-las-dos-versiones) | Funcional | Alta | Sí | ☐ |
| HU-004 | [CA-02](../HU-004-aviso-al-quedar-atras.md#ca-02--el-proyecto-al-día-no-recibe-nada) | [CP-002](#cp-002--al-día-no-sale-nada-y-sin-versión-declarada-sale-otro-aviso) | Negativa | Alta | Sí | ☐ |
| HU-004 | [CA-03](../HU-004-aviso-al-quedar-atras.md#ca-03--el-aviso-no-migra-ni-detiene) | [CP-003](#cp-003--con-desfase-el-trabajo-sigue-y-nada-se-actualiza-solo), [CP-004](#cp-004--con-una-derogación-sin-adoptar-la-fase-sí-se-detiene) | Límites | Crítica | Sí | ☐ |
| HU-004 | RNF — que el aviso no se vuelva ruido | [CP-005](#cp-005--el-aviso-sale-una-vez-por-apertura) | Legibilidad | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El proyecto atrasado recibe el aviso, con las dos versiones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna: `comparar` no toca disco |
| **Datos de entrada** | Una versión declarada menor que la vigente |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Llamar a `comparar` con la declarada menor que la vigente | Devuelve motivo |
| 2 | Leer el motivo | Nombra la versión declarada y la vigente |
| 3 | Buscar en el motivo qué cambió entre las dos | **No lo dice** — queda anotado como la carencia del CA-01 |
| 4 | Dejar escrita la duda 1, con lo que costaría cada opción | Queda para que el usuario decida |

**Resultado esperado final:** el aviso sale, y queda dicho exactamente qué le falta.

> **El paso 3 es una carencia esperada, no un fallo del caso.** Escribirlo así evita que el hueco se lea como defecto de esta fase.

---

### CP-002 — Al día no sale nada, y sin versión declarada sale otro aviso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Tres estados: al día, atrasado y sin versión declarada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Llamar a `comparar` con la versión al día | No devuelve nada |
| 2 | Llamar con la atrasada | Devuelve motivo: la diferencia es el estado, no que la función calle siempre |
| 3 | Llamar sin versión declarada | Devuelve el aviso de que falta fijarla, no un error |
| 4 | Correr sobre un proyecto sin `CLAUDE.md` | Lista vacía, sin excepción |

**Resultado esperado final:** el proyecto al día trabaja en silencio, y lo que no se puede decidir no se inventa.

> **El paso 2 es el que da valor al 1.** Sin él, el caso pasaría con una función que devuelve vacío siempre.

---

### CP-003 — Con desfase, el trabajo sigue y nada se actualiza solo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Un proyecto de mentira en carpeta temporal, atrasado y **sin** derogaciones en el tramo |
| **Datos de entrada** | El proyecto y su listado de archivos anotado antes |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el estado de los archivos del proyecto | Queda la línea base |
| 2 | Abrir sesión sobre él | Sale el aviso de desfase |
| 3 | Pedir un trabajo cualquiera | Se hace: el aviso no detiene |
| 4 | Comparar los archivos contra la línea base | Ninguno se actualizó solo: el aviso no migra |

**Resultado esperado final:** avisar no es actualizar, y avisar no es frenar.

---

### CP-004 — Con una derogación sin adoptar, la fase sí se detiene

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-03 — excepción |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | El estándar tiene al menos una regla derogada; el proyecto declara una versión anterior a ella y tiene una carpeta de fase |
| **Datos de entrada** | El mismo proyecto del CP-003, con la versión declarada movida hacia atrás |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que hay derogaciones en el tramo | Las hay; si no, el caso falla acá y lo dice |
| 2 | Correr el recorrido de flujo sobre el proyecto | La fase **sí** se detiene ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) |
| 3 | Comparar con el resultado del CP-003 | La diferencia es la derogación, no el desfase |
| 4 | Comprobar que la excepción quedó escrita en el CA-03 de la HU | Con su enlace a `F22` |

**Resultado esperado final:** la HU y la regla dejan de leerse como contradicción.

---

### CP-005 — El aviso sale una vez por apertura

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / RNF |
| **Tipo** | Legibilidad |
| **Prioridad** | Media |
| **Precondiciones** | Un proyecto atrasado en carpeta temporal |
| **Datos de entrada** | Una sesión con varios mensajes |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir sesión sobre el proyecto atrasado | Sale el aviso una vez |
| 2 | Mandar varios mensajes seguidos | No vuelve a salir |
| 3 | Cerrar y volver a abrir | Sale otra vez, una sola |

**Resultado esperado final:** un aviso que se repite deja de leerse, y esta regla existe para que se lea.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el aviso actualice algo del proyecto por su cuenta | Inmediato. El CA-03 queda en «No» |
| **Alta** | Que un proyecto al día reciba el aviso | Inmediato — el aviso se vuelve ruido y deja de leerse |
| **Media** | Que el aviso siga sin decir qué cambió entre las dos versiones | Se documenta con la duda 1. Cambiarlo lo decide el usuario |
| **Media** | Que completar el mensaje rompa pruebas que citan su texto (riesgo `R-01`) | Solo se toca con la duda resuelta y el plan ampliado |
| **Baja** | Repeticiones del aviso dentro de la misma sesión | Antes de cerrar |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Archivos del proyecto de prueba actualizados por el aviso | **0** |
| Estados del proyecto probados | 4: al día, atrasado, sin versión declarada y sin `CLAUDE.md` |
| Veces que sale el aviso por apertura | 1 |
| Pruebas de la suite | Las de la línea base, más las nuevas, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
