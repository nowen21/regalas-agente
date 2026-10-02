# -*- coding: utf-8 -*-
"""EP-023 · HU-005 · fase A: T-01, T-02, T-03 y T-09 sobre `base/01-conducta.md`.

T-01 crea `C30` debajo de `C14`; T-02 deroga `C14`; T-03 mueve `C25` debajo de
`C4` y la pone a extender `C4`; T-09 pone a `C15` a extender `C30`. Falla si
algún texto de partida no está tal cual.
"""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(RAIZ, "base", "01-conducta.md")

ANCLA_C14 = "#c14--lo-que-el-oficio-ya-da-por-sentado-se-aplica-sin-ofrecerlo-como-opción"
ANCLA_C14_NUEVA = ANCLA_C14 + "----derogada-en-4100--ver-01c30"
ANCLA_C30 = "#c30--no-agregues-lo-que-no-se-pidió"
F19 = "02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md"
CHECKLIST = "20-meta-reglas/checklist.md"


def una(texto, viejo, nuevo):
    assert texto.count(viejo) == 1, viejo[:70]
    return texto.replace(viejo, nuevo)


def bloque(texto, titulo, siguiente):
    i = texto.index("## " + titulo)
    j = texto.index("## " + siguiente, i)
    return texto[i:j]


SELLO = """### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](%s) contra **v41.0.0**, el **2026-10-02**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | %s |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: %s.**
""" % (CHECKLIST, "%s", "%s")

C30 = """## C30 · No agregues lo que no se pidió

Lo pedido es el criterio de aceptación más lo que exigen las reglas del estándar, y no se construye nada más. Lo que el oficio suele incluir y nadie pidió se pregunta en el análisis, y lo decide el usuario (deroga [`01·C14`](%s) · extiende [`02·F19`](%s)).

```
INCORRECTO: se pide la clase Matematicas con suma, y se entrega con suma,
            resta y división «porque una clase de matemáticas las trae»
CORRECTO:   se entrega la clase con suma; si la resta parece necesaria, se
            pregunta en el análisis
```

**Aplica a:** escribir-documento, cambiar-codigo

---

%s
**Fila 2 · se buscó por concepto y se leyó el capítulo entero.** [`C14`](%s) decía lo contrario y queda derogada por esta. [`02·F19`](%s) pide implementar literal el criterio, y [`02·F20`](02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) parar y proponer lo que aparezca fuera de él; ninguna dice qué es lo pedido ni dónde se decide lo que el oficio suele incluir.

**Fila 15 · sin ciclos:** `F19` no se apoya en esta.

**Fila 16 · N/A:** no tiene excepción.

**Fila 17 · los choques quedaron resueltos en el texto de las otras reglas.** [`00·ID1`](00-identidad-y-rol/reglas/ID1-trabaja-con-criterio-de-desarrollador-senior.md) pide el criterio del oficio dentro de lo pedido, y el ejemplo de `F19` dejó de prohibir lo que exige [`04·S1`](04-seguridad.md#s1--autorización-en-cada-acción-sensible).

**Fila 18 · no validable, y así queda registrada** en [validadores/reglas-validables.md](../validadores/reglas-validables.md): decidir si algo estaba pedido exige leer el criterio y las reglas.

Del [análisis 1](../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) (conclusiones 7 y 17) y el [análisis 6](../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-6.md) (conclusión 5) del pendiente «Lo que se construye se aparta de lo aprobado», fase `A` de la HU-005 de EP-023.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

""" % (ANCLA_C14_NUEVA, F19, SELLO % ("✅ ✅ N/A ✅", "19 ✅ · 0 ❌ · 1 N/A"), ANCLA_C14_NUEVA, F19)


def main():
    with open(RUTA, encoding="utf-8") as f:
        texto = f.read()

    # T-02 · C14 derogada, con su nota y su texto debajo.
    texto = una(texto,
        "## C14 · Lo que el oficio ya da por sentado se aplica sin ofrecerlo como opción\n\n",
        "## C14 · Lo que el oficio ya da por sentado se aplica sin ofrecerlo como opción  ·  "
        "`[DEROGADA en 41.0.0 → ver 01·C30]`\n\n"
        "> Dejó de regir: pedía construir de entrada lo que el oficio da por sentado, y con eso "
        "el agente agregaba lo que nadie pidió. Ahora lo que no se pidió no se agrega "
        "([`01·C30`](%s)). El texto original se conserva porque hay fases y análisis que la citan "
        "([`20·M11`](20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).\n\n" % ANCLA_C30)

    # T-01 · C30 debajo de C14.
    c25 = bloque(texto, "C25 · ", "C15 · ")
    texto = una(texto, c25, C30)

    # T-03 · C25 extiende a C4 y va debajo de ella, con su checklist sellado de nuevo.
    c25 = una(c25, "(extiende [`01·C14`](%s))" % ANCLA_C14, "(extiende [`01·C4`](#c4--no-decidas-por-tu-cuenta))")
    viejo = c25[c25.index("### Checklist"):c25.index("**Nace el 2026-08-18")]
    c25 = una(c25, viejo, SELLO % ("✅ ✅ N/A ✅", "19 ✅ · 0 ❌ · 1 N/A") + "\n")
    c25 = c25.replace(ANCLA_C14 + ")", ANCLA_C14_NUEVA + ")")
    c25 = una(c25, "> Vale mientras",
              "**Movida el 2026-10-02 debajo de `C4`.** Extendía a `C14`, que quedó derogada. Lo que pide, "
              "no decidir por cuenta propia lo que es del usuario, es el asunto de `C4`. Lo que exige no "
              "cambió. Fase `A` de la HU-005 de EP-023.\n\n> Vale mientras")
    c5 = texto.index("## C5 · ")
    texto = texto[:c5] + c25 + texto[c5:]

    # T-09 · C15 extiende a C30.
    texto = una(texto, "(extiende [`01·C14`](#c14--estándar-profesional-del-dominio))",
                "(extiende [`01·C30`](%s))" % ANCLA_C30)
    c15 = bloque(texto, "C15 · ", "C16 · ")
    viejo = c15[c15.index("### Checklist"):c15.index("**Corregida el 2026-08-22")]
    nuevo_c15 = una(c15, viejo, SELLO % ("✅ ✅ N/A ✅", "19 ✅ · 0 ❌ · 1 N/A") + "\n")
    nuevo_c15 = una(nuevo_c15, "> Vale mientras",
                    "**Cambió de dependencia el 2026-10-02.** Extendía a `C14`, que quedó derogada; ahora "
                    "extiende a `C30`. Lo que exige no cambió. Fase `A` de la HU-005 de EP-023.\n\n> Vale mientras")
    texto = una(texto, c15, nuevo_c15)

    # Las demás citas al ancla vieja de C14, dentro del capítulo.
    texto = texto.replace(ANCLA_C14 + ")", ANCLA_C14_NUEVA + ")")

    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


if __name__ == "__main__":
    main()
