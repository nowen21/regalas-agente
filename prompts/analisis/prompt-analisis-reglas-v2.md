# Prompt · análisis de las fichas de `prompts/` como candidatas a regla

Copia corregida de [prompt-analisis-reglas.md](prompt-analisis-reglas.md).

---

Analiza cada ficha de `prompts/` y determina qué se debe hacer con ella.

**Qué entra:** todos los `.md` de `prompts/`. **Qué no entra:** `README.md`, que es el índice, y esta carpeta `analisis/`.

**No excluyas ninguna ficha a mano.** Si su contenido ya está cubierto por una regla vigente, esa es una de las salidas del análisis y así queda registrado, citando el ID que la cubre. Excluirla de entrada esconde el dato más útil: cuánto de lo pedido ya está hecho.

## Antes de clasificar

1. **Lee el estándar de reglas:** [`base/20-meta-reglas/base.md`](../../base/20-meta-reglas/base.md), su [molde](../../base/20-meta-reglas/estructura-regla.md) y su [checklist](../../base/20-meta-reglas/checklist.md). Toda recomendación tiene que poder escribirse dentro de ese molde.
2. **Busca por concepto, no por palabra** (`20·M12`): el mismo criterio puede estar escrito con otro término. Revisa el capítulo dueño del tema completo, la memoria del agente y `pendientes/`.
3. **Enruta antes de decidir** (`20·M13`): no todo lo que pidió el usuario es regla del estándar. Puede ser instructivo del repositorio (`CLAUDE.md`), razonamiento (`notas/`), trabajo pendiente (`pendientes/`) o preferencia de trabajo (memoria del agente).

## Salidas posibles

Usa este vocabulario y ningún otro: es el que después se puede escribir. El orden es el de preferencia que manda `20·M12` — afinar sale más barato que crear.

| Salida | Qué significa en el estándar |
|---|---|
| **Ya está cubierta** | Una regla vigente ya lo exige. Se cita su ID y se explica dónde queda dicho. |
| **Afinar una regla existente** | Cambia la redacción o el ejemplo de una regla, sin cambiar qué exige. |
| **Complementar una regla** | Regla nueva que declara `(extiende NN·ID)`. La extendida sigue rigiendo igual (`20·M7`). |
| **Complementar varias reglas** | Regla nueva que declara más de una dependencia, cada una con su ID. Nunca en ciclo ni hacia una `[BLINDADA]` (`20·M7`). |
| **Regla nueva sin dependencia** | No hay dónde colgarla. Se justifica por qué ninguna existente la admite. |
| **Regla partida en hijas numeradas** | Solo cuando la regla padre no cabe en una página y hay que abrirle subcarpeta: `F12.1`, `F12.2` (`20·M2`). |
| **No es regla** | Se dice **a dónde va entonces**: `CLAUDE.md`, `notas/`, `pendientes/` o la memoria. |

**"Regla hija de varias" no existe en el estándar.** Lo que existe son las tres dependencias declarables: `extiende`, `depende de` y `deroga` (`20·M7`). Una regla puede declarar varias, pero sigue siendo una regla completa con su propio ID, su ejemplo y su checklist. La única jerarquía numerada es la de `20·M2`, y nace de que una regla crezca demasiado, no de que dependa de otras.

## Qué documentar de cada ficha

* Nombre de la ficha, con enlace.
* Qué exige, en una línea.
* Si ya está cubierta y por cuál regla.
* Salida recomendada, de la tabla de arriba.
* Regla o reglas relacionadas: nombre, ubicación y **enlace al sitio exacto** (`20·M15`).
* Justificación de la decisión.
* Si va a ser regla, además: capa (`20·M1`), capítulo dueño (`20·M2`), prefijo e ID libre (`20·M4`), si es agnóstica de stack y dominio (`20·M3`), si es validable por un script (`20·M9`) y qué tipo de versión implica (`20·M10`: MAYOR, MENOR o PARCHE).

## Choques entre fichas

Varias fichas se pisan entre sí. Dilo explícitamente: cuáles se solapan, cuál absorbe a cuál y cuál sobra. Dos reglas que dicen lo mismo con palabras distintas terminan contradiciéndose cuando una se actualiza y la otra no.

## Entregable

Un solo archivo: `prompts/analisis/prompts-2026-08-13-candidatas-a-regla.md`, junto al prompt que lo produjo.

1. **Tabla resumen**, una fila por ficha: ficha · salida · regla relacionada · tipo de versión.
2. **Detalle por ficha**, con los puntos de arriba.
3. **Tabla de cierre** (`13·DOC8`): en qué orden conviene ejecutarlas y de qué depende cada una.

Agrega su línea al índice de `prompts/analisis/README.md`.

## Límite

**No crees ni modifiques ninguna regla.** Nada de `base/`, `plantillas/`, `VERSION` ni `CHANGELOG.md`. Esta etapa entrega el mapa; qué se construye de él lo decide el usuario después.

---

## Qué cambió respecto de la versión anterior

| # | Cambio | Por qué |
|---|---|---|
| 1 | Se quita la exclusión a dedo de `sin-marcadores-de-ia` | No es la única ficha ya cubierta. "Ya está cubierta" pasa a ser una salida del análisis, y así se ve de una vez cuánto de lo pedido ya existe. |
| 2 | Se traducen las seis opciones al vocabulario del estándar | "Regla hija de varias" no se puede escribir: las relaciones declarables son tres (`20·M7`). Una recomendación que no se puede escribir no sirve. |
| 3 | Se agregan "ya está cubierta" y "afinar" como salidas | `20·M12` manda decidir en ese orden: afinar, extender, y solo entonces crear. La versión anterior ponía "crear nueva" de primera. |
| 4 | "No es regla" ahora exige decir a dónde va | Sin eso, lo descartado se pierde. `20·M13` ya tiene el destino para cada cosa. |
| 5 | Se pide capa, capítulo, ID, agnosticismo, validable y tipo de versión | Es lo que el procedimiento va a preguntar al escribir la regla. Sin eso, el mapa no alcanza para planear el trabajo. |
| 6 | Se exige enlace en cada cita, no solo el nombre | `20·M15`. |
| 7 | Se pide señalar los choques entre fichas | Varias se solapan entre sí. Si el análisis no lo dice, nacen reglas duplicadas. |
| 8 | Se agrega tabla resumen y tabla de cierre | La resumen deja ver el conjunto de un vistazo; la de cierre es lo que `13·DOC8` pide de todo análisis. |
| 9 | El entregable queda en `prompts/analisis/` | El análisis vive al lado de las fichas que analiza y del prompt que lo produjo. `analisis/` audita el estándar; esto audita el material que todavía no es estándar. |

---

## Cómo debe quedar el prompt

Esto es lo que se le pasa al agente, tal cual, sin nada de lo de arriba.

```
Analiza cada ficha de `prompts/` y determina qué se debe hacer con ella.

QUÉ ENTRA: todos los .md de `prompts/`. QUÉ NO ENTRA: `README.md`, que es el
índice, y la carpeta `analisis/`.

No excluyas ninguna ficha a mano. Si su contenido ya está cubierto por una regla
vigente, esa es una de las salidas del análisis y así queda registrado, citando
el ID que la cubre.

ANTES DE CLASIFICAR
1. Lee el estándar de reglas: base/20-meta-reglas/base.md, su molde
   (estructura-regla.md) y su checklist (checklist.md). Toda recomendación tiene
   que poder escribirse dentro de ese molde.
2. Busca por concepto y no por palabra (20·M12): el mismo criterio puede estar
   escrito con otro término. Revisa completo el capítulo dueño del tema, la
   memoria del agente y `pendientes/`.
3. Enruta antes de decidir (20·M13): no todo lo pedido es regla del estándar.
   Puede ser instructivo del repositorio (CLAUDE.md), razonamiento (notas/),
   trabajo pendiente (pendientes/) o preferencia de trabajo (memoria).

SALIDAS POSIBLES — usa este vocabulario y ningún otro, en este orden de
preferencia, que es el que manda 20·M12:
  · Ya está cubierta — una regla vigente ya lo exige. Se cita su ID.
  · Afinar una regla existente — cambia redacción o ejemplo, no qué exige.
  · Complementar una regla — regla nueva que declara (extiende NN·ID). La
    extendida sigue rigiendo igual (20·M7).
  · Complementar varias reglas — declara más de una dependencia, cada una con
    su ID. Nunca en ciclo ni hacia una [BLINDADA] (20·M7).
  · Regla nueva sin dependencia — no hay dónde colgarla, y se justifica.
  · Regla partida en hijas numeradas — solo si la regla padre no cabe en una
    página y hay que abrirle subcarpeta: F12.1, F12.2 (20·M2).
  · No es regla — se dice a dónde va: CLAUDE.md, notas/, pendientes/ o memoria.

"Regla hija de varias" no existe en el estándar. Lo que existe son las tres
dependencias declarables: extiende, depende de y deroga (20·M7). Una regla puede
declarar varias, pero sigue siendo una regla completa con su ID, su ejemplo y su
checklist. La única jerarquía numerada es la de 20·M2, y nace de que una regla
crezca demasiado, no de que dependa de otras.

DE CADA FICHA DOCUMENTA
  · Nombre de la ficha, con enlace.
  · Qué exige, en una línea.
  · Si ya está cubierta y por cuál regla.
  · Salida recomendada, de la lista de arriba.
  · Regla o reglas relacionadas: nombre, ubicación y enlace al sitio exacto
    (20·M15).
  · Justificación de la decisión.
  · Si va a ser regla, además: capa (20·M1), capítulo dueño (20·M2), prefijo e
    ID libre (20·M4), si es agnóstica de stack y dominio (20·M3), si es validable
    por un script (20·M9) y qué tipo de versión implica (20·M10: MAYOR, MENOR o
    PARCHE).

CHOQUES ENTRE FICHAS: varias se pisan entre sí. Dilo explícitamente — cuáles se
solapan, cuál absorbe a cuál y cuál sobra.

ENTREGABLE: un solo archivo, `prompts/analisis/prompts-2026-08-13-candidatas-a-regla.md`, junto al
prompt que lo produjo.
  1. Tabla resumen, una fila por ficha: ficha · salida · regla relacionada ·
     tipo de versión.
  2. Detalle por ficha, con los puntos de arriba.
  3. Tabla de cierre (13·DOC8): en qué orden conviene ejecutarlas y de qué
     depende cada una.
Agrega su línea al índice de `prompts/analisis/README.md`.

LÍMITE: no crees ni modifiques ninguna regla. Nada de base/, plantillas/,
VERSION ni CHANGELOG.md. Esta etapa entrega el mapa; qué se construye de él lo
decide el usuario después.
```
