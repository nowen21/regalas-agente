import io

p = r"C:\Ing. Jose\ia\agente\plantillas\sesion.md"
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")

viejo1 = """- **Qué pasó:** «…»
- **Por qué importa:** «…»
- **Qué lo soluciona:**
  **EP-000 · HU nueva — «título»**
  - **Como** «rol»
  - **Quiero** «capacidad»
  - **Para** «beneficio»
  - **Contexto:** «qué hay hoy, qué falta y qué se rompe si no se hace».
- **Qué se decidió:** «…»
- **Estado:** «resuelto acá / abierto»
- **Responde a:** «EP-000 · HU-000 · CA-00» / «—»
- **Dispara:** «EP-000 · HU-000 nueva» / «numeradas, si son varias» / «—»
- **Orden de resolución:** «n de N · por qué va ahí» / «—»
- **Dónde queda:** «señal S-00 / pendiente NN / [`NN·Xn`](«ruta a la regla») / memoria»
- **Nace en:** «AAAA-MM-DD · tema de la sesión»
- **Cerrado en:** «AAAA-MM-DD · tema de la sesión» / «—»
- **Con qué se retoma:** «la pregunta que quedó viva» / «—»
"""
nuevo1 = """| Campo | Valor |
|---|---|
| Qué pasó | «…» |
| Por qué importa | «…» |
| Qué lo soluciona | **EP-000, HU nueva: «título»**<br>Como «rol»<br>Quiero «capacidad»<br>Para «beneficio»<br>Contexto: «qué hay hoy, qué falta y qué se rompe si no se hace» |
| Qué se decidió | «…» |
| Estado | «resuelto acá / abierto» |
| Responde a | «EP-000 · HU-000 · CA-00» / «—» |
| Dispara | «EP-000 · HU-000 nueva» / «numeradas, si son varias» / «—» |
| Orden de resolución | «n de N, por qué va ahí» / «—» |
| Dónde queda | «señal S-00 / pendiente NN / [`NN·Xn`](«ruta a la regla») / memoria» |
| Nace en | «AAAA-MM-DD, tema de la sesión» |
| Cerrado en | «AAAA-MM-DD, tema de la sesión» / «—» |
| Con qué se retoma | «la pregunta que quedó viva» / «—» |
"""
viejo2 = """- **Qué pasó:** «…»
- **Por qué importa:** «…»
- **Qué lo soluciona:** «una pieza por cada historia que dispara, con su narrativa y su contexto»
- **Qué se decidió:** «…»
- **Estado:** «…»
- **Responde a:** «…»
- **Dispara:** «…»
- **Orden de resolución:** «…»
- **Dónde queda:** «…»
- **Nace en:** «…»
- **Cerrado en:** «…»
- **Con qué se retoma:** «…»
"""
nuevo2 = """| Campo | Valor |
|---|---|
| Qué pasó | «…» |
| Por qué importa | «…» |
| Qué lo soluciona | «una pieza por cada historia que dispara, con su narrativa y su contexto, separada con `<br>`» |
| Qué se decidió | «…» |
| Estado | «…» |
| Responde a | «…» |
| Dispara | «…» |
| Orden de resolución | «…» |
| Dónde queda | «…» |
| Nace en | «…» |
| Cerrado en | «…» |
| Con qué se retoma | «…» |
"""
for v, n in ((viejo1, nuevo1), (viejo2, nuevo2)):
    assert v in s, v[:40]
    s = s.replace(v, n, 1)

if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
