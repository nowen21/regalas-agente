# Plan de Pruebas — Fase A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que el código de salida sea 0 con solo avisos y 1 con una falla | Hallazgos armados en memoria | Sí |
| Salida real | Que cada hallazgo traiga archivo, línea y regla | Corrida real sobre este repositorio | No |
| Uso | Que se pueda arreglar el defecto sin abrir el programa que lo reportó | Este repositorio | No |

**Por qué el código de salida se prueba con hallazgos armados.** Así la prueba no depende de que exista un archivo roto en el repositorio: si mañana se arregla, la prueba seguiría sirviendo.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | Corrida sin hallazgos, y corrida con aviso y falla mezclados |
| Usabilidad | ☑ | El CA-01: arreglar sin abrir el programa |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Prueba de uso, no de forma** — el CA-01 no se cierra contando que el hallazgo trae tres campos: se cierra **arreglando dos defectos** con lo que el hallazgo dice y sin abrir el código del validador. Es la única forma de saber si alcanza.
- **Los tres datos son sí o no; la redacción no** — se prueba que archivo, línea y regla estén. Que el texto esté bien redactado es criterio y no lo decide un programa.
- **El recorrido incluye a los validadores futuros** — el caso del CA-01 recorre **todos** los hallazgos de la corrida, no una lista fija. Un validador nuevo entra solo, y el contrato escrito no se queda viejo (riesgo `R-03`).
- **La mezcla** — el caso de límites corre con avisos **y** una falla a la vez: el código de salida tiene que ser 1, no 0 por mayoría de avisos.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, y una corrida completa de `validar.py` sobre este repositorio para tomar los hallazgos reales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-01](../HU-003-formato-del-hallazgo.md#ca-01--el-hallazgo-alcanza-para-arreglar-sin-abrir-el-programa) | [CP-001](#cp-001--cada-hallazgo-de-la-corrida-trae-archivo-línea-y-regla), [CP-002](#cp-002--dos-defectos-se-arreglan-sin-abrir-el-programa) | Usabilidad | Crítica | No | ☐ |
| HU-003 | [CA-02](../HU-003-formato-del-hallazgo.md#ca-02--lo-dudoso-sale-como-aviso-y-no-detiene) | [CP-003](#cp-003--con-solo-avisos-el-código-de-salida-es-0) | Funcional | Alta | Sí | ☐ |
| HU-003 | [CA-03](../HU-003-formato-del-hallazgo.md#ca-03--una-falla-detiene) | [CP-004](#cp-004--con-una-falla-el-código-de-salida-es-1-aunque-haya-avisos) | Funcional | Alta | Sí | ☐ |
| HU-003 | RNF — que el contrato de la salida quede escrito | [CP-001](#cp-001--cada-hallazgo-de-la-corrida-trae-archivo-línea-y-regla) | Documento | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cada hallazgo de la corrida trae archivo, línea y regla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 y RNF |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los hallazgos de una corrida completa sobre este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación completa y guardar la salida | Queda la corrida, con cuántos hallazgos dio y de qué día |
| 2 | Tomar al menos diez hallazgos, de subcomandos distintos | Quedan elegidos, con su subcomando |
| 3 | Por cada uno, comprobar que trae archivo | Todos |
| 4 | Por cada uno, comprobar que trae línea | Todos, o se anota el subcomando que no la da |
| 5 | Por cada uno, comprobar que cita la regla incumplida | Todos |
| 6 | Recorrer **todos** los hallazgos, no solo los diez | Ningún subcomando queda sin revisar |

**Resultado esperado final:** el contrato de la salida vale para los 24 subcomandos, y para el que se agregue después.

> **El paso 6 es lo que evita que el contrato escrito se quede viejo.** Un validador nuevo entra al recorrido solo.

---

### CP-002 — Dos defectos se arreglan sin abrir el programa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Tipo** | Usabilidad |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Dos hallazgos reales de subcomandos distintos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar el primer hallazgo y **no** abrir el validador que lo reportó | Solo se lee la línea de salida |
| 2 | Arreglar el defecto con lo que la línea dice | Se puede arreglar |
| 3 | Volver a correr y comprobar que el hallazgo desapareció | Desapareció |
| 4 | Repetir los tres pasos con el segundo hallazgo, de otro subcomando | Mismo resultado |
| 5 | Anotar cada vez que hizo falta abrir el programa | Cada una es una carencia del formato |

**Resultado esperado final:** el hallazgo alcanza, o queda escrito exactamente dónde no alcanza.

---

### CP-003 — Con solo avisos, el código de salida es 0

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El número de pruebas de la suite anotado antes |
| **Datos de entrada** | Hallazgos armados en memoria, todos de severidad aviso |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar una corrida con solo avisos | Queda armada |
| 2 | Comprobar el código de salida | Es 0 |
| 3 | Comprobar que los avisos **sí** se muestran | Se muestran: no detener no es callar |
| 4 | Comprobar una corrida sin ningún hallazgo | También 0 |

**Resultado esperado final:** lo dudoso se dice y no frena.

> **El paso 3 es el que separa "no detiene" de "no se ve".** Un aviso que no se imprime cumpliría el código de salida y no cumpliría el CA.

---

### CP-004 — Con una falla, el código de salida es 1, aunque haya avisos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-003 corrido |
| **Datos de entrada** | Hallazgos armados: una falla sola, y una falla mezclada con varios avisos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar una corrida con una sola falla | Código de salida 1 |
| 2 | Armar una con una falla y varios avisos | Código de salida 1 |
| 3 | Comprobar que los avisos siguen mostrándose en ese caso | Se muestran |
| 4 | Correr la suite completa y comparar contra la línea base | Ninguna prueba que pasaba, falla |

**Resultado esperado final:** una falla detiene, y no la diluye la mayoría de avisos.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una falla no detenga la corrida | Inmediato. El CA-03 queda en «No» |
| **Alta** | Que haga falta abrir el validador para entender un hallazgo | Se anota como carencia del formato, con el subcomando |
| **Media** | Que algún validador reporte sin línea (riesgo `R-01`) | Se anota con el validador y la corrida. Corregirlo es de su propia fase |
| **Media** | Que la suite esté roja por trabajo ajeno (riesgo `R-02`) | Se anota el estado antes de tocarla y se compara |
| **Baja** | Redacción del texto del hallazgo | No es de esta fase: se prueban los tres datos, no la redacción |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Subcomandos revisados en la corrida | Todos los que produjeron hallazgos |
| Hallazgos sin archivo, sin línea o sin regla | **0**, o todos anotados con su subcomando |
| Veces que hizo falta abrir el programa para arreglar | **0** |
| Pruebas de la suite | Las de la línea base, más 2, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
