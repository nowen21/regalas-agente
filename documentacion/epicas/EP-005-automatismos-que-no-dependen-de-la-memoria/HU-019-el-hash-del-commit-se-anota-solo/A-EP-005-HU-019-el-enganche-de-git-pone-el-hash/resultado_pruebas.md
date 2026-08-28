# Resultado de Pruebas — Fase `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 3. **El primero no aplicó un sabotaje; el segundo lo dejó en verde** |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el hash se escribe solo y correcto, **no se toca ninguna de las 106 fases sin fila**, no se pisa un hash puesto, y **con el enganche roto el commit se hace igual**. Comprobado con repositorios de git de verdad.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 7 de 7 | 7 de 7 |
| **Documentos sin fila que cambian** | 0 de 106 | **0** |
| **Commits perdidos o bloqueados** | 0 | **0** |
| Hashes pisados | 0 | **0** |
| El enganche colgado y probado commiteando | Sí | **Sí** |
| Sabotajes cazados | Todos | **5 de 5**, tras dos ciclos |
| Fallas en la suite completa | 0 | 0, sobre **500 pruebas** |

---

## 3. Resultado por caso

### CP-000 — Las pruebas del instalador admiten un enganche más

Ninguna compara la lista completa ni cuenta cuántos hay. **El «15 archivos» que aparece en una explicación no es una comprobación**, y se verificó buscándolo.

### CP-001 — El hash se escribe solo

| Paso | Resultado |
|---|---|
| Commitear el cierre de una fase con su fila vacía | El commit se hace |
| La casilla | Trae el hash **del commit que se acaba de hacer** |
| Comparar con `git log` | **Es el mismo** |
| El resto del documento | Sin cambios |

**Comparar con `git log` no es adorno:** escribir *un* hash es fácil; escribir **el correcto** es lo que se pide.

### CP-002 — No se pisa un hash ya puesto

Con dos commits seguidos, el documento **conserva el primero** y no trae el segundo. El hash dice **qué commit cerró la fase**.

### CP-003 — Una fase sin la fila no se toca

| Qué se le puso delante | Qué hizo |
|---|---|
| Un `estado-fase.md` **sin tabla** | **Idéntico** |
| Con tabla pero **sin la fila 12** | Idéntico |
| Sobre el árbol real: los 106 | **Ninguno cambia** |

**Es el caso que decide si sirve.** Son 106 de 140.

### CP-004 — El conteo separa los tres grupos

```
22 fase(s) con su cierre escrito y la estación 12 sin marcar — es la marca, no el trabajo
 1 fase(s) sin cierre escrito y sin marcar — esto sí es trabajo
106 fase(s) sin la fila de la estación 12: no hay dónde marcar
```

**Con nombres**, y suman 129 sobre las 140 — las 11 restantes ya están marcadas.

Antes esto era **«23 fases sin commitear»**, donde hay **una**.

### CP-005 — Un fallo del enganche no rompe el commit

| Qué se rompió | Resultado |
|---|---|
| El guion de shell que lo llama | El commit se hace, y queda en el log |
| **`hook_estacion.py` sin `git` en el camino** | Termina en 0 y **sin decir nada** |

**El segundo se agregó después**, y el §4.2 dice por qué.

### CP-006 — El enganche está colgado

El instalador lo escribe en `.githooks/post-commit`, hay una prueba que lo comprueba **en su lista**, y al commitear el hash aparece **sin llamar a nada a mano**.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Cinco, restaurados **con copia** y en `try/finally`.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 | Ciclo 3 |
|---|---|---|---|---|
| 1 | Inventa la fila donde no hay tabla | Cazado (3) | Cazado | Cazado |
| 2 | Pisa el hash ya puesto | Cazado (2) | Cazado | Cazado |
| 3 | Marca aunque el cierre no esté en git | Cazado (1) | Cazado | Cazado |
| 4 | El enganche deja de callar y revienta | **No aplicó** | **Verde** | **Cazado (1)** |
| 5 | El instalador deja de colgarlo | Cazado (1) | Cazado | Cazado |

### 4.2 El sabotaje 4, en sus dos formas de fallar

**Ciclo 1: no se pudo aplicar.** El texto del sabotaje se escribió **sin los acentos** que el archivo tiene, así que no encontró nada y no rompió nada.

**Y el guion lo dijo:** *«NO SE PUDO SABOTEAR: el texto cambió»*. Sin esa línea, la salida habría sido idéntica a la de un sabotaje que las pruebas no detectan — **todo en verde** — y se habría leído como «cinco de cinco cazados». Es `S-068`.

**Ciclo 2: aplicado, y en verde.** La prueba que existía rompía **el guion de shell que llama al enganche**, no el enganche: su red de seguridad **nunca se tocaba**.

**El caso que sí la ejercita es real:** correr `hook_estacion.py` **sin `git` en el camino**, que es lo que pasa en una máquina que no lo tiene. Sin la red revienta con traza y código 1 **justo después de un commit correcto**. Con ella, termina en 0 y calla.

### 4.3 Un defecto que cazó una prueba escrita meses antes

Al correr la suite completa falló `test_todo_hallazgo_nombra_la_regla_que_se_incumple`: uno de los avisos nuevos **no nombraba la regla en la forma que el estándar exige**.

**La clase propia estaba en verde.** Lo encontró una prueba transversal, y es la tercera vez en la jornada que el estándar comprueba al agente.

### 4.4 Rastros

**Uno, declarado.** La copia de restauración del guion vive en la carpeta temporal, y **el enganche de la `HU-018` la avisa**.

**Y uno nuevo, que es el costo de esta fase:** después de cada commit **el árbol queda sucio** con el `estado-fase.md` recién marcado. Se decidió así, está en `S-067`, y el enganche lo dice en su salida.

### 4.5 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`). Los repositorios de prueba usan `user.name` y `user.email` **locales**, nunca globales (`00·N1`).

---

## 5. Defectos encontrados

| # | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | Un aviso nuevo no nombraba su regla en la forma exigida | Media | **Corregido.** Lo cazó una prueba transversal |
| DEF-02 | El texto del sabotaje 4 no coincidía: no se aplicó | Baja | **Corregido.** La guardia del guion lo dijo |
| DEF-03 | Ninguna prueba tocaba la red de seguridad del enganche | **Alta** — el sabotaje 4 pasó en verde | **Corregido** con el caso de «sin git» |
| DEF-04 | Una prueba usaba un atributo que su clase no tiene | Baja | **Corregido** |

**Ninguno en la lógica del código.** Y el `DEF-03` es la **cuarta** vez en la jornada que una prueba no toca lo que dice tocar.

---

## 6. Evidencias

- `validadores/estacion_commit.py` y `validadores/hook_estacion.py`
- El enganche `post-commit` en la lista del instalador
- **16 pruebas**, seis de ellas **con repositorios de git de verdad**
- La `T-01`, que resolvió la duda antes de escribir código
- La `T-08`, commiteando de verdad, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
