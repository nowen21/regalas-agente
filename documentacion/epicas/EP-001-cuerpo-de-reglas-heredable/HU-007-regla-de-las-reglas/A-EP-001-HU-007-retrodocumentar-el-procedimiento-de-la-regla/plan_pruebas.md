# Plan de Pruebas — Fase A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Dónde viven las candidatas.** En este documento, no en `base/`. Ninguna regla escrita para probar queda suelta en el cuerpo del estándar.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Recorrido del checklist | Que las veinte filas decidan dónde va, si entra y cómo entra | Este repositorio, rama aparte | No — varias filas piden leer |
| Contraste con reglas reales | Que el criterio que se aplica sea el mismo que ya se aplicó a las reglas vigentes | Este repositorio | No |
| Programa | Lo que `validar.py estandar` sí alcanza a mirar de la forma | Este repositorio | Sí |

**Por qué casi nada se automatiza.** La fila 5 la mira [`validadores/metareglas.py`](../../../../../validadores/metareglas.py), que **no se puede correr** (pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)), y la fila 9 es de las que piden leer: dos exigencias en un mismo texto no se detectan contando palabras.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA, cada uno sobre una candidata |
| Negativa | ☑ | Los CA-02 y CA-03 se prueban con candidatas que **deben** ser rechazadas |
| Documento | ☑ | El molde de [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) sobre cada candidata partida |
| No regresión | ☐ | No aplica: no se edita ninguna regla |

### 3.3 Técnicas de diseño de casos

- **Candidatas reales antes que inventadas** — se usan reglas que ya pasaron por el procedimiento y candidatas que ya se rechazaron. Una regla inventada no trae el defecto real que el procedimiento tiene que atajar. Lo que haya que armar se **marca como armado** (riesgo `R-03`).
- **El par rechazo / aceptación** — en el CA-02 no basta con que la candidata con nombre propio se rechace: su versión agnóstica tiene que pasar. Sin eso, el caso sería compatible con un procedimiento que rechaza todo.
- **Caso real del propio estándar** — el criterio de partición del CA-03 se contrasta con [`F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), que reprueba las filas 8 y 9 por llevar dos exigencias, y con las reglas que salieron de ella.
- **Fila por fila, diciendo cómo se decidió** — el resultado dice cuál se decidió leyendo y cuál no se pudo correr (riesgo `R-02`). Un "checklist aplicado" sin esa distinción se lee como comprobado por programa.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py estandar` y `enlaces` sobre este repositorio. La corrida de `metareglas` se **intenta**, y su silencio es evidencia del CA-02.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | [CA-01](../HU-007-regla-de-las-reglas.md#ca-01--una-regla-nueva-se-enruta-al-capítulo-correcto) | [CP-001](#cp-001--la-regla-existente-cae-en-el-capítulo-dueño-de-su-tema), [CP-002](#cp-002--la-candidata-que-no-era-de-base-se-devuelve-a-su-sitio) | Funcional | Alta | No | ☐ |
| HU-007 | [CA-02](../HU-007-regla-de-las-reglas.md#ca-02--una-regla-atada-a-un-stack-no-entra) | [CP-003](#cp-003--la-candidata-con-nombre-propio-se-rechaza-y-su-versión-agnóstica-pasa) | Negativa | Crítica | No | ☐ |
| HU-007 | [CA-03](../HU-007-regla-de-las-reglas.md#ca-03--una-regla-que-exige-dos-cosas-se-parte-antes-de-entrar) | [CP-004](#cp-004--la-candidata-doble-se-parte-y-las-dos-mitades-pasan-la-fila-9), [CP-005](#cp-005--el-criterio-de-partición-contra-un-caso-real-del-estándar) | Documento | Alta | No | ☐ |
| HU-007 | RNF — que el procedimiento quede citable | [CP-006](#cp-006--lo-rechazado-queda-escrito-con-su-motivo-y-en-su-sitio) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La regla existente cae en el capítulo dueño de su tema

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Una regla vigente del estándar, elegida por tener tema fronterizo entre dos capítulos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la regla y su capítulo actual | Queda a la vista, con su identificador |
| 2 | Recorrer las filas 1 a 4 del [checklist](../../../../../base/20-meta-reglas/checklist.md) sobre ella | Cada fila con su resultado anotado |
| 3 | Comparar el capítulo que sale del recorrido con el que tiene | Coinciden |
| 4 | Si no coinciden, anotarlo como hallazgo sin mover la regla | Queda citable; mover una regla no es de esta fase |

**Resultado esperado final:** el enrutamiento del procedimiento reproduce dónde ya está la regla, o dice exactamente dónde no.

---

### CP-002 — La candidata que no era de `base/` se devuelve a su sitio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta: qué candidatas rechazadas se usan |
| **Datos de entrada** | Una candidata cuyo destino no era `base/` sino `notas/`, `pendientes/` o la capa del proyecto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la candidata tal como se propuso | Queda escrita en este plan, marcada como real o armada |
| 2 | Recorrer las filas 1 a 4 | El recorrido la saca de `base/` |
| 3 | Leer a qué sitio la manda | Nombra uno concreto, no "otro lado" ([`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)) |
| 4 | Comprobar que no quedó escrita en `base/` | `base/` sin cambios |

**Resultado esperado final:** el procedimiento no solo rechaza: enruta.

---

### CP-003 — La candidata con nombre propio se rechaza, y su versión agnóstica pasa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Una candidata que nombra lenguaje, framework o herramienta, y la misma exigencia reescrita sin nombrarlos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aplicar la fila 5 a la candidata con nombre propio | Se rechaza, y el motivo cita [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) |
| 2 | Aplicar la fila 5 a la versión agnóstica | Pasa |
| 3 | Intentar correr el programa que mira la fila 5 | No hay punto de entrada; queda la evidencia de la corrida en silencio |
| 4 | Dejar escrito que la fila 5 se decidió leyendo, y con qué evidencia | Queda dicho en el resultado |

**Resultado esperado final:** el stack no entra a `base/`, y queda claro que hoy eso lo sostiene una lectura, no un programa.

> **El paso 2 es el que da valor al 1.** Sin él, el caso pasaría también con un procedimiento que rechaza toda candidata.

---

### CP-004 — La candidata doble se parte, y las dos mitades pasan la fila 9

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-03 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta |
| **Datos de entrada** | Una candidata que exige dos cosas que se cumplen por separado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aplicar la fila 9 a la candidata entera | Reprueba, y el motivo dice cuáles son las dos exigencias |
| 2 | Partirla en dos, cada una con su título y su cuerpo | Quedan dos candidatas |
| 3 | Aplicar la fila 9 a cada una | Las dos pasan |
| 4 | Comprobar que cada una llevaría identificador propio | Ninguna reutiliza el de la otra ([`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)) |

**Resultado esperado final:** la partición no es una opinión: la decide la fila 9, antes de que la regla entre.

---

### CP-005 — El criterio de partición contra un caso real del estándar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-03 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | [`F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) y las reglas que salieron de ella |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el bloque de checklist de `F4` | Reprueba las filas 8 y 9, y dice por qué |
| 2 | Aplicar el mismo criterio del CP-004 a `F4` | Da el mismo veredicto que el bloque ya escrito |
| 3 | Anotar la diferencia si no coincide | Queda como hallazgo, sin tocar `F4` |

**Resultado esperado final:** el criterio de partición que se usa es el mismo que el estándar ya se aplicó a sí mismo.

> **Esto es triangulación** ([`08·T7`](../../../../../base/08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos)): el resultado esperado no sale del criterio que se está probando, sino de un veredicto escrito antes y por otra razón.

---

### CP-006 — Lo rechazado queda escrito, con su motivo y en su sitio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / RNF |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | Los CP-002, CP-003 y CP-004 corridos |
| **Datos de entrada** | Las candidatas rechazadas del recorrido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir cada candidata rechazada en `notas/`, con su motivo | Queda una nota, no una sección dentro de `base/` |
| 2 | Comprobar que `base/` no tiene ninguna sección de rechazadas | `base/` es lo que se exige, nada más |
| 3 | Correr `validar.py estandar` y `enlaces` | Sin fallas nuevas |

**Resultado esperado final:** por qué algo no entró queda recuperable, y en el sitio que le toca ([`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)).

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una candidata con nombre propio pase la fila 5 | Inmediato. El CA queda en «No» |
| **Alta** | Que al recorrer el checklist sobre una regla vigente resulte que reprueba (riesgo `R-01`) | Se anota como evidencia y se suma al pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Corregir la regla no es de esta fase |
| **Media** | Que el enrutamiento mande una regla vigente a otro capítulo | Se anota; mover una regla lo decide el usuario |
| **Baja** | Que no se recuerden candidatas rechazadas y haya que armarlas (riesgo `R-03`) | Se admite: la armada se marca como tal |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 6 de 6 |
| Candidatas de mentira que quedan en `base/` | **0** |
| Filas del checklist con su forma de decisión declarada | Todas las que se apliquen |
| Candidatas rechazadas escritas en `notas/` con su motivo | Todas las que salgan |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
