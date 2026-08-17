# Plan de Pruebas — Fase A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Condición de arranque, no negociable.** El instalador **escribe archivos**. Todas las corridas van sobre proyectos de prueba en carpetas temporales: correrlo sobre un proyecto vivo es tocar trabajo ajeno.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Bitácora | Qué dice el instalador y **en qué momento** lo dice | Proyecto de prueba en carpeta temporal | No |
| Vista previa | Si existe una forma de ver el plan sin ejecutarlo | Carpeta temporal | Sí |
| Autorización | Qué escribe y qué pide antes de escribir | Carpeta temporal | Sí |

**Se mide antes de proponer.** Ya pasó en esta casa que una HU nació pidiendo algo que ya existía y hubo que recortarla el mismo día. El CA-01 se establece observando, no suponiendo.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Observación | ☑ | El CA-01: qué dice y cuándo |
| Funcional | ☑ | El CA-02: nada se toca sin autorización |
| Límites | ☑ | Instalación cancelada a mitad de camino |
| Seguridad | ☑ | Que no escriba fuera de la carpeta de destino |

### 3.3 Técnicas de diseño de casos

- **Se anota el momento, no solo el texto** — la diferencia entre cumplir el CA-01 y no cumplirlo es **cuándo** se dice: antes de tocar, o mientras se toca. La bitácora registra las dos cosas en orden.
- **El listado de archivos antes y después** — la forma de saber qué escribió el instalador es comparar el árbol contra su estado inicial, no leer lo que el instalador dice que hizo.
- **La cancelación como caso** — si se corta la instalación en el punto donde pide autorización, no debería quedar nada escrito. Es lo que distingue "avisa" de "avisa y espera".
- **La propuesta se escribe como propuesta** — el riesgo `R-03`: si falta la vista previa, se propone con su costo. Este es el programa que modifica **otros** proyectos: cambiarlo se aprueba aparte.
- **Que el CA-01 resulte cumplido también es resultado** — el riesgo `R-01`: queda escrito qué muestra y en qué momento, y eso hoy no está en ninguna parte.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y el instalador sobre carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-01](../HU-002-mostrar-antes-de-hacer.md#ca-01--antes-de-tocar-nada-dice-qué-va-a-hacer) | [CP-001](#cp-001--bitácora-de-la-corrida-qué-dice-y-en-qué-momento), [CP-002](#cp-002--existe-una-forma-de-ver-el-plan-sin-ejecutarlo) | Observación | Crítica | Parcial | ☐ |
| HU-002 | [CA-02](../HU-002-mostrar-antes-de-hacer.md#ca-02--nada-se-toca-sin-autorización) | [CP-003](#cp-003--qué-se-escribe-y-qué-se-pide-antes), [CP-004](#cp-004--cancelar-en-la-autorización-no-deja-nada-escrito) | Funcional | Crítica | Sí | ☐ |
| HU-002 | RNF — que se pueda saber qué va a pasar antes de que pase | [CP-002](#cp-002--existe-una-forma-de-ver-el-plan-sin-ejecutarlo) | Observación | Alta | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Bitácora de la corrida: qué dice y en qué momento

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Observación |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal con un proyecto de prueba, y su árbol anotado antes |
| **Datos de entrada** | El instalador corrido sobre esa carpeta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el árbol del proyecto antes de correr | Queda la línea base |
| 2 | Correr el instalador y anotar cada cosa que dice, en orden | Queda la bitácora |
| 3 | Anotar, entre esas líneas, en qué punto empezó a escribir | Queda marcado el momento |
| 4 | Comparar: ¿lo que dice está **antes** de escribir, o mientras escribe? | Sale el veredicto del CA-01 |
| 5 | Comparar el árbol contra la línea base | Se ve qué escribió de verdad, no lo que dijo |

**Resultado esperado final:** queda escrito qué muestra el instalador y en qué momento, que hoy no está en ninguna parte.

> **El paso 5 no confía en lo que el programa dice.** Lo que escribió se mide sobre el árbol.

---

### CP-002 — ¿Existe una forma de ver el plan sin ejecutarlo?

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 y RNF |
| **Tipo** | Observación |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal, con su árbol anotado |
| **Datos de entrada** | El instalador, con las formas de invocarlo que ofrezca |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar cómo se puede invocar el instalador | Queda el listado de formas |
| 2 | Buscar una que muestre el plan sin escribir | Se anota si la hay |
| 3 | Si la hay, correrla y comparar el árbol contra la línea base | **Nada escrito** |
| 4 | Comparar lo que anunció con lo que después escribe de verdad al ejecutar | Coincide |
| 5 | Si no la hay, anotarlo y proponerla con su costo | Queda como propuesta, no como decisión |

**Resultado esperado final:** o existe la vista previa y es fiel, o queda dicho que no existe y qué costaría.

> **El paso 4 es lo que hace útil una vista previa.** Una que anuncie algo distinto de lo que hace es peor que ninguna.

---

### CP-003 — Qué se escribe y qué se pide antes

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal, con su árbol anotado |
| **Datos de entrada** | Un proyecto de prueba, y otro con archivos previos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el instalador y anotar cada punto en que pide autorización | Queda el listado |
| 2 | Comparar el árbol antes y después | Se ve exactamente qué archivos escribió |
| 3 | Comprobar que cada escritura tiene su autorización previa | Cada una, o se anota cuál no la tuvo |
| 4 | Comprobar que **no escribió fuera** de la carpeta de destino | Ningún archivo afuera |
| 5 | Comprobar que la carpeta temporal quedó contenida | Contenida |

**Resultado esperado final:** [`00·N1`](../../../../../base/00-nucleo-blindado.md#n1--no-ejecutar-sin-validación-blindada) queda comprobado sobre el programa que modifica otros proyectos.

---

### CP-004 — Cancelar en la autorización no deja nada escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-003 corrido, con el punto de autorización identificado |
| **Datos de entrada** | Una corrida cancelada en ese punto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el instalador hasta el punto donde pide autorización | Se detiene ahí |
| 2 | Cancelar | Termina |
| 3 | Comparar el árbol contra la línea base | **Nada escrito** |
| 4 | Si algo se escribió antes de pedir, anotarlo con qué archivo | Queda como hallazgo del CA-02 |
| 5 | Repetir autorizando, y comparar | Ahora sí escribe: la diferencia es la autorización |

**Resultado esperado final:** avisar y **esperar** son dos cosas distintas, y el caso las separa.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la corrida de prueba escriba fuera de su carpeta (riesgo `R-02`) | Inmediato. Se detiene y se restaura |
| **Crítica** | Que el instalador escriba antes de pedir autorización | Inmediato. El CA-02 queda en «No» |
| **Alta** | Que no exista forma de ver el plan sin ejecutarlo | Se anota y se propone con su costo. Cambiar el instalador se aprueba aparte |
| **Media** | Que una vista previa anuncie algo distinto de lo que hace | Antes de cerrar: es peor que no tenerla |
| **Baja** | Que el CA-01 resulte cumplido y la fase parezca vacía (riesgo `R-01`) | Es un resultado: queda escrito qué muestra y cuándo |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Proyectos vivos instalados o actualizados | **0** |
| Archivos escritos fuera de la carpeta de destino | **0** |
| Archivos escritos antes de la autorización | **0** |
| Cambios hechos al instalador en esta fase | **0** — lo que falte se propone |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
