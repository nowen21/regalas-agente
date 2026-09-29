import io

p = r"C:\Ing. Jose\ia\agente\plantillas\sesion.md"
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")

pares = [
("**Viene de:** «AAAA-MM-DD · tema · H-N» / «—, es trabajo nuevo»",
 "| Campo | Valor |\n|---|---|\n| Viene de | «AAAA-MM-DD · tema · H-N» / «—, es trabajo nuevo» |"),
("| Qué lo soluciona | **EP-000, HU nueva: «título»**<br>",
 "| Qué lo soluciona | **EP-000 · HU nueva — «título»**<br>"),
("| Orden de resolución | «n de N, por qué va ahí» / «—» |",
 "| Orden de resolución | «n de N · por qué va ahí» / «—» |"),
("| Nace en | «AAAA-MM-DD, tema de la sesión» |",
 "| Nace en | «AAAA-MM-DD · tema de la sesión» |"),
("| Cerrado en | «AAAA-MM-DD, tema de la sesión» / «—» |",
 "| Cerrado en | «AAAA-MM-DD · tema de la sesión» / «—» |"),
("| Qué lo soluciona | **EP-000, HU nueva: «título»**<br>Como «rol»",
 "| Qué lo soluciona | **EP-000 · HU nueva — «título»**<br>Como «rol»"),
]
for v, n in pares:
    if v in s:
        s = s.replace(v, n)
if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
