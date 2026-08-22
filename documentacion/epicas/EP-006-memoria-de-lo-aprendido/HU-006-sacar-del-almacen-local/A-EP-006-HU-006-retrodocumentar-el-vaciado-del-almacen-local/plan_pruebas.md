# Plan de Pruebas — Fase A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-006-HU-006 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Condición de arranque.** Las pruebas usan **almacenes de mentira**. El almacén real puede tener algo del usuario sin recoger todavía, y borrarlo sería perder un recuerdo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que después de recoger no quede ningún archivo en el almacén | Almacén de mentira | Sí |
| Puntero | Que no quede un archivo que apunte al del repositorio | Almacén de mentira | Sí |
| Observación | Qué hay hoy en el almacén de esta máquina | Este equipo, en lectura | No |

**Por qué el puntero merece su propia prueba.** Un puntero es **peor que nada**: parece que hay memoria donde no hay, y es el caso que el índice de la memoria nombra explícitamente.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Negativa | ☑ | El puntero puesto a mano tiene que salir también |
| Límites | ☑ | Almacén vacío, y almacén con archivos que no son recuerdos |
| Observación | ☑ | El estado real de esta máquina |

### 3.3 Técnicas de diseño de casos

- **El puntero se pone a propósito** — el caso no espera a que el programa lo deje: se pone uno a mano y se comprueba que el recogido lo saca.
- **Se observa, no se limpia** — el riesgo `R-01`: si el almacén de esta máquina tiene algo sin recoger, se **anota qué había** y se deja que el programa lo recoja. Vaciarlo a mano hace el trabajo del programa y borra la evidencia de si funcionaba.
- **Lo que no es recuerdo no se toca** — el caso de límites comprueba que el recogido no se lleve archivos que no le corresponden.
- **Almacenes de mentira siempre** — arriba, y cada caso verifica que el real no se tocó.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, sobre almacenes de mentira.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | [CA-01](../HU-006-sacar-del-almacen-local.md#ca-01--el-almacén-queda-vacío) | [CP-001](#cp-001--después-de-recoger-el-almacén-no-tiene-archivos), [CP-003](#cp-003--qué-hay-hoy-en-el-almacén-de-esta-máquina) | Funcional | Crítica | Parcial | ☐ |
| HU-006 | [CA-02](../HU-006-sacar-del-almacen-local.md#ca-02--no-queda-un-puntero-en-lugar-del-texto) | [CP-002](#cp-002--el-puntero-puesto-a-mano-también-se-saca) | Negativa | Crítica | Sí | ☐ |
| HU-006 | RNF — que no haya dos versiones del mismo recuerdo | [CP-002](#cp-002--el-puntero-puesto-a-mano-también-se-saca) | Negativa | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Después de recoger, el almacén no tiene archivos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Almacén **de mentira** en carpeta temporal |
| **Datos de entrada** | Varios recuerdos puestos en ese almacén |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner tres recuerdos en el almacén de mentira | Quedan los tres |
| 2 | Correr el recogido | Los tres llegan al repositorio de prueba |
| 3 | Mirar el almacén | Sin archivos |
| 4 | Correr con el almacén ya vacío | No falla, y no hace nada |
| 5 | Poner un archivo que **no** es recuerdo y correr | No se lo lleva: no le corresponde |
| 6 | Comprobar que el almacén real de la máquina no se tocó | Intacto |

**Resultado esperado final:** el almacén queda vacío de recuerdos, y solo de recuerdos.

---

### CP-002 — El puntero puesto a mano también se saca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 y RNF |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un archivo en el almacén que **apunta** al recuerdo del repositorio, en vez de traer su texto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner el puntero a mano en el almacén | Queda puesto |
| 2 | Correr el recogido | El puntero se saca |
| 3 | Comprobar que no quedó **ni el texto ni el puntero** | Ninguno |
| 4 | Comprobar que el recuerdo del repositorio sigue intacto | Intacto |
| 5 | Comprobar que no hay dos versiones del mismo recuerdo | Una sola |

**Resultado esperado final:** no queda una segunda versión del recuerdo en un sitio que nadie revisa ([`01·C19`](../../../../../base/01-conducta.md)).

> **Un puntero es peor que nada.** Hace creer que hay memoria donde no la hay, y nadie lo mantiene.

---

### CP-003 — Qué hay hoy en el almacén de esta máquina

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Observación |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna. **Solo lectura** |
| **Datos de entrada** | El almacén local de esta máquina |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mirar el almacén sin tocarlo | Se ve qué hay |
| 2 | Anotar qué había, con la fecha | Queda escrito |
| 3 | Si hay algo, **no** borrarlo a mano | Se deja que el programa lo recoja |
| 4 | Correr el recogido y volver a mirar | Se anota qué quedó |
| 5 | Si quedó algo, anotarlo como hallazgo del recogido | Queda propuesto |

**Resultado esperado final:** se sabe si el vaciado está funcionando de verdad en esta máquina, con evidencia.

> **El paso 3 conserva la evidencia.** Vaciarlo a mano haría el trabajo del programa y borraría el dato de si funcionaba.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la prueba borre algo del almacén real (riesgo `R-02`) | Inmediato. Se detiene: es un recuerdo del usuario |
| **Crítica** | Que quede un puntero después de recoger | Inmediato. El CA-02 queda en «No» |
| **Alta** | Que en el almacén de esta máquina haya algo sin recoger (riesgo `R-01`) | Se anota qué había y se propone; se deja que el programa lo recoja |
| **Media** | Que el recogido se lleve archivos que no son recuerdos | Antes de cerrar |
| **Baja** | Que otra sesión esté tocando `validadores/pruebas.py` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 3 de 3 |
| Recuerdos del almacén real borrados a mano | **0** |
| Punteros que sobreviven al recogido | **0** |
| Archivos que no son recuerdos llevados por error | **0** |
| Estado del almacén de esta máquina | Anotado, con su fecha |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
