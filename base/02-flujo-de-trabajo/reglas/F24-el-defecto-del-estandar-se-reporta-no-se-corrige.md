> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F24 · El defecto del estándar se reporta, no se corrige

Un proyecto que encuentra un defecto del estándar **no lo toca**: abre un pendiente allá nombrando el proyecto de origen, otro acá diciendo que espera esa corrección, y sigue con lo suyo. El de acá queda abierto hasta que llegue el aviso de que se corrigió (extiende [`02·F23`](F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

```
INCORRECTO: se parchea el estándar en la copia local del proyecto → los otros
            proyectos siguen con el defecto y nadie se entera
CORRECTO:   se reporta en el estándar, se anota acá el seguimiento, y el
            proyecto sigue con su trabajo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v23.7.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

La fila **4** puso el capítulo en duda: el defecto lo encuentra un proyecto y el canal se parece a la instalación, que es de `EP-007`. Pero **lo que la regla gobierna es un paso del flujo de trabajo** —qué hace el agente cuando lo que hay que arreglar no es suyo—, y eso es del `02`. La instalación es por dónde viaja el aviso, no de qué trata la regla.

La fila **9** es una sola exigencia con tres consecuencias que no se pueden cumplir sueltas: reportar sin anotar el seguimiento deja el pendiente del proyecto sin nacer, y anotar sin reportar deja al estándar sin enterarse. **Es lo que pasó los dos días seguidos que originaron esto**, cada día con una mitad.

La fila **16** es N/A: no tiene excepción. Que el proyecto pueda seguir trabajando lo suyo no es un caso exento — es la regla diciendo qué **sí** hacer.

La fila **17** resuelve un choque que estaba abierto y conviene dejarlo dicho: [`02·F20`](F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) manda parar y proponer lo que se descubre fuera del criterio de aceptación, y **no decía qué hacer cuando lo descubierto es del estándar y no del proyecto**. Ahí `F20` para y esta dice a dónde va lo que se propuso. Era el hueco anotado en el punto 8 del [pendiente 33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).

**Validable a medias, y la mitad que se puede ya corre:** `validar.py pendientes` comprueba que un pendiente que declara «Proyecto de origen» lo **nombre** de verdad, en vez de dejar la casilla vacía o con el marcador sin llenar.

Lo que **no** puede ver ningún programa de acá: si el pendiente del otro lado existe —vive en otro repositorio— ni si el aviso de vuelta llegó. Queda dicho para que nadie lo dé por cubierto.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
