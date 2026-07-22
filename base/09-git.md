# 09 · Control de versiones

> **Capa 2 · agnóstica al stack.** Cómo se usa el control de versiones. El mínimo innegociable está blindado en el núcleo (`00` · N2): las operaciones que escriben historia o publican (**commit**, **push**) solo se ejecutan bajo pedido explícito del usuario, y la autorización es de un solo uso. Aquí, cómo se hace bien cuando toca hacerlo.

---

## G1 · Commits atómicos y con un solo propósito

Un commit representa **un cambio coherente**: una funcionalidad, una corrección, un refactor. No mezclar cambios sin relación en el mismo commit (una corrección + un refactor + un ajuste de estilo → tres commits).

- Un commit debería poder revertirse solo sin arrastrar cosas ajenas.
- Evitar el commit gigante que toca medio proyecto y no se puede revisar.

```
INCORRECTO: un commit "varios cambios" con la feature, un bugfix y reformateo mezclados
CORRECTO:   un commit por la feature, otro por el bugfix, otro por el formateo
```

---

## G2 · Mensajes que explican el qué y el porqué

- Primera línea breve e imperativa que resume el cambio; si hace falta, un cuerpo que explica **por qué** se hizo (el qué ya está en el diff).
- En el idioma del proyecto (`01-conducta.md` C8).
- Registrar en el mensaje (o en la documentación) las **decisiones** que el diff no revela por sí solo.

```
INCORRECTO: "cambios", "fix", "wip"
CORRECTO:   "Corrige el cálculo de saldo cuando hay documentos anulados

            Los anulados se sumaban al total; ahora se excluyen en la consulta."
```

---

## G3 · Qué nunca se versiona

No entra al control de versiones:

- **Secretos** (claves, tokens, credenciales, archivos de entorno con valores reales) — blindado en `00` · N6.
- **Datos sensibles o personales**, ni bases de datos con datos reales.
- **Artefactos generados** (dependencias instaladas, compilados, cachés, logs).
- **Archivos locales de cada máquina/editor** (configuración personal del entorno).

Todo eso va al archivo de exclusión (`.gitignore` o equivalente). Se versiona una **plantilla de ejemplo** de la configuración, sin valores reales.

```
INCORRECTO: commitear el archivo de entorno con la clave de producción
CORRECTO:   ignorar el archivo real; versionar solo una plantilla sin secretos
```

---

## G4 · Trabajar en ramas, integrar limpio

- El trabajo va en una **rama** dedicada, no directo sobre la rama principal (salvo que el proyecto lo defina distinto en capa 3).
- Mantener la rama al día con la principal para reducir conflictos.
- La rama principal se mantiene en estado **funcional** (integrable): no se sube algo que la deja rota.

---

## G5 · No reescribir historia compartida ni forzar sin necesidad

- La reescritura de historia (rebase, enmienda, purga) y el **push forzado** son operaciones sensibles: solo sobre historia **no compartida**, o con acuerdo explícito cuando la historia ya es pública (puede afectar a otros que la clonaron).
- Cada una de estas operaciones requiere autorización explícita del usuario (núcleo `00` · N2), y la autorización no se extiende a la siguiente.
- Ante un obstáculo (hook fallido, conflicto), no se fuerza el paso con banderas destructivas (`--no-verify` y equivalentes) — blindado en `00` · N3.

```
INCORRECTO: el push es rechazado → el agente hace push --force por su cuenta
CORRECTO:   el agente reporta el rechazo, explica la causa y espera decisión del usuario
```

---

## Relación con el resto del estándar

- **Núcleo `00` · N2** — commit y push solo bajo pedido; autorización de un solo uso.
- **Núcleo `00` · N3/N6** — no forzar con banderas destructivas; no versionar secretos.
- **`11-configuracion-entornos.md`** — configuración fuera del código, plantilla de ejemplo versionada.
- **`13-documentacion.md`** — las decisiones importantes viven también en la documentación, no solo en el mensaje del commit.
