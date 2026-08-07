# 20 · Checklist de la regla — el instrumento

> **Qué es.** El estándar contra el que se comprueba **una** regla. Veinte filas: cada una nombra la meta-regla que la respalda y el criterio con el que aprueba. Al final, un resultado que dice **CUMPLE** o **NO CUMPLE**.
>
> **De dónde sale.** [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) fija el molde y [`M1`](base.md#m1--la-jerarquía-tiene-cuatro-niveles-y-un-solo-orden)–[`M13`](base.md#m13--lo-que-no-es-regla-del-estándar-tiene-su-propio-sitio) el resto de las exigencias. En [`base.md`](base.md) queda el resumen; el instrumento está solo aquí, para no tenerlo escrito en dos sitios ([`M2`](base.md#m2--un-tema-un-capítulo-un-dueño)).
>
> **Cuándo se aplica.** Al escribir la regla, en el **paso 9** del procedimiento de `base.md` — antes de versionar, no después. Y en cualquier auditoría posterior sobre reglas que no lo traigan aplicado o lo traigan anulado.
>
> **Dónde queda el resultado.** Dentro de la regla, no aquí. Ver §3.

---

## 1 · Las veinte filas

### A · Dónde va

| # | Qué se comprueba | Meta-regla | Aprueba si… |
|---|---|---|---|
| 1 | Es regla del estándar, no otra cosa | [`M13`](base.md#m13--lo-que-no-es-regla-del-estándar-tiene-su-propio-sitio) | su destino es `base/` y no `.agente/` del proyecto, `notas/`, `pendientes/`, el `CLAUDE.md` del repo ni la memoria |
| 2 | No existe ya | [`M12`](base.md#m12--antes-de-crear-una-regla-buscar--la-duplicación-es-el-defecto-más-caro) | se buscó **por concepto** en `base/` y se leyó entero el capítulo dueño; no basta con afinar una existente |
| 3 | La capa es la correcta | [`M1`](base.md#m1--la-jerarquía-tiene-cuatro-niveles-y-un-solo-orden) | capa 1 solo si es seguridad innegociable; `[BLINDADA]` no aparece fuera de capa 1 |
| 4 | El capítulo es el dueño del tema | [`M2`](base.md#m2--un-tema-un-capítulo-un-dueño) | ningún otro capítulo es dueño; si toca el tema de otro, lo **enlaza** en vez de repetirlo |

### B · Cómo se identifica

| # | Qué se comprueba | Meta-regla | Aprueba si… |
|---|---|---|---|
| 5 | No nombra tecnología ni nombre propio | [`M3`](base.md#m3--la-base-es-agnóstica-sin-stack-y-sin-dominio) | no aparece lenguaje, framework, motor, nube, sector, cliente, herramienta ni ruta de un proyecto real |
| 6 | El ID es `<PREFIJO><n>` | [`M4`](base.md#m4--cada-regla-tiene-un-identificador-único-estable-y-prefijado) | el prefijo es el del capítulo y está registrado en la tabla de letras ocupadas; `n` es el siguiente consecutivo libre y nunca uno reutilizado |

### C · Cómo está escrita

| # | Qué se comprueba | Meta-regla | Aprueba si… |
|---|---|---|---|
| 7 | Encabezado `##` | [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) | son dos gatitos. Con `###` la regla se esconde: no sale en el índice y el validador no la ve |
| 8 | El título manda y se sostiene solo | [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) | es imperativo y se entiende leyéndolo en un índice, sin abrir el cuerpo |
| 9 | Una sola exigencia | [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) | no hay "y además". **Prueba:** si las partes se pueden cumplir por separado, son dos reglas |
| 10 | Cuerpo de 1 a 4 líneas | [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) | cabe. Si no cabe: o son dos reglas, o se está contando el **porqué** (va a `notas/`), o toca abrir subcarpeta ([`M2`](base.md#m2--un-tema-un-capítulo-un-dueño)) |
| 11 | Sin texto prestado | [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) | lo que ya dice otra regla está **enlazado** (`ver 04·S4`), no copiado |
| 12 | Ejemplo INCORRECTO / CORRECTO | [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) | está, y el INCORRECTO es el error que se comete de verdad, no uno exagerado. **N/A** si la regla es evidente y no se puede malinterpretar |
| 13 | Marca de la lista cerrada | [`M5`](base.md#m5--toda-regla-se-escribe-en-el-mismo-formato) | lleva `[BLINDADA]`, `*opt-in*`, `[DEROGADA en X.Y.Z → ver ID]` o ninguna. Cualquier etiqueta inventada **reprueba** |

### D · Cómo se relaciona

| # | Qué se comprueba | Meta-regla | Aprueba si… |
|---|---|---|---|
| 14 | Dependencias en una de las tres formas | [`M7`](base.md#m7--las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres) | van en el cuerpo, entre paréntesis: `extiende ID` · `depende de ID` · `deroga ID`. **N/A** si no depende de ninguna |
| 15 | Sin ciclos y sin apuntar hacia arriba | [`M7`](base.md#m7--las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres) | ninguna dependencia vuelve sobre sí misma, y ninguna regla de capa 2 extiende ni deroga una `[BLINDADA]`. **N/A** con la 14 |
| 16 | Excepción completa | [`M8`](base.md#m8--la-excepción-se-escribe-dentro-de-la-regla-que-la-admite) | declara **condición**, **límite** y **quién autoriza**. Si la regla es `[BLINDADA]`, tener excepción **reprueba**. **N/A** si no tiene |
| 17 | No choca con ninguna regla vigente | [`M6`](base.md#m6--ante-un-conflicto-el-desempate-es-este-y-en-este-orden) | se releyó el capítulo entero y no hay choque; si lo hay, quedó resuelto **en el texto**, no dejado para el desempate |

### E · Qué obliga fuera de su propio texto

| # | Qué se comprueba | Meta-regla | Aprueba si… |
|---|---|---|---|
| 18 | Declarada validable o no | [`M9`](base.md#m9--toda-regla-declara-si-es-validable) | quedó registrada en `validadores/reglas-validables.md`, en la lista que le toque |
| 19 | Versionada | [`M10`](base.md#m10--todo-cambio-de-regla-se-versiona-y-se-registra) | hay entrada en `CHANGELOG.md` con su tipo (MAYOR · MENOR · PARCHE) y `VERSION` subió |
| 20 | Las citas resuelven | [`M4`](base.md#m4--cada-regla-tiene-un-identificador-único-estable-y-prefijado) | toda cita usa el formato `NN·ID` y todos los IDs citados existen |

---

## 2 · Cómo se decide el resultado

- **CUMPLE** — ninguna fila quedó en ❌.
- **NO CUMPLE** — **una sola ❌ basta**. La regla no se publica: se corrige o se retira. No existe "cumple parcial": una regla a medias es la que después nadie sabe si rige.
- **N/A** solo en las filas **12, 14, 15 y 16**, y siempre con el motivo escrito. Un `N/A` sin motivo cuenta como ❌.

---

## 3 · Cómo lo aplica cada regla

El resultado se escribe **dentro de la regla**, al final de su archivo, como sección `###`:

````markdown
### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](<ruta relativa a este archivo>) contra **vX.Y.Z**, el **AAAA-MM-DD**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 0 ❌ · 4 N/A.** N/A — <fila y motivo, una por una>.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
````

**Para qué va dentro de la regla.** Para que una auditoría posterior **no vuelva a analizar lo ya verificado**: la regla que trae su resultado `CUMPLE` contra la versión vigente se salta, y el trabajo se concentra en las que no lo traen o lo traen anulado. Sin eso, cada auditoría reevalúa el catálogo entero desde cero.

**Y el enlace a este archivo, para que la regla diga de dónde sale su evaluación.** El resultado sin el instrumento es una afirmación sin respaldo: quien abra la regla tiene que poder llegar en un clic a las veinte filas y a los criterios con que se juzgaron.

**El encabezado es `###`, no `##`.** Cuelga de la regla y no es una regla: con `##` un conteo de reglas lo contaría como una más.

**El resultado caduca solo.** Vale para el **texto que tenía la regla al aplicarlo**. Editar la regla lo anula — aunque el cambio parezca de redacción, porque las filas 8, 9, 10 y 11 se juzgan sobre ese texto. Volver a aplicarlo es parte de la edición, no un paso aparte ([`M10`](base.md#m10--todo-cambio-de-regla-se-versiona-y-se-registra)).

**El razonamiento largo no va en el resultado.** El resultado dice qué pasó cada fila y por qué las `N/A`. Una discusión de criterio que no cabe en una línea —un caso límite, una alternativa descartada— va a `notas/` ([`M13`](base.md#m13--lo-que-no-es-regla-del-estándar-tiene-su-propio-sitio)), enlazada desde la fila que la necesita.

---

## 4 · Lo que un script puede decidir solo

**Once de las veinte filas son mecánicas:** 5, 6, 7, 10, 12, 13, 14, 15, 18, 19, 20.

**Las nueve restantes piden leer y entender la regla:** 1, 2, 3, 4, 8, 9, 11, 16, 17.

Esa división es la especificación del validador de meta-reglas. Mientras las once no se comprueben solas, este checklist depende de que alguien se acuerde de responderlo — y [`M9`](base.md#m9--toda-regla-declara-si-es-validable) ya dice en qué termina eso: *una regla validable que nadie valida es una regla que no se cumple*.
