# Funcionalidad implementada — Fase «B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-005](../HU-005-enlaces-y-citas.md) |
| **Versión del estándar** | sin cambio — no se toca `base/` ni `plantillas/` |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó funcionando

**El arreglo de `13·DOC14` lo hace el programa.** `enlaces.reparar_formato()` reescribe el **texto** de cada enlace para que diga la ruta desde la raíz; el destino no lo toca nunca.

**284 enlaces en 89 archivos**, y ningún enlace roto. El validador ya calculaba el texto correcto de cada uno desde hace días: lo que faltaba era escribirlo de vuelta.

**El que reporta y el que arregla comparten el criterio** (`_texto_esperado`). Si miran distinto, el arreglo deja hallazgos vivos o toca lo que nadie reportó — y hay dos casos que lo mantienen pegado.

---

## 2. Lo que se aplicó y se revirtió

**La primera corrida aplicó los 1031 y se revirtió entera.**

`DOC14` pide la ruta desde la raíz *«para saber dónde vive sin abrirlo»*. Para el archivo de **la misma carpeta** ese propósito ya está cumplido, y la regla no distingue el caso. Aplicada literal, nombrar al vecino costaba **132 caracteres de media** — y son **747 de los 1031**.

Se revirtieron los 347 archivos y quedaron solo los **284 de entre carpetas**, que son los que la regla resuelve de verdad.

> **Una regla puede tener razón en el caso para el que se escribió y volverse contraproducente en el que no se miró — y eso solo se ve aplicándola.** El validador llevaba días contando 1031 sin que nadie viera que tres de cada cuatro eran de otro tipo.

---

## 3. Lo que los casos encontraron antes de tocar nada

- **La exclusión de `prompts/` se contaba contra la raíz equivocada**, así que sobre un árbol de prueba escribía justo donde no debía. En el repositorio real las dos raíces coinciden: habría funcionado hasta el día que no.
- **El texto entre comillas invertidas nunca se ve.** `comun.enlaces()` borra esos trozos antes de buscar enlaces. No es de esta fase y quitarlo tocaría todo el repositorio; quedó **declarado en un caso**.

---

## 4. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/enlaces.py`](../../../../../validadores/enlaces.py) | `reparar_formato`, `_texto_esperado`, `_es_vecino`, `_es_del_usuario` |
| [`validadores/tests/test_el_texto_del_enlace_dice_donde_vive.py`](../../../../../validadores/tests/test_el_texto_del_enlace_dice_donde_vive.py) | 14 casos, la mitad de silencio |
| 89 `.md` del repositorio | Solo el **texto** de 284 enlaces |
| [`pendientes/18-…`](../../../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md) | Lo medido y la decisión que falta. **Sigue abierto** |

**Tres exclusiones, las tres declaradas y con caso propio:** las transcripciones del chat, `prompts/` —palabras del usuario— y el vecino de la misma carpeta.

---

## 5. Lo que no hace

- **No decide sobre el vecino.** 747 enlaces esperan a que se resuelva si `DOC14` lo exceptúa. La puerta queda abierta: `reparar_formato(incluir_vecinos=True)` los hace el día que se diga.
- **No ve el texto entre comillas invertidas**, y está dicho en un caso en vez de quedar como un número que no cuadra.
- **No mete el validador en la corrida diaria** — punto 3 del pendiente 18. Con 747 esperando decisión, hoy todavía sepultaría lo demás.
