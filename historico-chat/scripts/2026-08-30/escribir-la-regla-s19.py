# -*- coding: utf-8 -*-
"""Agrega la regla `04·S19` al final del capitulo de seguridad.

Se escribe como guion para que el texto de la regla quede en un solo sitio y no
se pegue a mano en un archivo de 600 lineas (`04·S18`).
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
R = os.path.join(RAIZ, "base", "04-seguridad.md")

REGLA = u"""

---

## S19 · En la memoria no se guarda un dato personal ni un secreto

Lo que queda escrito en la memoria del agente, sea recuerdo o señal, dice **qué se aprendió** y nunca el dato con el que se aprendió: ni nombres de personas, ni documentos, ni correos, ni claves. La memoria sobrevive a la sesión y se vuelve a leer sola, así que lo que entre ahí queda expuesto cada vez.

```
INCORRECTO: «Ana Gómez, cédula 1020…, no pudo entrar con la clave Patito2026»
            → el caso entero, con la persona y la credencial
CORRECTO:   «cuando la contraseña trae caracteres especiales, el archivo de
            configuración necesita comillas» → el aprendizaje, sin el caso
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v36.0.0**, el **2026-08-30**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 10 · el cuerpo mide 303 caracteres**, contados antes de escribirlo, para un molde de 320. La fila 17 es `N/A`: la regla no tiene excepción declarada.

**Nace el 2026-08-30 de que la exigencia no existía y una historia estaba en rojo por eso.** El criterio transversal de privacidad de [`EP-006·HU-001`](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-001-que-se-guarda-tipos-y-alcances/HU-001-que-se-guarda-tipos-y-alcances.md) pedía que la memoria no guardara datos personales ni claves, y al buscar la regla que lo dijera **no había ninguna**: [`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) dice qué se registra como señal y no dice qué no.

**Por qué va en seguridad y no en documentación.** No es una convención de cómo se escribe un documento: es qué dato puede salir de una sesión y quedar guardado. [`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada) ya prohíbe escribir una credencial en cualquier parte, y esta no la toca: agrega **el dato personal**, que el núcleo no cubre, y nombra el sitio donde el descuido se repite solo.

**Por qué el sitio importa.** Un dato en un registro se lee una vez y envejece. Un dato en la memoria **se carga al abrir cada sesión**: no envejece, se vuelve a decir. Por eso la exigencia no es «tener cuidado» sino que lo guardado sea el aprendizaje y no el caso.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
"""

with io.open(R, encoding="utf-8") as f:
    t = f.read()

if "## S19 ·" in t:
    print("S19 ya estaba: no se toca")
else:
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + REGLA)
    print("S19 agregada al capitulo 04")
