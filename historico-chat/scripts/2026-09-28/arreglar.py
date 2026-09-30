import io, sys

# Une las cadenas que quedaron partidas por un salto real: una línea de
# cadena abierta (número impar de comillas) se junta con la siguiente
# poniendo \n donde estaba el salto.
for p in sys.argv[1:]:
    lineas = io.open(p, encoding="utf-8").read().split("\n")
    salida, abierta = [], None
    for l in lineas:
        if abierta is not None:
            abierta += "\\n" + l
            if l.count('"') % 2 == 1:
                salida.append(abierta)
                abierta = None
            continue
        cuerpo = l.lstrip()
        if (cuerpo.startswith(('"', 'f"', '("', 'cabeza = ("'))
                or ' = ("' in l or '(f"' in l) and l.count('"') % 2 == 1 \
                and '"""' not in l:
            abierta = l
            continue
        salida.append(l)
    io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(salida))
