# Funcionalidad implementada — Fase «A-EP-002-HU-006-quien-manda-sobre-la-version»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-002-HU-006-quien-manda-sobre-la-version` |
| **Épica / HU** | [EP-002](../../epica.md) · [HU-006](../HU-006-quien-sube-la-version.md) |
| **Versión** | 23.11.0 |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

**Lo compartido se lee un instante antes de escribirlo.** Es [`20·M18`](../../../../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md), y extiende a [`M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): `M10` ya pedía que el cambio, la entrada y la subida fueran juntos, y eso es cierto y no alcanzaba — **no decía cuándo se lee lo que se va a escribir**. Una sesión que sube `VERSION` a las once y guarda a las siete cumple `M10` al pie de la letra y deja el cruce igual.

Y la comprobación: [`validadores/numeracion.py`](../../../../../validadores/numeracion.py), dentro de `validar.py versionado`. Mira tres cosas —que `VERSION` no se haya quedado atrás de lo guardado, que tenga su entrada, y que el registro no repita un número— y avisa de los huecos.

---

## 2. La salida elegida, entre las tres que había

El [pendiente 22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) dejaba tres: subir la versión al guardar, escribir la entrada en un archivo aparte, o una sola sesión a la vez.

**Se eligió la primera** porque las otras dos cobran caro lo mismo: la segunda cambia la forma del registro para todos los proyectos que ya lo heredaron, y la tercera prohíbe trabajar con dos sesiones abiertas, que la propia HU declara normal y no negociable.

**Y no quedó acotada a `VERSION`.** Los cuatro casos del pendiente son el mismo defecto en archivos distintos —la versión, el registro, el número de un pendiente, un índice—, y así lo decidió el usuario en la duda 2 de la §2.7 del plan. Acotarla habría dejado fuera tres roturas que ya ocurrieron.

**De paso contesta lo que el pendiente daba por sin decidir:** cómo se entera una sesión de que otra está viva. Releyendo al escribir **no hace falta enterarse**.

---

## 3. Lo que la simulación enseñó

Dos copias, cada una con su archivo, las dos subiendo el mismo día. Con el número elegido al guardar: `9.1.0` y `9.2.0`, las dos entradas puestas, el trabajo de cada una intacto.

Con el número elegido al editar, las dos eligieron `9.1.0` — y al resolver el choque **se perdió una entrada del registro**, que es la `RN-04` de la HU.

**Eso destapó que el cruce se rompe de dos maneras, y la comprobación solo ve una:** el número repetido deja rastro, la entrada perdida no. Por eso la regla vale más que el validador — es lo único que actúa antes.

---

## 4. Lo que ya estaba roto, y se deja

El registro tiene **dos entradas para la `15.4.0`**, del 14 y del 15 de agosto. No se renumera: un proyecto pudo haber adoptado ese número, y cambiárselo le movería el piso sin que se entere. Queda **marcado en su propio título** y el validador lo reporta como aviso.

---

## 5. Lo que no hace

- **No cierra la ventana**, la reduce de horas a segundos. Dos sesiones que guardan en el mismo minuto siguen pudiendo chocar.
- **No ve la entrada perdida.** Solo el número repetido y el hueco.
- **No comprueba el hábito.** Que el número se haya elegido al guardar no queda en ningún archivo; lo que se comprueba es el resultado de no haberlo hecho.
