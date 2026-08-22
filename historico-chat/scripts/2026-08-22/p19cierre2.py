# -*- coding: utf-8 -*-
import sys, os, re
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")

A = "base/17-interfaz.md"
s = L.leer(A)
ini, fin, _ = L.bloque(s, "I3")
b = s[ini:fin]
cl = b.find("### Checklist")

cuerpo = """La interfaz cumple el **mínimo de accesibilidad**, que es esta lista cerrada y se cumple entera, no a medias:

- Campos con **etiqueta** asociada; imágenes con texto alternativo.
- **Contraste** suficiente entre texto y fondo.
- Navegable por **teclado**, con el **foco visible**.
- Ninguna información transmitida **solo** por color.

> El nivel exigido (por ejemplo, un grado concreto de una norma de accesibilidad) y si es obligatorio por ley lo declara la capa 3, con el capítulo [`16`](16-cumplimiento-y-calidad.md).

```
INCORRECTO: la pantalla tiene etiquetas impecables y se entrega como accesible,
            con el texto en gris claro sobre blanco y el estado de cada fila
            indicado solo con un punto de color
CORRECTO:   los cuatro puntos de la lista, comprobados juntos antes de entregar
```"""

nota = """**Resuelta el 2026-08-22, con la salida que eligió el usuario (pendiente 19):** de las dos que el pendiente dejó escritas, **una regla que exige el mínimo con la lista como su contenido**, no cuatro reglas. Era la última de las 26 candidatas a partirse.

**Por qué la fila 9 pasa a ✅.** El sello traía dos lecturas opuestas escritas una debajo de la otra: la del 2026-08-07 decía «son cuatro exigencias y se cumplen por separado» y la del 2026-08-18 decía que son la definición de una sola. Con la decisión del usuario queda una: **el mínimo se cumple entero o no se cumple**, y el cuerpo ahora lo dice con esas palabras, en vez de dejarlo a la interpretación de quien lea la lista.

**Y gana el ejemplo que le faltaba** (fila 12, que estaba N/A): una pantalla con las etiquetas perfectas y el contraste ilegible es exactamente el caso que la regla rechaza."""

b = b[:b.find("\n")] + "\n\n" + cuerpo + "\n\n---\n\n" + b[cl:]
b = L.resellar(b, A, nota)
b = re.sub(r"\n\*\*Fila 9 · son cuatro exigencias.*?La nota sobre el nivel exigido[^\n]*\n", "\n", b, flags=re.S)
b = b.replace("| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ N/A ✅ |", "| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |")
b = b.replace("**20 filas: 16 ✅ · 0 ❌ · 4 N/A.**", "**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**")
L.escribir(A, s[:ini] + b + s[fin:])

# PR3 queda: se anota en su sello
P = "base/12-privacidad-datos.md"
s = L.leer(P)
ini, fin, _ = L.bloque(s, "PR3")
b = s[ini:fin]
marca = "Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md)."
extra = marca + """

**Confirmada el 2026-08-22: no se deroga.** El pendiente 19 la traía en la lista de derogaciones, y el usuario había dicho que sí; al ir a hacerlo se vio que ese sí venía del diagnóstico del 2026-08-14, cuando la regla era «un índice con forma de regla». Reescrita el 18, hoy exige lo que **ninguna otra dice**: que el dato personal es sensible **por defecto**, sin esperar a que el proyecto lo declare. Se le mostró al usuario y decidió que queda."""
assert marca in b
L.escribir(P, s[:ini] + b.replace(marca, extra, 1) + s[fin:])

# versión
assert L.leer("VERSION").strip() == "30.9.0"
L.escribir("VERSION", "30.9.1\n")
c = L.leer("CHANGELOG.md")
e = """## 30.9.1 — 2026-08-22

**PARCHE** (la regla de accesibilidad dice con palabras lo que su lista ya exigía, y gana ejemplo; nada cambia en lo que se pide).

**La accesibilidad mínima se cumple entera o no se cumple, y ahora la regla lo dice.** `17·I3` enumeraba cuatro cosas (etiquetas, contraste, teclado, color) sin decir si eran cuatro exigencias o una sola, y su sello traía las dos lecturas escritas una debajo de la otra. El usuario eligió: es una, con la lista como su contenido. También gana el ejemplo que le faltaba, una pantalla con las etiquetas perfectas y el contraste ilegible.

**Y `12·PR3` no se deroga.** Estaba en la lista de derogaciones del pendiente [19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), pero esa lista venía de cuando la regla no exigía nada propio; reescrita el 2026-08-18, hoy es la única que dice que un dato personal es sensible por defecto, sin esperar a que el proyecto lo declare. Se le mostró al usuario y decidió que queda. Con esto no queda ninguna de las 26 candidatas a partirse sin resolver.

"""
L.escribir("CHANGELOG.md", c.replace("## 30.9.0 — 2026-08-22", e + "## 30.9.0 — 2026-08-22", 1))

# señal
sn = L.leer("documentacion/senales.md")
sn = sn.rstrip() + """

## S-020 · Un sí dado sobre un diagnóstico viejo se vuelve a verificar contra el estado de hoy  ·  decisión · activa
- **What:** el pendiente 19 pedía cuatro decisiones y el usuario dijo que sí a las cuatro. Al ejecutarlas se encontró que el diagnóstico era del 2026-08-14 y el repositorio ya no era ese: 23 de las 26 particiones estaban hechas desde el 18, dos reglas se habían resuelto sin partirse, y `12·PR3`, que estaba en la lista de derogaciones por «no exigir nada propio», había sido reescrita y hoy exige lo que ninguna otra dice.
- **Why:** ejecutar el sí al pie de la letra habría borrado una exigencia viva (que el dato personal es sensible por defecto) y habría partido reglas ya partidas. La autorización era genuina; lo que había caducado era el diagnóstico sobre el que se dio.
- **Where:** [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), sección «Lo que queda, y es del usuario» · el sello de [`12·PR3`](../base/12-privacidad-datos.md).
- **Learned:** el trabajo de la ronda no fue partir sino **medir de nuevo antes de ejecutar**, y devolverle al usuario las dos que habían cambiado de sentido. Un pendiente con diagnóstico fechado se relee contra el estado actual antes de tocar nada, y lo que cambió se muestra en vez de ejecutarse.
- **When/Who:** 2026-08-22 · agente; las dos decisiones (`17·I3` como una regla, `12·PR3` queda) las tomó el usuario.
- **Scope:** estándar; aplica a cualquier proyecto donde un pendiente viejo se ejecute tal cual.
- **Rel:** S-018.
"""
L.escribir("documentacion/senales.md", sn)
print("ok")
