import io

p = r"C:\Ing. Jose\ia\agente\validadores\resumen.py"
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")

pares = [
('''# `- **Estado:** resuelto acá.` / `- **Estado:** abierto.`
_ESTADO = re.compile(r"^- \\*\\*Estado:\\*\\*\\s*(.+?)\\s*$", re.MULTILINE)''',
'''# `| Estado | abierto |`, la fila del molde desde la 39.5.0, o la viñeta
# `- **Estado:** abierto.` de los resúmenes anteriores, que no se reescriben.
# El molde pasó a tabla porque la viñeta llena es una marca de `00·ID8`
# (`EP-004·HU-012·CA-06`).
def _campo(nombre, vineta="- "):
    """El valor de un campo del resumen, en la fila de tabla o en la viñeta."""
    return re.compile(r"^(?:" + re.escape(vineta) + r"\\*\\*" + re.escape(nombre)
                      + r":\\*\\*|\\| " + re.escape(nombre) + r" \\|)\\s*(.+?)\\s*\\|?\\s*$",
                      re.MULTILINE)


_ESTADO = _campo("Estado")'''),
('''    m = re.search(r"^\\*\\*Viene de:\\*\\*\\s*(.+?)\\s*$", _leer(ruta), re.MULTILINE)''',
'''    m = _campo("Viene de", vineta="").search(_leer(ruta))'''),
('''            r = re.search(r"^- \\*\\*Con qu\\u00e9 se retoma:\\*\\*\\s*(.+?)\\s*$",
                          bloque[i + 1], re.MULTILINE)''',
'''            r = _campo("Con qu\\u00e9 se retoma").search(bloque[i + 1])'''),
('''            f"**Viene de:** \\u00ab...\\u00bb\\n\\n---\\n\\n"''',
'''            f"| Campo | Valor |\\n|---|---|\\n| Viene de | \\u00ab...\\u00bb |\\n\\n---\\n\\n"'''),
]
for v, n in pares:
    assert v in s, v[:60]
    s = s.replace(v, n, 1)
if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
