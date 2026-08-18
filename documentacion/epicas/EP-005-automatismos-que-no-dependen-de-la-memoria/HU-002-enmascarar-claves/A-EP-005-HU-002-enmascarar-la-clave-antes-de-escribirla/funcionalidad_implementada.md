# Funcionalidad implementada — Fase «A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-002](../HU-002-enmascarar-claves.md) |
| **Versión** | sin cambio — no se toca `base/` ni `plantillas/` |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

**Una clave pegada en el chat ya no llega a la transcripción.**

| Se escribe | Queda |
|---|---|
| `la clave es AKIA1234567890ABCDEF, guardala` | `la clave es «enmascarado», guardala` |

Nace [`validadores/enmascarar.py`](../../../../../validadores/enmascarar.py), y [`historico.py`](../../../../../validadores/historico.py) lo llama **antes** de escribir — tanto el mensaje del usuario como la respuesta del agente.

---

## 2. Por qué antes de escribir y no después

**Era el daño con el que se abrió la fase**, y estaba medido: la fase `A-EP-005-HU-001` comprobó que una clave pegada en el chat quedaba en claro en la transcripción, **y la transcripción se versiona**.

Un enmascarado que corriera sobre el archivo ya escrito llegaría tarde: el valor estuvo en disco y, si hubo un guardado en medio, quedó en el historial para siempre. De ahí no se borra.

---

## 3. La mitad del trabajo fue no tapar de más

- **El molde no se tapa** —`tu-clave`, `changeme`, `<TU-CLAVE>`—: taparlo vuelve ilegible un ejemplo.
- **La línea que lee del entorno tampoco.** `password: os.environ["X"]` es **la forma correcta**; taparla enseñaría lo contrario de lo que el estándar pide.
- **Se tapa el valor, no la variable.** Quien lea la transcripción tiene que seguir entendiendo de qué se hablaba.
- **No se reescribe nada más:** ni el orden, ni los saltos de línea. Un enmascarado que reescribe de más deja de ser fiable como transcripción, que es lo único que ese archivo tiene que ser.

**Y se reconoce con lo que [`secretos.py`](../../../../../validadores/secretos.py) ya sabe**, no con una lista nueva. Duplicarla dejaría dos listas que se separan.

---

## 4. Las dos decisiones que traía el pendiente 59

- **La marca es `«enmascarado»`**, la misma que el estándar usa para el espacio por llenar. Se ve que hubo algo y se distingue del texto del mensaje.
- **Una clave en una transcripción vieja se enmascara igual, y el bloque no se borra.** Borrar pierde lo dicho.

---

## 5. Lo que no hace

- **No revisa las transcripciones ya escritas.** Hay 47 archivos de histórico y buscar en ellos es otro trabajo.
- **Solo cubre el histórico.** Un resumen, un pendiente o un plan escritos a mano pueden llevar una clave y nadie los mira. `04·S4` cubre el código, esto cubre la transcripción, y en medio queda todo lo demás que el agente escribe.
