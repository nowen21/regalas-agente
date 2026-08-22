# Resultado de Pruebas — Fase A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Ejecución caso por caso

### CA-01 · El criterio existe y se puede citar

Existe, está escrito en una frase y tiene identificador. [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) dice:

> Al escribir la regla, responder **¿puede un script decir sí/no sin opinar?** y registrar la respuesta en `validadores/reglas-validables.md`.

Y el propio [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) lo enuncia de las dos formas, que es lo que lo vuelve usable:

> Si un script puede decir **sí/no sin opinar** → **validable**.
> Si dos personas pueden discutir si se cumplió → **se queda en el `.md`**.

**Se puede citar** porque tiene ID, y la decisión 5 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) fijó dónde vive cada cosa: `M9` enlaza, y el criterio con su detalle vive en `validadores/`, para no sacar a `M9` del molde de cuatro líneas.

**Resultado del criterio: Cumple.**

### CA-02 · Una regla que se discute queda afuera

El criterio no se quedó en teoría: se aplicó a las 175 reglas del cuerpo, una por una, y el resultado está contado:

| Categoría | Cuántas |
|---|---|
| Ya son validadores | ~54 |
| Validables, faltan | ~22 |
| **No validables, criterio humano** | **~99** |

**Noventa y nueve reglas quedaron afuera a propósito**, cada una con su motivo escrito. Ese es el CA-02 comprobado sobre el cuerpo entero, no sobre un ejemplo.

**Resultado del criterio: Cumple.**

### CA-03 · Una regla comprobable a medias se parte

El propio conteo lo muestra dentro de la categoría intermedia: de las 22 validables que faltan, cuatro se anotan como *fuzzy o pesadas* (`F2`, `F18`, `DOC7`, `DOC14`) y cinco necesitan que el proyecto declare algo antes de poder comprobarse.

O sea que el criterio **no obliga a elegir entre todo o nada**: una regla que solo se puede comprobar en parte queda con la parte comprobable identificada y la otra dicha. Es lo que el CA-03 pide.

**Y esta jornada dio un caso vivo:** la fase `A-EP-004-HU-013` declaró su CA-03 como criterio humano —comparar lo hecho con lo planeado exige leer los dos textos— mientras el resto de esa comprobación sí se automatizó. La regla se partió por donde el criterio manda.

**Resultado del criterio: Cumple.**

---

## 2. Verificaciones manuales

**Lo que el plan daba por cierto y no lo es.** Su línea base decía que el criterio *«no se puede citar porque no tiene identificador propio»* y que había que decidir si entraba al cuerpo de `M9`. Las dos cosas están resueltas: `M9` existe con su ID desde antes, y la decisión 5 del pendiente 59 fijó el reparto el 2026-08-18.

Es la quinta fase seguida de esta jornada cuyo plan afirma algo que hoy no se sostiene, y por el mismo motivo: se escribieron el 2026-08-17 y el repositorio cambió debajo.

---

## 3. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Baja | El plan daba el criterio por incitable | **Cerrado** al comprobarlo |
| D-02 | Media | El conteo de `reglas-validables.md` está escrito con `~` delante: «~54», «~22», «~99». Es una auditoría del 2026-08-05 que se ha ido tocando a mano, y **nadie comprueba que la suma cuadre con las reglas que hay** | **Abierto** |

---

## 4. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, el criterio existe y se puede citar | `20·M9` con su ID, y el enunciado en las dos direcciones | Cumple |
| CA-02, lo que se discute queda afuera | 99 reglas clasificadas como criterio humano, con su motivo | Cumple |
| CA-03, lo comprobable a medias se parte | Las cuatro *fuzzy* y las cinco que esperan declaración, más el caso de `A-EP-004-HU-013` | Cumple |

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios quedan verdes con el cuerpo entero como evidencia, no con un ejemplo. Lo que queda abierto es el D-02, que no es del criterio sino de su recuento.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El criterio como regla | [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) |
| EV-02 | El criterio aplicado y contado | [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) |
| EV-03 | Una regla partida de verdad | El CA-03 de `A-EP-004-HU-013`, declarado criterio humano |

---

## 7. Ciclos anteriores

Ninguno.
