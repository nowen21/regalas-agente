# Plan de Pruebas — Fase A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-001 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Ninguna regla se reclasifica acá.** Reclasificar cambia lo que se exige comprobar, y eso lo decide el usuario. Lo que aparezca mal clasificado se anota.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Aplicación del criterio | Que el criterio, aplicado a reglas reales, dé el mismo veredicto que el registro | Lectura de este repositorio | No |
| Partición | Que una regla comprobable a medias se pueda partir con el criterio en la mano | Lectura | No |
| Conteo | Que quede la cuenta por categoría, con fecha | Lectura | Parcial |

**Con qué reglas se prueba.** Con reglas **reales** de cada clase. Una regla inventada no discute, y el CA-02 necesita justamente una sobre la que dos personas puedan discutir de verdad.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Documento | ☑ | Los tres CA |
| Negativa | ☑ | El CA-02: la regla que se discute tiene que quedar **afuera** |
| Límites | ☑ | El CA-03: las reglas marcadas como difusas o pesadas |
| No regresión | ☐ | No aplica: la fase no cambia comportamiento |

### 3.3 Técnicas de diseño de casos

- **Triangulación contra la clasificación ya hecha** — el resultado esperado no sale del criterio que se está probando: sale del registro, que clasificó las reglas antes y por otra razón. Si el criterio aplicado hoy da otro veredicto, uno de los dos está mal, y eso es hallazgo.
- **La regla difusa como prueba del criterio** — el riesgo `R-02`: si con el criterio en la mano **no se puede** partir una regla difusa en su mitad comprobable y su mitad humana, al criterio le falta texto. El CA-03 es la prueba del propio criterio.
- **Conteo con fecha** — la cuenta por categoría se anota con el día, para que la comparación futura tenga contra qué medirse.
- **Hallazgo anotado, clasificación intacta** — arriba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py estandar` y `enlaces` sobre este repositorio, si `M9` cambia de texto. Lo demás es lectura.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | [CA-01](../HU-001-criterio-de-lo-comprobable.md#ca-01--el-criterio-existe-y-se-puede-citar) | [CP-001](#cp-001--el-criterio-se-cita-desde-otro-documento-por-su-identificador) | Documento | Alta | Parcial | ☐ |
| HU-001 | [CA-02](../HU-001-criterio-de-lo-comprobable.md#ca-02--una-regla-que-se-discute-queda-afuera) | [CP-002](#cp-002--tres-reglas-de-criterio-humano-quedan-afuera-y-tres-validables-quedan-adentro) | Negativa | Alta | No | ☐ |
| HU-001 | [CA-03](../HU-001-criterio-de-lo-comprobable.md#ca-03--una-regla-comprobable-a-medias-se-parte) | [CP-003](#cp-003--las-reglas-difusas-se-parten-con-el-criterio-en-la-mano) | Límites | Crítica | No | ☐ |
| HU-001 | RNF — que la clasificación no se vuelva a perder | [CP-004](#cp-004--la-cuenta-por-categoría-queda-anotada-con-su-fecha) | Documento | Media | Parcial | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El criterio se cita desde otro documento por su identificador

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta: dónde vive el criterio |
| **Datos de entrada** | [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) y [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar el criterio en el sitio que decidió la duda 1 | Está, escrito una sola vez |
| 2 | Comprobar que el otro documento lo **enlaza** y no lo copia | Lo enlaza ([`20·M15`](../../../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md)) |
| 3 | Comprobar que se puede citar por identificador desde una fase | Se puede |
| 4 | Correr `validar.py enlaces` | Ningún enlace roto |
| 5 | Si el criterio quedó en `validadores/`, comprobar si viaja a un proyecto heredero | Queda dicho si viaja o no |

**Resultado esperado final:** el criterio se cita, y queda claro si lo hereda un proyecto o es solo de esta casa.

> **El paso 5 es la carencia que el CA-01 tiene hoy.** El criterio existe, pero vive donde no se hereda.

---

### CP-002 — Tres reglas de criterio humano quedan afuera, y tres validables quedan adentro

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Tres reglas clasificadas como criterio humano y tres como validables, **reales** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar el criterio y las seis reglas | Quedan a la vista, con su clasificación actual |
| 2 | Aplicar el criterio a las tres humanas, sin mirar su clasificación | Las tres quedan afuera |
| 3 | Aplicarlo a las tres validables | Las tres quedan adentro |
| 4 | Comparar los seis veredictos contra el registro | Coinciden los seis |
| 5 | Anotar la que no coincida, sin reclasificarla | Queda como hallazgo |

**Resultado esperado final:** el criterio reproduce la clasificación que ya se hizo, o dice exactamente dónde no.

> **El paso 3 es el que da valor al 2.** Sin él, el caso pasaría con un criterio que deja todo afuera.

---

### CP-003 — Las reglas difusas se parten con el criterio en la mano

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-03 |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Las reglas que el registro marca como difusas o pesadas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar cada una y su marca | Quedan a la vista |
| 2 | Con el criterio, decir qué mitad se comprueba con un programa | Sale una respuesta concreta |
| 3 | Decir qué mitad se queda en el documento | Sale una respuesta concreta |
| 4 | Anotar la que no se pueda partir | **Es hallazgo del criterio, no de la regla**: le falta texto |
| 5 | No partir ninguna regla | Partirla es decisión del usuario |

**Resultado esperado final:** el criterio sirve para decidir, o queda dicho que no alcanza.

> **Este caso prueba el criterio, no las reglas.** Si con el criterio no se puede partir una regla difusa, el defecto está en el criterio (riesgo `R-02`).

---

### CP-004 — La cuenta por categoría queda anotada, con su fecha

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | El registro [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar las reglas por categoría | Sale un número por cada una |
| 2 | Anotar la fecha de la cuenta | Queda escrita junto a los números |
| 3 | Comprobar que la suma es el total de reglas del cuerpo | Coinciden |
| 4 | Anotar la diferencia si no coinciden | Queda como hallazgo |

**Resultado esperado final:** hay contra qué comparar la próxima vez que alguien pregunte si la clasificación se perdió.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que con el criterio no se pueda partir una regla difusa (riesgo `R-02`) | Inmediato. El criterio quedaría vacío y volvería a decidirse a ojo |
| **Alta** | Que el criterio aplicado dé otro veredicto que el registro (riesgo `R-01`) | Se anota y se suma al pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Reclasificar lo decide el usuario |
| **Media** | Que el criterio siga sin viajar a un proyecto heredero | Es la duda 1: se resuelve antes de escribir |
| **Baja** | Que la suma por categoría no dé el total del cuerpo | Se anota con la diferencia |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Reglas reclasificadas en esta fase | **0** |
| Veredictos que coinciden con el registro | 6 de 6, o los que no, anotados |
| Reglas difusas que no se pudieron partir | **0** — cada una es un hueco del criterio |
| Copias del criterio en el repositorio | **1** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
