# 09 · Control de versiones  ·  `[CAPA 2]`

El mínimo está en [`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada): **commit** y **push** solo bajo pedido explícito, autorización de un solo uso. Aquí, cómo hacerlo bien cuando toca.

---

## G1 · Commits atómicos, un solo propósito

Un commit = un cambio coherente (una feature, un fix, un refactor). No mezcles cosas sin relación. Debe poder revertirse solo, sin arrastrar lo ajeno.

```
INCORRECTO: un commit "varios cambios" con feature + fix + reformateo
CORRECTO:   uno por la feature, otro por el fix, otro por el formateo
```

## G2 · Mensajes que explican qué y por qué

Primera línea breve e imperativa; si hace falta, un cuerpo con el **por qué** (el qué ya está en el diff). En el idioma del proyecto ([`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto)).

```
INCORRECTO: "cambios", "fix", "wip"
CORRECTO:   "Corrige el saldo cuando hay documentos anulados

            Se sumaban al total; ahora se excluyen en la consulta."
```

## G3 · Qué nunca se versiona

Al archivo de exclusión (`.gitignore`): **secretos** (claves, tokens, entorno real — [`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada)), **datos sensibles/reales**, **artefactos generados** (dependencias, compilados, cachés, logs), **config local** de máquina/editor. Se versiona una **plantilla de ejemplo** sin valores.

```
INCORRECTO: commitear el archivo de entorno con la clave de producción
CORRECTO:   ignorar el real; versionar solo la plantilla sin secretos
```

## G4 · Trabaja en ramas, integra limpio

El trabajo va en una **rama** dedicada (salvo que la capa 3 diga otra cosa). Mantenla al día con la principal. La rama principal queda siempre **funcional**.

## G5 · No reescribas historia compartida ni fuerces sin necesidad

Reescribir historia (rebase, enmienda, purga) y **push forzado** solo sobre historia no compartida, o con acuerdo explícito si ya es pública (afecta a quien la clonó). Cada una requiere autorización ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)). No fuerces con banderas destructivas ([`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).

```
INCORRECTO: rechazan el push → hago push --force por mi cuenta
CORRECTO:   reporto el rechazo, explico la causa y espero decisión
```

---

## G6 · Integración continua: el verde es automático, no manual

Las **pruebas y el linter** corren en un **pipeline reproducible** (CI), no dependen de que alguien se acuerde. La rama principal se protege: **no se integra algo que no está en verde**.

- El pipeline corre la suite y el linter en cada cambio propuesto (pull request / pre-merge); si algo falla, no se mergea.
- Los hooks locales (pre-commit) **complementan**, no reemplazan al CI. No se saltan ([`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
- Lo que el entorno de pruebas no cubre queda como verificación manual documentada ([`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar)).

```
INCORRECTO: "corré las pruebas antes de mergear" dependiendo de que el dev lo haga
CORRECTO:   el CI corre pruebas + lint automáticamente; el merge exige verde
```

---

## G7 · Todo commit se muestra al usuario y se aprueba antes de ejecutarlo

Antes de `git commit` (y del `push`), el agente **muestra al usuario el mensaje completo del commit y los archivos afectados**, y **espera aprobación explícita**. El usuario primero lee, luego aprueba; recién ahí se ejecuta.

Aceptar un cambio en los archivos **no** autoriza a commitearlo: son dos permisos distintos ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada) — autorización de un solo uso). No encadenar el commit en la misma acción que produjo el cambio.

```
INCORRECTO: hago el cambio y en el mismo paso hago commit/push · "ya que estaba, lo subí"
CORRECTO:   hago el cambio → muestro el mensaje + los archivos → espero "sube / aprobado" → recién ahí commit/push
```

---

## G8 · El mensaje es del proyecto, no de la herramienta

El historial cuenta **qué se decidió y por qué**, no con qué se escribió. Dos consecuencias:

**El cuerpo arranca con la idea del usuario, y después lo que hizo el agente.** El origen del cambio es la necesidad, no la ejecución. Quien lea el historial mañana busca el porqué, no el cómo.

**Nunca se firman los commits con la herramienta.** Sin `Co-Authored-By`, sin líneas de "generado con", sin marcas de agente. El autor del commit ya lo dice el propio git.

```
INCORRECTO: "Agrega validación de saldo

            Se implementó el chequeo en el servicio.

            Co-Authored-By: <herramienta>"

CORRECTO:   "Agrega validación de saldo

            El usuario reportó que se podían registrar pagos mayores al
            saldo pendiente. Se agrega el chequeo en el servicio y su prueba."
```

Comprobable: `validadores/validar.py commit` (regla [`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto) para el idioma).

---

Ver: `00` N2/N3/N6, `07` Q6 (lint), `08` (pruebas), `11` (config fuera del código), `13` (decisiones también en docs).
