# Plan de Pruebas — Fase A-EP-005-HU-006-la-bateria-antes-de-publicar   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-006 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-006-la-bateria-antes-de-publicar` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**La batería niega el visto bueno; no bloquea nada.** Publicar lo autoriza y lo corre una persona ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)). Un programa que dijera que bloquea lo que no controla estaría mintiendo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Que al pedir publicar corra la batería y su resultado quede escrito | Carpeta temporal | Sí |
| Veredicto | Que una falla niegue el visto bueno y un aviso no | Carpeta temporal | Sí |
| Legibilidad | Que el veredicto diga qué falló y qué se saltó | Carpeta temporal | No |

**De qué depende esta fase.** De que exista la corrida completa de [EP-004 · HU-008](../../../EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md). Rearmarla acá daría dos formas de correr todo y dos verdades.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Negativa | ☑ | El CA-02: la falla niega el visto bueno |
| Límites | ☑ | Aviso solo, y comprobaciones salteadas |
| Legibilidad | ☑ | El veredicto que se puede accionar |

### 3.3 Técnicas de diseño de casos

- **El par falla / aviso** — con solo la falla, el caso pasaría con una batería que niega el visto bueno siempre.
- **El veredicto se lee, no se cuenta** — un "no" sin motivo se ignora o se fuerza. El caso comprueba que el veredicto diga **qué falló** y **qué se saltó**.
- **El texto dice quién publica** — el riesgo `R-02`: el veredicto no puede redactarse como si el programa hubiera bloqueado la publicación. Se comprueba leyendo el texto.
- **Lo lento se hereda** — el riesgo `R-01`: la separación de las comprobaciones lentas la decide la fase de EP-004 · HU-008. Acá no se inventa otra.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y los casos en carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | [CA-01](../HU-006-bateria-antes-de-publicar.md#ca-01--antes-de-publicar-corre-todo) | [CP-001](#cp-001--al-pedir-publicar-la-batería-corre-y-su-resultado-queda-escrito) | Integración | Crítica | Sí | ☐ |
| HU-006 | [CA-02](../HU-006-bateria-antes-de-publicar.md#ca-02--un-incumplimiento-claro-detiene-la-publicación) | [CP-002](#cp-002--la-falla-niega-el-visto-bueno-y-el-aviso-no), [CP-003](#cp-003--el-veredicto-dice-qué-falló-y-qué-se-salteó) | Negativa | Crítica | Sí | ☐ |
| HU-006 | RNF — que el paso no se saltee | [CP-001](#cp-001--al-pedir-publicar-la-batería-corre-y-su-resultado-queda-escrito) | Integración | Alta | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Al pedir publicar, la batería corre y su resultado queda escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 y RNF |
| **Tipo** | Integración |
| **Prioridad** | Crítica |
| **Precondiciones** | Dudas 1 y 2 resueltas: si se espera a la corrida completa, y qué cuenta como publicar |
| **Datos de entrada** | Un proyecto de prueba en carpeta temporal, sin fallas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir publicar | La batería corre sola, sin que nadie la llame |
| 2 | Comprobar que corrió lo que aplica al proyecto | Todo lo que aplica, según lo que decidió la duda 1 |
| 3 | Comprobar que el resultado quedó escrito | Queda, con su fecha |
| 4 | Pedir publicar otra vez sin cambiar nada | Vuelve a correr: el paso no se saltea |
| 5 | Comprobar cuánto tardó | Se anota, para decidir si es vivible |

**Resultado esperado final:** el paso existe y deja rastro.

---

### CP-002 — La falla niega el visto bueno, y el aviso no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un proyecto con una falla, y otro con solo avisos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir publicar con una falla presente | El veredicto es que **no** se puede publicar |
| 2 | Pedir publicar con solo avisos | El veredicto **sí** habilita, y los avisos se muestran |
| 3 | Comparar los dos veredictos | La diferencia es la severidad, no la cantidad |
| 4 | Arreglar la falla y volver a pedir | Ahora habilita |

**Resultado esperado final:** lo dudoso no frena y lo claro sí, que es lo que la HU pide.

> **El paso 2 es el que da valor al 1.** Sin él, el caso pasaría con una batería que niega siempre.

---

### CP-003 — El veredicto dice qué falló y qué se salteó

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Legibilidad |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-002 corrido |
| **Datos de entrada** | El texto del veredicto en los dos casos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el veredicto que niega | Nombra qué falló, no solo que falló algo |
| 2 | Comprobar que dice qué comprobaciones se saltearon y por qué | Lo dice |
| 3 | Comprobar que con eso alcanza para arreglar | Alcanza, sin abrir el programa |
| 4 | Comprobar que el texto **no** dice que bloqueó la publicación | Dice que niega el visto bueno; publicar lo hace una persona |

**Resultado esperado final:** el veredicto se puede accionar, y no se atribuye un poder que no tiene.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una falla no niegue el visto bueno | Inmediato. El CA-02 queda en «No» |
| **Alta** | Que un aviso niegue el visto bueno | Inmediato — la batería se volvería un obstáculo y se saltearía |
| **Alta** | Que la batería tarde tanto que se saltee siempre (riesgo `R-01`) | Se hereda la separación de lo lento de [EP-004 · HU-008](../../../EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md) |
| **Media** | Que el veredicto se lea como que el programa bloqueó (riesgo `R-02`) | Se corrige el texto: niega el visto bueno |
| **Media** | Que la fase se construya antes de la corrida completa (riesgo `R-03`) | Es la duda 1 |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 3 de 3 |
| Veces que el paso se salteó | **0** |
| Avisos que niegan el visto bueno | **0** |
| Veredictos sin motivo accionable | **0** |
| Tiempo de la batería | Anotado, para decidir si es vivible |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
