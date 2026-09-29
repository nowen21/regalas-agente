import io

p = r"C:\Ing. Jose\ia\agente\plantillas\sesion.md"
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")

pares = [
("""Por eso cada pieza se escribe con las dos secciones que abren una historia de usuario:

```
**EP-000 · HU nueva — «título»**
- **Como** «rol»
- **Quiero** «capacidad»
- **Para** «beneficio»
- **Contexto:** qué hay hoy, qué falta y qué se rompe si no se hace.
```
""",
"""Por eso cada pieza se escribe con las dos secciones que abren una historia de usuario. Va dentro de la celda, con `<br>` entre renglones:

```
| Qué lo soluciona | **EP-000, HU nueva: «título»**<br>Como «rol»<br>Quiero «capacidad»<br>Para «beneficio»<br>Contexto: qué hay hoy, qué falta y qué se rompe si no se hace |
```

Los campos van en tabla y no en viñetas con el nombre en negrita: una viñeta así, llena, es una marca de [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/marcadores-de-ia.md), y la tabla no lo es.
"""),
("""```
**Dispara:**
1. EP-000 · HU-000 — «por qué va primero». No sale de este hallazgo: la bloquea.
2. EP-000 · HU-000 — «por qué va después de la anterior».
```""",
"""```
| Dispara | 1. EP-000 · HU-000: «por qué va primero». No sale de este hallazgo: la bloquea.<br>2. EP-000 · HU-000: «por qué va después de la anterior». |
```"""),
]
for v, n in pares:
    assert v in s, v[:50]
    s = s.replace(v, n, 1)
if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
