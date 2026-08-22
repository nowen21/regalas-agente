# Plan de Pruebas — Fase A-EP-001-HU-008-retrodocumentar-la-derogacion   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-008 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-001-HU-008-retrodocumentar-la-derogacion` |
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
| Unitario sobre el cuerpo | Que cada derogación conserve su texto y que ningún identificador liberado vuelva | Lectura de `base/`, sin escribir | Sí — entran a `validadores/pruebas.py` |
| Revisión de marcas | Que la marca diga desde qué versión y por cuál se reemplaza, y que el reemplazo exista | Este repositorio | No |
| Corrida completa | Que la suite siga verde con las pruebas nuevas | Este repositorio | Sí |

**De dónde sale la lista de derogaciones.** De `version.derogaciones()`, leída del propio cuerpo. **No** de una lista escrita a mano dentro de la prueba: esa envejece con la primera derogación nueva y la prueba pasa a mentir.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | Identificadores con punto, como `F4.1`, que son los que dan falso positivo (riesgo `R-02`) |
| No regresión | ☑ | Las pruebas que ya existen, comparadas contra el número anotado **antes** de tocar nada |
| Documento | ☑ | La marca de cada derogación |

### 3.3 Técnicas de diseño de casos

- **Lista leída, no escrita** — arriba. Es lo que hace que la prueba siga sirviendo después de la novena derogación.
- **Línea base antes de tocar** — el riesgo `R-01`: se anota cuántas pruebas hay y cuántas pasan **antes** de agregar las nuevas. Sin ese número no se distingue lo propio de lo heredado si la suite aparece roja.
- **El formato que rompe, a propósito** — el CA-02 se prueba con `F4.1`, que lleva punto. Un caso que solo usara identificadores simples pasaría con una comprobación que ignora la mitad de las derogaciones.
- **Decir por qué camino se comprueba cada mitad** — el CA-03 lo cubre en parte [`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md), que corre, y en parte [`validadores/metareglas.py`](../../../../../validadores/metareglas.py), que no. Marcarlo cumplido porque el código lo contempla es el error que ya cerró un resultado falso.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera —las que ya están más las dos nuevas— y `validar.py estandar` como línea base.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | [CA-01](../HU-008-derogacion-sin-borrar.md#ca-01--una-regla-derogada-sigue-siendo-legible) | [CP-001](#cp-001--cada-derogación-conserva-su-archivo-y-su-cuerpo), [CP-002](#cp-002--la-marca-dice-desde-cuándo-y-por-cuál-y-el-reemplazo-existe) | Funcional | Alta | Parcial | ☐ |
| HU-008 | [CA-02](../HU-008-derogacion-sin-borrar.md#ca-02--un-identificador-liberado-no-se-reutiliza) | [CP-003](#cp-003--ningún-identificador-derogado-vuelve-como-regla-vigente), [CP-004](#cp-004--el-consecutivo-del-capítulo-no-toma-un-identificador-liberado) | Funcional — límites | Crítica | Parcial | ☐ |
| HU-008 | [CA-03](../HU-008-derogacion-sin-borrar.md#ca-03--una-regla-derogada-no-se-cuenta-como-incumplimiento) | [CP-005](#cp-005--la-derogada-no-entra-en-la-cuenta-de-incumplimientos) | Funcional | Alta | Parcial | ☐ |
| HU-008 | RNF — que la cuenta de derogaciones no se pierda | [CP-006](#cp-006--la-suite-queda-verde-y-con-su-número) | No regresión | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cada derogación conserva su archivo y su cuerpo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna: la prueba lee `base/` y no escribe |
| **Datos de entrada** | Lo que devuelva `version.derogaciones()` el día que se corra |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir la lista de derogaciones | Hay al menos una; si no, el caso falla acá y lo dice |
| 2 | Por cada una, comprobar que su archivo existe | Ninguno borrado |
| 3 | Por cada una, comprobar que conserva el cuerpo de la regla, no solo el aviso | El texto original sigue legible |

**Resultado esperado final:** derogar no borra, que es exactamente lo que [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) exige.

> **El paso 1 no es formalidad.** Sin él, el caso pasaría en silencio el día que la lista quedara vacía por un error de lectura.

---

### CP-002 — La marca dice desde cuándo y por cuál, y el reemplazo existe

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | La marca de cada derogación del cuerpo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la marca de cada una | Trae la versión y el identificador que la reemplaza |
| 2 | Comprobar que la versión existe en el [`CHANGELOG.md`](../../../../../CHANGELOG.md) | Cada una con su entrada |
| 3 | Comprobar que el identificador que nombra existe como regla vigente | Ninguno apunta al vacío |

**Resultado esperado final:** quien llegue a la regla vieja sale hacia la nueva sin preguntarle a nadie.

---

### CP-003 — Ningún identificador derogado vuelve como regla vigente

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los identificadores derogados y los vigentes del mismo capítulo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar los identificadores derogados | Queda la lista, leída del cuerpo |
| 2 | Tomar los vigentes de cada capítulo | Queda la lista |
| 3 | Cruzar las dos | Intersección vacía |
| 4 | Repetir el cruce incluyendo `F4.1`, que lleva punto | Se detecta igual: el formato con punto no lo saltea |

**Resultado esperado final:** un identificador liberado queda liberado para siempre ([`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).

> **El paso 4 es el que evita el falso verde.** Sin él, la prueba podría estar ignorando las derogaciones con punto y nadie lo notaría.

---

### CP-004 — El consecutivo del capítulo no toma un identificador liberado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-003 corrido |
| **Datos de entrada** | Un capítulo con al menos una derogación, y una regla candidata |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir el siguiente identificador libre del capítulo | Sale uno |
| 2 | Comprobar que no está entre los derogados | No lo está |
| 3 | Comprobar que es mayor que el último usado, derogado incluido | El consecutivo no retrocede |

**Resultado esperado final:** agregar una regla no reutiliza un número que ya tuvo dueño.

---

### CP-005 — La derogada no entra en la cuenta de incumplimientos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Una regla derogada sin checklist al día, y una vigente en la misma situación |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar las reglas sin checklist al día | Sale un número |
| 2 | Comprobar que ninguna derogada está en esa cuenta | Ninguna |
| 3 | Comprobar que la vigente en la misma situación **sí** está | Está: la diferencia es la derogación, no la falta de checklist |
| 4 | Anotar qué mitad la comprueba un programa que corre y cuál vive en uno sin punto de entrada | Queda dicho en el resultado |

**Resultado esperado final:** una regla jubilada no cuenta como deuda, y queda claro qué sostiene esa afirmación.

> **El paso 3 es el que da valor al 2.** Sin él, el caso pasaría también con una cuenta que devuelve cero siempre.

---

### CP-006 — La suite queda verde, y con su número

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / RNF |
| **Tipo** | No regresión |
| **Prioridad** | Media |
| **Precondiciones** | El número de pruebas anotado **antes** de tocar nada (riesgo `R-01`) |
| **Datos de entrada** | `validadores/pruebas.py` con las dos pruebas nuevas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar cuántas pruebas hay y cuántas pasan, antes de tocar | Queda la línea base con su número |
| 2 | Agregar las dos pruebas nuevas y correr la suite | Verde, y el conteo sube en dos |
| 3 | Comparar contra la línea base del paso 1 | Ninguna prueba que pasaba, falla |
| 4 | Comprobar que ninguna prueba nueva escribió en `base/` | `base/` sin cambios |

**Resultado esperado final:** lo nuevo se distingue de lo heredado porque hay contra qué compararlo.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un identificador derogado esté además en uso como regla vigente | Inmediato. El CA queda en «No» y se reporta |
| **Alta** | Que una derogación haya perdido el cuerpo de su regla | Inmediato — es lo que `M11` prohíbe |
| **Media** | Que la marca apunte a un identificador que no existe | Antes de cerrar |
| **Media** | Que aparezca una regla que debería estar derogada y no lo está (riesgo `R-04`) | Se propone. Derogar lo decide el usuario, no esta fase |
| **Baja** | Que la suite esté roja por algo ajeno | Se anota contra la línea base y se sigue |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 6 de 6 |
| Pruebas de la suite | Las de la línea base, más 2, todas en verde |
| Identificadores derogados reutilizados | **0** |
| Derogaciones sin marca completa | **0** |
| Listas de derogaciones escritas a mano dentro de una prueba | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
