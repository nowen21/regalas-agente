import io

p = r"C:\Ing. Jose\ia\agente\adaptadores\claude-code\hook_md.py"
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")


def c(viejo, nuevo):
    global s
    assert viejo in s, viejo[:60]
    s = s.replace(viejo, nuevo, 1)


c("""  - si el archivo editado NO es un `.md` del proyecto -> no hace nada más;
  - si lo es -> comprueba enlaces e índices de ese proyecto.
""", """  - si el archivo editado NO es un `.md` del proyecto -> no hace nada más;
  - si lo es -> comprueba enlaces e índices de ese proyecto, y mide las
    marcas de redacción de **lo que se acaba de escribir** (`00·ID8`).

**Las marcas se miden en el momento de escribir** (`EP-004·HU-012·CA-05`).
Antes solo las contaba el `pre-commit`, cuando el documento ya se había
entregado. Se mide el texto escrito (`content` de `Write`, `new_string` de
`Edit`) y no el archivo entero: el archivo trae marcas viejas, y repetirlas
en cada edición es ruido que se deja de leer. Son aviso, no falla: le llegan
al agente por su contexto y no detienen nada.
""")
c("""  0 — todo bien (o no aplicaba).
  2 — hay fallas; Claude Code se lo devuelve al modelo para que las corrija.""",
  """  0 — todo bien, no aplicaba, o solo hay marcas: esas van por el contexto.
  2 — hay enlaces rotos; Claude Code se lo devuelve al modelo para que los
      corrija, y si hay marcas se nombran en el mismo mensaje.""")
c("import enlaces\n", "import enlaces\nimport marcas                                           # noqa: E402\n")
c("def es_md_de(ruta, raiz):", '''def texto_escrito(datos):
    """Lo que se acaba de escribir: el `content` de `Write`, o los `new_string`
    de `Edit` y de `MultiEdit`."""
    entrada = datos.get("tool_input") or {}
    if entrada.get("content") is not None:
        return entrada.get("content") or ""
    partes = [entrada.get("new_string") or ""]
    partes += [e.get("new_string") or "" for e in entrada.get("edits") or []]
    return "\\n".join(p for p in partes if p)


# Hasta cuántas marcas se nombran una por una. Más que eso tapa el aviso.
TOPE_MARCAS = 15


def aviso_de_marcas(ruta, texto):
    """El aviso de las marcas de lo recién escrito, o `""` si no hay."""
    halladas = marcas.medir_texto(texto)
    if not halladas:
        return ""
    lineas = [f"[REDACCIÓN: LO QUE SE ACABA DE ESCRIBIR TIENE {len(halladas)} "
              f"MARCA(S) DE `00·ID8`] {os.path.basename(ruta)}",
              "Corregirlas ahora, antes de entregar. La línea cuenta desde el "
              "comienzo de lo escrito."]
    for n, _clave, nombre, lugar in halladas[:TOPE_MARCAS]:
        lineas.append(f"  línea {n}: {nombre}; en su lugar, {lugar}")
    if len(halladas) > TOPE_MARCAS:
        lineas.append(f"  y {len(halladas) - TOPE_MARCAS} más")
    return "\\n".join(lineas)


def es_md_de(ruta, raiz):''')
c("""    hallazgos = enlaces.validar_enlaces(raiz) + enlaces.validar_indices(raiz)
    fallas = [h for h in hallazgos if h.severidad == FALLA]
    if not fallas:
        return 0

    print("La edición dejó enlaces rotos:", file=sys.stderr)
    for h in fallas:
        print(f"  {h}", file=sys.stderr)
    return 2""", """    try:
        aviso = aviso_de_marcas(editado, texto_escrito(datos))
    except Exception:       # noqa: BLE001 — medir no puede tumbar el enganche
        aviso = ""

    hallazgos = enlaces.validar_enlaces(raiz) + enlaces.validar_indices(raiz)
    fallas = [h for h in hallazgos if h.severidad == FALLA]
    if not fallas:
        if aviso:
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": aviso}}, ensure_ascii=False))
        return 0

    print("La edición dejó enlaces rotos:", file=sys.stderr)
    for h in fallas:
        print(f"  {h}", file=sys.stderr)
    if aviso:
        print(f"\\n{aviso}", file=sys.stderr)
    return 2""")

if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
