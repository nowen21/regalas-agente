# 09 · Control de versiones  ·  `[CAPA 2]`

El mínimo está en `00` · N2: **commit** y **push** solo bajo pedido explícito, autorización de un solo uso. Aquí, cómo hacerlo bien cuando toca.

---

## G1 · Commits atómicos, un solo propósito

Un commit = un cambio coherente (una feature, un fix, un refactor). No mezcles cosas sin relación. Debe poder revertirse solo, sin arrastrar lo ajeno.

```
INCORRECTO: un commit "varios cambios" con feature + fix + reformateo
CORRECTO:   uno por la feature, otro por el fix, otro por el formateo
```

## G2 · Mensajes que explican qué y por qué

Primera línea breve e imperativa; si hace falta, un cuerpo con el **por qué** (el qué ya está en el diff). En el idioma del proyecto (`01` · C8).

```
INCORRECTO: "cambios", "fix", "wip"
CORRECTO:   "Corrige el saldo cuando hay documentos anulados

            Se sumaban al total; ahora se excluyen en la consulta."
```

## G3 · Qué nunca se versiona

Al archivo de exclusión (`.gitignore`): **secretos** (claves, tokens, entorno real — `00` · N6), **datos sensibles/reales**, **artefactos generados** (dependencias, compilados, cachés, logs), **config local** de máquina/editor. Se versiona una **plantilla de ejemplo** sin valores.

```
INCORRECTO: commitear el archivo de entorno con la clave de producción
CORRECTO:   ignorar el real; versionar solo la plantilla sin secretos
```

## G4 · Trabaja en ramas, integra limpio

El trabajo va en una **rama** dedicada (salvo que la capa 3 diga otra cosa). Mantenla al día con la principal. La rama principal queda siempre **funcional**.

## G5 · No reescribas historia compartida ni fuerces sin necesidad

Reescribir historia (rebase, enmienda, purga) y **push forzado** solo sobre historia no compartida, o con acuerdo explícito si ya es pública (afecta a quien la clonó). Cada una requiere autorización (`00` · N2). No fuerces con banderas destructivas (`00` · N3).

```
INCORRECTO: rechazan el push → hago push --force por mi cuenta
CORRECTO:   reporto el rechazo, explico la causa y espero decisión
```

---

## G6 · Integración continua: el verde es automático, no manual

Las **pruebas y el linter** corren en un **pipeline reproducible** (CI), no dependen de que alguien se acuerde. La rama principal se protege: **no se integra algo que no está en verde**.

- El pipeline corre la suite y el linter en cada cambio propuesto (pull request / pre-merge); si algo falla, no se mergea.
- Los hooks locales (pre-commit) **complementan**, no reemplazan al CI. No se saltan (`00`·N3).
- Lo que el entorno de pruebas no cubre queda como verificación manual documentada (`08`·T4).

```
INCORRECTO: "corré las pruebas antes de mergear" dependiendo de que el dev lo haga
CORRECTO:   el CI corre pruebas + lint automáticamente; el merge exige verde
```

---

## G7 · Todo commit se muestra al usuario y se aprueba antes de ejecutarlo

Antes de `git commit` (y del `push`), el agente **muestra al usuario el mensaje completo del commit y los archivos afectados**, y **espera aprobación explícita**. El usuario primero lee, luego aprueba; recién ahí se ejecuta.

Aceptar un cambio en los archivos **no** autoriza a commitearlo: son dos permisos distintos (`00`·N2 — autorización de un solo uso). No encadenar el commit en la misma acción que produjo el cambio.

```
INCORRECTO: hago el cambio y en el mismo paso hago commit/push · "ya que estaba, lo subí"
CORRECTO:   hago el cambio → muestro el mensaje + los archivos → espero "sube / aprobado" → recién ahí commit/push
```

---

Ver: `00` N2/N3/N6, `07` Q6 (lint), `08` (pruebas), `11` (config fuera del código), `13` (decisiones también en docs).
