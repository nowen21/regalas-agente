# 09 · Control de versiones

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

Ver: `00` N2/N3/N6, `11` (config fuera del código), `13` (decisiones también en docs).
