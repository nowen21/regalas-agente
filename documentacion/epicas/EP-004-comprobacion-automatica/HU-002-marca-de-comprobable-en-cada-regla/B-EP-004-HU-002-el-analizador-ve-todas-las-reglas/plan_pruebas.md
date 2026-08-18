# Plan de Pruebas — Fase B-EP-004-HU-002-el-analizador-ve-todas-las-reglas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso** — y en este molde, eso incluye los **transversales**.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-004-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

**Condición de arranque.** **No se escribe ninguna regla de mentira en `base/`**, ni un minuto: los casos que necesitan una se montan en árboles temporales.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Reconocimiento | Que el analizador vea las tres formas de escribir una regla | Este repositorio | Sí |
| Puerta | Que la regla sin clasificar detenga | Árbol temporal | Sí |
| No regresión | Que las derogadas y la clasificación existente no se muevan | Este repositorio | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El CA-01 y el CA-03 |
| **Negativa** | ☑ | Que lo que **no** es una regla no se cuente |
| **Transversal · Límites** | ☑ | La regla derogada se conserva marcada y no se le exige |
| **Transversal · No regresión** | ☑ | La clasificación existente no se pierde |

### 3.3 Técnicas de diseño de casos

- **El conteo se comprueba contra el árbol real, no contra un número escrito.** Un «200» en una prueba envejece; contar los encabezados de regla del árbol, no.
- **Cada forma de escribir una regla tiene su caso, y cada uno su negativo.** Reconocer viñetas sin caso negativo mete texto que no es una regla.
- **Lo que aparezca sin clasificar se lista, no se arregla.** El caso mide cuántas hay; clasificarlas es de otra HU, y hacerlo de paso convertiría un arreglo en una decisión.
- **La regla de mentira se escribe en un árbol temporal**, nunca en `base/`.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, porque tres clases distintas usan el analizador.

---

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-01](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-01--toda-regla-aparece-clasificada) | [CP-001](#cp-001--el-analizador-ve-las-tres-formas-de-escribir-una-regla), [CP-002](#cp-002--lo-que-no-es-una-regla-no-se-cuenta) | Funcional · Negativa | Crítica | Sí | ☐ |
| HU-002 | [CA-03](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-03--una-regla-nueva-no-se-publica-sin-clasificar) | [CP-003](#cp-003--la-regla-sin-clasificar-detiene) | Funcional | Crítica | Sí | ☐ |
| HU-002 | [CA-02](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-02--la-regla-comprobada-dice-quién-la-comprueba) | [CP-004](#cp-004--lo-que-ya-estaba-clasificado-sigue-estándolo) | Regresión | Alta | Sí | ☐ |
| HU-002 | **Transversal · Límites** | [CP-005](#cp-005--transversal-de-límites-la-derogada-se-conserva-y-no-se-le-exige) | Límites | Crítica | Sí | ☐ |
| HU-002 | **Transversal · No regresión** | [CP-004](#cp-004--lo-que-ya-estaba-clasificado-sigue-estándolo) | Regresión | Crítica | Sí | ☐ |

**Cobertura:** los tres CA y **los dos transversales** = 100%.

---

## 6. Casos de prueba

### CP-001 — El analizador ve las tres formas de escribir una regla

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-002 / CA-01 |
| **Tipo** | Funcional · **Prioridad** Crítica |
| **Precondiciones** | Este repositorio |
| **Datos de entrada** | Las reglas de `base/`, escritas de tres formas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar los encabezados de regla del árbol, por fuera del analizador | Sale un número |
| 2 | Contar lo que el analizador reconoce | **El mismo número** |
| 3 | Comprobar que las cuatro `CQ` del capítulo 16 están | Las cuatro |
| 4 | Comprobar que las sub-reglas de `F12` están | Están |
| 5 | Comprobar que ninguna se cuenta dos veces | Ninguna |

**Resultado esperado final:** lo que está escrito como regla, el programa lo ve.

> **El paso 1 se hace por fuera a propósito.** Comparar el analizador contra un número escrito en la prueba solo dice que el número no cambió; compararlo contra el árbol dice que **ve lo que hay**.

---

### CP-002 — Lo que no es una regla no se cuenta

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-002 / CA-01 |
| **Tipo** | **Negativa** · **Prioridad** Crítica |
| **Precondiciones** | Árbol temporal |
| **Datos de entrada** | Texto que se parece a una regla y no lo es |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un encabezado normal, sin identificador | No se cuenta |
| 2 | Una viñeta que menciona un identificador **en medio de una frase** | No se cuenta |
| 3 | Un identificador dentro de un bloque de código | No se cuenta |
| 4 | Una tabla que nombra identificadores como ejemplo | No se cuenta |
| 5 | Una regla de verdad, en cada una de las tres formas | Se cuentan las tres |

**Resultado esperado final:** ampliar lo que se reconoce no metió ruido.

> **El paso 4 es el que evita repetir un defecto conocido.** `citas.py` cuenta como cita un identificador nombrado como ejemplo — es el [pendiente 55](../../../../../pendientes/55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md). Este analizador no puede caer en lo mismo.

---

### CP-003 — La regla sin clasificar detiene

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-002 / CA-03 |
| **Tipo** | Funcional · **Prioridad** Crítica |
| **Precondiciones** | Árbol temporal con su cuerpo de reglas y su registro |
| **Datos de entrada** | Una regla nueva sin clasificar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir la regla sin clasificarla, **en el árbol temporal** | Queda escrita |
| 2 | Correr `validar.py metareglas` sobre ese árbol | El subcomando **existe** y corre |
| 3 | Mirar la severidad del hallazgo | **Falla**, no aviso |
| 4 | Mirar el código de salida | 1 |
| 5 | Clasificarla y volver a correr | Ya no falla |

**Resultado esperado final:** una regla nueva no se publica sin clasificar, y ahora hay cómo comprobarlo.

> **El paso 2 es la mitad del defecto.** La vigilancia ya existía y funcionaba: lo que no había era forma de correrla.

---

### CP-004 — Lo que ya estaba clasificado sigue estándolo

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-002 / CA-02 y transversal de no regresión |
| **Tipo** | Regresión · **Prioridad** Crítica |
| **Precondiciones** | Este repositorio |
| **Datos de entrada** | El registro de reglas validables |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el analizador con el conjunto ampliado | Corre |
| 2 | Comprobar que ninguna de las que ya estaban clasificadas quedó sin clasificar | Ninguna |
| 3 | **Listar** las que aparecen sin clasificar al verlas por primera vez | Quedan listadas, con su número |
| 4 | Comprobar que no se clasificó ninguna en esta fase | Ninguna |
| 5 | Comprobar que desde el registro se sigue llegando al programa que comprueba | Se llega |

**Resultado esperado final:** ampliar la vista no perdió nada, y lo que apareció quedó a la vista sin resolverse a la carrera.

> **El paso 4 es una decisión, no un olvido.** Decidir si una regla es validable no es trabajo de una fase que arregla un analizador.

---

### CP-005 — Transversal de límites: la derogada se conserva y no se le exige

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-002 / **Transversal · Límites** |
| **Tipo** | Límites · **Prioridad** Crítica |
| **Precondiciones** | Este repositorio, con sus ocho derogaciones |
| **Datos de entrada** | Las ocho |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que las derogadas siguen en el registro, marcadas | Siguen |
| 2 | Comprobar que a ninguna se le reclama clasificación | A ninguna |
| 3 | Comprobar que las cinco `F4.x` —sub-reglas derogadas— **entran** al conjunto ahora | Entran |
| 4 | Comprobar que aun así no se les reclama nada | No se les reclama |
| 5 | Comprobar que el subcomando nuevo tampoco las reclama | Tampoco |

**Resultado esperado final:** ver más reglas no convirtió las derogadas en incumplimientos.

> **El paso 3 y el 4 son el riesgo real de esta fase.** Las cinco `F4.x` estaban invisibles y ahora entran. Si la fila que salta las derogadas no las reconoce, aparecen cinco falsos incumplimientos el mismo día en que la falla empieza a detener.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que las derogadas empiecen a reclamarse (riesgo `R-02`) | Inmediato: con la falla encendida, bloquearía el trabajo |
| **Alta** | Que reconocer viñetas meta texto que no es una regla (riesgo `R-04`) | Se corrige antes de encender la falla |
| **Media** | Que aparezcan muchos hallazgos nuevos del checklist (riesgo `R-01`) | **Es lo que se busca.** Se listan y se decide, sin taparlos |
| **Baja** | Que se escriba una regla de mentira en `base/` | No puede pasar: los casos van en árboles temporales |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los tres CA y **los dos transversales** |
| Casos ejecutados | 5 de 5 |
| Diferencia entre las reglas del árbol y las que el analizador ve | **0** |
| Texto que no es regla contado como regla | **0** |
| Reglas derogadas a las que se les reclama algo | **0** |
| Reglas clasificadas **en esta fase** | **0** — se listan, no se clasifican |
| Reglas de mentira escritas en `base/` | **0** |
| Hallazgos nuevos del checklist al ampliar la vista | Anotados, con su número y su fecha |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
