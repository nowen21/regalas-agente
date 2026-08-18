# Resultado de Pruebas — Fase A-EP-005-HU-002: enmascarar la clave antes de escribirla

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos ejecutados

| Qué se comprobó | Veredicto |
|---|---|
| **CA-01** · una clave pegada en el chat no queda escrita en claro | ✅ **Pasa** |
| **CA-02** · el texto sigue siendo legible | ✅ **Pasa** |
| Se tapa **antes** de escribir, no después | ✅ **Pasa** |
| El molde y la lectura del entorno **no** se tapan | ✅ **Pasa** |
| No regresión | ✅ **Pasa** — `tests/` **208 · OK** · `pruebas.py` 357 · `estandar` limpio |

**11 casos automatizados** en [validadores/tests/test_la_clave_no_llega_al_historico.py](../../../../../validadores/tests/test_la_clave_no_llega_al_historico.py).

---

## 2. Qué quedó funcionando

**Una clave pegada en el chat ya no llega al archivo.** Se comprobó por el camino real —`historico.anotar_usuario`— y no llamando al enmascarado a mano:

| Se escribe | Queda |
|---|---|
| `la clave es AKIA1234567890ABCDEF, guardala` | `la clave es «enmascarado», guardala` |

**Se tapa antes de escribir, y esa es la decisión que importa.** Un enmascarado que corre sobre el archivo ya escrito llega tarde: el valor estuvo en disco y, si hubo un guardado en medio, quedó en el historial para siempre.

---

## 3. Las dos decisiones que venían del pendiente 59

- **Duda 29 · con qué marca se tapa:** `«enmascarado»`, la misma que el estándar ya usa para el espacio por llenar. No se inventa una marca nueva, se ve que hubo algo, y se distingue del texto que sí es del mensaje.
- **Duda 30 · qué se hace con una clave en una transcripción vieja:** se enmascara igual y queda dicho en el archivo. **El bloque no se borra** — borrar pierde lo dicho, que es lo que casi pasa hoy con el pendiente 29.

---

## 4. La mitad del trabajo fue no tapar de más

**El molde no se tapa** —`tu-clave`, `changeme`, `<TU-CLAVE>`—, porque taparlo vuelve ilegible un ejemplo.

**La línea que lee del entorno tampoco**, y ahí el motivo es más fuerte: `password: os.environ["X"]` es **la forma correcta**. Taparla enseñaría lo contrario de lo que el estándar pide.

**Y se reconoce con lo que `secretos.py` ya sabe**, no con una lista nueva: ocho formas de proveedor y el molde de la variable con pinta de clave. Duplicarlas dejaría dos listas que se separan con el tiempo.

---

## 5. Lo que queda abierto · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**Las transcripciones ya escritas no se revisaron.** La decisión de la duda 30 dice qué hacer cuando aparezca una; **buscarlas es otro trabajo**, y hay 47 archivos de histórico.

**Y el enmascarado solo cubre el histórico.** Un resumen, un pendiente o un plan escritos a mano pueden llevar una clave y nadie los mira. `04·S4` cubre el código; esto cubre la transcripción; en medio queda todo lo que el agente escribe.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **Defectos abiertos aceptados** | dos: las transcripciones viejas sin revisar, y lo que se escribe fuera del histórico |
| **Ciclos** | 1 |
