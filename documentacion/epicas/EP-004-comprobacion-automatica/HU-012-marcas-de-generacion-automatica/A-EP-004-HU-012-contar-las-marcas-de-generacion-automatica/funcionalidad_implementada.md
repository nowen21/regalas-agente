# Funcionalidad implementada — Fase «A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-012](../HU-012-marcas-de-generacion-automatica.md) |
| **Versión del estándar** | sin cambio — no se toca `base/` ni `plantillas/` |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó funcionando

**El primer programa que mira si el estándar cumple `00·ID8`.** [`validadores/marcas.py`](../../../../../validadores/marcas.py) cuenta las marcas mecánicas del anexo [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md); `validar.py marcas` reporta las de `base/` y `plantillas/`, que es lo que viaja a los proyectos.

**Era el punto 1 del [pendiente 11](../../../../../pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md) —*contar antes de tocar*— y lo que lo tenía trabado.** El propio pendiente decía que hacer el recuento a mano sobre 200 archivos es lo que lo volvía inabordable.

| Fuera del histórico | **16 477** marcas en **820** archivos |
|---|---|
| Solo `base/` y `plantillas/` | **4 491** en 137 archivos |
| Con el histórico | **26 920** en 945 |

Las dos que pesan: **raya larga, 7 286** y **punto medio, 6 237**.

---

## 2. Dónde se puso la frontera, y por qué

**Solo se cuenta lo que se cuenta sin opinar.** El anexo tiene ocho secciones y la mayoría pide criterio: si la raya aparece «muy seguido», si el paralelismo es «perfecto», si el español «no es de acá». El propio anexo lo dice de las invisibles: *«son las únicas que un script cuenta sin equivocarse»*.

**Un programa que opinara de lo demás llenaría de ruido lo que hoy nadie mira**, y una salida sepultada se deja de leer. Está declarado, y con caso de prueba.

**Tres exclusiones, las tres con su motivo:**

| Qué | Por qué |
|---|---|
| Dentro de un bloque cercado o de comillas invertidas | Ahí la marca es el ejemplo de lo que no hay que hacer |
| El propio anexo y esta documentación | Un catálogo de marcas está lleno de marcas por definición |
| `historico-chat/` | Transcripción literal: no se reescribe, y mezclarlo convierte la deuda en algo que nunca baja. **Se cuenta aparte**, con `--historico` |

**Y una que no se hizo a propósito:** el punto medio de los títulos de este repositorio —`09 · Control de versiones`, `Fase A · …`— **sí se cuenta**. El anexo llama marca a *«adornar títulos»* con él. Si el estándar quiere conservar esa forma, **es una decisión que se escribe, no un descuento que el programa hace callando**.

---

## 3. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/marcas.py`](../../../../../validadores/marcas.py) | Nuevo: `contar`, `validar`, `marcas_de_linea` |
| [`validadores/validar.py`](../../../../../validadores/validar.py) | El subcomando `marcas` |
| [`validadores/tests/test_las_marcas_de_ia_se_cuentan.py`](../../../../../validadores/tests/test_las_marcas_de_ia_se_cuentan.py) | 19 casos |
| [`validadores/tests/test_ninguno_termina_en_silencio.py`](../../../../../validadores/tests/test_ninguno_termina_en_silencio.py) | `marcas.py` entra a los de arranque propio, con el motivo escrito |
| [`pendientes/11-…`](../../../../../pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md) | El recuento. **Sigue abierto**: contar no es limpiar |

---

## 4. La duda que detuvo la fase un día ya estaba contestada

La fase quedó en la estación 6 el 2026-08-17, esperando saber **si la comprobación aplica a todo el repositorio o solo a lo que se entrega**.

El pendiente 11 lo respondía desde el 2026-08-10, en su paso 3: *«No tocar el histórico»*; y el paso 2 daba el orden: primero `base/` y `plantillas/`.

> **Es el primer caso encontrado de [`01·C23`](../../../../../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar)**, la regla que se escribió ayer: lo ya decidido no se pregunta otra vez, y antes de pedir una decisión se busca si está escrita.

---

## 5. Lo que no hace

- **No limpia.** Contar era el paso 1; limpiar `base/` obliga además a **reaplicar el checklist a cada regla que se reescriba**, porque editar el texto anula su sello.
- **No separa lo viejo de lo nuevo**, y hace falta: [`02·F21`](../../../../../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) dice que desde que un incumplimiento queda registrado lo nuevo nace cumpliendo, y buena parte de esas 16 477 se escribieron después del 2026-08-10. **Si la deuda sigue creciendo, limpiarla sin más es rehacer el trabajo el mes que viene.**
- **No juzga la mitad del anexo que pide criterio**, y está dicho en vez de aproximado.
