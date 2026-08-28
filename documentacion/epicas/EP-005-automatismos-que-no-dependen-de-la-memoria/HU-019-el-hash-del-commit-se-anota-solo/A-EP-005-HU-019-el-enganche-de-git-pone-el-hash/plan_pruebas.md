# Plan de Pruebas — Fase `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-019](../HU-019-el-hash-del-commit-se-anota-solo.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el hash **se escribe solo** donde hay dónde, **y que no se escribe en ningún otro sitio**.

### 1.2 Alcance

**Entra:** el enganche, la lógica que decide dónde escribir, lo que el instalador cuelga, y el conteo con sus tres grupos.

**No entra:** rellenar las 106 sin fila, marcar las 22 pendientes, ni cambiar el ciclo.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | El reparto de las 140, y la duda que se resuelve midiendo |
| `S-066` | Que 106 de 140 no tienen dónde marcar |
| [pendiente 87](../../../../../pendientes/87-la-estacion-del-commit-casi-nunca-se-marca.md) | Las tres salidas, y cuál quedó fuera |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La decisión de dónde escribir | Que acierte, y sobre todo **que no escriba de más** |
| El enganche | Que **nunca** deshaga ni bloquee un commit |
| Lo que cuelga el instalador | Que el enganche exista en la lista |
| El conteo | Que separe los tres grupos y los nombre |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Con repositorios de git de verdad.** Un enganche de git no se puede comprobar sin commits reales: un árbol de archivos sin `.git` no dispara nada, y probar la función suelta dejaría sin comprobar justo lo que falla.

| Tipo | Por qué |
|---|---|
| **De que no pase** | Escribir en 106 documentos viejos es peor que no escribir en ninguno |
| **De no destruir** | Un enganche que rompe un commit se desinstala el mismo día |
| De partición | Con fila y sin fila; casilla vacía y con hash; cierre en git y sin |
| **De conexión** | Que esté colgado, no solo escrito |
| De sabotaje | Que las pruebas cacen lo que dicen cazar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-003 | Son **106 de 140**: escribir donde no hay estructura es el daño mayor |
| Crítica | CP-005 | Un commit perdido no se recupera con un aviso |
| Alta | CP-001, CP-002 | Que escriba, y que no pise |
| Media | CP-004, CP-006 | El conteo, y la conexión |

### 3.3 Alcance de la ejecución automatizada  ·  `02·F5`

`python validadores/pruebas.py` **entera**, con el conteo a la vista.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La `T-00` corrida:** saber si alguna prueba compara la lista de enganches de git.
- **La `T-01` resuelta:** qué pasa al escribir un archivo desde dentro de un enganche.
- La línea base y el reparto de las 140, en el plan §2.

### 4.2 Criterios de salida

- Los siete casos ejecutados.
- **El enganche probado commiteando de verdad.**
- Los tres grupos del conteo, **con sus nombres**.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **Se modifica un solo `estado-fase.md` sin fila.** Cero es cero.
- **Un commit se pierde, se deshace o se bloquea** por el enganche.
- **La `T-01` revela que escribir desde el enganche deja el repositorio en un estado raro** que no se puede explicar en una línea. Ahí se para y se replantea el diseño, no se sigue de largo.

**El tercero es el que más protege.** Un automatismo que hace algo inesperado con un commit **no se arregla después**: se descubre cuando ya pasó.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Previo · las pruebas del instalador | CP-000 | De impacto |
| CA-01 — el hash se escribe solo | CP-001 | De sistema |
| CA-02 — no se pisa un hash puesto | CP-002 | Que **no** pase |
| CA-03 — una fase sin la fila no se toca | CP-003 | Que **no** pase |
| CA-04 — el conteo separa los tres grupos | CP-004 | De sistema |
| CA-05 — un fallo no rompe el commit | CP-005 | **De no destruir** |
| CA-01 · conexión | CP-006 | De sistema |

---

## 6. Casos de prueba

### CP-000 — Las pruebas del instalador admiten un enganche más

| Campo | Valor |
|---|---|
| **Tipo** | De impacto · **Prioridad** Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar las pruebas que miran `.githooks/` | Se listan |
| 2 | Ver si alguna compara la lista completa o cuenta cuántos hay | **Ninguna debería** |
| 3 | Si alguna lo hace, **parar y decidir** | — |

---

### CP-001 — El hash se escribe solo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-01 · **Prioridad** Alta |
| **Precondiciones** | Un repositorio de git de verdad, con una fase y su fila vacía |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Commitear el documento de cierre de la fase | El commit se hace |
| 2 | Abrir el `estado-fase.md` | La casilla trae **el hash de ese commit** |
| 3 | Comparar con `git log` | Es el mismo, no otro |
| 4 | Comprobar que **nada más cambió** en el documento | Solo la casilla |

**El paso 3 no es adorno:** escribir *un* hash es fácil; escribir **el correcto** es lo que se pide.

---

### CP-002 — No se pisa un hash ya puesto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-02 · **Prioridad** Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner un hash cualquiera en la casilla | — |
| 2 | Commitear otra vez el cierre | El commit se hace |
| 3 | Abrir el documento | **El primer hash sigue ahí** |

**Por qué:** el hash dice **qué commit cerró la fase**. Reescribirlo con el último la haría apuntar a una corrección de una coma.

---

### CP-003 — Una fase sin la fila no se toca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-03 · **Prioridad** Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un `estado-fase.md` **sin tabla de estaciones** | — |
| 2 | Commitear su cierre | El commit se hace |
| 3 | Comparar el documento **byte por byte** | **Idéntico** |
| 4 | Un `estado-fase.md` con tabla pero **sin la fila 12** | Idéntico también |
| 5 | Sobre el árbol real: contar los que cambiarían | **Ninguno de los 106** |

**Es el caso que decide si sirve.** Son 106 de 140: un programa que les invente estructura **haría más daño que el problema que corrige**.

---

### CP-004 — El conteo separa los tres grupos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-04 · **Prioridad** Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación sobre el árbol real | Tres cuentas |
| 2 | Leerlas | «Cerradas de hecho», «sin commitear de verdad», «sin dónde marcar» |
| 3 | Sumarlas contra el total de fases | **Cuadran** |
| 4 | Comprobar que dice **cuáles**, no solo cuántas | Con nombres |

**Hoy el reparto es 22 · 1 · 106**, y juntarlos daría «23 fases sin commitear» donde hay una.

---

### CP-005 — Un fallo del enganche no rompe el commit

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-05 · **Tipo** De no destruir · **Prioridad** Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Romper el enganche a propósito | — |
| 2 | Commitear | **El commit queda hecho** |
| 3 | `git log` | Está |
| 4 | El árbol de trabajo | Sin cambios inesperados |
| 5 | El enganche escribiendo en un archivo de solo lectura | El commit sobrevive |

**Un commit perdido no se recupera con un aviso.** Por eso este caso es crítico aunque el enganche «solo escriba una línea».

---

### CP-006 — El enganche está colgado, no solo escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-019 / CA-01 · conexión · **Prioridad** Media |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el instalador sobre un repositorio de prueba | El enganche aparece en `.githooks/` |
| 2 | Comprobar que el instalador lo tiene en su lista | Sí, con una prueba que lo mire ahí |
| 3 | Commitear de verdad | El hash aparece **sin llamar a nada a mano** |

**Es la lección de `EP-002·HU-004`:** construido, probado, en verde, **y nadie lo llamaba**.

---

## 7. Datos y ambientes de prueba

**Repositorios de git de verdad**, creados y borrados por la prueba, con `user.name` y `user.email` **locales** — nunca globales (`00·N1`). **Ninguna prueba usa credenciales** (`00·N6`), y **no se commitea nada en el repositorio del estándar**.

---

## 8. Herramientas

`unittest`, `git` de verdad, y un guion de sabotaje que **se restaura con copia**, **restaura en `try/finally`**, limpia sus rastros, y **no se corre por una tubería** (`S-060`).

> **La guardia del guion acepta `OK` y `OK (…)`**, y sigue rechazando `OK:` — que es la línea de los validadores. Las dos formas del defecto ya pasaron el mismo día.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | Se pierde un commit, o se toca una fase sin fila |
| Alta | Se pisa un hash puesto, o se escribe el hash equivocado |
| Media | El conteo no separa los tres grupos |
| Baja | Redacción |

Se anota en el `resultado_pruebas.md`, se arregla, y **se vuelve a correr el caso completo**.

---

## 10. Cronograma

Un solo tramo, con la `T-00` y la `T-01` antes de escribir código, y la `T-08` al final. La suite completa después.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente construye y corre; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 7 de 7 |
| **Documentos sin fila que cambian** | **0 de 106** |
| **Commits perdidos o bloqueados** | **0** |
| Hashes pisados | 0 |
| El enganche colgado y probado commiteando | Sí |
| Sabotajes cazados | Todos |
| Fallas en la suite completa | 0, con conteo distinto de cero |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar la función suelta y no el enganche | Los casos usan **repositorios de git de verdad** |
| Que se pruebe que escribe y no que **no** escribe | `CP-003`, con comparación byte por byte |
| Que un fallo del enganche pase inadvertido | `CP-005` lo rompe a propósito |
| Que se pruebe llamándolo a mano y quede sin colgar | `CP-006` paso 3 commitea de verdad |
| Que un sabotaje pase en verde | Se corre el escenario y se mira el estado final — **pasó tres veces el mismo día** |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
